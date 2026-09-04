# TanStack Query

**Role:** Primary | **Layer:** Frontend

## Mental model
TanStack Query manages asynchronous server state: fetching, caching, synchronization, invalidation, retries and mutations. It is not a general client-state store.

## Learn
- query keys and cache identity
- stale/fresh semantics
- queries and mutations
- invalidation and optimistic updates
- retries, cancellation and pagination
- dependent and parallel queries
- SSR/hydration

## Production
Define stable query keys, invalidate deliberately after mutations, bound retries, surface loading/error/empty states, and prevent duplicate network waterfalls.

## Related
React, Next.js, Zustand, HTTP APIs.
