# Cross-Cutting Engineering Gap List

This backlog contains knowledge that must exist in the integrated Fullstack repository because no specialized repository is the natural canonical owner.

## Closure status

The previously identified high-value cross-cutting gaps are now represented by canonical documents. This file remains an audit index, not a request to create one lesson per bullet.

## Programming and data handling

- Regular expressions and regex-engine behavior → `foundations/programming/regex.md`
- Unicode, normalization and grapheme handling → `foundations/programming/encoding-and-serialization.md`
- Bytes, encodings and base64 → `foundations/programming/encoding-and-serialization.md`
- Serialization/deserialization and schema evolution → `foundations/programming/encoding-and-serialization.md`, `architecture/frontend-backend-contracts.md`
- Floating-point behavior, precision and money representation → `foundations/programming/money-and-numeric-precision.md`
- Dates, time zones, clocks and monotonic time → `foundations/programming/time-and-randomness.md`
- Randomness and secure randomness → `foundations/programming/time-and-randomness.md`
- Hashing, checksums and content addressing → `foundations/programming/time-and-randomness.md`, `foundations/security/cryptography.md`
- Parsing vs validation → `foundations/programming/parsing-vs-validation.md`
- Resource ownership and cleanup → `systems/resource-lifecycle-and-graceful-shutdown.md`

## Web and networking

- DNS and caching → `web/dns-tls-networking.md`, `web/http.md`
- TCP/UDP/QUIC → `web/dns-tls-networking.md`
- TLS and certificate trust → `web/dns-tls-networking.md`
- HTTP semantics, caching and conditional requests → `web/http.md`
- proxies, load balancers and forwarded headers → `web/http.md`, `architecture/bff-and-gateway-patterns.md`
- CORS, CSP, same-origin policy → `web/browser-trust-boundaries.md`
- cookies, sessions and CSRF → `web/browser-trust-boundaries.md`
- WebSockets and SSE → `web/realtime-and-streaming.md`
- browser rendering and main-thread performance → frontend source + Fullstack frontend integration
- uploads/downloads and streaming → `web/realtime-and-streaming.md`

## Security

- threat modeling → `production/security.md`
- authentication vs authorization → `production/security.md`
- password hashing → `production/security.md`
- encryption and signatures → `foundations/security/cryptography.md`
- key/secret lifecycle → `foundations/security/cryptography.md`, `production/security.md`
- secure session design → `web/browser-trust-boundaries.md`, `production/security.md`
- OAuth/OIDC mental model → `production/security.md`
- JWT trade-offs → `production/security.md`
- SSRF, XSS, CSRF, SQL injection, IDOR, request smuggling → `production/security.md`
- supply-chain security → `production/security.md`, infrastructure security notes
- least privilege → `production/security.md`
- auditability and security logging → `production/security.md`, production observability

## Backend and distributed systems

- API contracts and evolution → `architecture/frontend-backend-contracts.md`
- idempotency → `production/reliability.md`, `fullstack-patterns/`
- timeouts and deadline propagation → `production/reliability.md`
- retries and retry storms → `production/reliability.md`
- rate limiting → `production/reliability.md`, `fullstack-patterns/`
- caching strategies and invalidation → `fullstack-patterns/`, data notes
- queues, streams and delivery semantics → `architecture/data-consistency-and-messaging.md`
- ordering and deduplication → `architecture/data-consistency-and-messaging.md`
- outbox/inbox patterns → `architecture/data-consistency-and-messaging.md`
- sagas and workflow state → `architecture/data-consistency-and-messaging.md`
- consistency models → `architecture/data-consistency-and-messaging.md`
- backpressure and load shedding → `systems/concurrency.md`, `production/reliability.md`

## Systems

- processes and threads → `systems/`
- virtual memory and resource limits → `systems/`
- filesystems and file descriptors → `systems/`
- event loops → `systems/concurrency.md`
- concurrency primitives → `systems/concurrency.md`
- synchronization and race conditions → `systems/concurrency.md`
- graceful shutdown → `systems/resource-lifecycle-and-graceful-shutdown.md`
- profiling and performance analysis → `systems/`, `production/`

## Production

- SLIs/SLOs/error budgets → `production/`
- capacity planning → `production/`
- saturation → `production/`
- incident response → `production/`
- disaster recovery and RPO/RTO → `production/disaster-recovery.md`
- observability design → `production/observability.md`
- structured logs, metrics and traces → `production/observability.md`
- load testing → `production/`
- dependency failure testing → `production/reliability.md`
- deployment/rollback strategy → `infrastructure/`, `production/`
- feature flags and graceful degradation → `production/reliability.md`

## Fullstack architecture

- frontend/backend ownership boundaries → `architecture/frontend-backend-contracts.md`
- transport DTO vs domain model → `architecture/frontend-backend-contracts.md`
- server state vs client state → `frontend/`, `fullstack-patterns/`
- BFF and gateway patterns → `architecture/bff-and-gateway-patterns.md`
- modular monoliths → `architecture/`
- service extraction criteria → `architecture/`
- synchronous vs asynchronous workflows → `architecture/data-consistency-and-messaging.md`
- transactional boundaries → `architecture/data-consistency-and-messaging.md`
- end-to-end security context → `production/security.md`
- end-to-end tracing → `production/observability.md`
- cost/performance trade-offs → `production/`, `architecture/`

## AI cross-layer gaps

AI depth remains in `learn-ai`. Fullstack owns:

- AI feature architecture in web applications → `architecture/ai-application-architecture.md`
- model API reliability and cost controls → AI architecture + production reliability
- streaming model responses to browsers → `web/realtime-and-streaming.md` + AI architecture
- RAG data lifecycle from ingestion to retrieval → AI architecture
- authorization-aware retrieval → AI architecture + security
- prompt/tool input validation → AI architecture + parsing/validation
- prompt injection as an application security problem → AI architecture + security
- agent execution limits and human approval → AI architecture
- evaluation integrated into CI/release processes → AI architecture + testing
- model observability and product metrics → AI architecture + production observability
- fallback/provider routing → AI architecture
- AI-specific latency and capacity planning → AI architecture + production

## Rule

A gap is closed only when the concept has a canonical explanation, a clear owner, links to implementation depth where applicable, and a path to exercise it in projects or interviews.
