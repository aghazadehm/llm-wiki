---
type: concept
status: draft
tags:
  - testing
  - refactoring
aliases:
  - Golden Master Testing
---

# Golden Master Test

A **golden master test** captures a program's output as a baseline and fails when a later run differs from it. The comparison is coarse by construction — a whole document, an image, or a rendered result rather than a value the test asked for. Koskela describes the technique as "the golden master technique of comparing a rendered image to a canned image that we've manually checked to be correct" (p. 102).

## The problem it addresses

Some systems expose no interface narrow enough for a meaningful assertion to be written. The output may be a generated document, a rendering, or a long stream of text, and the code may not be callable in pieces. A golden master test gets coverage by comparing the whole result against a recording of the previous one. Bahrmai sets out the same recipe for this situation in a self-published guide: capture the output once into a stored file, then compare later runs against that file.

## The sources do not use the same name

- Koskela uses "golden master" and treats the technique as one to avoid where possible.
- Meszaros does not use the term. The closest named pattern is Recorded Test — "we automate tests by recording interactions with the application and playing them back using a test tool" (p. 278), also listed under the names Record and Playback Test and Capture/Playback Test.
- Bahrmai presents golden master tests as a strategy for code that cannot be covered otherwise.

These are related but not identical. A recorded test replays interactions with the application, while a golden master compares output, so a system can be covered by one without the other. Grouping them under a single name would lose the distinction the sources draw between replaying what happened and diffing what was produced.

## Trade-offs

- Koskela's objection is that the tests are brittle and that maintaining them is the wrong kind of work: "These aren't the kinds of tests that we'd like to maintain", and he says what he would rather write: "We want to write tests without such brittle precision, using fuzzy matching and smart algorithms" (p. 102).
- Meszaros gives the same failure mode a name in his pattern language, noting that recorded tests "tend to be Fragile Tests" and that "we usually discard these tests once we have developed other tests that cover the functionality" (p. 5). He places them as a transition rather than a destination.
- They are hard to read. Meszaros observes that most such tests "suffer from Obscure Tests (page 186), because they are recorded by a tool that doesn't know what is relevant to the human reader" (p. 10), so a failure points at a diff without saying which requirement it broke.
- Bahrmai's own list of situations to avoid them in names the same weakness from the other direction: non-deterministic behavior, unstable outputs, and any need for more granular testing (Part 1).

What they buy is coverage of behavior nobody can enumerate: the parts of a large output that a team would not think to assert, and which a rewrite or a refactoring is otherwise free to change silently.

## When not to apply

- Where a narrower assertion is available. A golden master is the fallback for output that cannot be interrogated, not a cheap alternative to asking the code a specific question.
- Where the output varies for reasons unrelated to the change, such as timestamps, generated identifiers, or map iteration order. Bahrmai lists non-deterministic behavior as disqualifying.
- Where the failure would be unreadable. A diff in a large file tells a reader that something moved without telling them what it means, which is the harm Meszaros names.

## Related Concepts

- [[Characterization Test]] — the narrower technique a golden master stands in for when no interface allows it.
- [[Legacy Code]] — the usual context, since the technique is reached for when a system has no tests and no seam.
- [[Refactor or Rewrite]] — the decision a golden master is often used to make safe.
- [[Dependency-Breaking Technique]] — the alternative route, worth taking when a dependency can be broken at all.
- [[State Verification]] — the style of assertion a golden master generalises to a whole output.

## My Understanding

The technique looks like the cheapest way to get a large system under test, and the sources suggest that impression is misleading: what it produces is a very wide assertion that is cheap to write and expensive to live with. My reading is that its proper use is narrow and temporary — to cover a surface during one specific change, where the alternative is no feedback at all — and that the sources agree on this more than their vocabulary suggests. Koskela's criticism and Meszaros' note that such tests are usually discarded once better tests exist are the same judgement reached from different starting points, and the disagreement is really about naming rather than about whether the tests should survive.

## Sources

- Lasse Koskela, *Effective Unit Testing*, Manning, 2013. `raw/books/Effective Unit Testing.pdf`
- Gerard Meszaros, *xUnit Test Patterns: Refactoring Test Code*, Addison-Wesley, 2007. `raw/books/xUnit Test Patterns Refactoring Test Code-Addison-Wesley (2007).pdf`
- Masoud Bahrmai, *Refactoring Strategies Guide*, Loan Management System Edition, self-published. `raw/books/Refactoring Strategies Guide.pdf`
