# Agentic AI Workteam (GitHub Copilot / VS Code)

- Framework Version: 1.0.0

Agents live in `.github/agents/` and skills in `.github/skills/`. Invoke the **Coordinator** agent with your goal; it dispatches the others via `runSubagent`, stops at each stage for your approval, and keeps durable, transferable state under `.workteam/`.

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
