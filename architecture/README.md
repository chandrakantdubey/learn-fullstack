# Architecture

This section connects individual technologies into complete systems.

## Canonical guides

- [`api-design.md`](api-design.md) — API semantics, contracts, evolution, idempotency and security.
- [`frontend-backend-contracts.md`](frontend-backend-contracts.md) — cross-layer type/data boundaries.
- [`bff-and-gateway-patterns.md`](bff-and-gateway-patterns.md) — edge/BFF/gateway responsibilities.
- [`data-consistency-and-messaging.md`](data-consistency-and-messaging.md) — transactions, events, outbox and consistency.
- [`distributed-systems.md`](distributed-systems.md) — partial failure, consistency and distributed patterns.
- [`ai-application-architecture.md`](ai-application-architecture.md) — AI/RAG/agent integration boundaries.
- [`fullstack-system-design.md`](fullstack-system-design.md) — reference fullstack architecture.
- [`../docs/architecture-decision-guide.md`](../docs/architecture-decision-guide.md) — requirements-to-trade-off design process.

## Core competencies

- requirements and constraints
- domain boundaries
- API and data contracts
- modular monoliths
- service decomposition
- caching strategies
- asynchronous processing
- event-driven architecture
- distributed systems
- consistency models
- capacity planning
- scaling strategies
- failure modes
- security boundaries
- cost-performance trade-offs
- disaster recovery

## Design process

```text
Requirements
  ↓
Constraints
  ↓
Workload model
  ↓
Invariants
  ↓
Data model
  ↓
API / event contracts
  ↓
Component boundaries
  ↓
Deployment topology
  ↓
Failure + security analysis
  ↓
Observability
  ↓
Capacity / cost
  ↓
ADR + rollout plan
```

The preferred design is the simplest one that satisfies the requirements. Complexity must be justified by workload, reliability, security, organizational boundaries, or operational needs.
