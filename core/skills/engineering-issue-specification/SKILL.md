---
name: engineering-issue-specification
description: Convert each engineering task into a self-contained issue-ready work specification containing objective, context, source traceability, scope, technical constraints, acceptance criteria, verification, dependencies, and definition of done.
---

# Engineering Issue Specification

## Purpose

Ensure every planned task can be copied into GitHub Issues or another work-management system and assigned without requiring hidden context.

## Self-Contained Context Standard

An engineer should understand:

- why the task exists;
- what behaviour/design it implements;
- where it fits;
- what is explicitly included;
- what is excluded;
- which contracts/constraints must be followed;
- how completion will be verified.

The task may reference `PRD.md` and `TDD.md`, but it must not require access to the original discovery conversation.

## Required Metadata

Each task includes:

- ID
- Title
- Workstream
- Status
- Priority
- Related Epic(s)
- Related User Story(ies)
- Source Requirements
- Architecture References

Use `None` where a field legitimately has no value.

## Objective

One concise technical outcome.

Avoid implementation steps in the objective.

## Context

Explain:

- relevant product journey;
- component role;
- why this task is needed;
- dependencies on nearby capabilities.

## Scope

State concrete required behaviour.

Include relevant:

- validations;
- state;
- auth;
- transaction;
- API;
- integration;
- telemetry;
- error behaviour.

## Out of Scope

Prevent scope creep and clarify ownership split.

Use task IDs when another task owns related work.

## Technical Constraints

Carry forward applicable TDD decisions:

- ADR;
- technology;
- interface contract;
- data ownership;
- security;
- resilience;
- compatibility.

Do not invent new architecture.

## Interface / Data Impact

Identify affected:

- component;
- API;
- schema/entity;
- event;
- integration;
- configuration;
- runtime resource.

## Engineering Acceptance Criteria

Use:

`ENG-AC-xxx`

Criteria must be testable.

They may specify technical completion but cannot contradict product ACs.

## Verification Requirements

State relevant evidence:

- unit tests;
- integration tests;
- contract tests;
- UI tests;
- static checks;
- security checks;
- performance checks;
- manual validation.

## Dependencies

Use:

```text
Depends On: BE-001, DB-002
Blocks: FE-004, QA-005
External Dependencies: None
```

Task fields use IDs only.

## Implementation Notes

Optional.

Use for:

- known repository patterns;
- likely modules;
- safe sequencing;
- design cautions.

Do not prescribe unnecessary line-level implementation.

## Definition of Done

Tailor the shared DoD to the task.

Do not claim generic documentation or telemetry is required if irrelevant.

## Issue Quality Test

Reject a task if:

- title is vague;
- objective cannot be tested;
- source IDs are absent without justification;
- scope mixes unrelated outcomes;
- dependencies use prose instead of IDs;
- acceptance criteria merely say "works";
- engineer must make a new architecture decision;
- task repeats another task.

## Output Contribution

Refine all Engineering-Plan task sections into issue-ready format.

## Completion Check

Pass when every task is assignable as written.
