---
name: plan-workflow
description: Turns a non-trivial idea or request into an approved, executable durable plan in `.claude/plans/`. Use for multi-step work whose scope, architecture, data, compatibility, or verification is not already settled. Loaded by /wf:plan and /wf:grill-plan.
---

# Planning Workflow

Turn an idea or request into an approved, executable plan. Planning ends at a plan; while planning, never edit product code, run implementation commands, or silently begin delivery.

## Workflow

1. Use the `project-state` subagent when plans may already exist. Continue or revise an existing plan instead of creating a duplicate.
2. Load `scope-change` when requirements or boundaries remain ambiguous. Resolve facts before asking the user: use the `Explore` agent for local code and the `researcher` subagent for external behavior. Load `brainstorm` only when materially different solution directions are plausible.
3. Ask only decisions the user owns. State a recommended default and consequence. For explicit deep planning, architecture, destructive work, migrations, or unresolved product behavior, call the `plan-interviewer` subagent and present its frontier to the user; feed each answer round back and re-invoke until the frontier is empty.
4. Load `ticket-slicing` for multi-step work, then write the draft to `.claude/plans/<short-slug>.md`, creating the directory if needed. Keep exactly one plan for one objective.
5. Call the `plan-reviewer` subagent with the exact plan path for every multi-step or high-risk plan. Revise blocking findings and re-review, normally for no more than two passes.
6. Present the reviewed plan and wait for explicit user approval. Keep `status: draft` while decisions or approval remain. Set `status: ready` only after approval.

## Plan Contract

Use this structure:

```markdown
---
title: <title>
status: draft
created: YYYY-MM-DD
updated: YYYY-MM-DD
---

# Goal
# Context
# Requirements
# Non-Goals
# Decisions
# TODOs
- [ ] 1. <vertical slice>
  - Outcome: <observable result>
  - Starting points: <paths, symbols, or established patterns>
  - Depends on: <task numbers or none>
  - Verification: <specific command or observable check>
# Final Verification Wave
- [ ] F1. <focused checks>
- [ ] F2. <broad project checks>
- [ ] F3. <review the completed diff against this plan>
# Risks
# Open Questions
# Progress Notes
```

Statuses are `draft`, `ready`, `in-progress`, `blocked`, `complete`, or `abandoned`. Top-level task labels must remain numbered so `project-state` can report progress. Prefer paths and symbols over fragile line numbers. Tasks must be vertical, independently verifiable where possible, and small enough for one focused implementation context.

## Review Discipline

The interviewer discovers unresolved decisions; the short reviewer checks whether implementation can start. Do not ask the interviewer to answer on the user's behalf. Do not let the short reviewer relitigate settled architecture or demand perfection. The final plan must contain explicit non-goals, dependencies, verification, and enough evidence-backed starting points to avoid repeating discovery.
