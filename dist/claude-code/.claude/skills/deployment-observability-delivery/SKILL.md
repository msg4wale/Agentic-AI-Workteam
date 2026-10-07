---
name: deployment-observability-delivery
description: Define runtime topology, environments, network placement, configuration, scaling, CI/CD architecture, rollout/rollback, schema changes, logs, metrics, traces, health signals, alerting, and operational observability.
---

# Deployment, Observability & Delivery

## Purpose

Define how the designed system runs, is promoted safely, and can be understood in production.

## Deployment Architecture

Use:

`DEP-xxx`

Define:

- runtime platform;
- component placement;
- public/private exposure;
- network boundaries;
- region/location;
- availability zones where needed;
- scaling model;
- stateful/stateless placement;
- infrastructure dependencies.

Tie choices to NFRs and constraints.

## Environments

Define required environments, for example:

- local/development;
- test;
- integration;
- staging/UAT;
- production.

Only include environments that serve a clear delivery purpose.

Define:

- isolation;
- data policy;
- configuration separation;
- external integration strategy.

## Configuration

Define:

- environment-specific configuration;
- secret separation;
- runtime configuration;
- feature flags where justified.

Do not put secrets in version control.

## Scaling

Define:

- scaling unit;
- horizontal/vertical approach;
- bottlenecks;
- state implications;
- workload triggers if known.

Do not overdesign beyond workload drivers.

## Delivery Architecture

At architecture level define:

- source-to-build expectations;
- automated verification gates;
- artifact immutability;
- environment promotion;
- deployment method;
- rollback;
- approval/compliance gates where required.

Do not create pipeline implementation tasks.

## Database / Schema Change Strategy

Define:

- backward-compatible migration expectations;
- order of application/database deployment where important;
- rollback limitations;
- data migration validation.

## Feature Rollout

Use when justified:

- feature flags;
- canary;
- blue/green;
- staged rollout.

Do not add advanced rollout mechanisms without a risk/availability reason.

## Observability

Use:

`OBS-xxx`

### Logging

Define:

- structured logs;
- correlation/request IDs;
- security redaction;
- important operational events.

### Metrics

Define technical metrics such as:

- request rate;
- error rate;
- latency;
- saturation;
- queue depth;
- dependency failures;
- job success/failure.

Tie business telemetry separately to PRD product analytics.

### Tracing

Use distributed tracing where multiple components/dependencies make it useful.

Do not require it reflexively for a simple monolith.

### Health / Readiness

Define signals used to distinguish:

- process alive;
- ready to receive traffic;
- critical dependency state.

### Alerting

Alert on actionable failure conditions tied to service objectives.

Avoid alerts on every log error.

### Dashboards

Define required operational views:

- availability;
- latency;
- errors;
- saturation;
- critical dependency status;
- scheduled/background workload health.

## Release / Rollback

Define:

- safe release expectations;
- rollback conditions;
- database compatibility constraints;
- config rollback;
- verification after deployment.

## Output Contribution to TDD.md

Populate/refine:

- Deployment Architecture
- Delivery and Release Architecture
- Observability and Operations
- Performance and Scalability
- relevant Verification Strategy
- Technical Risks

## Completion Check

Pass when:

1. Component runtime placement is clear.
2. Environment and network boundaries are explicit.
3. Release/rollback behaviour is designed.
4. Observability covers critical production failure modes.
5. Scaling matches expected workload.
6. Delivery complexity is proportionate.
