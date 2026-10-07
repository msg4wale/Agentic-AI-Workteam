---
name: risk-based-test-design
description: Derive prioritized functional, negative, integration, data, security-behaviour, NFR, and regression scenarios from product requirements, acceptance criteria, edge cases, architecture concerns, and change risk.
---

# Risk-Based Test Design

## Purpose

Spend QA effort where failure would matter most.

## Inputs

Use:

- User Stories
- Product Acceptance Criteria
- FR / BR
- EC
- NFR
- ENG-AC
- QA tasks
- TDD verification concerns
- implementation change surface

## Risk Factors

Assess:

- business impact;
- user frequency;
- data sensitivity;
- financial impact;
- security exposure;
- integration complexity;
- state complexity;
- concurrency;
- recent code change;
- historical defect-proneness if known;
- irreversibility;
- operational impact.

Use High / Medium / Low unless a project standard exists.

## Test Design Techniques

Use selectively:

- equivalence partitioning;
- boundary-value analysis;
- decision tables;
- state-transition testing;
- pairwise/combinatorial testing;
- error guessing;
- use-case/scenario testing;
- contract testing;
- exploratory testing.

Do not apply every technique mechanically.

## Scenario Categories

Use relevant:

- `TC-FUNC`
- `TC-NEG`
- `TC-INT`
- `TC-DATA`
- `TC-SEC`
- `TC-PERF`
- `TC-ACC`
- `TC-REL`
- `TC-REG`

## Test Scenario Standard

Each material scenario should define:

- source requirement;
- risk;
- preconditions;
- input/action;
- expected result;
- evidence mechanism;
- automation suitability.

## Prioritization

Execute in order of risk and dependency.

A useful pattern:

1. smoke / basic deployability;
2. critical Must-Have journeys;
3. critical authorization/data rules;
4. high-risk negative/integration cases;
5. remaining functional scope;
6. applicable NFR;
7. regression.

## Completion Check

Pass when all high-risk requirements have an explicit verification strategy and lower-risk coverage is proportionate.
