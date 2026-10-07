---
name: testing-verification
description: Add or update task-relevant tests and execute evidence-based verification including targeted tests, integration/contract checks, lint/type/static analysis, build, and broader regression checks as required.
---

# Testing & Verification

## Purpose

Demonstrate that the implementation satisfies the task and does not knowingly break directly affected behaviour.

## Test Selection

Derive tests from:

- PRD Acceptance Criteria;
- Engineering Acceptance Criteria;
- FR/BR;
- edge cases;
- TDD verification concerns;
- current repository tests.

## Add / Update Tests

Cover relevant:

- happy path;
- validation;
- permissions;
- state transitions;
- error outcomes;
- duplicates/idempotency;
- concurrency;
- integration failures;
- serialization/contracts;
- data constraints.

Do not duplicate tests already providing equivalent coverage unless required for a new layer.

## Test Pyramid Discipline

Prefer the lowest practical test level that reliably proves the behaviour.

Use integration/end-to-end tests where behaviour crosses important boundaries.

Do not use E2E tests for everything.

## Verification Order

Prefer fast feedback:

1. tests directly changed/added;
2. related module/component suite;
3. static checks;
4. integration/contract tests;
5. build;
6. broader regression when required.

## Commands

Use repository-defined scripts where possible.

Record exactly what was run.

## Failure Handling

For every failure:

- capture failing check;
- inspect failure;
- classify as introduced/pre-existing/unknown;
- fix introduced failures within scope;
- rerun.

Do not simply rerun flaky tests repeatedly and declare success without investigating material flakiness.

## Environment-Limited Verification

If required verification cannot run because of:

- missing service;
- unavailable credentials;
- unsupported environment;
- missing external sandbox;

report it explicitly.

Do not substitute "code looks correct" for a required executable test.

## Evidence

Capture concise results:

```text
pytest tests/service/test_request.py -q -> PASS (12 passed)
npm run typecheck -> PASS
npm run build -> PASS
```

Do not fabricate counts.

## Completion Check

Pass only when all task-required verification has either passed or an explicitly allowed alternative has been completed.
