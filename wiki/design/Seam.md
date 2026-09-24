---
type: concept
status: draft
tags:
  - design
  - testing
aliases:
  - Seams
---

# Seam

A **seam** is "a place where you can alter behavior in your program without editing in that place". The definition is Michael Feathers's, and the wording is deliberate: the source code is expected to be identical in production and in test, so a test-only change cannot be made *at* the seam. It is made somewhere else, at what Feathers calls the enabling point (ch. 4, pp. 31 and 36).

## The problem it addresses

Code that constructs its own collaborators can only be made to behave differently for a test by editing the code under test, and Feathers treats that as disqualifying: "The source code should be the same in both production and test" (p. 36). Testing such code therefore needs a place where behavior can be changed from outside, without touching the logic being exercised.

Feathers frames seams as a way of seeing rather than a thing to add, which is why the idea comes from his book on legacy code:

> One of the biggest challenges in getting legacy code under test is breaking dependencies. When we are lucky, the dependencies that we have are small and localized; but in pathological cases, they are numerous and spread out throughout a code base. The seam view of software helps us see the opportunities that are already in the code base. If we can replace behavior at seams, we can selectively exclude dependencies in our tests. (p. 33)

## Enabling point

Feathers makes the enabling point part of the concept rather than a detail: "Every seam has an enabling point, a place where you can make the decision to use one behavior or another" (definition box, p. 36). A place where behavior happens to differ is not usable from a test unless the test can reach the decision.

Two of his examples make the pairing concrete:

- For a preprocessing seam, the enabling point is "a preprocessor define named TESTING", which makes a header file define macros that replace the calls in the source file (p. 36).
- For a link seam, "the enabling point is the classpath" (p. 38).

## Kinds of seam

Feathers describes the object seam as "only one of many different kinds of seams" (p. 33) and works through three in chapter 4. Each depends on a mechanism the language or toolchain provides, which is the main reason a seam is not portable between languages.

### Object seam

Feathers names the seam an object seam where the method that is called can be changed "without changing the method that calls it": the call site stays as written and the object that responds to it changes. "Object seams are available in object-oriented languages" (p. 33).

### Preprocessing seam

Behavior is altered by textual substitution before compilation: "the #include directive of the C preprocessor gives us a seam that we can use to replace text before it is compiled" (p. 36). Feathers is blunt about the cost, and does not present this as a technique to reach for by preference:

> It's not a good idea to use excessive preprocessing in production code because it tends to decrease code clarity. The conditional compilation directives (#ifdef, #ifndef, #if, and so on) pretty much force you to maintain several different programs in the same source code. (p. 34)

He also records that he would not want a preprocessor for "Java and other more modern languages", describing it as compensation for "some of the other testing obstacles" that C and C++ present (p. 36).

### Link seam

Behavior is changed where calls to code in other files are resolved. "In languages such as C and C++, there really is a separate linker that does the operation I just described. In Java and similar languages, the compiler does the linking process behind the scenes" (pp. 36-37). Because the enabling point is the classpath (p. 38), this seam belongs to the build rather than to the source.

## Trade-offs

- A seam is only as available as its mechanism: object seams need an object-oriented language, preprocessing seams need a preprocessor, and link seams need a distinct linking step.
- Preprocessing seams buy control at the cost of clarity, and Feathers states that cost rather than recommending them (p. 34).
- Feathers presents the seam view as a way of seeing "the opportunities that are already in the code base" (p. 33), so the concept belongs to retrofitting tests to an existing design rather than to a pattern to introduce.

## Related Concepts

- [[Dependency Injection]] — the mechanism that normally provides an object seam, giving a test somewhere to install a substitute.
- [[Test Doubles]] — the substitutes themselves; they require a seam to be installed at.
- [[Types of Test Doubles]] — the roles a substitute plays once it is installed.
- [[Choosing Test Doubles]] — the selection decision, which assumes an installable point already exists.

## My Understanding

The part of this idea I find most useful is that it separates two things usually conflated: the place where behavior differs, and the place where that difference is decided. Once they are distinguished, it becomes clear why the practical question in a test is not "which double should I use" but "can I reach the decision from here at all" — and why dependency injection earns its place without any framework, since it moves the decision to a point a test can reach. This is an interpretation, not a claim taken from the sources.

## Sources

- Michael Feathers, *Working Effectively with Legacy Code*, Prentice Hall, 2005. `raw/books/Working.Effectively.with.Legacy.Code.pdf`
