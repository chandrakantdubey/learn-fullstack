# Redis Engineering

Redis is useful when the application's latency, coordination, or asynchronous-work requirements benefit from fast in-memory operations.

## Primary uses

- cache
- session storage
- rate limiting
- distributed coordination
- lightweight queues
- short-lived state

Do not treat Redis as a default replacement for PostgreSQL. The source of truth should remain explicit.

## Cache-aside

The common application pattern is:

```text
request
  ↓
cache lookup
  ├── hit → return
  └── miss
       ↓
     database
       ↓
     populate cache
       ↓
     return
```

Questions every cache design must answer:

- What is cached?
- Who owns the cache entry?
- What is the TTL?
- What invalidates it?
- What happens when Redis is unavailable?
- Can stale data be served safely?

## Key design

Use predictable, namespaced keys.

```text
user:{id}
product:{id}
rate-limit:{identity}:{window}
```

Avoid keys whose meaning depends on undocumented application behavior.

## TTL

TTL is both a memory-management mechanism and a correctness decision. A longer TTL usually improves hit rate but increases staleness risk.

## Rate limiting

A simple counter pattern can enforce per-identity or per-route limits. Production implementations must account for atomicity, expiration, clock boundaries, and distributed instances.

## Distributed locks

Locks can coordinate access to a resource, but they are easy to misuse. Prefer database constraints or transactional mechanisms when those express the invariant more directly.

A distributed lock requires a bounded lease, ownership semantics, and a plan for client failure.

## Failure behavior

Redis should not automatically become a single point of failure for every request. Decide whether an outage should:

- fail open
- fail closed
- bypass cache and use the source of truth
- degrade a non-critical feature

The answer depends on the feature.

## Connects to

`data/postgresql.md`, `backend/service-architecture.md`, `production/reliability.md`, and `production/performance.md`.
