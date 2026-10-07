---
name: engineering-plan-validation
description: Validate Engineering-Plan.md for PRD/TDD fidelity, complete implementation and QA coverage, task cohesion, issue readiness, dependency integrity, traceability, cross-functional completeness, and implementation handoff readiness.
---

# Engineering Plan Validation

## Purpose

Determine whether `Engineering-Plan.md` can be handed to an implementation team without requiring them to invent product or architecture decisions.

## Classifications

Use:

- Pass
- Non-Blocking Gap
- Implementation-Blocking Product Gap
- Implementation-Blocking Architecture Gap
- Missing Implementation Coverage
- Missing Verification Coverage
- Task Ambiguity
- Task Overbreadth
- Task Overfragmentation
- Dependency Gap
- Dependency Cycle
- Traceability Gap
- Issue Context Gap
- Scope Leakage
- Architecture Drift
- Duplicate Work

## Validate Source Fidelity

Confirm:

- tasks implement the PRD;
- tasks follow the TDD;
- no future/out-of-scope work leaked in;
- no business rule was changed;
- no architecture was redesigned silently.

## Validate Coverage

For every Must-Have verify:

```text
Requirement / Story
 -> Implementation task(s)
 -> Verification task(s)
```

Check architecture coverage for:

- components;
- APIs;
- data;
- integrations;
- security;
- reliability;
- deployment;
- observability;
- migrations.

## Validate Task Cohesion

Flag tasks that:

- span unrelated components;
- combine independent outcomes;
- are only file edits;
- are too vague;
- duplicate another task.

## Validate QA

Confirm:

- positive and negative behaviour;
- permissions;
- edge cases;
- critical integrations;
- NFRs;
- security;
- resilience;
- release/deployment validation

have appropriate verification paths.

## Validate Dependencies

Confirm:

- IDs exist;
- `Depends On` / `Blocks` are reciprocal where represented;
- no cycles exist;
- no task depends on itself;
- external dependencies are separate;
- parallelization is not unnecessarily constrained.

## Validate Issue Readiness

Sample every task and verify:

- objective;
- context;
- scope;
- out-of-scope;
- source references;
- technical constraints;
- acceptance criteria;
- verification;
- dependencies;
- DoD.

Reject hidden-context tasks.

## Validate Sequencing

Confirm waves reflect dependencies.

Do not treat waves as dates/sprints.

Check that integration checkpoints occur after necessary predecessors.

## Validate Upstream Blockers

Blocked tasks must identify:

- blocker;
- upstream owner;
- decision/information needed.

Do not mark them Ready.

## Result

Return exactly one:

### `IMPLEMENTATION READY`

No material planning gap remains.

### `IMPLEMENTATION READY WITH NON-BLOCKING ITEMS`

Remaining issues do not force implementers to invent behaviour/design.

### `NOT IMPLEMENTATION READY`

At least one blocking product, architecture, coverage, dependency, or task-quality issue remains.

For every failure report:

- issue;
- classification;
- affected task(s);
- source IDs;
- why it matters;
- owner/skill to revisit;
- resolution needed.

## Completion Check

Validation is complete when:

1. source fidelity checked;
2. implementation coverage checked;
3. QA coverage checked;
4. dependency graph checked;
5. issue readiness checked;
6. sequencing checked;
7. upstream blockers checked;
8. readiness result returned.
