# Fullstack + AI Engineering Skill Map

This is the integrated skill map for the nine-repository learning system. `learn-dsa` is complete. The other specialized repositories remain deep sources; `learn-fullstack` owns synthesis, cross-layer engineering, architecture and gaps that do not belong naturally to one source.

## 0. Programming foundations

- variables, values, references and mutability
- expressions, control flow and functions
- collections and data modeling
- recursion and iteration
- errors and exception boundaries
- modules, packages and dependency boundaries
- generics and type systems
- runtime vs compile-time guarantees
- regular expressions
- parsing vs validation
- Unicode, normalization, strings and graphemes
- bytes, encodings, base64 and serialization
- hashing, checksums and content addressing
- randomness and secure randomness
- floating point, precision and money
- dates, time zones and monotonic clocks
- resource ownership and cleanup
- DSA and complexity through `learn-dsa`

## 1. Web platform

- HTML semantics and accessibility
- CSS layout, cascade and rendering
- DOM and Web APIs
- browser architecture
- rendering pipeline and main-thread work
- storage and browser lifecycle
- same-origin policy
- CORS
- CSP
- cookies and sessions
- CSRF and XSS
- HTTP semantics
- HTTP caching and conditional requests
- DNS
- TCP/UDP/QUIC
- TLS and certificate trust
- proxies and load balancers
- HTTP/2 and HTTP/3 concepts
- streaming responses
- SSE and WebSockets
- uploads/downloads

## 2. Frontend engineering

**Primary:** TypeScript → React → Next.js

- component architecture and composition
- rendering/reconciliation
- server/client boundaries
- data fetching and mutations
- client state vs server state
- forms and validation
- accessibility
- performance and Core Web Vitals
- caching and invalidation
- optimistic UI
- error/loading/empty states
- authentication UX without trusting the client for authorization
- frontend testing
- observability and production debugging
- Tailwind CSS, Radix UI, shadcn/ui
- Zustand, TanStack Query, React Hook Form
- Vite, pnpm, Vitest, Playwright

## 3. Backend and API engineering

**Primary:** Python/FastAPI and TypeScript/Node.js/Fastify

- HTTP/API semantics
- REST, OpenAPI, GraphQL and gRPC awareness
- API contracts and schema evolution
- DTO vs domain model
- validation and business invariants
- error contracts
- authentication and authorization
- OAuth/OIDC mental model
- sessions and token lifecycle
- pagination/filtering/sorting
- idempotency
- rate limiting
- timeouts/deadlines
- retries and retry storms
- cancellation
- background jobs
- queues and event-driven architecture
- modular monoliths and service boundaries
- dependency isolation
- graceful shutdown

## 4. Data engineering

- relational modeling
- SQL
- PostgreSQL
- transactions
- isolation and MVCC
- locks and contention
- indexes and query planning
- connection pooling
- migrations
- JSON/JSONB
- replication and partitioning concepts
- Redis and cache design
- cache invalidation/TTL/eviction
- MongoDB document-model awareness
- search/OpenSearch concepts
- vectors/embeddings/pgvector
- data lifecycle and schema evolution
- backups, restore and recovery

## 5. Distributed systems

- network failure and partial failure
- consistency models
- availability/capacity trade-offs
- queues vs streams
- Kafka
- SQS/EventBridge
- ordering and partitioning
- delivery semantics
- deduplication
- consumer groups
- backpressure
- load shedding
- idempotent consumers
- outbox/inbox patterns
- sagas/workflows
- circuit breakers
- bulkheads
- replication/sharding
- eventual consistency

## 6. Systems and operating environment

- Linux and shell
- processes and threads
- virtual memory
- filesystems and file descriptors
- event loops
- concurrency and synchronization
- CPU vs I/O workloads
- resource limits
- signals and process lifecycle
- graceful shutdown
- profiling
- CPU/memory/network/disk saturation
- container runtime mental model

## 7. Infrastructure and cloud

- Docker
- image layers and registries
- container networking/storage
- Docker Compose
- Kubernetes primitives
- scheduling, probes and resources
- deployments and rollouts
- Helm
- AWS fundamentals
- VPC/networking
- IAM
- secrets management
- Terraform/IaC
- GitHub Actions
- CI/CD
- environments and configuration

## 8. Production engineering

- threat modeling
- OWASP classes
- cryptography fundamentals
- secure password/session/token design
- secret/key lifecycle
- least privilege
- supply-chain security
- testing pyramid and test boundaries
- unit/integration/contract/E2E tests
- load testing
- observability
- logs, metrics and traces
- OpenTelemetry
- Prometheus/Grafana
- SLIs/SLOs/error budgets
- capacity planning
- incident response
- graceful degradation
- feature flags
- backups/restore
- RPO/RTO
- rollback and recovery

## 9. Architecture and system design

- requirements and constraints
- domain boundaries
- modular monolith vs services
- API/gateway/BFF patterns
- data ownership
- synchronous vs asynchronous flows
- transaction boundaries
- consistency choices
- caching architecture
- search architecture
- messaging architecture
- multi-region concepts
- scalability and capacity
- reliability and failure isolation
- security architecture
- observability architecture
- cost modeling
- migration strategy
- architectural trade-offs

## 10. AI/ML engineering

- AI/ML fundamentals
- classical ML
- neural networks
- deep learning
- NLP
- tokenization
- embeddings
- attention
- transformers
- language models
- LLMs
- inference
- prompting
- structured outputs
- tool calling
- fine-tuning
- LoRA/QLoRA
- distillation
- RAG
- chunking/retrieval/reranking
- evaluation
- guardrails
- prompt injection
- agents and deterministic workflows
- MCP
- model routing
- inference serving
- latency/cost/capacity
- AI observability

## Cross-layer engineering rule

For every important capability, understand:

```text
problem
 ↓
mental model
 ↓
constraints / invariants
 ↓
trust boundary
 ↓
API / data contract
 ↓
implementation
 ↓
failure modes
 ↓
security
 ↓
performance / scale
 ↓
observability
 ↓
testing
 ↓
production operation
```

Technology is the implementation choice, not the mental model.

See [`docs/module-map.md`](module-map.md) and [`docs/cross-cutting-gaps.md`](cross-cutting-gaps.md) for ownership and missing-topic tracking.
