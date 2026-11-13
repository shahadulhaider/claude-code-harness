---
name: delivery-loop
description: Guides implementation from repository inspection through small verified slices and final diff review. Use for small-to-medium code changes whose scope is already settled; route unsettled multi-step work to /wf:plan and approved plans to execute-plan; skip one-line or purely informational tasks.
---

# Delivery Loop

Use fast feedback and observable progress instead of a large speculative implementation.

## Establish Ground Truth

- Read governing instructions and the relevant build, test, and formatting commands.
- Inspect the current worktree so unrelated changes are preserved.
- Ask the `project-state` subagent whether an approved plan already governs the work. If so, load `execute-plan` (via `/wf:start-work`) and use that plan instead of creating a second checklist.
- State the acceptance checks and identify the narrowest command or observation that can prove each one.
- Choose a specialized loop when appropriate: `behavior-first-testing` for behavior changes, `root-cause-debugging` for defects, and `boundary-design` for expensive interface decisions.

## Work in Slices

For multi-step work without an approved plan, stop and recommend `/wf:plan`; do not improvise durable scope in a transient todo list. For small work, each slice should still produce one observable improvement and be independently checkable.

For each slice:

1. Establish the current signal or failing check.
2. Make the smallest coherent edit.
3. Run the narrow check.
4. Inspect the changed code and update the active plan from what was learned.

Do not build all layers horizontally before any path works. Prefer an end-to-end tracer through one real path, then expand. Avoid speculative hooks and compatibility code.

## Finish

- Map the final behavior back to every acceptance check.
- Run targeted tests plus the broadest proportionate project check.
- Inspect the final diff for accidental scope, generated artifacts, debug code, and unrelated changes.
- Use the `reviewer` subagent for substantial or high-risk diffs.
- Report exact checks run and any check that could not run.

Do not commit or push unless the user explicitly requested it.
