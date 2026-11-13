---
name: agent-document-design
description: Designs or refactors `CLAUDE.md`, `AGENTS.md`, repository instructions, agent prompts, and skill documents for concise progressive disclosure. Use when agent guidance is duplicated, stale, oversized, or loaded at the wrong scope.
---

# Agent Document Design

Put stable instructions at the narrowest scope where they are always useful; move situational procedures into lazy-loaded skills or linked documentation.

## Audit

- Map which files load globally, by repository, and by subdirectory.
- Identify contradictions, duplicated rules, stale commands, hidden prerequisites, and prose that merely restates tool behavior.
- Separate durable constraints from examples, background knowledge, and task-specific procedures.

## Design

- Keep always-loaded documents short: project shape, non-obvious commands, hard constraints, and where deeper guidance lives.
- Use imperative, testable instructions with literal filenames and command names.
- Place language- or directory-specific rules near the files they govern.
- Prefer one canonical rule with references over synchronized copies.
- Give every skill a concrete third-person trigger description; avoid broad triggers that load it for adjacent work.
- Preserve intentional local overrides and explain precedence only when it is non-obvious.

Validate that referenced paths and commands exist, configuration parses, and the intended agents can discover the guidance. Report removed duplication and any instruction whose ownership remains ambiguous.
