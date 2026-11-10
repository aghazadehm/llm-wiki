---
type: concept
status: draft
tags:
  - testing
aliases:
  - CDC Testing
  - Consumer Driven Contract Testing
---

# Consumer-Driven Contract Testing

**Consumer-Driven Contract Testing (CDCT)** is a testing approach where consumers define the contracts they expect from providers, and providers verify they can satisfy those contracts. It ensures compatibility between services without requiring exhaustive end-to-end integration tests.

## Problem it addresses

In microservices architectures, services are developed and deployed independently by different teams. Traditional integration tests require all services running together, creating tight coupling, slow feedback cycles, and coordination overhead. CDCT enables independent development while preventing breaking changes at service boundaries.

## How it works

1. **Consumer defines contract**: The consuming service specifies what it expects from the provider (endpoints, request/response formats, required fields, etc.).
2. **Contract shared/stored**: Contracts are published (often via a broker like Pact) or shared with the provider team.
3. **Provider verifies contract**: The provider runs contract tests against its implementation to ensure it meets all consumer expectations.
4. **Continuous verification**: Contract tests run in CI pipelines, catching breaking changes before deployment.

Key roles (as defined by the source): **Provider** (service providing functionality), **Consumer** (service/client using the provider), **Contract** (agreement specifying expected behavior, data formats, security requirements).

## Trade-offs

- **Benefits**: Supports independent development/deployment, makes consumer needs explicit, easier to debug contract failures, faster feedback than full E2E tests.
- **Costs**: Requires discipline in contract management, adds tooling/process complexity, contracts need versioning/evolution strategy.
- **Scope**: Tests the contract/communication boundary, not business logic end-to-end or full system behavior.

## When not to apply

- Monolithic applications with no service boundaries.
- When you need to test complex workflows across many services together.
- As a replacement for unit tests or all integration testing - it's complementary.

## Related Concepts

- [[Integration Testing]] — CDCT is a form of integration testing focused on service boundaries and contracts.
- [[Test Doubles]] — in unit tests within a service, doubles may simulate contracts; CDCT verifies real contract compliance.
- [[State Verification]] — contract tests verify response state/structure matches expectations.
- [[Behavior Verification]] — can verify specific interactions/calls match contract expectations.

## My Understanding

CDCT shifts the responsibility for defining compatibility to consumers - they declare what they actually need rather than providers guessing. This makes dependencies explicit and prevents over-engineering providers for unused capabilities. The approach is most valuable in distributed systems with multiple teams where coordination is expensive. Examples show it can be implemented with schema validation (like JSON Schema/tv4) or specialized tools like Pact.

## Sources

- Mihriban Kumarci, [Consumer-Driven Contract Testing (CDCT)](https://medium.com/insiderengineering/consumer-driven-contract-testing-cdct-b6c05c18ba25), 2024-03-18. `raw/articles/Consumer-Driven Contract Testing (CDCT).md`
- [Pact Documentation](https://docs.pact.io/) (referenced)
- [PactFlow - Contract Testing vs Integration Testing](https://pactflow.io/blog/contract-testing-vs-integration-testing/) (referenced)
