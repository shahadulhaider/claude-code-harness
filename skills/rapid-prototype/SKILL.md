---
name: rapid-prototype
description: Builds a small disposable experiment to resolve technical feasibility, integration, performance, or interaction uncertainty. Use when evidence from a cheap prototype is more reliable than extended design discussion.
---

# Rapid Prototype

Prototype to answer a question, not to start an unbounded implementation.

## Frame the Experiment

- Name one uncertainty and the decision it blocks.
- Define the observable success signal, failure signal, time or scope limit, and what will not be built.
- Prefer the cheapest realistic seam: a throwaway script, spike branch, fixture, API probe, benchmark, or thin end-to-end tracer.

## Run It

1. Keep the experiment isolated from production paths unless integration itself is the question.
2. Use realistic inputs at the risky boundary; fake unrelated infrastructure.
3. Capture the exact command, environment constraints, and observed result.
4. Stop when the decision has enough evidence. Do not polish a disposable artifact.

## Resolve the Artifact

Report what the experiment established, what remains unknown, and the resulting recommendation. Delete throwaway code when safe, or clearly mark it and ask before retaining it. Productionize only through a separate reviewed implementation step; prototype shortcuts are not an architecture.

When an active plan exists, record the conclusion and resulting decision in the plan, not raw logs.
