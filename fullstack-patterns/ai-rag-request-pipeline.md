# AI / RAG Request Pipeline

LLM features should be treated as probabilistic components inside deterministic application boundaries.

## Boundary

```text
browser
 → authenticated API
 → tenant/user policy
 → request validation + budget
 → retrieval / tools
 → prompt assembly
 → model inference
 → output validation
 → domain action or response
 → telemetry + evaluation
```

## Invariants

- The model is never the authority for identity or permissions.
- Retrieval is filtered by the caller's authorization scope.
- Tool arguments are validated before execution.
- External content is treated as untrusted data and cannot directly redefine system policy.
- Model output is not trusted merely because it is syntactically valid.
- Latency, token, and monetary budgets are explicit.

## RAG lifecycle

1. Ingest documents with ownership and source metadata.
2. Normalize and chunk according to retrieval needs.
3. Generate embeddings and store searchable representations.
4. Retrieve candidates using tenant-aware filters.
5. Optionally rerank or compress context.
6. Assemble a bounded prompt.
7. Generate an answer with citations or source references where appropriate.
8. Evaluate retrieval and answer quality independently.

## Implementation choices

Keep deterministic application state outside the model. Use explicit workflow/state-machine code for policies that must be reliable. Use tool schemas and runtime validation at every tool boundary.

Streaming to the browser requires cancellation propagation: if the client disconnects, downstream model work should stop where possible.

Provider routing should consider reliability, latency, capability, privacy, and cost rather than blindly retrying one provider.

## Failure modes

- cross-tenant retrieval
- prompt injection from documents or tool results
- tool misuse through malicious model arguments
- context windows exceeded
- hallucinated authorization or business state
- retries multiplying model spend
- no evaluation dataset
- model/provider outage taking down the whole application

## Security

Defend against prompt injection, data exfiltration, SSRF through tools, malicious documents, unsafe code/tool execution, and telemetry leakage. Require explicit approval for high-impact actions.

## Performance

Measure retrieval latency, candidate counts, reranking cost, input/output tokens, time to first token, total generation latency, cache hit rate, and provider error rate. Bound context size and tool fan-out.

## Operational signals

Track model availability, token spend, latency, retrieval quality, groundedness/answer quality, tool failures, safety blocks, fallback usage, and user-visible task success.

## Related technologies

Canonical technology notes live under `technologies/ai/` for providers, embeddings, Transformers, LangGraph, Langfuse, vLLM, and related infrastructure. This pattern owns the cross-layer architecture, not vendor APIs.
