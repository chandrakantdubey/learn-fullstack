# sentence-transformers

**Role:** Primary | **Layer:** AI/embeddings

## Mental model
Sentence Transformers packages encoder models and pooling strategies for producing dense representations where semantic relationships can be measured with vector similarity.

```text
text -> tokenizer -> encoder -> token representations
                                  |
                               pooling
                                  |
                              embedding
```

## Embedding fundamentals
Understand embedding dimensions, normalization, pooling, similarity metrics and model-specific training objectives. Embeddings are not universal semantic truth; quality depends on domain, language, model and query distribution.

## Retrieval
A typical semantic-search path is:

```text
query -> embedding -> vector search -> candidate set -> optional rerank
```

Use a representative evaluation set to measure recall and relevance rather than judging by a few visually plausible results.

## Model selection
Consider language coverage, domain fit, vector dimension, latency, licensing, hardware requirements and benchmark results. Record the exact model revision in persisted metadata.

## Batching
Batch encoding requests when throughput matters. For online traffic, balance batch wait time against throughput and tail latency.

## Fine-tuning
Understand contrastive learning and pair/triplet-style objectives at a conceptual level. Fine-tuning retrieval models requires representative positive/negative examples and a reliable evaluation set.

## Production patterns
- Store model ID/version with vectors.
- Keep dimensions and distance metrics explicit.
- Batch offline ingestion.
- Rate-limit online embedding work.
- Cache repeated embeddings where useful.
- Re-embed through a versioned migration when changing models.
- Monitor embedding latency and failure rate.

## Security
Do not embed sensitive data into systems without understanding retention, access and downstream exposure. Vector stores can leak information even when raw text is not directly returned.

## Testing
Evaluate retrieval separately from generation. Maintain known relevant documents per query and measure recall@k, MRR or other task-appropriate metrics.

## Common mistakes
- mixing models in one index
- ignoring model versioning
- using cosine similarity without understanding normalization/model behavior
- evaluating only generated answers
- embedding excessively large chunks
- assuming higher dimensions always mean better retrieval

## Interview-level topics
Encoder vs generative models, pooling, vector dimensions, cosine similarity, contrastive learning, batching, model versioning and retrieval evaluation.

## Related
pgvector, Hugging Face Transformers, RAG, OpenAI SDK.