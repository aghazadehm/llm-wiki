---
type: source
status: draft
title: "Consumer-Driven Contract Testing (CDCT)"
tags:
  - testing
last_updated: 2026-11-01
---

# Consumer-Driven Contract Testing (CDCT)

**"Consumer-Driven Contract Testing (CDCT)"** is a Medium article by Mihriban Kumarci (2024) introducing consumer-driven contract testing in microservices. It defines contracts between consumers and providers, explains why CDCT supports independent development and deployment, and shows concrete examples using Postman and Java/REST Assured style checks to validate responses against expected contracts.

## What it says

The article defines three key terms: **Provider** (service that provides functionality), **Consumer** (component using the provider), and **Contract** (agreement governing interaction - expected behavior, data formats, security requirements). In CDCT, contract tests are often run in the provider's CI pipeline, with responsibility for maintaining contracts and writing contract tests typically falling to the consumer team.

Benefits include: independent development/deployment of provider and consumer (reducing inter-team dependencies), clear visibility into what each consumer needs from the provider, and easier debugging/fixing when contract tests fail.

The article notes contract testing is one piece of a comprehensive testing strategy (complements unit, integration, user acceptance testing). It shows examples of contract validation - using Postman tests with schema validation (tv4) and Java code that reads expected contract JSON files and compares specific fields from actual vs expected responses.

## Related Concepts

- [[Test Doubles]] — contract testing operates at the integration boundary between services, distinct from in-process doubles.
- [[Integration Testing]] — contract testing is positioned as complementary to integration testing, not a replacement.

## My Understanding

The article frames CDCT as a way to prevent breaking changes between services without full end-to-end tests. The key insight is shifting responsibility to consumers to define what they need, with providers verifying they still satisfy all consumer contracts. The examples focus on response validation against contracts rather than the full Pact broker workflow, showing the core idea can be implemented without specific tooling.

## Sources

- Mihriban Kumarci, [Consumer-Driven Contract Testing (CDCT)](https://medium.com/insiderengineering/consumer-driven-contract-testing-cdct-b6c05c18ba25), 2024-03-18. `raw/articles/Consumer-Driven Contract Testing (CDCT).md`
