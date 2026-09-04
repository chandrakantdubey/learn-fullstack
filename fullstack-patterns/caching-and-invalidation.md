# Caching and Invalidation

Caching is a consistency decision disguised as a performance optimization.

## Problem

A cache can reduce latency and database load, but it introduces another copy of state. The hard problem is deciding when that copy is valid.

## Boundary

Define explicitly:

- source of truth
- cache key and namespace
- freshness policy
- invalidation trigger
- miss behavior
- stale behavior
- ownership of serialization

## Invariants

- A cache never becomes an accidental source of truth.
- Keys include every dimension that changes authorization or meaning, such as tenant and locale.
- Writes cannot silently leave security-sensitive cached data visible to the wrong principal.
- TTL is not a substitute for correctness when stale data can violate a business invariant.

## Strategies

**Cache-aside:** application reads cache, falls back to the source, then populates cache. Simple and common, but invalidation is the application's responsibility.

**Write-through:** writes update cache and source together through a coordinated abstraction. Useful when read-after-write behavior matters, but adds complexity.

**Event-driven invalidation:** a successful source change emits an event that invalidates or refreshes derived entries. Scales well across services but introduces delivery lag and failure handling.

## Failure modes

- cache stampedes on hot misses
- stale authorization data
- unbounded keys and memory growth
- deleting a key before a transaction commits
- inconsistent cache updates across services
- negative caching hiding newly created resources
- using local process caches when shared consistency is required

## Implementation choices

For hot keys, use TTL jitter, request coalescing, stale-while-revalidate, or bounded refresh work. Treat serialization formats as contracts and version keys when schemas change.

For database-backed applications, decide whether invalidation happens after commit, through an outbox event, or through a synchronous write path. Never assume an event was delivered merely because a database transaction committed.

## Security

Authorization-sensitive cache entries need identity/tenant-aware keys or a policy that guarantees the cached representation is safe for all readers. Never cache secrets or private responses in shared layers accidentally.

## Performance

Measure hit ratio, miss latency, backend load, eviction rate, memory use, and hot-key concentration. A cache that increases tail latency during stampedes is not a successful cache.

## Operational signals

Alert on abnormal miss rates, eviction pressure, backend saturation, stale-data incidents, and invalidation lag. Make cache bypass and safe degradation possible for incident response.
