# Cross-Cutting Engineering Gap List

This is the backlog for knowledge that should exist in the integrated Fullstack repository even when no specialized repository is the natural owner.

## Programming and data handling

- Regular expressions and regex-engine behavior
- Unicode, normalization and grapheme handling
- Bytes, encodings and base64
- Serialization/deserialization and schema evolution
- Floating-point behavior, precision and money representation
- dates, time zones, clocks and monotonic time
- randomness and secure randomness
- hashing, checksums and content addressing
- parsing vs validation
- resource ownership and cleanup

## Web and networking

- DNS and caching
- TCP/UDP/QUIC
- TLS and certificate trust
- HTTP semantics, caching and conditional requests
- proxies, load balancers and forwarded headers
- CORS, CSP, same-origin policy
- cookies, sessions and CSRF
- WebSockets and SSE
- browser rendering and main-thread performance
- uploads/downloads and streaming

## Security

- threat modeling
- authentication vs authorization
- password hashing
- encryption and signatures
- key/secret lifecycle
- secure session design
- OAuth/OIDC mental model
- JWT trade-offs
- SSRF, XSS, CSRF, SQL injection, IDOR, request smuggling
- supply-chain security
- least privilege
- auditability and security logging

## Backend and distributed systems

- API contracts and evolution
- idempotency
- timeouts and deadline propagation
- retries and retry storms
- rate limiting
- caching strategies and invalidation
- queues, streams and delivery semantics
- ordering and deduplication
- outbox/inbox patterns
- sagas and workflow state
- consistency models
- backpressure and load shedding

## Systems

- processes and threads
- virtual memory and resource limits
- filesystems and file descriptors
- event loops
- concurrency primitives
- synchronization and race conditions
- graceful shutdown
- profiling and performance analysis

## Production

- SLIs/SLOs/error budgets
- capacity planning
- saturation
- incident response
- disaster recovery
- RPO/RTO
- observability design
- structured logs, metrics and traces
- load testing
- dependency failure testing
- deployment/rollback strategy
- feature flags and graceful degradation

## Fullstack architecture

- frontend/backend ownership boundaries
- transport DTO vs domain model
- server state vs client state
- BFF and gateway patterns
- modular monoliths
- service extraction criteria
- synchronous vs asynchronous workflows
- transactional boundaries
- end-to-end security context
- end-to-end tracing
- cost/performance trade-offs

## AI cross-layer gaps

The AI repository owns AI depth. `learn-fullstack` additionally owns:

- AI feature architecture in web applications
- model API reliability and cost controls
- streaming model responses to browsers
- RAG data lifecycle from ingestion to retrieval
- authorization-aware retrieval
- prompt/tool input validation
- prompt injection as an application security problem
- agent execution limits and human approval
- evaluation integrated into CI/release processes
- model observability and product metrics
- fallback/provider routing
- AI-specific latency and capacity planning

## Rule

This list is not a checklist to blindly turn into lessons. Consolidate related ideas into strong mental-model documents, then link technology notes and projects to those concepts.
