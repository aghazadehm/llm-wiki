---
type: concept
status: draft
tags:
  - process
  - testing
---

# Specification by Example

Specification by Example (SBE) is an approach where requirements and business-oriented functional tests are expressed as examples. Rather than writing abstract specifications, teams collaborate to create concrete examples that illustrate desired behavior, using them as both specification and acceptance tests to create living documentation.

## Related Concepts

- [[Behavior-Driven Development]] — BDD is closely related to SBE; both use examples as specifications.
- [[Example Mapping]] — a discovery technique that produces examples for SBE.
- [[Three Amigos]] — collaboration pattern essential to creating good examples.

## My Understanding

Gojko Adzic's book synthesizes practices from teams successfully using this approach. Key practices include:
- **Derive scope from goals** — Start from business goals (relates to impact mapping)
- **Specify collaboratively** — Business and development collaborate to find examples
- **Illustrate with examples** — Use concrete examples rather than abstract rules
- **Refine the specification** — Examples evolve as understanding deepens
- **Automate validation** — Turn examples into executable tests
- **Evolve living documentation** — Keep specs in sync with implementation

The power of SBE is that examples are unambiguous. "The cart total is $10" is clearer than "apply appropriate discounts". Examples also become tests, so the specification never drifts from reality. And when written in accessible language, they serve as documentation for everyone.

SBE shifts the focus from "writing requirements" to "discovering and specifying through examples together". The specification emerges from collaboration, not from someone writing it in isolation.

## Sources

- Gojko Adzic, *Specification by Example: How Successful Teams Deliver the Right Software*, Manning, 2011. `raw/books/specification_by_example.pdf`
- Gojko Adzic, *Bridging the Communication Gap: Specification by Example and Agile Acceptance Testing*, Neuri Limited, 2009.
- John Ferguson Smart, *BDD in Action*, Manning, 2014.
- Matt Wynne & Aslak Hellesøy, *The Cucumber Book*, Pragmatic Bookshelf, 2012.
