# PostgreSQL

PostgreSQL is the canonical relational database for this repository. The goal is not to memorize SQL syntax; it is to understand how relational data behaves under real application workloads.

## Mental model

An application turns business state into rows and relationships. PostgreSQL provides constraints, transactions, indexing, query planning, concurrency control, durability, and recovery around that state.

```text
Application
   ↓
Connection Pool
   ↓
SQL / Driver
   ↓
PostgreSQL
   ├── Planner / Executor
   ├── MVCC / Locks
   ├── WAL
   └── Storage
```

## What to understand

- tables, rows, columns, primary keys, foreign keys
- normalization and deliberate denormalization
- constraints: NOT NULL, UNIQUE, CHECK, FK
- joins and set-based operations
- indexes and composite indexes
- transactions and ACID
- isolation levels
- MVCC and row visibility
- locks and deadlocks
- query planning and EXPLAIN
- connection pooling
- migrations
- backups and restore
- replication and read replicas
- partitioning when data volume or retention requires it

## Indexing

An index is a data structure that trades write/storage cost for faster access patterns. Do not add indexes because a column 'might be searched'. Start from real predicates and sort orders.

For a query such as:

```sql
SELECT id, status, created_at
FROM orders
WHERE tenant_id = $1
  AND status = $2
ORDER BY created_at DESC
LIMIT 50;
```

an index such as `(tenant_id, status, created_at DESC)` may be useful because it matches the access pattern. Verify with `EXPLAIN (ANALYZE, BUFFERS)` instead of guessing.

## Transactions

Use a transaction when multiple changes must satisfy one business invariant.

```text
BEGIN
  change A
  change B
  verify invariant
COMMIT
```

The key question is not 'should this query be transactional?' but 'what must become true together?'

## Isolation and concurrency

Higher isolation can prevent anomalies but may increase contention. Learn the common anomalies:

- dirty read
- non-repeatable read
- phantom read
- lost update
- write skew

Understand PostgreSQL's MVCC model, row locks, advisory locks, deadlocks, and why retries may be required around serialization/deadlock failures.

## Application integration

### Python

Preferred baseline:

- `psycopg` for direct PostgreSQL access
- SQLAlchemy when an ORM/query abstraction is useful
- Alembic for migrations
- explicit connection pooling

### TypeScript

Preferred baseline:

- `pg` for direct driver access
- Drizzle or Prisma when the team benefits from a higher-level data layer
- migration tooling checked into the repository

The database remains the source of truth. The ORM must not hide transaction boundaries, generated SQL, or important indexes.

## Production concerns

### Reliability

- keep migrations backward compatible during rolling deploys
- use statement and transaction timeouts
- size connection pools deliberately
- monitor replication lag if using replicas
- practice restore procedures, not only backups

### Performance

Track:

- query latency
- rows scanned vs returned
- buffer hits/misses
- lock waits
- connection utilization
- transaction duration
- replication lag

### Security

- parameterized queries
- least-privilege DB roles
- secrets in a secret manager
- TLS for remote connections
- avoid exposing production DBs directly to the public network

## Design rule

**Model business invariants in the database when they must hold regardless of which application path writes the data.**

The application can enforce richer workflow rules, but uniqueness, referential integrity, and other fundamental invariants should not depend solely on application code.
