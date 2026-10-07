---
name: scope-risk-discovery
description: Discover constraints, dependencies, success metrics, MVP scope, explicit exclusions, future enhancements, risks, and assumptions. Use after core behavior is understood or whenever release boundaries and business viability remain unclear.
---

# Scope, Constraint & Risk Discovery

## Purpose

Turn an understood product concept into a bounded, measurable, decision-ready MVP.

## Constraints and Dependencies

Use `CON-xxx`.

Capture stakeholder-confirmed constraints including:

- Budget
- Timeline
- Mandatory launch date
- Platforms/devices
- Countries
- Languages
- Legal requirements
- Regulatory obligations
- Procurement constraints
- Organizational policies
- Mandatory technologies
- Existing systems that must remain
- Vendor constraints
- Contractual constraints
- Data residency
- Operational dependencies
- External dependencies

A technology preference becomes a constraint only when explicitly required.

Do not recommend technology.

## Success Metrics

For each metric capture where known:

- Metric
- Baseline
- Target
- Time horizon
- Measurement source
- Owner

Potential categories:

- Adoption
- Active users
- Revenue
- Cost reduction
- Time saved
- Error reduction
- Retention
- Conversion
- Satisfaction
- Transaction completion
- Process cycle time
- Service performance

Do not invent targets.

If a target is not known, record an Open Question or Pending Stakeholder Decision.

## MVP Scope

Use MoSCoW.

### Must Have

Without this capability, the MVP cannot achieve its core outcome.

### Should Have

Important but can be deferred.

### Could Have

Valuable and optional.

### Won't Have in This Release

Explicitly excluded.

For each item, use stakeholder priority.

Do not assign MoSCoW priority yourself.

Challenge an MVP that includes nearly every proposed feature.

## Scope Boundaries

Explicitly identify:

- MVP entry boundary
- MVP completion boundary
- Out-of-scope features
- Deferred user groups
- Deferred workflows
- Deferred integrations
- Deferred markets/countries
- Deferred channels/platforms

## Future Enhancements

Capture future ideas outside MVP.

Examples:

- AI-assisted capabilities
- Premium capabilities
- Advanced analytics
- Automation
- New integrations
- Additional markets
- Additional roles

Never mix these into MVP requirements.

## Risks

Use `RISK-xxx`.

Relevant categories include:

- Business
- Operational
- Adoption
- Legal/regulatory
- Dependency
- Data
- Delivery
- High-level technology

Capture where known:

- Description
- Impact
- Likelihood
- Business mitigation/response
- Owner

If a risk is identified through analysis rather than stated by the stakeholder, label it as agent-identified for stakeholder validation.

Do not present an invented mitigation as a decision.

## Assumptions

Use `ASM-xxx`.

For each assumption capture:

- Statement
- Why it matters
- Validation/evidence needed
- Owner
- Consequence if false, where material

Never convert an assumption into a confirmed requirement.

## Output Contribution to idea.md

Populate or refine:

- MVP Scope
- Out of Scope
- Constraints and Dependencies
- Risks
- Assumptions
- Success Metrics
- Future Enhancements
- relevant Open Questions

## Completion Check

This skill is complete when:

1. MVP Must-Haves are explicit.
2. Out-of-scope items are explicit.
3. Future scope is clearly separate.
4. Material constraints/dependencies are known.
5. Success is measurable enough for Product Management.
6. Material risks are visible.
7. Assumptions are clearly separated from facts.
