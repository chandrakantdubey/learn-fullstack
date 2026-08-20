# Reliability Engineering

Reliability means the system continues to provide an acceptable level of service as load, dependencies, deployments, and failures change.

## Failure is normal

Design for:

- process crashes
- network timeouts
- dependency failures
- database contention
- queue backlog
- partial deploys
- malformed requests
- exhausted resources
- node/zone loss

## Core controls

### Timeouts

Every network dependency should have a bounded timeout. An unbounded wait consumes concurrency and can create cascading failure.

### Retries

Retry only failures that are likely transient. Use exponential backoff with jitter and cap the attempts.

Retries must consider idempotency. Retrying a non-idempotent operation can create duplicate effects.

### Circuit breakers

When a dependency is unhealthy, stop sending it unlimited work. Fail fast for a period and probe for recovery.

### Bulkheads

Isolate resource pools so one workload cannot consume all threads, connections, memory, or queue capacity.

### Backpressure

When consumers cannot keep up, explicitly limit producers or queue work rather than allowing unbounded memory growth.

### Graceful shutdown

Stop accepting new work, allow safe in-flight work to finish or be terminated, and release resources cleanly.

## SLO thinking

Define:

- service level indicator (SLI)
- service level objective (SLO)
- error budget

Example:

> 99.9% of successful API requests complete within the agreed latency threshold over a monthly window.

An SLO should influence deployment speed, alerting, capacity, and architecture decisions.

## Disaster recovery

Know the difference between:

- backup
- restore
- replication
- failover
- disaster recovery

A backup that has never been restored is an assumption, not a proven recovery mechanism.

Track:

- RTO
- RPO
- backup retention
- restore duration
- dependency recovery order

## Capacity

Capacity planning should cover:

```text
traffic → concurrency → CPU/memory → DB connections → storage → queue capacity
```

Estimate normal, peak, and failure-mode capacity. Headroom is part of reliability.

## Incident loop

```text
Detect
  ↓
Triage
  ↓
Mitigate
  ↓
Recover
  ↓
Verify
  ↓
Learn
```

Prefer blameless postmortems focused on system conditions, missing safeguards, and actionable follow-up.

## Project proof

Inject failure into the task platform: kill workers, introduce Redis latency, exhaust database connections, and return intermittent downstream errors. Verify timeout, retry, backpressure, health checks, and recovery behavior.