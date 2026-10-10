# Repository Guidelines

## Purpose

This repository is a model-agnostic personal knowledge base for software engineering.

| Directory | Contents | Who writes it |
| --- | --- | --- |
| `wiki/` | Reviewed, synthesized knowledge, organized by domain | Agents and the owner |
| `raw/` | Source material as captured: articles, books, papers | The owner |
| `templates/` | Reusable document templates | The owner |
| `tools/` | Scripts that check the repository | Agents and the owner |
| `Clippings/` | Inbox for externally clipped sources, before filing into `raw/` | The owner |

This file is repository policy, not a wiki article. It carries no frontmatter and is not itself validated.

The vault is read through Obsidian: frontmatter properties, `[[wikilinks]]`, tags, and the graph are the navigation model. The conventions below are therefore load-bearing rather than decorative.

## Enforcement

`Agents.md` is the normative description of how this repository is organized. `tools/validate_wiki.py` enforces the structural rules mechanically:

```
python tools/validate_wiki.py             # report errors and warnings
python tools/validate_wiki.py --strict    # treat warnings as failures
python tools/validate_wiki.py --json      # machine-readable report
python tools/validate_wiki.py --self-test # verify the rules themselves
python tools/validate_wiki.py --all       # the self-test and the vault, in one command
```

`--all` is the check that matters: it verifies that the rules still behave as fixtures expect, then validates the vault, and fails if either half fails. A rule can be quietly broken while every article still validates, which is why the two are one command rather than two habits. Under `--all` the self-test report goes to stderr, so `--all --json` still writes a single parseable JSON document to stdout.

- Run the validator before declaring any article finished. Exit code `0` is clean, `1` means errors were found, `2` means the vault could not be read.
- `tools/hooks/pre-commit` runs `--all` and refuses a commit that leaves the vault invalid. Git does not clone hooks, so a clone enables it once with `git config core.hooksPath tools/hooks`; setting that config is the only manual step, and `git commit --no-verify` bypasses the check deliberately.
- Rules that need judgement are listed in the Review Checklist. The validator cannot judge those.
- When these rules and actual practice disagree, stop and reconcile them explicitly: either fix the files or amend this document. Do not leave a rule that is silently ignored, and do not silently follow practice instead of the rule.
- The tooling uses the Python 3 standard library only. Do not introduce a package manager, lockfile, or additional runtime to the repository.

## General Rules

- Follow the existing repository structure.
- Do not modify `raw/` unless explicitly requested.
- Do not modify `templates/` unless explicitly requested.
- Keep knowledge organized, focused, and maintainable.
- Prefer one meaningful concept per article.
- Avoid unnecessary fragmentation.
- Reuse existing articles instead of creating duplicates.
- Use Markdown for knowledge articles.
- Use Obsidian wikilinks when referencing other wiki concepts.
- Do not invent facts, sources, references, or citations.

## Article Format

### Location and naming

- Articles live at `wiki/<domain>/<Article Name>.md`, exactly one folder level deep.
- Domain folders are lowercase: `wiki/testing/`, `wiki/design/`.
- File names are Title Case and match the canonical term for the concept, not a phrase that describes it.
- Use the established software engineering term as the title. When a concept has a widely used synonym or a plural form, record it in `aliases` instead of creating a second article.
- One concept per file. A concept earns its own article when it has an independent definition, its own terminology, and its own relationships. Keep it as a section of its parent when it can be stated in a paragraph without losing precision.
- Every domain folder contains an `index.md`. Nothing else belongs in `wiki/` besides articles and domain indexes.
- Domain indexes all share the name `index.md` by design. They are addressed by path and are never the target of a wikilink, so they are exempt from the rule that article titles must be unique.

### Frontmatter

Every article begins with a frontmatter block, opened and closed by a `---` line:

```
---
type: concept
status: draft
tags:
  - testing
aliases:
  - Test Double
---
```

- `type` is required, and is one of `concept`, `comparison`, or `index`.
- `status` is required, and is one of `draft`, `reviewed`, or `archived`.
    - `draft` — written but not yet reviewed. This is the only status an agent writes.
    - `reviewed` — accepted by the owner. Only the owner sets this.
    - `archived` — superseded or withdrawn; keep the file for history rather than deleting it.
