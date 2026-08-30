# Token Optimization Review

_Scope: the Agentic AI Workteam prompt surface (`.github/agents/*.agent.md`, `.github/skills/*/SKILL.md`)._

## Why this matters

In the VS Code / GitHub Copilot custom-agent model, an invoked agent's `*.agent.md` becomes the
**always-loaded system prompt** for that agent's whole run, while `SKILL.md` files are **loaded on
demand** (progressive disclosure) only when the agent chooses to apply them. Therefore:

> The cheapest tokens are the ones that live in a skill and are loaded only when needed. The most
> expensive are boilerplate repeated inside every agent's system prompt.

Optimization principle: **keep each agent's always-loaded prompt to its decision-critical rules, gates,
verdicts, and hand-offs; push reference detail, templates, and shared boilerplate into on-demand
skills.** Subagent isolation already helps at runtime (each worker/perspective runs in its own context
and returns only concise results), so the lever here is the static prompt size.

## Size profile (at time of review)

| Surface | Files | Words (approx.) |
|---|---|---|
| Agents (always-loaded per invocation) | 9 | ~27,300 |
| Skills (on-demand) | 52 | ~22,900 |

Largest agents by words: `solution-architect` (~4.2k), `engineering-lead` (~4.1k), `qa-engineer`
(~3.4k), `software-engineer` (~3.2k), `code-reviewer` (~3.2k). The five product/eng agents dominate the
always-loaded cost; the Coordinator and Plan Architect are already lean (~2k / ~1.2k).

## Findings

### Applied now (safe, behaviour-preserving)

1. **Deduplicated the `State & Decisions` block.** It was inlined near-verbatim in all 8 worker agents
   (~12–14 lines each). The full contract now lives once in the `workteam-state-management` skill
   (new *Worker Participation* section); each worker keeps a 6-line imperative pointer that preserves the
   load-bearing directives (read the decision log first; don't overwrite approved/`done` work; return
   decisions for the Coordinator to log). Net: ~40–60 lines / ~150–200 words removed from the
   always-loaded surface, and the canonical text is now single-sourced (no drift across 8 files).

### Applied (round 2 — output-contract extraction)

2. **Extracted the large embedded output-contract templates + worked examples** from the five heavy
   agents into new on-demand `*-output-contract` skills, leaving a short pointer + a terse required-section
   list in each agent:
   - `tdd-output-contract` ← `solution-architect` (~4230 → ~3593 words)
   - `engineering-plan-output-contract` ← `engineering-lead` (~4122 → ~3839 words)
   - `qa-report-contract` ← `qa-engineer` (report + `DEF-003` sample) (~3448 → ~3140 words)
   - `review-report-contract` ← `code-reviewer` (report + `[P1]` sample) (~3164 → ~3046 words)
   - `implementation-handoff-contract` ← `software-engineer` (~3174 → ~3027 words)
   The `tdd-output-contract` also now hosts the new **Deployment & Infrastructure Stack (15A)** section
   (the DevOps Engineer's input contract). Behaviour is preserved — the template loads on demand when the
   deliverable is produced — while ~1k words left the always-loaded surface of those five agents.

### Recommended next (still deferred)

4. **Compress repeated severity/verdict catalogues.** `P0–P3`/`SEV-1–4` example lists and verdict
   glossaries are stated at length; the definitions can be terse in the agent with examples pushed to the
   relevant review/QA skill.

### Deliberately kept inline (do not "optimize")

- Each agent's **Non-Negotiable Rules, gates, verdict set, and `Invocation & Delegation`** — these are
  decision-critical and agent-specific; trimming them risks behaviour/quality regressions.
- The **`Source-of-Truth Hierarchy`** (in 7 agents) reads as duplication but each instance is genuinely
  tailored to that stage's inputs; not safe to merge.

## Guidance for future edits

- New shared behaviour → put it in a skill and point to it from agents, rather than pasting into each.
- Prefer terse rule statements in agents; put rationale, examples, and templates in skills.
- Watch the five large agents; they are where any future token pressure should be relieved first.
