# Agentic AI Workteam (Claude Code)

- Framework Version: 1.0.0

A coordinator-orchestrated SDLC workteam. Subagents live in `.claude/agents/` and reusable skills in `.claude/skills/`. Start by invoking the **coordinator** subagent with your goal; it dispatches the other agents via the `Task` tool, stops at each stage for your approval, and keeps durable, transferable state under `.workteam/`.

**Capability bindings:** ASK_USER → AskUserQuestion · SUBAGENT → Task · READ/SEARCH/EDIT/SHELL → Read / Grep,Glob / Edit,Write / Bash.

**Transferable project:** read `.workteam/Project.md` and `.workteam/Workteam-State.md` first; if another harness was last active, reconcile and resume at the first unapproved stage. All agents honour `Constitution.md`.

## Agents

| slug | role | capabilities |
|---|---|---|
| `code-reviewer` | Code Reviewer | READ, SEARCH, EDIT, SHELL, ASK_USER, SUBAGENT |
| `coordinator` | Coordinator | READ, SEARCH, EDIT, ASK_USER, SUBAGENT |
| `devops-engineer` | DevOps Engineer | READ, SEARCH, EDIT, SHELL, ASK_USER, SUBAGENT |
| `engineering-lead` | Engineering Lead | READ, SEARCH, EDIT, ASK_USER |
| `idea-discovery` | Idea Discovery | READ, SEARCH, EDIT, ASK_USER |
| `plan-architect` | Plan Architect | READ, SEARCH, EDIT, SHELL, ASK_USER, SUBAGENT |
| `product-manager` | Product Manager | READ, SEARCH, EDIT, ASK_USER |
| `qa-engineer` | QA Engineer | READ, SEARCH, EDIT, SHELL, ASK_USER, SUBAGENT |
| `software-engineer` | Software Engineer | READ, SEARCH, EDIT, SHELL, ASK_USER, SUBAGENT |
| `solution-architect` | Solution Architect | READ, SEARCH, EDIT, ASK_USER |
