---
type: source
status: draft
title: "Mocks Aren't Stubs"
tags:
  - testing
  - tdd
  - test-doubles
last_updated: 2026-10-11
---

# Mocks Aren't Stubs

**"Mocks Aren't Stubs"** is Martin Fowler's 2007 article on why mock objects are so often confused with stubs, and on the deeper design split the confusion papers over. Fowler frames the difference as two separate differences rather than one: a difference in how test results are verified (state verification versus behavior verification), and "a whole different philosophy to the way testing and design play together, which I term here as the classical and mockist styles of Test Driven Development." The testing domain's central vocabulary and main tension come from this article.

## What it says

The article works one running example — an order that fills itself from a warehouse — through both verification styles. The state-verification test asserts the order is filled and the warehouse inventory reduced; the behavior-verification test instead programs a mock warehouse with expectations and verifies the order made the right calls on it.

It then adopts Gerard Meszaros's vocabulary, using **Test Double** as the generic term for any pretend object and naming five kinds: dummies (passed around but never used), fakes (working but shortcut), stubs (canned answers), spies (stubs that also record how they were called), and mocks (pre-programmed with expectations). Only mocks insist on behavior verification; the rest "can go either way," and a stub that verifies by behavior is, in Meszaros's terms, a spy.

The second half compares the classical and mockist styles across four dimensions — driving TDD (outside-in versus middle-out), fixture setup, test isolation, and coupling tests to implementations — and notes the design each style tends to produce: collecting parameters, role interfaces, and the "Tell, Don't Ask" style.

## Related Concepts

- [[Test Doubles]] — the umbrella term the article borrows from Meszaros.
- [[Types of Test Doubles]] — the five roles (dummy, fake, stub, spy, mock) it lists.
- [[State Verification]] — verification by examining the result after exercise.
- [[Behavior Verification]] — verification by checking the calls made on collaborators.
- [[Classical and Mockist Testing]] — the design divide the verification difference papers over.
- [[Choosing Test Doubles]] — the decision the article argues is mostly about style, not about the verification choice.

## My Understanding

The article's real move is to show that "mock versus stub" is the wrong question. The verification style is, as Fowler puts it, "mostly not a big decision"; the choice with teeth is classical versus mockist, because that one changes how the design comes together. The vault keeps those two distinctions as separate articles for exactly this reason: conflating them is the confusion the article is about.

## Sources

- Martin Fowler, [Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html), 2007. `raw/articles/Mocks Aren't Stubs.md`
