# Engineering Lead Agent Package

This package defines the Engineering Lead stage of the agentic software-development workflow.

## Inputs

- `PRD.md`
- `TDD.md`

## Output

- `Engineering-Plan.md`

## Structure

```text
.github/
├── agents/
│   └── engineering-lead.agent.md
└── skills/
    ├── engineering-readiness-analysis/
    │   └── SKILL.md
    ├── technical-task-decomposition/
    │   └── SKILL.md
    ├── qa-verification-planning/
    │   └── SKILL.md
    ├── dependency-sequencing-analysis/
    │   └── SKILL.md
    ├── parallel-execution-orchestration/
    │   └── SKILL.md
    ├── engineering-issue-specification/
    │   └── SKILL.md
    └── engineering-plan-validation/
        └── SKILL.md
```

## Workflow

```text
PRD.md + TDD.md
       |
       v
Engineering Readiness
       |
       +-- Product gap ------> Product Manager
       |
       +-- Architecture gap -> Solution Architect
       |
       v
Technical Task Decomposition
       |
       v
QA & Verification Planning
       |
       v
Dependency & Sequencing Analysis
       |
       v
Issue-Ready Task Specification
       |
       v
Engineering Plan Validation
       |
       v
Engineering-Plan.md
       |
       +--> Software Engineering
       +--> QA
       +--> Platform / DevOps
```

## Task Prefixes

Use only those required by the solution:

- BE — Backend
- FE — Frontend
- DB — Database
- DATA — Data/migration
- INT — Integration
- PLAT — Platform/DevOps
- SEC — Security
- OBS — Observability
- QA — Verification
- DOC — Technical/operational documentation

## Important Boundary

The Engineering Lead decomposes approved product and architecture into implementation work.

It must not:

- change product requirements;
- redesign architecture;
- write implementation code;
- fabricate estimates;
- create sprint commitments.

Every task is designed to be directly reusable as a GitHub Issue or equivalent engineering work item.


## Parallel Execution Model

The Engineering Lead is the cross-task orchestration owner.

It converts the dependency DAG into execution waves and parallel groups so separate Software Engineer agents can work concurrently when:
- hard dependencies are satisfied;
- contracts are stable;
- write ownership is safe;
- integration checkpoints are explicit.

Core rule: **Parallelize independent work. Serialize dependent decisions.**
