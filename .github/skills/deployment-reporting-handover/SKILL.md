---
name: deployment-reporting-handover
description: Produce the Deployment-Report.md handover after a verified deployment — how to access the application, how to reach every deployed system/infrastructure component, verification evidence, IaC/reproducibility, and rollback — with credentials referenced from a secure store, never embedded. Use as the final DevOps step.
---

# Deployment Reporting & Handover

## Purpose

Give the requester everything needed to use and operate the deployed system, with secrets handled safely.

## Contents of `Deployment-Report.md`

- **Target & outcome** — Local | Production, and the verdict (`DEPLOYED — VERIFIED`, running version).
- **Application access** — URL(s)/entry point(s) and how to reach/run the app.
- **Deployed systems & infrastructure** — each component (datastore, cache, queue, dashboards, etc.),
  where it runs, and how to access it.
- **Credentials** — where each credential is stored (secret manager / environment) and the **retrieval
  steps**. Never write a secret value into the report.
- **Verification evidence** — the smoke/health checks run and their results.
- **IaC & reproducibility** — where the IaC lives and how to re-apply/destroy it.
- **Rollback** — how to roll this release back.

## Security rules (non-negotiable)

- **No plaintext secrets** anywhere in the report (Constitution §6). Reference the secure store and how to
  retrieve, e.g. "DB password: in `secretsmanager://app/prod/db` — retrieve with `<command>`".
- Do not include private keys, tokens, or connection strings containing embedded credentials.
- Prefer least-privilege access instructions; note who should have access, not the access itself.

## Handover

Return a concise summary (target, outcome, access entry point, report location) to the Coordinator; the
full detail lives in `Deployment-Report.md`.

## Boundaries

- Report only; do not change infrastructure here.
- If a required access detail would expose a secret, replace it with a secure retrieval instruction.
