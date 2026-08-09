---
name: epic-user-story-design
description: Decompose confirmed MVP product capabilities and journeys into coherent epics and vertical user stories with traceability to goals, users, features, and business value.
---

# Epic & User Story Design

## Purpose

Structure confirmed product behaviour into product slices that can later support architecture, engineering planning, and QA.

Do not create engineering tasks.

## Epic Design

Use IDs:

`EPIC-001`, `EPIC-002`, ...

An Epic should represent a coherent product capability or user/business outcome.

For each Epic capture:

- Name
- Objective
- Primary persona(s)
- Business value
- Related Product Goal
- Related Feature(s)
- Relevant journey(s)
- Priority
- Dependencies

Avoid technical-layer epics such as:

- Backend
- Database
- APIs
- Frontend
- Infrastructure

## User Story Design

Use IDs:

`US-001`, `US-002`, ...

Prefer:

> As a [specific role], I want [capability/outcome], so that [value].

A story should represent a meaningful vertical product behaviour.

## Story Quality

Check that each story:

- has a real actor where appropriate;
- expresses outcome/value;
- is traceable to an Epic;
- is traceable to confirmed discovery;
- does not encode architecture;
- is not too broad to define acceptance criteria;
- is not artificially split by technical layer.

## When Not to Use User Stories

Do not force user-story form for:

- regulatory requirements;
- system-wide NFRs;
- audit requirements;
- retention policies;
- platform constraints;
- cross-cutting business rules.

Keep these in their proper PRD sections and link them to affected Epics/stories.

## Coverage Analysis

Verify:

- Every MVP Must-Have maps to at least one Epic.
- Every critical user journey maps to one or more stories.
- Every story contributes to a Product Goal or confirmed requirement.
- No Future/Out-of-Scope item appears as an MVP story.

## Story Slicing

Prefer slices based on:

- user outcome;
- journey stage;
- business state;
- distinct role;
- distinct business rule set.

Do not slice by:

- database/API/UI;
- service/repository/controller;
- infrastructure component.

## Output Contribution to PRD.md

Populate/refine:

- Epics
- User Stories
- Traceability references
- Epic and story priorities

## Completion Check

Pass when:

1. MVP behaviour is fully represented.
2. Epics are product-oriented.
3. Stories are vertical and user/business oriented.
4. Stories are neither duplicates nor technical tasks.
5. Scope leakage is absent.
