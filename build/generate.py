#!/usr/bin/env python3
"""
Generate per-harness packages for the Agentic AI Workteam from the neutral `core/`.

Single source of truth:  core/agents/*.agent.md  (neutral frontmatter + capability-abstract bodies)
                         core/skills/<name>/SKILL.md
                         core/Constitution.md
Outputs (committed):     dist/claude-code/ , dist/copilot/ , dist/codex/

Stdlib only. Run from the repo root:  python3 build/generate.py
Implements core/capability-map.yaml (kept in sync by hand).
"""
import os, re, glob, shutil, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORE = os.path.join(ROOT, "core")
DIST = os.path.join(ROOT, "dist")

CAPS = ["READ", "SEARCH", "EDIT", "SHELL", "ASK_USER", "SUBAGENT"]

PLATFORMS = {
    "claude-code": {
        "agents_dir": ".claude/agents", "agent_ext": ".md", "skills_dir": ".claude/skills",
        "tool": {"READ": "Read", "SEARCH": "Grep, Glob", "EDIT": "Edit, Write", "SHELL": "Bash",
                 "ASK_USER": "AskUserQuestion", "SUBAGENT": "Task"},
        "supports": {"subagent": True, "skills": True, "ask_user": True},
        "body_map": {"ASK_USER": "AskUserQuestion", "SUBAGENT": "the Task tool"},
        "legend": True,
    },
    "copilot": {
        "agents_dir": ".github/agents", "agent_ext": ".agent.md", "skills_dir": ".github/skills",
        "tool": {"READ": "read", "SEARCH": "search", "EDIT": "edit", "SHELL": "terminal",
                 "ASK_USER": "vscode/askQuestions", "SUBAGENT": "runSubagent"},
        "supports": {"subagent": True, "skills": True, "ask_user": True},
        "body_map": {"ASK_USER": "#vscode/askQuestions", "SUBAGENT": "runSubagent"},
        "legend": False,
    },
    "codex": {
        "agents_dir": "agents", "agent_ext": ".md", "skills_dir": "skills",
        "tool": {"READ": "read", "SEARCH": "grep", "EDIT": "apply_patch", "SHELL": "shell",
                 "ASK_USER": "ask the user inline in chat and wait",
                 "SUBAGENT": "run the subtask sequentially yourself (no subagents)"},
        "supports": {"subagent": False, "skills": False, "ask_user": False},
        "body_map": {},   # keep neutral tokens; the legend defines them
        "legend": True,
    },
}


def map_body(body, plat):
    for tok, native in PLATFORMS[plat]["body_map"].items():
        body = body.replace(tok, native)
    return body


def split_fm(text):
    if not text.startswith("---\n"):
        raise ValueError("missing frontmatter")
    end = text.index("\n---\n", 4)
    return text[4:end], text[end + 5:]


def parse_neutral_fm(fm):
    d = {"capabilities": [], "invocation": {}}
    cur = None
    for line in fm.split("\n"):
        m = re.match(r"^([A-Za-z0-9_]+):\s*(.*)$", line)
        sub = re.match(r"^\s+([A-Za-z0-9_]+):\s*(.*)$", line)
        if m and not line.startswith(" "):
            cur = m.group(1); val = m.group(2)
            if cur == "capabilities":
                d["capabilities"] = [c.strip() for c in val.strip("[]").split(",") if c.strip()]
            elif cur == "invocation":
                pass
            else:
                d[cur] = val
        elif sub and cur == "invocation":
            d["invocation"][sub.group(1)] = sub.group(2).strip()
    return d


def legend(plat, caps):
    cfg = PLATFORMS[plat]
    parts = [f"{c} → {cfg['tool'][c]}" for c in caps]
    line = f"> **Capability bindings ({plat}):** " + " · ".join(parts) + "."
    if not cfg["supports"]["subagent"] and "SUBAGENT" in caps:
        line += ("\n>\n> **No real subagents here:** run each dispatched subtask and each parallel "
                 "review/QA perspective as a *sequential pass* yourself — isolation is by discipline.")
    if not cfg["supports"]["ask_user"] and "ASK_USER" in caps:
        line += "\n>\n> **No question UI:** ask in chat and wait for the reply before proceeding."
    if not cfg["supports"]["skills"]:
        line += "\n>\n> **No skill system:** when a step cites a skill, read `skills/<name>/SKILL.md` on demand."
    return line


def copilot_fm(d):
    caps = d["capabilities"]
    tools = [PLATFORMS["copilot"]["tool"][c] for c in CAPS if c in caps]
    lines = ["---", f"name: {d['name']}", f"description: {d['description']}"]
    if d.get("argument_hint"):
        lines.append(f"argument-hint: {d['argument_hint']}")
    lines.append("tools:")
    lines += [f"  - {t}" for t in tools]
    lines.append("target: vscode")
    lines.append(f"user-invocable: {d['invocation'].get('user_invocable', 'true')}")
    lines.append(f"disable-model-invocation: {'false' if d['invocation'].get('auto','true')=='true' else 'true'}")
    lines.append("---")
    return "\n".join(lines)


