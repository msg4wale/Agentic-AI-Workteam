---
name: implementation-handoff-validation
description: Validate an implemented engineering task for scope fidelity, acceptance coverage, verification evidence, changed-file relevance, architecture compliance, secrets safety, documented deviations, and readiness for code review.
---

# Implementation Handoff Validation

## Purpose

Make the final decision on whether the implementation can be handed to independent review.

## Validate Task Scope

Confirm:

- every meaningful changed file is task-related;
- no unrelated refactor/package upgrade exists;
- Out of Scope was respected.

## Validate Acceptance Coverage

For each `ENG-AC-xxx` classify:

- PASS
- FAIL
- NOT VERIFIED

Do not mark PASS without evidence.

Where applicable confirm product ACs are preserved.

## Validate Verification

Confirm required:

- tests;
- lint/static checks;
- type checks;
- build;
- integration checks;
- security/performance checks

were executed.

If a required check could not run, determine whether review readiness is allowed by the task. Default to not ready for material missing verification.

## Validate Architecture

Confirm no unapproved:

- new service;
- new data store;
- API contract change;
- auth model change;
- integration change;
- major dependency;
- deployment change

was introduced.

## Validate Sensitive Information

Inspect changed content for:

- secrets;
- credentials;
- tokens;
- private keys;
- production data;
- accidental sensitive log output.

## Validate Handoff Completeness

Handoff must include:

- task ID/title;
- status;
- implemented summary;
- changed files;
- verification/results;
- acceptance coverage;
- deviations/decisions;
- known issues/follow-ups;
- review focus.

## Readiness Result

Return one:

### `READY FOR CODE REVIEW`

All required implementation and verification complete.

### `READY FOR CODE REVIEW WITH NON-BLOCKING NOTES`

Implementation complete; notes do not require reviewer to infer missing behaviour.

### `NOT READY FOR CODE REVIEW`

Any blocking acceptance, verification, scope, security, or architecture issue remains.

## Completion Check

Review handoff only after this validation passes.
