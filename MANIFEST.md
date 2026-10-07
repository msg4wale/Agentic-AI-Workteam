# Agentic AI Workteam Manifest

Source of truth: `core/` (platform-neutral). Installable packages are generated into `dist/`
by `build/generate.py` for Claude Code, GitHub Copilot, and Codex. Do not hand-edit `dist/`.

- Agents: 10   (core/agents/*.agent.md)
- Skills: 65   (core/skills/<name>/SKILL.md)
- Constitution: core/Constitution.md
- Generator: build/generate.py   ·   Capability map: core/capability-map.yaml
- Generated packages: dist/claude-code/ · dist/copilot/ · dist/codex/

## Agents (neutral source)
- `core/agents/code-reviewer.agent.md`
- `core/agents/coordinator.agent.md`
- `core/agents/devops-engineer.agent.md`
- `core/agents/engineering-lead.agent.md`
- `core/agents/idea-discovery.agent.md`
- `core/agents/plan-architect.agent.md`
- `core/agents/product-manager.agent.md`
- `core/agents/qa-engineer.agent.md`
- `core/agents/software-engineer.agent.md`
- `core/agents/solution-architect.agent.md`

## Skills (neutral source)
- `core/skills/architecture-drivers-decisions/SKILL.md`
- `core/skills/build-release-packaging/SKILL.md`
- `core/skills/change-correctness-analysis/SKILL.md`
- `core/skills/code-design-quality-review/SKILL.md`
- `core/skills/code-quality-security-review/SKILL.md`
- `core/skills/codebase-reuse-analysis/SKILL.md`
- `core/skills/constitution-governance/SKILL.md`
- `core/skills/data-interface-integration-design/SKILL.md`
- `core/skills/dependency-sequencing-analysis/SKILL.md`
- `core/skills/deploy-execution-verification/SKILL.md`
- `core/skills/deployment-observability-delivery/SKILL.md`
- `core/skills/deployment-plan-design/SKILL.md`
- `core/skills/deployment-readiness-analysis/SKILL.md`
- `core/skills/deployment-reporting-handover/SKILL.md`
- `core/skills/engineering-issue-specification/SKILL.md`
- `core/skills/engineering-plan-output-contract/SKILL.md`
- `core/skills/engineering-plan-validation/SKILL.md`
- `core/skills/engineering-readiness-analysis/SKILL.md`
- `core/skills/environment-provisioning/SKILL.md`
- `core/skills/epic-user-story-design/SKILL.md`
- `core/skills/existing-system-discovery/SKILL.md`
- `core/skills/focused-implementation/SKILL.md`
- `core/skills/functional-acceptance-validation/SKILL.md`
- `core/skills/idea-validation/SKILL.md`
- `core/skills/implementation-handoff-contract/SKILL.md`
- `core/skills/implementation-handoff-validation/SKILL.md`
- `core/skills/infrastructure-as-code-authoring/SKILL.md`
- `core/skills/integration-data-failure-validation/SKILL.md`
- `core/skills/journey-requirements-discovery/SKILL.md`
- `core/skills/nonfunctional-quality-validation/SKILL.md`
- `core/skills/parallel-execution-orchestration/SKILL.md`
- `core/skills/plan-duplication-detection/SKILL.md`
- `core/skills/plan-validation-reporting/SKILL.md`
- `core/skills/prd-validation/SKILL.md`
- `core/skills/prioritization-release-planning/SKILL.md`
- `core/skills/problem-outcome-discovery/SKILL.md`
- `core/skills/product-framing-synthesis/SKILL.md`
- `core/skills/product-quality-metrics/SKILL.md`
- `core/skills/qa-decision-defect-reporting/SKILL.md`
- `core/skills/qa-readiness-context/SKILL.md`
- `core/skills/qa-report-contract/SKILL.md`
- `core/skills/qa-verification-planning/SKILL.md`
- `core/skills/quality-edge-case-discovery/SKILL.md`
- `core/skills/regression-evidence-validation/SKILL.md`
- `core/skills/repository-context-analysis/SKILL.md`
- `core/skills/requirement-architecture-compliance/SKILL.md`
- `core/skills/requirements-acceptance-criteria/SKILL.md`
- `core/skills/review-decision-validation/SKILL.md`
- `core/skills/review-readiness-context/SKILL.md`
- `core/skills/review-report-contract/SKILL.md`
- `core/skills/risk-based-test-design/SKILL.md`
- `core/skills/scope-risk-discovery/SKILL.md`
- `core/skills/security-data-integrity-review/SKILL.md`
- `core/skills/security-reliability-operations/SKILL.md`
- `core/skills/stakeholder-user-discovery/SKILL.md`
- `core/skills/subagent-parallel-execution/SKILL.md`
- `core/skills/system-component-design/SKILL.md`
- `core/skills/task-readiness-analysis/SKILL.md`
- `core/skills/tdd-output-contract/SKILL.md`
- `core/skills/tdd-validation/SKILL.md`
- `core/skills/technical-task-decomposition/SKILL.md`
- `core/skills/technology-stack-discovery/SKILL.md`
- `core/skills/test-verification-review/SKILL.md`
- `core/skills/testing-verification/SKILL.md`
- `core/skills/workteam-state-management/SKILL.md`
