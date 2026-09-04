# AI Application Architecture

AI features are application systems with a probabilistic component. The surrounding software must provide deterministic boundaries for data, permissions, reliability and evaluation.

## Reference architecture

```text
Browser
  ↓
API / auth / tenant context
  ↓
AI application service
  ├─ prompt + model policy
  ├─ retrieval
  ├─ tools / MCP
  ├─ workflow state
  └─ output validation
       ↓
model gateway/provider/inference
       ↓
PostgreSQL / vector search / external systems
       ↓
telemetry + evaluation
```

## Model is not the authority

A model can propose text or actions. It must not decide authorization. Every protected operation must be checked by deterministic application policy.

```text
model proposal
 → schema validation
 → authenticated identity
 → authorization
 → policy/limits
 → execution
 → result validation
```

## RAG lifecycle

Production RAG is a data pipeline, not a single vector-search call:

```text
ingest
 → parse
 → normalize
 → chunk
 → embed
 → index
 → retrieve
 → rerank/filter
 → generate
 → evaluate
```

Authorization belongs in retrieval and execution paths, not only in the UI.

## Agent workflows

Prefer explicit state machines/workflows when the steps and policies are known. Give agents narrow tools, bounded iterations, timeouts, budgets and clear stop conditions.

High-impact side effects may require human approval.

## Reliability and cost

Treat model providers as remote dependencies. Set deadlines, retry only appropriate failures, control concurrency, handle rate limits and define fallbacks. Track token usage and cost per workflow/tenant where useful.

A cheaper model that materially lowers task quality is not necessarily a cheaper system.

## Streaming

Stream model output to the browser when it improves perceived latency, but preserve cancellation and authorization. Do not let abandoned streams continue unbounded inference work.

## Evaluation

Separate application tests from model evaluations:

- unit tests for deterministic logic
- integration tests for retrieval/tools/providers
- evaluation datasets for model behavior
- production metrics for latency, cost, failure and user outcomes

Version prompts, models, retrieval configuration and evaluation datasets so regressions can be attributed.

## Security

Threat-model prompt injection, sensitive-data exposure, cross-tenant retrieval, unsafe tool use, SSRF, malicious documents and telemetry leakage. Treat retrieved text and tool results as untrusted input.

## Production checklist

- Model access is behind application policy.
- Inputs and structured outputs are validated.
- Retrieval is authorization-aware.
- Tools have least privilege.
- Inference has timeouts and concurrency limits.
- Prompts/models/configuration are versioned.
- Cost and quality are observable.
- Evaluation runs in CI or release workflows where appropriate.
- Failure and fallback behavior are tested.
