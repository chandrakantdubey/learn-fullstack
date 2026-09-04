# Integrated Interview Verification Map

Interview preparation is a verification layer over the skill graph, not a separate course.

## Evaluation loop

```text
Explain → Implement → Debug → Measure → Secure → Scale → Defend
```

A candidate should be able to apply the same loop to a language feature, API, database query, distributed workflow or AI feature.

## Foundation questions

- What is a value, reference, mutation and ownership boundary?
- What does compile-time typing guarantee, and where does it stop?
- How do parsing, validation, serialization and normalization differ?
- When do bytes become text, and where can encoding fail?
- When should time use a wall clock versus a monotonic clock?
- What makes randomness suitable or unsuitable for security?
- What does hashing provide, and what does it not provide?

## Web and browser

- Walk a request from URL through DNS, transport, TLS, HTTP, proxy/load balancer and application.
- Explain HTTP caching and conditional requests.
- Explain cookies, sessions, CORS, CSRF, CSP and same-origin boundaries.
- Choose between HTTP streaming, SSE and WebSockets.
- Explain cancellation and what happens to work after a client disconnects.

## Frontend/backend

- Design an API contract that survives independent frontend/backend releases.
- Separate UI state, server state and domain state.
- Explain DTO versus domain model and validation at trust boundaries.
- Design pagination, errors, mutations and idempotency.
- Explain SSR, hydration, streaming and client/server boundaries.

## Backend and distributed systems

- Design request deadlines, retries and backoff without amplifying outages.
- Define idempotency for a mutation and show where the key is persisted.
- Compare synchronous transactions with asynchronous workflows.
- Explain at-most-once, at-least-once and effectively-once processing.
- Design an outbox and idempotent consumer.
- Explain ordering, partitioning, backpressure and load shedding.
- Identify the invariant that must remain true during partial failure.

## Data

- Design a relational schema from business invariants.
- Explain transaction isolation and a concrete anomaly each level prevents.
- Read a query plan and identify why an index is or is not useful.
- Explain connection pooling and failure behavior.
- Design cache invalidation and discuss stale data.
- Choose SQL, Redis, search and vector retrieval based on workload rather than fashion.

## Systems and infrastructure

- Explain process/thread/event-loop differences.
- Diagnose CPU, memory, I/O, network and file-descriptor saturation.
- Explain what a container isolates and what it does not.
- Design a deploy/rollback strategy.
- Explain readiness versus liveness.
- Estimate capacity and define useful SLOs.

## Security and production

- Threat-model a public API.
- Separate authentication, authorization and tenant isolation.
- Explain password hashing, encryption and signatures.
- Identify SSRF, XSS, CSRF, SQL injection, IDOR and request-smuggling risks.
- Design secrets and key rotation.
- Explain logs versus metrics versus traces.
- Walk through an incident from alert to mitigation to postmortem.

## AI engineering

- Design an AI feature as a system, not a prompt.
- Explain retrieval, chunking, embeddings, ranking and citation provenance.
- Enforce authorization before retrieval and treat model output as untrusted.
- Stream model output safely to a browser.
- Design tool execution with allowlists, validation, timeouts, budgets and approval gates.
- Define an evaluation set and regression criteria.
- Explain model/provider routing, fallback behavior, latency and cost.
- Identify prompt injection and indirect prompt injection paths.

## System-design exercises

Each exercise must include requirements, workload, data model, APIs/events, architecture, failure analysis, security, observability, capacity, cost and trade-offs.

1. Multi-tenant SaaS
2. Realtime collaboration
3. Event-driven order processing
4. Search service
5. RAG knowledge assistant
6. Agentic operations assistant
7. Background job platform
8. File/media processing pipeline
9. High-throughput URL service
10. Production AI application platform

## Senior/staff defense standard

Do not stop at “this technology is popular.” Defend:

- why this boundary exists;
- why this consistency model is sufficient;
- why this data store fits the access pattern;
- why work is synchronous or asynchronous;
- what fails first under load;
- how the system degrades;
- how operators detect and recover from failure;
- how security boundaries are enforced;
- how cost changes with traffic and model usage;
- what you would replace or simplify at the next scale.
