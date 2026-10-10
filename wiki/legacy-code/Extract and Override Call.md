---
type: concept
status: draft
tags:
  - refactoring
  - testing
---

# Extract and Override Call

**Extract and Override Call** replaces a troublesome method call with a call to a method on the same class, which a test subclass can then override. Feathers describes the case it is meant for as a local one: "At times, the dependencies that get in the way during testing are rather localized. We might have a single method call that we need to replace. If we can break the dependency on a method call, we can prevent odd side effects in our testing or sense values that are passed to the call" (p. 348).

## The problem it addresses

A single static call can make a class impossible to exercise — it reaches a global or a helper that the test cannot control, and the test either performs work it did not ask for or asserts on values it cannot see. The two problems Feathers names are side effects and unobservable inputs, and both are solved by moving the call somewhere the test can reach. His statement of the mechanism is minimal: "One option is to extract the call to a new method and override it in a testing subclass. This is known as Extract and Override Call" (p. 348).

In the worked example, a class calls a static method to build a list, and the extracted method is overridden in a subclass to return an empty list, since the test does not need the styles at all (p. 349). Later tests can vary that override to supply different values.

## Where it sits among the techniques

This is one of the smaller entries in the dependency-breaking catalog rather than a technique for a whole class, and Feathers is unreserved about how often he uses it: "Extract and Override Call is a very useful refactoring; I use it very often. It is an ideal way to break dependencies on global variables and static methods" (p. 349).

The steps are given for the case where no refactoring tool is available, and he notes why that is worth spelling out: with a tool the change is trivial, but done by hand the steps still allow a call to be extracted safely without tests in place (p. 349).

## Trade-offs

- It leaves a method that exists for the tests. The extracted call is a real method on the production class, so the design carries a small amount of structure whose only purpose is to be overridden.
- It relies on the language allowing the call to be overridden. If the method cannot be made overridable, the technique is unavailable.
- It buys observability rather than understanding. A test that overrides the call sees the value the test chose, which means the real call is no longer exercised in that test.
- Feathers reports the case where it stops being the right choice: "In general, I tend to use it unless there are many different calls against the same global. If there are, I often use Replace Global Reference with Getter (399) instead" (p. 349).

## When not to apply

- Where many calls reach the same global. Extracting each one separately multiplies the methods needed, and Feathers redirects to the entry for replacing the global reference with a getter (p. 349).
- Where the test can control the dependency already, through a constructor argument or a parameter, since the extraction adds a method that another mechanism has made unnecessary.
- Where the side effect needs to be exercised rather than avoided. The technique prevents the call from happening in the test, which is the wrong answer if the call is what is under examination.
- Where the class cannot be subclassed in a test at all, in which case no override point helps.

## Related Concepts

- [[Dependency-Breaking Technique]] — the catalog this entry belongs to, and the larger problem it addresses one dependency at a time.
- [[Seam]] — what the extraction creates: the call site itself is unchanged and the method that answers it differs between production and test.
- [[Types of Test Doubles]] — the override is a hand-written substitute, and its role — returning a value the test chose rather than recording a call — places it among the roles recorded there.
- [[Characterization Test]] — what the technique makes possible, since the class can now be exercised from a test.
- [[Legacy Code]] — the situation it was written for.

## My Understanding

The value of this technique seems to be its smallness. Rather than restructuring a class to accept a collaborator, it moves one call by a few lines and leaves the rest of the code alone, which is why Feathers says he uses it often and why it needs no framework. My reading is that its limit follows from the same property: because the override replaces the call rather than modelling the collaborator, it handles a call that produces a value and not an interaction that the test needs to inspect. Where the test needs to know what was passed or how often, a substitute installed at a seam — one of the [[Test Doubles]] — expresses the expectation rather than hiding the call.

## Sources

- Michael Feathers, *Working Effectively with Legacy Code*, Prentice Hall, 2005. `raw/books/Working.Effectively.with.Legacy.Code.pdf`
