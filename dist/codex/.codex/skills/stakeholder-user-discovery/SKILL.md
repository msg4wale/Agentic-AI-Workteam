---
name: stakeholder-user-discovery
description: Identify product stakeholders, decision ownership, user groups, personas, goals, pain points, current workflows, and business-level permissions. Use after problem discovery or whenever actors and ownership are unclear.
---

# Stakeholder & User Discovery

## Purpose

Identify everyone materially affected by, responsible for, operating, governing, approving, or using the proposed product.

Do not invent stakeholder roles merely because similar products have them.

## Stakeholder Discovery

Identify relevant parties such as:

- Sponsor
- Business Owner
- Product Owner
- Process Owner
- Administrator
- Moderator
- Operations
- Support
- Finance
- Legal
- Compliance
- Security
- External partner
- Vendor
- Regulator

For each relevant stakeholder capture:

- Role
- Responsibilities
- Expectations
- Decision ownership
- Product dependency
- Approval authority, if any

## User Discovery

Identify relevant user classes:

- Primary users
- Secondary users
- Guest/anonymous users
- Administrators
- Operators
- Support users
- External users

For each materially distinct user/persona capture:

- Persona name or business role
- Description
- Context of use
- Goals
- Pain points
- Current workflow
- Frequency of use, where known
- Access/permission needs
- Information they need
- Decisions/actions they perform

Avoid fictional demographic details unless they materially affect requirements and are stakeholder-supported.

## Roles and Permissions

At the business level discover:

- What can each role do?
- What can each role not do?
- Who owns a business record or process?
- Who can approve/reject?
- Are approvals tiered?
- Can authority be delegated?
- Can one user hold multiple roles?
- What happens when a role changes?

Do not design authentication, RBAC technology, identity infrastructure, or authorization code.

## Challenge Ambiguity

If the stakeholder says "users" without distinction, determine whether all users:

- have the same goals;
- have the same permissions;
- follow the same workflow;
- see the same information.

Split into personas only when differences are materially relevant.

## Output Contribution to idea.md

Populate or refine:

- Stakeholders
- Target Users
- Roles and Permissions
- relevant Glossary entries

## Completion Check

This skill is complete when:

1. Primary user/beneficiary is known.
2. Material secondary actors are known.
3. Decision ownership is clear where required.
4. Personas are differentiated by meaningful goals/workflows/permissions.
5. Business-level access and approval needs are sufficiently understood.
