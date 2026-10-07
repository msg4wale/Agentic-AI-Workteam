---
name: test-verification-review
description: Review test changes and verification evidence for adequacy against task acceptance criteria, product behaviour, edge cases, contracts, security, regressions, and architecture-significant verification requirements.
---

# Test & Verification Review

## Purpose

Determine whether the change has enough reliable evidence to support approval.

## Map Tests to Risk

Review coverage of:

- ENG-AC;
- Product AC;
- FR/BR;
- EC;
- interface contracts;
- integration failure;
- security;
- data integrity;
- NFR where applicable.

## Test Quality

Check tests for:

- meaningful assertions;
- behaviour-level verification;
- correct fixtures;
- deterministic outcomes;
- appropriate mocks;
- failure-path coverage;
- useful names.

## Mocking Risk

Flag tests that:

- mock the function under test;
- bypass critical integration logic;
- make the test pass regardless of the real contract;
- over-specify internal implementation.

## Missing Tests

Block when a material behaviour has no credible verification and the defect risk is significant.

Do not demand tests for trivial non-behavioural edits.

## Existing Test Evidence

Review:

- commands run;
- outputs where available;
- failing checks;
- pre-existing failures.

Run targeted tests when needed to validate a finding or missing evidence.

## Build / Static Checks

Check relevant:

- lint;
- type check;
- compile/build;
- schema validation;
- migration validation;
- security/static scans where required.

## Acceptance Matrix

For each ENG-AC classify:

- PASS
- FAIL
- NOT VERIFIED

## Completion Check

Approval requires adequate evidence for critical changed behaviour.
