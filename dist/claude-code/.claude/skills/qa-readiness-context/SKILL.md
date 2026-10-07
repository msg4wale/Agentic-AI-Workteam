---
name: qa-readiness-context
description: Establish QA scope, expected product behaviour, implemented build, environment, dependencies, test accounts, test data, acceptance criteria, prior findings, and blockers before test execution.
---

# QA Readiness & Context

## Purpose

Prevent invalid testing caused by unclear expected behaviour, incomplete implementation, or unsuitable environment.

## Identify QA Scope

Determine whether validating:

- QA task;
- implementation task;
- User Story;
- integrated capability;
- release slice.

## Read Source Intent

Collect relevant:

- US / Epic
- Product AC
- ENG-AC
- FR / BR / EC
- NFR
- TDD API / integration / data / security / reliability references

Do not read unrelated scope.

## Identify Implementation Under Test

Capture:

- branch/commit/build;
- changed capability;
- code-review status;
- known implementation notes.

## Environment Readiness

Confirm:

- application is runnable;
- required services exist;
- schema/migrations applied;
- feature flags/config known;
- external sandbox/stubs available;
- credentials/test accounts available;
- relevant role combinations available.

## Test Data

Identify:

- valid data;
- invalid data;
- boundary data;
- role-specific data;
- duplicate/conflict data;
- sensitive-data constraints.

Prefer synthetic data.

## Prior Findings

Review open Code Reviewer/implementation issues relevant to QA.

A known blocking code-review defect may make execution wasteful; determine whether QA should proceed on unaffected areas.

## Readiness Result

Return:

- `QA READY`
- `QA READY WITH LIMITATIONS`
- `QA NOT READY`

Classify blocker:

- Environment
- Incomplete Implementation
- Upstream Product Decision
- Upstream Architecture Decision
- Missing Test Dependency

## Completion Check

Testing begins only when expected behaviour and testability are sufficiently clear.