def claude_fm(d):
    caps = d["capabilities"]
    tools = []
    for c in CAPS:
        if c in caps:
            tools += [t.strip() for t in PLATFORMS["claude-code"]["tool"][c].split(",")]
    seen = []
    for t in tools:
        if t not in seen:
            seen.append(t)
    lines = ["---", f"name: {d['slug']}", f"description: {d['description']}",
             f"tools: {', '.join(seen)}", "---"]
    return "\n".join(lines)


def write(path, content):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w") as f:
        f.write(content)


def generate():
    agents = []
    for p in sorted(glob.glob(f"{CORE}/agents/*.agent.md")):
        fm, body = split_fm(open(p).read())
        agents.append((parse_neutral_fm(fm), body))
    skills = sorted(glob.glob(f"{CORE}/skills/*/SKILL.md"))

    if os.path.isdir(DIST):
        shutil.rmtree(DIST)

    for plat, cfg in PLATFORMS.items():
        base = os.path.join(DIST, plat)
        # skills (same <name>/SKILL.md layout everywhere -> relative ../skills links stay valid)
        for sp in skills:
            name = os.path.basename(os.path.dirname(sp))
            write(os.path.join(base, cfg["skills_dir"], name, "SKILL.md"), map_body(open(sp).read(), plat))
        # constitution at install root
        write(os.path.join(base, "Constitution.md"), open(f"{CORE}/Constitution.md").read())
        # agents
        for d, body in agents:
            body = map_body(body, plat)
            leg = (legend(plat, d["capabilities"]) + "\n\n") if cfg["legend"] else ""
            if plat == "copilot":
                content = copilot_fm(d) + "\n\n" + leg + body.lstrip("\n")
            elif plat == "claude-code":
                content = claude_fm(d) + "\n\n" + leg + body.lstrip("\n")
            else:  # codex: no frontmatter, role prompt file
                content = f"# {d['name']}\n\n" + leg + body.lstrip("\n")
            fname = d["slug"] + cfg["agent_ext"]
            write(os.path.join(base, cfg["agents_dir"], fname), content)

        if plat == "claude-code":
            write(os.path.join(base, "CLAUDE.md"), claude_entry(agents))
        if plat == "codex":
            write(os.path.join(base, "AGENTS.md"), codex_entry(agents))

    print(f"Generated {len(PLATFORMS)} platforms: {', '.join(PLATFORMS)}")
    print(f"  agents={len(agents)} skills={len(skills)} -> dist/")


def _agent_table(agents):
    rows = []
    for d, _ in agents:
        rows.append(f"| `{d['slug']}` | {d['name']} | {', '.join(d['capabilities'])} |")
    return "\n".join(rows)


def claude_entry(agents):
    return (
        "# Agentic AI Workteam (Claude Code)\n\n"
        "A coordinator-orchestrated SDLC workteam. Subagents live in `.claude/agents/` and reusable "
        "skills in `.claude/skills/`. Start by invoking the **coordinator** subagent with your goal; it "
        "dispatches the other agents via the `Task` tool, stops at each stage for your approval, and keeps "
        "durable state under `.workteam/`.\n\n"
        "**Capability bindings:** ASK_USER → AskUserQuestion · SUBAGENT → Task · "
        "READ/SEARCH/EDIT/SHELL → Read / Grep,Glob / Edit,Write / Bash.\n\n"
        "All agents honour `Constitution.md`.\n\n"
        "## Agents\n\n| slug | role | capabilities |\n|---|---|---|\n" + _agent_table(agents) + "\n"
    )


def codex_entry(agents):
    idx = "\n".join([f"- `agents/{d['slug']}.md` — {d['name']}" for d, _ in agents])
    return (
        "# Agentic AI Workteam (Codex)\n\n"
        "A coordinator-orchestrated SDLC workteam, adapted for Codex.\n\n"
        "## How to run it here\n\n"
        "Codex runs a **single agent** with no subagents, no skill system, and no interactive question UI, "
        "so this package degrades gracefully:\n\n"
        "- **Orchestration:** you play every role yourself, in order, following `agents/coordinator.md`. "
        "Dispatching a worker = reading that role's `agents/<slug>.md` and doing the stage.\n"
        "- **SUBAGENT (no subagents):** the Coordinator's dispatch and the parallel review/QA perspectives "
        "run as **sequential passes** — do each perspective as its own focused pass, then consolidate.\n"
        "- **Skills (no skill system):** when a role cites a skill, read `skills/<name>/SKILL.md` on demand.\n"
        "- **ASK_USER (no question UI):** ask the user in chat and wait for the reply before proceeding.\n"
        "- **Durable state:** keep `.workteam/Workteam-State.md` and `.workteam/Decisions-Log.md` by hand "
        "(same model as the other harnesses) so work resumes without re-running or duplicating.\n\n"
        "All roles honour `Constitution.md`.\n\n"
        "## Pipeline\n\n"
        "idea-discovery → product-manager → solution-architect → engineering-lead → "
        "plan-architect (gate) → software-engineer → code-reviewer → qa-engineer → "
        "devops-engineer. Stop for the user's approval after every stage.\n\n"
        "## Role prompts\n\n" + idx + "\n\n## Skills\n\nRead `skills/<name>/SKILL.md` as roles cite them.\n"
    )


if __name__ == "__main__":
    generate()
