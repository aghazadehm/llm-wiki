---
type: concept
status: draft
tags:
  - refactoring
  - design
aliases:
  - Refactoring versus Rewriting
  - Rewrite or Refactor
---

# Refactor or Rewrite

**Refactor or rewrite** is the decision about whether an existing system should be improved in place or replaced. It is the largest decision in this domain, and the sources available here treat it briefly: the distinction is stated clearly, and the grounds for choosing between the two are not worked out at any length.

## The distinction

Bahrmai frames the choice as the distinction on which everything else depends, and defines the two sides in terms of observable behavior. Refactoring is "a controlled change to the internal structure of software that preserves its externally observable behavior", while a rewrite replaces the system. In his account the practical difference is risk: a refactoring keeps a working system in service and is checked step by step, whereas a rewrite discards that continuity along with the behavior nobody documented (Part 1, Refactoring vs Rewriting).

Feathers reaches the decision from the team's side rather than the code's. He describes the moment when a system becomes "difficult to add new features" to the point of crisis, and people "are charged with the task of figuring out whether it would be better to rearchitect or rewrite the system" (p. 215). He observes that in other organizations "the system limps along for years", because the cost of poor structure is hard to measure: "nobody knows how much better it could be or how much money is being lost because of poor structure" (p. 215).

## The constraint the rest of the domain imposes

Whatever is chosen, the existing behavior has to be knowable before it can be preserved. A refactoring assumes the behavior that must not change is captured somewhere, and a rewrite assumes the behavior worth keeping can be identified in the old system. That is the same precondition as anywhere else in this domain, which is what ties the decision to the rest of these articles: [[Characterization Test]] and [[Golden Master Test]] produce the record, and [[Dependency-Breaking Technique]] is often needed before a record can be produced at all.

## Where the sources are thin

This article states less than the others in the domain, and the gap is worth naming rather than filling. The books here cover the techniques and the decision's precondition, but none of them works through the criteria for choosing: how large a system has to be before a rewrite is the cheaper option, what should happen to a codebase that cannot be brought under test, or how to compare the two costs. The one source that does set out the distinction deliberately — Bahrmai's guide — is self-published, carries no publication date, and has no page numbers, so claims drawn from it are attributed to its author rather than presented as settled. Nothing in the available sources settles the question, and this article does not pretend otherwise.

## Related Concepts

- [[Legacy Code]] — the condition that makes the decision urgent, since code with tests can usually be changed where it stands.
- [[Characterization Test]] — how the behavior a rewrite would have to preserve gets recorded.
- [[Golden Master Test]] — the coarse record used when the surface to preserve is wide.
- [[Dependency-Breaking Technique]] — the way in to code that has to be tested before the decision can be made on evidence.
- [[Seam]] — the property that makes preserving behavior while changing structure possible at all.

## My Understanding

The one thing the sources do establish is the direction of the dependency: this is not a decision to take before the code is under test, because until then neither option can be evaluated. A rewrite judged purely on the state of the existing code is a guess about how much hidden behavior it carries, and the techniques in this domain exist to replace that guess with a record. My reading is that this reframes the question usefully — the work of characterization is not wasted whichever way the decision goes, since a rewrite that preserves recorded behavior still needs the record, so it can be started before the choice is made and it makes the choice better informed.

## Sources

- Michael Feathers, *Working Effectively with Legacy Code*, Prentice Hall, 2005. `raw/books/Working.Effectively.with.Legacy.Code.pdf`
- Masoud Bahrmai, *Refactoring Strategies Guide*, Loan Management System Edition, self-published. `raw/books/Refactoring Strategies Guide.pdf`
