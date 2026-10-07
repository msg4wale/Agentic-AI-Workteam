---
name: technology-stack-discovery
description: Interview the stakeholder about local-development, testing and technology preferences; compare viable stacks; recommend BOTH a Local Dev/Test stack and a Production stack/platform (each with options and justifications) plus the Infrastructure-as-Code approach; and record separate stakeholder accept/modify/override decisions for each.
---

# Technology Stack Discovery & Recommendation

## Purpose

Select the technology deliberately, with explicit stakeholder input, producing **two separately-approved
recommendations**:

1. a **Local Dev/Test stack and platform** — how the software is built, hosted, and tested locally; and
2. a **Production stack and platform** — how it is shipped to and run in production.

Both must satisfy product and architecture requirements while keeping behavioural drift between local and
production minimal. Each also names its **Infrastructure-as-Code approach**, because the DevOps Engineer
provisions both from IaC.

### Hard constraint on Local
The **Local Dev/Test platform must be open-source and IaC-deployable** (Constitution §7). Recommend only
local options that meet this; if a preferred production service has no open-source local equivalent,
recommend an open-source local substitute (or a documented emulator) and record the parity gap.

## Interview Protocol

Actively interview the stakeholder. Ask no more than **three questions at a time**. Do not infer preferences from examples unless explicitly confirmed.

## Discovery Dimensions

### Backend
- preferred language/framework
- technologies to avoid
- existing capability

### Frontend
- framework
- TypeScript preference
- styling/component approach
- frontend test preference

### Persistence
- database preference
- local database expectations
- same local/PROD engine preference

### Local Development
- OS and hardware
- Docker / Docker Compose / Dev Containers
- one-command startup expectations
- cloud-only dependency tolerance
- emulator tolerance

### Testing
- unit, integration, contract, E2E expectations
- local full-journey testing
- Testcontainers or equivalent
- mock/stub tolerance

### PROD MVP
- cloud/provider
- managed service preference
- container/serverless preference
- cost sensitivity
- operational capability
- portability/vendor lock-in

### Identity
- production identity provider
- local-development auth approach
- real OIDC/OAuth testing expectations

## Local / PROD Parity Model

Assess at minimum:

| Concern | Local | PROD MVP | Parity Risk |
|---|---|---|---|
| App runtime | | | |
| Frontend runtime | | | |
| Database engine | | | |
| Cache | | | |
| Messaging | | | |
| Object storage | | | |
| Identity | | | |
| External integrations | | | |
| Config/secrets | | | |
| Container image | | | |

Use High parity, Acceptable parity, or Material parity gap.

## Recommendation Criteria

Evaluate:
1. Requirement Fit
2. Local Developer Experience
3. Local / PROD Parity
4. Testability
5. Team / Stakeholder Familiarity
6. MVP Delivery Speed
7. Operational Complexity
8. Security
9. Scalability
10. Cost
11. Ecosystem Maturity
12. Maintainability
13. Vendor Lock-In
14. Portability

Local developer experience, testability, and local/PROD parity are first-class criteria.

## Candidate Options (present for BOTH local and production)

Where genuine alternatives exist, present **two or three viable options each** for:

- **Local Dev/Test** — open-source, IaC-deployable options, with strengths, trade-offs, local topology,
  bring-up experience, and parity to the production candidate. Include the IaC tooling (e.g. Docker
  Compose / Dev Containers).
- **Production** — stack/platform options (cloud/provider/runtime), with strengths, trade-offs, operational
  cost/complexity, and the IaC tooling (e.g. Terraform / Pulumi / Ansible / K8s + Helm).

## Architect Recommendation (two recommendations)

Make **two explicit recommendations with justifications**:

1. **Recommended Local Dev/Test stack & platform + IaC approach** — why it best balances developer
   experience, testability, open-source/IaC constraint, and production parity.
2. **Recommended Production stack & platform + IaC approach** — why it best balances requirements,
   operability, delivery speed, cost, and maintainability.

State reasons for each; make the local↔production parity relationship explicit.

## Stakeholder Decision Gate (separate approval for each)

The stakeholder reviews and decides on **each** recommendation independently — one of:
- **Accept Recommendation**
- **Modify Recommendation**
- **Override Recommendation**

Present both recommendations for review and obtain an explicit decision on the Local recommendation **and**
on the Production recommendation. The stakeholder has final authority unless a choice cannot satisfy a
mandatory requirement, or a Local choice violates the open-source + IaC constraint.

## Override Handling

If overridden:
1. record the chosen stack exactly;
2. record material concerns only;
3. verify mandatory requirements remain achievable;
4. proceed if technically feasible;
5. do not repeatedly challenge an informed override.

## Technology Decision Levels

### Level 1 — Architecture-Level
Backend language/framework, frontend framework, primary database, cloud/runtime, identity, major messaging/cache platforms.

### Level 2 — Significant Engineering Standards
Tailwind CSS, ORM, migration framework, data-fetching library, validation framework, test framework.

### Level 3 — Local Implementation Libraries
Small utility libraries may be selected downstream within project standards.

## Output Contribution to TDD.md

Populate the **Deployment & Infrastructure Stack** section (the DevOps Engineer's input contract) plus the
stack tables:
- Approved **Local Dev/Test** stack, platform, and IaC approach (+ decision: accept/modify/override)
- Approved **Production** stack, platform, and IaC approach (+ decision: accept/modify/override)
- Technology Stack table
- Stakeholder Preference Summary
- Local / PROD Parity Assessment
- Local Development & Test Topology
- Override/Modification Notes
- Material Risks

Both approved stacks and their IaC approach must be explicit here so the DevOps Engineer can provision each
without re-deciding the stack.

## Completion Check

Complete only when preferences are explicitly gathered; viable options evaluated for both local and
production; a Local Dev/Test recommendation (open-source + IaC) **and** a Production recommendation made,
each with an IaC approach and justification; local/production parity assessed; a **separate stakeholder
decision recorded for each**; and mandatory requirements remain achievable.
