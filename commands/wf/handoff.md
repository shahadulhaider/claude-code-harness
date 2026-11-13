---
description: Write a compact durable handoff for a future session.
argument-hint: <next-action hint (optional)>
---

Load the `session-handoff` skill and persist the current state in the active plan. Tailor its next action to `$ARGUMENTS` when supplied. Do not create a competing handoff file unless the user explicitly named one.
