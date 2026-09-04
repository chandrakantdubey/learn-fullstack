# BFF and Gateway Patterns

A gateway is a boundary for shared edge concerns. A Backend-for-Frontend (BFF) is a backend boundary shaped around the needs of a particular client experience.

## Gateway responsibilities

A gateway may handle:

- routing
- TLS termination
- authentication handoff
- rate limiting
- request size limits
- observability propagation
- coarse-grained policy

It should not become an unbounded business-logic dump.

## BFF responsibilities

A BFF can:

- aggregate multiple backend calls;
- shape responses for a frontend;
- coordinate frontend-specific workflows;
- reduce chatty browser-to-service communication;
- provide a stable client-facing contract while backend services evolve.

## Decision model

Use a BFF when client-specific composition is substantial and stable enough to justify a boundary. Prefer a simpler application API when a gateway/BFF would only add routing and operational complexity.

## Failure considerations

Aggregation creates new failure modes:

- partial dependency failure
- increased tail latency
- fan-out amplification
- inconsistent authorization across downstream calls
- retry multiplication

Use deadlines, bounded concurrency, explicit partial-response policy and end-to-end authorization.

## Cross-layer ownership

Frontend owns client needs and rendering. Backend owns service implementation. This document owns the architectural boundary and trade-offs.

## Related concepts

- API contracts and schema evolution
- authentication and authorization
- retries and deadlines
- distributed tracing
- service decomposition
