---
name: requirement-architecture-compliance
description: Validate an implementation against its Engineering-Plan task, PRD behaviour, TDD architecture, interfaces, data ownership, security/reliability controls, observability requirements, and scope boundaries.
---

# Requirement & Architecture Compliance

## Purpose

Detect implementation that may work locally but violates approved product or technical design.

## Task Compliance

Confirm implementation satisfies:

- Objective
- Scope
- Technical Constraints
- Interface/Data Impact
- ENG-AC
- Out of Scope

## Product Compliance

Check relevant:

- User Story
- PRD Acceptance Criteria
- FR
- BR
- roles/permissions
- EC
- NFR

Do not reinterpret product requirements.

## Architecture Compliance

Check relevant:

- ADR
- component responsibility
- API/interface
- data ownership
- transaction/consistency
- integration contract
- security control
- reliability mechanism
- deployment/config constraint
- observability requirement

## Architecture Drift

Examples:

- direct database access bypasses owning component;
- new endpoint breaks `API-004`;
- new queue introduced outside TDD;
- client enforces a rule that must be server authoritative;
- required audit event omitted;
- retry semantics differ from `INT-003`.

Flag drift based on source design, not preference.

## Scope Leakage

Flag:

- Future scope;
- Out-of-Scope behaviour;
- unrelated refactor;
- undocumented feature;
- unrelated dependency change.

## Missing Required Work

Check that implementation includes all relevant required changes:

- config;
- telemetry;
- migration;
- documentation;
- security;
- tests.

## Completion Check

Pass when implementation is faithful to both product intent and technical design.
