# Agentic AI Workteam

A reusable **agentic software-development workteam** for GitHub Copilot in VS Code. A **Coordinator**
agent owns the overall task and delegates each stage of the software-development lifecycle to a
specialised worker agent — from idea discovery through product definition, architecture, engineering
planning, plan validation, implementation, code review, and QA.

The design principle is simple: **the Coordinator orchestrates, each worker owns one SDLC
responsibility, each skill encapsulates a repeatable capability, upstream decisions remain
authoritative downstream, and independent work runs in parallel while dependent decisions stay
serial.**

## What's new in this redesign

- **Coordinator agent** — a single accountable orchestrator that dispatches every worker as an
  **isolated subagent** (`runSubagent`), keeping the main thread lean and each stage's context clean.
- **Tailored tools per role** — each agent carries only the tools its job needs. Reviewer and QA are
  **read-only on production code**; the Software Engineer and Plan Architect hold edit capability.
- **`#vscode/askQuestions` everywhere** — all agents use the interactive questions carousel for
  clarifying decisions instead of guessing.
- **Plan Architect** — a new hard gate that validates the Engineering Plan against the actual codebase,
  surfaces reusable patterns/utilities/libraries, and flags steps that duplicate existing functionality.
- **Parallel, unbiased Review and QA** — the Code Reviewer and QA Engineer run each perspective as an
  independent parallel subagent, then consolidate, so findings are unbiased.

## Workteam Overview

| # | Agent | Role | Primary Input | Primary Output |
|---|---|---|---|---|
| 0 | Coordinator | Orchestrates the whole task, delegates to workers | Requester goal | Coordinated delivery |
| 1 | Idea Discovery | Discovery | Problem owner / idea | `idea.md` |
| 2 | Product Manager | Product definition | `idea.md` | `PRD.md` |
| 3 | Solution Architect | Architecture | `PRD.md` | `TDD.md` |
| 4 | Engineering Lead | Engineering planning | `PRD.md` + `TDD.md` | `Engineering-Plan.md` |
| 5 | Plan Architect | Plan-vs-codebase validation & reuse gate | `Engineering-Plan.md` + repo | `Plan-Validation-Report.md` |
| 6 | Software Engineer | Implementation | One approved task | Repository change + PR-ready handoff |
| 7 | Code Reviewer | Independent review (parallel perspectives) | Task + diff/change set | Approve / changes required / blocked |
| 8 | QA Engineer | Independent QA (parallel perspectives) | Implemented capability | `QA-Report.md` + QA evidence |

## Per-Role Tool Tailoring

Each agent is granted only the tools its responsibility requires.

| Agent | read | search | edit | terminal | askQuestions | runSubagent |
|---|:--:|:--:|:--:|:--:|:--:|:--:|
| Coordinator | ✓ | ✓ | | | ✓ | ✓ |
| Idea Discovery | ✓ | ✓ | ✓ | | ✓ | |
| Product Manager | ✓ | ✓ | ✓ | | ✓ | |
| Solution Architect | ✓ | ✓ | ✓ | | ✓ | |
| Engineering Lead | ✓ | ✓ | ✓ | | ✓ | |
| Plan Architect | ✓ | ✓ | ✓* | ✓ | ✓ | ✓ |
| Software Engineer | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |
| Code Reviewer | ✓ | ✓ | ✓† | ✓ | ✓ | ✓ |
| QA Engineer | ✓ | ✓ | ✓‡ | ✓ | ✓ | ✓ |

\* Plan Architect `edit` is scoped to `Plan-Validation-Report.md` only.
† Code Reviewer `edit` is scoped to its own review report artifact only — **never production code**.
‡ QA Engineer `edit` is scoped to QA artifacts only (`QA-Report.md`, tests, fixtures, mocks, test data)
— **never production code**.

## End-to-End Development Workflow

