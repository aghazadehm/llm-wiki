#!/usr/bin/env python3
"""Validate the wiki against the structural rules in Agents.md.

Checks every article in ``wiki/**/*.md`` for:

* frontmatter: present, terminated, and carrying a valid ``type`` and ``status``
* frontmatter: ``tags`` present and drawn from the known vocabulary
* structure: one H1 with definition content beneath it, no empty sections
* structure: the required core sections present, in order, with ``Sources`` last
* links: every ``[[wikilink]]`` resolves, including its ``#heading`` anchor
* links: wikilinks point into ``wiki/`` (sources are cited, not linked)
* sources: at least one entry, and any cited local file exists under ``raw/``
* language: an article is written in the language its domain declares in Agents.md
* prose: a passage of one article that also appears in another is reported
* collection: no duplicate titles, no domain without an index, no orphan article

Usage::

    python tools/validate_wiki.py                 # validate ./wiki
    python tools/validate_wiki.py --root .        # explicit vault root
    python tools/validate_wiki.py --strict        # treat warnings as failures
    python tools/validate_wiki.py --json          # machine-readable report
    python tools/validate_wiki.py --self-test     # verify the rules themselves
    python tools/validate_wiki.py --all           # both of the above, in one command

Exit codes: ``0`` clean, ``1`` errors found (or warnings under ``--strict``),
``2`` the vault could not be read. Under ``--all`` a failure in either check
makes the whole run fail, so one command is enough to gate a commit.

The script uses the standard library only. It deliberately introduces no
package manager, lockfile, or runtime beyond Python 3, so the vault stays
independent of any particular toolchain, as Agents.md requires.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import unicodedata
from dataclasses import dataclass, field
from pathlib import Path
from typing import Callable, Iterable, Iterator, Sequence

# --- rule configuration -----------------------------------------------------

VALID_TYPES = ("concept", "comparison", "index")
VALID_STATUSES = ("draft", "reviewed", "archived")

#: Tag vocabulary. Extend only by decision, so tags stay meaningful filters.
KNOWN_TAGS = (
    "testing",
    "tdd",
    "test-doubles",
    "design",
    "refactoring",
    "architecture",
    "tooling",
    "process",
    "llm",
    "prompting",
    "rag",
    "agents",
    "fine-tuning",
    "evaluation",
    "security",
)

#: Language each domain's articles are written in. Mirrors the table in
#: Agents.md, which is the authority: a domain absent here is English, and
#: declaring a domain non-English is a decision recorded in both places.
DOMAIN_LANGUAGES = {
    "llm": "fa",
}

#: An English article tolerates this share of non-Latin letters before the
#: language rule fires, which leaves room for a quoted term or a proper name.
LANGUAGE_MAX_NON_LATIN_SHARE = 0.10

#: A non-English article must be at least half non-Latin to count as written
#: in its declared language. Every known article sits far outside both bounds,
#: so the check separates practice rather than splitting hairs.
LANGUAGE_MIN_NON_LATIN_SHARE = 0.50

#: Unicode scripts that make an article non-Latin. Naming the scripts keeps the
#: check script-based rather than tied to one language.
NON_LATIN_SCRIPTS = frozenset(
    {
        "ARABIC",
        "HEBREW",
        "CYRILLIC",
        "GREEK",
        "CJK",
        "HIRAGANA",
        "KATAKANA",
        "HANGUL",
        "THAI",
        "DEVANAGARI",
    }
)

#: Core headings every article must carry, in this order. ``type: index``
#: articles are entry points, so they are exempt and checked separately.
REQUIRED_SECTIONS = ("Related Concepts", "My Understanding", "Sources")

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
WIKILINK_RE = re.compile(r"\[\[([^\[\]]+?)\]\]")
BACKTICK_RE = re.compile(r"`([^`\n]+)`")
RAW_PATH_RE = re.compile(r"raw/[^\s`)\]|,]+\.(?:pdf|md|txt)")
CURLY_QUOTE_RE = re.compile(r"[\u2018\u2019\u201c\u201d]")
LIST_ITEM_RE = re.compile(r"^\s*[-*]\s+\S")
FENCE_RE = re.compile(r"^(```|~~~)")
TABLE_ROW_RE = re.compile(r"^\s*\|")

#: Every rule id this validator can emit. ``--self-test`` asserts that each one
#: is exercised by at least one fixture, so rule coverage cannot silently rot.
ALL_RULES = frozenset(
    {
        "frontmatter.missing",
        "frontmatter.unterminated",
        "frontmatter.type",
        "frontmatter.status",
        "frontmatter.tags",
        "frontmatter.tags_unknown",
        "structure.h1",
        "structure.definition",
        "structure.empty_section",
        "structure.required_section",
        "structure.section_order",
        "structure.sources_last",
        "structure.index_links",
        "sources.empty",
        "sources.local_file",
        "link.unresolved",
        "link.anchor",
        "link.outside_wiki",
        "link.pipe_in_table",
        "style.curly_quotes",
        "style.language",
        "collection.duplicate_prose",
        "collection.duplicate_title",
        "collection.no_index",
        "collection.index_missing",
        "collection.orphan",
    }
)


# --- model ------------------------------------------------------------------


@dataclass
class Finding:
    """One rule violation, positioned for editor navigation."""

    path: str
    line: int
    severity: str
    rule: str
    message: str

    def format(self) -> str:
        return f"{self.path}:{self.line}: {self.severity}: {self.message} [{self.rule}]"

    @property
    def sort_key(self) -> tuple:
        return (self.path, self.line, self.rule)


@dataclass
class Heading:
    level: int
    text: str
    line: int
    content: list[tuple[int, str]] = field(default_factory=list)

    def has_content(self) -> bool:
        return any(text.strip() for _, text in self.content)


@dataclass
class Doc:
    path: str
    lines: list[str]
    meta: dict
    fm_error: str | None
    fm_end: int
    headings: list[Heading]
    intro: list[tuple[int, str]]

    @property
    def doc_type(self) -> str:
        value = self.meta.get("type", "")
        return value if isinstance(value, str) else ""

    @property
    def status(self) -> str:
        value = self.meta.get("status", "")
        return value if isinstance(value, str) else ""

    @property
    def tags(self) -> list:
        value = self.meta.get("tags", [])
        if isinstance(value, str) and value:
            return [value]
        if isinstance(value, list):
            return [str(v) for v in value]
        return []


# --- frontmatter parsing (subset of YAML, no dependency) --------------------


def _scalar(raw: str) -> str:
    value = raw.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        value = value[1:-1]
    return value


def _parse_value(raw: str):
    value = raw.strip()
    if not value:
        return []  # a block list may follow on indented lines
    if value.startswith("[") and value.endswith("]"):
        inner = value[1:-1].strip()
        return [_scalar(part) for part in inner.split(",") if part.strip()] if inner else []
    return _scalar(value)


def parse_frontmatter(lines: Sequence[str]) -> tuple[dict, str | None, int]:
    """Return (metadata, error, index of the first body line)."""
    if not lines or lines[0].strip() != "---":
        return {}, "missing frontmatter (an article must open with a '---' block)", 0
    for index in range(1, len(lines)):
        if lines[index].strip() == "---":
            return _parse_meta(lines[1:index]), None, index + 1
    return {}, "unterminated frontmatter (no closing '---')", 0


def _parse_meta(block: Sequence[str]) -> dict:
    meta: dict = {}
    key: str | None = None
    for raw in block:
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        stripped = raw.lstrip()
        if stripped.startswith("- ") and key is not None and isinstance(meta.get(key), list):
            meta[key].append(_scalar(stripped[2:]))
            continue
        if ":" in raw:
            key, _, value = raw.partition(":")
            key = key.strip()
            meta[key] = _parse_value(value)
    return meta


# --- structure scanning -----------------------------------------------------


def scan_structure(lines: Sequence[str], start: int) -> tuple[list[Heading], list]:
    """Collect headings (with their own content) and any pre-heading text."""
    headings: list[Heading] = []
    stack: list[Heading] = []
    intro: list[tuple[int, str]] = []
    fence: str | None = None

    for index in range(start, len(lines)):
        raw = lines[index]
        stripped = raw.strip()
        if fence is None and FENCE_RE.match(stripped):
            fence = stripped[:3]
            _add_content(intro, stack, index + 1, raw)
            continue
        if fence is not None:
            _add_content(intro, stack, index + 1, raw)
            if stripped.startswith(fence):
                fence = None
            continue
        match = HEADING_RE.match(raw)
        if match:
            heading = Heading(
                level=len(match.group(1)),
                text=match.group(2).strip().strip("#").strip(),
                line=index + 1,
            )
            while stack and stack[-1].level >= heading.level:
                stack.pop()
            stack.append(heading)
            headings.append(heading)
            continue
        _add_content(intro, stack, index + 1, raw)

    return headings, intro


def _add_content(intro: list, stack: list[Heading], line: int, raw: str) -> None:
    if stack:
        stack[-1].content.append((line, raw))
    else:
        intro.append((line, raw))


def parse_doc(path: str, text: str) -> Doc:
    lines = text.split("\n")
    meta, fm_error, start = parse_frontmatter(lines)
    headings, intro = scan_structure(lines, start)
    return Doc(path, lines, meta, fm_error, start, headings, intro)


def iter_body_lines(doc: Doc) -> Iterator[tuple[int, str]]:
    """Yield (line number, text) for prose, skipping frontmatter and code fences."""
    fence: str | None = None
    for index in range(doc.fm_end, len(doc.lines)):
        raw = doc.lines[index]
        stripped = raw.strip()
        if fence is None and FENCE_RE.match(stripped):
            fence = stripped[:3]
            continue
        if fence is not None:
            if stripped.startswith(fence):
                fence = None
            continue
        yield index + 1, raw


def _domain_of(path: str) -> str:
    """The domain folder an article lives in, read from its vault path."""
    parts = path.replace("\\", "/").split("/")
    return parts[-2] if len(parts) >= 2 else ""


def _prose_text(doc: Doc) -> str:
    """Article prose, with code removed so that code never sets the language."""
    return "\n".join(BACKTICK_RE.sub(" ", text) for _, text in iter_body_lines(doc))


def _non_latin_share(text: str) -> float | None:
    """Share of letters outside the Latin script, or ``None`` if unlettered.

    Counting letters by Unicode script rather than by language keeps this free
    of a language database, which the standard library does not carry.
    """
    latin = other = 0
    for character in text:
        if not character.isalpha():
            continue
        name = unicodedata.name(character, "")
        if name.startswith("LATIN"):
            latin += 1
        elif name.split(" ", 1)[0] in NON_LATIN_SCRIPTS:
            other += 1
    total = latin + other
    return None if total == 0 else other / total


def _normalise(text: str) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^\w\s-]", "", text)
    return re.sub(r"\s+", " ", text).strip()


def _subtree_has_content(headings: Sequence[Heading], index: int) -> bool:
    """True when a heading holds text of its own or in any descendant section."""
    if headings[index].has_content():
        return True
    level = headings[index].level
    for child in headings[index + 1 :]:
        if child.level <= level:
            break
        if child.has_content():
            return True
    return False


#: Headings that legitimately carry an article's opening definition.
_DEFINITION_HEADINGS = ("definition", "purpose", "overview", "introduction")


def _has_definition(headings: Sequence[Heading], index: int) -> bool:
    """A lead paragraph beneath the H1, or an explicit definition section."""
    if headings[index].has_content():
        return True
    level = headings[index].level
    for position in range(index + 1, len(headings)):
        child = headings[position]
        if child.level <= level:
            break
        if _normalise(child.text) in _DEFINITION_HEADINGS:
            return _subtree_has_content(headings, position)
        break
    return False


def find_section(headings: Sequence[Heading], name: str) -> Heading | None:
    for heading in headings:
        if _normalise(heading.text) == _normalise(name):
            return heading
    return None


def _section_lines(doc: Doc, name: str) -> set[int]:
    """Body lines of a section and its subsections, so one can be skipped."""
    for index, heading in enumerate(doc.headings):
        if _normalise(heading.text) != _normalise(name):
            continue
        lines = {line for line, _ in heading.content}
        for child in doc.headings[index + 1 :]:
            if child.level <= heading.level:
                break
            lines.update(line for line, _ in child.content)
        return lines
    return set()


# --- repeated prose ---------------------------------------------------------

#: A sentence shorter than this is not evidence of duplication. Short bullets,
#: section lead-ins and one-line definitions recur legitimately, and a check
#: that flagged them would be noise rather than a gate.
DUPLICATE_MIN_WORDS = 8

_MARKDOWN_LINK_RE = re.compile(r"\[([^\]]*)\]\([^)]*\)")
_SENTENCE_SPLIT_RE = re.compile(r"(?<=[.!?\u061f])\s+|\n+")
_WORD_RE = re.compile(r"\w+")


def _comparison_key(sentence: str) -> str | None:
    """Reduce a sentence to its words, or ``None`` when it is too short to count.

    Markdown decoration, link syntax, and the zero-width non-joiner are dropped
    so that wording decides whether two passages match, not formatting: Persian
    ``می\u200cشود`` and ``میشود`` are the same word to a reader.
    """
    text = WIKILINK_RE.sub(lambda match: match.group(1).split("|")[-1], sentence)
    text = _MARKDOWN_LINK_RE.sub(r"\1", text)
    text = re.sub(r"[*_`#>|]", " ", text)
    text = text.replace("\u200c", "").lower()
    words = _WORD_RE.findall(text)
    if len(words) < DUPLICATE_MIN_WORDS:
        return None
    return " ".join(words)


def _duplicate_prose_findings(docs: dict[str, Doc]) -> list[Finding]:
    """Report a passage that appears in more than one article.

    Reports each repeat after the first, naming the article and line it first
    appeared in, the way duplicate titles are reported. ``Sources`` is skipped,
    because two articles citing the same edition on purpose are not repeating
    each other's prose.
    """
    first_seen: dict[str, tuple[str, int, str]] = {}
    findings: list[Finding] = []

    for path in sorted(docs):
        doc = docs[path]
        sources_lines = _section_lines(doc, "Sources")
        for line, text in iter_body_lines(doc):
            if line in sources_lines:
                continue
            for sentence in _SENTENCE_SPLIT_RE.split(text):
                sentence = sentence.strip()
                key = _comparison_key(sentence)
                if key is None:
                    continue
                origin = first_seen.get(key)
                if origin is None:
                    first_seen[key] = (path, line, sentence)
                    continue
                if origin[0] == path:
                    continue  # repetition inside one article is not this check
                findings.append(
                    Finding(
                        path,
                        line,
                        "warning",
                        "collection.duplicate_prose",
                        f"this passage already appears in {origin[0]}:{origin[1]} "
                        f'("{_truncate(origin[2])}"); link to that article instead of restating it',
                    )
                )
    return findings


def _truncate(text: str, limit: int = 60) -> str:
    text = " ".join(text.split())
    return text if len(text) <= limit else text[: limit - 1].rstrip() + "\u2026"


# --- link resolution --------------------------------------------------------


def split_link(body: str) -> tuple[str, str]:
    """Split a wikilink body into (target, display text).

    Inside a table row Obsidian requires the alias separator to be escaped as
    ``\\|``; both forms are accepted here and the backslash is stripped so the
    target still resolves. An unescaped pipe inside a table row is reported
    separately, because the markdown parser reads it as a cell separator.
    """
    for index, char in enumerate(body):
        if char != "|":
            continue
        if index and body[index - 1] == "\\":
            return body[: index - 1], body[index + 1 :]
        return body[:index], body[index + 1 :]
    return body, ""


def has_unescaped_pipe(body: str) -> bool:
    """True when a wikilink body carries a '|' that no backslash escapes."""
    for index, char in enumerate(body):
        if char == "|" and (index == 0 or body[index - 1] != "\\"):
            return True
    return False


def build_link_index(docs: dict[str, Doc]) -> dict[str, str]:
    """Map every referenceable name (path, basename, alias) to a document."""
    index: dict[str, str] = {}
    for path, doc in docs.items():
        stem = path[:-3] if path.endswith(".md") else path
        for key in (stem, stem.rsplit("/", 1)[-1]):
            index.setdefault(key.lower(), path)
        aliases = doc.meta.get("aliases", [])
        if isinstance(aliases, str):
            aliases = [aliases]
        if isinstance(aliases, list):
            for alias in aliases:
                name = str(alias).strip()
                if name:
                    index.setdefault(name.lower(), path)
    return index


def _local_file_refs(text: str) -> list[str]:
    """Extract cited local file paths from a Sources entry."""
    refs: list[str] = []
    for match in BACKTICK_RE.finditer(text):
        token = match.group(1).strip()
        if "/" in token and not token.startswith(("http://", "https://")):
            refs.append(token)
    for match in RAW_PATH_RE.finditer(text):
        refs.append(match.group(0))
    cleaned: list[str] = []
    for ref in refs:
        ref = ref.strip().rstrip(".,;:").strip()
        if ref and ref not in cleaned:
            cleaned.append(ref)
    return cleaned


# --- per-document rules -----------------------------------------------------


def check_doc(
    doc: Doc,
    link_index: dict[str, str],
    docs: dict[str, Doc],
    other_md_paths: Sequence[str],
    resolve_source: Callable[[str], bool],
) -> list[Finding]:
    findings: list[Finding] = []

    def error(line: int, rule: str, message: str) -> None:
        findings.append(Finding(doc.path, line, "error", rule, message))

    def warn(line: int, rule: str, message: str) -> None:
        findings.append(Finding(doc.path, line, "warning", rule, message))

    # frontmatter: report the block once, then the individual keys inside it
    if doc.fm_error:
        rule = "frontmatter.missing" if "missing" in doc.fm_error else "frontmatter.unterminated"
        error(1, rule, doc.fm_error)
    else:
        if "type" not in doc.meta:
            error(1, "frontmatter.type", "frontmatter is missing the required 'type' key")
        elif doc.doc_type not in VALID_TYPES:
            error(1, "frontmatter.type", f"unknown type '{doc.doc_type}' (expected one of {', '.join(VALID_TYPES)})")

        if "status" not in doc.meta:
            error(1, "frontmatter.status", "frontmatter is missing the required 'status' key")
        elif doc.status not in VALID_STATUSES:
            error(
                1,
                "frontmatter.status",
                f"unknown status '{doc.status}' (expected one of {', '.join(VALID_STATUSES)})",
            )

        tags = doc.tags
        if not tags:
            error(1, "frontmatter.tags", "frontmatter has no 'tags'; add at least one so the article is findable")
        else:
            unknown = [tag for tag in tags if tag not in KNOWN_TAGS]
            if unknown:
                warn(1, "frontmatter.tags_unknown", f"tag(s) outside the known vocabulary: {', '.join(unknown)}")

    # structure
    h1s = [heading for heading in doc.headings if heading.level == 1]
    if len(h1s) != 1:
        error(1, "structure.h1", f"expected exactly one '# ' heading, found {len(h1s)}")
    else:
        h1_index = doc.headings.index(h1s[0])
        if not _has_definition(doc.headings, h1_index):
            error(
                h1s[0].line,
                "structure.definition",
                "no definition content beneath the H1 heading (add a lead paragraph or a '## Definition' section)",
            )

    for position, heading in enumerate(doc.headings):
        if heading.level >= 2 and not _subtree_has_content(doc.headings, position):
            error(heading.line, "structure.empty_section", f"section '{heading.text}' has no content")

    if doc.doc_type == "index":
        if not any(WIKILINK_RE.search(text) for _, text in iter_body_lines(doc)):
            error(1, "structure.index_links", "an index article must link at least one article")
    else:
        positions: dict[str, int] = {}
        missing: list[str] = []
        for name in REQUIRED_SECTIONS:
            for position, heading in enumerate(doc.headings):
                if _normalise(heading.text) == _normalise(name):
                    positions[name] = position
                    break
            else:
                missing.append(name)
        if missing:
            error(1, "structure.required_section", f"missing required section(s): {', '.join(missing)}")
        else:
            found = [positions[name] for name in REQUIRED_SECTIONS]
            if found != sorted(found):
                expected = " -> ".join(REQUIRED_SECTIONS)
                error(1, "structure.section_order", f"required sections out of order (expected {expected})")
            if found[-1] != len(doc.headings) - 1:
                error(
                    doc.headings[found[-1]].line,
                    "structure.sources_last",
                    "'Sources' must be the final section of an article",
                )

    # sources
    sources = find_section(doc.headings, "Sources")
    if sources is not None:
        bullets = [text for _, text in sources.content if LIST_ITEM_RE.match(text)]
        if not bullets:
            error(sources.line, "sources.empty", "'Sources' must contain at least one '- ' entry")
        for line, text in sources.content:
            for ref in _local_file_refs(text):
                if not resolve_source(ref):
                    error(line, "sources.local_file", f"cited source '{ref}' does not exist in the vault")

    # language: the domain declares its language in Agents.md, so prose that
    # drifts to another script means either the article or the rule is wrong
    domain = _domain_of(doc.path)
    language = DOMAIN_LANGUAGES.get(domain, "en")
    non_latin = _non_latin_share(_prose_text(doc))
    if non_latin is not None:
        if language == "en" and non_latin > LANGUAGE_MAX_NON_LATIN_SHARE:
            warn(
                1,
                "style.language",
                f"{non_latin:.0%} of the letters are non-Latin, but this domain is declared English; "
                "write the article in English, or declare the domain's language in Agents.md",
            )
        elif language != "en" and non_latin < LANGUAGE_MIN_NON_LATIN_SHARE:
            warn(
                1,
                "style.language",
                f"only {non_latin:.0%} of the letters are non-Latin, but domain '{domain}' is declared "
                f"'{language}'; write the article in that language, or declare the domain English",
            )

    # links
    other_index = {Path(path).stem.lower(): path for path in other_md_paths}
    for line, text in iter_body_lines(doc):
        for match in WIKILINK_RE.finditer(text):
            target = split_link(match.group(1))[0]
            page, _, anchor = target.partition("#")
            if not page.strip():
                target_doc = doc
            else:
                resolved = link_index.get(page.strip().lower())
                if resolved is None:
                    if page.strip().lower() in other_index:
                        warn(line, "link.outside_wiki", f"[[{target}]] points outside wiki/; cite sources instead of linking them")
                    else:
                        error(line, "link.unresolved", f"[[{target}]] does not resolve to any article")
                    continue
                target_doc = docs[resolved]
            if anchor.strip():
                wanted = _normalise(anchor)
                if not any(_normalise(h.text) == wanted for h in target_doc.headings):
                    error(line, "link.anchor", f"[[{target}]] anchor '#{anchor.strip()}' is not a heading in {target_doc.path}")

        if TABLE_ROW_RE.match(text):
            for match in WIKILINK_RE.finditer(text):
                if has_unescaped_pipe(match.group(1)):
                    error(
                        line,
                        "link.pipe_in_table",
                        f"[[{match.group(1)}]] uses an unescaped '|' in a table row; escape it as '\\|' "
                        "or the row is rendered with extra cells",
                    )
                    break

        for _ in CURLY_QUOTE_RE.finditer(text):
            warn(line, "style.curly_quotes", "curly quotes found; use straight quotes for consistency")
            break

    return findings


# --- collection rules -------------------------------------------------------


def check_collection(docs: dict[str, Doc], link_index: dict[str, str]) -> list[Finding]:
    findings: list[Finding] = []
    by_folder: dict[str, list[str]] = {}
    for path in docs:
        folder = path.rsplit("/", 1)[0] if "/" in path else ""
        by_folder.setdefault(folder, []).append(path)

    for folder, paths in sorted(by_folder.items()):
        index_path = f"{folder}/index.md" if folder else "index.md"
        if index_path not in docs:
            findings.append(
                Finding(
                    f"{folder}/" if folder else "./",
                    1,
                    "warning",
                    "collection.no_index",
                    "no index.md recording this domain's knowledge map",
                )
            )

    by_title: dict[str, list[str]] = {}
    for path, doc in docs.items():
        if doc.doc_type == "index":
            # Domain entry points are all named index.md by design and are
            # addressed by path, so they can never make a wikilink ambiguous.
            continue
        title = Path(path).stem.lower()
        by_title.setdefault(title, []).append(path)
    for title, paths in sorted(by_title.items()):
        if len(paths) > 1:
            ordered = sorted(paths)
            for path in ordered[1:]:
                findings.append(
                    Finding(
                        path,
                        1,
                        "error",
                        "collection.duplicate_title",
                        f"title '{Path(path).stem}' also used by {ordered[0]}; wikilinks become ambiguous",
                    )
                )

    findings.extend(_duplicate_prose_findings(docs))

    referenced: set[str] = set()
    link_lines: dict[str, list[tuple[str, int]]] = {}
    for path, doc in docs.items():
        for line, text in iter_body_lines(doc):
            for match in WIKILINK_RE.finditer(text):
                target = split_link(match.group(1))[0].split("#", 1)[0].strip()
                resolved = link_index.get(target.lower()) if target else None
                if resolved:
                    referenced.add(resolved)
                    link_lines.setdefault(resolved, []).append((path, line))

    for folder, paths in sorted(by_folder.items()):
        index_path = f"{folder}/index.md" if folder else "index.md"
        if index_path not in docs:
            continue
        for path in sorted(paths):
            if path == index_path:
                continue
            if index_path not in {source for source, _ in link_lines.get(path, [])}:
                findings.append(
                    Finding(
                        path,
                        1,
                        "warning",
                        "collection.index_missing",
                        f"not linked from its domain index {index_path}",
                    )
                )

    for path, doc in docs.items():
        if doc.doc_type == "index":
            continue
        if path not in referenced:
            findings.append(
                Finding(path, 1, "warning", "collection.orphan", "no other article links here")
            )

    return findings


# --- analysis entry point ---------------------------------------------------


def analyze(
    docs: dict[str, str],
    other_md_paths: Iterable[str] = (),
    resolve_source: Callable[[str], bool] | None = None,
) -> list[Finding]:
    """Validate in-memory documents. Pure: no disk access, so it is testable."""
    parsed = {path: parse_doc(path, text) for path, text in docs.items()}
    link_index = build_link_index(parsed)
    resolver = resolve_source or (lambda ref: True)

    findings: list[Finding] = []
    for path in sorted(parsed):
        findings.extend(check_doc(parsed[path], link_index, parsed, list(other_md_paths), resolver))
    findings.extend(check_collection(parsed, link_index))
    return sorted(findings, key=lambda finding: finding.sort_key)


# --- disk loading -----------------------------------------------------------


def _walk_markdown(root: Path) -> list[Path]:
    found: list[Path] = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(name for name in dirnames if not name.startswith("."))
        for name in sorted(filenames):
            if name.endswith(".md"):
                found.append(Path(dirpath) / name)
    return found


def load_docs(root: Path) -> dict[str, str]:
    wiki = root / "wiki"
    if not wiki.is_dir():
        return {}
    return {
        path.relative_to(root).as_posix(): path.read_text(encoding="utf-8", errors="replace")
        for path in _walk_markdown(wiki)
    }


def load_other_markdown(root: Path) -> list[str]:
    return [
        path.relative_to(root).as_posix()
        for path in _walk_markdown(root)
        if "wiki" not in path.relative_to(root).parts
    ]


def make_source_resolver(root: Path) -> Callable[[str], bool]:
    candidates = [path for path in _walk_markdown(root)]

    def resolve(ref: str) -> bool:
        if (root / ref).exists():
            return True
        if "/" not in ref:
            lowered = ref.lower()
            return any(path.name.lower() == lowered for path in candidates)
        return False

    return resolve


# --- self-test --------------------------------------------------------------

_FM = """---
type: concept
status: draft
tags:
  - testing
