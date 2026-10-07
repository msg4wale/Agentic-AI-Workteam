---
name: engineering-readiness-analysis
description: Validate PRD.md and TDD.md together for consistency, implementation-plannability, requirement coverage, architecture completeness, repository fit, and upstream blockers before task decomposition.
---

# Engineering Readiness Analysis

## Purpose

Determine whether Product Management and Solution Architecture have supplied enough stable context to decompose implementation work safely.

This skill does not repair missing product or architecture decisions by assumption.

## Inputs

Required:

- `PRD.md`
- `TDD.md`

Optional when relevant:

- existing repository;
- project engineering standards;
- existing schemas/contracts;
- migration context.

## Validate PRD/TDD Consistency

Check that:

- TDD implements the PRD's MVP scope;
- product behaviour has not changed;
- FRs and BRs have technical realization;
- critical NFRs have design responses;
- edge cases have technical behaviour;
- required integrations exist in the design;
- roles/permissions map to security architecture;
- Out of Scope/Future features have not leaked into TDD.

## Validate Implementation Boundaries

Confirm that Engineering can identify:

- components;
- APIs/interfaces;
- data ownership;
- persistence;
- integration contracts;
- authentication/authorization;
- deployment model;
- observability;
- migration implications;
- critical failure behaviour.

## Detect Upstream Gaps

Classify each gap:

### Product Gap

Examples:

- unclear acceptance behaviour;
- unresolved workflow;
- missing business rule;
- unclear MVP boundary.

Route to Product Manager.

### Architecture Gap

Examples:

- missing data owner;
- unresolved API contract;
- missing component responsibility;
- unresolved technology choice;
- undefined security mechanism;
- missing consistency strategy.

Route to Solution Architect.

### External Blocker

Examples:

- vendor specification unavailable;
- sandbox access missing;
- unknown legacy schema.

Record clearly.

## Repository Fit

For an existing system, inspect relevant implementation context.

Identify:

- architecture drift;
- reusable existing component;
- incompatible current pattern;
- required migration/refactor;
- existing tests/contracts that constrain planning.

Do not treat current code as more authoritative than approved design.

## Readiness Result

Return:

### `ENGINEERING PLANNING READY`

No material upstream gap prevents task decomposition.

### `ENGINEERING PLANNING READY WITH NON-BLOCKING ITEMS`

Known items can be isolated without forcing tasks to assume missing behaviour.

### `NOT ENGINEERING PLANNING READY`

A material product or architecture gap prevents reliable decomposition.

For each gap provide:

- classification;
- affected source IDs;
- why it blocks planning;
- upstream owner;
- required resolution.

## Output Contribution

Populate/refine:

- Upstream Open Items
- Assumptions
- Engineering Risks/Blockers
- implementation readiness status

## Completion Check

Pass when Engineering can decompose work without inventing material requirements or design decisions.
