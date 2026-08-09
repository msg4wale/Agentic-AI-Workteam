# Software Engineer Agent Package

This package defines the implementation stage of the agentic software-development workflow.

## Inputs

The agent implements one task from:

- `Engineering-Plan.md`

It uses:

- `PRD.md` for product behaviour
- `TDD.md` for architecture
- the repository for current implementation context

## Output

The Software Engineer does not create another planning document.

Its outputs are:

1. repository code/configuration/test changes required by the assigned task; and
2. a concise PR-ready implementation handoff in chat.

## Structure

```text
.github/
├── agents/
│   └── software-engineer.agent.md
└── skills/
    ├── task-readiness-analysis/
    │   └── SKILL.md
    ├── repository-context-analysis/
    │   └── SKILL.md
    ├── subagent-parallel-execution/
    │   └── SKILL.md
    ├── focused-implementation/
    │   └── SKILL.md
    ├── testing-verification/
    │   └── SKILL.md
    ├── code-quality-security-review/
    │   └── SKILL.md
    └── implementation-handoff-validation/
        └── SKILL.md
```

## Workflow

```text
TASK-ID
  |
  v
Task Readiness
  |
  +-- Product issue ------> Product Manager
  +-- Architecture issue -> Solution Architect
  +-- Task issue ---------> Engineering Lead
  |
  v
Repository Context Analysis
  |
  v
Focused Implementation
  |
  v
Testing & Verification
  |
  v
Code Quality & Security Self-Review
  |
  v
Implementation Handoff Validation
  |
  v
Repository Change + PR-Ready Handoff
  |
  v
Code Review / QA
```

## Task Execution Principle

One session should normally implement one engineering task.

Example:

```text
Implement BE-002 from Engineering-Plan.md
```

The agent locates the task, follows its source references, inspects the repository, implements it, runs verification, and reports readiness.

## VS Code Tools

The custom agent grants search, edit, and terminal capabilities because implementation requires repository inspection, file changes, builds, and tests.

Review VS Code's tool approvals/permissions for your environment before enabling highly autonomous execution.


## Subagent and Parallel Execution Model

For non-trivial tasks, the Software Engineer evaluates safe subagent delegation.

Default:
- parallel repository exploration;
- parallel requirements/contract analysis;
- parallel test/risk analysis;
- consolidated primary implementation;
- parallel verification.

Parallel code editing is allowed only when ownership is non-overlapping, contracts are fixed, and integration is deterministic.

The primary Software Engineer remains accountable for the final task.
