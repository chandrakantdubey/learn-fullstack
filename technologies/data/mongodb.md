# MongoDB

**Role:** Awareness | **Layer:** Data

## Mental model
MongoDB is a document database that stores JSON-like documents and provides indexed queries, aggregation and replication.

## Learn
- document modeling and embedding/reference tradeoffs
- indexes and query plans
- aggregation pipelines
- atomic document updates
- transactions
- replication and sharding

## Production
Model around access patterns, bound document size and index count, inspect query plans, understand consistency/read concerns, and avoid choosing a document database simply to avoid relational modeling.

## Tradeoff
MongoDB can be a strong fit for document-shaped data with evolving schemas; PostgreSQL is generally the primary relational choice in this repository when transactions and relational constraints dominate.
