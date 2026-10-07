---
name: data-interface-integration-design
description: Define logical data architecture, persistence, consistency, transactions, API/interface contracts, external integrations, events, migration, retention, and failure semantics.
---

# Data, Interface & Integration Design

## Purpose

Define how information is owned, persisted, exchanged, validated, and kept consistent across the solution.

## Data Ownership

Identify which component/system is authoritative for each major business record.

Avoid multiple writers without a clear consistency model.

## Logical Data Model

Use:

`DATA-xxx`

Capture important entities and relationships.

For architecture-significant entities identify:

- purpose;
- owner;
- identifier;
- key attributes where behaviour depends on them;
- relationships;
- lifecycle/state;
- sensitivity;
- retention;
- uniqueness/business constraints.

Do not generate ORM classes.

## Persistence Strategy

For each persistent concern define:

- persistence technology/category;
- why it fits the access pattern;
- durability requirement;
- expected workload;
- backup implications.

Examples:

- relational database;
- object storage;
- search index;
- document store;
- key/value store.

Do not create multiple persistence technologies without need.

## Transactions and Consistency

Define:

- transaction boundary;
- atomic operations;
- eventual vs strong consistency;
- concurrent update behaviour;
- optimistic/pessimistic concurrency where important;
- idempotency requirement.

Tie choices to PRD edge cases and business rules.

## API / Interface Contracts

Use:

`API-xxx`

For each material interface capture as relevant:

- provider;
- consumer;
- purpose;
- interaction type;
- logical operation/endpoint;
- method if HTTP;
- request structure;
- response structure;
- validation;
- authentication/authorization;
- error semantics;
- pagination/filtering;
- idempotency;
- versioning;
- related requirements.

Contracts should be concrete enough for planning but need not be full OpenAPI documents.

## Error Contract

Avoid generic:

> Return an error.

Define architecture-level categories such as:

- validation failure;
- unauthorized;
- forbidden;
- not found;
- conflict;
- rate limited;
- dependency unavailable;
- timeout;
- internal failure.

Do not expose sensitive internal detail.

## Integration Design

Use:

`INT-xxx`

For external systems capture:

- business purpose;
- owner;
- protocol/transport;
- authentication;
- direction;
- payload/data;
- latency expectation;
- timeout;
- retry policy;
- idempotency;
- availability dependency;
- failure/degraded behaviour;
- quota/rate limit where known;
- reconciliation where needed.

## Events / Messaging

Use only when justified.

Use:

`EVT-xxx`

Capture:

- producer;
- consumer(s);
- trigger;
- semantic event name;
- contract;
- delivery semantics;
- ordering requirement;
- idempotency;
- retention;
- failure handling;
- schema/version evolution.

Do not use events merely to make the architecture "decoupled."

## Migration / Import / Export

Where applicable define:

- source;
- destination;
- mapping;
- validation;
- reconciliation;
- rollback;
- cutover;
- data quality expectations.

## Retention / Deletion

Translate PRD policies into technical behaviour:

- archive;
- deletion;
- legal hold;
- anonymization/pseudonymization where required;
- backup retention interaction.

Do not invent retention periods.

## Output Contribution to TDD.md

Populate/refine:

- Data Architecture
- API and Interface Design
- Integration Architecture
- Event / Messaging Design
- relevant Runtime Flows
- relevant Technical Risks

## Completion Check

Pass when:

1. Major data has one clear owner.
2. Transaction/consistency decisions are explicit.
3. Critical interfaces are implementation-plannable.
4. External integration failure behaviour is defined.
5. Sensitive data treatment is explicit.
6. No unjustified data/integration technology is introduced.
