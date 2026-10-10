---
type: concept
status: draft
tags:
  - testing
  - process
---

# Cover and Modify

**Cover and Modify** is Feathers' name for changing software beneath a safety net of tests, as opposed to changing it first and inspecting the damage afterwards. He presents these as the two ways changes are made and introduces them flatly: "Changes in a system can be made in two primary ways. I like to call them Edit and Pray and Cover and Modify" (p. 9).

## The two ways

Edit and Pray is the method he describes from practice: plan the change, make sure the code is understood, make the edit, then run the system and look around to see whether anything broke. He does not present it as carelessness, and notes that it looks like diligence because the care is on display — the planning and the checking are both visible work (p. 9).

His objection is that the diligence is aimed at the wrong thing rather than absent: "safety isn't solely a function of care" (p. 9). The analogy he uses to make the point is deliberately unflattering — "I don't think any of us would choose a surgeon who operated with a butter knife just because he worked with care" (p. 9). Care without the right instrument buys less than it appears to.

Cover and Modify supplies the missing instrument, and the name is literal: "Covering software means covering it with tests" (p. 9).

## What the method looks like in practice

Feathers describes the effect with a physical image. Tests written around the area being changed "act as a software vise", holding behavior in place so that whatever moves is the change that was intended: "The behavior of the code is fixed in place" (p. 10). He also marks out what these tests are for, distinguishing them from testing that tries to demonstrate correctness — this is testing "to detect change" (p. 10).

The care is not removed, only supported. Feathers keeps both halves of Edit and Pray and replaces the guessing with feedback: the same care is still applied, and it is the feedback that lets the changes be made with more confidence (p. 9). The tests are what supply that feedback.

## Trade-offs

- The cost is paid up front. The tests have to exist around the code being changed, and code that has none needs them written first, so a change that looked like an afternoon's work can require days of preparation.
- The method's value depends on the tests being good enough to notice the change actually being made. Covering code with weak tests produces the appearance of a safety net rather than one.
- It is unavailable while the code cannot be instantiated at all. Getting to that state is the work described by [[Dependency-Breaking Technique]], and the point a test can then use is a [[Seam]].
- Understanding the code is still required. The method changes what understanding is checked against, not whether any is needed.

## Related Concepts

- [[Legacy Code]] — the situation the method answers, since code without tests is exactly what Edit and Pray is used on.
- [[Characterization Test]] — the technique that usually produces the covering tests.
- [[Dependency-Breaking Technique]] — what makes the method possible when the code cannot be called from a test.
- [[Golden Master Test]] — a coarse way to get the feedback this method needs when no narrower assertion is available.
- [[Seam]] — the design property that lets a covering test reach the decision it needs to vary.

## My Understanding

What I find most useful here is that the distinction is about feedback rather than about risk appetite or discipline. Read that way it explains why the argument for tests so often fails to land: a team already taking care, and being seen to take care, is being asked to give up time for something the care is meant to provide. Feathers separates the two — care and technique — and argues that only one of them scales. My reading of the trade-off is that the cost is genuinely front-loaded and the benefit genuinely deferred, so the method suits code that will be changed again, and is a hard sell for a system facing one last change.

## Sources

- Michael Feathers, *Working Effectively with Legacy Code*, Prentice Hall, 2005. `raw/books/Working.Effectively.with.Legacy.Code.pdf`
