---
name: journey-requirements-discovery
description: Discover current and target user journeys, core features, business capabilities, business rules, data needs, external integrations, and functional requirements. Use after actors are understood or whenever product behavior is incomplete.
---

# Journey & Requirements Discovery

## Purpose

Translate the confirmed problem, outcomes, and actors into complete business behaviour without designing implementation.

## Current Journey

Where a process already exists, capture:

- Trigger
- Actor
- Preconditions
- Steps
- Decisions
- Handoffs
- Tools/systems used
- Pain points
- Workarounds
- Completion condition
- Exceptions

## Target Journey

For every materially different user role, walk from trigger to completion.

Capture:

- Entry point
- Actor
- Preconditions
- Major actions
- Business decisions
- Approvals
- Handoffs
- Notifications
- Alternate paths
- Cancellation/abandonment
- Completion
- Return/repeat use

Do not assume registration, login, profiles, notifications, or logout.

## Core Features

For every stakeholder-confirmed feature capture:

- `FEAT-xxx`
- Name
- Description
- User served
- Problem addressed
- Business value
- Stakeholder-assigned priority
- Related journey

Do not add common features by convention.

## Business Capabilities

For every feature, discover required actions such as:

- Create
- View
- Edit
- Delete
- Submit
- Approve
- Reject
- Cancel
- Assign
- Search
- Filter
- Save
- Share
- Export
- Import
- Schedule
- Notify
- Escalate

## Business Rules

Use `BR-xxx`.

Discover:

- Who may perform an action?
- Under what conditions?
- What validations apply?
- What approvals are required?
- What states exist?
- What transitions are permitted?
- What actions are prohibited?
- What thresholds or deadlines apply?
- What happens when a rule is violated?

Business rules must be explicit enough that a Product Manager does not need to infer them.

## Business Data Needs

Capture business-level information requirements only:

- Important records/entities
- Information entered by users
- Information displayed to users
- Information updated
- Sensitive/regulatory information
- Known source of record
- Retention needs
- Import/export needs

Do not design schemas, tables, fields, indexes, databases, or storage technology.

## External Systems and Integrations

Identify required dependencies such as:

- Identity providers
- Payment providers
- ERP/CRM
- Email/SMS
- Messaging
- Government systems
- Partner platforms
- Existing internal systems
- Data feeds

Capture:

- Business purpose
- Information or outcome exchanged
- Direction of business dependency
- Known constraint
- What the business expects if the dependency is unavailable

Do not design APIs or protocols.

## Functional Requirements

Use `FR-xxx`.

Convert confirmed journeys, features, capabilities, and rules into testable business requirements.

Each FR should identify:

- Actor/subject
- Required capability/behaviour
- Relevant condition
- Expected business outcome

Example:

> FR-012: An approver must be able to reject a submitted request and provide a rejection reason before the request is returned to the requester.

Avoid implementation wording.

## Traceability

Where useful, relate:

`Problem -> Persona -> Journey -> Feature -> Business Rule -> Functional Requirement`

Do not create traceability merely for decoration. Use it to expose orphan requirements or features.

## Output Contribution to idea.md

Populate or refine:

- User Journeys
- Core Features
- Business Rules
- Roles and Permissions
- Business Data Needs
- External Systems and Integrations
- Functional Requirements

## Completion Check

This skill is complete when:

1. Core journeys are end-to-end.
2. Features map to a confirmed problem or outcome.
3. Critical business rules are explicit.
4. Business data needs are understood.
5. Required integrations are identified.
6. Functional requirements describe expected business behaviour without implementation detail.
