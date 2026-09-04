# Retries, Timeouts, and Circuit Breakers

Reliability controls must be designed together. A retry without a deadline can make an outage worse.

## Problem

Distributed calls fail through latency, dropped connections, overload, partial responses, and dependency outages. Clients need a bounded strategy for deciding when to wait, retry, fail, or degrade.

## Invariants

- Every remote call has a deadline or timeout.
- The caller's remaining budget constrains downstream work.
- Retries apply only when the operation is safe to repeat or has idempotency protection.
- Backoff includes jitter to avoid synchronized retry waves.
- Retry counts and total elapsed time are bounded.

## Retry policy

Classify errors before retrying. Transient transport failures and selected `5xx` responses may be retryable. Validation errors, authorization failures, deterministic conflicts, and many `4xx` responses are not.

Use exponential backoff with jitter and a maximum attempt count. Respect server-provided retry hints where appropriate.

## Timeouts and deadlines

A timeout answers how long one operation may wait. A deadline answers how much total time remains for the whole request. Propagate the deadline downstream so nested calls cannot outlive the parent budget.

## Circuit breakers

A breaker can stop sending traffic to a failing dependency after evidence of failure, allowing recovery. It should have explicit closed/open/half-open behavior and should not be used as a substitute for timeouts or capacity controls.

## Failure modes

- retrying non-idempotent mutations
- nested retries multiplying traffic
- timeout longer than the caller's deadline
- no jitter
- breaker opens on harmless application errors
- all instances probe a recovering dependency simultaneously
- fallback returns misleading success

## Security

Do not retry credential failures or authorization failures indiscriminately. Avoid logging sensitive request bodies during repeated failures.

## Performance

Budget retries as part of capacity planning. If one request can fan out to N dependencies and each can retry, worst-case work can grow rapidly. Bound concurrency and use load shedding when necessary.

## Operational signals

Track timeout rate, retry attempts, retry amplification, breaker state, dependency latency, error class, and fallback usage.