---
"""

GOOD = _FM + """
# Good Article

A definition paragraph that explains the concept under test.

## Example

A short illustration.

## Related Concepts

- [[Other Article]] — a related concept.

## My Understanding

An interpretation, not a claim taken from the sources.

## Sources

- Martin Fowler, [Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html), 2007.
"""

OTHER = _FM + """
# Other Article

A definition paragraph for the other concept.

## Related Concepts

- [[Good Article]] — the article under test.

## My Understanding

A separate reading of the other concept, recorded as interpretation.

## Sources

- Gerard Meszaros, *xUnit Test Patterns*, Addison-Wesley, 2007.
"""

INDEX = """---
type: index
status: draft
tags:
  - testing
---

# Testing Index

The entry point for this domain. Planned articles are listed without links.

## Written

- [[Good Article]] — one concept.
- [[Other Article]] — another concept.
"""

LONELY = _FM + """
# Lonely Article

A definition paragraph.

## Related Concepts

- [[Good Article]] — a related concept.

## My Understanding

A lone interpretation, set down apart from the sources.

## Sources

- Gerard Meszaros, *xUnit Test Patterns*, Addison-Wesley, 2007.
"""

#: Fixtures for the language rule. ``wiki/llm/`` is the domain Agents.md
#: declares Persian, so these prove the check fires in both directions.
PERSIAN_ARTICLE = """---
type: concept
status: draft
tags:
  - llm
  - rag
