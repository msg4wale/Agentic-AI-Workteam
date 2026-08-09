# Agentic AI Workteam

A reusable **agentic software-development workteam** for GitHub Copilot in VS Code. The repository defines specialized AI agents and Agent Skills that work together across the software-development lifecycle, from idea discovery through product definition, architecture, engineering planning, implementation, code review, and QA validation.

The design principle is simple: **each agent owns a clear SDLC responsibility, each skill encapsulates a repeatable capability, and upstream decisions remain authoritative downstream.**

## Workteam Overview

| Stage | Agent | Primary Input | Primary Output |
|---|---|---|---|
| 1 | Idea Discovery | Problem owner / idea | `idea.md` |
| 2 | Product Manager | `idea.md` | `PRD.md` |
| 3 | Solution Architect | `PRD.md` | `TDD.md` |
| 4 | Engineering Lead | `PRD.md` + `TDD.md` | `Engineering-Plan.md` |
| 5 | Software Engineer | One engineering task | Repository change + PR-ready handoff |
| 6 | Code Reviewer | Task + diff/change set | Approve / changes required / blocked |
| 7 | QA Engineer | Implemented capability | `QA-Report.md` + QA evidence |

## End-to-End Development Workflow

```text
Problem Owner
    |
    v
Idea Discovery Agent
    |
    v
idea.md
    |
    v
Product Manager Agent
    |
    v
PRD.md
    |
    v
Solution Architect Agent
    |
    v
TDD.md
    |
    v
Engineering Lead Agent
    |
    v
Engineering-Plan.md
    |
    +-------------------- parallel task execution --------------------+
    |                                                               |
    v                                                               v
Software Engineer Agent                                      Software Engineer Agent
(one task per agent)                                         (another safe task)
    |                                                               |
    +---------------------------+-----------------------------------+
                                |
                                v
                         Integrated Change
                                |
                                v
                         Code Reviewer Agent
                                |
                    +-----------+-----------+
                    |                       |
             CHANGES REQUIRED             APPROVE
                    |                       |
                    v                       v
             Software Engineer        QA Engineer Agent
                    ^                       |
                    |                       v
                    +-- review loop     QA-Report.md
                                            |
                                  +---------+---------+
                                  |                   |
                               QA FAIL             QA PASS
                                  |                   |
                                  v                   v
                           Software Engineer     Release / Merge Gate
```

The Engineering Lead owns **cross-task parallelism**. The Software Engineer owns **controlled intra-task subagent parallelism**. The governing rule is:

> **Parallelize independent work. Serialize dependent decisions.**

---

# Agents and Skills

## 1. Idea Discovery Agent

**Purpose:** Interview, groom, challenge, and clarify the problem owner until the proposed product idea is sufficiently defined for Product Management without hidden assumptions.

**Input:** Problem owner / innovator

**Output:** `idea.md`

**Agent:** `.github/agents/idea-discovery.agent.md`

### Skills

| Skill | Responsibility |
|---|---|
| `problem-outcome-discovery` | Clarifies the problem, desired outcome, evidence, value, and success definition. |
| `stakeholder-user-discovery` | Identifies users, stakeholders, actors, needs, permissions, and affected parties. |
| `journey-requirements-discovery` | Discovers journeys, functional requirements, business rules, states, and interactions. |
| `quality-edge-case-discovery` | Discovers quality expectations, exceptions, negative paths, edge cases, and failure behaviour. |
| `scope-risk-discovery` | Establishes MVP scope, exclusions, constraints, assumptions, dependencies, and risks. |
| `idea-validation` | Validates whether the discovered idea is sufficiently complete and unambiguous for Product Management. |

The Idea Discovery Agent deliberately stays out of architecture, APIs, databases, frameworks, and implementation design.

---

## 2. Product Manager Agent

**Purpose:** Convert validated product discovery into a structured, traceable, architecture-ready Product Requirements Document.

**Input:** `idea.md`

**Output:** `PRD.md`

**Agent:** `.github/agents/product-manager.agent.md`

### Skills

| Skill | Responsibility |
|---|---|
| `product-framing-synthesis` | Converts discovery into product framing, goals, personas, journeys, scope, and measurable outcomes. |
| `epic-user-story-design` | Organizes product capabilities into epics and implementable user stories. |
| `requirements-acceptance-criteria` | Produces precise requirements and testable product acceptance criteria. |
| `prioritization-release-planning` | Prioritizes MVP, future scope, sequencing, and release intent without engineering task decomposition. |
| `product-quality-metrics` | Defines product success metrics and quality expectations. |
| `prd-validation` | Validates that the PRD is sufficiently complete and internally consistent for architecture. |

The Product Manager preserves business truth and must not silently invent policy, architecture, or technical implementation.

---

## 3. Solution Architect Agent

