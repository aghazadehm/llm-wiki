---
type: index
status: draft
tags:
  - design
---

# Design Index

Entry point for the design domain. It records the properties of a design that let behavior be changed from outside the code being changed, which is the property tests depend on before any question about substitutes can be answered. Written articles are listed as links; concepts that do not have an article yet are listed as plain text.

## Written articles

- [[Seam]] — a place where behavior can be altered without editing that place, its enabling point, and the object, preprocessing, and link kinds.
- [[Dependency Injection]] — supplying an object's collaborators from outside, the three flavours, and whether a container is needed.

## How the articles relate

- Seam is the general property, from Feathers: behavior can be changed somewhere without editing there. Dependency Injection is one mechanism that provides the object kind of seam, so the injection article links to the seam article and not the reverse. Both can be stated independently, and neither is a prerequisite for reading the other.
- The two are not synonyms, and the sources come from different traditions: Feathers, who defined the seam, never uses the term dependency injection anywhere in his book, so the relationship is that injection supplies what a seam needs rather than that one explains the other.

## Relationship to other domains

- The testing domain assumes this material rather than explaining it. A [[Test Doubles|test double]] has to be installed somewhere, and a seam is where; [[Dependency Injection]] is how the point of installation usually comes to exist. The doubles articles link here for that reason.
- Getting legacy code under test is where the concepts were developed, since retrofitting tests to an existing design usually means finding seams rather than creating them.

## Concepts without an article yet

Listed as plain text until they are written, because the rules forbid linking to articles that do not exist:

- Dependency Inversion Principle — code should depend on abstractions rather than concrete implementations. It shares an abbreviation with dependency injection and is regularly confused with it, though the sources treat the principle and the mechanism as different things.
- Inversion of Control — used in these sources for the framework that resolves dependencies at runtime, and the thing Bender and McWherter advise keeping at a distance. Distinct from the principle above, which is the third meaning of the same phrase.

## Sources

- Michael Feathers, *Working Effectively with Legacy Code*, Prentice Hall, 2005. `raw/books/Working.Effectively.with.Legacy.Code.pdf`
- Gerard Meszaros, *xUnit Test Patterns: Refactoring Test Code*, Addison-Wesley, 2007. `raw/books/xUnit Test Patterns Refactoring Test Code-Addison-Wesley (2007).pdf`
- Lasse Koskela, *Effective Unit Testing*, Manning, 2013. `raw/books/Effective Unit Testing.pdf`
- James Bender and Jeff McWherter, *Professional Test-Driven Development with C#*, Wrox, 2011. `raw/books/Test_Driven_Development_With_C#.pdf`
