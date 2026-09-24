---
type: concept
status: draft
tags:
  - testing
  - test-doubles
---

# Types of Test Doubles

[[Test Doubles]] is a collective term. Gerard Meszaros's taxonomy separates five roles that are often blurred together as "mocks". The distinctions matter because each role gives the test different evidence.

## Dummy

A dummy is passed only to satisfy a parameter or constructor requirement. The system under test should not use it for the behavior being exercised. If it is used, the test normally fails or exposes an unintended dependency.

Meszaros calls a dummy a degenerate form of test double, since it is not expected to do anything except exist, and notes that a null is often enough. Where a real object is required for type compatibility, its behavior is still irrelevant, which is what separates a dummy from a Null Object: the latter is used by the system under test but designed to do nothing (pp. 134-135, Dummy Object, p. 728).

## Stub

A stub supplies predetermined answers to calls made during a test. It gives the system under test the indirect inputs needed to reach a particular path. A stub generally does not assert how it was called.

## Spy

A spy is a double that records information about received calls. The test performs assertions on that recorded information after exercising the system, which makes the interaction observable without requiring predeclared expectations. Because those assertions concern interactions rather than final state, a spy belongs with [[Behavior Verification]].

Fowler defines a spy as a stub that also records how it was called, and equates Meszaros's test spy with a stub that uses behavior verification. The sources therefore differ in emphasis: Meszaros lists the spy as one of five distinct roles (Test Spy, p. 538), while Fowler presents it as a stub classified by how the test verifies it. The role table below follows Meszaros's five-role list.

## Mock

A mock is configured with expected interactions and verifies whether they occurred. It is therefore associated with [[Behavior Verification]], rather than solely checking the final result of the system under test.

## Fake

A fake has a working implementation, but uses a shortcut that makes it unsuitable for production. An in-memory implementation of a persistence boundary is a common example. A fake can exercise more realistic collaboration than a canned response, while still differing from the production dependency in important ways.

Meszaros places the fake outside the verification axis altogether: a fake object is neither directly controlled nor observed by the test, and is typically used because the real dependency has not been built yet, is too slow, or is unavailable in the test environment (Fake Object, p. 551).

## Distinguishing the roles

The same helper can sometimes serve more than one role. Classification should follow how it is used in the test:

| Role | Primary contribution to the test | Meszaros pattern |
| --- | --- | --- |
| Dummy | Satisfies an API requirement | Dummy Object, p. 728 |
| Stub | Provides indirect inputs | Test Stub, p. 529 |
| Spy | Makes received interactions observable | Test Spy, p. 538 |
| Mock | Verifies expected interactions | Mock Object, p. 544 |
| Fake | Provides a simplified working implementation | Fake Object, p. 551 |

## Related Concepts

- [[Test Doubles]] — the collective term, and why substitutes are used at all.
- [[Choosing Test Doubles]] — selection guidance for a specific test.
- [[State Verification]] and [[Behavior Verification]] — the separate question of how a test establishes correctness.

## My Understanding

The roles overlap in practice more than the list suggests, because classification follows use rather than implementation. My reading is that a substitute offering a hard-coded answer is a stub even if it is named after a fake, and that a stub becomes a spy only once the test actually asserts what it recorded — a double that records calls nobody asserts is dead instrumentation. This is an interpretation, not a claim taken from the sources.

## Sources

- Martin Fowler, [Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html), 2007. `raw/articles/Mocks Aren't Stubs.md`
- Gerard Meszaros, *xUnit Test Patterns: Refactoring Test Code*, Addison-Wesley, 2007. `raw/books/xUnit Test Patterns Refactoring Test Code-Addison-Wesley (2007).pdf`
