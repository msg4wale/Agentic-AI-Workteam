---
name: infrastructure-as-code-authoring
description: Author or update reproducible Infrastructure as Code for the approved local or production stack — Docker Compose, Terraform, Pulumi, Ansible, Kubernetes/Helm, or the project's chosen tools — so environments are declarative, versioned, and repeatable. Use when provisioning or modifying infrastructure.
---

# Infrastructure as Code Authoring

## Purpose

Express the target environment and infrastructure as **declarative, versioned code** so it is
reproducible, reviewable, and idempotent — never hand-built.

## Principles

- Use the **approved IaC approach and tooling** from `TDD.md`. Common choices: Docker Compose / Dev
  Containers for local; Terraform / Pulumi / Ansible / Kubernetes + Helm for production. Do not introduce a
  different tool than the one approved without routing back.
- **Local platforms must be open-source and IaC-deployable** (Constitution §7).
- Keep configuration declarative and parameterised per environment; no environment-specific values baked
  into images or code.
- **Secrets never in IaC or the repo in plaintext** (Constitution §6): reference a secret manager or
  injected environment; commit only non-secret config and secret *references*.
- Aim for **local/production parity** as designed in `TDD.md`; document any deliberate divergence.
- IaC is the single source of truth for infrastructure — no undocumented manual changes.

## Method

1. Locate the approved stack, platform, and topology in `TDD.md`.
2. Author/update IaC for each component (app runtime, datastore, cache, messaging, storage, identity,
   networking, config/secrets wiring) at the level the target needs.
3. Parameterise per environment (local vs production) via variables/workspaces/overlays.
4. Keep changes **idempotent**: re-applying without changes must be a no-op.
5. Store IaC in the target repo's conventional location (e.g. `infra/`, `deploy/`) and version it.

## Output

Reproducible IaC for the target, plus a short note of what it provisions and how to apply/destroy it
(feeds the Deployment Plan/Report).

## Boundaries

- Author code here; execution/verification belongs to `environment-provisioning` and
  `deploy-execution-verification`.
- Do not embed secrets; reference them securely.
