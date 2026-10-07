---
name: existing-system-discovery
description: For a brownfield idea (add, modify, update, or refactor an existing application), scan the existing codebase read-only at product/behavioral level to understand current features, journeys, behaviour, business rules, and integration points, so discovery is grounded in what already exists. Use during Idea Discovery when the idea targets an existing app; do not design architecture or implementation.
---

# Existing System Discovery

## Purpose

When the idea is not a brand-new product but a change to an existing application — a new feature on it, a
modification, an update, or a refactor — ground discovery in the **current reality** of that application.

Understand *what the system does today* at a business/behavioural level so the Product Manager inherits an
accurate "current state" and the idea is scoped against real capabilities, not guesses.

This skill discovers current behaviour. It does **not** design architecture, APIs, databases, or
implementation, and it does not write code.

## When to Apply

Only for a **brownfield** idea (existing app is present in or described for the workspace). Skip entirely
for a greenfield idea. Idea Discovery determines greenfield vs brownfield during Context Intake.

## Altitude

Product/behavioural, not technical design. You may read code to learn what the app *does*; you translate
findings into business language (features, journeys, rules), never into an implementation plan.

Reuse the search-and-inspection method of
[repository-context-analysis](../repository-context-analysis/SKILL.md) — but where that skill prepares to
implement a task, this one builds a **business-level picture of the existing system**. Stay read-only.

## What to Discover

### Current capabilities
- What features/capabilities exist today, described as user- or business-facing outcomes.
- The primary and notable secondary user journeys **as they currently work**.
- Observable behaviour of the area the idea touches (inputs, outputs, states, key rules).

### Rules & constraints in force
- Business rules, validations, permissions/roles enforced today that the change must respect or revise.
- Constraints the existing system imposes (platform, external dependencies, data already owned).

### Change surface
- Which existing features/areas the idea would **add to, modify, or remove**.
- Integration points and other capabilities that could be **affected** by the change.
- For a **refactor**: the current behaviour that must be **preserved** (the refactor's invariants) and the
  drivers for change (pain points, duplication, fragility) — at a behavioural level.

### Gaps & unknowns
- Where current behaviour cannot be determined from the workspace, record it as an open question rather
  than guessing.

## Output (feeds `idea.md`)

Produce concise, business-level findings that populate the **Existing System Context** section and enrich
the **Current Approach** and **Current Journey** sections of `idea.md`:

- Current capabilities relevant to the idea
- Current journey(s) for the affected area
- Business rules / permissions in force
- Change surface: areas added-to / modified / affected
- Refactor invariants (behaviour to preserve), if applicable
- Constraints and integration points
- Open questions about current behaviour

## Boundaries

- Read-only. Never edit code or any file except (via the agent) `idea.md`.
- No architecture, API, schema, or implementation design — that is downstream (Solution Architect).
- Do not restate large code excerpts; translate into business behaviour.
- Separate **confirmed** current behaviour (evidenced in the workspace) from **assumed** behaviour, and
  keep assumptions out of the confirmed record.
