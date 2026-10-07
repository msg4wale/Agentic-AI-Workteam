---
name: task-readiness-analysis
description: Validate one assigned Engineering-Plan task before implementation, including source traceability, dependencies, scope, acceptance criteria, architecture references, external prerequisites, and upstream blockers.
---

# Task Readiness Analysis

## Purpose

Prevent implementation from starting on an ambiguous, blocked, or internally inconsistent task.

## Required Inputs

- Assigned task ID or full task text
- `Engineering-Plan.md`
- relevant `PRD.md` sections
- relevant `TDD.md` sections

## Validate Task Identity

Confirm:

- task exists;
- task ID/title match;
- task is not Deferred or Out of Scope;
- task status permits implementation.

## Validate Source Traceability

Confirm the task identifies or can clearly map to:

- User Story/Epic where applicable;
- FR/BR/NFR/EC;
- architecture component/interface/data/integration;
- engineering acceptance criteria.

Do not require irrelevant reference types.

## Validate Scope

Confirm:

- Objective is clear.
- Scope describes required outcome.
- Out of Scope is explicit enough to prevent obvious creep.
- Technical constraints are known.
- Interface/data impact is sufficiently defined.

## Validate Dependencies

Check:

- `Depends On` task IDs;
- predecessor state where visible;
- external dependencies;
- environment/credentials/sandbox needs.

Do not assume a dependency is complete if evidence is absent and its completion is required for safe implementation.

A fixed contract may allow implementation before a provider implementation is complete. Distinguish contract dependency from runtime dependency.

## Validate Acceptance Criteria

Acceptance criteria must be testable.

Flag:

- "works correctly";
- "handles errors";
- "is secure";
- unspecified expected state;
- missing response/error outcome where required.

## Detect Blocking Gap

Classify:

### Product
Missing/contradictory behaviour or business rule.

### Architecture
Missing component/API/data/security/technology decision.

### Task Definition
Task decomposition/scope/dependency ambiguity.

### External
Vendor, credential, access, environment, upstream service.

## Result

Return:

- `TASK READY`
- `TASK READY WITH NON-BLOCKING NOTES`
- `TASK NOT READY`

For each blocking item include:

- issue;
- source;
- owner;
- exact resolution needed.

## Completion Check

Implementation may begin only if no material behaviour/design must be invented.
