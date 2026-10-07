# Agentic AI Workteam (Codex)

A coordinator-orchestrated SDLC workteam, adapted for Codex.

## How to run it here

Codex runs a **single agent** with no subagents, no skill system, and no interactive question UI, so this package degrades gracefully:

- **Orchestration:** you play every role yourself, in order, following `agents/coordinator.md`. Dispatching a worker = reading that role's `agents/<slug>.md` and doing the stage.
- **SUBAGENT (no subagents):** the Coordinator's dispatch and the parallel review/QA perspectives run as **sequential passes** — do each perspective as its own focused pass, then consolidate.
- **Skills (no skill system):** when a role cites a skill, read `skills/<name>/SKILL.md` on demand.
- **ASK_USER (no question UI):** ask the user in chat and wait for the reply before proceeding.
- **Durable state:** keep `.workteam/Workteam-State.md` and `.workteam/Decisions-Log.md` by hand (same model as the other harnesses) so work resumes without re-running or duplicating.

All roles honour `Constitution.md`.

## Pipeline

idea-discovery → product-manager → solution-architect → engineering-lead → plan-architect (gate) → software-engineer → code-reviewer → qa-engineer → devops-engineer. Stop for the user's approval after every stage.

## Role prompts

- `agents/code-reviewer.md` — Code Reviewer
- `agents/coordinator.md` — Coordinator
- `agents/devops-engineer.md` — DevOps Engineer
- `agents/engineering-lead.md` — Engineering Lead
- `agents/idea-discovery.md` — Idea Discovery
- `agents/plan-architect.md` — Plan Architect
- `agents/product-manager.md` — Product Manager
- `agents/qa-engineer.md` — QA Engineer
- `agents/software-engineer.md` — Software Engineer
- `agents/solution-architect.md` — Solution Architect

## Skills

Read `skills/<name>/SKILL.md` as roles cite them.
