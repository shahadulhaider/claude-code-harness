---
name: boundary-design
description: Designs or evaluates module boundaries, public interfaces, dependency direction, and refactor seams. Use for architectural changes where placement and abstraction are expensive to reverse, or when code is hard to test or change locally.
---

# Boundary Design

Optimize for a small stable interface, hidden complexity, and local change.

## Frame the Decision

- Name the callers, observable responsibilities, invariants, failure modes, and dependencies.
- Separate what callers must know from implementation detail.
- Identify where changes currently spread and why.

## Evaluate Options

For expensive decisions, compare at least two materially different designs. For a local low-risk change, prefer the existing shape unless evidence requires more.

Evaluate each option by:

- interface size and conceptual cost;
- complexity hidden from callers;
- locality of future changes;
- dependency direction and ownership;
- testability through real behavior;
- error and lifecycle semantics;
- migration cost and reversibility.

An abstraction must remove knowledge from callers, not merely move code into another file. Avoid pass-through wrappers, generic extension points without a current use, interfaces with only a hypothetical alternate implementation, and layers that duplicate an existing boundary.

Choose the simplest option that protects the important invariants. Show the proposed interface and one representative caller before implementing internals. Record a short ADR only when the decision is durable, non-obvious, and likely to be revisited.
