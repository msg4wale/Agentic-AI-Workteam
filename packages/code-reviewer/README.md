# Code Reviewer Agent Package

This package defines the independent Code Review stage of the agentic software-development workflow.

## Inputs

Typical inputs:

- TASK-ID from `Engineering-Plan.md`
- implementation diff / current branch
- `PRD.md`
- `TDD.md`
- Software Engineer implementation handoff
- repository tests and verification results

## Output

The reviewer does not create another planning artifact.

It returns a review verdict and evidence-based findings suitable for a Pull Request review.

## Structure

```text
.github/
├── agents/
│   └── code-reviewer.agent.md
└── skills/
    ├── review-readiness-context/
    │   └── SKILL.md
    ├── change-correctness-analysis/
    │   └── SKILL.md
    ├── requirement-architecture-compliance/
    │   └── SKILL.md
    ├── code-design-quality-review/
    │   └── SKILL.md
    ├── security-data-integrity-review/
    │   └── SKILL.md
    ├── test-verification-review/
    │   └── SKILL.md
    └── review-decision-validation/
        └── SKILL.md
```

## Workflow

```text
TASK-ID / DIFF
      |
      v
Review Readiness & Context
      |
      v
Change & Correctness Analysis
      |
      v
Requirement & Architecture Compliance
      |
      v
Code Design Quality Review
      |
      v
Security & Data Integrity Review
      |
      v
Test & Verification Review
      |
      v
Review Decision Validation
      |
      v
APPROVE
or
APPROVE WITH NON-BLOCKING COMMENTS
or
CHANGES REQUIRED
or
BLOCKED
```

## Independence

The reviewer intentionally has no `edit` tool in the draft agent.

That separation prevents the same agent from silently fixing its own review findings and preserves an independent-review boundary.

If you later want an "apply review fixes" workflow, use the Software Engineer Agent after the reviewer returns `CHANGES REQUIRED`.


## Code Design Quality Gate

The reviewer now has a mandatory dedicated review stage for:

- Clean code
- Cohesion and coupling
- Modularity
- Separation of concerns
- Testability
- Dangerous duplication
- Dependency direction
- Complexity
- Abstraction quality
- Interface quality
- Changeability

SOLID and DRY are used as diagnostic principles, not rigid pass/fail rules.
