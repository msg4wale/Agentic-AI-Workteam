---
name: code-design-quality-review
description: Review changed code for clean-code quality, cohesion, coupling, modularity, separation of concerns, testability, duplication, dependency direction, complexity, abstraction quality, and maintainability without enforcing design principles mechanically.
---

# Code Design Quality Review

## Purpose

Independently determine whether the implementation is structured so that it is understandable, testable, maintainable, and safe to change.

This skill evaluates implementation design quality.

It must not become a style-policing or pattern-enforcement exercise.

---

# Core Principle

Use clean-code principles, SOLID, DRY, composition, dependency inversion, encapsulation, and similar concepts as **diagnostic tools**.

Do not treat them as laws.

A finding is justified only when the current design creates a material problem such as:

- harder testing;
- higher defect risk;
- duplicated business behaviour;
- unnecessary coupling;
- unclear ownership;
- unsafe change propagation;
- excessive complexity;
- architecture drift.

Prefer the simplest design that satisfies the task and repository standards.

---

# Review Dimensions

## 1. Readability and Intent

Check:

- names communicate purpose;
- control flow is understandable;
- important domain intent is visible;
- magic values are avoided where they obscure meaning;
- comments explain non-obvious reasoning rather than restating code.

Do not block on naming taste alone.

A naming issue is material when it can mislead future maintainers or obscure domain behaviour.

---

## 2. Cohesion

Check whether each:

- function;
- class;
- module;
- component;

has a coherent responsibility.

Flag units that combine unrelated concerns such as:

- validation + persistence + notification + formatting;
- HTTP concerns mixed deeply into domain logic;
- database mapping mixed with unrelated business policy.

Do not split cohesive code into artificial micro-functions.

---

## 3. Coupling

Check:

- number and direction of dependencies;
- knowledge of internal implementation details;
- tight binding to infrastructure;
- unnecessary cross-module access;
- temporal coupling;
- implicit order dependencies.

Prefer explicit contracts and narrow boundaries where they materially reduce change risk.

---

## 4. Separation of Concerns

Assess whether product/domain logic is unnecessarily mixed with:

- network transport;
- database mechanics;
- filesystem;
- UI rendering;
- environment/configuration access;
- logging side effects;
- external provider SDK details.

Separation is valuable when it materially improves testability, portability, or clarity.

Do not demand additional layers when the current code is already simple and testable.

---

## 5. Testability

Check whether important behaviour can be verified deterministically.

Potential defects include:

- hidden global state;
- hard-coded external dependencies;
- direct time/random/network calls in core logic without a controllable seam where tests require one;
- business logic embedded inside framework callbacks with no practical isolation;
- constructors/functions that create their own hard-to-control infrastructure dependencies;
- excessive static/singleton coupling.

Do not require dependency injection frameworks.

A simple parameter or small boundary may be sufficient.

---

## 6. Duplication

Differentiate:

### Harmless repetition

Small repeated syntax that remains clearer than abstraction.

### Dangerous duplication

Repeated:

- business rules;
- permission rules;
- validation;
- state-transition rules;
- contract mapping;

that can diverge independently.

Flag the latter.

Do not apply DRY mechanically.

---

## 7. Dependency Direction

Where architecture uses layered, hexagonal, clean, or similar boundaries, verify dependencies point in the intended direction.

Examples of problematic direction:

- domain layer imports web framework;
- core business logic imports concrete database adapter;
- frontend domain model imports UI rendering implementation;
- reusable module imports application-specific orchestration.

Tie the finding to TDD/repository architecture.

---

## 8. Modularity

Assess whether change is localized appropriately.

Healthy modularity typically means:

- responsibilities are discoverable;
- public interface is narrow;
- internal details are encapsulated;
- changes do not require unrelated modules to know internal state;
- modules can be tested or reasoned about independently.

Flag circular dependencies and inappropriate cross-module reach.

---

## 9. Complexity

Review:

- cyclomatic/branching complexity;
- deep nesting;
- long methods;
- many condition combinations;
- boolean parameter explosions;
- difficult-to-reason state mutation.

A long function is not automatically bad.

Flag complexity when it materially harms comprehension, testing, or correctness.

Suggest the smallest refactor that reduces risk.

---

## 10. Abstraction Quality

Check for both under-abstraction and over-abstraction.

### Under-abstraction

Examples:

- duplicated critical policy;
- repeated provider-specific handling across callers;
- direct infrastructure details spread through domain code.

### Over-abstraction

Examples:

- interface with one implementation and no useful seam;
- factories/builders around trivial construction;
- generic frameworks for one simple use case;
- excessive indirection hiding straightforward logic.

Do not reward abstraction count.

---

## 11. Interface Quality

Review relevant internal/public interfaces for:

- narrow responsibility;
- explicit inputs/outputs;
- stable semantics;
- minimal leakage;
- invalid-state prevention where practical;
- appropriate error modelling.

Do not redesign approved public APIs unless the implementation violates the TDD/task.

---

## 12. Changeability

Ask:

> If the most likely next requirement changes, how much unrelated code must change?

This is not permission to design speculative flexibility.

Use known adjacent requirements and architecture only.

Flag designs where a small foreseeable change would require editing many unrelated locations because of avoidable coupling or duplication.

---

# SOLID as a Diagnostic Lens

Use selectively:

## Single Responsibility

Flag only when multiple unrelated reasons to change create real maintenance/testing risk.

## Open/Closed

Do not demand extensibility for hypothetical future variants.

Use only when the source requirements already imply multiple variants or extension points.

## Liskov Substitution

Check where inheritance/subtyping exists.

Flag broken behavioural contracts.

## Interface Segregation

Flag broad interfaces forcing consumers to depend on irrelevant methods.

## Dependency Inversion

Use where coupling to concrete infrastructure materially harms testability or violates architecture.

Do not create interfaces everywhere.

---

# Clean Code Finding Standard

A blocking or material finding must state:

```markdown
### [P2] Duplicated approval policy creates two sources of truth

**Location:** `src/requests/service.py:85-112`, `src/approvals/service.py:41-68`

**Issue**

The same approval-threshold rule from BR-008 is implemented independently in two modules.

**Why it matters**

A future policy change can update one path without the other, producing inconsistent authorization behaviour.

**Evidence**

BR-008; both branches encode the same threshold logic.

**Required change**

Consolidate the rule behind one existing or appropriately scoped policy boundary and have both callers use it.
```

Avoid:

> Refactor this to follow SOLID.

That is not actionable.

---

# Severity Guidance

Use severity based on engineering impact.

## P1

Use when design quality creates a high likelihood of:

- incorrect business behaviour;
- serious data/security issue;
- architecture violation;
- near-term unmaintainability blocking safe release.

## P2

Typical for material:

- duplicated business rule;
- untestable core logic;
- excessive coupling;
- serious complexity;
- broken modular boundary.

## P3

Localized maintainability issue with limited risk.

## Suggestion

Optional simplification or clarity improvement.

Do not make every clean-code concern blocking.

---

# Review Boundary

This skill must not:

- redesign the system;
- request speculative abstractions;
- enforce personal formatting preferences;
- demand interfaces/factories/repositories by default;
- reject straightforward procedural code solely because it is not object-oriented;
- require patterns that conflict with repository conventions.

---

# Completion Check

This skill is complete when the changed code has been assessed for:

1. readability;
2. cohesion;
3. coupling;
4. separation of concerns;
5. testability;
6. dangerous duplication;
7. dependency direction;
8. modularity;
9. complexity;
10. abstraction quality;
11. interface quality;
12. changeability;

and all findings are tied to a concrete engineering consequence.
