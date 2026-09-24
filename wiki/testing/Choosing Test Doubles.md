---
type: concept
status: draft
tags:
  - testing
  - test-doubles
---

# Choosing Test Doubles

Choose a [[Test Doubles|test double]] based on the behavior the test needs to establish, the collaborator's characteristics, and the evidence required to verify the behavior. A double is a means to define a useful test boundary, not a default replacement for every dependency.

## Selection guide

The links below escape their alias pipe as `\|`, because a raw `|` inside a table row is read as a cell separator. That is a Markdown constraint and not part of the concept.

| Need in the test | Suitable choice |
| --- | --- |
| A required argument is irrelevant to the scenario | [[Types of Test Doubles#Dummy\|Dummy]] |
| The system needs a controlled answer from a collaborator | [[Types of Test Doubles#Stub\|Stub]] |
| The test must inspect information received by a collaborator | [[Types of Test Doubles#Spy\|Spy]] |
| The required behavior is an explicit collaboration | [[Types of Test Doubles#Mock\|Mock]] with [[Behavior Verification]] |
| A usable but simplified implementation supports the scenario | [[Types of Test Doubles#Fake\|Fake]] |
| A real collaborator is practical and appropriate to the test scope | Use the real collaborator, often with [[State Verification]] |

## Questions to ask

1. What behavior is under test, and what observable evidence would establish it?
2. Does the collaborator make the test slow, nondeterministic, unsafe, unavailable, or difficult to configure?
3. Is the requirement about the outcome, the interaction, or both?
4. Would asserting this interaction describe a stable contract, or merely reproduce the current implementation?
5. What important differences remain between a fake or stub and the production collaborator?

## Risks and trade-offs

Replacing a collaborator can improve control and isolation, but it can also omit behavior that would occur in production. Fakes may differ from the production system in semantics or failure behavior. Stubs and mocks can let tests pass despite an incorrect real integration. Detailed mock expectations can couple tests to implementation and make refactoring noisy.

Conversely, always using real collaborators can make tests slow, fragile, difficult to set up, or dependent on external state. The appropriate choice is contextual and should be supported by tests at other scopes where integration behavior matters.

## Related Concepts

- [[Test Doubles]] and [[Types of Test Doubles]] — the substitutes being chosen between.
- [[State Verification]] and [[Behavior Verification]] — the evidence each choice produces.
- [[Classical and Mockist Testing]] — the broader philosophies behind recurring choices between real collaborators, doubles, state verification, and behavior verification.

## My Understanding

This guide is only as good as the collaborator's contract, since a double that permits a call production would reject gives false confidence. My reading is that the most defensible default is the least capable substitute that still lets the test express its requirement — a dummy before a stub, a stub before a fake, and a real collaborator before any of them when it is practical — because each step toward a more elaborate double adds behavior the test now depends on and that production may not share. This is an interpretation, not a claim taken from the sources.

## Sources

- Martin Fowler, [Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html), 2007. `raw/articles/Mocks Aren't Stubs.md`
- Gerard Meszaros, *xUnit Test Patterns: Refactoring Test Code*, Addison-Wesley, 2007. `raw/books/xUnit Test Patterns Refactoring Test Code-Addison-Wesley (2007).pdf`
