---
name: environment-provisioning
description: Detect the current state of the target environment and infrastructure — absent, present-and-healthy, or present-but-needs-change — and provision or verify it idempotently via Infrastructure as Code, so healthy unchanged infrastructure is never rebuilt. Use before deploying.
---

# Environment Provisioning

## Purpose

Bring the target environment and infrastructure to the required, healthy state — creating it if absent,
verifying it if present, and modifying only what actually needs to change.

## Assess current state first

For the chosen target (Local or Production), determine which case applies:

- **Absent** → provision from IaC.
- **Present, healthy, and matching the required spec** → no change; proceed to deploy.
- **Present but drifted / missing components / needs modification** → plan the minimal change (hand to
  `deployment-plan-design`), then apply only the delta.

Base this on real inspection (IaC state, running resources, health) — not assumption.

## Provision / verify

- Apply the IaC from `infrastructure-as-code-authoring` for absent or changed components.
- Keep it **idempotent**: never re-provision healthy, unchanged infrastructure (Constitution §7).
- Wire configuration and **secret references** (never plaintext) per environment.
- Confirm the environment/platform is **ready**: dependencies up, health endpoints reachable, access
  paths working.

## Local vs production

- **Local**: open-source, IaC-deployable, one-command-ish bring-up where possible; parity with production
  as designed.
- **Production**: follow the approved platform; apply stricter change control and require explicit
  approval before any destructive or irreversible operation.

## Output

Environment-ready confirmation (or a precise list of what is missing/blocking), plus the state that feeds
the Deployment Report (what exists, where, health).

## Boundaries

- Provision/verify infrastructure; application build/deploy belongs to the build/deploy skills.
- Never perform a destructive change without explicit approval.
