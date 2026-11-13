---
description: Create or revise a reviewed, executable Markdown plan.
argument-hint: <request or plan-name>
---

Load the `plan-workflow` skill and apply it to the request below. Follow the full workflow: use the `project-state` subagent to check for an existing plan, resolve repository facts before asking questions, write the plan under `.claude/plans/`, run the `plan-reviewer` subagent, and wait for explicit approval. Never implement product changes.

$ARGUMENTS