---

# RAG

بازیابی و تولید معماری‌ای است که مدل را به یک پایگاه دانش بیرونی وصل می‌کند و پاسخ را از متن بازیابی‌شده می‌سازد.

## Related Concepts

- [[Good Article]] — یک مفهوم مرتبط.

## My Understanding

این یک برداشت شخصی است، نه نقل‌قولی از یک منبع.

## Sources

- 3lf, *LLM به زبان آدمیزاد*, `raw/books/llm.md`
"""

PERSIAN_INDEX = """---
type: index
status: draft
tags:
  - llm
---

# LLM Index

نقطه ورود این دامنه است و مقالات برنامه‌ریزی‌شده بدون پیوند فهرست می‌شوند.

## نوشته‌شده

- [[RAG]] — یک مفهوم پایه.
"""

PERSIAN_CLEAN = {
    "wiki/llm/RAG.md": PERSIAN_ARTICLE,
    "wiki/llm/index.md": PERSIAN_INDEX,
}

ENGLISH_IN_PERSIAN_DOMAIN = _FM + """
# RAG

A definition paragraph for the article under test.

## Related Concepts

- [[Good Article]] — a related concept.

## My Understanding

A retrieval reading, held as interpretation rather than sourced fact.

## Sources

- 3lf, *LLM for humans*, `raw/books/llm.md`
"""

PERSIAN_IN_ENGLISH_DOMAIN = _FM + """
# Good Article

