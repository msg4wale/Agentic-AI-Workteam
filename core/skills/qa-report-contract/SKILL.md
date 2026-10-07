---
name: qa-report-contract
description: The output contracts for QA — the defect report template and the QA-Report.md section template the QA Engineer fills in. Load when writing a defect or assembling QA-Report.md.
---

# QA Output Contracts

## Defect Report Template

Use this structure for each defect. Do not prescribe an architectural fix unless the source design already
specifies it.

```markdown
### DEF-003 — Unauthorized user can approve another user's request

**Severity:** SEV-2 — High
**Status:** Open
**Affected Task:** BE-006
**User Story:** US-008
**Requirements:** BR-004, FR-019
**Acceptance Criteria:** AC-033, ENG-AC-041
**Environment:** QA / commit abc123

#### Preconditions
- User A owns request R1
- User B has requester role but no approver authority

#### Steps to Reproduce
1. Authenticate as User B.
2. Submit approval request for R1.
3. Observe response and request state.

#### Expected Result
The action is rejected and request state remains unchanged.

#### Actual Result
The request is approved.

#### Evidence
- Response: ...
- Log/test reference: ...
- Screenshot/artifact if applicable

#### Impact
Unauthorized approval violates BR-004 and allows privilege escalation.

#### Suggested Owner
Software Engineer

#### Blocking
Yes
```

## `QA-Report.md` Output Contract

Use this structure. Remove irrelevant NFR subsections; do not create empty defect entries.

```markdown
# QA Validation Report

## Document Control
- Product:
- QA Scope:
- Task / Capability:
- Version / Commit:
- Environment:
- Date:
- QA Engineer:
- Verdict:

## Executive QA Summary

## 1. Scope
### In Scope
### Out of Scope
### Source Requirements
### Dependencies / Preconditions

## 2. Risk Assessment
| Risk Area | Risk Level | Rationale | Test Approach |
|---|---|---|---|

## 3. Test Environment
- Environment:
- Build / Commit:
- Configuration:
- Test Accounts / Roles:
- External Dependencies:
- Test Data:

## 4. Acceptance Coverage
| Source ID | Acceptance / Requirement | Test ID / Evidence | Status | Notes |
|---|---|---|---|---|
Status: PASS | FAIL | BLOCKED | NOT APPLICABLE

## 5. Functional Test Results
| Test ID | Scenario | Expected | Result | Status |
|---|---|---|---|---|

## 6. Integration / Data Test Results

## 7. Non-Functional Test Results
### Performance
### Security Behaviour
### Accessibility
### Reliability / Resilience
### Compatibility
### Other
Include only applicable areas.

## 8. Regression Results
| Area / Suite | Result | Evidence |
|---|---|---|

## 9. Automated QA Changes
| File / Test Suite | Purpose |
|---|---|

## 10. Defects
### DEF-001 — ...

## 11. Blockers / Environment Issues

## 12. Residual Risks

## 13. Evidence Summary
| Evidence | Location / Command / Artifact |
|---|---|

## 14. QA Verdict
**QA PASS | QA PASS WITH NON-BLOCKING ISSUES | QA FAIL | QA BLOCKED ...**
### Rationale
### Required Next Action

## 15. Handoff
- Software Engineer:
- Code Reviewer:
- Engineering Lead:
- Release / Integration:
```
