# Data Engineering for Fullstack

The database is part of application architecture, not merely a persistence layer.

## Core areas

- Data modeling
- Relational theory
- SQL
- PostgreSQL
- Transactions and ACID
- MVCC and isolation
- Indexes and query planning
- Constraints and integrity
- Migrations
- Connection pooling
- Replication and read scaling
- Partitioning
- Caching with Redis
- Document databases
- Search systems
- Queues and event streams
- Vector search

## Default progression

```text
Data modeling
   ↓
SQL
   ↓
PostgreSQL internals
   ↓
Transactions / indexes / query plans
   ↓
Application data access
   ↓
Redis / queues / search
   ↓
Distributed data systems
```

Start with PostgreSQL. Add another database only because its data model or operational characteristics solve a real problem.
