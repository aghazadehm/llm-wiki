---
type: index
status: draft
tags:
  - process
---

# Discovery Index

Entry point for the discovery domain. It covers outcome-focused discovery, visual planning techniques, collaborative specification, and the principles that connect business goals to testable requirements. Written articles are listed as links; concepts that do not have an article yet are listed as plain text.

## Written articles

- [[Impact Mapping]] — goal-driven planning connecting business goals to actors, impacts, and deliverables (Gojko Adzic).
- [[User Story Mapping]] — organizing user stories by journey activities and tasks to slice releases by value (Jeff Patton).
- [[Example Mapping]] — collaborative discovery technique for breaking down rules, examples, questions, and assumptions (Matt Wynne / Seb Rose).
- [[EventStorming]] — workshop for discovering domain events and complex processes through collaborative modeling (Alberto Brandolini).
- [[Three Amigos]] — cross-functional collaboration pattern (business, development, testing) for shared understanding.
- [[Outcome Over Output]] — underlying principle of focusing on measurable impacts rather than delivered features.
- [[Feature Injection]] — ensuring features trace to business value and desired outcomes (Chris Matts / Gojko Adzic).
- [[Outside-In Development]] — starting from user needs and desired outcomes, working inward to implementation.
- [[Behavior-Driven Development]] — discovery, formulation, and automation cycle for collaborative specification (Dan North et al., refined by Wynne/Rose/Nagy).
- [[Specification by Example]] — concrete examples as specification and tests, creating living documentation (Gojko Adzic).

## How the articles relate

- **Strategy first**: [[Impact Mapping]] sets the "why" by tracing deliverables to measurable business goals. It prevents building features with no clear impact.
- **Tactical organization**: Take high-priority deliverables from impact maps and use [[User Story Mapping]] to organize them along the user journey, identify gaps, and slice horizontal releases.
- **Collaborative discovery**: [[Example Mapping]] and [[Three Amigos]] help refine stories/requirements through conversation. [[EventStorming]] helps explore complex domains and discover events/processes at a larger scale.
- **Concrete specification**: [[Specification by Example]] and [[Behavior-Driven Development]] turn discovered requirements into concrete examples that become executable specifications and living documentation.
- **Principles underpin all**: [[Outcome Over Output]], [[Feature Injection]], and [[Outside-In Development]] provide the mindset that keeps all techniques focused on delivering value.

## Relationship to other domains

- **Design**: Discovery ensures we're solving the right problem before worrying about testability. The right scope matters as much as having seams for testing.
- **Testing**: BDD and Specification by Example feed directly into [[Test Doubles]] and testing strategy. Concrete examples become acceptance criteria/tests.
- **Legacy Code**: Discovery techniques help understand unclear requirements and desired behavior in legacy systems where requirements may be implicit or lost.

## Concepts without an article yet

Kept as plain text rather than links, since a link to an article that does not exist yet would dangle:

- **Domain Storytelling** — pictographic domain modeling technique (Stefan Hofer & Henning Schwentner). Often used alongside or instead of EventStorming.
- **Deliberate Discovery** — Gojko Adzic's approach to reducing uncertainty through targeted exploration and experiments.
- **Real Options** — delaying commitment until more information is available, maximizing optionality (Chris Matts & Olav Maassen).
- **Ubiquitous Language** — shared vocabulary between domain experts and developers (Eric Evans, Domain-Driven Design).
- **Living Documentation** — documentation that stays in sync with code because it's generated from executable specifications.

## Sources

- Gojko Adzic, *Impact Mapping: Making a Big Impact with Software Products and Projects*, Provoking Thoughts, 2012. `raw/books/Impact_Mapping_-_Gojko_Adzic.pdf`
- Jeff Patton with Peter Economy, *User Story Mapping: Discover the Whole Story, Build the Right Product*, O'Reilly, 2014. `raw/books/User_Story_Mapping_-_Jeff_Patton_Peter_Economy_Editor.pdf`
- Gojko Adzic, *Specification by Example: How Successful Teams Deliver the Right Software*, Manning, 2011. `raw/books/specification_by_example.pdf`
- John Ferguson Smart, *BDD in Action: Behavior-Driven Development for the Whole Software Lifecycle*, Manning, 2014. (Referenced; book added to collection)
- Matt Wynne & Aslak Hellesøy, *The Cucumber Book: Behaviour-Driven Development for Testers and Developers*, Pragmatic Bookshelf, 2012.
- Alberto Brandolini, *Introducing EventStorming*, Leanpub (various editions).
- Seb Rose & Gaspar Nagy, *BDD Books: Discovery*, Leanpub, 2018.
- Chris Matts & Gojko Adzic, *Feature Injection: three steps to success*, various publications.
- Mary Poppendieck & Tom Poppendieck, *Lean Software Development: An Agile Toolkit*, Addison-Wesley, 2003.
- Donald G. Reinertsen, *The Principles of Product Development Flow: Second Generation Lean Product Development*, Celeritas Publishing, 2009.
