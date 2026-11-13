---
name: change-review
description: Reviews a worktree, branch, commit range, or PR for behavioral defects, regressions, security risks, scope drift, and missing tests. Use when the user asks for review or before completing a substantial high-risk change.
---

# Change Review

Review against intent, not aesthetic preference.

## Set the Review Frame

- Pin the diff range. For uncommitted work, include staged, unstaged, and untracked files; `git diff` alone omits new files, so list them with `git status --porcelain`. For a branch, compare from the merge base.
- Identify intent from the active `.claude/plans/*.md` plan when supplied, then the user request, issue, specification, tests, and project instructions.
- Read enough unchanged surrounding code to understand callers and invariants.

## Review Axes

1. Requirement fit: missing behavior, wrong behavior, and unrequested scope.
2. Correctness: edge cases, state transitions, errors, concurrency, ordering, and cleanup.
3. Safety: authorization, validation, secrets, privacy, injection, data loss, and unsafe migrations.
4. Compatibility: public interfaces, persisted data, configuration, consumers, and rollout.
5. Verification: tests that fail to cover the risky path, brittle assertions, and checks not run.
6. Maintainability only where it creates a concrete defect risk, such as duplicated invariants or scattered ownership.

For a large diff, independent reviewers may inspect separate axes in parallel. Do not duplicate the whole review for a small change.

## Report

Put findings first, ordered by severity. Every finding must include `path:line`, the triggering scenario, user or system impact, supporting evidence, and a concise fix direction. Verify a concern against the surrounding code before reporting it. Omit pure style preferences and unsupported possibilities.

If there are no findings, say so explicitly and list residual risks or checks that were unavailable. Do not edit code during a review unless the user asks for fixes.
