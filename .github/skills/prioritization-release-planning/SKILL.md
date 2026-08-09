---
name: prioritization-release-planning
description: Structure stakeholder-approved product priorities, MVP boundaries, release goals, product dependencies, sequencing constraints, and deferred scope without creating engineering estimates or sprint plans.
---

# Prioritization & Release Planning

## Purpose

Create a coherent product release boundary that Engineering can later plan against.

This is product sequencing, not engineering scheduling.

## MVP Release Goal

Define the outcome the MVP release must enable.

The release goal should answer:

- who receives value;
- what core outcome becomes possible;
- what success means at release level.

Do not write a list of features as the release goal.

## MoSCoW

Preserve stakeholder priorities:

- Must Have
- Should Have
- Could Have
- Won't Have in This Release

Do not upgrade priority without approval.

## Priority Consistency

Check for conflicts such as:

- a Must-Have story depending on a Could-Have capability;
- a Future feature required by an MVP acceptance criterion;
- an Out-of-Scope integration required by a Must-Have journey.

Surface conflicts.

## Epic and Story Priority

Assign product priority only when supported by:

- existing stakeholder prioritization;
- explicit Product Manager decision approved by the stakeholder;
- a logically necessary dependency.

If proposing a priority, label it `Proposed`.

## Product Dependencies

Capture dependencies that affect product sequencing:

- external system availability;
- business policy approval;
- regulatory approval;
- partner onboarding;
- source-data readiness;
- prerequisite product capability.

Do not define code/build dependencies.

## Product Sequencing

Where necessary describe:

```text
Capability A must be available before Capability B
```

because of a business/product dependency.

Do not create:

- sprint plans;
- story points;
- developer assignments;
- implementation dates unsupported by stakeholder commitments.

## Deferred Scope

Ensure deferred items appear in only the appropriate sections:

- Should/Could
- Won't Have
- Out of Scope
- Future Enhancements

## Output Contribution to PRD.md

Populate/refine:

- MVP Release Goal
- Product Scope
- Epic/story priority
- Dependencies and Sequencing
- Future Enhancements

## Completion Check

Pass when:

1. MVP boundary is internally coherent.
2. Priority conflicts are resolved or exposed.
3. Dependencies affecting product sequencing are visible.
4. No engineering estimate or sprint plan has been introduced.
