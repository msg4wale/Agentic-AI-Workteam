---
name: review-report-contract
description: The output contract for the Code Reviewer's verdict — the review structure (summary, findings with severity/location/evidence/required-change, verification, acceptance coverage, decision). Load when writing the review output.
---

# Final Review Output Contract

Use this structure. Do not create `Code-Review.md` unless explicitly requested.

```markdown
## Code Review

**Task:** BE-002 — [Title]
**Verdict:** CHANGES REQUIRED

### Summary

One concise paragraph on overall implementation quality and risk.

### Findings

#### [P1] Finding title

**Location:** `path/file.ext:123-145`

**Issue:** ...

**Why it matters:** ...

**Evidence:** FR-006, API-004, ENG-AC-002

**Required change:** ...

#### [P2] Finding title

...

### Verification Reviewed / Run

| Check | Evidence / Result |
|---|---|
| Existing implementation handoff | Reviewed |
| `pytest ...` | PASS |
| `npm run typecheck` | PASS |

### Acceptance Coverage

| Criterion | Status | Notes |
|---|---|---|
| ENG-AC-001 | PASS | ... |
| ENG-AC-002 | FAIL | Finding P1 |

### Non-Blocking Notes

- ...

### Upstream Issues

- None

### Review Decision

**CHANGES REQUIRED**

Resolve P1 findings before approval.
```

If there are no findings:

```markdown
## Code Review

**Task:** ...
**Verdict:** APPROVE

### Summary
...

### Verification Reviewed / Run
...

### Acceptance Coverage
...

### Review Decision

**APPROVE**
```
