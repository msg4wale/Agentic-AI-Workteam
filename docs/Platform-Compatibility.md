# Platform Compatibility & Install

The workteam is authored once in **`core/`** (platform-neutral) and compiled by `build/generate.py`
into ready-to-copy packages under **`dist/`** for three harnesses. This page is the capability matrix,
the Codex degradations, and how to install each.

## Capability matrix

| Capability | Claude Code | GitHub Copilot (VS Code) | Codex |
|---|---|---|---|
| Agent definitions | `.claude/agents/<slug>.md` (subagents) | `.github/agents/<slug>.agent.md` | roles in `.codex/agents/<slug>.md`, driven by `AGENTS.md` |
| Skills / progressive disclosure | ✅ `.claude/skills` | ✅ `.github/skills` | ⚠️ plain files, read on demand |
| Subagents (`SUBAGENT`) | ✅ `Task` tool | ✅ `runSubagent` | ❌ none → **sequential passes** |
| Interactive questions (`ASK_USER`) | ✅ `AskUserQuestion` | ✅ `#vscode/askQuestions` | ⚠️ ask inline in chat |
| Read / Search / Edit / Shell | Read / Grep,Glob / Edit,Write / Bash | read / search / edit / terminal | read / grep / apply_patch / shell |
| Durable state (`.workteam/`) | ✅ | ✅ | ✅ (maintained by the single agent) |

Neutral capability tokens used in `core/`: `READ, SEARCH, EDIT, SHELL, ASK_USER, SUBAGENT`. Each
generated agent carries a **Capability Bindings** legend (Claude Code and Codex) or native tool names in
the body (Copilot), so every harness knows how to realize each token. Full mapping:
`core/capability-map.yaml`.

## What degrades on Codex (and how)

Codex runs a single agent with no subagents, no skill system, and no interactive-question UI. The package
preserves the **same methodology**, with these graceful degradations spelled out in each role's legend
and in `AGENTS.md`:

- **Orchestration & parallelism** — the Coordinator's worker dispatch and the Code Reviewer's five and QA
  Engineer's four parallel perspectives become **sequential passes** performed by the one agent; isolation
  is by discipline, not runtime. Findings are still produced per perspective, then consolidated.
- **Skills** — cited skills are read on demand from `skills/<name>/SKILL.md` instead of being auto-loaded.
- **Questions** — `ASK_USER` means ask in chat and wait; the checkpoint-approval model still applies.
- **Durable state** — the agent maintains `.workteam/Workteam-State.md` and `Decisions-Log.md` by hand,
  the same model as the other harnesses, so runs still resume without re-running or duplicating work.

Behaviour is therefore **equivalent in method, not in runtime guarantees**, on Codex.

## Install

All packages install the same product artifacts (`idea.md`, `PRD.md`, …) at your project root. The
easiest path — and the one that makes a project **transferable across harnesses** — is the installer:

```bash
python3 build/generate.py --install all        <YOUR-PROJECT>   # every harness, one framework version
python3 build/generate.py --install claude-code <YOUR-PROJECT>  # or copilot | codex, a single harness
```
`--install` copies the chosen package(s) and seeds `.workteam/` (`Workteam-State.md`, `Decisions-Log.md`,
`Project.md` stamped with the framework version). See [Project-Portability.md](Project-Portability.md).

Or copy a package by hand:

### Claude Code
```bash
cp -R dist/claude-code/.claude   <YOUR-PROJECT>/.claude
cp    dist/claude-code/CLAUDE.md dist/claude-code/Constitution.md <YOUR-PROJECT>/
```
Invoke the **coordinator** subagent with your goal; it dispatches the others via `Task`.

### GitHub Copilot (VS Code)
```bash
cp -R dist/copilot/.github         <YOUR-PROJECT>/.github
cp    dist/copilot/WORKTEAM.md dist/copilot/Constitution.md <YOUR-PROJECT>/
```
Open in VS Code with Copilot agent mode; invoke the **Coordinator** agent.

### Codex
```bash
cp    dist/codex/AGENTS.md dist/codex/Constitution.md <YOUR-PROJECT>/
cp -R dist/codex/.codex                               <YOUR-PROJECT>/.codex
```
Point Codex at the repo; it reads `AGENTS.md` and follows the pipeline, reading `.codex/agents` and
`.codex/skills` on demand.

## Regenerating

`core/` is the only hand-authored tree. After editing it:
```bash
python3 build/generate.py     # rewrites dist/ for all three platforms (idempotent, stdlib only)
```
Never hand-edit `dist/` — it is build output. Keep `core/capability-map.yaml` and the mapping in
`build/generate.py` in sync.
