# Production Project Build Playbook

This document turns the ten project specifications into executable engineering work. It is intentionally not a tutorial. Each project is a system boundary exercise with explicit proof requirements.

## Universal project contract

Every project follows the same lifecycle:

```text
Requirements
→ workload + invariants
→ architecture
→ contracts + schema
→ smallest vertical slice
→ tests
→ observability
→ failure injection
→ security verification
→ load/capacity test
→ deployment
→ rollback/recovery
→ architecture defense
```

Do not add infrastructure before the failure mode or workload requires it.

## Evidence directory

For each project keep:

```text
docs/
  requirements.md
  architecture.md
  adr/
  threat-model.md
  api-contract.md
  events.md
  data-model.md
  failure-tests.md
  load-test.md
  runbook.md
  rollback.md
  recovery.md
  cost-model.md
```

## Project 1 — Multi-tenant SaaS

### Build slices

1. identity and tenant membership
2. protected CRUD with server-side authorization
3. PostgreSQL invariants and migrations
4. Redis cache with explicit invalidation
5. audit trail
6. frontend loading/error/optimistic states
7. E2E critical path
8. production telemetry and deployment

### Hard invariants

- a user can access only resources belonging to an authorized tenant;
- membership changes are transactional;
- duplicate mutations do not create duplicate business effects;
- audit records identify actor, action and resource.

### Break tests

IDOR, cross-tenant IDs, expired session, duplicate mutation, stale cache, DB timeout, Redis outage, partial frontend mutation.

### Defense

Explain shared-schema tenancy, authorization placement, cache keys, transaction boundaries and session/token trade-offs.

## Project 2 — Realtime Collaboration

### Build slices

1. HTTP bootstrap and authorization
2. authenticated realtime connection
3. durable document state
4. ephemeral presence
5. reconnect/resynchronization
6. multi-instance fan-out
7. slow-consumer handling
8. browser failure states

### Hard invariants

- unauthorized users never receive protected events;
- durable state remains authoritative;
- reconnecting clients converge to an accepted state;
- slow consumers cannot exhaust server resources.

### Break tests

Disconnect during mutation, duplicate event, out-of-order delivery, reconnect storm, server restart, slow consumer, Redis/pub-sub failure.

### Defense

WebSocket vs SSE, presence vs durable state, ordering guarantees and backpressure strategy.

## Project 3 — Event-Driven Order Platform

### Build slices

1. order API + transactional database state
2. outbox writer
3. publisher
4. idempotent consumers
5. retry/DLQ
6. downstream side effect
7. reconciliation job
8. tracing across async boundaries

### Hard invariants

- an order cannot enter an invalid state;
- a downstream side effect is idempotent;
- a committed business state cannot depend on an uncommitted event;
- failed messages remain diagnosable and recoverable.

### Break tests

DB commit before publish, publish duplication, consumer crash after effect, poison message, downstream timeout and queue backlog.

### Defense

Outbox vs direct publish, partition key, ordering, delivery semantics and why “exactly once” is usually an application property rather than a magical transport guarantee.

## Project 4 — Search Platform

### Build slices

1. canonical relational source
2. index document mapping
3. ingestion worker
4. query API
5. ranking/filtering/pagination
6. index versioning
7. zero/low-downtime reindex
8. reconciliation and recovery

### Hard invariants

The source of truth remains authoritative; search is derived state and may have bounded staleness.

### Break tests

Partial batch, stale document, failed reindex, incompatible mapping, hot query and index outage.

### Defense

PostgreSQL full-text search vs dedicated search, ranking trade-offs, consistency expectations and alias/version strategy.

## Project 5 — AI Knowledge Assistant

### Build slices

1. authenticated document upload
2. parsing and normalized representation
3. chunking + provenance
4. embeddings + pgvector
5. authorization-aware retrieval
6. reranking/context construction
7. model response + citations
8. browser streaming
9. evaluation dataset + regression gate
10. cost/latency telemetry

### Hard invariants

- retrieval cannot cross tenant/resource boundaries;
- model context contains only authorized material;
- every citation maps to known source provenance;
- model output is not treated as authoritative business state.

### Break tests

Cross-tenant retrieval, malicious document instructions, stale index, empty retrieval, embedding failure, provider timeout, high-token query.

### Defense

Chunking strategy, lexical/vector/hybrid retrieval, reranking, retrieval metrics, fallback behavior and cost-quality trade-offs.

