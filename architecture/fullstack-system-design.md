# Fullstack System Design

This is the canonical reference architecture that ties the repository together.

## Baseline architecture

```text
                     Internet
                         │
                    Route 53 / DNS
                         │
                    CDN / Edge
                         │
                 Load Balancer / Gateway
                         │
              ┌──────────┴───────────┐
              │                      │
          Web / Next.js           API / FastAPI
              │                      │
              └──────────┬───────────┘
                         │
                   Service Layer
                         │
             ┌───────────┼───────────┐
             │           │           │
         PostgreSQL     Redis       Queue
             │           │           │
             │           │        Worker
             │           │           │
             └───────────┴───────────┘
                         │
                 Observability
                         │
              Logs / Metrics / Traces
```

## Request lifecycle

1. DNS resolves the public endpoint.
2. Edge infrastructure terminates TLS and applies caching/routing controls.
3. The application gateway/load balancer selects a healthy backend.
4. The API authenticates the request and validates input.
5. The service layer applies business rules.
6. PostgreSQL owns durable business state.
7. Redis handles bounded, disposable acceleration such as caching or rate limits.
8. Queues isolate slow or asynchronous work.
9. Workers execute background processing idempotently.
10. Telemetry follows the request across all relevant boundaries.

## Consistency model

Default to strong consistency for business invariants that must be immediately true. Use asynchronous propagation for secondary concerns such as search indexing, analytics, notifications, or cache invalidation where eventual consistency is acceptable.

## Scaling path

```text
Single process
   ↓
Multiple API replicas
   ↓
Connection pools + cache
   ↓
Queue-backed workers
   ↓
Read replicas / partitioning
   ↓
Horizontal service scaling
   ↓
Multi-zone resilience
   ↓
Multi-region only when justified
```

Scale the bottleneck, not the architecture diagram.

## Security boundaries

- browser is untrusted
- public API is untrusted input boundary
- application service enforces authorization
- database credentials are never exposed to clients
- workers use separate identities
- infrastructure uses least-privilege roles
- secrets never live in source code or container images

## Failure strategy

Every dependency has:

- timeout
- bounded retries where safe
- idempotency strategy
- observability
- degradation behavior

The system should remain useful when non-critical dependencies fail.

## Deployment strategy

```text
PR
 ↓
CI
 ↓
Immutable images
 ↓
Staging
 ↓
Smoke tests
 ↓
Progressive production rollout
 ↓
Telemetry verification
 ↓
Promote / Roll back
```

## Cost strategy

Start with managed services and a simple topology. Measure compute, database, storage, egress, observability, and idle resource costs before introducing more infrastructure.

## Project milestone

Implement this architecture for the fullstack task system first as a modular monolith plus workers. Then evolve it only where measured workload or reliability requirements justify additional services.