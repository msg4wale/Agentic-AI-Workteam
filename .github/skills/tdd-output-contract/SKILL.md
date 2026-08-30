---
name: tdd-output-contract
description: The output contract and section template for TDD.md — the structure the Solution Architect fills in, including the Deployment & Infrastructure Stack section that is the DevOps Engineer's input contract. Load when assembling or validating TDD.md.
---

# `TDD.md` Output Contract

Use this structure. Remove irrelevant placeholders; for sections that genuinely do not apply, write
`Not Applicable` with a brief technical reason; do not add speculative subsystems to fill the template.

```markdown
# Technical Design Document

## Document Control
- Product:
- Version:
- Status:
- Last Updated:
- Solution Architect:
- TDD Readiness:
- Source PRD: PRD.md

## Executive Technical Summary

## 1. Scope and Design Context
### 1.1 Product Capabilities in Scope
### 1.2 Technical Scope
### 1.3 Technical Non-Goals
### 1.4 Existing-System Context
### 1.5 Constraints
### 1.6 Technical Assumptions

## 2. Architecture Drivers
| ID | Driver | Source Requirement | Design Impact | Priority |
|---|---|---|---|---|

## 3. Architecture Decisions
### ADR-001 — [Decision]
- Status:
- Context:
- Drivers / Requirements:
- Decision:
- Alternatives Considered:
- Rationale:
- Trade-offs:
- Consequences:

## 4. System Context
### 4.1 Context Diagram
### 4.2 Actors and External Systems
### 4.3 System / Trust Boundaries

## 5. Architecture Overview
### 5.1 Architecture Style
### 5.2 High-Level Architecture Diagram
### 5.3 Technology Stack
| Layer / Concern | Selected Technology | Local Development / Test Form | PROD MVP Form | Decision Source | Rationale |
|---|---|---|---|---|---|
### 5.4 Technology Stack Decision Summary
- Stakeholder Preference Summary:
- Architect Recommendation:
- Stakeholder Decision: Accepted / Modified / Overridden
- Material Override Concerns:
- Local / PROD Parity Assessment:
### 5.5 Major Interaction Patterns

## 6. Component Design
### COMP-001 — [Component Name]
- Purpose:
- Responsibilities:
- Owned Data:
- Interfaces:
- Dependencies:
- Scaling / Availability:
- Security Considerations:
- Related Requirements:

## 7. Key Runtime Flows
### 7.1 [Flow Name]
- Trigger:
- Components:
- Main Flow:
- Failure / Alternate Flow:
- Related Requirements:

## 8. Data Architecture
### 8.1 Data Ownership
### 8.2 Logical Data Model
### 8.3 Entity / Relationship Design
### 8.4 Persistence Strategy
### 8.5 Transaction Boundaries
### 8.6 Consistency Model
### 8.7 Data Lifecycle / Retention
### 8.8 Sensitive Data / Classification
### 8.9 Migration / Import / Export

## 9. API and Interface Design
### API-001 — [Interface Name]
- Purpose:
- Provider:
- Consumer:
- Interaction:
- Operation / Endpoint:
- Authentication / Authorization:
- Request:
- Response:
- Validation:
- Errors:
- Idempotency:
- Versioning:
- Related Requirements:

## 10. Integration Architecture
### INT-001 — [Integration Name]
- External System:
- Business Purpose:
- Interaction Pattern:
- Data Exchanged:
- Authentication / Trust:
- Timeout / Failure Behaviour:
- Retry / Idempotency:
- Availability Dependency:
- Related Requirements:

## 11. Event / Messaging Design
Use only if applicable.
### EVT-001 — [Event Name]
- Producer:
- Consumer(s):
- Trigger:
- Contract:
- Delivery Semantics:
- Ordering:
- Idempotency:
- Failure Handling:
- Retention:
- Related Requirements:

## 12. Security Architecture
### 12.1 Identity and Authentication
### 12.2 Authorization
### 12.3 Trust Boundaries
### 12.4 Data Protection
### 12.5 Secrets and Key Management
### 12.6 Audit Logging
### 12.7 Threat / Abuse Controls
### 12.8 Security Verification Requirements

## 13. Reliability and Resilience
### 13.1 Availability Design
### 13.2 Dependency Failure Handling
### 13.3 Timeout / Retry / Idempotency
### 13.4 Graceful Degradation
### 13.5 Backup and Restore
### 13.6 Disaster Recovery
### 13.7 Capacity / Overload Protection

## 14. Performance and Scalability
### 14.1 Workload Assumptions
### 14.2 Critical Performance Paths
### 14.3 Scaling Strategy
### 14.4 Caching Strategy
### 14.5 Performance Verification

## 15. Deployment Architecture
### 15.1 Runtime Topology
### 15.2 Environments
### 15.3 Network Architecture
### 15.4 Configuration Management
### 15.5 Infrastructure Dependencies
### 15.6 Scaling and Availability Placement

## 15A. Deployment & Infrastructure Stack (DevOps input contract)
<!-- The approved stacks the DevOps Engineer provisions from. Both must be explicit and approved. -->
### 15A.1 Local Dev/Test Stack & Platform
- Approved stack (open-source, IaC-deployable):
- Local platform / topology:
- IaC approach & tooling (e.g. Docker Compose / Dev Containers):
- Stakeholder Decision: Accepted / Modified / Overridden
### 15A.2 Production Stack & Platform
- Approved stack:
- Production platform (cloud/provider/runtime):
- IaC approach & tooling (e.g. Terraform / Pulumi / Ansible / K8s + Helm):
- Stakeholder Decision: Accepted / Modified / Overridden
### 15A.3 Local ↔ Production Parity & Divergence

## 16. Delivery and Release Architecture
### 16.1 Build / CI Expectations
### 16.2 Deployment / CD Expectations
### 16.3 Database / Schema Change Strategy
### 16.4 Feature Rollout
### 16.5 Rollback Strategy
### 16.6 Environment Promotion

## 17. Observability and Operations
### 17.1 Logging
### 17.2 Metrics
### 17.3 Tracing
### 17.4 Health / Readiness
### 17.5 Alerting
### 17.6 Dashboards
### 17.7 Operational Runbook Requirements

## 18. Compliance, Privacy and Data Governance

## 19. Technical Verification Strategy
### 19.1 Unit-Level Concerns
### 19.2 Component / Integration Verification
### 19.3 Contract Verification
### 19.4 Performance Verification
### 19.5 Security Verification
### 19.6 Resilience / Recovery Verification

This section defines architecture-significant verification concerns, not detailed QA test cases.

## 20. Technical Risks
| ID | Risk | Impact | Likelihood | Mitigation / Design Response | Owner |
|---|---|---|---|---|---|

## 21. Open Technical Questions
| Question / Decision | Why It Matters | Owner | Engineering-Planning Blocking? | Required By |
|---|---|---|---|---|

## 22. Requirement-to-Architecture Traceability
| PRD Requirement | Architecture Driver | ADR | Component / Interface | Verification Concern |
|---|---|---|---|---|

## 23. Glossary
```

The **Deployment & Infrastructure Stack (15A)** section is mandatory once technology is chosen: it records
the approved Local and Production stacks, platforms, and IaC approaches, each with its stakeholder
decision — this is the DevOps Engineer's authoritative input.
