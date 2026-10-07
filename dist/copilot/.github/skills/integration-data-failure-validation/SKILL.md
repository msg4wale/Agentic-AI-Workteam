---
name: integration-data-failure-validation
description: Validate APIs, external integrations, data persistence, transactions, concurrency, idempotency, dependency failures, partial completion, reconciliation, migration, and data-integrity behaviour.
---

# Integration, Data & Failure Validation

## Purpose

Validate behaviour at system boundaries and under conditions where isolated happy-path tests commonly miss defects.

## API / Interface

Use relevant `API-xxx`.

Validate:

- request;
- response;
- validation;
- auth;
- errors;
- compatibility;
- idempotency;
- pagination/filtering.

## External Integration

Use `INT-xxx`.

Test where relevant:

- successful exchange;
- mapping;
- credentials/auth;
- invalid external response;
- timeout;
- service unavailable;
- duplicate callback/event;
- retry;
- reconciliation;
- rate/quota behaviour.

## Data Persistence

Validate:

- correct records written;
- no unintended records;
- relationships;
- constraints;
- state persistence;
- sensitive-data handling.

## Transactions

Validate critical atomicity:

- all succeed;
- one step fails;
- expected rollback/compensation;
- user-visible result.

## Concurrency

Where material:

- simultaneous update;
- double submission;
- race around state transition;
- lost-update risk.

## Idempotency

Repeat relevant operation using same idempotency condition and validate required outcome.

## Migration / Backfill

Where in scope validate:

- before/after data;
- default/backfill;
- constraints;
- re-runnability if designed;
- compatibility with old/new application version where required.

## Failure Injection Safety

Use controlled test techniques.

Do not create destructive production conditions.

## Completion Check

Pass when critical boundaries and data-integrity risks have evidenced results.
