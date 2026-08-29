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

### Recommended next (deferred — larger savings, more churn)

These were **not** applied (they exceed "safe dedup"); they are the high-value opportunities if deeper
optimization is wanted later. Each moves reference bulk out of the always-loaded agent into an
on-demand skill, keeping a short pointer in the agent.

2. **Extract large embedded output-contract templates.** The biggest agents carry full markdown
   templates for their deliverables inline (e.g. the `TDD.md` skeleton in `solution-architect`, the
   `Engineering-Plan.md` section list in `engineering-lead`, the review/QA report templates in
   `code-reviewer`/`qa-engineer`). Moving each template into its stage's validation/output skill (or a
   small `*-output-contract` skill) and referencing it would remove an estimated 1–3k words from the
   always-loaded surface of those five agents — the single largest available saving.
3. **Extract worked examples.** The long illustrative task/finding/defect examples (e.g. sample `BE-002`
   task, sample `[P1]` finding, sample `DEF-003` defect) are teaching aids that rarely need to be in the
   system prompt; relocate to their skills.
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
