# OpenSearch

**Role:** Primary | **Layer:** Search

## Mental model
OpenSearch is a distributed search and analytics engine based on inverted indexes and related data structures, optimized for text search, filtering, aggregations and log analytics.

## Learn
- indexes and mappings
- analyzers/tokenization
- full-text queries
- filters and scoring
- aggregations
- shards and replicas
- refresh and consistency behavior

## Production
Design mappings deliberately, avoid unbounded field explosion, monitor shard sizes and heap, use pagination strategies suited to the workload, and distinguish search relevance from exact filtering.

## Related
PostgreSQL, logs, OpenTelemetry, RAG retrieval.
