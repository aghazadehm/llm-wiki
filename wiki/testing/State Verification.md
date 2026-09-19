---
type: concept
status: draft
---

# State Verification

**State verification** establishes correctness by checking the observable result after the system under test has been exercised. The result may be a return value, a visible state change, or another observable outcome exposed by the system or a collaborator.

For example, a test can call an operation and assert that an order is marked as fulfilled and that its inventory is reduced. The test checks the outcome, not the sequence of calls used to produce it.

## Relationship to test doubles

[[Types of Test Doubles#Stub|Stubs]] can supply indirect inputs required to produce an outcome. [[Types of Test Doubles#Fake|Fakes]] can provide a usable collaborator whose resulting state is inspected. These uses contrast with a [[Types of Test Doubles#Mock|mock]], which is defined by [[Behavior Verification]], and with a [[Types of Test Doubles#Spy|spy]], whose recorded calls are also interaction evidence: the assertions are made after the exercise phase instead of as predeclared expectations, but they still concern calls rather than resulting state.

State verification is compatible with tests using real collaborators, provided those collaborators are practical and their state is observable within the intended test scope.

## Trade-offs

State verification tends to focus a test on externally observable results, which can make implementation refactoring less likely to require test changes. It may be a poor fit when the important outcome is an interaction that has no useful final state to inspect, such as deciding whether a cache was consulted or whether a message was sent.

The verification method alone does not determine the test level or quality. The test must still have a clear behavioral purpose and appropriate collaborators.

## Related Concepts

- [[Behavior Verification]] — the contrasting approach.
- [[Test Doubles]] and [[Types of Test Doubles]] — the substitutes discussed above.
- [[Classical and Mockist Testing]] — the broader design discussion.

## My Understanding

What makes state verification durable is that the assertion usually names something a caller of the system could also observe, so internal restructuring does not invalidate it. My reading is that its real limit is not that state is unavailable but that some requirements are about an interaction — a cache being consulted, a message being sent, an audit entry being written — and forcing those into state assertions makes the test read bookkeeping the requirement never mentions. This is an interpretation, not a claim taken from the sources.

## Sources

- Martin Fowler, [Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html), 2007.
- Gerard Meszaros, *xUnit Test Patterns: Refactoring Test Code*, Addison-Wesley, 2007.
