---
name: session-handoff
description: Creates compact durable state for another Claude Code session or engineer to continue a long-running task. Use when the user asks for a handoff, pause point, context reset, or work that will span sessions.
---

# Session Handoff

Create durable state that lets a fresh session act without replaying the conversation. An active `.claude/plans/*.md` plan is the canonical handoff artifact.

Ask the `project-state` subagent to select the active plan. If one exists, update its status, checkboxes, Open Questions, and Progress Notes in place; do not create a separate handoff file. If no plan exists, use a user-supplied path, or create a draft plan only when there is a continuing multi-step objective. For a short unplanned task, return the handoff in the response without inventing durable project state.

Include:

- objective and acceptance checks;
- current plan status and the next concrete unchecked task;
- decisions and brief rationale;
- files changed or important locations;
- exact verification commands and observed results;
- unresolved questions, blockers, and risks;
- relevant issue, spec, ADR, commit, or subagent-session references.

Reference existing artifacts instead of copying them. Exclude raw logs, long diffs, abandoned speculation, and secrets. Mark assumptions clearly. Keep Progress Notes append-only and concise.

Before finishing, verify paths and commands still exist and tell the user which plan was updated, or why no durable file was needed.
