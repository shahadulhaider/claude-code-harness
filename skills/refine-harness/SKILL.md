---
name: refine-harness
description: Use ONLY when the user explicitly asks to improve, refine, or update their Claude Code agents, skills, commands, permissions, models, or workflow based on observed experience. Applies one evidence-backed harness change and validates it.
---

# Refine the Harness

Improve the workflow through small reviewable changes, not autonomous prompt growth.

## Evidence

Identify the observed trajectory: what task occurred, what behavior helped or failed, and what outcome proves it. Prefer patterns seen more than once. A single severe safety or correctness failure may justify immediate action.

Do not turn one preference, model mistake, or temporary project condition into a global rule. Project-specific knowledge belongs in the project's `CLAUDE.md`, not the global harness.

## Choose One Lever

Select the narrowest artifact that owns the behavior:

- agent prompt (`~/.claude/agents/*.md`) for role and delegation behavior;
- skill (`~/.claude/skills/*/SKILL.md`) for a reusable on-demand procedure;
- command (`~/.claude/commands/wf/*.md`) for an invocable entry point;
- permission rule (`~/.claude/settings.json`) for a safety boundary;
- model selection for cost and capability;
- project instruction (`<project>/CLAUDE.md`) for repository-specific conventions;
- new specialist agent only when an existing role cannot hold the responsibility cleanly.

Prefer editing an existing artifact over adding another overlapping one. Keep the always-loaded `CLAUDE.md` short; put detailed procedures in lazy-loaded skills.

## Apply and Validate

1. State the evidence, proposed change, expected measurable effect, and rollback.
2. Preserve unrelated configuration and never expose credentials.
3. Apply the smallest patch.
4. Validate that `settings.json` still parses and that changed agents, skills, and commands have valid frontmatter and are discoverable (`/agents`, `/help`).
5. Report what changed and what future observation would confirm or reject the refinement.

Do not recursively invoke this skill or let subagents edit the harness. New Claude Code sessions pick up agent, skill, and command changes; some `settings.json` changes require restarting the session.
