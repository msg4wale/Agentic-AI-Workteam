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
- **Checkpoint approvals** — the Coordinator stops after **every** stage, shows you the deliverable, and
  asks you to **Approve / Request changes / Pause** before proceeding. Nothing advances without you.
- **Durable state & decision memory** — the Coordinator maintains `.workteam/Workteam-State.md` (stage,
  gate, and task status) and `.workteam/Decisions-Log.md` (every on-the-fly clarification). After any
  disruption it **resumes exactly where it stopped** — never re-running an approved stage, overwriting
  an approved deliverable, or duplicating a completed task.
- **DevOps Engineer** — after QA certifies a build, builds/releases it and provisions the **local** or
  **production** environment via **Infrastructure as Code**, deploys behind approval checkpoints, and
  hands over access. The Solution Architect recommends and gets approval for **both** a local dev/test
  stack (open-source + IaC) and a production stack.
- **Constitution** — a shipped, tailorable `Constitution.md` states the durable quality/spec/security
  principles the whole team is held to; agents load it on demand.
- **Leaner agent prompts** — the large deliverable templates now live in on-demand `*-output-contract`
  skills, keeping each agent's always-loaded prompt focused on its rules and gates.

## How progression works

You invoke the **Coordinator once**; it dispatches every downstream agent itself — you never hand-call
the next agent. Between stages it does **not** auto-advance: it presents the finished deliverable and
prompts you via `#vscode/askQuestions`:

- **Approve** → the stage is marked `approved` in the state ledger and the next stage is dispatched.
- **Request changes** → your feedback is logged and the **same** worker revises the deliverable in place.
- **Pause** → work stops with the stage left `awaiting-approval`; a later session resumes cleanly.

A stage is "done" when its agent's own gate/Definition-of-Done verdict is met **and** you approve it at
the checkpoint. Because state lives in `.workteam/` (not in chat memory), you can close the session and
resume later: the Coordinator reads the ledger first and continues from the first unapproved stage.

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
| 9 | DevOps Engineer | Build, release, deploy; provision local/prod infra (IaC) | QA-certified build + approved stacks | Deployed app + `Deployment-Report.md` |

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
| DevOps Engineer | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

\* Plan Architect `edit` is scoped to `Plan-Validation-Report.md` only.
† Code Reviewer `edit` is scoped to its own review report artifact only — **never production code**.
‡ QA Engineer `edit` is scoped to QA artifacts only (`QA-Report.md`, tests, fixtures, mocks, test data)
— **never production code**.

## End-to-End Development Workflow

`[CHK]` = requester review-and-approve checkpoint (Approve / Request changes / Pause). Every stage ends
with one, and every transition is written to `.workteam/` durable state.

```text
Requester
    |
    v
Coordinator  (reads .workteam/ state first & resumes; clarifies goal via #vscode/askQuestions;
              dispatches each worker as an isolated subagent; owns the state ledger + decision log)
    |
    v
1. Idea Discovery ........ idea.md ................... [CHK]
    v
2. Product Manager ....... PRD.md .................... [CHK]
    v
3. Solution Architect .... TDD.md .................... [CHK]
    v
4. Engineering Lead ...... Engineering-Plan.md ....... [CHK]
    v
5. Plan Architect ........ Plan-Validation-Report.md  [HARD GATE] [CHK]
    |                          |
    |                          +-- REVISE --> back to Engineering Lead (reuse / duplication findings)
    |                          |
    |                          +-- APPROVE
    v
    +----------------- parallel task execution (plan marks parallel-safe) -----------------+
    |                                                                                     |
    v                                                                                     v
6. Software Engineer                                                          6. Software Engineer
   (one approved task per subagent) [CHK]                                        (another safe task) [CHK]
    |                                                                                     |
    +---------------------------------------+---------------------------------------------+
                                            |
                                            v
                                     Integrated Change
                                            |
                                            v
7. Code Reviewer  (5 perspectives run as parallel, blind subagents -> consolidate -> verdict) [CHK]
                                            |
                          +-----------------+-----------------+
                          |                                   |
                   CHANGES REQUIRED                        APPROVE
                          |                                   |
                          v                                   v
                  Software Engineer               8. QA Engineer  (4 perspectives run as
                          ^                            parallel, blind subagents -> consolidate) [CHK]
                          |                                   |
                          |                        +----------+----------+
                          |                        |                     |
                          +--- QA FAIL          QA FAIL               QA PASS [CHK]
                                                                        |
                                                                        v
                                              9. DevOps Engineer  (implements approved TDD stacks via IaC)
                                                 - target? Local | Production
                                                 - new/changed infra -> Deployment-Plan.md [CHK]
                                                 - env ready -> proceed-to-deploy [CHK]
                                                 - build + deploy + verify
                                                                        |
                                                                        v
                                              Deployment-Report.md  (access + secure credentials)

Every stage transition updates .workteam/Workteam-State.md (stage/gate/task status) and
.workteam/Decisions-Log.md (clarifications). On restart the Coordinator reads these and resumes at the
first unapproved stage — no re-running, overwriting, or duplicating completed work.
```