**Purpose:** Translate approved product requirements into an engineering-plannable technical design and make consequential architecture decisions explicitly.

**Input:** `PRD.md`

**Output:** `TDD.md`

**Agent:** `.github/agents/solution-architect.agent.md`

### Skills

| Skill | Responsibility |
|---|---|
| `architecture-drivers-decisions` | Identifies architecture-significant requirements, quality attributes, constraints, trade-offs, and ADRs. |
| `technology-stack-discovery` | Interviews the stakeholder on local-dev/testing preferences, evaluates candidate stacks, recommends the PROD MVP stack, and records accept/modify/override decisions. |
| `system-component-design` | Defines system context, architecture style, component responsibilities, boundaries, runtime interactions, and technology allocation. |
| `data-interface-integration-design` | Defines data ownership, persistence, consistency, APIs, integrations, contracts, events, and migration behaviour. |
| `security-reliability-operations` | Defines authentication, authorization, trust boundaries, secrets, audit, failure handling, resilience, recovery, and operational concerns. |
| `deployment-observability-delivery` | Defines environments, topology, CI/CD architecture, rollout/rollback, logs, metrics, traces, health, and alerts. |
| `tdd-validation` | Validates requirement fidelity, completeness, traceability, operability, security, and readiness for engineering planning. |

### Technology Stack Decision Model

The Solution Architect actively asks about technology preferences instead of silently selecting a stack. It considers local developer experience, local integration testing, local/PROD parity, team familiarity, delivery speed, operational complexity, security, cost, maintainability, ecosystem maturity, portability, and vendor lock-in.

The Architect recommends the PROD MVP stack, but the stakeholder has final decision authority and may:

- **Accept** the recommendation
- **Modify** the recommendation
- **Override** the recommendation

An override is blocked only when it makes a mandatory requirement technically unachievable.

---

## 4. Engineering Lead Agent

**Purpose:** Convert approved product and architecture into complete, dependency-aware, issue-ready implementation work.

**Input:** `PRD.md` + `TDD.md`

**Output:** `Engineering-Plan.md`

**Agent:** `.github/agents/engineering-lead.agent.md`

### Skills

| Skill | Responsibility |
|---|---|
| `engineering-readiness-analysis` | Validates PRD/TDD consistency and implementation-planning readiness. |
| `technical-task-decomposition` | Converts stories and architecture into cohesive Backend, Frontend, Data, Integration, Platform, Security, Observability, and other tasks. |
| `qa-verification-planning` | Creates explicit QA and technical-verification tasks from acceptance criteria, edge cases, NFRs, security, and reliability requirements. |
| `dependency-sequencing-analysis` | Builds the task dependency DAG, identifies sequencing, parallelization, critical chains, and integration checkpoints. |
| `parallel-execution-orchestration` | Converts dependency-safe work into execution waves and parallel groups for multiple Software Engineer agents while controlling write conflict and contract risk. |
| `engineering-issue-specification` | Makes each task self-contained and suitable for direct use as a GitHub Issue or equivalent work item. |
| `engineering-plan-validation` | Validates task coverage, traceability, dependencies, QA coverage, issue readiness, and implementation handoff quality. |

### Parallel Implementation

The Engineering Lead is the primary **cross-task orchestration owner**. Independent tasks may be assigned to separate Software Engineer agents concurrently when:

- hard dependencies are satisfied;
- shared contracts are stable;
- write ownership is isolated or controlled;
- integration checkpoints are explicit;
- no unresolved product or architecture decision exists.

---

## 5. Software Engineer Agent

**Purpose:** Implement one assigned engineering task at a time, using the repository and approved planning artifacts as authoritative context.

**Input:** One task from `Engineering-Plan.md`, plus relevant `PRD.md`, `TDD.md`, and repository state

**Output:** Repository changes + tests + PR-ready implementation handoff

**Agent:** `.github/agents/software-engineer.agent.md`

### Skills

| Skill | Responsibility |
|---|---|
| `task-readiness-analysis` | Confirms the assigned task is implementable without inventing requirements or architecture. |
| `repository-context-analysis` | Locates existing modules, patterns, schemas, contracts, tests, commands, and relevant implementation context. |
| `subagent-parallel-execution` | Uses controlled subagents for parallel repository analysis, contract tracing, test/risk analysis, verification, and selectively isolated parallel implementation. |
| `focused-implementation` | Implements the smallest complete change that satisfies the assigned task and approved architecture. |
| `testing-verification` | Adds/updates tests and runs targeted, integration, static, build, and broader verification as required. |
| `code-quality-security-review` | Performs the Software Engineer's pre-handoff correctness, maintainability, security, data-integrity, compatibility, and architecture self-review. |
| `implementation-handoff-validation` | Verifies acceptance coverage, test evidence, scope fidelity, security, and readiness for independent review. |

