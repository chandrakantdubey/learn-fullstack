# React Architecture

React is a component model and rendering library. Treat it as a UI architecture tool, not the source of frontend fundamentals.

## Core model

```text
State / Props
     ↓
Render
     ↓
React element tree
     ↓
Reconciliation
     ↓
DOM mutations
     ↓
Browser rendering
```

A component should make ownership of state and side effects obvious.

## Component design

Prefer components with one clear responsibility and explicit inputs.

Use composition for reusable behavior rather than creating deep inheritance-like component trees.

Separate:

- presentation
- state ownership
- data fetching
- domain logic
- side effects

## State ownership

Ask where state actually belongs.

- local UI state → component
- shared UI state → nearest common owner/context
- server state → data-fetching/cache layer
- URL state → router
- durable client state → explicit persistence layer

Do not put server data into a global store simply because it is shared.

## Effects

Effects synchronize React with external systems.

Examples:

- browser APIs
- subscriptions
- imperative libraries
- external connections

Do not use effects to derive values that can be calculated during render.

## Rendering performance

Common causes of unnecessary work:

- unstable props
- over-broad context updates
- duplicated state
- expensive rendering on hot paths
- large client bundles

Measure before adding memoization.

## Forms

Forms should have:

- explicit validation
- clear error states
- disabled/submitting states
- accessible labels
- server-side validation

Client validation improves UX; server validation protects the system.

## Error handling

Design for:

- loading
- success
- empty
- error
- retry
- stale data
- partial rendering

An error boundary handles rendering failures. It is not a replacement for request-level error handling.

## Architecture rule

A healthy React codebase makes it easy to answer:

> Where does this data come from, who owns it, when is it fetched, and what happens when it fails?
