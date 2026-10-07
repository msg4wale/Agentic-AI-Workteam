---
name: system-component-design
description: Define system context, boundaries, architecture style, major components, responsibilities, dependencies, interaction patterns, runtime flows, and technology allocation from validated architecture drivers.
---

# System & Component Design

## Purpose

Turn architecture drivers into a coherent system structure.

The component model should be detailed enough that Engineering can identify implementation boundaries without the Architect writing engineering tasks.

## System Context

Identify:

- human actors;
- external systems;
- system under design;
- trust boundaries;
- network/system boundaries;
- inbound/outbound relationships.

Use Mermaid or other Markdown-compatible diagrams when useful.

## Architecture Style

State and justify the selected architecture style.

Examples include:

- modular monolith;
- layered application;
- hexagonal/ports-and-adapters;
- service-oriented;
- microservices;
- event-driven;
- serverless;
- hybrid.

Do not choose a pattern merely because it is fashionable.

## Component Identification

Use IDs:

`COMP-001`, `COMP-002`, ...

A component should have a coherent technical responsibility.

For each capture:

- Purpose
- Responsibilities
- Owned data/state
- Exposed interfaces
- Dependencies
- Relevant requirements
- Security considerations
- Availability/scaling concerns
- Technology, if architecture-significant

## Responsibility Rules

A component should have:

- clear ownership;
- minimal overlap;
- explicit input/output;
- justified existence.

Avoid components that are only vague labels such as:

- "Business Logic"
- "Utility Service"
- "Manager"
- "Processing Module"

without concrete responsibilities.

## Product-to-Component Coverage

Verify every material:

- Epic
- Must-Have feature
- FR
- BR
- NFR
- external integration

has a technical realization path.

## Interaction Patterns

Define when relevant:

- request/response;
- asynchronous messaging;
- scheduled/background processing;
- publish/subscribe;
- batch processing;
- streaming.

For each pattern explain why it is appropriate.

Do not introduce async processing without a latency, decoupling, workload, reliability, or integration reason.

## Runtime Flows

Document architecture-significant flows such as:

- authentication/login;
- primary transactional journey;
- approval workflow;
- payment;
- notification;
- ingestion/import;
- scheduled processing;
- reporting.

For each capture:

- trigger;
- components;
- ordered interaction;
- data/state changes;
- failure path.

## Cross-Cutting Concerns

Identify shared capabilities such as:

- identity;
- audit;
- notifications;
- configuration;
- feature flags;
- observability;
- file/object storage.

Avoid turning every cross-cutting concern into a separate service.

## Technology Allocation

Map selected technologies to components where relevant.

Example:

```text
COMP-001 Web Application -> React
COMP-002 Application API -> FastAPI
COMP-003 Primary Store -> PostgreSQL
```

Only after technology choices are justified.

## Output Contribution to TDD.md

Populate/refine:

- System Context
- Architecture Overview
- Component Design
- Key Runtime Flows
- Technology Stack

## Completion Check

Pass when:

1. System boundaries are clear.
2. Components have non-overlapping responsibilities.
3. Critical requirements map to components.
4. Interaction patterns are justified.
5. Key workflows can be traced end-to-end.
6. No unjustified subsystem remains.
