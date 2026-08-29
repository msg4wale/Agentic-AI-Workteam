---
name: codebase-reuse-analysis
description: Locate existing patterns, utilities, modules, and libraries in the repository that are relevant to each engineering-plan task, so implementation reuses what already exists instead of rebuilding it. Use during plan validation, before implementation begins.
---

# Codebase Reuse Analysis

## Purpose

For each task in an `Engineering-Plan.md`, identify the existing code the task should build on:
reusable patterns, utilities, helpers, modules, base classes, configuration, and third-party or
internal libraries already present in the repository.

This skill discovers reuse candidates. It does not implement, and it does not modify code or the plan.

## Relationship to Repository Context Analysis

Reuse the search-and-inspection method of
[repository-context-analysis](../repository-context-analysis/SKILL.md). The difference in intent:

- `repository-context-analysis` prepares to implement one task.
- `codebase-reuse-analysis` evaluates a whole plan for reuse and duplication risk, read-only.

Do not duplicate that skill's procedure here — apply it per task cluster.

## Parallel, Isolated Scanning

For a multi-task plan, group tasks by area (backend module, data layer, API/integration, frontend,
platform) and dispatch **one read-only scan per group** via `runSubagent`.

Each scan subagent must:

- stay read-only (no edits, no builds that mutate state);
- return only **concise findings** — relevant paths, symbols, libraries, and candidate duplication —
  never a raw dump of file contents into the caller's context;
- note where a task has **no existing counterpart** ("none found").

Consolidate all subagent findings before classification.

## What to Look For

Per task, search from the task's references (module, route, entity, integration, screen, test name):

### Reusable building blocks
- Existing utilities/helpers that already perform the needed operation.
- Established patterns for the same concern (validation, auth, error handling, pagination, retries).
- Base classes, interfaces, mixins, decorators, or middleware to extend.
- Shared configuration, constants, feature flags, and env handling.

### Existing capabilities
- Endpoints, services, jobs, or components that already deliver part of the task's behaviour.
- Data models, schemas, migrations, or repositories covering the same entities.
- Integration clients/SDK wrappers already wired to the same external system.

### Libraries
- Internal packages and third-party libraries already in the dependency manifest that provide the
  capability, so no new dependency or hand-rolled implementation is needed.

## Findings Format

Return, per task:

- `Task ID`
- `Relevant existing code`: path + symbol for each candidate
- `Relevant libraries`: name + why it fits
- `Reuse candidate`: the specific thing to reuse/extend, or `none found`
- `Confidence`: high / medium / low, with the evidence

## Boundaries

- Read-only. Never edit code or the plan.
- Do not decide final reuse policy when a legitimate choice exists — surface it for a decision.
- Prefer precise, evidence-backed candidates over broad guesses; "none found" is a valid result.
