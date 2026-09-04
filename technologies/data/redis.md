# Redis

**Role:** Primary | **Layer:** Data/cache/messaging

## Mental model
Redis is an in-memory data structure server commonly used for caching, counters, ephemeral state, rate limiting and queue-like coordination.

## Learn
- strings, hashes, lists, sets, sorted sets
- TTL and eviction
- atomic commands and transactions
- Lua/scripts and server-side operations
- pub/sub and streams
- persistence and replication
- clustering

## Production
Treat cached data as reconstructible unless explicitly designed otherwise. Bound TTLs and memory, design stampede protection, understand eviction policy, and never rely on fragile distributed locks without understanding failure semantics.

## Related
PostgreSQL, Celery, BullMQ, rate limiting, caching.
