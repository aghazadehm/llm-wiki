---
type: concept
status: draft
tags:
  - testing
  - tdd
aliases:
  - Interaction Testing
---

# Behavior Verification

**Behavior verification** establishes correctness by checking that the system under test interacted with a collaborator as expected. Expectations can include the operation called, arguments, number of calls, and sometimes their order.

For example, a test may verify that an unfulfilled order asks a notification service to send a message. The interaction itself is the evidence of the required behavior.

Meszaros states the pattern's question as how to make tests self-checking when there is no state to verify, and records the alternative name Interaction Testing (Behavior Verification pattern, p. 468).

## Relationship to test doubles

A [[Types of Test Doubles#Mock|mock]] is configured with expectations before the system is exercised and verifies those expectations. A [[Types of Test Doubles#Spy|spy]] also makes interactions observable, but the test normally asserts its recorded calls afterward rather than relying on predeclared interaction expectations. Fowler places the spy in this category directly: he defines spies as stubs that record how they were called, and equates Meszaros's test spy with a stub that uses behavior verification.

Behavior verification is useful when an indirect output matters and does not have a practical state representation for the test to inspect. It is not limited to a particular framework, although frameworks can automate expectation setup and verification.

## Trade-offs

Interaction assertions can specify more than the behavior actually requires. When a test asserts incidental calls, argument details, or ordering, a valid internal refactoring may break the test. Expectations should therefore represent a meaningful collaboration boundary rather than an implementation trace.

Behavior verification complements rather than replaces assertions about outcomes where those outcomes are part of the requirement.

## Related Concepts

- [[State Verification]] — the contrasting approach.
- [[Test Doubles]] and [[Types of Test Doubles]] — the substitutes that make interactions observable.
- [[Classical and Mockist Testing]] — the broader design discussion.

## My Understanding

The failure mode that recurs in these sources is asserting more than the requirement states: argument values, ordering, or call counts that no caller depends on. My reading is that an interaction assertion earns its place only when something outside the system under test would notice if the interaction stopped happening; otherwise the assertion documents the current implementation instead of the required behavior. This is an interpretation, not a claim taken from the sources.

## Sources

- Martin Fowler, [Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html), 2007. `raw/articles/Mocks Aren't Stubs.md`
- Gerard Meszaros, *xUnit Test Patterns: Refactoring Test Code*, Addison-Wesley, 2007. `raw/books/xUnit Test Patterns Refactoring Test Code-Addison-Wesley (2007).pdf`
