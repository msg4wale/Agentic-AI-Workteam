---
name: code-quality-security-review
description: Self-review the implemented change for correctness, maintainability, security, data integrity, concurrency, error handling, performance, dependency hygiene, observability, compatibility, and architecture compliance before handoff.
---

# Code Quality & Security Review

## Purpose

Perform a focused pre-review on the changed code and directly affected behaviour.

This is not a substitute for independent code review.

## Correctness

Check:

- acceptance behaviour;
- branch/edge handling;
- null/empty states;
- transaction boundaries;
- state transitions;
- error propagation;
- partial failure.

## Maintainability

Check:

- names;
- cohesion;
- duplication;
- complexity;
- unnecessary abstractions;
- consistency with repository patterns;
- comments explaining why rather than restating code.

## Security

Check as relevant:

- input validation;
- authorization;
- injection;
- path traversal;
- unsafe deserialization;
- SSRF/outbound requests;
- secret handling;
- sensitive logging;
- token/session handling;
- insecure defaults;
- file upload/content handling;
- dependency risk.

## Data Integrity

Check:

- constraints;
- uniqueness;
- concurrency;
- idempotency;
- rollback/partial transaction;
- migration safety;
- unexpected null/default behaviour.

## Reliability

Check:

- timeouts;
- retry safety;
- bounded retries;
- resource cleanup;
- dependency failure;
- graceful error outcome.

## Performance

Check task-relevant issues:

- N+1 queries;
- unbounded loops/collections;
- excessive network calls;
- large object copies;
- blocking I/O in async path;
- missing pagination/bounds.

Do not optimize without evidence.

## Observability

Check:

- required logs;
- useful context;
- correlation;
- audit events;
- metric/tracing requirements;
- sensitive data redaction.

## Compatibility

Check:

- public contract;
- schema;
- config;
- dependency versions;
- callers;
- rollout order.

## Architecture Compliance

Check against:

- ADR;
- component boundary;
- API/data ownership;
- security architecture;
- reliability design.

## Findings

Fix in-scope issues.

Escalate issues that require:

- product change;
- architecture change;
- task rescoping.

## Completion Check

Pass when no known material in-scope quality/security issue remains.
