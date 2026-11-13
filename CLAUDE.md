# Global Engineering Rules

These rules apply across projects. Explicit user instructions and more specific project instructions (a project's own `CLAUDE.md`) take precedence.

## Working Mode

- Read applicable project instructions and inspect the current worktree before making changes.
- Resolve repository and dependency facts with tools before asking the user. Ask only material decisions the user owns, and include a recommended default with its consequence.
- Implement small, clear requests directly. Use the durable planning workflow (`/wf:plan`) for multi-step work whose scope, architecture, data, compatibility, or verification is not already settled.
- Treat an active `.claude/plans/*.md` file as the source of truth. Keep its status, task checkboxes, verification, blockers, and Progress Notes current; do not create a competing checklist.
- For bugs, reproduce the symptom and establish a failing signal before changing code. Fix the earliest proven cause rather than masking the symptom.

## Changes

- Make the smallest coherent change that satisfies the requested behavior.
- Preserve unrelated user changes and generated artifacts. Never revert work you did not create unless explicitly asked.
- Follow existing project structure and conventions. Add abstractions, compatibility paths, dependencies, or configuration only for a concrete current need.
- Keep comments rare and focused on non-obvious intent, invariants, or constraints.

## Verification

- Define observable acceptance checks before substantial implementation.
- Run the narrowest relevant check after each coherent slice, then the broadest proportionate project check.
- Never claim an unrun or failing check passed. Report exact commands and any unavailable verification.
- Inspect the final diff for accidental scope, debug code, secrets, and unrelated changes. Use independent review for substantial or high-risk work.

## Git And Safety

- Do not commit, amend, push, create releases, or open pull requests unless explicitly requested.
- Before a requested commit, inspect status, diff, and recent history; stage only intended files.
- Never use destructive Git or filesystem operations without explicit approval.
- Do not expose credentials, private URLs, personal data, or secret-bearing files in output, plans, logs, or commits.

## Communication

- Keep progress updates brief and factual. Surface discoveries, tradeoffs, and blockers rather than narrating routine tool use.
- For reviews, report actionable findings first, ordered by severity with file references. If there are no findings, state that and identify residual testing gaps.
- Finish with the outcome, important files changed, verification performed, and any remaining limitation or user decision.

## Harness

- `/wf:plan` produces a reviewed durable plan in `.claude/plans/`; `/wf:start-work` implements it; `/wf:status` reports state to resume; `/wf:review` runs independent review before finishing substantial work; `/wf:brainstorm` compares options when the direction is unclear.
- Delegate read-only discovery to the `Explore` agent, bounded implementation or analysis to `general-purpose`, authoritative external research to the `researcher` subagent, independent code review to the `reviewer` subagent, and plan/worktree status to the `project-state` subagent.
- Skills are lazy-loaded playbooks; load the one whose trigger matches the task instead of improvising the procedure.
- Plan statuses are `draft`, `ready`, `in-progress`, `blocked`, `complete`, and `abandoned`.
