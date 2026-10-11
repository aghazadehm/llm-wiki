---
type: synthesis
status: draft
title: "When a Stub Is Really a Mock"
question: "How do you tell a stub from a mock once the test is verifying behavior?"
tags:
  - testing
  - test-doubles
related:
  - State Verification.md
  - Behavior Verification.md
  - Choosing Test Doubles.md
  - Classical and Mockist Testing.md
sources:
  - Mocks Aren't Stubs.md
last_updated: 2026-10-11
---

# When a Stub Is Really a Mock

A reader who meets a test that programs a collaborator with an expectation and then checks how the SUT used it will often not know which of the five doubles is on the screen — because a stub and a mock can both be used that way. The answer the vault works out from its testing articles is that the distinction is not visible in how the double is *used*, but in what the double is *for*.

## The working distinction

[[State Verification]] and [[Behavior Verification]] are two ways to check a test, and either can be built on top of either kind of double. A [[Test Doubles|stub]] is defined by its purpose — it returns canned answers so the SUT has something sensible to work against — and nothing about that purpose forces a verification style. When a stub additionally records how it was called so a test can check it, Meszaros gives it a different name: a spy. A [[Behavior Verification|mock]] is defined by its purpose in the opposite direction: it is a specification of the calls the SUT is expected to make, so behavior verification is not one option among several for a mock, it is what the double *is*.

The two articles in this vault's testing domain keep the verification style and the double kind as separate concepts precisely so this question can be answered cleanly: the style of a test is a property of the assertion, the kind of double is a property of the collaborator, and the two are joined by a convention, not an identity.

## Where it changes the design

The consequence the [[Mocks Aren't Stubs|source article]] draws is the one that matters in practice. If the choice were only state versus behavior verification, it would be, as Fowler puts it, "mostly not a big decision," and the double could go either way. The choice with weight is the classical-versus-mockist one, because that one fixes the design: a mockist test reaches for a mock at the seam and gets an outside-in shape from it, while a classical test reaches for a real collaborator or a stub and stays middle-out. The double is a symptom of the style, not the style itself.

## Related Concepts

- [[State Verification]] — the assertion style a stub most naturally serves.
- [[Behavior Verification]] — the assertion style a mock is built to serve, and the one a spy reaches for when it needs it.
- [[Choosing Test Doubles]] — the decision this synthesis is about, from the test's side.
- [[Classical and Mockist Testing]] — the design divide the double choice reveals.

## My Understanding

The naming is the trap. "Mock" has drifted into meaning "any fake collaborator" in common usage, which is exactly the confusion Fowler's title names, and it makes the spy almost redundant: once a stub is doing the mock's job, the only thing keeping the categories apart is a name. I read the vault as keeping Meszaros's vocabulary deliberately, because the moment "mock" and "stub" are used interchangeably, the classical-versus-mockist distinction loses its foothold — the style is signaled by which double reaches for which collaborator, and if the doubles are the same word, the style is just an adjective.

## Sources

- Martin Fowler, [Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html), 2007. `raw/articles/Mocks Aren't Stubs.md`
- Gerard Meszaros, *xUnit Test Patterns: Refactoring Test Code*, Addison-Wesley, 2007. `raw/books/xUnit Test Patterns Refactoring Test Code-Addison-Wesley (2007).pdf`
