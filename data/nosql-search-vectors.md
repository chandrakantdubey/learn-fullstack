# NoSQL, Search, and Vector Data

Do not choose a data store from fashion. Choose it from access patterns, consistency requirements, workload shape, and operational constraints.

## Document databases

MongoDB and similar document stores fit workloads where documents map naturally to the application aggregate and schema flexibility is useful.

Understand:

- embedded vs referenced data
- document boundaries
- indexes
- aggregation
- atomicity boundaries
- transactions and their limits
- denormalization for read patterns

## Search engines

OpenSearch/Elasticsearch are specialized retrieval systems, not substitutes for the transactional database.

Mental model:

```text
PostgreSQL
   │ source of truth
   └── change / indexing pipeline
             ↓
       Search index
             ↓
       query + ranking
```

Understand:

- inverted indexes
- analyzers/tokenization
- full-text matching
- filters vs scoring
- relevance
- aggregations
- indexing latency
- refresh behavior
- shard/replica concepts

## Vector search

Use vectors when semantic similarity is part of the product behavior.

Understand:

- embeddings
- cosine/dot-product/distance concepts
- nearest-neighbor search
- ANN
- HNSW
- metadata filtering
- hybrid lexical + semantic retrieval
- reranking
- chunking and retrieval quality

Prefer **pgvector first** when PostgreSQL is already the operational center and the scale/workload fits. Introduce a dedicated vector system when workload or operational needs justify the added system.

## Retrieval architecture

```text
User query
   ↓
Query normalization
   ↓
Lexical / vector retrieval
   ↓
Metadata filters
   ↓
Reranker (optional)
   ↓
Context construction
```

## Failure modes

- stale index
- missing documents
- poor chunk boundaries
- embedding/model mismatch
- low recall
- noisy metadata filters
- vector index memory pressure
- unbounded context construction

## Design rule

Keep the transactional database authoritative unless the search/vector store is explicitly the source of truth for that workload. Treat derived indexes as rebuildable.
