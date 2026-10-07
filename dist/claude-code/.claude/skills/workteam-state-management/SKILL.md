---
name: workteam-state-management
description: Maintain durable workteam state and a decision log so the Coordinator can enforce per-stage checkpoint approvals and resume exactly where it stopped after any disruption, without re-running approved stages, overwriting approved deliverables, or duplicating work. Use to read/initialize/update the state ledger and decision log at every stage transition.
---

# Workteam State Management

## Purpose

Give the workteam a **durable, transferable memory** so orchestration survives interruption, stays
idempotent, and can resume on a different harness. Three files under `.workteam/` hold everything needed
to answer "where are we, what was decided, and what is safe to do next":

- `.workteam/Workteam-State.md` — the state ledger (stage/gate/task status, deliverables, open loops).
- `.workteam/Decisions-Log.md` — an append-only log of on-the-fly decisions and clarifications.
- `.workteam/Project.md` — the portable project manifest (framework version, installed harnesses,
  last-active-harness, deliverable index, transfer log) used for cross-harness resume.

This skill defines the file schemas and the read/update/resume/approval/transfer protocols. It does not
produce any stage deliverable.

## Ownership & Write Rules

- During an orchestrated run, the **Coordinator is the sole writer** of both files. Workers **return**
  their material decisions in their concise result and the Coordinator appends them. This prevents
  concurrent-write conflicts when parallel Software Engineer subagents run.
- A worker running **standalone** (no Coordinator) may update the two files itself.
- These files are **orchestration state, not deliverables**. Writing them is scoped to `.workteam/*`.
  Never write a stage deliverable (`idea.md`, `PRD.md`, `TDD.md`, `Engineering-Plan.md`,
  `Plan-Validation-Report.md`, source, `QA-Report.md`, `Deployment-Plan.md`, `Deployment-Report.md`)
  through this skill.

## Worker Participation (the "State & Decisions" contract)

Every worker agent — Idea Discovery, Product Manager, Solution Architect, Engineering Lead, Plan
Architect, Software Engineer, Code Reviewer, QA Engineer — participates in durable memory as follows.
Each worker states a short pointer to this contract rather than repeating it:

- **On start**, read `.workteam/Decisions-Log.md` (and your input artifact/task) to inherit prior
  decisions and on-the-fly clarifications, so you never re-ask a resolved question or contradict an
  approved decision. Do not overwrite a deliverable the requester has already approved, and do not
  re-implement a task the state ledger marks `done`; work only what is in scope.
- **On finish**, return your material decisions/clarifications (with the requirement/artifact/task IDs
  they affect) in your concise result so the Coordinator can append them to `.workteam/Decisions-Log.md`
  and update the state ledger / task board. During an orchestrated run, do **not** write the ledgers
  yourself — the Coordinator is the sole writer (this keeps parallel subagents free of write conflicts).
- Running **standalone** (no Coordinator), you may read and append the `.workteam/` files directly.
- Read-only reviewers (Code Reviewer, QA Engineer) treat the decision log as read context only and never
  edit production code; QA's writes remain limited to its own QA artifacts.

## Stage & Status Model

Stages (in order): `idea-discovery`, `product-manager`, `solution-architect`, `engineering-lead`,
`plan-architect`, `software-engineer`, `code-reviewer`, `qa-engineer`, `devops-engineer`, `release`.
The `devops-engineer` stage is re-runnable per target (Local / Production); track each target's status.

Per-stage status: `not-started | in-progress | awaiting-approval | approved | blocked`.

Per implementation task (`TASK-ID`): `pending | in-progress | in-review | in-qa | done | blocked`.

## `Workteam-State.md` Schema

```markdown
# Workteam State

## Task
- Title:
- Requester:
- Entry Stage:
- Current Stage:
- Last Updated:

## Stage Ledger
| Stage | Status | Deliverable | Fingerprint | Approved At | Notes |
|---|---|---|---|---|---|
| idea-discovery | approved | idea.md | <hash/last-updated> | <ts> | |
| product-manager | awaiting-approval | PRD.md | <hash> | | |
| solution-architect | not-started | TDD.md | | | |
| ... | | | | | |

## Implementation Task Board
| TASK-ID | Status | Owner | Parallel Group | Review | QA | Notes |
|---|---|---|---|---|---|---|

## Open Loops
| Loop | Type (PLAN-REVISE / REVIEW-CHANGES / QA-FAIL) | Owner Stage | Opened | Detail |
|---|---|---|---|---|

## Transition History
| Timestamp | From → To | Trigger | By |
|---|---|---|---|
```

The **Fingerprint** is a cheap content marker (git blob hash, or path + last-updated) used to detect
whether an approved deliverable has changed unexpectedly.

## `Decisions-Log.md` Schema

Append-only. Never rewrite or delete prior entries; supersede with a new entry that references the old.

```markdown
# Decisions Log

| ID | Timestamp | Stage | Question / Context | Decision / Answer | Decided By | Affects |
|---|---|---|---|---|---|---|
| DEC-001 | <ts> | solution-architect | Which persistence store for MVP? | Postgres (managed) | stakeholder | ADR-003, TDD §8.4 |
| DEC-002 | <ts> | product-manager | approval of PRD.md | Approved | stakeholder | PRD.md |
```