```text
Requester
    |
    v
Coordinator  (clarifies goal via #vscode/askQuestions; dispatches each worker as an isolated subagent)
    |
    v
1. Idea Discovery ........ idea.md
    v
2. Product Manager ....... PRD.md
    v
3. Solution Architect .... TDD.md
    v
4. Engineering Lead ...... Engineering-Plan.md
    v
5. Plan Architect ........ Plan-Validation-Report.md      [HARD GATE]
    |                          |
    |                          +-- REVISE --> back to Engineering Lead (reuse / duplication findings)
    |                          |
    |                          +-- APPROVE
    v
    +----------------- parallel task execution (plan marks parallel-safe) -----------------+
    |                                                                                     |
    v                                                                                     v
6. Software Engineer                                                          6. Software Engineer
   (one approved task per subagent)                                              (another safe task)
    |                                                                                     |
    +---------------------------------------+---------------------------------------------+
                                            |
                                            v
                                     Integrated Change
                                            |
                                            v
7. Code Reviewer  (5 perspectives run as parallel, blind subagents -> consolidate -> verdict)
                                            |
                          +-----------------+-----------------+
                          |                                   |
                   CHANGES REQUIRED                        APPROVE
                          |                                   |
                          v                                   v
                  Software Engineer               8. QA Engineer  (4 perspectives run as
                          ^                            parallel, blind subagents -> consolidate)
                          |                                   |
                          |                        +----------+----------+
                          |                        |                     |
                          +--- QA FAIL          QA FAIL               QA PASS
                                                                        |
                                                                        v
                                                            Release / Merge Gate
```

The **Coordinator** owns cross-stage orchestration and gate enforcement. The **Engineering Lead** owns
cross-task parallelism. The **Software Engineer** owns controlled intra-task subagent parallelism. The
governing rule is:

> **Parallelize independent work. Serialize dependent decisions.**

---

# Agents and Skills

## 0. Coordinator Agent

**Purpose:** Own the overall task and orchestrate the workteam. Interview the requester, dispatch each
stage to the right worker as an isolated subagent, enforce lifecycle gates, and route rework loops until
the task is releasable.

**Agent:** `.github/agents/coordinator.agent.md`

The Coordinator does not produce any stage deliverable itself. It dispatches every worker via
`runSubagent` (isolated context, concise result returned), enforces the Plan Architect gate before
implementation, and routes Review `CHANGES REQUIRED` and QA `FAIL` loops back to the Software Engineer.

---

## 1. Idea Discovery Agent

**Purpose:** Interview, groom, challenge, and clarify the problem owner until the product idea is
sufficiently defined for Product Management without hidden assumptions.

**Input:** Problem owner / innovator → **Output:** `idea.md`

**Agent:** `.github/agents/idea-discovery.agent.md`

### Skills

| Skill | Responsibility |
|---|---|
| `problem-outcome-discovery` | Clarifies the problem, desired outcome, evidence, value, and success definition. |
| `stakeholder-user-discovery` | Identifies users, stakeholders, actors, needs, permissions, and affected parties. |
| `journey-requirements-discovery` | Discovers journeys, functional requirements, business rules, states, and interactions. |
| `quality-edge-case-discovery` | Discovers quality expectations, exceptions, negative paths, edge cases, and failure behaviour. |
| `scope-risk-discovery` | Establishes MVP scope, exclusions, constraints, assumptions, dependencies, and risks. |
| `idea-validation` | Validates whether the discovered idea is sufficiently complete for Product Management. |

---

## 2. Product Manager Agent

**Purpose:** Convert validated product discovery into a structured, traceable, architecture-ready PRD.

**Input:** `idea.md` → **Output:** `PRD.md`

**Agent:** `.github/agents/product-manager.agent.md`

### Skills

| Skill | Responsibility |
|---|---|
| `product-framing-synthesis` | Converts discovery into product framing, goals, personas, journeys, scope, outcomes. |
| `epic-user-story-design` | Organizes product capabilities into epics and implementable user stories. |
| `requirements-acceptance-criteria` | Produces precise requirements and testable acceptance criteria. |
| `prioritization-release-planning` | Prioritizes MVP, future scope, sequencing, and release intent. |
| `product-quality-metrics` | Defines product success metrics and quality expectations. |
| `prd-validation` | Validates that the PRD is complete and internally consistent for architecture. |

---

## 3. Solution Architect Agent

**Purpose:** Translate approved requirements into an engineering-plannable technical design and make
architecture decisions explicitly. Interviews the stakeholder on technology-stack preferences via
`#vscode/askQuestions` (accept / modify / override the recommended PROD MVP stack).

