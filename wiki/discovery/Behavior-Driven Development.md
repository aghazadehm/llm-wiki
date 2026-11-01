---
type: concept
status: draft
tags:
  - process
  - testing
---

# Behavior-Driven Development

Behavior-Driven Development (BDD) is a collaborative approach to software development that uses natural language descriptions of expected behavior to bridge communication gaps between business, development, and testing. It evolved from TDD and emphasizes discovery, formulation, and automation of examples as executable specifications.

## Related Concepts

- [[Specification by Example]] — BDD is a form of Specification by Example with specific practices and tools.
- [[Three Amigos]] — the discovery phase of BDD involves cross-functional collaboration.
- [[Example Mapping]] — a technique used in BDD discovery.

## My Understanding

BDD typically follows a cycle of Discovery, Formulation, and Automation (as described by Seb Rose/Gaspar Nagy):
- **Discovery** — Collaborative conversation to understand the problem and find examples (using Example Mapping, Three Amigos, etc.)
- **Formulation** — Capturing examples as executable specifications in a structured format like Gherkin (Given-When-Then)
- **Automation** — Implementing the behavior to make the scenarios pass

Dan North originally coined BDD as "test-driven development done right" - shifting focus from "testing" to "behavior specification". The key is using ubiquitous language understood by all stakeholders. Scenarios describe behavior from the user's perspective in business language, not technical implementation details.

BDD is not just about tools like Cucumber; it's fundamentally about collaboration and communication. The tools support the process, but the value comes from the conversations.

## Sources

- Dan North, "Introducing BDD", 2006. [dannorth.net/introducing-bdd/](https://dannorth.net/introducing-bdd/)
- John Ferguson Smart, *BDD in Action: Behavior-Driven Development for the Whole Software Lifecycle*, Manning, 2014.
- Matt Wynne & Aslak Hellesøy, *The Cucumber Book*, Pragmatic Bookshelf, 2012.
- Seb Rose & Gaspar Nagy, *BDD Books: Discovery* and *BDD Books: Formulation*, Leanpub.
- Gojko Adzic, *Specification by Example*, Manning, 2011. `raw/books/specification_by_example.pdf`
