# Solution Architect Agent Package

This package defines the Solution Architect stage in the agentic software-development workflow.

## Dependencies

It assumes the Product Manager stage produces:

`PRD.md`

If the Product Manager package is installed, the Solution Architect reuses:

```text
.github/skills/prd-validation/SKILL.md
```

as the architecture-readiness gate.

## Structure

```text
.github/
├── agents/
│   └── solution-architect.agent.md
└── skills/
    ├── architecture-drivers-decisions/
    │   └── SKILL.md
    ├── technology-stack-discovery/
    │   └── SKILL.md
    ├── system-component-design/
    │   └── SKILL.md
    ├── data-interface-integration-design/
    │   └── SKILL.md
    ├── security-reliability-operations/
    │   └── SKILL.md
    ├── deployment-observability-delivery/
    │   └── SKILL.md
    └── tdd-validation/
        └── SKILL.md
```

## Workflow

```text
PRD.md
   |
   v
PRD Validation (shared PM skill)
   |
   +-- Not Architecture Ready --> Product Manager
   |
   v
Architecture Drivers & Decisions
   |
   v
System & Component Architecture
   |
   v
Data, API & Integration Design
   |
   v
Security, Reliability & Operations
   |
   v
Deployment, Observability & Delivery
   |
   v
TDD Validation
   |
   v
TDD.md
   |
   v
Engineering Lead
```

## Boundary

The Solution Architect may make technical design choices and select technologies where the PRD leaves those decisions open.

It must not:

- change product behaviour;
- invent product requirements;
- create engineering tasks;
- create sprint plans;
- write implementation code.

The TDD should be sufficiently detailed for the Engineering Lead to decompose the solution into Backend, Frontend, QA, Platform/DevOps and other technical tasks.


## Technology Stack Decision
The Architect interviews the stakeholder on local-development/testing preferences, recommends the PROD MVP stack, assesses local/PROD parity, and records Accept / Modify / Override.