یک بند تعریف که مفهوم مورد آزمون را توضیح می‌دهد و نسبت آن را با مفاهیم همسایه روشن می‌کند.

## Example

یک تصویر کوتاه از کاربرد آن در عمل، بی‌آنکه ادعایی فراتر از منابع داشته باشد.

## Related Concepts

- [[Other Article]] — یک مفهوم مرتبط.

## My Understanding

یک برداشت، نه ادعایی برگرفته از منابع.

## Sources

- Martin Fowler, [Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html), 2007.
"""

CLEAN = {
    "wiki/testing/Good Article.md": GOOD,
    "wiki/testing/Other Article.md": OTHER,
    "wiki/testing/index.md": INDEX,
}


def _cases() -> list[tuple[str, dict[str, str], list[str], set[str]]]:
    def mutate(*positional: str, **replacements: str) -> dict[str, str]:
        """Start from the clean vault and apply one deliberate defect."""
        docs = dict(CLEAN)
        if positional:
            path, text = positional
            docs[path] = text
        docs.update(replacements)
        return docs

    good = "wiki/testing/Good Article.md"
    index_path = "wiki/testing/index.md"

    persian_vault = dict(CLEAN)
    persian_vault.update(PERSIAN_CLEAN)

    return [
        ("clean", dict(CLEAN), [], set()),
        ("persian domain, persian prose", persian_vault, [], set()),
        (
            "latin prose in a persian domain",
            {**persian_vault, "wiki/llm/RAG.md": ENGLISH_IN_PERSIAN_DOMAIN},
            [],
            {"style.language"},
        ),
        (
            "non-latin prose in an english domain",
            mutate(**{"wiki/testing/Good Article.md": PERSIAN_IN_ENGLISH_DOMAIN}),
            [],
            {"style.language"},
        ),
        (
            "frontmatter missing",
            mutate(**{"wiki/testing/Good Article.md": GOOD.split("\n---\n", 1)[1].lstrip("\n")}),
            [],
            {"frontmatter.missing"},
        ),
        (
            "unterminated frontmatter",
            mutate(good, GOOD.replace("  - testing\n---", "  - testing", 1)),
            [],
            {"frontmatter.unterminated"},
        ),
        (
            "bad type",
            mutate(**{"wiki/testing/Good Article.md": GOOD.replace("type: concept", "type: note")}),
            [],
            {"frontmatter.type"},
        ),
        (
            "bad status",
            mutate(**{"wiki/testing/Good Article.md": GOOD.replace("status: draft", "status: published")}),
            [],
            {"frontmatter.status"},
        ),
        (
            "missing tags",
            mutate(**{"wiki/testing/Good Article.md": GOOD.replace("tags:\n  - testing\n", "")}),
            [],
            {"frontmatter.tags"},
        ),
        (
            "unknown tag",
            mutate(**{"wiki/testing/Good Article.md": GOOD.replace("  - testing", "  - wibble")}),
            [],
            {"frontmatter.tags_unknown"},
        ),
        (
            "no H1",
            mutate(**{"wiki/testing/Good Article.md": GOOD.replace("# Good Article\n\n", "")}),
            [],
            {"structure.h1"},
        ),
        (
            "no definition content",
            mutate(
                **{
                    "wiki/testing/Good Article.md": GOOD.replace(
                        "# Good Article\n\nA definition paragraph that explains the concept under test.\n\n", "# Good Article\n\n"
                    )
                }
            ),
            [],
            {"structure.definition"},
        ),
        (
            "empty section",
            mutate(
                **{
                    "wiki/testing/Good Article.md": GOOD.replace(
                        "## Example\n\nA short illustration.\n\n", "## Example\n\n"
                    )
                }
            ),
            [],
            {"structure.empty_section"},
        ),
        (
            "missing required section",
            mutate(
                **{
                    "wiki/testing/Good Article.md": GOOD.replace(
                        "## My Understanding\n\nAn interpretation, not a claim taken from the sources.\n\n", ""
                    )
                }
            ),
            [],
            {"structure.required_section"},
        ),
        (
            "required sections out of order",
            mutate(
                **{
                    "wiki/testing/Good Article.md": GOOD.replace(
                        "## Related Concepts\n\n- [[Other Article]] — a related concept.\n\n## My Understanding\n\nAn interpretation, not a claim taken from the sources.\n",
                        "## My Understanding\n\nAn interpretation, not a claim taken from the sources.\n\n## Related Concepts\n\n- [[Other Article]] — a related concept.\n",
                    )
                }
            ),
            [],
            {"structure.section_order"},
        ),
        (
            "content after Sources",
            mutate(
                **{
                    "wiki/testing/Good Article.md": GOOD
                    + "\n## Notes\n\nSomething after the sources.\n"
                }
            ),
            [],
            {"structure.sources_last"},
        ),
        (
            "unresolved wikilink",
            mutate(
                **{
                    "wiki/testing/Good Article.md": GOOD.replace("[[Other Article]]", "[[Ghost Concept]]")
                }
            ),
            [],
            {"link.unresolved"},
        ),
        (
            "broken anchor",
            mutate(
                **{
                    "wiki/testing/Good Article.md": GOOD.replace("[[Other Article]]", "[[Other Article#Nowhere]]")
                }
            ),
            [],
            {"link.anchor"},
        ),
        (
            "link outside wiki",
            mutate(**{"wiki/testing/Good Article.md": GOOD.replace("[[Other Article]]", "[[Raw Note]]")}),
            ["raw/articles/Raw Note.md"],
            {"link.outside_wiki"},
        ),
        (
            "empty Sources",
            mutate(
                **{
                    "wiki/testing/Good Article.md": GOOD.replace(
                        "- Martin Fowler, [Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html), 2007.\n",
                        "See the references above.\n",
                    )
                }
            ),
            [],
            {"sources.empty"},
        ),
        (
            "cited file absent",
            mutate(
                **{
                    "wiki/testing/Good Article.md": GOOD.replace(
                        "- Martin Fowler, [Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html), 2007.\n",
                        "- Gerard Meszaros, *xUnit Test Patterns*, `raw/books/missing.pdf`.\n",
                    )
                }
            ),
            [],
            {"sources.local_file"},
        ),
        (
            "duplicate title",
            # Reworded, so this case isolates the ambiguous title: a copied body
            # would also trip the repeated-prose check, which is its own case.
            mutate(
                **{
                    "wiki/design/Good Article.md": GOOD.replace(
                        "A definition paragraph that explains the concept under test.",
                        "A definition paragraph for a same-titled article elsewhere.",
                    ).replace(
                        "An interpretation, not a claim taken from the sources.",
                        "A different reading, recorded beside the same title.",
                    )
                }
            ),
            [],
            {"collection.duplicate_title", "collection.no_index", "collection.orphan"},
        ),
        (
            "not linked from index",
            mutate(
                **{
                    "wiki/testing/index.md": INDEX.replace("- [[Other Article]] — another concept.\n", "")
                }
            ),
            [],
            {"collection.index_missing"},
        ),
        (
            "orphan article",
            mutate(**{"wiki/testing/Lonely Article.md": LONELY}),
            [],
            {"collection.index_missing", "collection.orphan"},
        ),
        (
            "index without links",
            mutate(
                index_path,
                INDEX.replace(
                    "- [[Good Article]] — one concept.\n- [[Other Article]] — another concept.\n",
                    "Planned articles are listed here once written.\n",
                ),
            ),
            [],
            {"structure.index_links", "collection.index_missing"},
        ),
        (
            "curly quotes",
            mutate(
                **{
                    "wiki/testing/Good Article.md": GOOD.replace(
                        "explains the concept under test", "explains the \u201cconcept\u201d under test"
                    )
                }
            ),
            [],
            {"style.curly_quotes"},
        ),
        (
            "two domain indexes",
            mutate(**{index_path: INDEX, "wiki/design/index.md": INDEX.replace("this domain", "the design vault")}),
            [],
            set(),
        ),
        (
            "duplicated prose",
            mutate(
                **{
                    "wiki/testing/Other Article.md": OTHER.replace(
                        "A separate reading of the other concept, recorded as interpretation.",
                        "A definition paragraph that explains the concept under test.",
                    )
                }
            ),
            [],
            {"collection.duplicate_prose"},
        ),
        (
            "escaped pipe in a table wikilink",
            mutate(
                **{
                    good: GOOD.replace(
                        "A short illustration.\n",
                        "A short illustration.\n\n| Need | Choice |\n| --- | --- |\n"
                        "| a related concept | [[Other Article\\|Other]] |\n",
                    )
                }
            ),
            [],
            set(),
        ),
        (
            "raw pipe in a table wikilink",
            mutate(
                **{
                    good: GOOD.replace(
                        "A short illustration.\n",
                        "A short illustration.\n\n| Need | Choice |\n| --- | --- |\n"
                        "| a related concept | [[Other Article|Other]] |\n",
                    )
                }
            ),
            [],
            {"link.pipe_in_table"},
        ),
    ]


def run_self_test(quiet: bool = False, stream=sys.stdout) -> int:
    """Check the rules fire on minimal fixtures and stay quiet on a clean vault.

    ``quiet`` suppresses the passing lines so that a hook can report one line;
    failures always print in full, because a suppressed failure is a lie.
    """
    failures = 0
    for name, docs, other_paths, expected in _cases():
        findings = analyze(
            docs,
            other_md_paths=other_paths,
            resolve_source=lambda ref: ref not in ("raw/books/missing.pdf",),
        )
        actual = {finding.rule for finding in findings}
        if actual == expected:
            if not quiet:
                print(f"PASS  {name}", file=stream)
            continue
        failures += 1
        print(f"FAIL  {name}", file=stream)
        print(f"      expected: {sorted(expected) or ['<no findings>']}", file=stream)
        print(f"      actual:   {sorted(actual) or ['<no findings>']}", file=stream)
        for finding in findings:
            print(f"        {finding.format()}", file=stream)

    cases = _cases()
    covered: set[str] = set()
    for _, _, _, expected in cases:
        covered |= expected
    uncovered = sorted(ALL_RULES - covered)
    unregistered = sorted(covered - ALL_RULES)
    if uncovered or unregistered:
        failures += 1
        print("FAIL  rule coverage", file=stream)
        if uncovered:
            print(f"      no fixture exercises: {uncovered}", file=stream)
        if unregistered:
            print(f"      fixtures assert rules that are not declared in ALL_RULES: {unregistered}", file=stream)
    elif not quiet:
        print(f"PASS  rule coverage ({len(ALL_RULES)} rules exercised)", file=stream)

    total = len(cases) + 1
    print(f"\n{total - failures}/{total} self-test checks passed", file=stream)
    return 1 if failures else 0


# --- command line -----------------------------------------------------------


def _infer_root(explicit: str | None) -> Path:
    if explicit:
        return Path(explicit).resolve()
    cwd = Path.cwd()
    if (cwd / "wiki").is_dir():
        return cwd
    script_root = Path(__file__).resolve().parent.parent
    return script_root


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="validate_wiki.py",
        description="Validate wiki/ articles against the structural rules in Agents.md.",
    )
    parser.add_argument("--root", default=None, help="vault root (default: nearest directory containing wiki/)")
    parser.add_argument("--json", action="store_true", help="emit a machine-readable report")
    parser.add_argument("--strict", action="store_true", help="treat warnings as failures")
    parser.add_argument("--quiet", action="store_true", help="print errors only")
    parser.add_argument("--self-test", action="store_true", help="verify the rules using in-memory fixtures")
    parser.add_argument(
        "--all",
        action="store_true",
        help="run the self-test and then validate the vault, failing if either fails",
    )
    args = parser.parse_args(argv)

    self_test_status = 0
    if args.self_test or args.all:
        # Under --all the self-test report is diagnostics, so it goes to stderr
        # and the vault report keeps stdout to itself: ``--all --json`` then
        # stays a parseable single JSON document.
        self_test_status = run_self_test(
            quiet=args.quiet,
            stream=sys.stderr if args.all else sys.stdout,
        )
        if args.self_test:
            return self_test_status

    root = _infer_root(args.root)
    docs = load_docs(root)
    if not docs:
        print(f"error: no markdown articles found under {root / 'wiki'}", file=sys.stderr)
        return 2

    findings = analyze(docs, load_other_markdown(root), make_source_resolver(root))
    errors = [f for f in findings if f.severity == "error"]
    warnings = [f for f in findings if f.severity == "warning"]

    if args.json:
        print(
            json.dumps(
                {
                    "root": root.as_posix(),
                    "articles": len(docs),
                    "errors": len(errors),
                    "warnings": len(warnings),
                    "findings": [
                        {
                            "path": f.path,
                            "line": f.line,
                            "severity": f.severity,
                            "rule": f.rule,
                            "message": f.message,
                        }
                        for f in findings
                    ],
                },
                indent=2,
            )
        )
    else:
        for finding in findings:
            if args.quiet and finding.severity == "warning":
                continue
            print(finding.format())
        if findings:
            print()
        print(
            f"{len(errors)} error(s), {len(warnings)} warning(s) across {len(docs)} article(s) in {root.as_posix()}"
        )

    if errors or (args.strict and warnings):
        return 1
    return self_test_status


if __name__ == "__main__":
    sys.exit(main())
