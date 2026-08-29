---
name: plan-validation-reporting
description: Assemble the Plan-Validation-Report.md from codebase reuse analysis and duplication detection findings, set the APPROVE or REVISE verdict, and route specific loop-back items to the Engineering Lead. Use as the final step of plan validation.
---

# Plan Validation Reporting

## Purpose

Consolidate the reuse and duplication findings into a single, decision-ready
`Plan-Validation-Report.md`, set a verdict that follows the findings, and produce specific loop-back
items so the Engineering Lead can revise the plan without guessing.

This skill reports and routes. It does not change the plan or the code.

## Inputs

- Reuse candidates from [codebase-reuse-analysis](../codebase-reuse-analysis/SKILL.md).
- Classifications and duplication flags from
  [plan-duplication-detection](../plan-duplication-detection/SKILL.md).

## Verdict Rules

Set the verdict strictly from the findings:

- **REVISE** — any blocking duplication flag or ignored mandatory reuse target exists.
- **APPROVE WITH REUSE NOTES** — no blocking flags, but non-blocking reuse opportunities remain.
- **APPROVE** — no blocking flags and no material reuse notes.
- **BLOCKED** — the plan, PRD/TDD, or repository access was insufficient to validate.

Never soften a REVISE into an APPROVE to avoid a loop; never escalate a non-blocking note into REVISE.

## Loop-Back Items (REVISE)

Each loop-back item must be actionable by the Engineering Lead and name:

- the plan task ID;
- the existing functionality to reuse/extend (path + symbol);
- the required change to the plan step;
- why it is blocking (duplication / mandatory reuse / codebase conflict).

## Report Assembly

Produce `Plan-Validation-Report.md` using the Plan Architect output contract:

- Status (verdict, plan ref, timestamp)
- Summary
- Per-Task Findings table
- Reuse Opportunities
- Duplication Flags
- Loop-Back Items for Engineering Lead
- Non-Blocking Reuse Notes (for Software Engineer)
- Open Questions

## Routing

- **REVISE** → hand the loop-back items back to `engineering-lead`; implementation must not start.
- **APPROVE / APPROVE WITH REUSE NOTES** → forward the report (and any non-blocking notes) to the
  next stage; the Coordinator releases the Software Engineer.
- **BLOCKED** → state exactly what is missing and who must provide it.

## Boundaries

- Only create or modify `Plan-Validation-Report.md`.
- Never edit `Engineering-Plan.md` or production code.
- The verdict must be reproducible from the evidence in the report.
