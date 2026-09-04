# Master Skill Universe

This is the canonical master checklist for the nine-repository system. It is based on the original 20-section skill universe and assigns every capability to one primary repository. Specialized repositories own implementation depth; `learn-fullstack` owns cross-layer concepts, architecture, production behavior and system-design synthesis.

## 1. Computer Science / Engineering Fundamentals

**Primary:** `learn-dsa`, `learn-js-ts`, `learn-python`; synthesis in `learn-fullstack`.

- Data structures, algorithms, complexity analysis
- OOP, functional programming, design patterns, SOLID
- Clean code, clean architecture, refactoring, separation of concerns
- Concurrency, parallelism, processes, threads, async programming
- Memory management, garbage collection, runtime fundamentals
- Debugging and profiling

## 2. Networking

**Primary:** `learn-fullstack` for protocol/system concepts; implementation support from `learn-backend` and `learn-python`.

- TCP/IP, UDP, DNS, DHCP, IP/subnets, routing, NAT
- HTTP/1.1, HTTP/2, HTTP/3, TLS, QUIC
- WebSockets, SSE, gRPC, REST
- Reverse proxies, load balancing, CDN, caching, proxies
- Network security and service-to-service networking

## 3. Linux

**Primary:** `learn-fullstack` for systems mental models; `learn-docker` for container/Linux boundary.

- Linux fundamentals, shell/Bash
- Processes, threads, signals, filesystems, permissions, users/groups
- SSH, systemd, cron, networking tools, logs, package management
- Environment variables and resource management
- CPU/memory/disk troubleshooting and Linux performance
- Containers from the Linux perspective

## 4. Databases

**Primary:** `learn-sql` for relational depth; `learn-fullstack` for cross-system data architecture.

- SQL, PostgreSQL, MySQL
- Schema design, normalization, denormalization, constraints
- Transactions, ACID, isolation, MVCC, locks, deadlocks
- Indexes, B-tree, GIN/GiST, query planning, EXPLAIN/ANALYZE, optimization
- Connection pooling, replication, read replicas, partitioning, sharding, failover
- Backup/restore and migrations
- NoSQL: MongoDB, DynamoDB, document/key-value modeling, eventual consistency, CAP
- Redis: cache-aside, write-through, write-behind, TTL, eviction, locks, rate limiting, sessions, Pub/Sub, Streams
- Search: Elasticsearch/OpenSearch, full-text search, inverted indexes

## 5. Backend

**Primary:** `learn-backend`; language/runtime depth also in `learn-js-ts` and `learn-python`.

- JavaScript, TypeScript, Node.js, V8, event loop, libuv, streams, buffers, workers, clustering
- npm/pnpm and package management
- Express, Fastify, NestJS awareness
- Python, asyncio, FastAPI, Pydantic, SQLAlchemy, Alembic, httpx
- REST/RPC/GraphQL/gRPC API design
- Versioning, pagination, filtering, sorting, validation, error handling
- Idempotency, rate limiting, retries, timeouts, circuit breakers, bulkheads
- API gateways, webhooks, background jobs, file uploads, streaming APIs
- Sessions, JWT, OAuth 2.0, OIDC, RBAC, ABAC, API keys, secrets, password hashing
- Kafka, SQS, RabbitMQ, Redis Streams, queues/topics/consumer groups/order/delivery semantics/DLQs
- Event-driven architecture, event sourcing and CQRS concepts

## 6. Frontend

**Primary:** `learn-frontend`; JS/TS depth in `learn-js-ts`.

- HTML, CSS, JavaScript, TypeScript, browser APIs, DOM
- Web storage, cookies, accessibility, responsive design
- React, Hooks, Context, rendering, reconciliation, component architecture
- State management, performance, Suspense, error boundaries, Server Components
- Next.js App Router, SSR, SSG, ISR, Server Actions, streaming, RSC
- TanStack Query, Zustand, Zod, Redux Toolkit awareness, Tailwind CSS, Vite
- Vitest, Jest awareness, React Testing Library, Playwright
- Code splitting, lazy loading, bundles, caching, prefetching, virtualization, Core Web Vitals
- Design systems, component/feature architecture, state/API architecture, micro-frontends awareness
- Frontend security

