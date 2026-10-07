# Project Portability — resume across harnesses

A workteam project can be started on one harness (Claude Code, GitHub Copilot in VS Code, or Codex) and
**continued on another**. This page explains how, and the one discipline that makes it reliable.

## Why it works

Everything that defines an in-flight project is a **plain, harness-neutral file committed to the repo**:

- **Deliverables** at the project root — `idea.md`, `PRD.md`, `TDD.md`, `Engineering-Plan.md`,
  `Plan-Validation-Report.md`, `QA-Report.md`, `Deployment-Plan.md`, `Deployment-Report.md`, plus the
  source and tests.
- **Durable state** under `.workteam/` — `Workteam-State.md` (stage/gate/task status),
  `Decisions-Log.md` (every clarification), and `Project.md` (the portable manifest).
- **`Constitution.md`** — the quality/spec/security bar.

None of these reference a specific harness (agents are named by **slug**, deliverables by **root path**),
so git carries the whole project between harnesses unchanged.

The **one rule**: only **committed** files transfer. Ephemeral chat/session context does not — so you
**flush and commit before switching**.

## One-time setup: carry all harnesses

Install every harness package into the project so it opens anywhere with no reinstall:

```bash
python3 build/generate.py --install all <YOUR-PROJECT>
```

This lays down `.claude/` (+ `CLAUDE.md`), `.github/` (+ `WORKTEAM.md`), `.codex/` (+ `AGENTS.md`),
`Constitution.md`, and seeds `.workteam/` with `Workteam-State.md`, `Decisions-Log.md`, and `Project.md`
(stamped with the framework version and the installed harnesses). Commit it.

> Carrying all harnesses triplicates the skills directory (`.claude/skills`, `.github/skills`,
> `.codex/skills`) — that is the cost of opening instantly in any harness. Install a single harness
> instead (`--install claude-code .`) if you don't need that.

## The switch loop

```
         ┌─────────────────────────── Harness A (e.g. Copilot) ───────────────────────────┐
         │ work … → Flush-on-leave: make .workteam/ true, set Last Active Harness = A,     │
         │ append a Transfer Log row, COMMIT + push                                        │
         └─────────────────────────────────────────┬───────────────────────────────────────┘
                                                    │ git pull
         ┌──────────────────────────── Harness B (e.g. Claude Code) ──────────────────────┐
         │ Resume-on-enter: read .workteam/Project.md first → sees Last Active = A ≠ B →   │
         │ reconcile, resume at first unapproved stage (no re-run / overwrite / duplicate) │
         └─────────────────────────────────────────────────────────────────────────────────┘
```

### Flush-on-leave (Harness A, before you switch)
1. Ensure `Workteam-State.md` and `Decisions-Log.md` reflect true current reality.
2. Update `Project.md`: set **Last Active Harness** + timestamp, refresh Current Stage and the
   Deliverables table, append a **Transfer Log** row.
3. **Commit and push.**

### Resume-on-enter (Harness B)
1. `git pull`, open the project in Harness B, invoke the **Coordinator**.
2. It reads `.workteam/Project.md` first, sees a different Last Active Harness, records the handoff, and
   resumes at the first non-approved stage — never restarting approved work.
3. **Version drift:** if `Project.md`'s Framework Version differs from Harness B's installed package stamp
   (in `CLAUDE.md` / `WORKTEAM.md` / `AGENTS.md`), the Coordinator surfaces it. Re-sync with
   `python3 build/generate.py --install <harness> .` from a matching framework version.

## Worked example: Copilot → Claude Code → back

1. **Copilot (VS Code):** run through Idea Discovery → PRD → TDD; each approved. Flush: `Project.md` Last
   Active = `copilot`, Current Stage = `engineering-lead`. Commit + push.
2. **Claude Code:** pull, invoke `coordinator`. It reads `Project.md` (Last Active = copilot), resumes at
   Engineering Lead — the approved `idea.md`/`PRD.md`/`TDD.md` are untouched. Work proceeds through
   Plan Architect, implementation, review, QA. Flush: Last Active = `claude-code`. Commit + push.
3. **Copilot again:** pull, invoke Coordinator. It resumes at DevOps (QA already passed and approved).
   No stage is re-run; decisions made in Claude Code are already in `Decisions-Log.md`.

## What does NOT transfer
- Uncommitted edits and the live chat/session transcript of the other harness — hence flush + commit.
- Harness-specific runtime behaviour: on **Codex** there are no real subagents, so the parallel
  review/QA perspectives ran (and resume) as sequential passes. The *decisions and verdicts* transfer;
  the runtime shape is per harness. See [Platform-Compatibility.md](Platform-Compatibility.md).
