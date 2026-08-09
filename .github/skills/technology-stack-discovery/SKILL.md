---
name: technology-stack-discovery
description: Interview the stakeholder about local-development, testing and technology preferences; compare viable technology stacks; recommend the PROD MVP stack with local/PROD parity; and record stakeholder accept, modify, or override decisions.
---

# Technology Stack Discovery & Recommendation

## Purpose

Select a technology stack deliberately, with explicit stakeholder input and strong consideration for local development and testing.

The stack must satisfy product and architecture requirements while remaining practical to develop and test locally, with minimal behavioural drift between local and PROD.

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

## Candidate Stacks

Where genuine alternatives exist, present two or three viable options with strengths, trade-offs, local-dev topology, PROD form, and parity assessment.

## Architect Recommendation

Recommend one PROD MVP stack and explain why it best balances requirements, local testability, operational simplicity, delivery speed, and maintainability.

## Stakeholder Decision Gate

The stakeholder must choose one:
- **Accept Recommendation**
- **Modify Recommendation**
- **Override Recommendation**

The stakeholder has final authority unless the selected stack cannot satisfy a mandatory requirement.

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

Populate:
- Technology Stack table
- Stakeholder Preference Summary
- Architect Recommendation
- Stakeholder Decision
- Override/Modification Notes
- Local / PROD Parity Assessment
- Local Development & Test Topology
- Material Risks

## Completion Check

Complete only when preferences are explicitly gathered, viable options evaluated, PROD MVP recommendation made, local/PROD parity assessed, stakeholder decision recorded, and mandatory requirements remain achievable.
