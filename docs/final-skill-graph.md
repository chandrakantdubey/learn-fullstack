# Final Fullstack + AI Skill Graph

This is the integration graph for the nine repositories. It is a dependency graph, not a course playlist.

## 1. Programming foundations

`values/types → control flow/functions → collections → errors/modules → runtime → testing/debugging → complexity`

Sources:
- `learn-js-ts` for JS/TS depth
- `learn-python` for Python depth
- `learn-dsa` for algorithms and interview problem solving

Cross-cutting Fullstack ownership:
- regex, parsing vs validation
- Unicode/encoding/bytes
- serialization and schema evolution
- numeric precision and money
- dates/timezones/clocks
- randomness and hashing
- cryptography
- resource ownership and cleanup

## 2. Web platform

`OS/processes → sockets → DNS → TCP/UDP/QUIC → TLS → HTTP → browser → HTML/CSS/JS → React → Next.js`

The learner should understand the mechanism before the framework.

## 3. Application boundary

`browser → request → authentication → API contract → parse → validate → authorize → domain logic → transaction → database/cache → response`

Cross-layer ownership lives in `learn-fullstack`; implementation depth returns to frontend/backend/SQL sources.

## 4. State and consistency

`database invariants → transactions/isolation → cache → jobs → queues/events → delivery semantics → idempotency → outbox/inbox → workflows → recovery`

The central question is not “which tool?” but “which invariant must remain true when something fails?”

## 5. Distributed systems

`concurrency → cancellation → backpressure → deadlines → retries → rate limits → queues/streams → ordering/deduplication → consistency → failure recovery → capacity`

Kafka, SQS, Redis and workers are implementation choices around these mechanisms.

## 6. Production engineering

`tests → logs → metrics → traces → SLOs → capacity → deployment → rollback → incident response → disaster recovery`

Security is continuous across every edge:

`identity → authorization → validation → secrets → least privilege → isolation → auditability`

Resource lifecycle is continuous too:

`startup → readiness → serve → drain → cleanup → recovery`

## 7. AI engineering

`ML foundations → neural networks → NLP → tokenization → embeddings → attention → Transformers → language models → LLMs → generative AI → inference → prompting → structured output → retrieval → RAG → tools → workflows/agents → evaluation → serving → production`

AI then joins the normal product flow:

`browser → API/auth → AI service → retrieval/tools → model/provider → validated output → persistence/events → streaming UI → telemetry/evaluation`

Deterministic application code controls identity, authorization, retrieval filters, tool permissions, budgets, state transitions, approvals and release gates.

## 8. Architecture synthesis

A senior/staff engineer must reason across:

- requirements and invariants
- API and event contracts
- frontend/backend boundaries
- BFF/gateway boundaries
- data ownership
- synchronous vs asynchronous work
- consistency and failure semantics
- security boundaries
- observability
- capacity and cost
- deployment topology
- backup/recovery and RPO/RTO
- AI quality, safety and cost

## 9. Canonical stack

### Frontend
`TypeScript → React → Next.js → TanStack Query/Zustand → React Hook Form + Zod → Playwright/Vitest`

### Backend
`TypeScript → Node.js → Fastify → OpenAPI → PostgreSQL/Redis → workers`

`Python → FastAPI → Pydantic → SQLAlchemy → PostgreSQL/Redis → workers`

### Data
`PostgreSQL → Redis → pgvector → search concepts`

### Infrastructure
`Linux → Docker → Kubernetes → AWS → Terraform → GitHub Actions`

### Production
`OpenTelemetry → Prometheus → Grafana → structured logs → k6`

### AI
`PyTorch/scikit-learn → Transformers → sentence-transformers → provider SDKs → pgvector → LangGraph where justified → Langfuse → vLLM where justified`

## 10. Mastery gate

A capability is not complete because the learner read it.

It is complete when they can:

**Explain → Implement → Debug → Measure → Secure → Test → Scale → Operate → Recover → Defend**

The strongest proof is an end-to-end production project plus an interview/system-design defense.
