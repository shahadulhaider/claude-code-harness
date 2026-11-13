---
name: ticket-slicing
description: Splits an approved change into small vertical, dependency-aware, independently verifiable implementation tasks. Use when writing or repairing the TODO section of a multi-step `.claude/plans/*.md` plan.
---

# Ticket Slicing

Create executable slices that deliver observable progress instead of horizontal layers.

## Slice Rules

- Each top-level task should produce one coherent behavior or integration outcome.
- Include the production change, tests, and local documentation needed for that outcome in the same task.
- Name concrete starting paths or symbols without prescribing every implementation detail.
- State dependencies explicitly. Remove accidental dependencies by choosing a thin end-to-end tracer first.
- Keep a task small enough for one focused implementation context, but do not split mechanical edits that cannot be verified independently.
- Separate final cross-cutting checks into the Final Verification Wave rather than repeating them in every task.

Use this plan shape:

```markdown
- [ ] 1. <vertical outcome>
  - Outcome: <observable result>
  - Starting points: <paths, symbols, or established patterns>
  - Depends on: <task numbers or none>
  - Verification: <specific command or observable check>
```

Reject tasks named only "backend", "frontend", "tests", "refactor", or "cleanup" unless that work is independently meaningful. Merge tiny tasks whose value appears only together. Split tasks that combine unrelated risks, have multiple independent outcomes, or cannot name a focused verification signal.