**Input:** `PRD.md` → **Output:** `TDD.md`

**Agent:** `.github/agents/solution-architect.agent.md`

### Skills

| Skill | Responsibility |
|---|---|
| `architecture-drivers-decisions` | Identifies architecture-significant requirements, quality attributes, trade-offs, ADRs. |
| `technology-stack-discovery` | Interviews on preferences, evaluates stacks, recommends the PROD MVP stack, records the decision. |
| `system-component-design` | Defines context, style, component responsibilities, boundaries, runtime interactions. |
| `data-interface-integration-design` | Defines data ownership, persistence, APIs, integrations, contracts, events, migration. |
| `security-reliability-operations` | Defines authn/authz, trust boundaries, secrets, audit, resilience, recovery. |
| `deployment-observability-delivery` | Defines environments, CI/CD, rollout/rollback, logs, metrics, traces, health, alerts. |
| `tdd-validation` | Validates fidelity, completeness, traceability, operability, security, planning readiness. |

---

## 4. Engineering Lead Agent

**Purpose:** Convert approved product and architecture into complete, dependency-aware, issue-ready
implementation work, and revise it against Plan Architect reuse findings.

**Input:** `PRD.md` + `TDD.md` → **Output:** `Engineering-Plan.md`

**Agent:** `.github/agents/engineering-lead.agent.md`

### Skills

| Skill | Responsibility |
|---|---|
| `engineering-readiness-analysis` | Validates PRD/TDD consistency and implementation-planning readiness. |
| `technical-task-decomposition` | Converts stories and architecture into cohesive tasks across all disciplines. |
| `qa-verification-planning` | Creates explicit QA and verification tasks from acceptance criteria, edge cases, NFRs. |
| `dependency-sequencing-analysis` | Builds the task dependency DAG, sequencing, parallelization, integration checkpoints. |
| `parallel-execution-orchestration` | Converts dependency-safe work into execution waves and parallel groups. |
| `engineering-issue-specification` | Makes each task self-contained and suitable as a GitHub Issue. |
| `engineering-plan-validation` | Validates coverage, traceability, dependencies, QA coverage, issue readiness. |

The Engineering Lead is the primary **cross-task orchestration owner**, but its plan must pass the
**Plan Architect** gate before any implementation begins.

---

## 5. Plan Architect Agent

**Purpose:** Validate `Engineering-Plan.md` against the actual codebase before implementation.
Identify existing patterns, utilities, and libraries that should be reused; flag any plan step that
duplicates existing functionality; return an **APPROVE** or **REVISE** verdict that gates the Software
Engineer.

**Input:** `Engineering-Plan.md` + `PRD.md` + `TDD.md` + repository → **Output:** `Plan-Validation-Report.md`

**Agent:** `.github/agents/plan-architect.agent.md`

### Skills

| Skill | Responsibility |
|---|---|
| `engineering-readiness-analysis` *(reused)* | Confirms the plan is coherent enough to validate against code. |
| `repository-context-analysis` *(reused)* | Inspects the relevant repository surface for existing implementation context. |
| `codebase-reuse-analysis` | Locates existing patterns/utilities/libraries relevant to each task (parallel read-only scans). |
| `plan-duplication-detection` | Classifies each step reuse / extend / build-new and flags duplication. |
| `plan-validation-reporting` | Assembles the report, sets the verdict, routes loop-back items to the Engineering Lead. |

On **REVISE**, the report's loop-back items return to the Engineering Lead; implementation does not
start until **APPROVE**.

---

## 6. Software Engineer Agent

**Purpose:** Implement one Plan-Architect-approved task at a time, honouring the reuse targets from the
validation report, using controlled subagents for isolated analysis and (conditionally) parallel
implementation.

**Input:** One approved task + relevant `PRD.md`/`TDD.md` + `Plan-Validation-Report.md` reuse notes +
repository → **Output:** Repository changes + tests + PR-ready handoff

**Agent:** `.github/agents/software-engineer.agent.md`

### Skills

