---
description: Review the current worktree or a supplied branch, commit, or diff range.
argument-hint: <branch | commit range | path (optional)>
---

Use the `reviewer` subagent to review `$ARGUMENTS`; if no range is supplied, review all current staged, unstaged, and untracked worktree changes (list untracked files with `git status --porcelain` and read them in full). Pass the active `.claude/plans/*.md` plan as intent when applicable. Report findings only; never edit files.
