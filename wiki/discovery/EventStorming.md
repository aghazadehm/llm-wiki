---
type: concept
status: draft
tags:
  - process
  - design
---

# EventStorming

EventStorming is a workshop format for exploring complex business domains through collaborative modeling. Created by Alberto Brandolini, it uses sticky notes (events, commands, actors, systems, etc.) on a timeline to discover domain events, processes, and boundaries through rapid, chaotic collaboration.

## Related Concepts

- [[Impact Mapping]] — can be used at strategic level; EventStorming dives deeper into how processes actually work.
- [[User Story Mapping]] — EventStorming reveals the domain; story mapping organizes the user journey for delivery.

## My Understanding

EventStorming comes in different flavors depending on purpose:
- **Big Picture EventStorming** (1-2 days) — explores entire business lines, discovers bounded contexts, identifies hot spots and bottlenecks.
- **Process Modeling EventStorming** (half day) — focuses on a specific process, adds commands, policies, read models.
- **Design-Level EventStorming** (half day) — more detailed, looks at aggregates, commands, and implementation details.

The core is events (orange stickies) representing things that happened in the domain, arranged on a timeline. Participants add actors, commands (blue), policies (lilac), external systems (pink), read models (green), etc. The format is intentionally unstructured at first ("chaotic exploration") then converges. Hot spots (pink with squiggles) mark areas of confusion or conflict.

What makes it powerful is that it brings together domain experts and technical people, surfaces hidden complexity, reveals conflicting mental models, and discovers the ubiquitous language. It's particularly valuable for brownfield/legacy systems where knowledge is scattered, or for greenfield domains that are complex.

## Sources

- Alberto Brandolini, *Introducing EventStorming*, Leanpub.
- Alberto Brandolini, [EventStorming.com](https://www.eventstorming.com/).
- Paul Rayner, *The EventStorming Handbook*, Leanpub.
- Evelyn van Kelle et al., *Collaborative Software Design: How to Facilitate Domain Modeling Decisions*, Manning, 2024.