| Skill | Responsibility |
|---|---|
| `task-readiness-analysis` | Confirms the task is implementable without inventing requirements or architecture. |
| `repository-context-analysis` | Locates existing modules, patterns, schemas, contracts, tests, commands. |
| `subagent-parallel-execution` | Uses `runSubagent` for isolated analysis, verification, and selective parallel implementation. |
| `focused-implementation` | Implements the smallest complete change that satisfies the task and architecture. |
| `testing-verification` | Adds/updates tests and runs targeted, integration, static, and build verification. |
| `code-quality-security-review` | Pre-handoff correctness, maintainability, security, data-integrity self-review. |
| `implementation-handoff-validation` | Verifies acceptance coverage, test evidence, and readiness for independent review. |

---

## 7. Code Reviewer Agent

**Purpose:** Independently review an implementation **from multiple perspectives simultaneously**.
Each perspective runs as an isolated, blind parallel subagent (`runSubagent`) so findings are
unbiased, then a consolidation skill merges them into one verdict. **Read-only on production code** —
`edit` is scoped to the review report only.

**Input:** Engineering task + change set/diff + relevant PRD/TDD + implementation evidence →
**Output:** `APPROVE`, `APPROVE WITH NON-BLOCKING COMMENTS`, `CHANGES REQUIRED`, or a blocked verdict

**Agent:** `.github/agents/code-reviewer.agent.md`

### Skills

| Skill | Role | Responsibility |
|---|---|---|
| `review-readiness-context` | pre-step | Shared context pack: scope, intent, changed files, acceptance criteria, evidence. |
| `change-correctness-analysis` | **perspective** | Behaviour, boundaries, state, errors, concurrency, side effects, scope. |
| `requirement-architecture-compliance` | **perspective** | Fidelity to plan, PRD, TDD, contracts, scope boundaries. |
| `code-design-quality-review` | **perspective** | Cohesion, coupling, modularity, testability, complexity, duplication. |
| `security-data-integrity-review` | **perspective** | Authz, trust boundaries, injection, secrets, transactions, corruption risk. |
| `test-verification-review` | **perspective** | Test quality, acceptance coverage, negative cases, regressions, evidence. |
| `review-decision-validation` | consolidation | Merges independent findings, normalizes severity, sets the single verdict. |

The five perspectives are dispatched in parallel and are blind to one another; consolidation happens
only after all return. `CHANGES REQUIRED` routes back to the Software Engineer.

---

## 8. QA Engineer Agent

**Purpose:** Independently validate the implemented capability **from multiple perspectives
simultaneously**. Each perspective runs as an isolated, blind parallel subagent (`runSubagent`), then a
consolidation skill merges the results into one QA verdict. **Read-only on production code** — `edit`
is scoped to QA artifacts (report, tests, fixtures, mocks, test data).

**Input:** Implemented capability/task + `PRD.md` + `Engineering-Plan.md` + relevant `TDD.md` →
**Output:** `QA-Report.md`, QA automation/evidence, and QA verdict

**Agent:** `.github/agents/qa-engineer.agent.md`

### Skills

| Skill | Role | Responsibility |
|---|---|---|
| `qa-readiness-context` | pre-step | QA scope, expected behaviour, build/environment, data, dependencies, blockers. |
| `risk-based-test-design` | pre-step | Prioritized scenarios by business impact, probability, complexity, sensitivity, risk. |
| `functional-acceptance-validation` | **perspective** | Journeys, acceptance criteria, business rules, roles, states, edge cases. |
| `integration-data-failure-validation` | **perspective** | APIs, integrations, persistence, transactions, idempotency, dependency failure. |
| `nonfunctional-quality-validation` | **perspective** | Performance, security behaviour, accessibility, compatibility, reliability, recovery. |
| `regression-evidence-validation` | **perspective** | Regression scope, suite runs, automation reliability, evidence completeness. |
| `qa-decision-defect-reporting` | consolidation | Merges results, de-duplicates defects, sets the single QA verdict. |

The four perspectives are dispatched in parallel and are blind to one another; consolidation happens
only after all return. `FAIL` routes back to the Software Engineer (re-review if code changes).

---

# Traceability Model

The workteam preserves traceability across the lifecycle:

