---
type: index
status: draft
tags:
  - testing
---

# Testing Index

Entry point for the testing domain. It records how a test establishes correctness, which substitutes can stand in for a real collaborator during a test, and how that choice is made. Written articles are listed as links; concepts that do not have an article yet are listed as plain text, so the knowledge map stays visible without linking to pages that do not exist.

## Written articles

- [[Test Doubles]] — a substitute for a real collaborator, and why a test uses one.
- [[Types of Test Doubles]] — the five roles a substitute can play, with their pattern references.
- [[Choosing Test Doubles]] — selecting between a real collaborator and a particular kind of double.
- [[State Verification]] — establishing correctness from an observable result.
- [[Behavior Verification]] — establishing correctness from observed interactions.
- [[Classical and Mockist Testing]] — the two broad stances on collaborators and verification.

## How the articles relate

Foundational, and used by the rest:

- Test Doubles, then Types of Test Doubles, then Choosing Test Doubles: the general idea, its roles, and the selection decision drawn from them.
- State Verification and Behavior Verification are the two ways a test establishes correctness. They are peers, and each contrasts with the other.

Crossing relationships:

- Classical and Mockist Testing takes a position on both axes at once: which collaborators to replace, and which verification style to prefer. Both verification articles and the doubles articles link to it.

## Related material in other domains

These articles are in the design domain and are linked rather than restated here, because the mechanism they describe is a design property that happens to be what testing needs:

- [[Seam]] — the point in a design where a collaborator can be replaced without editing the code under test. The substitutes described here are only installable where a seam already exists.
- [[Dependency Injection]] — how a collaborator reaches the object under test, and therefore where a substitute can be installed.

## Concepts without an article yet

Listed as plain text until they are written, because the rules forbid linking to articles that do not exist:

- Test Data Builder — constructing the input state a test needs without obscuring the values that matter to it.

## Sources

- Martin Fowler, [Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html), 2007. `raw/articles/Mocks Aren't Stubs.md`
- Gerard Meszaros, *xUnit Test Patterns: Refactoring Test Code*, Addison-Wesley, 2007. `raw/books/xUnit Test Patterns Refactoring Test Code-Addison-Wesley (2007).pdf`
