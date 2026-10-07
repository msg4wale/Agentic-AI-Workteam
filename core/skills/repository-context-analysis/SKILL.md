---
name: repository-context-analysis
description: Inspect the smallest relevant repository surface for an assigned task to identify current architecture, patterns, modules, tests, contracts, schemas, commands, conventions, and implementation impact before editing.
---

# Repository Context Analysis

## Purpose

Understand the current code before changing it.

Do not implement during this analysis unless a trivial read-only discovery action naturally reveals the exact required change.

## Search Strategy

Start from task references:

- component/module name;
- API route/interface;
- entity/table/model;
- integration name;
- user journey/screen;
- existing test names.

Then expand only as needed.

## Inspect Relevant Areas

### Project Structure

Identify:

- application boundaries;
- package/module organization;
- test locations;
- configuration;
- build tooling.

### Existing Patterns

Find established patterns for:

- services;
- controllers/handlers;
- repositories/data access;
- validation;
- errors;
- logging;
- authentication/authorization;
- dependency injection;
- async/background work;
- frontend state/components;
- tests.

### Interfaces

Inspect:

- current API contracts;
- types/models;
- events;
- integration adapters.

### Data

Inspect:

- models/schema;
- migrations;
- constraints;
- transaction patterns.

### Tests

Identify:

- nearest analogous tests;
- test framework;
- fixtures/factories;
- integration test setup;
- mocking conventions.

### Commands

Determine repository-supported commands for:

- tests;
- lint;
- type checks;
- format;
- build;
- migrations.

Prefer project scripts over inventing custom commands.

## Existing Architecture vs TDD

If repository reality differs from TDD:

1. identify exact discrepancy;
2. determine whether this task includes migration/refactor work;
3. do not silently redesign;
4. escalate material architecture drift.

## Impact Map

Before implementation know:

- likely files/modules;
- test files;
- config/schema impact;
- compatibility risk;
- neighbouring behaviour that could regress.

## Avoid Context Bloat

Do not read the entire repository without need.

Stop when you have enough evidence to implement safely.

## Completion Check

Pass when:

1. change location is known;
2. existing patterns are known;
3. verification path is known;
4. key compatibility risks are understood;
5. no unresolved repository/TDD conflict blocks work.
