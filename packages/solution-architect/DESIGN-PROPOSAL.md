# Solution Architect Agent — Design Proposal

## Role

Convert a validated `PRD.md` into an engineering-planning-ready `TDD.md`.

## New Skills

1. `architecture-drivers-decisions`
2. `technology-stack-discovery`
3. `system-component-design`
4. `data-interface-integration-design`
5. `security-reliability-operations`
6. `deployment-observability-delivery`
7. `tdd-validation`

## Shared Skill Reused

- `prd-validation` from the Product Manager package

## Core Boundary

The Solution Architect owns technical design decisions.

It may select technologies and architecture patterns when justified by requirements and constraints.

It must not change product requirements or decompose the design into engineering tasks.

## Handoff Contract

Input: `PRD.md`

Output: `TDD.md`

Next owner: Engineering Lead


## Stack Selection Authority
The Architect recommends; the stakeholder may accept, modify, or override. Overrides are blocked only when mandatory requirements become technically unachievable.
