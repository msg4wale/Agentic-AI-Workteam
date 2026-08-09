---
name: functional-acceptance-validation
description: Execute and evaluate functional product validation against User Stories, product acceptance criteria, engineering acceptance criteria, functional requirements, business rules, roles, validations, state transitions, and edge cases.
---

# Functional & Acceptance Validation

## Purpose

Determine whether the product capability behaves as specified from the user/business perspective.

## Acceptance-First

Start from acceptance criteria, not code structure.

For each in-scope criterion define:

- test/evidence;
- actual outcome;
- status.

## Main Flow

Validate the complete primary journey, not only isolated functions.

## Business Rules

Test:

- thresholds;
- approvals;
- eligibility;
- ownership;
- deadlines;
- validations;
- prohibited actions;
- state restrictions.

## Roles / Permissions

Validate:

- authorized actor;
- unauthorized actor;
- ownership boundaries;
- admin/approver distinctions;
- changed role where relevant.

## Validation

Test relevant:

- required fields;
- allowed values;
- lengths/ranges;
- cross-field rules;
- duplicates;
- malformed input.

## State Transition

Verify:

- valid transition;
- invalid transition;
- repeated action;
- transition precondition;
- resulting user-visible state;
- required audit/notification.

## Negative / Edge Flows

Use source `EC-xxx` plus risk-derived cases.

Do not invent desired behaviour; if expected result is missing, block that scenario and route upstream.

## Evidence

Evidence may include:

- automated test result;
- API response;
- UI observation;
- database-safe test query;
- log/audit record;
- screenshot/artifact if supported.

Do not rely solely on implementation code reading.

## Completion Check

Pass when every required acceptance criterion has an evidenced status.
