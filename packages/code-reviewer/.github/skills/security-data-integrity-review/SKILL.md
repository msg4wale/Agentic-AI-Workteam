---
name: security-data-integrity-review
description: Review changed code for material security vulnerabilities, authorization failures, input trust issues, secret/sensitive-data exposure, unsafe integrations, migration risks, transaction defects, concurrency, and data corruption.
---

# Security & Data Integrity Review

## Purpose

Identify security and data-safety defects introduced or exposed by the change.

Use risk-based review.

## Authorization

Check:

- enforcement happens server-side / authoritative layer;
- ownership/tenant checks;
- privilege escalation;
- admin boundaries;
- IDOR-style access.

## Authentication / Session

Where relevant:

- token validation;
- expiry;
- session fixation;
- insecure cookie/token handling;
- trust of client-provided identity.

## Input / Injection

Check relevant:

- SQL/NoSQL injection;
- command injection;
- template injection;
- XSS;
- path traversal;
- SSRF;
- malicious file content;
- unsafe deserialization.

## Sensitive Information

Check:

- secrets in code/config;
- production data;
- sensitive logs;
- tokens in URLs;
- excessive response fields;
- stack traces.

## Cryptography

Flag:

- custom crypto;
- weak/insecure algorithms;
- hard-coded keys;
- insecure randomness.

Do not demand cryptography where no requirement exists.

## External Requests

Check:

- validation of destination;
- TLS expectations;
- timeout;
- auth;
- response trust;
- SSRF risk;
- retry safety.

## Data Integrity

Check:

- transaction atomicity;
- uniqueness;
- referential integrity;
- partial writes;
- concurrency races;
- lost updates;
- idempotency;
- precision/truncation;
- migration/backfill correctness.

## Migrations

Review for:

- destructive changes;
- lock/downtime risk;
- missing backfill;
- incompatible rollout ordering;
- unsafe rollback assumptions.

## Severity

Use P0/P1 for realistic critical/high impact, not speculative theoretical issues.

## Completion Check

Pass when material security and data-integrity surfaces touched by the change have been assessed.
