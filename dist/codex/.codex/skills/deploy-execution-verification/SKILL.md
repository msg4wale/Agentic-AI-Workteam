---
name: deploy-execution-verification
description: Execute the deployment of the published release to the ready target environment, then verify it with smoke and health checks, rolling back safely on failure. Use after the environment is ready and proceed-to-deploy is approved.
---

# Deploy Execution & Verification

## Purpose

Deploy the published release to the ready target and prove it works — or roll back cleanly.

Runs only after the environment is confirmed ready and the requester approved **proceed to deploy**.

## Execute

- Deploy via the approved mechanism (IaC apply, pipeline, orchestrator rollout) — not by hand.
- Use a safe rollout strategy appropriate to the target (e.g. recreate for local; rolling/blue-green/
  canary for production per `TDD.md`).
- Inject configuration and **secret references** at deploy time; never bake secrets into artifacts.
- Production deploys follow stricter change control; destructive steps need explicit prior approval.

## Verify (required)

A deploy is not done until verified with evidence:

- run **smoke tests** against the deployed app (key journeys reachable);
- check **health/readiness** endpoints and dependency connectivity;
- confirm the running version matches the intended release.

Record the checks and results (feeds the Deployment Report and durable-state evidence).

## Rollback

- If verification fails, **roll back** to the last known-good release/state using the plan's rollback
  strategy, and report `ROLLED BACK` with the reason.
- Never leave the target in a half-deployed, unverified state.

## Output

Deployment outcome (`DEPLOYED — VERIFIED` or `ROLLED BACK`), the running version, verification evidence,
and access endpoints — feeds `deployment-reporting-handover`.

## Boundaries

- Deploy/verify only; environment provisioning and artifact build are separate skills.
- No unapproved destructive or production actions.
