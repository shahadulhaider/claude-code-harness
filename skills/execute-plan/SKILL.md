---
name: execute-plan
description: Executes an approved `.claude/plans/*.md` plan and keeps its status, task checkboxes, verification, blockers, and progress notes current. Use when the user says start work, resume, continue, or implement an approved plan.
---

# Execute a Plan

The selected Markdown plan is the source of truth for scope and durable progress. Do not maintain a competing conversational or handoff checklist.

## Select and Enter

1. Ask the `project-state` subagent to identify the active plan, or read the `.claude/plans` directory directly when delegation is unavailable. If selection is ambiguous, ask the user instead of guessing.
2. Execute only a plan with `status: ready`, `in-progress`, or `blocked`. A clear `/wf:start-work` request for one reviewed draft counts as explicit approval when no Open Questions remain; set it to `ready` before continuing. Otherwise never implement a `draft`, `complete`, or `abandoned` plan.
3. Change `ready` to `in-progress` before editing product code. Resume `blocked` work only after recording how the blocker was resolved and restoring `in-progress`.
4. Read the full plan, applicable repository instructions, and current worktree before choosing the next unchecked task whose dependencies are complete.

## Deliver One Slice at a Time

For each top-level task:

1. Confirm its outcome, starting points, dependencies, and verification signal against the current repository.
2. Preserve unrelated worktree changes and make the smallest coherent vertical edit.
3. Run the task's focused verification and inspect the resulting diff.
4. Mark the task `[x]` only after its outcome is present and verification passes. Append one concise Progress Note with the date, task number, result, and exact check.

Treat local implementation detail as yours to resolve. If discovery changes an approved requirement, non-goal, public contract, data decision, or risk materially, set `status: blocked`, record the issue under Open Questions or Progress Notes, and ask the user. Do not silently expand scope.

## Finish or Pause

- Run and check off every Final Verification Wave item only when its named evidence passes.
- Use the `reviewer` subagent for the final plan-to-diff check when the plan requires it or risk is substantial.
- Set `status: complete` only when all top-level TODOs and final checks are complete; update the `updated` date.
- When work must pause, keep `status: in-progress` if the next action is executable. Use `blocked` only for a real external decision or dependency, and name it explicitly.

Never claim a failed or unrun check passed. Do not renumber settled tasks during execution, erase prior Progress Notes, commit, or push unless explicitly requested.
