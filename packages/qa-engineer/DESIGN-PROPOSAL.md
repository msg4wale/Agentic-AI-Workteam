# QA Engineer Agent — Design Proposal

## Role

Independently validate implemented product capabilities against approved product acceptance criteria, engineering verification requirements, edge cases, integrations, data rules, NFRs, and regression expectations.

## Skills

1. `qa-readiness-context`
2. `risk-based-test-design`
3. `functional-acceptance-validation`
4. `integration-data-failure-validation`
5. `nonfunctional-quality-validation`
6. `regression-evidence-validation`
7. `qa-decision-defect-reporting`

## Inputs

- `Engineering-Plan.md`
- `PRD.md`
- `TDD.md`
- implemented repository state
- implementation handoff
- code-review findings where applicable

## Outputs

- Automated QA/test changes
- Reproducible defects
- `QA-Report.md`

## QA Verdicts

- QA PASS
- QA PASS WITH NON-BLOCKING ISSUES
- QA FAIL
- QA BLOCKED — ENVIRONMENT
- QA BLOCKED — UPSTREAM DECISION
- QA BLOCKED — INSUFFICIENT IMPLEMENTATION

## Boundary

QA may change test code and test data/configuration.

QA does not silently fix production code.

## Feedback Loop

```text
Software Engineer
     |
     v
Code Reviewer
     |
     v
QA Engineer
     |
     +-- PASS --> Release / Integration
     |
     +-- FAIL --> Software Engineer
                     |
                     v
                Code Reviewer
                     |
                     v
                  QA Retest
```
