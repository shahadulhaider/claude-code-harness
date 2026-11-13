---
name: evidence-research
description: Researches external APIs, libraries, standards, and upstream behavior using authoritative evidence. Use when implementation or planning depends on a fact the local repository cannot establish.
---

# Evidence Research

Answer one bounded external question with evidence strong enough to support a decision.

## Method

1. State the exact question, relevant version, platform, and date constraints.
2. Search versioned official documentation, specifications, upstream source, release notes, and maintainer statements in that order. Use secondary sources only to locate primary evidence.
3. Confirm that examples and behavior match the dependency version actually used by the project.
4. Distinguish documented behavior, observed source behavior, and inference. Do not silently promote an inference to a guarantee.
5. Stop when the question is answered or the remaining uncertainty is explicit; do not produce a broad tutorial.

## Return

- concise answer;
- source URL for each material claim;
- version or date limitations;
- implications for the current decision;
- unresolved uncertainty and the smallest way to test it.

Never edit the workspace or paste large source excerpts. Redact credentials and private URLs.