```text
Idea Discovery       FEAT / BR / FR / NFR / EC / CON / RISK / ASM
      v
Product Management   EPIC / US / AC / MET + preserved discovery IDs
      v
Solution Architecture ADR / COMP / DATA / API / INT / EVT / SEC / REL / OBS / DEP
      v
Engineering Planning BE / FE / DB / DATA / INT / PLAT / SEC / OBS / QA / DOC
      v
Plan Validation      reuse-existing / extend-existing / build-new + duplication flags
      v
Implementation       ENG-AC + code + tests + verification evidence
      v
Code Review          P0 / P1 / P2 / P3 findings (5 parallel perspectives)
      v
QA                   TC-* / DEF-* + PASS / FAIL / BLOCKED (4 parallel perspectives)
```

---

# Repository Layout

```text
Agentic-AI-Workteam/
├── .github/
│   ├── agents/
│   │   ├── coordinator.agent.md
│   │   ├── idea-discovery.agent.md
│   │   ├── product-manager.agent.md
│   │   ├── solution-architect.agent.md
│   │   ├── engineering-lead.agent.md
│   │   ├── plan-architect.agent.md
│   │   ├── software-engineer.agent.md
│   │   ├── code-reviewer.agent.md
│   │   └── qa-engineer.agent.md
│   └── skills/
│       └── <reusable skill folders>/SKILL.md
├── MANIFEST.md
└── README.md
```

`.github/` is the **single source of truth** and the installable workteam. Custom agents live under
`.github/agents/`; reusable Agent Skills live under `.github/skills/<skill-name>/SKILL.md`.

---

# Installation

Clone this repository next to your target project, then copy the `.github` content into the target
repository.

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

Open the target project in a current version of **VS Code with GitHub Copilot agent capabilities
enabled**. Invoke the **Coordinator** to run the whole lifecycle, or invoke any individual worker agent
directly for a single stage.

---

# Recommended Operating Sequence

1. Invoke the **Coordinator** with your goal; it clarifies scope and entry point via
   `#vscode/askQuestions`.
2. The Coordinator dispatches **Idea Discovery**, then **Product Manager**, then **Solution Architect**,
   then **Engineering Lead** — each as an isolated subagent, each gated on the prior deliverable.
3. **Plan Architect** validates the engineering plan against the codebase. On **REVISE**, the plan
   returns to the Engineering Lead; only **APPROVE** releases implementation.
4. The Coordinator dispatches one approved task per **Software Engineer** subagent, running
   parallel-safe tasks concurrently.
5. **Code Reviewer** runs its five perspectives in parallel and returns a verdict; `CHANGES REQUIRED`
   loops back to Software Engineering.
6. **QA Engineer** runs its four perspectives in parallel and returns a verdict; `FAIL` loops back to
   Software Engineering (re-review if code changes).
7. Release/merge only when review and QA gates pass.

---

# Design Principles

- **Coordinator orchestrates; workers execute.** One accountable role per stage; the Coordinator never
  authors a worker's deliverable.
- **Context isolation via subagents.** Every worker and every review/QA perspective runs in an isolated
  `runSubagent` context and returns concise results, keeping the main thread lean.
- **Least-privilege tooling.** Each agent holds only the tools its job needs; Reviewer and QA never edit
  production code.
- **Reuse before rebuild.** The Plan Architect gate enforces reuse of existing patterns, utilities, and
  libraries and blocks duplicated work.
- **Independent, unbiased evaluation.** Review and QA perspectives run in parallel, blind to one
  another, before consolidation.
- **No silent assumptions.** Ambiguity is routed via `#vscode/askQuestions` or upstream, never guessed.
- **Source-of-truth hierarchy.** Downstream agents do not rewrite upstream intent.
- **Parallelize independent work; serialize dependent decisions.**
- **Evidence over claims.** Tests, review findings, and QA verdicts trace to actual evidence.

---

# Version Notes

This repository contains the Coordinator-orchestrated redesign:

- Coordinator agent with isolated subagent delegation and gate enforcement
- Idea Discovery, Product Manager, Solution Architect, Engineering Lead (as before, now
  `#vscode/askQuestions`-enabled and Coordinator-dispatchable)
- Plan Architect with codebase reuse analysis and duplication detection
- Software Engineer with controlled `runSubagent` parallel execution and reuse-target adherence
- Code Reviewer with five parallel, blind review perspectives (read-only on production code)
- QA Engineer with four parallel, blind validation perspectives (read-only on production code)
