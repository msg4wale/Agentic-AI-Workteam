---
name: change-correctness-analysis
description: Review the implemented change for behavioural correctness, state management, boundaries, error handling, concurrency, idempotency, compatibility, resource handling, unintended side effects, and scope discipline.
---

# Change & Correctness Analysis

## Purpose

Determine whether the code actually performs the assigned technical/product behaviour correctly.

## Review the Diff First

Inspect changed lines, then surrounding code necessary to reason about them.

Avoid unfocused repository-wide review.

## Behavioural Correctness

Check:

- main path;
- alternate paths;
- invalid input;
- missing/empty/null data;
- state transitions;
- error outcomes;
- partial failure;
- retries;
- duplicate execution;
- concurrency;
- idempotency.

## Control Flow

Look for:

- unreachable branches;
- missing return/error;
- swallowed exceptions;
- incorrect fall-through;
- incomplete async handling;
- missing cleanup;
- stale state.

## Data Flow

Check:

- input mapping;
- output mapping;
- type conversion;
- default values;
- truncation/precision;
- ownership;
- mutation.

## Boundary Conditions

Consider:

- zero;
- one;
- maximum;
- empty collections;
- first/last page;
- expiration boundaries;
- time zones;
- date boundaries;
- numeric precision where relevant.

## Compatibility

Check:

- callers;
- API contract;
- schema;
- config;
- serialization;
- migrations;
- deployment order.

## Resource Handling

Where relevant:

- file handles;
- connections;
- transactions;
- locks;
- subprocesses;
- streams;
- async tasks.

## Scope Discipline

Flag unrelated changes and unnecessary refactors that increase review/regression risk.

## Evidence Standard

A finding should identify:

- location;
- concrete execution path;
- expected behaviour;
- actual behaviour;
- source requirement/test where possible.

## Completion Check

Correctness assessment is complete when all changed behaviour and directly affected paths have been considered proportionately to risk.