`Affects` links the decision to the artifact/requirement IDs it constrains, so downstream workers
inherit it.

## Update Protocol (every transition)

Update the ledger at each of these moments — never batch them:

1. **Stage dispatch** → set stage `in-progress`; add a Transition History row.
2. **Worker returns** → set stage `awaiting-approval`; record deliverable path + fingerprint; append any
   returned clarifications as `DEC-###`.
3. **User approves** → set stage `approved` with `Approved At`; append the approval as `DEC-###`; set
   the next stage `not-started → in-progress` only when it is actually dispatched.
4. **User requests changes** → keep stage `awaiting-approval`; append the feedback as `DEC-###`; the
   same worker is re-dispatched (deliverable revised in place).
5. **Rework verdict** (Plan REVISE / Review CHANGES REQUIRED / QA FAIL) → open an Open Loops row and set
   the owning stage/task back to the appropriate active status.
6. **Task-board changes** (implementation) → update each `TASK-ID` status as it moves review→qa→done.

## Checkpoint Approval Procedure

After a worker returns and the ledger is set to `awaiting-approval`:

1. Present a **concise summary** of the deliverable and its location to the user.
2. Ask, via `AskUserQuestion`: **Approve** / **Request changes** / **Pause**.
3. **Approve** → mark `approved`, log `DEC-###`, proceed to dispatch the next stage.
4. **Request changes** → log the feedback `DEC-###`, re-dispatch the **same** worker to revise the
   existing deliverable in place (do not create a second copy).
5. **Pause** → stop with the stage left `awaiting-approval`; the ledger enables a clean later resume.

Every stage passes this checkpoint — including the Plan Architect, Code Review, and QA verdict stages,
whose verdicts are shown to the user for approval before the workteam proceeds.

## Resume & Idempotency Procedure (run startup)

Before any dispatch, **read `.workteam/Workteam-State.md` and `.workteam/Decisions-Log.md` first**:

- If **absent** → fresh run: create both files; begin at the entry stage (`in-progress`).
- If **present** → reconstruct approved stages, current stage, open loops, and decisions, then:
  - **Resume at the first stage that is not `approved`** (respecting its sub-status).
  - Never re-run an `approved` stage; never regenerate or overwrite an `approved` deliverable.
  - A deliverable that exists but is `awaiting-approval` resumes **at its approval checkpoint**, not by
    re-running the worker (unless the user requested changes).
  - Never re-dispatch a `done` `TASK-ID`; resume only `pending` / in-flight tasks. Re-open a task only
    on an explicit REVIEW-CHANGES / QA-FAIL loop.
  - Pass the relevant `Decisions-Log.md` entries to each dispatched worker so resolved clarifications
    are not asked again.
- If a deliverable's current fingerprint differs from the approved fingerprint, flag it to the user
  rather than silently trusting or overwriting it.

## Cross-Harness Transfer (resume on a different harness)

A project can be started on one harness (Claude Code, Copilot, or Codex) and continued on another. All
project state is **harness-neutral and git-portable** — deliverables at the project root, and the
`.workteam/` ledgers. The portable record is **`.workteam/Project.md`** (the project manifest). Only
**committed** files transfer; ephemeral chat/session context does not — so flush before you switch.

### `Project.md` manifest
Tracks: Project title, Framework Version, Installed Harnesses, **Last Active Harness @ timestamp**,
Current Stage (mirrors the state ledger), a Deliverables presence/approval table, and a **Transfer Log**
(timestamp · from-harness · to-harness · at-stage · notes).

### Flush-on-leave (before switching harness)
1. Make `Workteam-State.md` and `Decisions-Log.md` reflect true current reality.
2. Update `Project.md`: set **Last Active Harness** to the current harness + timestamp, refresh Current
   Stage and the Deliverables table, and append a **Transfer Log** row when you know the target harness.
3. **Commit** (git). Uncommitted work does not transfer.

### Resume-on-enter (on a possibly different harness)
1. Read `Project.md` **first**, then the state and decision ledgers.
2. If **Last Active Harness ≠ the current harness**, note the handoff (append a Transfer Log row) and
   continue — do not restart.
3. Resume per **Resume & Idempotency** above (first non-approved stage; never re-run/overwrite/duplicate).
4. **Version drift:** if `Project.md` Framework Version ≠ the installed package's stamp (in
   `CLAUDE.md` / `WORKTEAM.md` / `AGENTS.md`), surface it to the user before proceeding — behaviour may
   differ; offer to re-install matching packages (`build/generate.py --install <harness> .`).
5. Set Last Active Harness to the current harness and keep maintaining `Project.md` each transition.

The manifest and ledgers reference agents by **slug** and deliverables by **root path**, so nothing in
them is harness-specific.

## Boundaries

- Only `.workteam/*` is written here. Stage deliverables remain owned by their workers.
- The decision log is append-only; corrections are new superseding entries.
- Keep entries concise and evidence-linked (artifact/requirement IDs), not full transcripts.
