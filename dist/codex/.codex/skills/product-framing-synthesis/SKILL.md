---
name: product-framing-synthesis
description: Convert validated product discovery into coherent PRD framing covering product context, goals, users, value, scope, non-goals, assumptions, constraints, and dependencies without introducing new requirements.
---

# Product Framing & Scope Synthesis

## Purpose

Transform validated discovery content into the product-level framing needed at the start of a PRD.

This skill synthesizes. It does not rediscover the idea or invent product strategy.

## Inputs

Primary:

`idea.md`

Use only confirmed or appropriately labelled content.

## Build the Product Context

Synthesize:

- Problem Statement
- Product Vision
- Value Proposition
- Product Goals
- User Outcomes
- Business Outcomes
- Non-Goals

## Product Goals

Use IDs:

`PG-001`, `PG-002`, ...

A Product Goal should be:

- outcome-oriented;
- measurable where possible;
- tied to the discovered problem;
- relevant to one or more target users or business outcomes.

Do not rewrite a feature as a goal.

Bad:

> PG-001: Build a notification feature.

Better:

> PG-001: Reduce the number of submitted requests that miss required stakeholder action.

## Value Proposition

Describe:

- target user or beneficiary;
- problem addressed;
- meaningful product value;
- why the product improves the current state.

Do not add marketing claims unsupported by discovery.

## Target Users

Carry forward material personas.

Preserve:

- goals;
- pain points;
- context;
- business permissions/responsibilities.

Do not invent demographic detail.

## Scope Synthesis

Carry forward and normalize:

- Must Have
- Should Have
- Could Have
- Won't Have
- Out of Scope
- Future Enhancements

Do not change stakeholder priority silently.

If two scope statements conflict, return a decision request.

## Product Principles

Only create Product Principles if strongly supported by multiple confirmed requirements or explicit stakeholder intent.

Examples:

- Mobile-first field operation
- Auditability of every approval
- Low-connectivity usability

Label inferred principles `PM Derived`.

Do not turn them into requirements unless traceable to source requirements.

## Assumptions, Constraints and Dependencies

Preserve source identifiers.

Do not convert:

`ASM-xxx -> Confirmed`

Do not redesign around constraints.

## Output Contribution to PRD.md

Populate/refine:

- Executive Summary
- Product Context
- Product Goals
- Target Users
- Product Scope
- Constraints
- Assumptions
- relevant Dependencies

## Completion Check

Pass when:

1. Product purpose is understandable without implementation detail.
2. Goals map to the discovered problem/outcomes.
3. Users are explicit.
4. MVP and non-goals are clear.
5. Future scope is separate.
6. Assumptions and constraints remain visible.
