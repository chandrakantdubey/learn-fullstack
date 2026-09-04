# PostgreSQL

**Role:** Primary | **Layer:** Data

## Mental model
PostgreSQL is a relational database where correctness comes from data modeling, constraints and transactions, while performance comes from access patterns, indexes, query planning and resource management.

```text
application
   -> connection pool
   -> transaction
   -> planner -> indexes/table access
   -> WAL/storage
   -> commit
```

## Relational modeling
Use normalized tables and explicit relationships by default. Choose primary keys deliberately, define foreign keys, unique constraints, checks and not-null requirements. Denormalize only for a measured access pattern or architectural reason.

## Transactions
Know atomicity, consistency, isolation and durability. Understand read committed, repeatable read and serializable isolation, plus how locks and MVCC interact.

A transaction should be as short as practical. Do not hold a database transaction while waiting on slow external APIs.

## MVCC and locks
PostgreSQL uses multi-version concurrency control so readers and writers can often proceed without blocking each other. Understand row locks, predicate behavior, deadlocks, lock waits and vacuum.

Deadlocks are not proof that transactions are broken; they are a signal to make lock ordering consistent and retry safe operations where appropriate.

## Indexes
Know B-tree, GIN, GiST and partial/expression indexes at a conceptual and practical level. An index is useful only when its selectivity, ordering and access pattern justify its storage and write cost.

Do not add indexes blindly. Every index affects writes, vacuum, cache pressure and storage.

## Query planner
Use `EXPLAIN` and `EXPLAIN ANALYZE` to understand scans, joins, estimates, row counts and actual timing. Bad plans often originate from inaccurate statistics, poor indexes, query shape or data distribution.

## SQL
Master joins, CTEs, window functions, aggregates, subqueries, `INSERT ... ON CONFLICT`, `RETURNING`, pagination strategies and careful NULL semantics.

Prefer keyset pagination for large ordered datasets when offset pagination becomes increasingly expensive.

## Connection pooling
A pool is a concurrency control mechanism, not simply a performance knob. Total possible connections across application replicas must fit the database's capacity. Too many connections can make a database slower, not faster.

## JSONB
JSONB is useful for bounded flexible attributes and document-like substructures, but it does not eliminate relational modeling. Index JSONB deliberately and keep core relational invariants in normal columns/constraints.

## Replication and scaling
Read replicas introduce replication lag and therefore stale-read semantics. Route reads based on correctness requirements, not merely on a desire to use replicas.

For larger systems consider partitioning, archival, logical replication, read models and workload isolation only when measured requirements justify the complexity.

## Production patterns
- Enforce critical invariants in the database.
- Parameterize queries.
- Keep transactions short.
- Set statement and lock timeouts where appropriate.
- Monitor connection usage and pool saturation.
- Monitor replication lag and vacuum health.
- Back up and regularly test restores.
- Perform migrations with lock and deployment behavior understood.

## Reliability
A backup that has never been restored is an assumption. Test recovery procedures and define RPO/RTO. Understand WAL, checkpoints, replicas and failover behavior at the level required by your operating model.

## Security
Use least-privilege database roles, TLS where required, parameterized queries, encrypted backups and controlled network access. Never put database credentials into source control or application logs.

## Testing
Use migrations in test environments, integration tests against real PostgreSQL for SQL behavior, and deterministic fixtures. Mocking SQL calls alone does not validate query correctness.

## Debugging checklist
1. Check query duration and frequency.
2. Inspect `EXPLAIN ANALYZE`.
3. Check locks and waits.
4. Check pool saturation.
5. Check cache hit behavior and I/O.
6. Check data distribution/statistics.
7. Check replication lag if replicas are involved.

## Common mistakes
- missing indexes for actual predicates
- indexes on every column
- oversized connection pools
- long transactions
- offset pagination at massive scale
- business invariants enforced only in application code
- schema changes without deployment/lock analysis
- treating replicas as strongly consistent

## Interview-level topics
MVCC, isolation levels, locking/deadlocks, indexes, query planning, WAL, vacuum, connection pooling, replication, partitioning, transactions and schema design.

## Related
SQLAlchemy, Alembic, Redis, pgvector, OpenSearch.