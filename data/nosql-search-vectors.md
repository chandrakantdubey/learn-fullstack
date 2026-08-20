# NoSQL, Search, and Vector Data

Use specialized data stores when the access pattern justifies them. PostgreSQL remains the default source of truth for transactional application state.

## Document databases

Document stores fit aggregates that are naturally retrieved and updated as documents, with flexible schemas and fewer relational joins.

Understand:

- embedding vs referencing
- document size limits
- secondary indexes
- consistency and transactions
- denormalization trade-offs

MongoDB is a representative technology, not a default requirement.

## Search engines

Search systems are optimized for retrieval rather than transactional truth.

Understand:

- inverted indexes
- analyzers and tokenization
- relevance scoring
- filtering vs full-text search
- facets/aggregations
- indexing pipelines
- refresh and eventual consistency

OpenSearch/Elasticsearch are representative technologies.

Typical architecture:

```text
PostgreSQL
   │
   └── change/event
          ↓
      indexing worker
          ↓
   Search index
```

The search index is normally a derived projection and can be rebuilt.

## Vector search

Vector databases store embeddings for semantic similarity retrieval.

Understand:

- embeddings
- cosine/dot-product/L2 similarity
- approximate nearest neighbors
- HNSW and index parameters
- metadata filtering
- chunking and document identity
- hybrid lexical + vector retrieval
- reranking
- freshness and deletion

Start with `pgvector` when PostgreSQL is sufficient. Use a dedicated vector system when scale, isolation, or retrieval requirements justify it.

## Production concerns

- index asynchronously where possible
- make source data authoritative
- support rebuilds
- version embedding models
- attach metadata and source identifiers
- monitor recall/latency/index size
- never treat a vector index as the only copy of business data
