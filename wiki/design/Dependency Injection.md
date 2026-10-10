---
type: concept
status: draft
tags:
  - design
  - testing
aliases:
  - DI
---

# Dependency Injection

**Dependency injection** supplies an object's collaborators from outside instead of letting the object construct them. Gerard Meszaros states the pattern as a question and an answer: "How do we design the SUT so that we can replace its dependencies at runtime?" — "The client provides the depended-on object to the SUT" (Dependency Injection pattern, p. 678). The emphasis in the sources is not on the wiring being clever but on the consequence: the decision about which implementation to use stops living inside the code that uses it.

## The problem it addresses

The default way to obtain a collaborator is to construct it where it is needed, which binds the class to one concrete type. Meszaros describes the effect as taking a design decision away from the test: dependency injection "is a class of design decoupling in which the client tells the SUT which DOC to use at runtime", and he notes that "the test-driven development (TDD) movement has greatly increased its popularity because Dependency Injection makes for more easily tested designs" (p. 143).

Bender and McWherter give the practitioner's version of the same starting point: "The most obvious way to express and manage these dependencies is to statically create them in code as part of your class's initialization process" (p. 98), and static binding is what prevents components from being tested "in isolation, away from the external resources" (p. 97).

Koskela names the alternative that the absence of injection forces, and rejects it: to substitute a test double in a class that builds its own collaborators, you would have to break encapsulation with visibility modifiers, or use reflection to assign to a private field. "That could turn ugly real soon." His guideline is that dependencies "shouldn't be instantiated in the same place they're used" (p. 43).

## Mechanism

Injection has two parts: the collaborator is referred to by an abstraction, and something other than the using class chooses the concrete type.

- Meszaros's pattern answer assigns the choice to the client: "The client provides the depended-on object to the SUT" (p. 678).
- Bender and McWherter describe what the abstraction buys: "By declaring my member variables as interfaces above, I'm implicitly stating that I don't care what the specific concrete implementation of each service is, I only care that it implements the interface that it's being declared as" — which lets the injector become "the sole storehouse of the rules and logic to determine which concrete instance to use when" (p. 101).

This is where the concept connects to design principles rather than to a tool. Bender and McWherter present dependency inversion as the principle — code "should depend on abstractions, not concrete implementations", with the abstractions not depending "on details; the details should depend on the abstractions" — and then note that "the most common way of doing this, especially for practitioners of TDD in .NET, is the Dependency Injection (DI) pattern" (p. 52). Injection is a way to satisfy a design principle, not a synonym for it; the two share an abbreviation that regularly causes confusion between them.

## Where it fits with seams

Injection is one way to create the object [[Seam]] that a test needs. Meszaros sets out the alternatives explicitly when describing how a test installs a double: "The basic choices boil down to Dependency Injection (page 678), in which the client software tells the SUT which DOC to use; Dependency Lookup (page 686), in which the SUT delegates the construction or retrieval of the DOC to another object; and Test Hook, in which the DOC or the calls to it within the SUT are modified" (p. 143). So injection is one of three mechanisms rather than the only one, and the seam it provides is the enabling point a test acts on.

## Flavours

Meszaros describes the flavours as a matter of taste, and lists three, "each of these three variations ... can be hand-coded" (p. 679):

| Flavour | What it does |
| --- | --- |
| Parameter Injection | The dependency is passed in as an argument of the method being called, and the SUT keeps no reference to it. |
| Constructor Injection | The SUT is told which dependency to use when it is constructed. |
| Setter Injection | The SUT is told about the dependency between construction and use. |

Koskela singles out the middle one as the common case: pass dependencies in "typically using constructor injection" (p. 43). Meszaros records that Parameter Injection "is advocated by the original paper on Mock Objects" and is "especially effective when we are doing true TDD because that's when we have the greatest control over the design" (p. 679).

Two naming cautions follow from the sources available here. Meszaros's third flavour is *Parameter Injection*, not the "method injection" that circulates in other literature — that term, along with setter-side synonyms such as "property injection" and "interface injection", appears nowhere in this repository's sources. And the flavours are described as interchangeable in effect, differing in where the dependency's identity is known, which is a design consequence rather than a matter of correctness.

## Frameworks are optional

The sources agree on this point from different directions, which is worth recording because the opposite assumption is common.

- Koskela adds it as a footnote to the guideline above: "Note that dependency injection doesn't necessarily mean that you must use a dependency injection framework. Simply passing in dependencies through constructors already goes a long way!"
- Meszaros treats a framework as one option: "If an inversion of control framework is available in our language, our tests can substitute dependencies without much additional work on our part. This removes the need for building in the Dependency Injection or Dependency Lookup mechanism" (p. 143), and notes that such a framework "avoids superfluous diversity in how Dependency Injection is implemented across the application" (p. 679).
- Bender and McWherter are framework-positive but conditional: DI frameworks "give developers an alternative to the traditional factory patterns", which become "difficult and time-consuming" to maintain as an application grows (p. 100). Their advice on choosing one is a caution rather than an endorsement: "Keep the framework at a distance. Focus on the Inversion of Control pattern" (p. 289).

The cost of a container is visible in how Bender and McWherter describe it: the configuration becomes "the sole storehouse of the rules and logic to determine which concrete instance to use when" (p. 101), so the benefit and the concentration of that knowledge are the same fact seen twice.

## Related Concepts

- [[Seam]] — the property injection provides; injection is one of several ways to create one.
- [[Test Doubles]] — what gets injected in a test, and why injection is wanted in the first place.
- [[Types of Test Doubles]] — the roles those substitutes play once injected.
- [[Choosing Test Doubles]] — the selection decision, which presupposes that a substitute can be installed.

## My Understanding

Reading these sources together, the disagreement between them is narrower than it looks: all four treat injection as moving the choice of implementation to a place a test can reach, and they differ only in how much machinery that justifies. My reading is that the framework question is a genuine trade rather than a maturity step, because a container converts a set of readable constructor calls into rules held somewhere else — which is exactly the benefit Bender and McWherter claim for it and exactly what Koskela's footnote warns against paying for.

## Sources

- Gerard Meszaros, *xUnit Test Patterns: Refactoring Test Code*, Addison-Wesley, 2007. `raw/books/xUnit Test Patterns Refactoring Test Code-Addison-Wesley (2007).pdf`
- Lasse Koskela, *Effective Unit Testing*, Manning, 2013. `raw/books/Effective Unit Testing.pdf`
- James Bender and Jeff McWherter, *Professional Test-Driven Development with C#*, Wrox, 2011. `raw/books/Test_Driven_Development_With_C#.pdf`
- Michael Feathers, *Working Effectively with Legacy Code*, Prentice Hall, 2005. `raw/books/Working.Effectively.with.Legacy.Code.pdf` — cited for the relationship to [[Seam]]. Note that Feathers never uses the term "dependency injection": it does not appear anywhere in his book, so the two concepts come from different traditions and are not synonymous.
