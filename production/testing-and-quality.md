# Testing and Quality Engineering

Testing is a risk-control system. The goal is not maximum test count; it is high confidence at the cheapest useful layer.

## Test boundaries

| Layer | Best for | Avoid |
|---|---|---|
| Unit | pure logic, invariants, transformations | testing framework internals |
| Integration | DB/cache/queue/provider boundaries | mocking the dependency being verified |
| Contract | independent API/event compatibility | duplicating every unit assertion |
| E2E | critical user journeys | making every edge case an expensive browser test |
| Load | capacity and saturation | treating peak RPS as a quality metric |
| Security | abuse cases and trust boundaries | assuming scanners prove security |
| AI evaluation | model/retrieval behavior | relying only on unit tests |

## Testing pyramid

```text
                 small number
                     E2E
                      ▲
                Contract / API
                      ▲
                 Integration
                      ▲
                    Unit
                 large number
```

The shape is a heuristic, not a law. Expensive distributed behavior may require more integration coverage than a simplistic pyramid suggests.

## Contract testing

A frontend and backend can be individually correct and still disagree. Verify:

- request schemas
- response schemas
- error codes
- pagination/cursor semantics
- enum evolution
- optional/null behavior
- authentication requirements

OpenAPI can describe HTTP contracts. Runtime schemas enforce actual input/output boundaries. Keep business invariants separate from transport schemas.

## Database testing

Integration tests should run against a real supported database when SQL semantics matter.

Verify:

- migrations from a clean database
- migrations from representative previous versions
- constraints
- transactions and rollback
- concurrent access where relevant
- query behavior/index assumptions
- seed/fixture isolation

Testcontainers is useful when a real dependency is required without sharing a fragile developer database.

## Async testing

For queues/workers verify:

- job persistence
- duplicate delivery
- retry classification
- backoff
- dead-letter behavior
- visibility/lease expiry
- cancellation
- graceful shutdown
- eventual completion

Do not sleep for arbitrary durations to wait for a worker. Poll for an observable condition with a bounded timeout.

## Failure injection

Every important project should deliberately cause:

- database timeout
- cache outage
- queue backlog
- worker crash
- downstream 5xx
- downstream rate limit
- network disconnect
- invalid message
- duplicate message
- expired credentials
- stale client

Verify the resulting state, not just the returned error.

## Performance testing

Load tests should define:

- workload shape
- concurrency
- duration
- dataset size
- dependency configuration
- success criteria
- resource limits

Measure p50/p95/p99 latency, error rate, throughput and saturation. Compare against an explicit SLO/capacity target.

## Security testing

Turn threat-model abuse cases into tests:

- cross-tenant resource access
- IDOR
- invalid signatures/webhooks
- CSRF where applicable
- SSRF targets
- oversized payloads
- path traversal
- injection attempts
- privilege escalation
- secret leakage
- rate-limit bypass

## AI evaluation

Separate deterministic application tests from probabilistic evaluation.

A useful AI regression pipeline contains:

```text
golden dataset
 → model/retrieval execution
 → deterministic checks
 → retrieval metrics
 → answer-quality evaluation
 → safety checks
 → threshold gate
 → versioned results
```

Track model, prompt, retrieval configuration and dataset versions. A change is not safe merely because the average score improved; inspect regressions on important cases.

## Flaky tests

When a test flakes:

1. preserve the failure evidence
2. identify timing/order/shared-state dependence
3. reproduce repeatedly
4. remove accidental nondeterminism
5. add the smallest deterministic synchronization
6. fix the underlying race rather than adding arbitrary sleeps

## CI quality gates

Minimum useful pipeline:

`format → lint → typecheck → unit → integration → contract → security → build → E2E/smoke`

Expensive load and full browser suites can run on release/nightly paths when appropriate, but critical regressions must have a fast feedback path.

## Definition of test completeness

A feature is adequately tested when the important invariants, trust boundaries, failure modes and critical user journeys have explicit evidence. Test count alone is not evidence.
