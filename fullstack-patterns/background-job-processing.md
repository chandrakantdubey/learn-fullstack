# Background Job Processing

Move work out of the request path when it is slow, retryable, bursty, or independently scalable.

## Problem

Email, document processing, exports, indexing, AI inference, and other long-running tasks should not consume an HTTP request's latency budget.

## Boundary

```text
HTTP command
  → durable job record / queue
  → worker
  → dependency calls
  → result/state update
  → notification/polling/webhook
```

The queue is a coordination mechanism, not automatically a source of truth.

## Invariants

- Enqueueing work has a durable acceptance point.
- Jobs have unique identities and explicit states.
- Workers are safe under duplicate execution.
- Retries are bounded and classified by error type.
- Poison jobs cannot block unrelated work indefinitely.
- Cancellation and shutdown semantics are explicit.

## Implementation choices

A job should carry an ID, type, version, input reference, attempt count, timestamps, and enough context to execute safely. Prefer references to large mutable blobs where possible.

Use visibility timeouts/leases or explicit state transitions so a crashed worker's job can become available again. Use dead-letter handling for jobs that exceed retry policy.

Separate queues by workload class when latency, priority, or resource requirements differ.

## Failure modes

- worker crashes after performing a side effect
- duplicate delivery
- retry storms
- unbounded queue growth
- one poison job monopolizes workers
- job payload becomes incompatible after deployment
- shutdown abandons in-flight work

## Security

Never trust job payloads merely because they came from an internal producer. Re-check authorization for sensitive actions when execution happens later. Protect queue access and redact sensitive data from job logs.

## Performance

Control concurrency, batch where useful, apply backpressure, and set dependency deadlines. Capacity planning should use arrival rate, service time, worker concurrency, and queue age—not just CPU utilization.

## Operational signals

Track queue depth, oldest-job age, throughput, processing latency, retry rate, failure rate, dead letters, worker saturation, and dependency timeouts.
