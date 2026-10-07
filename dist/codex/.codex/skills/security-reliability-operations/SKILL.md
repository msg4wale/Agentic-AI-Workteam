---
name: security-reliability-operations
description: Translate PRD security, privacy, availability, edge-case, and recovery requirements into concrete security controls, resilience mechanisms, backup/recovery design, and operational behaviour.
---

# Security, Reliability & Operations

## Purpose

Design how the system protects assets, enforces trust, survives expected failures, recovers from incidents, and supports production operation.

## Security Architecture

Use security-control IDs:

`SEC-xxx`

### Identity and Authentication

Define where applicable:

- identity provider;
- authentication protocol;
- session/token model;
- MFA requirement if source requirements demand it;
- service-to-service identity.

### Authorization

Translate PRD roles/permissions into enforcement points.

Define:

- role/claim model;
- ownership checks;
- policy boundaries;
- administrative privilege;
- least privilege.

Do not change business authorization rules.

### Trust Boundaries

Identify:

- browser/client boundary;
- public/private network;
- internal service boundary;
- third-party boundary;
- privileged admin boundary.

### Data Protection

Define:

- encryption in transit;
- encryption at rest;
- sensitive-field handling;
- key ownership;
- masking/redaction where required.

### Secret Management

Define:

- secret storage;
- injection/access;
- rotation expectation;
- prohibition on credentials in source/config files.

### Audit Logging

Tie audit records to PRD requirements.

Define:

- events that must be auditable;
- actor identity;
- timestamp;
- before/after values where required;
- retention source requirement;
- tamper protection expectation.

### Threat / Abuse Considerations

Consider relevant threats:

- broken authorization;
- credential abuse;
- injection;
- malicious file/input;
- replay;
- duplicate transaction;
- brute force;
- rate abuse;
- data exfiltration;
- SSRF where relevant;
- unsafe deserialization where relevant;
- dependency compromise.

Do not mechanically add controls unrelated to the architecture.

## Reliability Design

Use:

`REL-xxx`

### Dependency Failure

For each critical dependency define:

- timeout;
- retry eligibility;
- maximum bounded retry;
- fallback/degraded behaviour;
- circuit breaking if justified;
- user-visible outcome;
- reconciliation if needed.

Avoid retries for non-idempotent operations unless protected.

### Idempotency

Define for operations susceptible to duplicate delivery/submission.

### Failure Isolation

Identify which failures must not cascade.

### Graceful Degradation

Where allowed, define reduced functionality rather than total failure.

Do not invent degraded modes that violate product requirements.

### Capacity Protection

Consider:

- request limits;
- rate limiting;
- queue bounds;
- connection pools;
- backpressure;
- workload isolation.

Only where justified.

## Backup / Restore

Define:

- protected data;
- backup method/category;
- frequency derived from RPO;
- retention if provided;
- encryption;
- restore verification;
- ownership.

## Disaster Recovery

Translate RTO/RPO to architecture.

Define:

- recovery topology;
- data recovery;
- dependency recovery;
- failover/manual recovery expectation;
- verification/test expectation.

Do not introduce multi-region active-active unless justified.

## Operational Support

Define architecture-level needs:

- administrative operations;
- audit/support tooling;
- safe reprocessing;
- reconciliation;
- operational overrides where approved;
- support visibility.

Do not create detailed runbooks here; specify what runbooks will be required.

## Output Contribution to TDD.md

Populate/refine:

- Security Architecture
- Reliability and Resilience
- Performance/Capacity protections where relevant
- Compliance/Privacy
- Technical Verification Strategy
- Technical Risks

## Completion Check

Pass when:

1. Material security requirements have enforceable controls.
2. Critical threats are addressed proportionately.
3. Dependency failures have explicit behaviour.
4. Critical duplicate/concurrency risks are controlled.
5. Backup/recovery meets source requirements.
6. Resilience complexity is justified.
