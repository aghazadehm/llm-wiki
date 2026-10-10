---
type: concept
status: draft
tags:
  - design
  - testing
aliases:
  - Pinch Points
---

# Pinch Point

A **pinch point** is a place in a design where a small number of tests can detect changes made in many places. Feathers defines it as a property of the effects a change has rather than of the code itself: "A pinch point is a narrowing in an effect sketch, a place where tests against a couple of methods can detect changes in many methods" (p. 181).

## The problem it addresses

Testing a large area of code that has no tests raises a question of where to start, and the answer decides how much the first tests are worth. Written at an arbitrary method, a test covers that method and says nothing about anything else, so an invasive change to the area remains unverified. Written at a narrowing, the same effort covers the effects of the whole area, because everything passing through has to be observable there.

Feathers describes the same property a second way, in terms of design rather than of testing: "A pinch point is a natural encapsulation boundary. When you find a pinch point, you've found a narrow funnel for all of the effects of a large piece of code" (p. 182). That is why the concept is useful before any test is written — it marks where a boundary already exists in the code, whether or not anyone intended one.

## Finding one

Feathers is straightforward that this cannot always be done. "In some software, it is pretty easy to find pinch points for sets of changes, but in many cases it is nearly impossible" (p. 181), and where a single class affects dozens of others, the drawing of effects resembles "a large tangled tree". His first suggestion is to reconsider the scope, since "maybe we are trying to do too much at once", and his fallback is to give up on narrowing and stay close to the changes: "If you can't find a pinch point at all, just try to write tests for individual changes as close as you can" (p. 181).

Once a candidate is found, the question that decides whether it will work is about sensitivity rather than about design: "If I break this method, will I be able to sense it in this place?" (p. 182). Answering it means asking how the method is used, because a method reached in several ways is only a pinch point for the uses that resemble each other.

## Judging design with pinch points

The concept has a second use that has nothing to do with testing. Feathers notes that pinch points mark the shape a design already has: "If you pay attention to where your pinch points are, they can give you hints about how to make your code better" (p. 182). A narrowing that shows up in an effect sketch is a place where responsibilities could be redistributed, which turns the search for somewhere to test into a way of reading the code.

He also treats a pinch point as somewhere to begin work rather than as a destination: "Writing tests at pinch points is an ideal way to start some invasive work in part of a program" (p. 183), with the tests providing cover while the area is carved up.

## Trade-offs

- The tests written there are coarse by construction, since they cover a cluster of collaborating objects rather than one. Feathers devotes a section to the way these can degenerate into tests that are large and slow to run, and to the fact that they are meant to be provisional — tests written for the area are expected to be replaced by narrower ones around the individual classes as those accumulate (p. 184).
- A pinch point can be impossible to find in a tangled area, in which case the technique offers no shortcut and the work reverts to testing individual changes (p. 181).
- Judging a candidate requires knowing how the code is used, which is often the knowledge the team does not have — the situation that made the code hard to change in the first place.
- Choosing a wide pinch point is a deliberate trade of precision for reach. Tests there will catch a change to anything flowing through, and will also fail for reasons that have nothing to do with the change being made.

## When not to apply

- Where the area is already under test, since the question of where to begin does not arise.
- Where the change is confined to one method and the method can be tested where it stands. Narrowing adds nothing when there is nothing to narrow.
- Where a pinch point cannot be found after reconsidering scope, because the fallback — testing close to the change — is the honest answer rather than a failure.
- Where the tests would be the coarse kind and the area is not going to be changed again, since the cost of maintaining them falls on whoever comes next.

## Related Concepts

- [[Characterization Test]] — what is usually written at a pinch point, and where the technique's coarse tests and their costs are recorded.
- [[Legacy Code]] — the situation that makes the question of where to start a real one.
- [[Dependency-Breaking Technique]] — how a candidate pinch point becomes usable when the code there cannot be instantiated.
- [[Seam]] — a distinct property: a seam is where behavior can be replaced, while a pinch point is where changes can be observed.
- [[Refactor or Rewrite]] — the decision that pinch points inform, since they show where a design can be divided.

## My Understanding

What strikes me about this concept is that it is a way of looking rather than a technique to apply, which is why Feathers can use it for testing and for design without changing the definition. The same narrowing that makes a change observable also reveals where a boundary already exists, so the two uses are one observation read twice. My reading is that its practical value is in the fallback as much as in the idea: by saying plainly that pinch points are often not findable, and that testing close to the change is the next best thing, Feathers keeps the concept from becoming an excuse for not starting. The trap he records — coarse cluster tests that quietly become permanent — is the same risk in a different form.

## Sources

- Michael Feathers, *Working Effectively with Legacy Code*, Prentice Hall, 2005. `raw/books/Working.Effectively.with.Legacy.Code.pdf`
