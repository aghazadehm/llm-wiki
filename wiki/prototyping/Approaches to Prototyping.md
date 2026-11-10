---
type: comparison
status: draft
tags:
  - process
  - design
aliases:
  - Exploratory Prototyping
  - Experimental Prototyping
  - Evolutionary Prototyping
---

# Approaches to Prototyping

**Approaches to prototyping** is Christiane Floyd's classification of prototyping by the goal it serves in software development: **exploration**, **experimentation**, and **evolution** (p. 6). The classification is about the relation between prototype and target system, not about the prototype's appearance, and the same artifact could serve different approaches depending on what the team intends to learn from it.

## The shared process

Floyd describes every prototyping effort as four steps: **functional selection** (choosing the functions the prototype exhibits), **construction**, **evaluation**, and **further use** (p. 4). Evaluation is "the decisive step", because it provides the feedback the rest of the process depends on (p. 4). The prototype is a learning vehicle, and the process should be designed as a learning process: early availability, demonstration and modification, training, and a clear understanding of the commitment a demonstration creates (p. 5).

## Exploratory prototyping

Exploratory prototyping addresses the communication gap at the start of a project: developers know too little about the application field, and users have no clear idea what the computer could do for them (p. 6). A practical demonstration acts as a catalyst for ideas. It should not push a single solution but "point out alternatives whose respective merits can then be discussed" (p. 6).

The approach is informal, and its steps happen as needed within the conversation rather than in a fixed sequence (p. 7). Its output is usually thrown away, and its tools need not integrate with the production environment, because the prototype has no well-defined relation to the final product (p. 7). Floyd recommends it only when construction is cheap and the system's expected lifetime or quality requirements justify the investment (p. 7).

## Experimental prototyping

Experimental prototyping evaluates a proposed solution by using it experimentally. The areas of concern can include interface transparency, acceptable performance, or feasibility with the available resources (p. 8). Floyd lists five strategies (pp. 8-9):

- **Full functional simulation** — all functions intended for users are present, but built for ease of implementation rather than efficiency.
- **Human interface (front end) simulation** — the intended interface is real, and everything behind it is a mock-up.
- **Skeleton programming** — the overall structure is real, with a drastically reduced set of functions.
- **Base machine construction** — primitive functions are provided for users to combine into higher-level ones, useful when several user communities have different needs.
- **Partial functional simulation** — a hypothesis about one part of the system is tested, for example whether an algorithm produces acceptable results within resource limits.

Floyd is explicit that "there is no universal answer as to which of these forms of prototyping is best" (p. 9). The choice depends on the communication needs of the situation and on available resources and tools, and the contributors to her paper disagreed among themselves (p. 9). A recurring danger is that a prototype found unsuitable is retained as the production system because further investment is unwelcome, which reverses the purpose of prototyping (p. 9).

## Evolutionary prototyping

Evolutionary prototyping treats the product as a sequence of versions, each evaluated and used as a prototype for its successor (pp. 10-11). It rests on two observations: the organization around the system changes, and the system itself changes its usage context once it is used (p. 10). Floyd calls it the most powerful approach and the most remote from the original meaning of "prototype"; some authors would call it versioning instead (p. 10).

She distinguishes two forms. **Incremental system development** extends a solution step by step within one overall design and mainly affects implementation (p. 11). **Evolutionary system development** maps all phases onto repeated cycles of redesign, reimplementation, and reevaluation, and has no maintenance phase as such (p. 11). It demands that developers accept repeated revision and that users accept repeated change, and it requires the prototype and product environments to be integrated (pp. 11-12).

## Trade-offs

- Exploration buys shared understanding at the cost of a prototype that is usually discarded; it pays only when construction is cheap (p. 7).
- Experimentation buys evidence about a proposed solution, but the evidence is only as good as the strategy, and a convincing prototype can be kept for the wrong reason (p. 9).
- Evolution buys fitness to changing requirements at the cost of discipline and user tolerance for change (p. 11).
- None of the approaches is a development method on its own. Floyd insists that prototyping is "one procedure within system development that needs to be combined with others" (p. 14).

## When not to apply

Where requirements are stable and well understood, a phase-oriented process may be adequate and prototyping adds cost without adding knowledge. Exploratory prototyping is a poor fit when tools make construction expensive or the system is short-lived. Evolutionary prototyping is a poor fit for teams unable to revise repeatedly or for users who cannot absorb successive changes. Floyd also warns that prototyping can be misused to give the appearance of participation while tuning the system against users' interests (p. 15).

## Related Concepts

- [[Prototype]] — the artifact these approaches organize.
- [[Anatomy of Prototypes]] — how to choose what a given prototype filters and manifests.
- [[Prototype Fidelity]] — why the approach, not the finish, should drive the level of detail.
- [[Prototype as Communication Medium]] — the audience and commitment problems Floyd's evaluation step raises.

## My Understanding

Floyd's taxonomy is easy to misread as a maturity ladder: explore, then experiment, then evolve. Her own text resists that. The approaches answer different questions, can be combined, and are distinguished by the relation to the target system rather than by chronology. The most durable part is the insistence that evaluation is the decisive step and that further use must be decided deliberately, because those two choices determine whether the prototype teaches anything or quietly becomes the product.

## Sources

- Christiane Floyd, "A Systematic Look at Prototyping", in *Approaches to Prototyping*, Springer, 1984, pp. 1-18. `raw/books/prototypes/A Systematic Look at Prototyping - Christiane Floyd (1984).pdf`
