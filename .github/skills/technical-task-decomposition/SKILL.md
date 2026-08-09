---
name: technical-task-decomposition
description: Decompose PRD and TDD scope into cohesive, independently verifiable backend, frontend, data, integration, platform, security, observability, documentation, and other engineering tasks with complete source traceability.
---

# Technical Task Decomposition

## Purpose

Convert product scope and architecture into executable engineering outcomes.

Do not implement the work.

## Coverage First

Before creating task titles, build a mental coverage map:

```text
US / FR / BR / NFR / EC
        |
        v
ADR / COMP / API / DATA / INT / SEC / REL / DEP / OBS
        |
        v
Required implementation outcomes
```

Do not begin with arbitrary frontend/backend lists.

## Workstream Selection

Create only workstreams required by the design.

Common prefixes:

- `BE` Backend
- `FE` Frontend/client
- `DB` Database/schema
- `DATA` Migration/data processing
- `INT` External integration
- `PLAT` Platform/DevOps
- `SEC` Security-specific
- `OBS` Observability/operations
- `DOC` Documentation/enablement

QA is decomposed by the QA skill.

## Cohesion Test

A task should:

- have one dominant engineering outcome;
- be independently reviewable;
- have clear completion criteria;
- have meaningful source traceability;
- avoid spanning unrelated components.

Split a task when it contains multiple independently deployable/reviewable concerns.

Keep work together when splitting would create artificial file-level fragments.

## Backend Decomposition

Consider:

- application/service logic;
- APIs;
- validations;
- business-rule enforcement;
- authorization;
- transactions;
- persistence;
- background processing;
- integration orchestration;
- idempotency;
- errors;
- telemetry.

## Frontend Decomposition

Consider:

- journey/screen flow;
- state management;
- forms/validation;
- permissions/visibility;
- API integration;
- error/loading/empty states;
- accessibility;
- responsive behaviour;
- analytics;
- component tests.

## Data Decomposition

Consider:

- schema;
- constraints;
- indexing;
- migration/backfill;
- retention;
- data transformation;
- reconciliation;
- rollback risk.

## Integration Decomposition

Consider:

- client/adapter;
- authentication;
- mapping;
- resilience;
- reconciliation;
- webhook/event handling;
- sandbox/test capability.

## Platform Decomposition

Consider:

- infrastructure;
- network;
- secrets/config;
- runtime;
- pipeline;
- environment;
- backup/recovery;
- deployment/rollback.

## Security / Observability

Do not forget cross-cutting work when architecture requires it.

Embed small concerns into owning implementation tasks.

Create standalone `SEC`/`OBS` tasks only when substantial and independently verifiable.

## Task Source Fields

Each task must reference relevant:

- Epic/User Story;
- FR/BR/NFR/EC;
- ADR;
- Component;
- API;
- Data entity/store;
- Integration;
- Security/reliability/deployment design.

Do not require every field when not relevant.

## Implementation vs Architecture

If decomposition exposes a missing design decision, stop and route it to Solution Architecture.

Do not use the engineering task itself to make a consequential new architecture decision.

## Output Contribution

Produce/refine implementation tasks in Engineering-Plan.md.

## Completion Check

Pass when:

1. all MVP implementation work is represented;
2. every task is cohesive;
3. no task duplicates another;
4. source traceability exists;
5. cross-cutting technical work is not omitted;
6. no major architecture decision was invented.
