---
type: source
status: draft
title: "A Systematic Look at Prototyping"
tags:
  - process
  - design
last_updated: 2026-11-10
---

# A Systematic Look at Prototyping

Christiane Floyd wrote this paper as the introduction to the Working Conference on Prototyping, published in *Approaches to Prototyping* (Springer, 1984). It is an attempt to give the conference a shared conceptual framework, and it draws on position papers by the other contributors.

## What it says

Floyd starts from the observation that "prototype" cannot be used in its strict engineering sense for software: there is no mass-produced type, no clear "first" instance, and the desired characteristics are not well defined in advance (p. 2). She therefore treats prototyping as a process rather than a product, and as a learning vehicle whose overriding concern is the quality of the target system (p. 3).

The process has four steps: functional selection, construction, evaluation, and further use (p. 4). Evaluation is decisive because it supplies the feedback for further development, and it requires resources, training, and the participation of the relevant user groups (p. 4). The learning-process aspects are early availability, demonstration and modification, teaching and training, and awareness of the commitment created by showing a prototype (p. 5).

The three approaches are exploratory, experimental, and evolutionary (p. 6). Exploratory prototyping clarifies requirements and discusses alternatives; experimental prototyping evaluates a proposed solution through strategies such as full functional simulation, interface simulation, skeleton programming, base machine construction, and partial functional simulation (pp. 8-9); evolutionary prototyping treats the product as a sequence of versions, either incrementally within one design or through repeated redesign cycles (pp. 10-11). The paper closes with techniques and tools (modular design, dialogue design, simulation, high-level languages, toolkits), and with a discussion of dangers and benefits, including the possibility of manipulating users and the argument that prototyping need not raise overall costs (pp. 12-16).

## Related Concepts

- [[Approaches to Prototyping]] — the three-approach classification.
- [[Prototype]] — the artifact the paper treats as a learning vehicle.
- [[Prototype Fidelity]] — the functional scope and simulation choices the strategies imply.

## My Understanding

The paper is a product of its moment: the tools it names are dated, and the debate over whether "prototyping" is the right word has not aged into a consensus. What remains useful is the insistence that prototyping is a procedure inside a development strategy, not a strategy of its own, and that the decision about further use is part of the method. The warning about prototypes being retained because further investment is unwelcome is still recognizable in projects that ship a demo.

## Sources

- Christiane Floyd, "A Systematic Look at Prototyping", in *Approaches to Prototyping*, Springer, 1984, pp. 1-18. `raw/books/prototypes/A Systematic Look at Prototyping - Christiane Floyd (1984).pdf`