### Subagent Model

For non-trivial tasks the Software Engineer evaluates safe subagent delegation. The default pattern is:

```text
Primary Software Engineer
    |
    +-- Repository Explorer
    +-- Requirement / Contract Analyst
    +-- Test Analyst
    +-- Security / Risk Analyst
    |
    v
Consolidate findings
    |
    v
Primary implementation
    |
    +-- Targeted test verification
    +-- Static/build verification
    +-- Security/edge verification
    |
    v
PR-ready handoff
```

Parallel read/analysis is encouraged. Parallel editing is conditional and requires non-overlapping ownership, fixed contracts, deterministic integration, and explicit verification.

---

## 6. Code Reviewer Agent

**Purpose:** Independently determine whether an implementation is correct, maintainable, secure, testable, architecture-compliant, and suitable for approval.

**Input:** Engineering task + change set/diff + relevant PRD/TDD + implementation evidence

**Output:** `APPROVE`, `APPROVE WITH NON-BLOCKING COMMENTS`, `CHANGES REQUIRED`, or a blocked verdict

**Agent:** `.github/agents/code-reviewer.agent.md`

### Skills

| Skill | Responsibility |
|---|---|
| `review-readiness-context` | Establishes review scope, source intent, changed files, acceptance criteria, and verification context. |
| `change-correctness-analysis` | Reviews behaviour, boundaries, state, errors, compatibility, concurrency, side effects, and scope discipline. |
| `requirement-architecture-compliance` | Verifies implementation fidelity to Engineering Plan, PRD, TDD, contracts, security/reliability controls, and scope boundaries. |
| `code-design-quality-review` | Reviews clean code, cohesion, coupling, modularity, separation of concerns, testability, complexity, duplication, abstraction quality, dependency direction, and changeability. |
| `security-data-integrity-review` | Reviews authorization, trust boundaries, injection risks, secrets, sensitive data, transactions, migrations, concurrency, and corruption risk. |
| `test-verification-review` | Evaluates test quality, acceptance coverage, negative cases, contracts, regressions, and verification evidence. |
| `review-decision-validation` | Normalizes findings, validates severity/evidence, eliminates subjective comments, and ensures the verdict follows the actual findings. |

The reviewer deliberately does **not edit production code by default**. Findings return to the Software Engineer for correction, preserving independent review.

SOLID, DRY, dependency inversion, and design patterns are used as diagnostic tools, not mechanical rules.

---

## 7. QA Engineer Agent

**Purpose:** Independently validate the implemented capability from the product-quality perspective, including acceptance behaviour, edge cases, integrations, data integrity, NFRs, and regressions.

**Input:** Implemented capability/task + `PRD.md` + `Engineering-Plan.md` + relevant `TDD.md`

**Output:** `QA-Report.md`, QA automation/evidence, and QA verdict

**Agent:** `.github/agents/qa-engineer.agent.md`

### Skills

| Skill | Responsibility |
|---|---|
| `qa-readiness-context` | Establishes QA scope, expected behaviour, build/environment, data, accounts, dependencies, and blockers. |
| `risk-based-test-design` | Designs prioritized test scenarios using business impact, probability, integration complexity, data/security sensitivity, and change risk. |
| `functional-acceptance-validation` | Validates user journeys, acceptance criteria, business rules, roles, validation, state transitions, and edge cases. |
| `integration-data-failure-validation` | Validates APIs, integrations, data persistence, transactions, concurrency, idempotency, dependency failure, reconciliation, and migrations. |
| `nonfunctional-quality-validation` | Validates applicable performance, security behaviour, accessibility, compatibility, reliability, recovery, auditability, localization, and offline/low-connectivity requirements. |
| `regression-evidence-validation` | Determines regression scope, runs relevant suites, validates automation reliability, and checks evidence completeness. |
| `qa-decision-defect-reporting` | Produces reproducible defects and an evidence-based QA verdict. |

QA may add or update test automation, fixtures, mocks, test data, and QA configuration. It does not silently fix production code defects.

---

# Traceability Model

The workteam preserves traceability across the lifecycle:

```text
Idea Discovery
    FEAT / BR / FR / NFR / EC / CON / RISK / ASM
        |
        v
Product Management
    EPIC / US / AC / MET + preserved discovery IDs
        |
        v
Solution Architecture
    ADR / COMP / DATA / API / INT / EVT / SEC / REL / OBS / DEP
        |
        v
Engineering Planning
    BE / FE / DB / DATA / INT / PLAT / SEC / OBS / QA / DOC
        |
        v
Implementation
    ENG-AC + code + tests + verification evidence
        |
        v
Code Review
    P0 / P1 / P2 / P3 findings
        |
        v
QA
    TC-* / DEF-* + PASS / FAIL / BLOCKED evidence
```