## Project 6 — Agentic Operations Assistant

### Build slices

1. authenticated conversation
2. explicit workflow/state model
3. read-only tools
4. validated tool arguments
5. policy authorization
6. approval gate
7. idempotent side-effect tool
8. budgets and loop limits
9. audit trail
10. trajectory evaluation

### Hard invariants

- the model cannot grant itself permission;
- every side effect passes deterministic authorization;
- high-impact operations require explicit approval;
- execution is bounded by time, iterations and cost.

### Break tests

Prompt injection, unsafe arguments, repeated calls, stale state, partial execution, timeout and approval expiration.

### Defense

Agent vs workflow, autonomy boundaries, tool contracts, approval policy and why deterministic control belongs outside the model.

## Project 7 — Background Job Platform

### Build slices

1. job submission API
2. durable queue state
3. worker lease/claim
4. heartbeat and timeout
5. retry policy
6. deduplication
7. concurrency limits
8. DLQ/replay
9. graceful shutdown
10. queue-age telemetry

### Hard invariants

A job must have an observable state and safe recovery path even when a worker dies at any point in execution.

### Break tests

Crash after side effect, duplicate delivery, stuck worker, queue overload, dependency outage and lease expiration.

### Defense

Lease/visibility semantics, fairness, backpressure, retry storms and idempotent job design.

## Project 8 — Media/File Processing Pipeline

### Build slices

1. authenticated upload intent
2. direct object-storage upload
3. metadata/status record
4. processing job
5. streaming processor
6. validation/scanning boundary
7. progress/status API
8. cleanup/retention
9. retry/recovery

### Hard invariants

Untrusted file bytes never become executable or trusted merely because upload succeeded. Processing state is durable and auditable.

### Break tests

Oversized file, misleading content type, malformed input, abandoned upload, duplicate job, worker crash and storage outage.

### Defense

Direct-to-storage vs proxy, streaming vs buffering, retention and isolation strategy.

## Project 9 — High-Throughput URL Service

### Build slices

1. URL creation with idempotency
2. redirect read path
3. Redis cache
4. rate limiting
5. hot-key protection
6. async analytics
7. load test
8. capacity model

### Hard invariants

A redirect lookup should remain cheap and predictable under read-heavy traffic; analytics must not block the redirect path.

### Break tests

Cache outage, hot key, duplicate creation, analytics backlog and DB saturation.

### Defense

Cache consistency, hot-key mitigation, read/write scaling, rate-limit placement and cost model.

## Project 10 — Production AI Application Platform

### Build slices

1. multi-tenant identity and authorization
2. document ingestion pipeline
3. RAG retrieval with ACL filtering
4. model gateway/provider routing
5. bounded tool workflow
6. streaming UI
7. evaluation/regression pipeline
8. token/cost accounting
9. OpenTelemetry traces and production metrics
10. containerized deployment
11. progressive release
12. rollback and recovery

### Hard invariants

- authorization is enforced independently of the model;
- tool side effects require deterministic policy checks;
- retrieval respects tenant/resource scope;
- AI quality is measured with task-specific evaluations;
- provider failures degrade predictably;
- model spend is bounded and attributable.

### Break tests

Provider outage, retrieval outage, queue backlog, model latency spike, cross-tenant access attempt, prompt injection, unsafe tool call and runaway cost.

### Defense

Explain the complete browser→API→data→AI→telemetry path, model/provider abstraction, RAG boundaries, agent controls, SLOs, capacity, cost and when the architecture should be simplified or split.

## Portfolio execution order

Do not build all ten simultaneously.

```text
01 → 02 → 03 → 07 → 08 → 09 → 04 → 05 → 06 → 10
```

This order moves from request/data fundamentals into async systems, then high-throughput and search, then AI retrieval and agents, and finally the integrated platform.

Projects 1 and 2 establish the fullstack baseline. Projects 3, 7, 8 and 9 establish production systems judgment. Projects 4–6 establish search/AI specialization. Project 10 is the final synthesis.

## Promotion rule

After each project, record:

```text
what failed
why it failed
what evidence exposed it
what changed
what trade-off was accepted
what remains unknown
```

A project is promoted to portfolio-quality only when its evidence satisfies the production verification playbook. Do not mark a project complete from a README or passing happy-path tests alone.
