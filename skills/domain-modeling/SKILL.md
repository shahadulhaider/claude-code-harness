---
name: domain-modeling
description: Models domain concepts, invariants, lifecycles, and state transitions before changing business logic or persisted data. Use when terminology is ambiguous or rules currently leak across modules.
---

# Domain Modeling

Make the business rules and ownership explicit before choosing code structure.

## Discover the Model

- Extract terms from user language, existing interfaces, schemas, tests, and events. Resolve synonyms and overloaded names.
- Identify identities, immutable values, stateful records, actors, commands, events, and external systems only where they clarify behavior.
- Write invariants as testable statements and map legal state transitions, including failure, retry, cancellation, and deletion.
- Name who owns each rule and transaction boundary. Identify consistency, idempotency, ordering, and retention requirements.

## Test the Model

Walk representative happy paths and adversarial cases through the proposed states. Look for impossible states, duplicated authority, temporal ambiguity, and rules that rely on callers remembering hidden requirements.

## Produce a Useful Result

Return a concise glossary, invariants, transition table or lifecycle, ownership boundaries, and unresolved policy decisions. Translate the model into code types or database changes only after the behavior is stable. Do not introduce classes, repositories, aggregates, or events solely to imitate a modeling style.

Record durable terminology and invariants in the active plan's Decisions or Requirements section when one exists.
