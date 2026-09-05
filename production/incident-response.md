# Incident Response and Operational Debugging

Production engineering includes the ability to turn an alert into a controlled recovery.

## Incident lifecycle

```text
Detect
 ↓
Triage
 ↓
Mitigate
 ↓
Diagnose
 ↓
Recover
 ↓
Verify
 ↓
Communicate
 ↓
Learn
```

Mitigation comes before perfect diagnosis when customer impact is active.

## First five questions

1. What changed?
2. What is failing?
3. Who is affected?
4. When did it start?
5. What resource/dependency is saturated or unhealthy?

Start with user-visible symptoms and recent changes, then narrow the fault domain.

## Layered debugging

```text
DNS
 ↓
TLS / connection
 ↓
HTTP / gateway
 ↓
application
 ↓
database / cache / queue
 ↓
external dependency
 ↓
infrastructure
```

Use correlation IDs and traces to move from an individual failed request to the responsible dependency.

## Symptom → hypothesis

### High latency

Check:

- p95/p99 versus average
- queue wait
- DB pool wait
- DB query latency
- downstream latency
- CPU/memory/I/O saturation
- cache misses

### 5xx spike

Check:

- deployment history
- dependency errors
- connection exhaustion
- process crashes
- configuration/secrets
- schema compatibility

### Queue backlog

Check:

- arrival rate
- consumer throughput
- worker health
- downstream latency
- retry amplification
- poison messages
- concurrency limits

### Memory growth

Check:

- process RSS/heap
- object/cache growth
- queue size
- connection/file-descriptor leaks
- workload correlation

## Safe mitigation

Examples:

- rollback a bad deployment
- disable a feature flag
- reduce traffic or concurrency
- stop a runaway worker
- shed non-critical work
- switch to a healthy dependency/provider
- serve cached/degraded results

Every mitigation should have a verification step.

## Communication

During an incident record:

- impact
- start time
- current hypothesis
- mitigation
- owner
- next checkpoint
- customer-facing status when required

Avoid speculative blame. Keep the incident channel focused on facts, actions and decisions.

## Post-incident review

Capture:

- timeline
- customer impact
- trigger
- contributing conditions
- why detection worked/failed
- why mitigation worked/failed
- missing safeguards
- concrete follow-ups with owners

Do not stop at “engineer made a mistake.” Ask which system property allowed the mistake to create customer impact.

## Operational drills

Run these against the portfolio projects:

1. kill an API instance
2. exhaust DB connections
3. add database latency
4. make Redis unavailable
5. pause workers
6. create queue backlog
7. return intermittent downstream 5xx
8. deploy an intentionally incompatible version
9. revoke a credential
10. introduce a stale/partial index
11. trigger a cross-tenant authorization test
12. cause a model provider outage

For each drill record detection time, mitigation, recovery time and missing telemetry.

## Senior/staff standard

You should be able to explain not only how to fix the immediate failure, but:

- why the system allowed it
- why monitoring did or did not catch it
- how to reduce blast radius
- what automation is worth adding
- what trade-off the fix introduces
- whether the architecture should change
