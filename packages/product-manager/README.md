# Product Manager Agent Package

This package contains the draft Product Manager stage for the agentic software-development workflow.

## Dependency

This design assumes the shared Idea Discovery package is already installed and provides:

```text
.github/skills/idea-validation/SKILL.md
```

The Product Manager reuses that skill as its input-readiness gate rather than duplicating discovery validation.

## Structure

```text
.github/
├── agents/
│   └── product-manager.agent.md
└── skills/
    ├── product-framing-synthesis/
    │   └── SKILL.md
    ├── epic-user-story-design/
    │   └── SKILL.md
    ├── requirements-acceptance-criteria/
    │   └── SKILL.md
    ├── prioritization-release-planning/
    │   └── SKILL.md
    ├── product-quality-metrics/
    │   └── SKILL.md
    └── prd-validation/
        └── SKILL.md
```

## End-to-End Product Manager Workflow

```text
idea.md
   |
   v
Idea Validation (shared discovery skill)
   |
   +-- Not Ready --> Idea Discovery
   |
   v
Product Framing & Scope Synthesis
   |
   v
Epic & User Story Design
   |
   v
Requirements & Acceptance Criteria
   |
   v
Prioritization & Release Planning
   |
   v
Product Quality & Metrics
   |
   v
PRD Validation
   |
   v
PRD.md
   |
   v
Solution Architect
```

## Design Principle

The Product Manager Agent owns product definition and orchestration.

Skills contain reusable product-management methods.

The Product Manager does not design the technical solution and does not silently repair missing discovery information.
