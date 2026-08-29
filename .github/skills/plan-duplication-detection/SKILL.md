---
name: plan-duplication-detection
description: Compare each engineering-plan task against the existing codebase, classify it as reuse-existing, extend-existing, or build-new, and flag any step that would re-implement functionality the repository already provides. Use after codebase reuse analysis, during plan validation.
---

# Plan Duplication Detection

## Purpose

Turn the reuse candidates found by [codebase-reuse-analysis](../codebase-reuse-analysis/SKILL.md) into
an explicit, per-task verdict: does this plan step reuse what exists, extend it, or build something
new — and if new, does it duplicate functionality already present?

This skill classifies and flags. It does not modify the plan or the code.

## Classification

For each plan task, assign exactly one classification:

- **reuse-existing** — the repository already provides the capability; the task should call/apply it as-is.
- **extend-existing** — an existing pattern/utility/module covers most of it; the task should extend or
  configure it rather than start fresh.
- **build-new** — no adequate existing counterpart; net-new code is justified.

Every classification must cite evidence (path + symbol, or "none found").

## Duplication Flag

Raise a **duplication flag** when a task is written as build-new (or extend where a cleaner reuse
exists) but the codebase already provides equivalent functionality. For each flag record:

- the plan step and its stated approach;
- the existing functionality it duplicates (path + symbol + short description);
- the required action (reuse X / extend X / justify why a new implementation is necessary).

## Severity

- **Blocking** — clear duplication of existing functionality, or a mandatory reuse target ignored
  without justification. Forces a REVISE verdict.
- **Non-blocking** — a reasonable reuse opportunity that improves consistency but is not strictly
  required; attached as a note for the Software Engineer.

## Justified New Implementation

A build-new that overlaps existing code is acceptable **only** with an explicit reason, such as:

- the existing code is deprecated or being replaced by this very plan;
- the existing implementation cannot meet a mandatory PRD/TDD requirement;
- reuse would create an unacceptable coupling the TDD forbids.

Record the justification. Absent one, the overlap is a blocking duplication flag.

## Output

Per task: `Task ID | Classification | Existing target(s) | Duplication? (Y/N) | Severity | Required action`.

Aggregate the blocking flags — they drive the REVISE loop-back items in
[plan-validation-reporting](../plan-validation-reporting/SKILL.md).

## Boundaries

- Read-only. Never edit code or the plan.
- Classify from evidence, not assumption; when the existing code's fitness is genuinely ambiguous,
  surface it as an open question rather than forcing a classification.
