---
name: tdd-validation
description: Validate TDD.md for fidelity to the PRD, architecture completeness, technical consistency, traceability, security, reliability, operability, interface/data completeness, justified complexity, and readiness for Engineering Planning.
---

# TDD Validation

## Purpose

Determine whether `TDD.md` gives the Engineering Lead enough technical context to create implementation tasks without inventing major architecture.

Validation does not repair missing product requirements by assumption.

## Validation Classifications

Use:

- Pass
- Non-Blocking Gap
- Engineering-Planning-Blocking Gap
- Product Requirement Conflict
- Architecture Contradiction
- Unvalidated Technical Assumption
- Missing Decision
- Traceability Gap
- Interface Gap
- Data Gap
- Security Gap
- Reliability Gap
- Operability Gap
- Unjustified Complexity
- Premature Task Decomposition

## Validate PRD Fidelity

Confirm:

- every architecture-significant design maps to a PRD requirement/constraint or explicit architecture rationale;
- no user behaviour changed;
- no NFR target was silently relaxed;
- no business rule was reinterpreted;
- out-of-scope features were not introduced.

## Validate Architecture Drivers

Confirm:

- critical FRs/NFRs/constraints are recognized;
- architecture-significant quality attributes have design responses;
- material uncertainties are assumptions/risks.

## Validate Decisions

For consequential ADRs verify:

- context exists;
- alternatives are credible;
- rationale uses real drivers;
- trade-offs are explicit;
- consequences are understood.

Flag "we chose X because it is scalable" without requirement-specific rationale.

## Validate System Structure

Confirm:

- boundaries are clear;
- components have coherent responsibilities;
- every major component is justified;
- major product capabilities have technical owners;
- interactions are understandable end-to-end.

## Validate Data Architecture

Confirm:

- ownership is explicit;
- key relationships are understood;
- persistence strategy is justified;
- transaction boundaries are explicit;
- concurrency/consistency needs are addressed;
- lifecycle/retention/sensitivity are handled.

## Validate Interfaces

Confirm critical APIs/integrations define:

- consumer/provider;
- purpose;
- contract;
- validation;
- auth;
- errors;
- timeout/failure;
- idempotency where needed;
- related requirement.

## Validate Security

Confirm:

- trust boundaries;
- identity/authentication;
- authorization;
- secrets;
- encryption;
- audit;
- material threats;
- sensitive data handling.

## Validate Reliability

Confirm:

- critical dependencies have failure behaviour;
- timeouts/retries are bounded and safe;
- duplicate-sensitive operations are idempotent;
- backup/restore exists where required;
- RPO/RTO are addressed;
- overload behaviour is addressed where material.

## Validate Deployment / Operations

Confirm:

- runtime topology;
- environments;
- network exposure;
- configuration;
- scaling;
- deployment/rollback;
- observability;
- health signals;
- actionable alerting.

## Validate Complexity

Flag architecture elements with no clear driver, especially:

- microservices;
- queues;
- caches;
- multiple data stores;
- event buses;
- Kubernetes;
- multi-region;
- service mesh.

Complexity is acceptable when justified.

## Validate Traceability

Check:

```text
PRD requirement
 -> Architecture Driver
 -> ADR
 -> Component / Interface / Control
 -> Verification concern
```

Not every requirement needs an ADR, but every critical requirement needs a clear realization.

## Validate Engineering Planning Boundary

Flag content that has become implementation planning:

- `BE-001`
- `FE-001`
- `QA-001`
- task assignment
- story points
- sprint assignment
- developer estimates
- pull request instructions

The Architect may specify design work, not work-item decomposition.

## Result

Return exactly one:

### `ENGINEERING PLANNING READY`

No material technical gap remains.

### `ENGINEERING PLANNING READY WITH NON-BLOCKING OPEN ITEMS`

Remaining questions are documented and do not force the Engineering Lead to invent major architecture.

### `NOT ENGINEERING PLANNING READY`

At least one blocking design gap, contradiction, product conflict, or critical unknown remains.

For every failure report:

- Issue
- Classification
- Affected TDD section
- Related PRD requirement
- Why it matters
- Skill to revisit or upstream owner
- Decision/information required

## Completion Check

Validation is complete only when:

1. PRD fidelity has been checked.
2. Architecture drivers and decisions are coherent.
3. Components, data and interfaces are complete enough for planning.
4. Security/reliability/operability are addressed.
5. Complexity is justified.
6. Traceability is sufficient.
7. No task decomposition has leaked into the TDD.
8. A clear readiness result is returned.
