---
type: concept
status: draft
---

# Test Doubles

A **test double** is a substitute used in a test in place of a real collaborator of the system under test. The term was introduced by Gerard Meszaros, by analogy with a film stunt double: the substitute stands in for something that is impractical or undesirable to use in that test.

Test doubles help a test control a collaborator's responses, observe effects on that collaborator, or avoid dependencies that are slow, nondeterministic, unavailable, costly, or unsafe to invoke. A double is not automatically preferable to a real collaborator; using one changes both what the test exercises and what it can detect.

## Taxonomy

[[Types of Test Doubles]] distinguishes five commonly used kinds:

- [[Types of Test Doubles#Dummy|Dummy]] objects fill required parameters but are not used by the behavior under test.
- [[Types of Test Doubles#Stub|Stubs]] provide predetermined answers.
- [[Types of Test Doubles#Spy|Spies]] provide answers and record how they were used.
- [[Types of Test Doubles#Mock|Mocks]] specify and verify expected interactions.
- [[Types of Test Doubles#Fake|Fakes]] are simplified working implementations.

The taxonomy describes the role played by a substitute in a test. Terminology varies between teams and frameworks, so an article or test should state the double's observable purpose rather than relying only on a label.

## Verification

Tests using doubles commonly use one or both of these approaches:

- [[State Verification]] checks returned values or observable state after exercising the system.
- [[Behavior Verification]] checks calls made to a collaborator.

A [[Types of Test Doubles#Mock|mock]] is defined by its use of behavior verification, and a [[Types of Test Doubles#Spy|spy]] also uses behavior verification: it records interactions for the test to assert, but the assertions are made after the exercise phase rather than as predeclared expectations. [[Types of Test Doubles#Stub|Stubs]] and [[Types of Test Doubles#Fake|fakes]] supply indirect inputs and resulting state, which supports state verification.

## Related Concepts

- [[Types of Test Doubles]] — the five roles a substitute can play in a test.
- [[Choosing Test Doubles]] — deciding whether a real collaborator or a particular kind of double fits the behavior and the test scope.
- [[State Verification]] and [[Behavior Verification]] — the two ways a test establishes correctness.
- [[Classical and Mockist Testing]] — the broader design philosophies behind recurring choices between real collaborators, doubles, state verification, and behavior verification.

## My Understanding

The taxonomy describes the role a substitute plays in one particular test, not a category a class permanently belongs to; the same helper can be a stub in one test and a spy in another depending on what the test asserts. My reading is that the practical dividing line is the evidence the test needs — a fixed answer, an observable interaction, or a usable working collaborator — and that the labels are shorthand for that need. This is an interpretation, not a claim taken from the sources.

## Sources

- Martin Fowler, [Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html), 2007.
- Gerard Meszaros, *xUnit Test Patterns: Refactoring Test Code*, Addison-Wesley, 2007.