## 7. Fullstack Engineering

**Primary:** `learn-fullstack`.

- End-to-end architecture
- Monorepos
- API contracts, type-safe APIs, shared schemas
- Authentication flows
- File handling
- Realtime and streaming applications
- Background processing
- Fullstack testing and end-to-end debugging
- Performance optimization
- Deployment and production configuration
- Environment management

## 8. AI Engineering

**Primary:** `learn-ai`; product/system synthesis in `learn-fullstack`.

- AI, ML, deep learning, neural networks
- Training vs inference, models, parameters, tokens, tokenization, embeddings, context windows
- Transformers, attention, decoder-only/GPT-style models
- Sampling, temperature, top-k/top-p, logits, KV cache, batching, quantization
- Model routing and multimodal models
- Provider APIs, open-source models, structured outputs, tool calling, streaming
- Prompt/context engineering, response validation, model selection, token/cost optimization, fallbacks and caching
- RAG: ingestion, parsing, chunking, metadata, embeddings, vector/keyword/hybrid search, reranking, context construction, citations, evaluation
- Agents: loops, planning, state, memory, permissions, human-in-the-loop, multi-agent, workflows, evaluation, reliability and cost
- Frameworks/protocols: LangChain awareness, LangGraph, provider agent SDKs, MCP, smolagents/LlamaIndex awareness
- Evaluation: golden datasets, regression, retrieval metrics, answer quality, faithfulness, relevance, judges, human evaluation, prompt/version evaluation, experiment tracking
- Observability: traces, token/latency/cost/model/retrieval/tool/prompt metrics
- AI security: prompt injection, indirect injection, jailbreaks, exfiltration, tool abuse, excessive agency, validation, PII, tenant isolation, secrets, sandboxing
- Fine-tuning, LoRA, QLoRA, PEFT, quantization, distillation, Transformers/Datasets
- Serving: vLLM, Ollama, llama.cpp awareness, GPU/CPU inference, throughput, latency, autoscaling and serving architecture

## 9. Cloud

**Primary:** `learn-fullstack` infrastructure architecture + AWS canonical technology notes; deployment mechanics in `learn-docker`.

- AWS IAM, VPC, EC2, ECS, EKS, Lambda, S3, CloudFront, Route 53, ALB, RDS, DynamoDB, ElastiCache, SQS, SNS, EventBridge, CloudWatch, Secrets Manager, KMS, ECR
- GCP fundamentals, Compute, Cloud Run, GKE, Storage, Cloud SQL, Memorystore, IAM, VPC
- Azure fundamentals, AKS, Storage, networking, identity, compute

## 10. Containers

**Primary:** `learn-docker`.

- Docker, Dockerfiles, multi-stage builds, BuildKit
- Image layers, registries, Compose
- Container networking, security and resource constraints

## 11. Kubernetes

**Primary:** `learn-docker` for operational depth; `learn-fullstack` for architecture/trade-offs.

- Architecture, Pods, Deployments, StatefulSets, DaemonSets, Jobs, CronJobs
- Services, Ingress, Gateway API
- ConfigMaps, Secrets, Volumes, PV/PVC, StorageClasses
- RBAC, ServiceAccounts, NetworkPolicies
- Probes, requests/limits, scheduling, taints/tolerations
- HPA/autoscaling, Helm, Operators, troubleshooting, security, EKS

## 12. Infrastructure as Code / DevOps

**Primary:** `learn-fullstack` architecture and production synthesis; Terraform/GitHub Actions mechanics in canonical technology notes and `learn-docker`.

- Terraform state, remote state, modules, workspaces, infrastructure design
- GitHub Actions, CI/CD, GitOps, ArgoCD awareness
- Helm, blue/green, canary, rollbacks
- Secrets management, environment promotion, release automation