The **Coordinator** owns cross-stage orchestration and gate enforcement. The **Engineering Lead** owns
cross-task parallelism. The **Software Engineer** owns controlled intra-task subagent parallelism. The
governing rule is:

> **Parallelize independent work. Serialize dependent decisions.**

---

# Agents and Skills

## 0. Coordinator Agent

**Purpose:** Own the overall task and orchestrate the workteam. Interview the requester, dispatch each
stage to the right worker as an isolated subagent, stop at every stage for the requester to review and
approve the deliverable, maintain durable state, and route rework loops until the task is releasable.

**Agent:** `.github/agents/coordinator.agent.md`

The Coordinator does not produce any stage deliverable itself. It dispatches every worker via
`runSubagent` (isolated context, concise result returned), enforces the Plan Architect gate before
implementation, and routes Review `CHANGES REQUIRED` and QA `FAIL` loops back to the Software Engineer.
It presents each deliverable at a **checkpoint** and advances only on the requester's approval, and it
maintains the workteam's **durable memory** so an interrupted run resumes cleanly.

### Skill

| Skill | Responsibility |
|---|---|
| `workteam-state-management` | Maintains `.workteam/Workteam-State.md` and `.workteam/Decisions-Log.md`; defines the checkpoint-approval, update-at-every-transition, and resume/idempotency protocols. |

The Coordinator's only writes are to `.workteam/*` (state ledger + decision log) — never to a stage
deliverable.

---

## 1. Idea Discovery Agent

**Purpose:** Interview, groom, challenge, and clarify the problem owner until the product idea is
sufficiently defined for Product Management without hidden assumptions. Handles both **greenfield** (new
product) and **brownfield** ideas — adding, modifying, updating, or refactoring an existing app — and
determines which up front.

**Input:** Problem owner / innovator (+ existing codebase for brownfield) → **Output:** `idea.md`

**Agent:** `.github/agents/idea-discovery.agent.md`

### Skills

| Skill | Responsibility |
|---|---|
| `existing-system-discovery` | **Brownfield only.** Read-only, product-level scan of the existing app — current features, journeys, rules, integration points, change surface, and (for a refactor) behaviour to preserve — feeding `idea.md`'s Existing System Context. |
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

## 9. DevOps Engineer Agent

**Purpose:** Deliver the QA-certified application into a running environment. Build, release, and publish
the software, and provision the **local** or **production** environment and infrastructure it needs using
**Infrastructure as Code** — activated only after QA PASS + approval, implementing the **approved** stacks
from `TDD.md`. **Read-only on production/source code** (it never edits the app); it authors IaC and runs
provisioning/deploys behind approval checkpoints.

**Input:** QA-certified build + approved Local/Production stacks (`TDD.md`) + infra state →
**Output:** provisioned infra (IaC), deployed & verified app, `Deployment-Plan.md`, `Deployment-Report.md`

**Agent:** `.github/agents/devops-engineer.agent.md`

### Skills

| Skill | Responsibility |
|---|---|
| `deployment-readiness-analysis` | Confirm QA certification, the certified build, and the approved target stack; select target. |
| `infrastructure-as-code-authoring` | Author/update reproducible IaC (Compose/Terraform/Pulumi/Ansible/K8s/Helm) for the approved stack. |
| `environment-provisioning` | Detect env/infra state (exists/healthy/needs-change) and provision or verify it idempotently. |
| `deployment-plan-design` | Break new setup/modification into a granular `Deployment-Plan.md` with order, risks, rollback. |
| `build-release-packaging` | Build, version, package, and publish the certified release artifact/image. |
| `deploy-execution-verification` | Execute the deploy, run smoke/health checks, and roll back safely on failure. |
| `deployment-reporting-handover` | Produce `Deployment-Report.md` with access details and secure credential referencing. |

