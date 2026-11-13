---
name: scope-change
description: Clarifies an ambiguous feature, refactor, migration, or design request into acceptance checks and boundaries. Use when unresolved product or technical decisions could materially change the implementation; skip for small obvious edits.
---

# Scope a Change

Align on the decisions that matter without turning routine work into an interview.

## Process

1. Inspect the repository, current behavior, documentation, and configuration to resolve factual questions yourself.
2. Build a compact decision map: desired outcome, users or callers affected, constraints, risky assumptions, and decisions still open.
3. Ask only questions whose answers can change behavior, architecture, data handling, compatibility, or rollout. Ask at most four in a round. Give a recommended default and its consequence for each.
4. Treat low-risk details as explicit assumptions and proceed. Do not ask the user to choose facts you can discover or implementation details that do not affect them.
5. Finish with a Change Contract. When a draft plan exists, merge this into its Requirements, Non-Goals, Decisions, and verification sections instead of creating another artifact:
   - Outcome
   - Acceptance checks
   - Non-goals
   - Constraints and compatibility requirements
   - Affected interfaces or data
   - Verification approach
   - Remaining assumptions

For irreversible operations, public contracts, migrations, authentication, billing, or destructive changes, obtain confirmation on the Change Contract before implementation. Otherwise, state it concisely and continue unless the user asked only for planning.
