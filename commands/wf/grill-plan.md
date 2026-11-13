---
description: Deeply interview unresolved decisions in a draft plan.
argument-hint: <plan-name (optional)>
---

Load the `plan-workflow` skill. Deeply stress-test the draft plan matching `$ARGUMENTS`, or the uniquely active draft when no argument is supplied. Invoke the `plan-interviewer` subagent, present each decision frontier to the user, incorporate the answers into the plan, then run the `plan-reviewer` subagent. Stop with the reviewed draft and wait for approval; never implement.
