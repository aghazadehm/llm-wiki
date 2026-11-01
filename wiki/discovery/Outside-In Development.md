---
type: concept
status: draft
tags:
  - process
  - design
---

# Outside-In Development

Outside-In Development is an approach that starts from the user's needs and desired outcomes, then works inward toward implementation. Rather than starting with internal architecture or technical components, you begin with what the user wants to achieve and build only what's needed to satisfy that.

## Related Concepts

- [[Outcome Over Output]] — outside-in focuses on user outcomes.
- [[Behavior-Driven Development]] — BDD is often practiced outside-in (start with acceptance criteria from user's perspective).
- [[Impact Mapping]] — starts at business goal (outside) and works inward to deliverables.

## My Understanding

Outside-in development inverts the traditional inside-out approach. Instead of building data models/components first and hoping they solve user problems, you:
1. Start with a user goal or need (outside)
2. Define what success looks like from user's perspective (acceptance criteria)
3. Work inward, building only the layers/components needed to satisfy that need
4. Drive development with tests from the outside

This naturally leads to focusing on behavior and outcomes. It also tends to produce simpler, more focused designs because you're pulled by real needs rather than pushing technical abstractions. When combined with BDD/TDD, outside-in helps ensure you're building the right thing and building it right.

## Sources

- Nat Pryce & Steve Freeman, *Growing Object-Oriented Software, Guided by Tests*, Addison-Wesley, 2009. `raw/books/growing_object-oriented_software_guided_by_tests.pdf` (demonstrates outside-in TDD)
- Liz Keogh, various writings on outside-in development.
- John Ferguson Smart, *BDD in Action*, Manning, 2014.
- Alistair Cockburn, *Hexagonal Architecture* (ports and adapters) — supports outside-in thinking.