Flow: confirm target (Local/Production) → assess env → if new/changed, an approved `Deployment-Plan.md` →
confirm ready → proceed-to-deploy approval → build & deploy & verify → `Deployment-Report.md`. Local
platforms must be open-source and IaC-deployable; **secrets are never committed** — the report references
a secure store. Re-runnable per target.

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
│   │   ├── qa-engineer.agent.md
│   │   └── devops-engineer.agent.md
│   └── skills/
│       └── <reusable skill folders>/SKILL.md
├── Constitution.md                # durable quality/spec/security principles (tailor per project)
├── .workteam/                     # created at run time in the TARGET project (not shipped here)
│   ├── Workteam-State.md          #   durable state ledger (stage/gate/task status)
│   └── Decisions-Log.md           #   append-only on-the-fly decisions & clarifications
├── docs/
│   ├── Token-Optimization-Review.md   # prompt-surface size review & guidance
│   └── SDD-Alignment-Review.md        # Specification-Driven Development alignment assessment
├── MANIFEST.md
└── README.md
```

`.github/` is the **single source of truth** and the installable workteam. Custom agents live under
`.github/agents/`; reusable Agent Skills live under `.github/skills/<skill-name>/SKILL.md`.
`Constitution.md` is the standing quality/spec/security bar every agent honours (via the
`constitution-governance` skill) — tailor it per project.
`docs/` holds design reviews that inform future changes (token optimization, SDD alignment).
The DevOps Engineer also produces `Deployment-Plan.md` / `Deployment-Report.md` at the target project root.

`.workteam/` is the Coordinator's **durable memory**, created at run time in the project the workteam is
operating on. It is committed by default so a project can version its workteam progress; delete it to
start a task fresh. It holds no product deliverable — those (`idea.md`, `PRD.md`, …) live at the project
root as before.

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

1. Invoke the **Coordinator** with your goal. It first reads any existing `.workteam/` state (resuming
   if a task is in progress), then clarifies scope and entry point via `#vscode/askQuestions`.
2. The Coordinator dispatches **Idea Discovery**, then **Product Manager**, then **Solution Architect**,
   then **Engineering Lead** — each as an isolated subagent, each gated on the prior deliverable.
   **After each stage it stops and asks you to review the deliverable and Approve / Request changes /
   Pause.** It advances only on your approval; "Request changes" re-runs the same worker in place.
3. **Plan Architect** validates the engineering plan against the codebase. On **REVISE**, the plan
   returns to the Engineering Lead; only **APPROVE** (plus your checkpoint approval) releases
   implementation.
4. The Coordinator dispatches one approved task per **Software Engineer** subagent, running
   parallel-safe tasks concurrently, and updates the task board in the state ledger.
5. **Code Reviewer** runs its five perspectives in parallel and returns a verdict; `CHANGES REQUIRED`
   loops back to Software Engineering.
6. **QA Engineer** runs its four perspectives in parallel and returns a verdict; `FAIL` loops back to
   Software Engineering (re-review if code changes).
7. On **QA PASS + your approval**, the **DevOps Engineer** is activated: it confirms the target (Local or
   Production), provisions/verifies the environment via IaC (an approved `Deployment-Plan.md` first if new
   setup/changes are needed), builds and deploys the certified build behind a proceed-to-deploy approval,
   verifies it, and delivers `Deployment-Report.md` with access details and secure credential referencing.
   Re-run it per target. Release/merge only when review and QA pass **and** you approve at the checkpoint.

Throughout, every agent honours `Constitution.md` — the standing quality/spec/security bar (tailor it per
project).

**Resuming after a disruption:** just invoke the Coordinator again. It reads `.workteam/Workteam-State.md`
and `.workteam/Decisions-Log.md`, continues from the first unapproved stage, and never re-runs an
approved stage, overwrites an approved deliverable, or re-dispatches a completed task.

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
- **Human-approved progression.** The Coordinator advances only on the requester's checkpoint approval,
  never on a technically-met gate alone.
- **Durable, resumable state.** Stage/task status and every decision live in `.workteam/`, so a disrupted
  run resumes exactly where it stopped — idempotent, no re-running or duplication.
- **Governed by a constitution.** `Constitution.md` states the durable quality/spec/security bar every
  agent honours; the stricter of a stage rule and the constitution wins.
- **Reproducible, IaC-provisioned delivery.** Environments are Infrastructure as Code (open-source local),
  secrets are never committed, and infrastructure changes are idempotent.
- **Source-of-truth hierarchy.** Downstream agents do not rewrite upstream intent.
- **Parallelize independent work; serialize dependent decisions.**
- **Evidence over claims.** Tests, review findings, QA verdicts, and deployment results trace to actual evidence.

---

# Version Notes

This repository contains the Coordinator-orchestrated redesign:

- Coordinator agent with isolated subagent delegation, per-stage checkpoint approvals, and a durable
  state ledger + decision log (`.workteam/`) for resumable, idempotent runs
- Idea Discovery, Product Manager, Solution Architect, Engineering Lead (as before, now
  `#vscode/askQuestions`-enabled and Coordinator-dispatchable)
- Plan Architect with codebase reuse analysis and duplication detection
- Software Engineer with controlled `runSubagent` parallel execution and reuse-target adherence
- Code Reviewer with five parallel, blind review perspectives (read-only on production code)
- QA Engineer with four parallel, blind validation perspectives (read-only on production code)
- DevOps Engineer with IaC provisioning and gated build/deploy of the QA-certified build to Local or
  Production, plus dual-stack (local + production) recommendation and approval in the Solution Architect
- Shipped, tailorable `Constitution.md` governing quality/spec/security across the team
- Leaner agent prompts: large deliverable templates moved into on-demand `*-output-contract` skills
