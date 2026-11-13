# Lean Claude Code Engineering Harness

A small, opinionated workflow layer for [Claude Code](https://claude.com/claude-code) that makes an AI coding agent behave like a disciplined engineer: it plans before building, verifies before claiming success, and keeps durable state in plain Markdown instead of chat history.

It is built entirely from Claude Code's native extension points — 5 subagents, 9 slash commands, 18 skills, and one global `CLAUDE.md` — with no plugins, servers, or runtime dependencies.

## Why

Out of the box, coding agents tend to fail in predictable ways: they start implementing before scope is settled, ask the user questions the codebase could answer, lose track of multi-session work, and report checks as passing without running them. This harness addresses each of those directly:

| Failure mode | Countermeasure |
| --- | --- |
| Implementing unsettled scope | `/wf:plan` writes a reviewed plan and stops for approval; planning never edits product code. |
| Asking the user for discoverable facts | Facts go to the `Explore` agent or `researcher` subagent; only user-owned decisions reach the user, each with a recommended default. |
| Losing state across sessions | One Markdown plan per objective in `.claude/plans/` is the only durable state; status, checkboxes, and progress notes live there. |
| Unverified "done" claims | Every task names a verification signal; a box is checked only after it passes, and failed or unrun checks must be reported. |
| Self-review blind spots | Independent `reviewer` and `plan-reviewer` subagents run with fresh context. |
| Prompt bloat | Always-loaded `CLAUDE.md` stays short; detailed procedures are lazy-loaded skills. |

## Workflow

```text
             unclear direction?
                    │
             /wf:brainstorm ──► compare ≥3 materially different options
                    │
  /wf:plan ──► facts via Explore / researcher
                    │
             user-owned decisions (/wf:grill-plan for deep interviewing)
                    │
             draft plan ──► plan-reviewer ──► [APPROVED] / [REVISE]
                    │
             user approval (status: ready)
                    │
  /wf:start-work ──► vertical slice → verify → check box → progress note ─┐
                    ▲                                                     │
                    └─────────────────────────────────────────────────────┘
                    │
  /wf:review ──► reviewer subagent (findings only)
                    │
             status: complete

  Anytime: /wf:status (where am I?) · /wf:handoff (pause for another session)
```

### Example

```text
> /wf:plan add rate limiting to the public API
  … inspects routes and middleware, asks 2 decisions (per-key vs per-IP, 429 body format)
  … writes .claude/plans/api-rate-limiting.md, plan-reviewer returns [APPROVED]

> /wf:start-work api-rate-limiting
  … task 1: limiter middleware on one route, test fails → passes, box checked
  … task 2: config + remaining routes …

> /wf:status
  Active plan: api-rate-limiting   Status: in-progress   Progress: 2/4 …
```

## Contents

### Agents (`agents/`)

| Agent | Model | Purpose |
| --- | --- | --- |
| `researcher` | sonnet | Authoritative external research from versioned primary sources. |
| `reviewer` | sonnet | Independent findings-first code review. |
| `plan-interviewer` | opus | Computes the next round of unresolved user decisions for a plan. |
| `plan-reviewer` | opus | Short executability review of one plan: `[APPROVED]` or `[REVISE]`. |
| `project-state` | haiku | Status report from plans and the Git worktree. |

Claude Code's built-in `Explore` (read-only discovery) and `general-purpose` (bounded delegated work) agents are used as-is. Model choice follows the task: judgment-heavy planning on `opus`, review and research on `sonnet`, mechanical status on `haiku`.

### Commands (`commands/wf/`)

All commands are namespaced under `wf:` so they never collide with Claude Code built-ins.

| Command | Purpose |
| --- | --- |
| `/wf:brainstorm` | Compare divergent options without planning or implementing. |
| `/wf:plan` | Create or revise a reviewed durable plan. |
| `/wf:grill-plan` | Run deep iterative decision interviewing on a draft. |
| `/wf:shape` | Produce a compact Change Contract. |
| `/wf:start-work` | Approve, start, or resume one plan. |
| `/wf:status` | Report concise plan and worktree state. |
| `/wf:review` | Run independent review via the `reviewer` subagent. |
| `/wf:handoff` | Persist pause state into the active plan. |
| `/wf:refine-workflow` | Apply one evidence-backed harness improvement. |

### Skills (`skills/`)

Skills are lazy-loaded playbooks; Claude loads one when its description matches the task.

- **Alignment and planning:** `plan-workflow`, `brainstorm`, `scope-change`, `decision-interview`, `ticket-slicing`, `domain-modeling`, `boundary-design`
- **Delivery:** `delivery-loop`, `execute-plan`, `behavior-first-testing`, `root-cause-debugging`, `rapid-prototype`, `merge-conflict-resolution`
- **Evidence and quality:** `evidence-research`, `change-review`
- **Continuity and maintenance:** `session-handoff`, `agent-document-design`, `refine-harness`

### Global rules

[`CLAUDE.md`](CLAUDE.md) holds concise cross-project engineering and safety rules (smallest coherent change, reproduce before fixing, never claim an unrun check passed, no commits or pushes unless asked). Project-level `CLAUDE.md` files take precedence. [`settings.json`](settings.json) requires confirmation for `git commit`, `push`, `reset`, and `clean`.

## Plan lifecycle

Plans live at `.claude/plans/<short-slug>.md` in each project, with statuses `draft` → `ready` → `in-progress` (↔ `blocked`) → `complete`, or `abandoned`.

1. `/wf:plan` discovers facts, resolves user-owned decisions, writes a `draft`, and runs `plan-reviewer`.
2. User approval sets `ready`. `/wf:start-work` also counts as approval for one reviewed draft with no open questions.
3. `/wf:start-work` sets `in-progress` and works through dependency-aware vertical tasks.
4. A task is checked only after its named outcome exists and its verification passes.
5. `/wf:status` derives state from the plan and worktree; `/wf:handoff` updates the same plan rather than creating another state file.
6. The plan is `complete` only after every task and Final Verification Wave item passes.

See [`skills/plan-workflow/SKILL.md`](skills/plan-workflow/SKILL.md) for the full plan template.

## Design decisions

- **The main agent owns implementation and synthesis.** Subagents are one level deep and scoped to research, review, interviewing, or status. They are instructed never to edit files, and their tool lists exclude `Edit`/`Write`; `Bash` is retained so they can run `git` and test commands.
- **Planning runs in the main agent**, not a subagent, because interactive multi-round interviewing cannot happen inside a one-shot subagent. Built-in Plan Mode is not used because it cannot write the project-local plan store.
- **Markdown plans are the only durable state** — no database, plugin, or parallel handoff file — so state is diffable, reviewable, and readable by humans.
- **Progressive disclosure:** always-loaded context is ~40 lines; everything situational lives in skills that load on demand.
- **The harness refines itself conservatively:** `/wf:refine-workflow` applies one evidence-backed change at a time and validates it, rather than letting prompts grow autonomously.

The harness was originally developed for [OpenCode](https://opencode.ai) and ported to Claude Code; the port replaced custom explore/general agents with Claude Code's built-ins and per-agent permission blocks with tool lists plus global permission rules.

## Install

Clone outside `~/.claude` and symlink the pieces, so your existing credentials, history, and local settings are untouched:

```sh
git clone https://github.com/shahadulhaider/claude-code-harness.git ~/src/claude-harness
cd ~/src/claude-harness
mkdir -p ~/.claude
for item in agents commands skills CLAUDE.md; do
  [ -e ~/.claude/$item ] && echo "skip: ~/.claude/$item exists" || ln -s "$PWD/$item" ~/.claude/$item
done
```

Merge the `permissions.ask` rules from `settings.json` into your own `~/.claude/settings.json` if you want the same Git safety prompts. Start a new Claude Code session and type `/wf:` to see the commands.

## Validation

`scripts/validate.py` checks that every agent, command, and skill has valid frontmatter, that every referenced skill and agent exists, that this README's agent models match the agent files, and that `settings.json` parses. It runs in CI on every push:

```sh
python3 scripts/validate.py
```

## License

[MIT](LICENSE)