- `tags` is required and uses lowercase, singular terms from the vocabulary below. Reuse an existing tag before proposing a new one; a new tag is a change to this document.
- `aliases` is optional and lists synonyms, abbreviations, and plural forms so that links from prose still resolve.

The current tag vocabulary is `testing`, `tdd`, `test-doubles`, `design`, `refactoring`, `architecture`, `tooling`, `process`, `llm`, `prompting`, `rag`, `agents`, `fine-tuning`, `evaluation`, `security`. It is mirrored in `KNOWN_TAGS` in `tools/validate_wiki.py`; changing it means changing both places.

### Language

English is the default. A domain is declared in another language only when the material it synthesizes is written in that language; that decision is recorded here and mirrored in `DOMAIN_LANGUAGES` in `tools/validate_wiki.py`, so changing it means changing both places.

| Domain | Language |
| --- | --- |
| any domain not listed below | English |
| `wiki/llm/` | Persian (`fa`) |

The declaration covers the prose an article is written in. Frontmatter keys, tag values, required section names, and wikilink targets stay in English in every domain regardless of language, because they are navigation rather than exposition: an Obsidian property, a tag, or a link that changes spelling per domain stops being searchable across the vault.

The validator measures the script the letters of an article's prose belong to, with code blocks and inline code excluded so that an example does not set the language. It reports a warning when an English domain reads mostly non-Latin, and when a domain declared non-English reads mostly Latin, in both cases because one of the two — the article or this table — is now wrong.

### Required sections

Every `concept` and `comparison` article contains these sections, in this order, with `Sources` last:

1. `Related Concepts` — wikilinks to neighbouring articles, each with a short reason it is related.
2. `My Understanding` — what the author concluded, clearly separated from what the sources state.
3. `Sources` — where the material came from.

Other sections are welcome and encouraged. Use domain-appropriate headings rather than padding the required ones, and delete any section that has no content rather than leaving an empty heading.

An article opens with exactly one `# ` heading and a definition beneath it: either a lead paragraph, or a `## Definition`, `## Purpose`, `## Overview`, or `## Introduction` section. Two H1 headings, or a heading with nothing under it, are errors.

An `index` article is an entry point rather than an exposition. Required sections do not apply to it. It must link at least one article, and it lists written articles as wikilinks and planned articles as plain text so that the knowledge map stays visible without creating links to pages that do not exist.

## Sources and Citations

- Every knowledge article contains a `Sources` section with at least one entry.
- Use one entry per source, in this form:
    - Web source: `- Martin Fowler, [Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html), 2007.`
    - Local source: `` - Gerard Meszaros, *xUnit Test Patterns*, Addison-Wesley, 2007. `raw/books/xUnit Test Patterns Refactoring Test Code-Addison-Wesley (2007).pdf` ``
- A cited local file must exist in the repository. When a source exists in `raw/`, cite the local file rather than a URL.
- Prefer printed page numbers, and name the section or pattern as well, so a reference survives a different edition: `(Test Double pattern, p. 521)`.
- Verify a page reference against the file it points to before writing it. A reference that cannot be confirmed is removed, not guessed.
- Name the source inline when attributing a definition or a disputed claim, so a reader can tell who holds the position.
- Preserve important differences between sources. Do not silently merge conflicting definitions or viewpoints; state both and say they differ.
- Clearly distinguish sourced information from interpretation, and keep interpretation in `My Understanding`.
- If information cannot be supported by the available sources, say so explicitly rather than implying support.

## Links

- Link wiki concepts with wikilinks: `[[State Verification]]`.
- Use `[[Target|display text]]` when the grammar of the sentence needs different wording, such as a plural. Do not change the meaning of the target.
- Use `[[Target#Heading]]` to point at a section, and only when that heading exists in the target. A section rename breaks every such link, so prefer a page link unless the section is the point.
- Inside a table row, escape the alias pipe as `\|`: `[[Target\|display text]]`. An unescaped `|` is read as a cell separator and renders the row with extra cells, which is invisible in the plain text but breaks the table.
- Link on first mention in a section rather than at every occurrence.
- Do not link to an article that does not exist. Record the concept as a planned article in the domain index instead.
- Do not link into `raw/` or `templates/`. Sources are cited in `Sources`, not linked from prose.
- Every article must be reachable from its domain index and linked from at least one other article, so that nothing is orphaned in the graph.

## Writing

