---
type: concept
status: draft
tags:
  - process
---

# Three Amigos

Three Amigos is a collaborative specification pattern where three perspectives - business (product/BA), development, and testing/QA - come together to discuss and refine a user story before implementation. The goal is shared understanding and catching issues early through conversation.

## Related Concepts

- [[Example Mapping]] — a structured way to run Three Amigos sessions using rules/examples/questions.
- [[Behavior-Driven Development]] — Three Amigos is the discovery phase of BDD.
- [[Specification by Example]] — collaboration between different roles is key to creating good examples.

## My Understanding

The three amigos represent different viewpoints:
- **Business/Product** (the "what" and "why") — ensures the story delivers business value and meets user needs
- **Development** (the "how") — considers technical feasibility, edge cases, architecture implications
- **Testing/QA** (the "what could go wrong") — thinks about edge cases, error conditions, and how to verify

Bringing these perspectives together before coding surfaces ambiguities, missing rules, and edge cases when they're cheapest to fix. The conversation produces concrete examples and acceptance criteria that all three understand. It's not about consensus through documentation written separately, but about shared understanding through dialogue.

The practice is flexible - sometimes more than three people participate (still called Three Amigos informally), and the roles can vary. What matters is cross-functional collaboration and diverse perspectives.

## Sources

- John Ferguson Smart, *BDD in Action: Behavior-Driven Development for the Whole Software Lifecycle*, Manning, 2014.
- Gojko Adzic, *Specification by Example: How Successful Teams Deliver the Right Software*, Manning, 2011. `raw/books/specification_by_example.pdf`
- Chris Matts, "The Three Amigos", various blog posts (origin of the term).
