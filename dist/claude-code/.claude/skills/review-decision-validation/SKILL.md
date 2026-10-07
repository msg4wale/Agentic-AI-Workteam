---
name: review-decision-validation
description: Normalize review findings, verify severity and evidence, remove duplicate or subjective comments, ensure blockers are actionable, and produce a verdict consistent with the actual review findings.
---

# Review Decision Validation

## Purpose

Ensure the final review is fair, precise, actionable, and internally consistent.

## Normalize Findings

For each finding confirm:

- unique issue;
- correct severity;
- concrete location;
- factual description;
- material impact;
- evidence;
- required outcome.

Merge duplicate findings.

## Remove Weak Comments

Remove or downgrade comments based only on:

- personal style preference;
- hypothetical issue with no plausible path;
- unrelated existing code;
- speculative future requirements;
- arbitrary abstraction preference.

## Severity Check

### P0/P1

Must reflect blocking critical/high risk.

### P2

Material but typically non-catastrophic.

Whether P2 blocks depends on correctness/risk context.

### P3/Suggestion

Normally non-blocking.

Do not mechanically block all P2 findings if the issue is genuinely safe to defer, but document the rationale.

## Verdict Consistency

Use:

### APPROVE
No blocking finding.

### APPROVE WITH NON-BLOCKING COMMENTS
Only genuinely non-blocking findings/suggestions.

### CHANGES REQUIRED
At least one implementation defect must be corrected.

### BLOCKED — UPSTREAM DECISION
Correctness cannot be determined due to product/architecture/task conflict.

### BLOCKED — INSUFFICIENT REVIEW CONTEXT
Required review input is missing.

## Actionability Test

A developer should know what outcome resolves every blocking finding.

Do not prescribe exact code unless the defect can only be safely fixed one way.

## Final Quality Check

The final review should:

- lead with important findings;
- avoid praise filler;
- avoid excessive narration;
- distinguish evidence from inference;
- state verification reviewed/run;
- state acceptance coverage;
- end with explicit verdict.

## Completion Check

Return the final verdict only after findings and severity are consistent.
