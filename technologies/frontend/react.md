# React

**Role:** Primary | **Layer:** Frontend

## Mental model
React renders UI from state and props. Components describe a tree; updates re-render affected work and React commits the resulting changes to the host environment.

## Core areas
- components, props and composition
- state and derived state
- hooks and effect lifecycle
- controlled vs uncontrolled inputs
- context and provider boundaries
- refs and imperative escape hatches
- rendering, reconciliation and keys
- server/client boundaries in modern frameworks

## Production patterns
Keep components focused, derive values instead of duplicating state, isolate side effects, model async states explicitly, and avoid global state unless ownership genuinely crosses the tree.

## Performance
Measure before optimizing. Watch unnecessary renders, large component trees, expensive calculations, network waterfalls and oversized client bundles. Memoization is a tool, not architecture.

## Testing
Prefer user-visible behavior and integration tests; use component-level tests where they clarify contracts.

## Related
Next.js, TanStack Query, Zustand, React Hook Form, Testing Library.