## 13. Observability / SRE

**Primary:** `learn-fullstack`.

- Logging, metrics, tracing, OpenTelemetry
- Prometheus, Grafana, Loki, CloudWatch
- Alerting, SLIs, SLOs, SLAs, error budgets
- Incident response and root-cause analysis
- Capacity planning, performance/load testing, k6
- Chaos engineering, graceful degradation, disaster recovery

## 14. Security

**Primary:** `learn-fullstack` for cross-stack security; implementation depth in backend/frontend/AI/container sources.

- OWASP Top 10 and secure API design
- XSS, CSRF, CORS, SSRF, SQL injection, command injection
- Authentication and authorization, OAuth/OIDC
- Secrets management, encryption, TLS, IAM, least privilege
- Container/Kubernetes/supply-chain/dependency security
- Threat modeling and zero trust

## 15. System Design

**Primary:** `learn-fullstack`.

- Requirements and NFRs
- Capacity, throughput, latency, availability, reliability, scalability
- Monoliths, modular monoliths, microservices, service decomposition
- API gateways, load balancers, CDNs, caching, queues, events, Pub/Sub, service discovery, configuration
- Consistency, CAP, PACELC, replication, partitioning, sharding, leader/follower, quorums, locks, consensus awareness
- Idempotency, exactly-once myths, failure detection, retries, backpressure
- SQL/NoSQL/search/object/distributed storage and caching layers
- Realtime, presence, fan-out and stream processing
- Redundancy, failover, backups, DR, multi-AZ/multi-region, RPO/RTO
- AI system design: gateways, routing, RAG, agents, vector stores, evals, inference/GPU serving, prompt/version management, observability, cost and security

## 16. Architecture / Code Design

**Primary:** `learn-fullstack`; language-specific implementation in source repos.

- SOLID, design patterns, dependency injection
- Layered, hexagonal and clean architecture
- DDD concepts, modular monoliths and service boundaries
- API contracts
- Event-driven design
- CQRS, event sourcing and idempotent design

## 17. Testing / Quality

**Primary:** `learn-fullstack` for test strategy; implementation in frontend/backend/python sources.

- Unit, integration, contract, E2E and API testing
- Load/performance/security testing
- Mocking, fixtures, Testcontainers and test environments
- CI quality gates
- AI evaluation testing

## 18. Developer Tooling

**Primary:** source-specific tooling plus `learn-fullstack` integration.

- Git, GitHub, GitHub Actions
- npm/pnpm, uv/pip, virtual environments, pyproject.toml
- Linters/formatters: ESLint, Prettier, Ruff, mypy
- TypeScript compiler, Docker, Make, shell tooling

## 19. Engineering Practices

**Primary:** `learn-fullstack`.

- Code review and technical documentation
- ADRs and API documentation
- OpenAPI and versioning
- Backward compatibility and semantic versioning
- Dependency management and release management
- Incident management and technical debt management
- Observability-driven and cost-aware engineering

## 20. Interview Skills

**Primary:** `learn-fullstack` interview map, with deep practice delegated to each source; DSA is `learn-dsa`.

- DSA and coding under time pressure
- Debugging interviews
- JavaScript/TypeScript/Python/React/Node/backend/database/networking/cloud/Kubernetes/DevOps interviews
- AI/LLM, RAG and agent interviews
- AI system design and general system design
- Frontend system design
- Behavioral interviews
- Project deep dives, architecture defense and trade-off communication

## Ownership rule

Every item has one primary home. A second repository may contain an implementation-specific treatment, but the same conceptual explanation must not be duplicated unnecessarily.

**Specialized repo = depth. Fullstack = connection, architecture, production judgment, projects and verification.**

## Completion rule

A section is not considered complete merely because a keyword exists. The required bar is:

**Understand → Implement → Debug → Measure → Secure → Test → Scale → Operate → Defend trade-offs.**
