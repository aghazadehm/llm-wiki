---
type: index
status: draft
tags:
  - refactoring
---

# Legacy Code Index

Entry point for the legacy-code domain. It covers what makes code hard to change, how to pin down behavior that nobody has written down, and the techniques that make such code testable at all. Articles that exist appear here as links; those still to be written appear as plain text.

## Written articles

The situation and the decisions:

- [[Legacy Code]] — the competing definitions of the term, and why the choice between them changes the remedy.
- [[Characterization Test]] — recording what a system does now, before changing it.
- [[Dependency-Breaking Technique]] — small conservative edits that make code testable before any test exists.
- [[Golden Master Test]] — comparing whole output against a captured baseline, and what that costs.
- [[Refactor or Rewrite]] — deciding whether to improve a system or replace it.

Techniques for changing code that cannot be tested yet:

- [[Sprout Method]] — writing new behavior in a new method called from the old one.
- [[Wrap Method]] — putting new behavior around an existing method, and leaving a seam behind.
- [[Extract and Override Call]] — moving a single call to a method a test subclass can override.
- [[Cover and Modify]] — working beneath a safety net of tests rather than inspecting afterwards.
- [[Pinch Point]] — a narrowing where a few tests can detect changes in many methods.

## How the articles relate

- [[Legacy Code]] is the premise: it states the problem that the rest of the domain answers.
- [[Characterization Test]] is the usual first move once a change is unavoidable, and [[Dependency-Breaking Technique]] is what makes that move possible when the code cannot be instantiated in a test at all.
- The five technique articles are siblings with different costs. [[Sprout Method]] and [[Wrap Method]] add behavior beside or around a method that cannot be tested, [[Extract and Override Call]] removes one dependency at a single call site, and [[Cover and Modify]] names the discipline the others serve.
- [[Pinch Point]] answers where to start when an area has no tests, and [[Golden Master Test]] is the fallback when the smallest observable surface is too coarse to assert against.
- [[Refactor or Rewrite]] is the decision that follows once behavior is pinned down, or the one taken instead of doing so.

## Relationship to other domains

- The design domain supplies the mechanism these techniques assume or produce. [[Seam]] is where a dependency can be replaced without editing the logic being exercised, and [[Dependency Injection]] is how that replacement point usually comes to exist.
- [[Types of Test Doubles]] and [[Test Doubles]] describe what gets installed at a seam, and [[State Verification]] is the assertion style a characterization test usually uses.

## Concepts without an article yet

Recorded as plain text, because a link to a page that does not exist yet would dangle:

- Effect Sketch — a drawing of how a change propagates through a design, since pinch points are narrowings in it.
- Sprout Class — the class-level companion to Sprout Method, for when the source class cannot be instantiated at all.
- Wrap Class — the class-level companion to Wrap Method.
- Replace Global Reference with Getter — the alternative when many calls reach the same global (p. 399).
- Pass Null — passing a null for a parameter the test does not care about (p. 111).
- Lean on the Compiler — using compilation errors to find what a signature change has affected (pp. 315-317).
- Software Vise — the image used for tests that hold behavior in place while it is changed (p. 10).

## Sources

- Michael Feathers, *Working Effectively with Legacy Code*, Prentice Hall, 2005. `raw/books/Working.Effectively.with.Legacy.Code.pdf`
- Gerard Meszaros, *xUnit Test Patterns: Refactoring Test Code*, Addison-Wesley, 2007. `raw/books/xUnit Test Patterns Refactoring Test Code-Addison-Wesley (2007).pdf`
- Lasse Koskela, *Effective Unit Testing*, Manning, 2013. `raw/books/Effective Unit Testing.pdf`
- Masoud Bahrmai, *Refactoring Strategies Guide*, Loan Management System Edition, self-published. `raw/books/Refactoring Strategies Guide.pdf`
