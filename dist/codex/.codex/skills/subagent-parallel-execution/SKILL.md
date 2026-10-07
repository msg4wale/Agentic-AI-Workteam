---
name: subagent-parallel-execution
description: Assess and orchestrate safe intra-task subagent delegation for independent repository analysis, contract tracing, test planning, security analysis, verification, and selectively isolated parallel implementation.
---

# Subagent & Parallel Execution

## Purpose

Use subagents to reduce task latency and preserve primary-agent context without sacrificing consistency.

The primary Software Engineer remains accountable for the final integrated change.

Core rule:

> Parallelize independent work. Serialize dependent decisions.

---

# Step 1 — Decide Whether Subagents Add Value

Subagents are useful when the task has independent workstreams such as:

- repository exploration;
- requirements/contract tracing;
- test analysis;
- security analysis;
- migration impact analysis;
- integration analysis;
- verification.

Do not spawn subagents for trivial work.

---

# Step 2 — Choose Subagent Roles

Use only relevant roles.

## Repository Explorer

Read-only by default.

Returns:

- relevant files/modules;
- existing patterns;
- analogous implementation;
- test locations;
- likely impact surface.

## Requirement / Contract Analyst

Read-only.

Returns:

- PRD/TDD/task references;
- fixed API/data/integration contracts;
- acceptance requirements;
- constraints;
- unresolved conflicts.

## Test Analyst

Read-only or test-edit capable if explicitly delegated.

Returns:

- required test scenarios;
- existing test coverage;
- missing coverage;
- recommended commands.

## Security / Risk Analyst

Read-only.

Returns task-specific concerns:

- auth/authz;
- sensitive data;
- injection/trust;
- concurrency/idempotency;
- migration/data integrity;
- failure/retry risk.

## Verification Subagent

Executes independent checks after implementation.

Returns concise evidence:

- command;
- result;
- failures.

---

# Step 3 — Parallel Analysis

Safe default:

```text
Primary Engineer
   |
   +-- Repository Explorer
   +-- Requirement/Contract Analyst
   +-- Test Analyst
   +-- Security Analyst
```

Run these concurrently when their work is independent.

Each subagent must return a concise structured summary.

Avoid returning large raw file dumps.

---

# Step 4 — Consolidate Before Implementation

The primary agent must reconcile findings before making consequential code changes.

Resolve:

- contradictory repository patterns;
- task/TDD mismatch;
- test expectation conflicts;
- contract ambiguity.

If reconciliation requires an upstream decision, stop and route it.

---

# Step 5 — Parallel Write Assessment

Concurrent editing is exceptional.

Allow it only if all criteria pass:

## Isolation

Each writer owns distinct:

- component;
- module;
- file set;
- test surface.

## Stable Contracts

Shared API/data/event interfaces are already approved.

## No Shared Decision

Writers do not independently decide the same:

- API shape;
- schema shape;
- authorization model;
- architectural boundary.

## Deterministic Integration

The primary engineer can integrate the outputs without arbitrary conflict resolution.

## Verification

There is an integration test/checkpoint proving the pieces work together.

---

# Examples

## Safe

```text
Fixed API-004

Writer A:
Backend handler/service implementation

Writer B:
Frontend client/component implementation

Writer C:
E2E test in isolated test files
```

provided no writer changes `API-004`.

## Unsafe

```text
Writer A:
Changes API response schema

Writer B:
Implements frontend against assumed schema

Writer C:
Changes shared generated types
```

Serialize the contract decision first.

---

# Worktree / Isolation Principle

Where the platform supports isolated branches/worktrees/subagent sandboxes, prefer isolation for parallel writers.

Do not assume isolation exists.

If all writers operate in one working tree, be more conservative and avoid overlapping edits.

---

# Parallel Verification

After implementation, independent checks may run concurrently where tooling permits:

```text
+-- targeted tests
+-- type/static checks
+-- build
+-- security-oriented checks
```

Do not run commands concurrently if they mutate the same build/test state unsafely.

---

# Subagent Result Contract

Each subagent should return:

```markdown
## Subagent Result

**Role:** Repository Explorer
**Scope:** BE-002
**Status:** Complete

### Findings
- ...

### Relevant Files
- ...

### Risks / Conflicts
- None

### Recommendation
- ...
```

Keep summaries compact.

---

# Primary Agent Accountability

The primary Software Engineer must:

- validate subagent findings;
- integrate decisions;
- own final code;
- own final test results;
- own task acceptance;
- own implementation handoff.

Never blame a subagent for an unverified change.

---

# Completion Check

This skill passes when:

1. subagent utility was assessed;
2. independent analysis was parallelized when beneficial;
3. write-capable delegation was isolated and contract-safe;
4. findings were consolidated;
5. parallel verification was used where safe;
6. primary ownership remained clear.
