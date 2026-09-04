# Zustand

**Role:** Primary | **Layer:** Frontend

## Mental model
Zustand is a small state-management library centered on stores and subscriptions. Components subscribe to selected slices rather than a framework-wide action/reducer ceremony.

## Learn
- store creation
- selectors and shallow comparison
- actions and derived state
- middleware and persistence
- reset/hydration behavior

## Production
Use it for client-owned state such as UI preferences, workflows or local session state. Keep server state in TanStack Query and avoid duplicating remote data in a Zustand store.

## Pitfalls
Global stores become dumping grounds when domain ownership is unclear. Persist only data that is safe and useful to persist.
