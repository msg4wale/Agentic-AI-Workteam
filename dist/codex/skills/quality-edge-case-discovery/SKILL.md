---
name: quality-edge-case-discovery
description: Discover measurable non-functional requirements and expected business behavior for edge cases, failures, concurrency, abuse, and recovery. Use after core functional behavior is understood or whenever quality and exception behavior are incomplete.
---

# Quality & Edge-Case Discovery

## Purpose

Discover how well the product must behave and what users/business processes expect when the happy path fails.

Do not design technical mechanisms.

## Non-Functional Requirements

Use `NFR-xxx`.

Explore only relevant quality attributes:

- Performance
- Availability
- Usage volume/scalability expectation
- Security expectation
- Privacy
- Compliance
- Accessibility
- Localization
- Offline/low-connectivity support
- Reliability
- Auditability
- Retention
- Recovery expectation
- Supported platform/device expectations

## Make Vague Quality Language Measurable

If the stakeholder says:

> It should be fast.

Ask:

- Which actions are performance-critical?
- What response time is acceptable?

If they say:

> It must always be available.

Ask:

- Which business periods are critical?
- Is scheduled downtime acceptable?
- What availability target is required, if known?

Do not invent targets.

## What-If Technique

For each material workflow ask relevant "What if?" questions.

Examples:

- What if input is invalid?
- What if required information is missing?
- What if a user submits twice?
- What if connectivity drops?
- What if an external service is unavailable?
- What if a payment/transaction status is uncertain?
- What if two users act on the same item?
- What if a user's permissions change mid-process?
- What if approval is delayed or rejected?
- What if a notification cannot be delivered?
- What if a process is abandoned?
- What if only part of a transaction completes?
- What if data is stale or conflicting?
- What if a user attempts to bypass a business rule?
- What if a user behaves maliciously?

Do not ask every example mechanically. Select those relevant to the discovered product.

## Edge Case Requirements

Use `EC-xxx`.

For each material scenario capture:

- Trigger
- Expected user-visible behaviour
- Expected business behaviour
- Data/business consistency expectation
- Recovery/escalation expectation
- Whether manual intervention is acceptable
- Relevant actor/feature/journey

## Boundary With Technical Design

Do not design:

- Memory handling
- Threads
- Server topology
- Queues
- Retry algorithms
- Circuit breakers
- Infrastructure failover
- Database locking
- Cache strategy

A business requirement may specify the desired resulting behaviour, but implementation belongs to the TDD.

## Abuse and Adversarial Behaviour

Where relevant discover:

- Unauthorized action attempts
- Duplicate or fraudulent submissions
- Manipulation of workflow state
- Excessive/repetitive use
- Attempts to access another user's information
- Bypass of approval/business rules

Capture required business outcome, not cybersecurity implementation.

## Output Contribution to idea.md

Populate or refine:

- Non-Functional Requirements
- Edge Case Requirements
- relevant Business Rules
- relevant Risks

## Completion Check

This skill is complete when:

1. Relevant NFR domains have been considered.
2. Stakeholder-provided targets are measurable.
3. Important failure/exception paths have expected business behaviour.
4. Abuse/adversarial scenarios are considered where material.
5. No low-level solution design has been introduced.
