# Workteam Constitution

The durable, project-governing principles the entire Agentic AI Workteam is held to. It is the standing
**quality and specification bar** that every agent honours in addition to its stage instructions. Where a
stage instruction and this constitution appear to conflict on quality, the stricter interpretation wins.

This file is shipped as a sensible default and is **meant to be tailored per project** — adjust the
specifics (test thresholds, stacks, conventions) to your context, but keep a principle-per-line, testable
style. Agents load it on demand via the `constitution-governance` skill.

## 1. Specification is the source of truth
- Requirements (`PRD.md`), architecture (`TDD.md`), and the engineering plan govern implementation.
- Downstream never silently rewrites upstream intent; changes are routed to the owning stage and re-approved.
- Every change traces to an explicit, testable requirement or acceptance criterion — never to a guess.

## 2. Clean, readable code
- Prefer clear names, small cohesive units, and low coupling over cleverness.
- Match the surrounding code's idiom, structure, and conventions.
- No dead code, no commented-out blocks, no unexplained magic values.

## 3. Reuse before rebuild
- Reuse existing patterns, utilities, and libraries over introducing parallel implementations.
- The Plan Architect gate must clear duplication before implementation begins.

## 4. Quality is verified, not asserted
- Acceptance criteria are testable; each is validated with evidence.
- Tests cover happy paths and critical negative/edge paths; do not weaken tests to pass.
- "Done" means: acceptance met, tests green, review approved, QA passed — with evidence.

## 5. Reliability and safety
- Handle errors, boundaries, and partial failures deliberately; fail safe.
- Protect data integrity; migrations are reversible or explicitly guarded.

## 6. Security by default
- Least privilege everywhere; each agent uses only the tools its role needs.
- **Never commit plaintext secrets.** Credentials, tokens, and keys live in a secret manager or
  environment; artifacts reference secure retrieval, never embed the secret.
- Validate and sanitise untrusted input; never log sensitive data.

## 7. Reproducible environments and infrastructure
- Environments are provisioned via **Infrastructure as Code** — no undocumented manual changes.
- **Local platforms are open-source and IaC-deployable**; keep local/production parity high.
- Infrastructure changes are idempotent: don't re-provision healthy, unchanged infrastructure.

## 8. Human-approved, resumable progression
- Consequential steps stop for requester review and approval before proceeding.
- Durable state (`.workteam/`) records stage status and every decision, so work resumes without
  re-running, overwriting, or duplicating completed work.

## 9. Parallelise independent work; serialise dependent decisions
- Independent work may run concurrently; decisions that depend on each other are sequenced.
- Independent evaluation (review, QA) runs from multiple unbiased perspectives before consolidation.

## 10. Evidence over claims
- Tests, review findings, QA verdicts, and deployment results must trace to actual evidence — never to a
  summary or an unverified assertion.
