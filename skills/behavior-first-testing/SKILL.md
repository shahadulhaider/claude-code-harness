---
name: behavior-first-testing
description: Applies a practical red-green-cleanup loop for features and bug fixes. Use when the user requests TDD or when a behavior change has a stable observable test seam; avoid forcing unit tests onto configuration, generated code, or unsuitable legacy seams.
---

# Behavior-First Testing

Protect observable behavior, not implementation shape.

## Select the Test Surface

- Identify the closest stable interface used by real callers.
- Express one behavior in domain language: setup, action, observable result.
- Prefer existing test style and the lowest-cost level that still exercises the real path.
- Mock only slow, nondeterministic, destructive, or truly external boundaries. Do not mock the code whose behavior is under test.

## Cycle

1. Red: add one focused test and run it. Confirm it fails for the intended missing behavior, not because of setup or a typo.
2. Green: implement only enough production code to satisfy that behavior. Run the focused test.
3. Cleanup: improve names and structure without changing behavior. Re-run the focused test and nearby tests.
4. Repeat for the next behavior.

Use independent expected values from requirements, examples, or known fixtures. Avoid assertions that recompute the implementation, snapshots for logic that deserves explicit assertions, private-method tests, and broad mock interaction tests.

If no stable automated seam exists, say why and create the tightest alternative signal, such as a CLI fixture, HTTP probe, integration harness, or reproducible manual check. Do not add a misleading shallow test merely to claim coverage.

At completion, run the relevant suite and confirm the new test would fail if the new behavior were removed.
