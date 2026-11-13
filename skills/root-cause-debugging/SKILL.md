---
name: root-cause-debugging
description: Diagnoses bugs, failing tests, crashes, flaky behavior, and performance regressions with a reproducible signal and falsifiable hypotheses. Use when something is broken or slow and the cause is not already proven.
---

# Root-Cause Debugging

Do not patch the first plausible line. Build evidence that distinguishes cause from symptom.

## Loop

1. Define the exact symptom, expected behavior, environment, and last known good state. Redact secrets from all output.
2. Create the tightest repeatable signal that exercises the real failure: a focused test, fixture-driven command, request replay, browser script, or benchmark. Run it before proposing a fix.
3. Reduce the failing case when practical. Remove one variable at a time while preserving the symptom.
4. Trace the relevant data and control flow. List two to four ranked hypotheses, each with a prediction that could prove it wrong.
5. Test one hypothesis at a time with the smallest probe. Prefer debugger state, targeted instrumentation, bisection, or differential runs over broad logging.
6. Fix the earliest proven cause at the narrowest responsible location. Avoid catch-all guards that only hide the symptom.
7. Turn the reproducer into a regression check at a stable interface when possible. Run both the reduced case and the original scenario.
8. Remove temporary instrumentation and artifacts. State the causal chain and the evidence that the fix breaks it.

For flaky bugs, improve the reproduction rate with repetition, fixed seeds, controlled time, stress, or synchronization before reasoning from absence. For performance issues, capture a baseline and profile before editing.

If the failure cannot be reproduced, do not invent certainty. Report what was attempted and request the smallest redacted artifact or access needed to create a useful signal.
