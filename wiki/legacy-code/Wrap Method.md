---
type: concept
status: draft
tags:
  - refactoring
  - testing
---

# Wrap Method

**Wrap Method** adds new behavior to a system by putting it around an existing method rather than inside it, so the addition can be developed under test even when the original method cannot be. The mechanism is a rename: "We create a method with the name of the original method and have it delegate to our old code. We use this when we want to add behavior to existing calls of the original method" (p. 69).

## The problem it addresses

Feathers frames the temptation first. Adding a line to a method that already exists is the simplest way to get new behavior in, and he treats the simplicity as a warning sign: "Adding behavior to existing methods is easy to do, but often it isn't the right thing to do" (p. 67). The reason is that the addition usually belongs somewhere else and is only going in because it has to run at the same moment. He gives the old name for that mistake — "Back in the early days of programming, this was named temporal coupling, and it is a pretty nasty thing when you do it excessively" (p. 67).

Wrap Method answers both halves of that problem at once. The new behavior lands in its own method, where it can be tested, and the method it was going to be pasted into keeps its size and its shape.

## The two forms

- The original name is reused. The existing method is renamed, and a new method taking the old name and signature calls the renamed one. Feathers directs the reader to preserve signatures while doing this, and describes the result as the form to use when every existing call should gain the new behavior (pp. 69-70).
- A new name is added instead. The new behavior goes into its own method, and a second method calls it and the original one so that callers may choose either path (p. 69).

Both forms are developed test first, with the steps listed on p. 70: identify the method, rename or add, place the call to the old code inside the new method, and write the new feature's method under test before wiring it in. Feathers credits the second form to Kent Beck (p. 69).

## Trade-offs

- The new behavior cannot be interleaved with the old logic. It has to happen either before or after, which he lists as the first limitation: "The first is that the new feature that you add can't be intertwined with the logic of the old feature. It has to be something that you do either before or after the old feature" (p. 69). In many cases that constraint matches what the change actually is, so it costs nothing.
- It leaves the existing method the same size, which he contrasts with the sibling techniques: "Sprout Method and Sprout Class add code to existing methods and make them longer by at least one line, but Wrap Method does not increase the size of existing methods" (p. 70).
- What it produces is a seam. Feathers recommends it partly for that: "Wrap Method is a great way to introduce seams while adding new features" (p. 69), which means the wrapping is not only a way to test the new code but also a place where the old behavior can later be varied.
- Like its siblings, it is a way of working around the original method rather than bringing it under test — "a good way of getting new, tested functionality into an application when we can't easily write tests for the calling code" (p. 70).

## When not to apply

- Where the added behavior genuinely interleaves with the logic already in the method, since the technique can only place new code before or after the call.
- Where the callers of the original method can be tested already. If the code around the call is covered, the new behavior can be written in place and verified there, and the extra method is structural noise.
- Where the only obstacle is the method's size or responsibilities rather than the absence of tests, which is a design change to make with a suite in place rather than a technique for working without one.
- Where a class-level wrapper is what the situation needs. Feathers gives Wrap Class as the companion for adding behavior in another class entirely, for cases where the original class cannot be instantiated under test at all (p. 71).

## Related Concepts

- [[Sprout Method]] — the sibling technique, which puts new behavior in a new method called from the old one rather than around it.
- [[Seam]] — what a wrap leaves behind, and the reason Feathers recommends the technique beyond getting tests around new code.
- [[Dependency-Breaking Technique]] — the catalog for when the goal is to make the existing code testable instead of routing around it.
- [[Characterization Test]] — how the behavior being wrapped gets recorded before it is changed.
- [[Legacy Code]] — the situation both this technique and its siblings were devised for.

## My Understanding

The interesting move here is that the technique solves a design problem and a testing problem with the same edit. Splitting new behavior out of a method is what a reviewer would ask for anyway; writing it as a separate method that is developed test first is what makes it verifiable. My reading is that this is why Feathers presents Wrap Method as the most comfortable of the three siblings — the constraint it imposes, that the new behavior must sit before or after the old, is the same separation the code wanted, so the technique's main limitation is also its argument. Where Sprout Method asks the reader to accept an untested caller, this one leaves behind a seam that can be used later.

## Sources

- Michael Feathers, *Working Effectively with Legacy Code*, Prentice Hall, 2005. `raw/books/Working.Effectively.with.Legacy.Code.pdf`
