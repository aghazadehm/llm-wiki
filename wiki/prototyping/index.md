---
type: index
status: draft
tags:
  - design
  - process
---

# Prototyping Index

Entry point for the prototyping domain. It covers how designers use representations of a design idea to ask and answer questions before the product exists: what a prototype is, which questions it can be built to explore, what it filters and how it manifests it, how much detail it should carry, how prototyping fits a development process, and how prototypes mediate communication. Written articles are listed as links; concepts without an article yet are listed as plain text.

## Written articles

- [[Prototype]] — the broad definition, the prototype/product distinction, and the failure modes of building one.
- [[Prototype Purpose Model]] — Houde and Hill's role, look-and-feel, and implementation triangle, and the integration prototypes at its centre.
- [[Anatomy of Prototypes]] — Lim, Stolterman, and Tenenberg's filtering and manifestation dimensions, with the two case studies behind them.
- [[Prototype Fidelity]] — resolution, scope, and material as separate decisions, and why finish is read as completeness.
- [[Approaches to Prototyping]] — Floyd's exploratory, experimental, and evolutionary approaches and their trade-offs.
- [[Prototype as Communication Medium]] — Erickson's audiences and stages, vision and working prototypes, accessibility, and roughness.

## How the articles relate

- [[Prototype]] is the foundation: it fixes the vocabulary the rest of the domain uses and refuses to define a prototype by its medium.
- [[Prototype Purpose Model]] answers "which question is this prototype for?", while [[Anatomy of Prototypes]] answers "what does it include, and how is that made concrete?". The second is finer-grained and was proposed later; the first is easier to explain to a non-specialist audience.
- [[Prototype Fidelity]] isolates one attribute that both frameworks treat as secondary: how much detail, how much scope, and in what material. It depends on the anatomy for the distinction between resolution and scope.
- [[Approaches to Prototyping]] places prototypes in a development process, so it answers "why build one now?" rather than "what should it contain?".
- [[Prototype as Communication Medium]] answers "who is it for?", and it explains why the same prototype can succeed with one audience and fail with another.

## Relationship to other domains

- The `discovery` domain frames the problem before prototyping starts: [[Impact Mapping]] and [[User Story Mapping]] decide what is worth building, and [[Specification by Example]] turns examples into a shared specification. A prototype is one way to make those decisions concrete.
- The `design` domain is about code-level properties that make behavior changeable, such as [[Seam]] and [[Dependency Injection]]. Prototyping is artifact-level and happens earlier; the two meet when an implementation prototype is used to test a technical design.
- The `testing` domain asks whether a system behaves correctly. A prototype is not a test: it is built to explore a question, and its evaluation is usually qualitative and formative, as [[Approaches to Prototyping]] describes.

## Concepts without an article yet

Recorded as plain text so the map stays visible without linking to pages that do not exist:

- Wizard of Oz Prototype — a hidden operator simulates a system behavior that is difficult to implement, so users can respond to the behavior before it exists. Houde and Hill describe it as the "man behind the curtain" technique (p. 10).
- Prototype Profile — Lim et al.'s record of the filtering dimensions and manifestation values a prototype uses. It is currently a section of [[Anatomy of Prototypes]].
- Roughness — Erickson's property of working prototypes: relaxed conventions or visible process, which creates ambiguity and invites critique. It is currently a section of [[Prototype as Communication Medium]].
- Mixed-Fidelity Prototype — a prototype that combines low and high fidelity on different dimensions, cited by Lim et al. (p. 7:5).
- Evolutionary Development — Floyd's version-based development, distinct from incremental development within one design.

## Sources

- Stephanie Houde and Charles Hill, "What Do Prototypes Prototype?", in *Handbook of Human-Computer Interaction* (2nd ed.), Elsevier, 1997, pp. 1-16. `raw/books/prototypes/What_Do_Prototypes_Prototype_Stephanie_Houde_&_Charles_Hill_1997.pdf`
- Youn-Kyung Lim, Erik Stolterman, and Josh Tenenberg, "The Anatomy of Prototypes: Prototypes as Filters, Prototypes as Manifestations of Design Ideas", *ACM Transactions on Computer-Human Interaction* 15(2), Article 7, 2008. `raw/books/prototypes/The_Anatomy_of_Prototypes_Youn_Kyung_Lim,_Erik_Stolterman_&_Josh.pdf`
- Christiane Floyd, "A Systematic Look at Prototyping", in *Approaches to Prototyping*, Springer, 1984, pp. 1-18. `raw/books/prototypes/A Systematic Look at Prototyping - Christiane Floyd (1984).pdf`
- Thomas Erickson, "Notes on Design Practice: Stories and Prototypes as Catalysts for Communication", in *Scenario-Based Design*, Wiley, 1995. `raw/books/prototypes/Stories_and_Prototypes_as_Catalysts_for_Communication_Thomas_Erickson.pdf`
