# pgvector

**Role:** Primary | **Layer:** Data/AI

## Mental model
pgvector adds vector columns and similarity search to PostgreSQL. This lets embeddings live beside relational metadata, permissions and transactional records.

```text
text -> embedding model -> vector
                         |
                         v
PostgreSQL row: metadata + vector
                         |
                         v
similarity search + relational filtering
```

## Vector fundamentals
A vector is a numeric representation produced by an embedding model. Its dimension and semantic behavior are determined by the model. Vectors from incompatible models should not be mixed casually.

## Similarity
Know cosine distance, inner product and Euclidean distance conceptually. The metric must match how the embedding model was trained and how relevance is evaluated.

## Exact vs approximate search
Exact search compares candidates directly and provides high recall at increasing computational cost. Approximate nearest-neighbor indexes trade some recall for speed at scale.

## HNSW and IVFFlat
Understand the architectural trade-off:
- HNSW builds a navigable graph and generally provides strong query performance/recall trade-offs.
- IVFFlat partitions vectors into lists and requires training/build considerations.

Do not choose an index by popularity alone. Benchmark on your corpus and query distribution.

## Retrieval with filters
RAG retrieval usually needs both semantic similarity and authorization/metadata constraints. A vector that is semantically relevant but belongs to another tenant is not a valid result.

Design indexes and query shapes around actual filter selectivity.

## RAG architecture
```text
ingestion
  -> parse
  -> chunk
  -> metadata
  -> embed
  -> store

query
  -> normalize/rewrite
  -> embed
  -> retrieve
  -> filter/rerank
  -> context assembly
  -> model
  -> answer/evaluation
```

The vector index is only one component of this pipeline.

## Production patterns
- Store embedding model/version with data.
- Keep dimensions explicit.
- Re-embed through a versioned migration pipeline when models change.
- Benchmark recall@k, precision/relevance and latency.
- Apply tenant/ACL filters as part of retrieval correctness.
- Keep chunk identity and source metadata for citations/debugging.
- Monitor index size and build time.

## Performance
Measure query latency, candidate counts, recall, index build time, memory and database CPU. Tune retrieval count and reranking separately. Increasing `k` blindly can increase model context cost and latency without improving answer quality.

## Failure modes
Watch for stale embeddings, wrong model/dimension, missing metadata, weak chunks, permission leaks, low recall and index configuration that works in a small development dataset but collapses at production scale.

## Testing and evaluation
Maintain a representative retrieval dataset with known relevant documents. Test retrieval independently from generation. A good generation model cannot compensate for systematically missing evidence.

## Security
Treat document metadata and retrieved text as untrusted content. Enforce authorization before context reaches the model. Retrieval must not become a data-exfiltration path across tenants.

## Common mistakes
- treating vector similarity as truth
- skipping metadata/ACL filters
- mixing embedding models
- changing chunking without re-evaluation
- evaluating only final generated answers
- increasing `k` instead of improving retrieval quality

## Interview-level topics
Embedding dimensions, similarity metrics, ANN search, HNSW/IVFFlat, filtering, recall/latency trade-offs, re-embedding migrations, multi-tenancy and RAG evaluation.

## Related
PostgreSQL, sentence-transformers, Hugging Face Transformers, OpenAI SDK, RAG.