---
name: dependency-sequencing-analysis
description: Build and validate the engineering task dependency graph, detect circular or missing dependencies, identify parallelizable work, implementation waves, integration checkpoints, and critical-path task chains.
---

# Dependency & Sequencing Analysis

## Purpose

Turn a flat task list into an executable work graph.

## Dependency Types

The canonical task graph uses task-to-task dependencies.

For every task capture:

- `Depends On`
- `Blocks`

These fields must use task IDs only.

Track non-task dependencies separately under:

`External Dependencies`

## Infer Dependencies from Design

Common dependency patterns:

### Schema before code that requires the schema

```text
DB-001 -> BE-003
```

unless the project deliberately uses a different migration sequencing strategy.

### Provider before consumer integration verification

```text
BE-004 -> FE-006
BE-004 -> QA-010
```

Contract-first work may allow FE to proceed in parallel if the contract is already fixed.

Do not add dependencies merely because one task is numbered earlier.

### Infrastructure before deployment-dependent work

```text
PLAT-002 -> OBS-003
PLAT-002 -> QA-015
```

### Implementation before end-to-end QA

```text
BE-007, FE-005 -> QA-012
```

## Dependency Challenge

For each dependency ask:

- Is the predecessor truly required?
- Could both proceed from an approved contract?
- Is this actually an external dependency?
- Does the dependency represent architecture or only convenience?

Avoid unnecessary serialization.

## Circular Dependency Detection

Detect cycles such as:

```text
BE-003 -> FE-002 -> BE-003
```

Resolve by:

- fixed interface contract;
- splitting a foundational task;
- identifying the actual common predecessor;
- routing unresolved architecture issue upstream.

Never leave a cycle in the final plan.

## Parallelization

Identify task sets that can proceed concurrently after prerequisites.

Use task IDs.

Example:

```text
After DB-001:
- BE-002
- BE-003
- DATA-001
```

## Implementation Waves

Group by dependency readiness:

- Wave 0: foundations
- Wave 1: first independent implementation
- Wave 2: dependent capabilities/integrations
- Wave 3: end-to-end verification/release

The actual number of waves depends on the graph.

A wave is not a sprint.

## Critical Path

Identify dependency chains that constrain completion.

Without estimates, critical path here means **structural dependency chain**, not duration-based CPM.

Example:

```text
DB-001 -> BE-004 -> FE-006 -> QA-011
```

Do not claim which path is time-critical unless durations are known.

## Integration Checkpoints

Identify points where parallel work must converge.

Examples:

- API contract integration
- end-to-end feature integration
- external sandbox validation
- migration rehearsal
- release candidate verification

## Output Contribution

Populate:

- Dependency Matrix
- Implementation Waves
- Parallelization Opportunities
- Critical Path
- Integration Checkpoints

## Completion Check

Pass when:

1. dependency graph is acyclic;
2. task IDs are used consistently;
3. avoidable serialization is removed;
4. parallel work is explicit;
5. integration points are explicit;
6. external dependencies are separated.
