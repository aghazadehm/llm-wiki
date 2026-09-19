---
type: concept
status: draft
---

# Types of Test Doubles

[[Test Doubles]] is a collective term. Gerard Meszaros's taxonomy separates five roles that are often blurred together as “mocks.” The distinctions matter because each role gives the test different evidence.

## Dummy

A dummy is passed only to satisfy a parameter or constructor requirement. The system under test should not use it for the behavior being exercised. If it is used, the test normally fails or exposes an unintended dependency.

## Stub

A stub supplies predetermined answers to calls made during a test. It gives the system under test the indirect inputs needed to reach a particular path. A stub generally does not assert how it was called.

## Spy

A spy is a double that records information about received calls. The test performs assertions on that recorded information after exercising the system, which makes the interaction observable without requiring predeclared expectations. Because those assertions concern interactions rather than final state, a spy belongs with [[Behavior Verification]].

Fowler defines a spy as a stub that also records how it was called, and equates Meszaros's test spy with a stub that uses behavior verification. The sources therefore differ in emphasis: Meszaros lists the spy as one of five distinct roles, while Fowler presents it as a stub classified by how the test verifies it. The role table below follows Meszaros's five-role list.

## Mock

A mock is configured with expected interactions and verifies whether they occurred. It is therefore associated with [[Behavior Verification]], rather than solely checking the final result of the system under test.

## Fake

A fake has a working implementation, but uses a shortcut that makes it unsuitable for production. An in-memory implementation of a persistence boundary is a common example. A fake can exercise more realistic collaboration than a canned response, while still differing from the production dependency in important ways.

## Distinguishing the roles

The same helper can sometimes serve more than one role. Classification should follow how it is used in the test:

| Role | Primary contribution to the test |
| --- | --- |
| Dummy | Satisfies an API requirement |
| Stub | Provides indirect inputs |
| Spy | Makes received interactions observable |
| Mock | Verifies expected interactions |
| Fake | Provides a simplified working implementation |

## Related Concepts

- [[Test Doubles]] — the collective term, and why substitutes are used at all.
- [[Choosing Test Doubles]] — selection guidance for a specific test.
- [[State Verification]] and [[Behavior Verification]] — the separate question of how a test establishes correctness.

## My Understanding

The roles overlap in practice more than the list suggests, because classification follows use rather than implementation. My reading is that a substitute offering a hard-coded answer is a stub even if it is named after a fake, and that a stub becomes a spy only once the test actually asserts what it recorded — a double that records calls nobody asserts is dead instrumentation. This is an interpretation, not a claim taken from the sources.

## Sources

- Martin Fowler, [Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html), 2007.
- Gerard Meszaros, *xUnit Test Patterns: Refactoring Test Code*, Addison-Wesley, 2007.
