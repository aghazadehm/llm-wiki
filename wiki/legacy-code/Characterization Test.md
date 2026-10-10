---
type: concept
status: draft
tags:
  - testing
  - refactoring
aliases:
  - Characterization Tests
  - Characterization Testing
---

# Characterization Test

A **characterization test** records what a piece of code does today, so that a change can be made without quietly altering behavior. Feathers defines it as "a test that characterizes the actual behavior of a piece of code" (p. 186), and the wording is deliberately free of expectation. He contrasts the test with a claim about what the code ought to do, and the point is that "the tests document the actual current behavior of the system" (p. 186).

## The problem it addresses

Untested code leaves a change with two possible outcomes and no way to tell them apart: the behavior a caller relies on survives, or it does not. Documentation is a poor substitute, because it records intent rather than what the code does. A characterization test supplies the missing comparison by capturing behavior before the change rather than after it. Feathers introduces the technique at the point where a change is already unavoidable: "We need to make some changes, and we need to write characterization tests (186) to pin down the behavior that is already there" (p. 151).

## Why it is honest about defects

Because it records behavior rather than intent, a characterization test will lock in a bug just as readily as correct behavior. Feathers treats that as the working assumption rather than a defect to fix first: bugs are something a team will encounter "along the way", but "in most legacy code, if we make finding and fixing all of the bugs our goal, we'll never finish" (p. 186). The test exists to make the next change safe, not to certify the code.

## Trade-offs

- The tests describe a system as it stands, so they have to be edited when the behavior is meant to change. Their value falls once the interesting behavior has been re-expressed as tests that state an expectation instead of a record.
- Feathers warns that success where they are written can mislead. Having carved out a cluster of classes and got them to the point of being instantiable together, "you can make changes with impunity. You've made a little oasis in your application where the work has just gotten easier. But be careful — it could be a trap" (p. 183).
- The trap he names on the following page is growth. Tests written for a cluster of collaborating objects can "slowly grow into mini-integration tests" which end up "big, bulky" and "take forever to run" (Pinch Point Traps, p. 184).
- His remedy makes them transitional by design. The wider tests make an area safe to work in, but "eventually, the tests at the pinch point can go away" as narrower tests accumulate around the classes involved (p. 184).

## When it is the wrong technique

- Where passing tests already state what should happen. A record of behavior adds nothing once an expectation exists and holds.
- Where the code has no reachable point to assert from, because the technique assumes the code can be instantiated and called at all. Getting it to that state is the subject of [[Dependency-Breaking Technique]].
- Where the only observable is a coarse one, such as a generated document or a rendering. A [[Golden Master Test]] is the usual fallback, with the fragility costs recorded there.

## Related Concepts

- [[Legacy Code]] — the situation that makes the technique necessary.
- [[Dependency-Breaking Technique]] — how code is made instantiable when it is not.
- [[Golden Master Test]] — the coarse-grained alternative when no narrow interface exists.
- [[Seam]] — where a substitute is installed so the code under characterization does not call a real collaborator.
- [[Test Doubles]] — the substitutes themselves.
- [[State Verification]] — the style of assertion a characterization test usually makes after calling the code.

## My Understanding

What I find most useful in the definition is that it removes a decision from the writer. There is nothing to judge, only something to record, so the work can proceed while the system is still poorly understood — which is exactly the condition that makes a change feel risky. My reading is that the technique's real cost is not the tests it produces but the expectation it creates. A characterization test proves that behavior has not changed, which is what a team needs before a refactoring and precisely what it must not rely on afterwards, when the point of the change was to alter behavior. Treating them as scaffolding rather than as a suite seems to be the position Feathers takes when he says they can go away.

## Sources

- Michael Feathers, *Working Effectively with Legacy Code*, Prentice Hall, 2005. `raw/books/Working.Effectively.with.Legacy.Code.pdf`
