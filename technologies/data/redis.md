# Redis

**Role:** Primary | **Layer:** Data/cache/coordination

## Mental model
Redis is an in-memory data structure server optimized for very low-latency operations. In application architecture it is commonly a cache, counter store, ephemeral state store, rate limiter or coordination primitive—not a universal replacement for PostgreSQL.

## Data structures
Know strings, hashes, lists, sets, sorted sets, streams and key expiration. Choose structures based on access pattern rather than familiarity.

## TTL and eviction
TTL makes ephemeral data self-cleaning. Eviction policies determine what happens under memory pressure. Design keys and values with bounded size and predictable lifecycle.

## Atomicity
Individual Redis commands are atomic. Transactions and Lua/server-side operations can group logic, but they are not equivalent to a relational transaction across Redis and PostgreSQL.

## Caching
A production cache needs:
- key design
- TTL policy
- invalidation strategy
- serialization format
- stampede protection
- negative caching where appropriate
- authorization-aware key scope

```text
request -> cache lookup -> hit
                    |
                    +-> miss -> source of truth -> populate cache
```

The source of truth must remain clear.

## Rate limiting
Counters with expiry can implement simple fixed-window limits. More accurate algorithms include sliding windows or token buckets. Distributed rate limiting must account for shared state, clock behavior and failure semantics.

## Streams and messaging
Redis Streams provide append-oriented consumer-group semantics. They can be useful for bounded workloads, but do not automatically replace a dedicated durable event-streaming platform.

## Persistence and durability
Understand RDB snapshots, AOF, replication and failover. If data cannot be reconstructed, treat durability and recovery as first-class requirements rather than assuming "Redis" means disposable.

## Distributed locks
Locks are deceptively hard. Lease expiry, client pauses, network partitions and ownership ambiguity can produce incorrect assumptions. Never use a Redis lock as the sole correctness mechanism for critical state without a design that explicitly handles failure.

## Production patterns
- Bound memory and value sizes.
- Set TTLs for ephemeral data.
- Monitor hit rate, memory, evictions, latency and connection counts.
- Use connection pooling appropriately.
- Prevent cache stampedes with jitter, request coalescing or stale-while-revalidate patterns.
- Keep cache keys tenant/user scoped when authorization requires it.
- Treat cache misses as normal behavior.

## Performance
Track p50/p95/p99 latency, commands/sec, memory fragmentation, hit rate and network overhead. Large values can make a low-latency datastore behave poorly due to serialization and transfer costs.

## Failure modes
Design for cache outage, partial connectivity, stale values, evictions, failover and hot keys. A cache should not turn a database outage into a total application outage through synchronized retries.

## Security
Require authentication, restrict network access, encrypt traffic where appropriate, avoid storing secrets unnecessarily and never expose an administrative Redis endpoint publicly.

## Testing
Integration-test cache behavior with a real Redis instance when commands, TTLs or scripts matter. Test degraded behavior with cache unavailable.

## Common mistakes
- using Redis as an accidental source of truth
- unbounded keys/values
- no TTL on ephemeral data
- cache keys that ignore tenant/auth scope
- unbounded retries after Redis failure
- assuming distributed locks are automatically safe

## Interview-level topics
Data structures, TTL/eviction, atomicity, persistence, replication, streams, cache-aside, stampede prevention, hot keys, rate limiting and distributed lock failure modes.

## Related
PostgreSQL, Celery, BullMQ, Kafka, caching and rate limiting.