- Write in the language the article's domain declares under Language above. English is the default, and a domain leaves it only when the source material it synthesizes is written in another language.
- Use established software engineering terminology.
- Be precise and avoid unnecessary verbosity.
- Use headings, lists, tables, and code examples where they improve clarity.
- Avoid repetition, including restating in one article what another article already covers; link to it instead.
- Use straight quotes, not typographic quotes, so that text is searchable and diffable.
- Do not overstate uncertain or disputed claims.

## Content Standards

Knowledge here is written for an engineer who has to decide whether a practice applies to their situation, so an article about a practice must answer more than what it is.

- State the problem the practice addresses before describing the mechanism.
- State the forces and trade-offs, what the practice costs, and the failure mode it prevents.
- State when the practice does not apply, and what it makes worse. A practice presented with no costs is incomplete.
- Separate the mechanism from opinion and method preference. Labelling a recommendation as interpretation is not the same as presenting it as fact.
- Avoid absolutes such as "always" or "never" unless a cited source takes that position, in which case attribute it.
- Note when a claim is specific to a language, framework, or tool, and when it is general.
- Prefer a concrete scenario over a restatement of the definition.

## Structure and Knowledge Maps

- Keep folder structure meaningful and shallow. `wiki/<domain>/` is the intended shape; do not add sub-folders per topic, article type, or author.
- Create separate articles when a concept has an independent definition, terminology, purpose, or relationships. Do not create separate files merely because a topic is mentioned in another article.
- Prefer semantic organization over arbitrary categorization.
- Start a new knowledge domain by proposing a Knowledge Map: the concepts that deserve articles, the supporting concepts, the relationships between them, which are foundational, and which existing material can be reused. Obtain approval before writing.
- The Knowledge Map's permanent home is the domain index. Written articles appear there as wikilinks; planned articles appear as plain text. Update the index in the same change as any article addition, rename, or deletion.

## Workflow

For a new knowledge topic:

1. Analyze the topic.
2. Propose a Knowledge Map.
3. Propose the article and folder structure.
4. Wait for approval. No file is created or modified before approval, including the domain index.
5. Create or modify files only after approval.
6. Research and synthesize the knowledge, citing what `raw/` actually contains.
7. Add appropriate references and relationships, and update the domain index.
8. Run `python tools/validate_wiki.py` and work through the Review Checklist.
9. Leave the new or changed articles at `status: draft` for the owner to review.

## Review Checklist

The validator covers the first group mechanically. The second group needs judgement and is the author's responsibility.

Mechanical:

- Frontmatter present, with a valid `type`, `status`, and at least one known tag.
- The article's prose is written in the language its domain declares.
- Exactly one H1, with definition content beneath it.
- `Related Concepts`, `My Understanding`, and `Sources` present in that order, with `Sources` last.
- No empty sections.
- Every wikilink and every `#heading` anchor resolves, and no wikilink in a table row carries an unescaped `|`.
- No wikilinks pointing outside `wiki/`.
- `Sources` non-empty, with every cited local file present in the repository.
- No duplicate article titles, no domain missing an index, no article missing from its index, no orphan article.
- No sentence of eight words or more is repeated between two articles — the validator's threshold. `Sources` is excluded from this check, because two articles citing the same edition on purpose are not repeating each other's prose.

Judgement:

- Interpretation is confined to `My Understanding` and reads as interpretation.
- Two articles do not restate the same idea in different words. The repeated-prose check only sees matching sentences, so search for a distinctive phrase before writing a section that may already exist elsewhere.
- Every page reference was opened and confirmed in the file it cites.
- A practice article states the problem, the trade-offs, and when not to apply it.
- The tags describe the article well enough to be useful as a filter.
- Nothing in the knowledge itself depends on a particular model, agent, or vendor.

## Change Control

- Do not make large structural changes without approval.
- New folders, article renames, deletions, new tags, and `status` promotions require approval.
- Do not introduce unrelated concepts or files.
- When an existing concept is relevant, link to it rather than duplicating it.
- The human owner has final authority over the knowledge model and repository structure.

## Model Independence

The repository must remain independent of any specific:

- LLM
- AI provider
- coding agent
- IDE
- CLI tool
- automation platform

Repository rules and knowledge structure must not depend on the behavior or features of a particular model or vendor. This applies to the tooling as well: prefer the standard library over a dependency, and never make a convention conditional on one agent's behaviour.
