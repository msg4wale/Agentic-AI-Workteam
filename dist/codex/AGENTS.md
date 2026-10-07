# Agentic AI Workteam (Codex)

- Framework Version: 1.0.0

A coordinator-orchestrated SDLC workteam, adapted for Codex.

## How to run it here

Codex runs a **single agent** with no subagents, no skill system, and no interactive question UI, so this package degrades gracefully:

- **Orchestration:** you play every role yourself, in order, following `.codex/agents/coordinator.md`. Dispatching a worker = reading that role's `.codex/agents/<slug>.md` and doing the stage.
- **SUBAGENT (no subagents):** the Coordinator's dispatch and the parallel review/QA perspectives run as **sequential passes** — do each perspective as its own focused pass, then consolidate.
- **Skills (no skill system):** when a role cites a skill, read `.codex/skills/<name>/SKILL.md`.
- **ASK_USER (no question UI):** ask the user in chat and wait for the reply before proceeding.
- **Durable, transferable state:** maintain `.workteam/Workteam-State.md`, `Decisions-Log.md`, and `Project.md` by hand (same model as the other harnesses) so work resumes — in this or any other harness — without re-running or duplicating. Read `.workteam/Project.md` first.

All roles honour `Constitution.md`.

## Pipeline

idea-discovery → product-manager → solution-architect → engineering-lead → plan-architect (gate) → software-engineer → code-reviewer → qa-engineer → devops-engineer. Stop for the user's approval after every stage.

## Role prompts

- `.codex/agents/code-reviewer.md` — Code Reviewer
- `.codex/agents/coordinator.md` — Coordinator
- `.codex/agents/devops-engineer.md` — DevOps Engineer
- `.codex/agents/engineering-lead.md` — Engineering Lead
- `.codex/agents/idea-discovery.md` — Idea Discovery
- `.codex/agents/plan-architect.md` — Plan Architect
- `.codex/agents/product-manager.md` — Product Manager
- `.codex/agents/qa-engineer.md` — QA Engineer
- `.codex/agents/software-engineer.md` — Software Engineer
- `.codex/agents/solution-architect.md` — Solution Architect

## Skills

Read `.codex/skills/<name>/SKILL.md` as roles cite them.
