---
name: review-readiness-context
description: Establish review scope, source intent, changed files, acceptance criteria, architecture references, diff completeness, and available verification evidence before evaluating implementation quality.
---

# Review Readiness & Context

## Purpose

Ensure the reviewer knows what the change is supposed to do before judging how it was implemented.

## Establish Review Target

Identify:

- Task ID/title
- Branch/change set
- Changed files
- Related PR/implementation handoff if available

## Establish Source Intent

Read relevant:

- Engineering task
- User Story/Epic
- FR/BR/NFR/EC
- ENG-AC
- ADR/COMP/API/DATA/INT/SEC/REL/OBS

Do not read unrelated sections.

## Inspect Change Set

Use git/repository tools to identify:

- modified files;
- added/deleted files;
- staged/unstaged state;
- diff boundaries.

Confirm the reviewed change set is complete enough to assess.

## Verification Context

Collect available:

- Software Engineer handoff
- Test commands/results
- CI output if available in repository context
- Build/lint/type results

Treat claims as evidence to verify, not authority.

## Detect Context Blockers

Examples:

- no task/intent;
- diff not available;
- generated code without source change;
- PRD/TDD conflict;
- required dependency change omitted from review scope.

## Result

Return:

- `REVIEW READY`
- `REVIEW READY WITH NOTES`
- `REVIEW NOT READY`

For blockers specify exact missing context.

## Completion Check

Proceed only when intended behaviour and actual change set can be compared meaningfully.
