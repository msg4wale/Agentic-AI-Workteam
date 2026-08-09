# Idea Discovery Agent Package

This package contains a decomposed VS Code Custom Agent for product idea discovery.

## Structure

```text
.github/
├── agents/
│   └── idea-discovery.agent.md
└── skills/
    ├── problem-outcome-discovery/
    │   └── SKILL.md
    ├── stakeholder-user-discovery/
    │   └── SKILL.md
    ├── journey-requirements-discovery/
    │   └── SKILL.md
    ├── quality-edge-case-discovery/
    │   └── SKILL.md
    ├── scope-risk-discovery/
    │   └── SKILL.md
    └── idea-validation/
        └── SKILL.md
```

## Installation

Copy the `.github` directory into the root of your VS Code project/workspace.

VS Code recognizes workspace custom agents from `.github/agents` and project Agent Skills from `.github/skills`.

## Workflow

```text
Context Intake
  -> Problem & Outcome Discovery
  -> Stakeholder & User Discovery
  -> Journey & Requirements Discovery
  -> Quality & Edge-Case Discovery
  -> Scope, Constraint & Risk Discovery
  -> Idea Validation
  -> idea.md
  -> Product Management
```

The agent controls orchestration and the skills provide reusable discovery methods.
