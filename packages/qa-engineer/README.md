# QA Engineer Agent Package

This package defines the independent QA stage of the agentic software-development workflow.

## Inputs

Typical inputs:

- QA task or implementation TASK-ID from `Engineering-Plan.md`
- `PRD.md`
- `TDD.md`
- implemented repository state
- Software Engineer implementation handoff
- Code Reviewer verdict/findings where available

## Outputs

1. QA/test automation changes where appropriate
2. Defect evidence
3. `QA-Report.md`

## Structure

```text
.github/
├── agents/
│   └── qa-engineer.agent.md
└── skills/
    ├── qa-readiness-context/
    │   └── SKILL.md
    ├── risk-based-test-design/
    │   └── SKILL.md
    ├── functional-acceptance-validation/
    │   └── SKILL.md
    ├── integration-data-failure-validation/
    │   └── SKILL.md
    ├── nonfunctional-quality-validation/
    │   └── SKILL.md
    ├── regression-evidence-validation/
    │   └── SKILL.md
    └── qa-decision-defect-reporting/
        └── SKILL.md
```

## Workflow

```text
TASK / CAPABILITY
      |
      v
QA Readiness & Context
      |
      v
Risk-Based Test Design
      |
      v
Functional & Acceptance Validation
      |
      v
Integration, Data & Failure Validation
      |
      v
Non-Functional Quality Validation
      |
      v
Regression & Evidence Validation
      |
      v
QA Decision & Defect Reporting
      |
      v
QA-Report.md
      |
      +-- PASS --> Release / Integration Gate
      |
      +-- FAIL --> Software Engineer
      |
      +-- BLOCKED --> Appropriate upstream owner
```

## Key Boundary

The QA Engineer may add/update automated tests and test fixtures.

It does not fix production code defects by default.

The distinction is:

- Code Reviewer: implementation/code quality and design correctness
- QA Engineer: observable product behaviour and quality validation

## VS Code Compatibility

The package uses the same custom-agent plus Agent-Skills structure as the other workflow stages. Current VS Code documentation supports custom `.agent.md` roles and on-demand Agent Skills for specialized workflows.
