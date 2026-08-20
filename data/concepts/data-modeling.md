# Data Modeling

Data modeling is the translation between a domain and the state required to serve its access patterns.

## Mental model

```text
Domain
  ↓
Entities + relationships
  ↓
Invariants
  ↓
Access patterns
  ↓
Schema
  ↓
Indexes
  ↓
Queries / transactions
```

The critical mistake is designing tables first and queries later. Start from the behavior the system must support.

## Core concepts

### Entity
A thing with identity and lifecycle.

Examples: User, Organization, Invoice, Order.

### Relationship
A semantic connection between entities.

- one-to-one
- one-to-many
- many-to-many

### Invariant
A condition that must remain true.

Examples:

- an email is unique within an account system
- an order cannot have two active payments
- a balance cannot become negative unless overdraft is explicitly supported

## Relational modeling

Prefer normalized models when multiple records share independently changing facts. Denormalize only for a measured access-pattern reason.

Typical sequence:

```text
users
organizations
organization_members
orders
order_items
payments
```

Use primary keys for identity, foreign keys for referential integrity, unique constraints for business invariants, and check constraints for local validity.

## Access-pattern thinking

Before adding an index, write the queries that matter.

```sql
SELECT *
FROM orders
WHERE customer_id = $1
  AND created_at >= $2
ORDER BY created_at DESC
LIMIT 50;
```

The corresponding index may be:

```sql
CREATE INDEX idx_orders_customer_created
ON orders (customer_id, created_at DESC);
```

Index design depends on predicate order, cardinality, ordering, write cost, and query shape.

## Normalization vs denormalization

Normalization reduces duplicated state and update anomalies.

Denormalization can reduce joins or improve read latency, but creates consistency responsibilities.

Use denormalization when the read path is important enough to justify the additional synchronization burden.

## Deletion strategy

Choose explicitly:

- hard delete
- soft delete
- archival
- retention-based deletion

Do not use soft delete automatically. It complicates uniqueness, indexing, joins, and operational cleanup.

## Production checklist

- identify invariants
- identify hot access paths
- define transaction boundaries
- define retention and deletion behavior
- test representative query plans
- estimate row growth
- define backup and recovery expectations
- document deliberately denormalized fields

## Connects to

`postgresql.md`, `redis.md`, `data-consistency.md`, `backend/service-architecture.md`, and `production/reliability.md`.
