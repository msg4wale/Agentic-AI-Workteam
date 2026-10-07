---
name: requirements-acceptance-criteria
description: Refine functional requirements and business rules and define testable acceptance criteria, validations, permissions, states, and exception behavior without specifying implementation.
---

# Requirements & Acceptance Criteria

## Purpose

Turn product behaviour into precise, observable acceptance conditions.

This skill elaborates confirmed requirements. It must not create new business policy.

## Functional Requirements

Preserve inherited `FR-xxx` identifiers.

Refine wording only when meaning remains unchanged.

Each FR should identify:

- actor or scope;
- required behaviour;
- condition;
- expected outcome.

If decomposition produces a more specific child requirement, make traceability explicit rather than silently replacing the source requirement.

## Business Rules

Preserve `BR-xxx`.

For each affected story identify relevant:

- eligibility rules;
- permissions;
- ownership;
- approvals;
- validation rules;
- thresholds;
- state transitions;
- deadlines;
- prohibited actions.

If a necessary rule is absent from discovery, flag it as a discovery/product decision gap.

## Acceptance Criteria

Use IDs:

`AC-001`, `AC-002`, ...

Acceptance criteria must be:

- observable;
- testable;
- unambiguous;
- product/business focused;
- traceable to a User Story or requirement.

## Given / When / Then

Use where useful:

```text
Given [precondition]
And [additional condition]
When [actor/action/event]
Then [observable product outcome]
And [additional observable outcome]
```

Do not force Gherkin if a concise declarative criterion is clearer.

## Include Relevant Negative Conditions

For important behaviours include cases such as:

- invalid input;
- missing required information;
- unauthorized action;
- invalid state;
- duplicate action;
- failed dependency;
- abandoned process;
- rejected approval.

Use confirmed `EC-xxx` requirements when available.

## State Behaviour

Where workflow state matters, make product states and transitions explicit.

Example:

```text
Draft -> Submitted -> Approved
                   -> Rejected
```

This describes product behaviour, not implementation.

Do not specify database enums, state machines, queues, or code design.

## Business Data Requirements

Identify only product-visible data requirements:

- required business information;
- information users must see;
- editable vs read-only information;
- retention/sensitivity constraints.

Do not define database schema.

## Output Contribution to PRD.md

Populate/refine:

- Functional Requirements
- Business Rules
- Roles and Permissions
- Business Data Requirements
- User Story Acceptance Criteria
- Edge/Exception Behaviour

## Completion Check

Pass when:

1. MVP behaviour is testable.
2. Acceptance criteria reflect source requirements.
3. Critical business rules are linked.
4. Permissions/state conditions are explicit.
5. Negative outcomes are represented where material.
6. No implementation detail appears.
