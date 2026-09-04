# React

**Role:** Primary | **Layer:** Frontend

## Mental model
React describes UI as a function of state. Components form a tree, rendering computes what the UI should look like, and React reconciles that description before committing necessary host changes.

```text
props + state + context
        |
        v
     render
        |
   reconciliation
        |
        v
      commit
```

Rendering should be treated as a pure calculation. Side effects belong outside render.

## Components and composition
Prefer small components with clear ownership. Composition is usually safer than inheritance. Keep component APIs based on domain intent rather than exposing implementation details.

## State
Separate:
- local UI state
- derived state
- server state
- cross-tree client state
- URL state
- form state

Do not copy the same remote resource into multiple state systems without a clear synchronization strategy.

## Hooks
Know `useState`, `useReducer`, `useEffect`, `useMemo`, `useCallback`, `useRef`, context and custom hooks. Hooks are not lifecycle methods with different names; they express stateful behavior and synchronization around rendering.

### Effects
An effect synchronizes React with something external: subscriptions, browser APIs, imperative widgets or network side effects that truly belong there. If a value can be calculated from props/state during render, do not create an effect just to derive it.

## Rendering and reconciliation
Keys identify stable siblings. Index keys are dangerous when list order or membership changes. Understand state preservation, remounting, conditional trees and how component identity affects local state.

## Server/client boundaries
Modern React applications can render on the server and selectively ship client code. Keep browser-only behavior behind client boundaries and avoid sending unnecessary JavaScript to users.

## Forms
For complex forms, separate form state, schema validation and server mutation. The canonical stack uses React Hook Form for form lifecycle and Zod for runtime schemas.

## Server state
Use TanStack Query for remote asynchronous state when appropriate. Do not build a second server-state cache inside a general Zustand store.

## Performance
Optimize based on measurements:
- avoid unnecessary client components
- reduce network waterfalls
- virtualize genuinely large lists
- split heavy bundles
- stabilize expensive calculations only when profiling shows value
- avoid context updates that invalidate huge subtrees
- keep images and data payloads appropriately sized

Memoization is an optimization, not a substitute for good ownership and data flow.

## Accessibility
Semantic HTML, keyboard interaction, focus management, labels and accessible names are application requirements. Component libraries help but do not make an application automatically accessible.

## Testing
Prefer behavior-oriented tests. Test important user interactions and component contracts rather than implementation details such as internal hook calls. Use Testing Library for component behavior and Playwright for high-value journeys.

## Security
React escapes ordinary text rendering, but dangerous HTML, URLs, browser storage, authentication flows and third-party scripts still require explicit security design. Never place secrets in client bundles.

## Debugging checklist
1. Is the value truly state or derived?
2. Which component owns it?
3. Which context/store causes the render?
4. Is an effect synchronizing with an external system or compensating for bad state design?
5. Is the bottleneck render work, network, bundle size or server latency?

## Common mistakes
- putting everything in global state
- effect chains that derive state
- unstable or incorrect keys
- excessive memoization
- fetching the same data from multiple layers
- client-rendering content that could remain server-side
- testing implementation details

## Interview-level topics
Reconciliation, keys and identity, render vs commit, hooks and effects, context propagation, controlled inputs, state ownership, server/client boundaries, concurrent rendering concepts and performance diagnosis.

## Related
Next.js, TanStack Query, Zustand, React Hook Form, Zod, Testing Library.