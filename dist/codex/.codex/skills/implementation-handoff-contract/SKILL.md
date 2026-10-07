---
name: implementation-handoff-contract
description: The output contract for the Software Engineer's PR-ready handoff — the completion structure (implemented changes, changed files, verification, acceptance coverage, deviations, review focus) and the blocked structure. Load when producing the implementation handoff.
---

# Implementation Handoff Contract

At completion, return a concise handoff using this structure. Do not create an `Implementation-Report.md`
file unless explicitly requested.

```markdown
## Implementation Result

**Task:** BE-002 — [Title]
**Status:** READY FOR CODE REVIEW

### Execution Model
- Subagents used: [Yes/No]
- Parallel analysis performed: [areas]
- Parallel implementation performed: [Yes/No; ownership boundaries]
- Integration checkpoint: [if applicable]

### Implemented
- [Concise change]
- [Concise change]

### Changed Files
- `path/file.ext` — purpose
- `path/file.ext` — purpose

### Verification
| Check | Result |
|---|---|
| `command or check` | PASS |
| `command or check` | PASS |

### Acceptance Coverage
- ENG-AC-001 — PASS — [evidence]
- ENG-AC-002 — PASS — [evidence]

### Deviations / Decisions
- None

### Known Issues / Follow-Ups
- None

### Review Focus
- [Area reviewers should pay particular attention to]
```

If blocked, replace the completion structure with:

```markdown
## Implementation Blocked

**Task:** ...
**Status:** BLOCKED — [TYPE]

### Blocker
...

### Source Conflict / Missing Decision
...

### Required Owner
Product Manager | Solution Architect | Engineering Lead | External

### Required Resolution
...
```

The handoff must be suitable as the basis of a PR description: what changed, why, task/source references,
verification performed, deviations, remaining issues, and review focus. Do not claim a PR was created
unless the environment/tooling actually created one.