---

# Repository Layout

```text
Agentic-AI-Workteam/
├── .github/
│   ├── agents/
│   │   ├── idea-discovery.agent.md
│   │   ├── product-manager.agent.md
│   │   ├── solution-architect.agent.md
│   │   ├── engineering-lead.agent.md
│   │   ├── software-engineer.agent.md
│   │   ├── code-reviewer.agent.md
│   │   └── qa-engineer.agent.md
│   └── skills/
│       └── <all reusable skill folders>/SKILL.md
├── packages/
│   ├── idea-discovery/
│   ├── product-manager/
│   ├── solution-architect/
│   ├── engineering-lead/
│   ├── software-engineer/
│   ├── code-reviewer/
│   └── qa-engineer/
└── README.md
```

The root `.github/` directory is the **combined installable workteam**. `packages/` preserves each standalone agent package.

---

# Installation

## Option 1: Install the Entire Workteam into a Project

Clone this repository next to your target project, then copy the combined `.github` content into the target repository.

### macOS / Linux

```bash
git clone https://github.com/msg4wale/Agentic-AI-Workteam.git
cd <YOUR-TARGET-PROJECT>
mkdir -p .github/agents .github/skills
cp -R ../Agentic-AI-Workteam/.github/agents/* .github/agents/
cp -R ../Agentic-AI-Workteam/.github/skills/* .github/skills/
```

### PowerShell

```powershell
git clone https://github.com/msg4wale/Agentic-AI-Workteam.git
Set-Location <YOUR-TARGET-PROJECT>
New-Item -ItemType Directory -Force .github\agents | Out-Null
New-Item -ItemType Directory -Force .github\skills | Out-Null
Copy-Item ..\Agentic-AI-Workteam\.github\agents\* .github\agents\ -Recurse -Force
Copy-Item ..\Agentic-AI-Workteam\.github\skills\* .github\skills\ -Recurse -Force
```

Open the target project in a current version of **VS Code with GitHub Copilot agent capabilities enabled**. The custom agents are stored under `.github/agents/`, while reusable Agent Skills are stored under `.github/skills/<skill-name>/SKILL.md`.

## Option 2: Install a Single Agent Package

For example, to install only the Solution Architect package:

```bash
mkdir -p .github/agents .github/skills
cp packages/solution-architect/.github/agents/* .github/agents/
cp -R packages/solution-architect/.github/skills/* .github/skills/
```

Repeat with another package as needed.

## Option 3: Use as a Template Workteam

1. Clone/fork this repository.
2. Copy the complete root `.github/` directory into a new software project.
3. Add your project artifacts (`idea.md`, `PRD.md`, `TDD.md`, etc.) as the workflow advances.
4. Invoke the appropriate custom agent for the current lifecycle stage.

---

# Recommended Operating Sequence

1. Start with the **Idea Discovery Agent** and the problem owner.
2. Do not proceed to Product Management until discovery validation reports PRD readiness.
3. Use the **Product Manager Agent** to create `PRD.md`.
4. Use the **Solution Architect Agent** to select architecture and technology stack, including local-dev/testing preferences and stakeholder override.
5. Use the **Engineering Lead Agent** to create `Engineering-Plan.md`, dependency waves, and parallel execution groups.
6. Assign one ready task at a time to each **Software Engineer Agent**, running independent tasks concurrently where safe.
7. Send implemented changes to the **Code Reviewer Agent**. If `CHANGES REQUIRED`, return the task to Software Engineering.
8. After approval, validate the capability with the **QA Engineer Agent**.
9. If QA fails, route the defect to Software Engineering, re-run code review where the code changes, and then retest QA.
10. Release/merge only when the project's required review and QA gates have passed.

---

# Design Principles

- **No silent assumptions:** ambiguous product or architecture decisions are routed upstream.
- **Source-of-truth hierarchy:** downstream agents do not rewrite upstream intent.
- **One clear accountable role per stage.**
- **Skills are reusable capabilities; agents are orchestrators.**
- **Parallelize independent work; serialize dependent decisions.**
- **Prefer local/PROD parity for MVP development and testing.**
- **Stakeholders may override technology recommendations after informed trade-off review.**
- **Implementation and independent review are separated.**
- **QA verifies observable product quality, not only source-code quality.**
- **Evidence over claims:** tests, review findings, and QA verdicts must be traceable to actual evidence.

---

# Version Notes

This repository currently contains the latest assembled versions from the workteam design:

- Idea Discovery Agent
- Product Manager Agent
- Solution Architect with technology-stack discovery and stakeholder override
- Engineering Lead with parallel execution orchestration
- Software Engineer with controlled subagent/parallel execution
- Code Reviewer with dedicated code-design-quality review
- QA Engineer with risk-based functional, integration, NFR, regression, and defect validation

