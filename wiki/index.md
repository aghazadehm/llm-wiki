---
type: index
status: draft
tags:
  - process
---

# Index

The vault's single entry point. It does not restate each domain's article list — that belongs to the domain index — but it records what each domain covers, where its index lives, and a few articles that are worth starting from. A reader who knows nothing about the vault can reach any knowledge area from here in one hop.

## Domain map

| Domain        | What it covers                                                                                                                            | Index                       |
| ------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | --------------------------- |
| `testing`     | How a test establishes correctness, which substitute can stand in for a real collaborator, and how that choice is made.                   | `wiki/testing/index.md`     |
| `design`      | The properties of a design that let behavior be changed from outside the code — the property tests depend on.                             | `wiki/design/index.md`      |
| `legacy-code` | What makes code hard to change, how to pin down behavior nobody has written down, and the techniques that make such code testable at all. | `wiki/legacy-code/index.md` |
| `llm`         | 模型、提示、工具、检索与安全 (Persian; the domain is written in the language of the source material it synthesizes).                                    | `wiki/llm/index.md`         |
| `sources`     | One summary page per raw source: what it says, where, and what the articles drew from it.                                                 | `wiki/sources/index.md`     |
| `synthesis`   | Questions answered across the vault, filed back so the vault compounds from its own exploration, not only from its sources.               | `wiki/synthesis/index.md`   |

The `sources` and `synthesis` domains are the two that let the wiki grow from more than its books: `sources` records what each raw document actually contributed, and `synthesis` files an answer back into the vault instead of letting it disappear into chat.

## Start here

- [[Test Doubles]] — the entry point to the testing domain and the question most of it exists to answer.
- [[Seam]] — the design property that makes a system testable in the first place.
- [[Legacy Code]] — where testing and design meet code that cannot yet be changed safely.
- [[RAG]] — the retrieval pattern the llm domain treats most, and the pattern this whole vault is an alternative to.

## Sources

- Andrej Karpathy, [LLM Wiki: a pattern for building personal knowledge bases using LLMs](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f), 2026.
