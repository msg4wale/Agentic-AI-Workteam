---
name: focused-implementation
description: Implement one assigned engineering task with minimal, cohesive repository changes that follow approved architecture, project conventions, task scope, interfaces, data rules, security controls, and observability requirements.
---

# Focused Implementation

## Purpose

Produce the smallest complete implementation that satisfies the assigned task.

## Before Editing

Confirm:

- task readiness;
- repository impact map;
- accepted contract/design;
- tests to add/update.

## Implementation Sequence

Choose the sequence appropriate to the task.

Typical safe sequence:

1. update/add tests when test-first is useful;
2. implement domain/application behaviour;
3. implement persistence/interface changes;
4. integrate dependency;
5. add telemetry/config;
6. update directly required docs;
7. run targeted verification.

Do not force this sequence if repository architecture implies another.

## Minimal Change Rule

Prefer:

- modifying existing abstractions;
- reusing established helpers;
- following current patterns;
- small cohesive refactors.

Avoid:

- broad renames;
- unrelated cleanup;
- framework upgrades;
- package upgrades;
- replacing working architecture.

## Behaviour Fidelity

Implementation must preserve:

- PRD acceptance intent;
- BR rules;
- permissions;
- error behaviour;
- edge-case expectations;
- NFR constraints.

## Architecture Fidelity

Follow:

- ADR decisions;
- component ownership;
- API contracts;
- data ownership;
- transaction/consistency model;
- integration semantics;
- security controls;
- resilience requirements;
- deployment constraints.

## Code Quality

Prefer:

- clear names;
- small cohesive functions/classes;
- explicit error handling;
- minimal duplication;
- testability;
- readable control flow.

Avoid abstractions that do not reduce actual complexity.

## Compatibility

Where applicable preserve:

- API compatibility;
- schema migration safety;
- serialized formats;
- configuration compatibility;
- existing callers.

Breaking changes require explicit design approval.

## Dependencies

Do not add a dependency for trivial functionality.

If necessary:

- use project-standard package manager;
- pin/manage version according to project conventions;
- update lockfile;
- validate license/security implications where tooling exists.

## Documentation

Update only documentation directly required by the task, such as:

- config keys;
- environment variable documentation;
- public interface usage;
- operational procedure.

Do not create broad documentation unrelated to implementation.

## Completion Check

Pass when the assigned outcome exists completely and no unapproved scope has been added.
