---
name: decision-interview
description: Stress-tests a plan or design through focused decision-tree interviewing. Use for deep planning, architecture, migrations, destructive work, or unresolved product choices where user decisions could materially change the result.
---

# Decision Interview

Discover every material decision without asking the user to do repository research or choose incidental implementation details.

## Build the Frontier

1. Read the request, repository evidence, and current draft plan before asking anything.
2. Separate facts from decisions. Resolve facts with code inspection or authoritative research; ask the user only about intent, priorities, policy, and acceptable tradeoffs.
3. Treat a decision as material when it can change observable behavior, scope, architecture, data handling, migration, compatibility, rollout, or verification.
4. Infer reversible low-risk details and label them as assumptions instead of creating unnecessary questions.

## Interview in Rounds

Ask every currently unblocked material decision in one round. For each decision provide:

- the decision and why it matters now;
- two to four concrete options when useful;
- a recommended default based on current evidence;
- the consequence of accepting that default.

Avoid vague prompts such as "What do you want?" Do not ask downstream questions until their prerequisites are answered. After each answer round, update resolved decisions, detect contradictions, and compute the next frontier.

Finish only when no unresolved user-owned decision could materially alter the plan. Return resolved decisions, accepted assumptions, explicitly deferred decisions, and any remaining blockers. Never answer on the user's behalf.
