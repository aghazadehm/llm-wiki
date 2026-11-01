---
type: concept
status: draft
tags:
  - process
  - testing
---

# Example Mapping

Example Mapping is a collaborative discovery technique for breaking down a user story or feature into concrete rules, examples, questions, and assumptions. Developed by Matt Wynne and refined by Seb Rose and others, it uses a simple structure of colored index cards (or columns) to facilitate conversation and expose uncertainty before implementation.

## Related Concepts

- [[Three Amigos]] — Example Mapping is typically run as a Three Amigos session (business, development, testing).
- [[Specification by Example]] — Example Mapping is a discovery technique that feeds into Specification by Example's formulation phase.
- [[Behavior-Driven Development]] — Example Mapping is used in the discovery phase of BDD to find examples.
- [[User Story Mapping]] — can be used to break down individual stories identified in a story map.

## My Understanding

Example Mapping structures conversation around four elements, typically represented as columns:
- **Story/Rule** (yellow) — the thing we're discussing (often a user story or acceptance criterion)
- **Rules** (blue) — business rules that must be satisfied
- **Examples** (green) — concrete examples that illustrate the rules
- **Questions** (red) — unknowns, assumptions, or things that need clarification
- **Notes/Assumptions** (sometimes) — other things that come up

The process is simple: the group discusses the story, writes rules as they emerge, finds examples for each rule, and captures questions. When questions arise, the group tries to answer them or identifies who needs to answer. The goal is to surface all the rules and edge cases, and expose uncertainty. A good sign the story is ready is when there are few questions left and examples cover the rules.

Example Mapping is intentionally lightweight and fast (usually 15-30 minutes per story). It prevents going straight to implementation by forcing concrete examples early, and it creates shared understanding through conversation rather than documentation written in isolation.

## Sources

- Seb Rose & Gaspar Nagy, *BDD Books: Discovery*, Leanpub, 2018.
- Matt Wynne, "Introducing Example Mapping", 2014. [cucumber.io/blog/bdd/example-mapping-introduction/](https://cucumber.io/blog/bdd/example-mapping-introduction/)
- John Ferguson Smart, *BDD in Action: Behavior-Driven Development for the Whole Software Lifecycle*, Manning, 2014.
- Gojko Adzic, *Specification by Example: How Successful Teams Deliver the Right Software*, Manning, 2011. `raw/books/specification_by_example.pdf`
