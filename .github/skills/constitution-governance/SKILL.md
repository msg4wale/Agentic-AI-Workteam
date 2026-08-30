---
name: constitution-governance
description: Apply the project's Workteam Constitution — the durable quality and specification principles every agent is held to — and keep it tailored to the project. Use when an agent needs the standing quality/security/reliability bar, or when establishing or updating the constitution for a project.
---

# Constitution Governance

## Purpose

The `Constitution.md` at the project root states the durable principles the whole workteam is held to:
specification as source of truth, clean/readable code, reuse before rebuild, verified quality, reliability,
security by default (no plaintext secrets), reproducible IaC environments (open-source local),
human-approved resumable progression, parallelise-independent/serialise-dependent, and evidence over
claims.

This skill is how agents **honour** and **maintain** that constitution. It does not replace stage
instructions; it is the standing bar layered on top of them.

## How agents honour it

- Treat `Constitution.md` as a governing input alongside the stage's own source-of-truth hierarchy.
- When a stage instruction and the constitution both bear on quality, apply the **stricter** reading.
- Producing code/tests/infra: satisfy the relevant principles (clean code, tests-with-evidence, security
  defaults, IaC reproducibility) as part of "done", not as an afterthought.
- Reviewing/validating (Code Reviewer, QA, Plan Architect): use the constitution as an explicit checklist
  dimension; a constitution violation is a finding, ranked by its real impact.
- DevOps: enforce §6 (no plaintext secrets) and §7 (IaC, open-source local, idempotent infra) without
  exception.

## Establishing / tailoring it (per project)

- If `Constitution.md` is missing, seed it from the framework default and adapt the specifics (test
  thresholds, approved stacks, naming conventions) to the project.
- Keep it **principle-per-line and testable** — each item should be checkable against real work.
- Tailor specifics; do not delete a whole principle without the stakeholder's explicit decision (record it
  as a decision in `.workteam/Decisions-Log.md`).
- Changes to the constitution are stakeholder decisions, not silent edits.

## Boundaries

- The constitution sets the quality bar; it does not invent product requirements or architecture.
- It is guidance to honour, not a place to duplicate full stage procedures.
