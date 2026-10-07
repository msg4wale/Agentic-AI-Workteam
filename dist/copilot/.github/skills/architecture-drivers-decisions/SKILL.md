---
name: architecture-drivers-decisions
description: Extract architecture drivers from PRD requirements and constraints, identify architecture-significant quality attributes, evaluate solution options, and document consequential technical decisions and trade-offs.
---

# Architecture Drivers & Decisions

## Purpose

Establish the forces that should shape the architecture before decomposing the system.

Architecture should be requirement-driven, not technology-driven.

## Inputs

Primary:

`PRD.md`

Also use explicitly identified:

- existing architecture documentation;
- enterprise technology standards;
- hosting/platform constraints;
- security/compliance standards.

Do not assume unstated organization standards.

## Architecture Drivers

Use IDs:

`AD-001`, `AD-002`, ...

Potential drivers include:

- critical functional flows;
- performance targets;
- availability targets;
- RPO/RTO;
- scale and transaction volume;
- data sensitivity;
- privacy/compliance;
- auditability;
- integration constraints;
- offline/low-connectivity requirements;
- geography/data residency;
- device/platform constraints;
- legacy integration;
- delivery timeline;
- budget/cost constraints;
- team capability if explicitly known;
- operational support model.

For each driver capture:

- source requirement;
- importance;
- architectural consequence;
- uncertainty.

## Architecture-Significant Requirements

Not every requirement needs to shape system structure.

Identify those that materially affect:

- architecture style;
- component boundary;
- data architecture;
- communication style;
- deployment;
- security;
- reliability;
- technology selection.

## Quality Attribute Scenarios

Where important, normalize NFRs into:

```text
Source / Trigger
Environment
Stimulus
Artifact
Expected Response
Measure
```

Example:

> During normal production load, an authenticated user requests their dashboard; the application must return the initial dashboard response within the PRD target.

Do not invent target numbers.

## Technology Constraints

Separate:

- mandatory constraint;
- preferred technology;
- existing platform;
- architect-selected option.

A preference is not automatically mandatory.

## Architecture Options

For consequential decisions evaluate credible alternatives.

Use criteria relevant to the actual drivers:

- fit;
- complexity;
- cost;
- maturity;
- security;
- performance;
- operability;
- maintainability;
- team capability;
- vendor dependency;
- portability;
- scalability.

Avoid fake precision scoring unless weights and scores are genuinely meaningful.

## Architecture Decision Records

Use:

`ADR-xxx`

Capture:

- Context
- Drivers
- Alternatives
- Decision
- Rationale
- Trade-offs
- Consequences
- Status

Consequential decisions may include:

- monolith vs distributed architecture;
- relational vs document persistence;
- sync vs async integration;
- managed identity strategy;
- cloud/runtime platform;
- queue/message platform;
- search technology;
- caching approach;
- deployment topology.

Do not create ADRs for trivial code-level choices.

## Complexity Challenge

For every additional subsystem ask:

- Which requirement requires it?
- What failure/cost does it prevent?
- Could the same requirement be met more simply?
- Does the team now need to operate another distributed dependency?

## Technical Risks

Use:

`TRISK-xxx`

Capture architecture risks such as:

- unproven external dependency;
- unclear throughput;
- vendor quota;
- legacy integration uncertainty;
- data migration complexity;
- unsupported platform constraint;
- availability mismatch.

Do not convert risk into fact.

## Output Contribution to TDD.md

Populate/refine:

- Scope and Design Context
- Architecture Drivers
- Architecture Decisions
- Technology Stack
- Technical Risks
- Technical Assumptions

## Completion Check

Pass when:

1. Critical drivers are traceable to the PRD.
2. Major technical choices are justified.
3. Alternatives were considered where consequential.
4. Complexity is proportionate.
5. Unknowns are visible.
