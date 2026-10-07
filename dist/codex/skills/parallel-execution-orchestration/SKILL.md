---
name: parallel-execution-orchestration
description: Convert the engineering dependency graph into dependency-safe execution waves and parallel groups for concurrent Software Engineer agents while controlling shared-write risk, contracts, ownership, and integration checkpoints.
---

# Parallel Execution & Wave Orchestration

## Purpose

Maximize safe implementation concurrency without creating inconsistent code, merge conflicts, or contract drift.

The Engineering Lead is the cross-task concurrency owner.

Core rule:

> Parallelize independent work. Serialize dependent decisions.

---

# Inputs

Use:

- all engineering task IDs;
- dependency graph;
- architecture contracts;
- affected components/modules;
- schema/API ownership;
- external dependencies;
- integration checkpoints.

---

# Hard Dependency vs Contract Dependency

## Hard Dependency

Task B cannot safely begin until Task A produces an implementation artifact.

Example:

```text
DB-001 -> BE-004
```

when BE-004 cannot compile or function until the schema/migration exists.

## Contract Dependency

Task B can begin before Task A completes because the interface is already fixed.

Example:

```text
BE-004 and FE-006
```

may run concurrently when `API-009` is approved and stable.

Do not serialize work merely because one task consumes another task's eventual output.

---

# Parallel Safety Assessment

For each task assess:

1. Are hard dependencies satisfied?
2. Is the relevant contract stable?
3. Does another concurrent task modify the same contract?
4. Is there shared file/module ownership?
5. Is there shared schema/migration ownership?
6. Could both tasks make conflicting architecture assumptions?
7. Can each task be verified independently?
8. Is there a defined convergence/integration checkpoint?

Use:

- `Yes`
- `No`
- `Conditional`

---

# Shared Write Risk

Classify:

- Low
- Medium
- High

## Low

Distinct components/files with stable contracts.

## Medium

Some shared configuration/types or common utilities.

Parallel execution may proceed with explicit ownership.

## High

Same core module, same migration chain, same public contract, or tightly coupled refactor.

Prefer serialization or intentional task partitioning.

---

# Execution Waves

A wave is the set of tasks whose hard dependencies are satisfied at the same logical point.

Example:

```text
Wave 0
- DB-001
- PLAT-001

Wave 1
- BE-002
- BE-003
- FE-001

Wave 2
- INT-001
- FE-004
- QA-006
```

Wave does not mean sprint or duration.

---

# Parallel Groups

Within a wave, form concurrency groups.

Example:

```text
PG-01
- BE-002
- BE-003
- FE-001
```

All tasks in a parallel group may be assigned to separate Software Engineer agents concurrently.

Use stable IDs:

- `PG-01`
- `PG-02`

---

# Task Ownership

Each task has one primary implementation owner role.

Default:

```text
BE/FE/DB/INT/PLAT/SEC/OBS/DATA
    -> Software Engineer or appropriate specialist
```

Do not assign the same task to multiple independent implementers.

If a task is too broad for one owner, return it to task decomposition and split it before parallel dispatch.

---

# Write Isolation

Prefer task boundaries that map to distinct:

- components;
- modules;
- services;
- interfaces;
- migrations;
- test surfaces.

When concurrent tasks share files:

- specify ownership;
- avoid simultaneous edits to the same contract;
- establish integration order.

If safe isolation cannot be achieved, serialize.

---

# Interface-First Parallelization

Stable contracts can unlock concurrency.

Examples:

- approved API contract allows frontend/backend parallel work;
- approved event schema allows producer/consumer parallel work;
- approved data migration contract allows application/test preparation in parallel.

Do not let implementation agents independently modify the shared contract.

Contract change must return to the appropriate upstream owner.

---

# Integration Checkpoints

Every parallel group should converge at a named checkpoint such as:

- `IC-01 API integration`
- `IC-02 Database migration integration`
- `IC-03 End-to-end feature integration`
- `IC-04 Release candidate validation`

Define which task IDs must be complete before the checkpoint.

---

# Critical Path

Preserve the structural dependency chain.

Do not delay critical-path work in favor of low-value parallelism.

Without duration estimates, do not claim a time-based critical path.

---

# Output Contribution

Populate:

## Parallel Execution Plan

| Parallel Group | Wave | Tasks | Parallel-Safe | Shared Write Risk | Integration Checkpoint |
|---|---|---|---|---|---|

Update each task with:

- Execution Wave
- Parallel Group
- Parallel-Safe
- Shared Write Risk
- Integration Checkpoint

---

# Completion Check

Pass when:

1. all Ready tasks have a wave;
2. hard dependencies are respected;
3. contract dependencies are not unnecessarily serialized;
4. concurrency groups are explicit;
5. shared-write risk is controlled;
6. each task has one primary owner;
7. integration checkpoints exist;
8. critical path is preserved.
