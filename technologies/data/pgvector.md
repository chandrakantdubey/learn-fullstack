# pgvector

**Role:** Primary | **Layer:** Data/AI

## Mental model
pgvector adds vector storage and similarity search to PostgreSQL, allowing embeddings and relational metadata to live under one transactional system.

## Learn
- vector types and distance functions
- exact vs approximate search
- HNSW and IVFFlat concepts
- filtering with relational predicates
- index sizing and recall/latency tradeoffs
- embedding dimensions and model compatibility

## Production
Choose embedding models deliberately, version embedding pipelines, filter before/with retrieval where possible, benchmark recall and latency on real data, and re-embed safely when models change.

## RAG role
A vector database is only one retrieval component. Good RAG also needs chunking, metadata, query transformation, ranking, access control, freshness and evaluation.

## Related
PostgreSQL, sentence-transformers, RAG, OpenAI SDK.
