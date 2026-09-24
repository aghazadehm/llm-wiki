---
type: concept
status: draft
tags:
  - testing
  - test-doubles
aliases:
  - Test Double
---

# Test Doubles

A **test double** is a substitute used in a test in place of a real collaborator of the system under test. Gerard Meszaros, who coined the term, defines it as "any object or component that we install in place of the real component for the express purpose of running a test" (Test Double pattern, p. 133), and introduces the pattern with the film stunt-double analogy the name refers to (p. 523).

Test doubles help a test control a collaborator's responses, observe effects on that collaborator, or avoid dependencies that are slow, nondeterministic, unavailable, costly, or unsafe to invoke. A double is not automatically preferable to a real collaborator; using one changes both what the test exercises and what it can detect.

Installing a double requires a [[Seam]] in the design: a place where behavior can be changed without editing the code being tested. [[Dependency Injection]] is the usual way that seam comes to exist, which is why the two concepts are prerequisites for this one rather than alternatives to it.

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

A [[Types of Test Doubles#Mock|mock]] is defined by its use of behavior verification, and a [[Types of Test Doubles#Spy|spy]] also uses behavior verification: it records interactions for the test to assert, but the assertions are made after the exercise phase rather than as predeclared expectations. A [[Types of Test Doubles#Stub|stub]] can support either style, since what the test asserts about it is the test's own decision, and a [[Types of Test Doubles#Fake|fake]] provides a working collaborator whose resulting state the test can inspect.

Meszaros divides the same doubles along a different axis than this state-versus-behavior one: a test stub is used to control the indirect *inputs* of the system under test, while a test spy or a mock object is used to verify its indirect *outputs*, and a fake object is "neither directly controlled nor observed by the test" (Figure 11.8, p. 134; Fake Object, p. 551).

## Related Concepts

- [[Types of Test Doubles]] — the five roles a substitute can play in a test.
- [[Choosing Test Doubles]] — deciding whether a real collaborator or a particular kind of double fits the behavior and the test scope.
- [[State Verification]] and [[Behavior Verification]] — the two ways a test establishes correctness.
- [[Classical and Mockist Testing]] — the broader design philosophies behind recurring choices between real collaborators, doubles, state verification, and behavior verification.
- [[Seam]] — the property a design needs before a substitute can be installed at all.
- [[Dependency Injection]] — the mechanism that normally provides that property.

## My Understanding

The taxonomy describes the role a substitute plays in one particular test, not a category a class permanently belongs to; the same helper can be a stub in one test and a spy in another depending on what the test asserts. My reading is that the practical dividing line is the evidence the test needs — a fixed answer, an observable interaction, or a usable working collaborator — and that the labels are shorthand for that need. This is an interpretation, not a claim taken from the sources.

## Sources

- Martin Fowler, [Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html), 2007. `raw/articles/Mocks Aren't Stubs.md`
- Gerard Meszaros, *xUnit Test Patterns: Refactoring Test Code*, Addison-Wesley, 2007. `raw/books/xUnit Test Patterns Refactoring Test Code-Addison-Wesley (2007).pdf`
