---
type: concept
status: draft
tags:
  - testing
  - tdd
---

# Classical and Mockist Testing

**Classical testing** and **mockist testing** are different approaches to choosing collaborators and verification in unit tests. They are often also called Detroit and London styles, respectively, after the C3 project in Detroit and the early XP adopters in London. The labels describe tendencies, not rules that every test must follow, and Fowler notes that some mockist TDD practitioners reject the distinction and any terminology that implies it.

## Classical testing

Classical testing prefers real collaborators when they are practical to use. It introduces a [[Test Doubles|test double]] when a real dependency is awkward, such as an external service. Tests commonly use [[State Verification]] to check results across a small cluster of collaborating objects.

## Mockist testing

Mockist testing more readily replaces collaborators with [[Types of Test Doubles#Mock|mocks]], especially collaborators with meaningful behavior. It relies on [[Behavior Verification]] to specify the interactions that the system under test should have with those collaborators. This can support an outside-in design process in which expectations help define collaboration boundaries.

## Comparison

| Concern | Classical tendency | Mockist tendency |
| --- | --- | --- |
| Collaborators | Use real collaborators when practical | Replace collaborators with mocks more readily |
| Primary evidence | Observable result or state | Expected interactions |
| Test scope | May cover a small group of real objects | Usually isolates the object from its immediate collaborators |
| Refactoring sensitivity | Less tied to internal call structure | Can be sensitive to changed interactions |

Neither style removes the need for broader tests that validate integrations and end-to-end behavior. A team can also use techniques from both styles where the dependency and behavior justify them.

## Related Concepts

- [[Test Doubles]] and [[Types of Test Doubles]] — the substitutes the two styles disagree about using.
- [[State Verification]] and [[Behavior Verification]] — the evidence each style tends to rely on.
- [[Choosing Test Doubles]] — the selection decision in an individual test.

## My Understanding

These are stances about where to put the test boundary rather than competing correctness criteria, and the same codebase can use both where the dependency justifies it. My reading is that the sharpest practical difference is in what a failure tells you: isolated tests localize a fault quickly but can pass while the real collaboration is broken, while tests over real collaborators catch interaction problems but let one faulty collaborator fail many unrelated tests. That is a trade between diagnosis speed and integration coverage, not a question of which camp is right. This is an interpretation, not a claim taken from the sources.

## Sources

- Martin Fowler, [Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html), 2007. `raw/articles/Mocks Aren't Stubs.md`
