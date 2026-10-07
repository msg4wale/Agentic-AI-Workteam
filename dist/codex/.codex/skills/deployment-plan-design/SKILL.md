---
name: deployment-plan-design
description: When new setup or modification of an environment/infrastructure is required, break the work into a granular, ordered, risk-aware Deployment-Plan.md with dependencies, verification, and rollback, for requester approval before execution. Use before provisioning or deploying anything new or changed.
---

# Deployment Plan Design

## Purpose

Make any new setup or modification explicit and approvable **before** it is executed. Produce a granular
`Deployment-Plan.md` the requester can review and approve.

Only required when the environment is absent or needs change. If the environment already exists, is
healthy, and needs no change, skip straight to build/deploy.

## Granular tasks

Decompose the work into small, independently-verifiable steps. For each task capture:

- what it does (provision component, apply migration, configure secret reference, wire networking, …);
- the IaC/tool used;
- dependencies / order;
- risk and blast radius;
- how it is verified;
- how it is rolled back.

Order tasks by dependency; mark which are safe to run together and which must be serial. Flag any
destructive or irreversible step explicitly — it needs specific approval.

## Contents of `Deployment-Plan.md`

- Target (Local | Production) and current state summary
- Approved stack reference (from `TDD.md`)
- Ordered task table (task, IaC/tool, depends-on, risk, rollback)
- Verification plan (how "ready" and "deployed" will be proven)
- Rollback strategy
- Approvals required (plan approval; proceed-to-deploy; any destructive step)

## Approval

The plan is a **checkpoint**: present it and obtain the requester's approval before executing any of it.
Production plans require stricter, explicit approval.

## Boundaries

- Plan here; execution belongs to the provisioning/deploy skills.
- Do not include plaintext secrets in the plan; reference the secret store.
