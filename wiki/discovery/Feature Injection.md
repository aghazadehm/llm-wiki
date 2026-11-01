---
type: concept
status: draft
tags:
  - process
---

# Feature Injection

Feature Injection is a technique for ensuring every feature delivers business value by tracing it back to a business need or desired outcome. Developed by Chris Matts and refined with Gojko Adzic, it provides a structured way to inject value at the right points rather than guessing what features are needed.

## Related Concepts

- [[Impact Mapping]] — builds on feature injection ideas; Adzic credits feature injection as influence.
- [[Outcome Over Output]] — feature injection enforces this by requiring traceability to business goals.
- [[Outside-In Development]] — both start from business needs/user goals.
- [[Behavior-Driven Development]] — feature injection's process aligns with BDD's discovery focus.

## My Understanding

Feature Injection typically follows three steps (as described by Chris Matts):
1. **Find the value** — Identify the business need or desired outcome. Why does this feature matter?
2. **Inject the behavior** — Determine what behavior needs to change and what features would create that behavior change.
3. **Measure the value** — Define how to know if the feature achieved the desired outcome.

The technique emphasizes that we often get the feature idea first ("We need X") but haven't identified the underlying need. By working backwards from business goals and forwards to measurable outcomes, we avoid building features for their own sake. It's about injecting features at the right place to achieve desired results.

Feature Injection shares lineage with Impact Mapping - both come from the same community concerned with connecting delivery to business outcomes.

## Sources

- Chris Matts & Gojko Adzic, *Feature Injection: three steps to success*, various publications and blog posts.
- Gojko Adzic, "Feature Injection" and related writings on [gojko.net](https://gojko.net/).
- Chris Matts, "Feature Injection: A Practical Process for Business Value", Agile 2007 and subsequent writings.
- Gojko Adzic, *Impact Mapping: Making a Big Impact with Software Products and Projects*, 2012 (credits feature injection ideas). `raw/books/Impact_Mapping_-_Gojko_Adzic.pdf`
