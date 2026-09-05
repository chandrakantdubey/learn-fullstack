# Architecture Decision Guide

Use this when designing or reviewing a system. Architecture is a set of explicit trade-offs under constraints, not a collection of fashionable components.

## 1. Start with requirements

Write:

- users and actors
- core use cases
- data ownership
- consistency requirements
- availability target
- latency target
- throughput and peak factor
- data retention
- security/compliance constraints
- team/operational constraints
- budget

If a design has no workload model, capacity and scaling claims are mostly guesses.

## 2. Identify invariants

Examples:

- a payment is not charged twice
- a user cannot read another tenant's document
- an order cannot move from cancelled to fulfilled
- a job cannot become successful without its durable result
- a published document must eventually be searchable

Architecture should protect these invariants explicitly.

## 3. Choose the simplest boundary

Default progression:

```text
function/module
  ↓
modular component
  ↓
modular monolith
  ↓
worker / queue
  ↓
separate service
  ↓
multi-region/distributed topology
```

Move right only when workload, isolation, reliability, team ownership or security justifies it.

## 4. Decide sync vs async

Use synchronous work when the caller needs the result immediately and the operation fits the request latency budget.

Use asynchronous work when the work is slow, retryable, bursty, independently scalable, or does not need to block the user response.

Ask:

- what state is committed before returning?
- what happens if the caller disconnects?
- can the work run twice?
- how does the user learn completion/failure?

## 5. Data decisions

Choose storage from access patterns and invariants:

| Need | Typical fit |
|---|---|
| relational invariants/transactions | PostgreSQL |
| bounded low-latency acceleration | Redis |
| full-text relevance | search engine |
| semantic retrieval | vector index |
| large blobs | object storage |
| durable asynchronous work | queue |
| ordered event streams | streaming platform |

Do not introduce a second database until the access pattern or operational requirement is real.

## 6. Consistency decisions

For every cross-component write identify:

```text
source of truth
→ derived state
→ propagation mechanism
→ acceptable staleness
→ reconciliation path
```

Business invariants generally belong in the authoritative transactional boundary. Search indexes, caches, analytics and notifications are often derived state.

## 7. Reliability decisions

For every remote dependency define:

- deadline
- retryable failures
- maximum retries
- jitter/backoff
- idempotency
- circuit/bulkhead behavior
- fallback/degraded mode
- telemetry

Do not blindly retry all failures. Retries consume the same scarce resources that an overloaded dependency needs to recover.

## 8. Security decisions

For every data flow identify:

- actor
- asset
- trust boundary
- authentication
- authorization
- tenant/resource scope
- secret boundary
- abuse case
- audit requirement

Authorization must be enforced where the protected resource is accessed.

## 9. Observability decisions

Define telemetry before production:

```text
request → trace
state transition → structured event/log
aggregate behavior → metric
failure → actionable alert
```

Choose dimensions carefully. High-cardinality labels can make metrics expensive and difficult to operate.

## 10. Capacity decisions

Estimate:

`traffic → concurrency → compute → memory → DB connections → storage → queue throughput → dependency capacity`

Then model peak and failure cases. A service that works at average traffic but collapses during a burst is not capacity-planned.

## 11. Deployment decisions

Prefer:

`immutable artifact → staging verification → progressive release → telemetry check → promote/rollback`

The deployment mechanism must preserve compatibility between old and new versions during rollout when multiple versions coexist.

## 12. ADR template

```text
# ADR: <decision>

## Context
What problem and constraints exist?

## Decision
What are we doing?

## Why
Which requirements/invariants does it satisfy?

## Alternatives
What credible alternatives were considered?

## Trade-offs
What complexity, cost, latency, consistency or operational burden are accepted?

## Failure modes
What happens when dependencies or components fail?

## Security
What trust boundaries and abuse cases matter?

## Consequences
What becomes easier/harder?

## Revisit when
Which measured condition would invalidate the decision?
```

## Architecture review questions

- Is every component necessary?
- Is the source of truth obvious?
- Are boundaries aligned with ownership and invariants?
- Can failures be contained?
- Are retries safe?
- Can the system be observed?
- Can it be recovered?
- Is authorization enforced at the correct boundary?
- Is the capacity model plausible?
- Is the cost model known?
- Can the design evolve without a flag day?
