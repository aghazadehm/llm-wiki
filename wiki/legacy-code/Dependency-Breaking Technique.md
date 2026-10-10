---
type: concept
status: draft
tags:
  - refactoring
  - testing
aliases:
  - Dependency-Breaking Techniques
---

# Dependency-Breaking Technique

A **dependency-breaking technique** is a small, behavior-preserving edit whose purpose is to make code testable rather than to improve its design. Feathers keeps a catalog of them for code that cannot be instantiated in a test at all, and states the constraint that makes them unusual as refactorings: they are "meant to be done without tests, and they have to be particularly conservative" (p. 312).

## The problem it addresses

The techniques exist for the case where the first step of testing is impossible. A class that builds its own collaborators, or that reaches a database or a global on the way into a method, cannot be called from a test, so no characterization test can be written and nothing can be verified before an edit is made. The technique moves the decision about which collaborator is used to a point the test can reach, which is what [[Seam]] describes in general and what [[Dependency Injection]] often supplies.

Meszaros names the same family from the testing side and gives its purpose: there is a set of "dependency-breaking techniques" — "mostly refactorings" — that can "help you isolate the software for the purpose of automated testing" (p. 832). Koskela frames the obstacle as a modularity gap rather than a design flaw, and argues the effort is repaid: test isolation "can be difficult when working with legacy code that wasn't designed for testability", but "the gain is worth the effort of breaking those nasty dependencies" (p. 23).

## What the catalog contains

Feathers gathers the techniques into the dependency-breaking part of his book (p. 323). Each entry is organised around the obstacle it removes:

- Adapt Parameter — replaces a parameter type that cannot be substituted with one that can (p. 326).
- Extract and Override Call — extracts the call to a troublesome dependency into a method a test subclass can override (p. 348).
- Introduce Static Setter — provides somewhere to install a replacement for a value obtained from a global or a singleton (p. 372).

The entries are deliberately narrow. The aim is to change one dependency at a time so that the result can be checked by inspection, since there is no test yet to catch a mistake.

## Trade-offs

- They break encapsulation, and Feathers records the objection as fair rather than dismissing it: "many of them break encapsulation. That's true. Many of them do" (p. 171). His defence is that encapsulation is valuable for a reason — it helps a team reason about the code — and that losing some of it temporarily buys the ability to test at all.
- They are edits made without a safety net, which is why they must be conservative. Feathers admits the temptation to go further than the obstacle requires: "When I first started using these techniques, it was tempting to do too much" (p. 312).
- They are not an end state. A technique that moves a decision to a reachable point leaves the design with an extra join, and the join is only worth keeping while it carries a test.
- Sometimes no technique in the catalog applies. Feathers records that with singletons, in some languages, "there might not be any way to use Introduce Static Setter (372) or many of the other dependency-breaking techniques", and that wrapping the singleton "is the only choice available" (p. 198).

## When not to apply

- Where the code can already be instantiated and called from a test, since the edit adds a seam nothing needs and would then have to be justified on design grounds instead.
- Where the decision has been taken to [[Refactor or Rewrite|replace the code]], because the effort of making something testable is only repaid if the code is going to be kept.
- Where the technique would change behavior rather than access. These edits are meant to be behavior-preserving, and the absence of tests is exactly the condition that makes an accidental behavior change hard to notice.

## Related Concepts

- [[Legacy Code]] — the situation the catalog was written for.
- [[Characterization Test]] — what the technique makes possible, and the reason it is worth doing without tests.
- [[Seam]] — the general property each technique creates at a specific place.
- [[Dependency Injection]] — one mechanism that supplies a replacement point, which some catalog entries approximate by hand.
- [[Golden Master Test]] — a way to get some coverage when breaking a dependency is not feasible.
- [[Test Doubles]] — what gets installed at the point the technique creates.

## My Understanding

The interesting claim in this material is that a refactoring can be justified without tests. It runs against the usual account, where tests are the precondition for refactoring, and Feathers resolves the tension by making the edits small and mechanical: each one preserves behavior by construction rather than by verification. My reading is that this is where the technique's real cost sits — not in the extra indirection, which is usually modest, but in the discipline the absence of tests demands. A team that treats these edits as ordinary refactoring has removed the only thing keeping them safe, and I notice Feathers flags exactly that temptation rather than assuming the discipline will hold.

## Sources

- Michael Feathers, *Working Effectively with Legacy Code*, Prentice Hall, 2005. `raw/books/Working.Effectively.with.Legacy.Code.pdf`
- Gerard Meszaros, *xUnit Test Patterns: Refactoring Test Code*, Addison-Wesley, 2007. `raw/books/xUnit Test Patterns Refactoring Test Code-Addison-Wesley (2007).pdf`
- Lasse Koskela, *Effective Unit Testing*, Manning, 2013. `raw/books/Effective Unit Testing.pdf`
