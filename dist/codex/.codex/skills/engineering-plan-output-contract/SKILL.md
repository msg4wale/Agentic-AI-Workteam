---
name: engineering-plan-output-contract
description: The output contract and section template for Engineering-Plan.md — the structure the Engineering Lead fills in (workstreams, coverage matrix, task sections, dependency matrix, waves, parallel groups, critical path). Load when assembling or validating Engineering-Plan.md.
---

# `Engineering-Plan.md` Output Contract

Use this structure. Each task uses the Issue-Ready Task Contract (self-contained, acceptance-linked).
Remove workstream sections that genuinely do not apply; do not create empty task categories.

```markdown
# Engineering Implementation Plan

## Document Control
- Product:
- Version:
- Status:
- Last Updated:
- Engineering Lead:
- Implementation Readiness:
- Source PRD: PRD.md
- Source TDD: TDD.md

## Executive Engineering Summary

## 1. Implementation Scope
### 1.1 MVP Engineering Scope
### 1.2 Engineering Non-Goals
### 1.3 Constraints
### 1.4 Assumptions
### 1.5 Upstream Open Items

## 2. Implementation Workstreams
| Workstream | Scope | Primary Architecture Components | Task Count |
|---|---|---|---|

## 3. Coverage Matrix
| Product / Technical Requirement | Architecture Reference | Implementation Task(s) | Verification Task(s) | Coverage Status |
|---|---|---|---|---|

## 4. Backend Tasks
### BE-001 — ...
[Use Issue-Ready Task Contract]

## 5. Frontend Tasks
### FE-001 — ...

## 6. Database / Data Tasks
### DB-001 — ...

## 7. Integration Tasks
### INT-001 — ...

## 8. Platform / DevOps Tasks
### PLAT-001 — ...

## 9. Security Tasks
### SEC-001 — ...

## 10. Observability / Operations Tasks
### OBS-001 — ...

## 11. QA / Verification Tasks
### QA-001 — ...

## 12. Documentation / Enablement Tasks
### DOC-001 — ...

## 13. Dependency Matrix
| Task | Depends On | Blocks | External Dependencies |
|---|---|---|---|
Task dependency columns must use task IDs only.

## 14. Implementation Waves
### Wave 0 — Foundations
### Wave 1 — ...
### Wave 2 — ...

## 15. Parallel Execution Plan
| Parallel Group | Execution Wave | Tasks | Parallel-Safe | Shared Write Risk | Integration Checkpoint |
|---|---|---|---|---|---|
Each group contains tasks that may be assigned to separate Software Engineer agents concurrently.

## 16. Parallelization Opportunities
List additional conditional concurrency opportunities and the condition that unlocks them.

## 17. Critical Path
List the task-ID chain(s) that constrain implementation completion. Do not estimate duration unless requested.

## 18. Integration Checkpoints
Define points where independently developed workstreams must be integrated and verified.

## 19. Engineering Risks and Blockers
| ID | Risk / Blocker | Affected Tasks | Impact | Owner / Upstream Owner | Resolution Needed |
|---|---|---|---|---|---|

## 20. Open Engineering Questions
| Question | Affected Tasks | Blocking? | Owner | Required Before |
|---|---|---|---|---|

## 21. Handoff Summary
Summarize readiness for Software Engineering, QA, Platform and other implementation roles.
```

Platform / DevOps tasks (section 8) should reflect the approved Local and Production stacks and IaC
approach from `TDD.md` (Deployment & Infrastructure Stack), so the DevOps Engineer's work is planned, not
improvised.
