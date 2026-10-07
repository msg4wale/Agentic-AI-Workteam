---
name: regression-evidence-validation
description: Assess the regression surface of the implemented change, execute appropriate existing/new automated suites, validate test reliability, and ensure QA evidence is complete and traceable.
---

# Regression & QA Evidence Validation

## Purpose

Determine whether directly related existing behaviour remains intact and whether the QA conclusion is supported by sufficient evidence.

## Regression Surface

Derive from:

- changed components;
- callers/consumers;
- shared business rules;
- shared schema/data;
- public APIs;
- permissions;
- integrations;
- configuration;
- deployment changes.

## Select Regression Scope

Use risk.

Possible levels:

- targeted regression;
- component regression;
- feature regression;
- integration regression;
- full suite.

Do not run full regression solely by habit.

## Existing Automation

Inspect and execute relevant project-standard suites.

Record exact command and result.

## New Automation

Validate new tests are:

- deterministic;
- meaningful;
- maintainable;
- correctly isolated;
- independent of execution order;
- clean in test data.

## Flakiness

If a test is flaky:

- identify pattern;
- do not repeatedly rerun until green and call it pass;
- classify evidence accordingly.

## Evidence Completeness

For each critical acceptance/NFR claim ensure there is traceable evidence.

Evidence can include:

- command output;
- automated test;
- manual scenario result;
- API response;
- approved performance report;
- artifact/screenshot.

## Completion Check

Pass when regression risk is proportionately covered and verdict claims are backed by evidence.
