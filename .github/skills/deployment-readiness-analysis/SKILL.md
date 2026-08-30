---
name: deployment-readiness-analysis
description: Before any provisioning or deployment, confirm the build is QA-certified, the certified artifact is identifiable, and TDD.md carries an approved stack/platform for the chosen target; then select the deployment target. Use as the DevOps entry gate.
---

# Deployment Readiness Analysis

## Purpose

Establish that it is safe and authorised to deploy, and against what. This is the DevOps entry gate.

## Confirm

- **QA certification.** A QA PASS exists for the capability/build to be deployed; identify the exact
  certified build/commit. If no certification exists → `BLOCKED — NOT QA-CERTIFIED`.
- **Approved stacks.** `TDD.md` (Deployment & Infrastructure Stack section) defines an **approved** stack,
  platform, and IaC approach for the intended target. If the target's stack is missing/unapproved →
  `BLOCKED — STACK NOT APPROVED` (route to Solution Architect).
- **Build integrity.** The artifact to deploy is exactly what QA certified (not modified since).
- **Access & prerequisites.** Required tooling, credentials (via secret store), and platform access are
  available, or record the gap.

## Select target

Confirm the **deployment target** — Local or Production — via `vscode/askQuestions`. One target per
activation. Production readiness is stricter: require explicit acknowledgement before proceeding.

## Output

A concise readiness result: certified build id, target, approved stack reference, prerequisites/gaps, and
the readiness verdict (ready / blocked with reason).

## Boundaries

- Do not select or change the stack; only verify it is approved.
- Do not deploy here; this only establishes readiness.
