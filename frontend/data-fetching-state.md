# Frontend Data Fetching and State

The frontend consumes server state over unreliable networks. Treat fetching, caching, synchronization, and UI state as separate concerns.

## State taxonomy

```text
URL state
Client UI state
Form state
Server state
Durable local state
```

### Server state

Server state is owned by the backend and can become stale independently of the current browser.

Examples:

- user profile
- product catalog
- notifications
- orders

Use a query/cache abstraction when the application has enough server state to require synchronization, deduplication, stale handling, or optimistic updates.

## Fetch lifecycle

```text
idle
 ↓
loading
 ↓
success ─────→ refetch
 │               │
 └──── error ←───┘
```

A production UI should also model:

- empty results
- stale data
- partial data
- cancellation
- retry
- pagination
- optimistic updates

## Caching

Client caching is not the same as HTTP caching.

Client cache answers:

> Can another component reuse data we already fetched?

HTTP cache answers:

> Can an intermediary or browser reuse this response without contacting the origin?

Use both deliberately.

## Query keys

A cache key must represent every input that changes the result.

Bad:

```text
users
```

Better:

```text
users:{tenantId}:{page}:{filters}:{sort}
```

## Mutations

A mutation can require:

1. send request
2. disable/restrict duplicate submission
3. update or invalidate related cache
4. reconcile server response
5. surface errors

Optimistic updates are useful when the operation is reversible and the failure path is well designed.

## Pagination

Choose based on access pattern:

- offset pagination is simple and useful for stable small datasets
- cursor pagination scales better for continuously changing or large collections

Do not make pagination an unexamined frontend convention; it is an API/database contract.

## Tooling

Canonical choices for this repository:

- native `fetch` for low-level HTTP
- TanStack Query when server-state synchronization is needed
- local component state for local UI state
- URL/router state for shareable navigation state
- schema validation at response boundaries

Redux Toolkit or Zustand are options for genuinely shared client state, not automatic replacements for server-state caching.
