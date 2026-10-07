---
name: idea-validation
description: Validate a discovered product idea for completeness, consistency, traceability, scope discipline, and PRD readiness. Use as the final discovery gate and after material discovery changes.
---

# Idea Validation

## Purpose

Determine whether the accumulated discovery can be handed to Product Management without forcing the Product Manager to guess material requirements or repeat stakeholder discovery.

This skill validates. It does not invent missing content.

## Validation Method

Review the full discovery record and `idea.md` if present.

Classify each issue as:

- Pass
- Non-blocking Gap
- PRD-Blocking Gap
- Contradiction
- Unvalidated Assumption
- Scope Leakage
- Implementation Detail
- Traceability Gap

## Completeness Checklist

Verify:

### Problem and Value

- Problem clearly defined
- Affected user/business group identified
- Current approach understood
- Evidence/impact captured where available
- Desired user outcome defined
- Desired business outcome defined
- Vision and goals defined
- Business value/model captured where relevant

### Stakeholders and Users

- Sponsor/owner/decision maker known where relevant
- Primary user/beneficiary known
- Material secondary users known
- Personas sufficiently differentiated
- Goals/pain points/current workflows understood
- Permissions and ownership rules understood

### Journeys and Requirements

- Current journey captured where applicable
- Target journey complete
- Alternate/exception journeys considered
- Features map to business value
- Business rules explicit
- Business data needs understood
- Required integrations identified
- Functional requirements testable and implementation-neutral

### Quality and Edge Cases

- Relevant NFR categories considered
- Measurable targets captured where available
- Material edge cases identified
- Expected business behaviour defined
- Abuse/adversarial scenarios considered where relevant

### Scope and Viability

- Must-Have MVP scope explicit
- Should/Could/Won't categories captured where useful
- Out of Scope explicit
- Future Enhancements separated
- Constraints/dependencies captured
- Success metrics sufficiently defined
- Risks visible
- Assumptions separated from facts

## PRD-Blocking Topics

Normally classify these as blocking if unresolved:

- Core problem
- Primary user/beneficiary
- Desired business outcome
- Core user journey
- MVP Must-Have scope
- Critical business rules
- Material legal/regulatory constraints
- Material platform/organizational constraints
- Core success definition

A blocking topic can remain unresolved only if the stakeholder explicitly accepts the PRD limitation.

## Contradiction Check

Look for contradictions across:

- Personas
- Requirements
- Priorities
- Business rules
- MVP scope
- Constraints
- Metrics
- Assumptions

Do not reconcile silently.

Return the contradiction to the stakeholder through the parent agent.

## Assumption Check

Verify that:

- assumptions are labeled;
- assumptions are not presented as requirements;
- consequences of false assumptions are visible where material;
- validation needs are recorded.

## Scope Leakage Check

Identify:

- Future enhancements appearing in MVP
- Should/Could items expressed as mandatory FRs
- Features not tied to a problem/user/outcome
- Technical implementation presented as a business requirement

## Implementation Detail Check

Flag content such as:

- Database schema
- API design
- Cloud architecture
- Specific framework selection
- Queue design
- Cache design
- Source code
- Infrastructure topology

unless the stakeholder explicitly imposed a technology as a constraint. Even then, retain it as a constraint rather than expanding into design.

## Traceability Check

Where reasonable verify:

`Problem -> User -> Journey -> Feature -> Business Rule/FR -> MVP`

Flag orphan features and requirements.

## Validation Result

Return one of:

### `PRD READY`

Use only when no unresolved blocking issue remains.

### `PRD READY WITH NON-BLOCKING OPEN ITEMS`

Use when remaining items are explicitly non-blocking and documented.

### `NOT PRD READY`

Use when one or more blocking gaps, contradictions, or critical assumptions remain.

For every failure item report:

- Issue
- Classification
- Why it matters
- Which discovery skill should be revisited
- Question/decision needed from stakeholder

## Output Contribution to idea.md

Update/refine:

- Document Status
- PRD Readiness
- Open Questions
- Notes, where necessary

Do not add missing business content yourself.

## Completion Check

Validation is complete only when:

1. Every checklist domain has been reviewed.
2. Blocking and non-blocking issues are distinguished.
3. Contradictions are visible.
4. Assumptions are not disguised as facts.
5. Scope leakage is corrected.
6. Implementation details are removed or correctly classified as constraints.
7. A clear PRD-readiness result is returned.
