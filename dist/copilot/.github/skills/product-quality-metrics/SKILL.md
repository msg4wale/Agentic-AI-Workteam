---
name: product-quality-metrics
description: Refine non-functional requirements, product success metrics, analytics measurement needs, compliance, operational expectations, and external dependencies without prescribing architecture or instrumentation implementation.
---

# Product Quality & Metrics

## Purpose

Ensure the PRD explains both how well the product must behave and how product success will be measured.

## Non-Functional Requirements

Preserve `NFR-xxx`.

Relevant categories may include:

- Performance
- Availability
- Reliability
- Security
- Privacy
- Compliance
- Accessibility
- Localization
- Offline/low-connectivity
- Auditability
- Retention
- Recovery expectation
- Supported platform/device
- Scale/volume expectations

Use measurable targets where present in discovery.

Do not invent technical SLOs.

## Product Success Metrics

Use IDs:

`MET-001`, `MET-002`, ...

For each metric capture:

- Related Product Goal
- Metric definition
- Baseline, if known
- Target
- Time horizon
- Measurement owner/source, if known

Do not invent missing targets.

## Analytics / Measurement Requirements

Describe what the product must make measurable.

Examples:

- number of completed submissions;
- abandonment rate by journey stage;
- average approval cycle time;
- conversion from trial to paid subscription.

Do not specify:

- analytics SDK;
- database schema;
- event bus;
- telemetry architecture.

## Metric Integrity

Check that:

- each important Product Goal has a meaningful success measure;
- vanity metrics do not substitute for outcomes;
- metrics can distinguish success from mere usage;
- metrics do not conflict with privacy/compliance constraints.

## External Dependencies

Carry forward product-level integration dependencies.

Capture:

- business purpose;
- criticality;
- expected user/product outcome if dependency is unavailable.

Do not design integration architecture.

## Operational Product Expectations

Where discovery supports them, capture:

- support model expectations;
- administrator needs;
- audit/reporting needs;
- business continuity expectations;
- rollout/adoption considerations;
- training/change-management dependencies.

Do not create operational processes unsupported by discovery.

## Output Contribution to PRD.md

Populate/refine:

- Success Measures
- Non-Functional Requirements
- Product Analytics and Measurement Requirements
- External Systems and Product Dependencies
- relevant Constraints
- relevant Risks

## Completion Check

Pass when:

1. Key goals have measures.
2. Critical NFRs are explicit.
3. Measurement needs are product-level and implementation-neutral.
4. External dependencies and expected behaviour are visible.
5. Compliance/privacy implications are not contradicted by analytics requirements.
