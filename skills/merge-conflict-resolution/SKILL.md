---
name: merge-conflict-resolution
description: Resolves Git merge, rebase, cherry-pick, or stash conflicts while preserving both sides' intent. Use when conflict markers or unmerged paths exist; never use for routine source edits.
---

# Merge Conflict Resolution

Resolve conflicts from intent and history, not by mechanically choosing ours or theirs.

## Establish Safety

1. Inspect Git status and identify the operation in progress, unmerged paths, unrelated local changes, and the intended target history.
2. Do not abort, reset, clean, checkout files, or rewrite history unless the user explicitly requests it.
3. For each conflicted unit, inspect the base and both sides plus relevant surrounding commits, tests, and callers.

## Resolve

- Describe what each side was trying to preserve.
- Combine compatible behavior and make an explicit choice where intent conflicts.
- Follow the destination branch's current interfaces and conventions while retaining required behavior from the incoming change.
- Resolve generated files through their generator when practical; do not hand-merge lockfiles blindly when the package manager can regenerate them safely.
- Remove every conflict marker and inspect the resulting diff before staging anything.

Run focused checks for each resolved behavior, then the broadest proportionate suite. Report remaining unmerged paths, choices made, and checks run. Do not continue a rebase, create a merge commit, commit, or push unless explicitly requested.
