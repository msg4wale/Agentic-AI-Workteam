---
name: qa-verification-planning
description: Derive specific QA and technical verification tasks from PRD acceptance criteria, business rules, edge cases, NFRs, and TDD verification/security/reliability concerns.
---

# QA & Verification Planning

## Purpose

Ensure the Engineering Plan includes explicit evidence that the implemented system satisfies both product behaviour and architecture-significant technical requirements.

QA is not one generic final task.

## Source Coverage

Derive verification from:

- User Stories
- Product Acceptance Criteria
- FRs
- BRs
- Roles/permissions
- NFRs
- Edge cases
- API contracts
- Data constraints
- Integrations
- SEC controls
- REL controls
- deployment/release requirements
- TDD verification strategy

## QA Task IDs

Use:

`QA-001`, `QA-002`, ...

Create cohesive verification tasks by feature, integration, quality attribute, or test level where appropriate.

## Test Levels

Use as relevant:

- Unit
- Component
- API
- Contract
- Integration
- End-to-End
- UI
- Accessibility
- Security
- Performance/load
- Resilience/failure
- Migration/data
- Backup/restore
- Deployment/smoke
- Regression

Do not force every level onto every feature.

## Functional Verification

Cover:

- positive happy path;
- validation;
- state transitions;
- permissions;
- duplicate actions;
- alternative paths;
- error feedback;
- critical business rules.

## API / Contract Verification

Cover relevant:

- requests/responses;
- validation;
- auth;
- error codes/contracts;
- idempotency;
- pagination/filtering;
- version compatibility.

## Integration Verification

Cover:

- successful exchange;
- mapping;
- auth;
- timeout;
- dependency unavailable;
- retry/idempotency;
- reconciliation;
- duplicate callback/event;
- invalid external payload.

## NFR Verification

Create explicit work where required for:

- latency;
- throughput;
- availability;
- scale;
- security;
- accessibility;
- recovery;
- auditability.

Do not invent NFR targets.

## Test Data / Environment Needs

Each QA task should identify:

- fixtures/data;
- roles/accounts;
- external sandbox;
- environment;
- feature flags/config;
- prerequisites.

## Automation

State automation expectation when sensible:

- required automated regression;
- contract tests;
- integration automation;
- performance tooling.

Do not prescribe a tool absent a project standard or design reason.

## Traceability

Every Must-Have story must map to at least one QA task.

Critical NFRs and edge cases must have explicit verification paths.

## Output Contribution

Populate:

- QA / Verification Tasks
- Coverage Matrix
- relevant Dependencies
- Integration Checkpoints

## Completion Check

Pass when:

1. every Must-Have has verification coverage;
2. critical rules and edge cases are test-covered;
3. architecture-significant NFRs are verifiable;
4. QA tasks are specific and issue-ready;
5. test prerequisites are known.
