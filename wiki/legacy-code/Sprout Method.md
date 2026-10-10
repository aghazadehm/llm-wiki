---
type: concept
status: draft
tags:
  - refactoring
  - testing
---

# Sprout Method

**Sprout Method** adds new behavior to a system by writing it in a new method and calling that method from the code that needs it, so the new code can be tested even when the code around it cannot. Feathers states it as a rule rather than a preference: "When you need to add a feature to a system and it can be formulated completely as new code, write the code in a new method. Call it from the places where the new functionality needs to be" (p. 59).

## The problem it addresses

The alternative is to edit the existing method in place, and Feathers works through an example to show what that costs (p. 60). The edit itself was simple, but it mingled two responsibilities in one method, introduced a temporary variable, and left no separation between the new code and the old — so there was no way to know whether the result was right. Writing the addition as its own method keeps the new code separable and therefore testable, even though the method that calls it remains untested.

His rule for when the technique applies is about recognition rather than about code: use it "whenever you can see the code that you are adding as a distinct piece of work or you can't get tests around a method yet", and he judges it "far preferable to adding code inline" (p. 62).

## Trade-offs

- The code that calls the sprouted method stays untested. Feathers is explicit that this is the price, and states it as a warning about the whole family of techniques: "you are adding tested code into your system, but unless you cover the code that calls it, you aren't testing its use" (p. 59).
- The source method is deferred rather than improved. He puts the disadvantage plainly: using the technique means "you are giving up on the source method and its class for the moment. You aren't going to get it under test, and you aren't going to make it better" (p. 62).
- What it buys is separateness. The new code can be seen on its own and has a clean boundary against the old, which makes it easier to judge whether the change is right in context (p. 63).
- When the class cannot be instantiated even to call the new method, Feathers treats the sprout as something to make work anyway — as a public static method if necessary — and describes static methods as a staging area from which the code can later be moved onto a proper class (p. 62).

## When not to apply

- Where the class can be brought under test without much trouble. Feathers suggests trying to instantiate it in a test harness first, and points at the chapters on breaking dependencies before deciding the effort is unaffordable (p. 59).
- Where the new behavior cannot be stated as a separate piece of work. If it has to interleave with the logic already in the method, a technique that adds code around the call cannot express it — the limit that [[Wrap Method]] has as well.
- Where the change needs its own type rather than its own method. Feathers gives the class-level companion, Sprout Class, for cases where the source class cannot be instantiated at all, and notes its cost as conceptual complexity, since work that belonged in one class ends up spread across others (p. 67).

## Related Concepts

- [[Wrap Method]] — the sibling technique, which adds behavior around an existing method instead of beside it.
- [[Dependency-Breaking Technique]] — the alternative route, worth taking when the code can be made testable rather than worked around.
- [[Characterization Test]] — how behavior gets pinned down when the code around the sprout eventually is covered.
- [[Legacy Code]] — the situation the technique was devised for.
- [[Seam]] — the property a sprout does not create, since the calling code still cannot be varied from a test.
- [[Test Doubles]] — unnecessary for the sprouted method itself, which needs no collaborators replaced.

## My Understanding

The technique is honest about what it is: a way to make progress when the code is not yet testable, not a way to make it testable. What I find most useful is how narrowly Feathers bounds it — the new work has to be expressible as a distinct piece, and the method that calls it is left uncovered by design. That makes it a technique for buying time rather than for reducing debt, and it is easy to see how a codebase could accumulate a layer of sprouted methods whose callers are still untested. The recommendation to treat statics as a staging area reads as the same instinct: keep the new code movable, so that the next pass can put it where it belongs.

## Sources

- Michael Feathers, *Working Effectively with Legacy Code*, Prentice Hall, 2005. `raw/books/Working.Effectively.with.Legacy.Code.pdf`
