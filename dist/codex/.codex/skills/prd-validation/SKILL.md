---
name: prd-validation
description: Validate PRD.md for completeness, traceability, testability, scope integrity, assumption visibility, architecture neutrality, and readiness for Solution Architecture.
---

# PRD Validation

## Purpose

Determine whether `PRD.md` is sufficiently complete and precise for a Solution Architect to design the technical solution without inventing product behaviour.

This skill validates. It does not fix missing stakeholder decisions by assumption.

## Validation Classifications

Use:

- Pass
- Non-Blocking Gap
- Architecture-Blocking Gap
- Contradiction
- Unvalidated Assumption
- Scope Leakage
- Requirement Ambiguity
- Untestable Acceptance Criterion
- Traceability Gap
- Implementation Leakage

## Validate Product Context

Confirm:

- Problem Statement aligns with `idea.md`
- Vision aligns with `idea.md`
- Product Goals are outcome-oriented
- Non-Goals are explicit
- Personas are consistent
- Value proposition is supported

## Validate Scope

Confirm:

- Must/Should/Could/Won't are internally consistent
- MVP Must-Haves are complete
- Out of Scope is explicit
- Future Enhancements remain future
- No acceptance criterion depends on excluded scope
- No hidden feature appears inside a requirement

## Validate User Journeys

Confirm:

- Primary journeys are end-to-end
- Actors are explicit
- Preconditions are clear
- Alternate/exception paths exist where material
- Completion states are clear

## Validate Epics and Stories

Confirm:

- every MVP capability maps to an Epic;
- Epics map to Product Goals;
- stories are product-oriented;
- stories are not technical tasks;
- duplicate stories are removed;
- orphan stories are explained.

## Validate Requirements

Confirm:

- FRs are specific;
- BRs are explicit;
- permissions are explicit;
- business data needs are sufficient;
- external dependencies are defined;
- NFRs are measurable where targets exist;
- edge cases include expected product behaviour.

## Validate Acceptance Criteria

Acceptance criteria must be:

- observable;
- testable;
- non-contradictory;
- implementation-neutral;
- sufficiently complete for QA interpretation.

Flag acceptance criteria like:

> System uses Redis for caching.

as implementation leakage.

## Validate Traceability

Where applicable check:

```text
Problem
 -> Product Goal
 -> Persona/Journey
 -> Epic
 -> User Story
 -> FR/BR
 -> Acceptance Criteria
 -> Metric
```

Flag:

- orphan features;
- orphan stories;
- requirements without product rationale;
- goals with no measurable outcome;
- Must-Haves with no acceptance definition.

## Validate Assumptions and Decisions

Confirm:

- assumptions remain labelled;
- pending decisions are visible;
- blocking decisions are not hidden in Notes;
- stakeholder-approved decisions are distinguishable from PM proposals.

## Validate Architecture Neutrality

Flag:

- database design;
- API contracts;
- service decomposition;
- framework selection;
- deployment topology;
- cloud resource design;
- source code;
- queues/caches;
- implementation task lists.

Explicit stakeholder technology constraints may remain in Constraints but must not expand into design.

## Architecture-Blocking Topics

Treat unresolved material issues as blocking when they affect:

- core workflow;
- MVP boundary;
- permissions;
- business rules;
- data requirements;
- mandatory integrations;
- compliance;
- critical NFR target;
- critical failure behaviour.

## Result

Return exactly one readiness state:

### `ARCHITECTURE READY`

No material unresolved product issue.

### `ARCHITECTURE READY WITH NON-BLOCKING OPEN ITEMS`

Remaining issues are documented and do not require the architect to invent product behaviour.

### `NOT ARCHITECTURE READY`

At least one blocking gap, contradiction, assumption, or ambiguous requirement remains.

For every failure report:

- issue;
- classification;
- affected PRD section;
- why it matters;
- skill to revisit;
- stakeholder/product decision needed.

## Completion Check

Validation passes only when:

1. Product intent remains faithful to `idea.md`.
2. MVP scope is coherent.
3. Requirements are testable.
4. Acceptance criteria are usable by QA.
5. Traceability is sufficient.
6. Assumptions/open decisions are visible.
7. No architecture or implementation leakage remains.
8. The architect can proceed without inventing product behaviour.
