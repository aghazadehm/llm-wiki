---
type: concept
status: draft
tags:
  - testing
aliases:
  - Integration Tests
---

# Integration Testing

**Integration testing** verifies that multiple components work together correctly when combined, checking interactions between modules, services, or external dependencies rather than testing units in isolation.

## Problem it addresses

Unit tests with [[Test Doubles]] isolate behavior but cannot catch issues in component boundaries: mismatched assumptions, incorrect wiring, serialization/deserialization problems, or failures in how components collaborate. Integration testing validates these real interactions.

## How it works

Integration tests exercise combinations of real components (or a mix of real and substituted components) to verify they communicate correctly. The scope can vary - from testing two modules together to testing against real databases, message queues, or external services. The key is verifying collaboration between components rather than internal logic of a single unit.

## Trade-offs

- **Confidence**: Catches boundary bugs that unit tests miss.
- **Speed/cost**: Slower and more complex to set up than unit tests; often requires more infrastructure.
- **Isolation**: Harder to pinpoint failures compared to focused unit tests.
- **Flakiness**: External dependencies can introduce non-determinism.

## When not to apply

- As a substitute for unit tests - integration tests are coarser and slower.
- When boundaries are unstable - changes break many integration tests.
- For testing every permutation - prefer focused tests at appropriate levels.

## Related Concepts

- [[Test Doubles]] — used to control scope in integration tests when some collaborators are expensive/unavailable.
- [[State Verification]] — often used to check outcomes across integrated components.
- [[Behavior Verification]] — used to verify interactions between integrated components.
- [[Consumer-Driven Contract Testing (CDCT)]] — a form of integration testing focused on verifying contracts between consumers and providers.

## My Understanding

Integration testing sits between unit and end-to-end testing. The challenge is choosing the right scope - too narrow misses boundary issues, too broad makes failures hard to diagnose. Contract testing offers a middle ground for service boundaries by verifying expectations without full system integration.

## Sources

- Martin Fowler, [IntegrationTest](https://martinfowler.com/bliki/IntegrationTest.html). `raw/articles/` (referenced conceptually)
- Gerard Meszaros, *xUnit Test Patterns: Refactoring Test Code*, Addison-Wesley, 2007. `raw/books/xUnit Test Patterns Refactoring Test Code-Addison-Wesley (2007).pdf`
