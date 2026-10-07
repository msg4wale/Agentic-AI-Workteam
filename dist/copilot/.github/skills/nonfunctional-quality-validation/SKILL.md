---
name: nonfunctional-quality-validation
description: Validate in-scope non-functional quality attributes including performance, security behaviour, accessibility, compatibility, reliability, recovery, auditability, localization, and low-connectivity behaviour against explicit PRD/TDD targets.
---

# Non-Functional Quality Validation

## Purpose

Provide evidence for quality requirements that functional tests alone cannot establish.

Only test applicable requirements.

## Performance

Use exact source targets.

Capture:

- environment;
- data size;
- concurrency;
- duration;
- measured latency/throughput;
- percentile if required;
- threshold.

Do not infer production capability from unsuitable test conditions.

## Security Behaviour

Validate observable controls such as:

- authorization;
- session expiry;
- access isolation;
- rate limiting;
- input rejection;
- sensitive response/logging;
- audit trail.

Do not label this penetration testing unless that is the actual scope.

## Accessibility

Use specified standard/level.

Test relevant:

- keyboard;
- focus;
- labels/names;
- semantics;
- errors;
- contrast;
- screen-reader-critical flow.

## Compatibility

Where required test:

- browsers;
- devices;
- operating systems;
- API/client versions.

Use the supported matrix from requirements.

## Reliability / Resilience

Test source-defined behaviour:

- timeout;
- unavailable dependency;
- restart;
- retry;
- degraded behaviour;
- duplicate request;
- reconnect.

## Recovery

Where required:

- backup restore;
- RPO/RTO evidence;
- recovery procedure;
- recovered data validation.

Only in safe approved environment.

## Auditability

Validate required audit events include required actor/action/time/context and sensitive-data rules.

## Localization

Where required:

- language;
- formatting;
- date/time;
- currency;
- text overflow;
- locale rules.

## Low Connectivity / Offline

Where required:

- disconnect;
- reconnect;
- queued action;
- conflict;
- user feedback;
- data sync.

## Result

For each NFR use:

- PASS
- FAIL
- BLOCKED
- NOT TESTED — NOT IN SCOPE

Do not silently omit required NFRs.

## Completion Check

Pass when every required in-scope quality attribute has appropriate evidence.
