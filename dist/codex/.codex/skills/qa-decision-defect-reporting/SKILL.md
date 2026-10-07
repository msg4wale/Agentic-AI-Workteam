---
name: qa-decision-defect-reporting
description: Classify QA results, create reproducible severity-ranked defect reports, distinguish implementation defects from environment/upstream blockers, and produce a QA verdict consistent with acceptance and quality evidence.
---

# QA Decision & Defect Reporting

## Purpose

Convert test evidence into a defensible QA decision and actionable defect handoff.

## Before Logging a Defect

Confirm:

- expected result is supported;
- implementation/build tested is known;
- environment is suitable;
- issue is reproducible or evidence is strong;
- test itself is not faulty.

## Defect Fields

Use `DEF-xxx`.

Capture:

- Title
- Severity
- Status
- Task
- Story
- Requirements
- Acceptance Criteria
- Environment/build
- Preconditions
- Reproduction
- Expected
- Actual
- Evidence
- Impact
- Suggested owner
- Blocking

## Severity

Use impact, not effort.

- SEV-1 Critical
- SEV-2 High
- SEV-3 Medium
- SEV-4 Low

## Classification

Where useful classify:

- Functional
- Authorization
- Data
- Integration
- Performance
- Accessibility
- Reliability
- Compatibility
- Regression
- Environment
- Test Automation

Environment/test defects are not automatically product defects.

## Ownership Routing

Implementation defect:
`Software Engineer`

Product ambiguity:
`Product Manager`

Architecture/quality-design ambiguity:
`Solution Architect`

Task/test-scope ambiguity:
`Engineering Lead`

Code-design concern with correct behaviour:
`Code Reviewer`

## Verdict Rules

### QA PASS

All required criteria pass; no blocking defects.

### QA PASS WITH NON-BLOCKING ISSUES

Only explicitly non-blocking issues remain.

### QA FAIL

At least one required acceptance/NFR fails or blocking defect exists.

### QA BLOCKED

Valid decision cannot be made due to environment, upstream decision, or incomplete implementation.

## Defect Retest

After a fix:

- use same defect ID;
- record fixed build;
- rerun reproduction;
- run relevant regression;
- update status.

Do not close solely because code changed.

## Completion Check

The verdict must be derivable from the recorded results without relying on subjective optimism.
