# PostgreSQL

**Role:** Primary | **Layer:** Data

## Mental model
PostgreSQL is a relational database built around tables, constraints, MVCC transactions, indexes, a query planner and durable storage.

## Learn
- SQL and relational modeling
- primary/foreign/unique/check constraints
- B-tree, GIN and other indexes
- joins, CTEs and window functions
- transactions and isolation levels
- MVCC, locks and deadlocks
- query planning and `EXPLAIN`
- connection pooling and replication
- JSONB and extensions

## Production
Let the database enforce invariants, use parameterized queries, keep transactions short, inspect slow plans, size pools with total connection capacity in mind, and design indexes from actual access patterns.

## Scaling
Use read replicas carefully, partition only when justified, archive cold data, and understand that replication lag changes read semantics.

## Related
SQLAlchemy, Drizzle/Prisma, Redis, pgvector, OpenSearch.
