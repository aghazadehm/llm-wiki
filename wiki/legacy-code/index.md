---
type: index
status: draft
tags:
  - refactoring
---

# Legacy Code Index

Entry point for the legacy-code domain. It covers what makes code hard to change, how to pin down behavior that nobody has written down, and the techniques that make such code testable at all. Articles that exist appear here as links; those still to be written appear as plain text.

## Written articles

- [[Legacy Code]] — the competing definitions of the term, and why the choice between them changes the remedy.
- [[Characterization Test]] — recording what a system does now, before changing it.
- [[Dependency-Breaking Technique]] — small conservative edits that make code testable before any test exists.
- [[Golden Master Test]] — comparing whole output against a captured baseline, and what that costs.
- [[Refactor or Rewrite]] — deciding whether to improve a system or replace it.

## How the articles relate

- [[Legacy Code]] is the premise: it states the problem that the rest of the domain answers.
- [[Characterization Test]] is the usual first move once a change is unavoidable. [[Dependency-Breaking Technique]] is what makes that move possible when the code cannot be instantiated in a test at all, so the two are used in either order rather than one after the other.
- [[Golden Master Test]] is the alternative when the smallest available interface is too coarse to assert against, and it is the one technique here that the sources disagree about.
- [[Refactor or Rewrite]] is the decision that follows once behavior is pinned down, or the one taken instead of doing so.

## Relationship to other domains

- The design domain supplies the mechanism this domain assumes. A [[Seam]] is where a dependency can be replaced without editing the logic being exercised, and [[Dependency Injection]] is how that replacement point usually comes to exist, so the articles here link there instead of explaining it again.
- [[Test Doubles]] are what gets installed at a seam when a characterization test has to avoid a real collaborator.

## Concepts without an article yet

Recorded as plain text, because a link to a page that does not exist yet would dangle:

- Cover and Modify — Feathers' name for putting code under test before changing it, contrasted with what he calls Edit and Pray (p. 9).
- Pinch Point — a narrow place where a design change can be judged, used together with effect sketches (p. 183).
- Effect Sketch — marking how a change propagates through a design, in order to find natural break points.
- Sprout Method — adding new behavior in a new method rather than editing the existing one (pp. 59-67).
- Wrap Method — renaming the method that exists and adding behavior around the call.
- Extract and Override Call — the catalog entry for introducing a replacement point at a call site (p. 348).

## Sources

- Michael Feathers, *Working Effectively with Legacy Code*, Prentice Hall, 2005. `raw/books/Working.Effectively.with.Legacy.Code.pdf`
- Gerard Meszaros, *xUnit Test Patterns: Refactoring Test Code*, Addison-Wesley, 2007. `raw/books/xUnit Test Patterns Refactoring Test Code-Addison-Wesley (2007).pdf`
- Lasse Koskela, *Effective Unit Testing*, Manning, 2013. `raw/books/Effective Unit Testing.pdf`
- Masoud Bahrmai, *Refactoring Strategies Guide*, Loan Management System Edition, self-published. `raw/books/Refactoring Strategies Guide.pdf`
