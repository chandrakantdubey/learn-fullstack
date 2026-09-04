# Nine-Repository Fullstack Skill Map

`learn-dsa` is complete. The remaining eight repositories are deep domain sources. `learn-fullstack` is the synthesis layer and owns cross-domain engineering knowledge that cannot be cleanly assigned to one specialized repository.

## Source ownership

| Source | Owns | Fullstack integrates |
|---|---|---|
| `learn-js-ts` | JavaScript/TypeScript language and runtime | language-agnostic programming models, browser/server runtime connections, application boundaries |
| `learn-frontend` | browser, HTML/CSS, React, Next.js | end-to-end web lifecycle, frontend/backend contracts, performance/security boundaries |
| `learn-backend` | APIs, services, distributed backend systems | cross-layer API architecture, reliability, service-to-data interactions |
| `learn-python` | Python language/runtime/ecosystem | Python vs TypeScript engineering decisions and shared backend patterns |
| `learn-sql` | SQL/PostgreSQL/database internals | application data lifecycle, transactions, caching, queues, search and consistency |
| `learn-docker` | Docker/container operations | container-to-application-to-cloud deployment model |
| `learn-ai` | ML/LLM/AI engineering | AI features inside real fullstack systems, security, evaluation, cost, reliability |
| `learn-dsa` | DSA/interview problem solving | complexity judgment inside architecture and production code |

## Fullstack-owned cross-cutting knowledge

These are deliberately not duplicated into specialized repositories unless a domain needs its own implementation details:

- regular expressions and text processing
- encoding, Unicode, bytes and serialization
- cryptographic primitives and application security mental models
- HTTP semantics and protocol evolution
- DNS, TLS, TCP/UDP and connection lifecycle
- cookies, sessions, CORS, CSRF, CSP and browser trust boundaries
- WebSockets, SSE and realtime architecture
- processes, threads, memory, filesystems and OS boundaries
- concurrency, synchronization, backpressure and cancellation
- API design, contracts, versioning and error semantics
- distributed-systems invariants and failure models
- caching, idempotency, retries, timeouts and rate limiting
- observability and production debugging across layers
- capacity planning, SLOs, incident response and cost reasoning
- architecture and system-design trade-offs
- end-to-end project architecture

## Rule

Do not move a concept merely because a framework happens to use it. Put durable engineering knowledge at the layer where it is most reusable. Technology notes remain canonical under `technologies/`; cross-layer concepts remain concept documents.
