# Production Engineering

Production engineering is where correctness becomes operational reliability.

## Canonical guides

- [`security.md`](security.md) — cross-stack security baseline.
- [`security-engineering.md`](security-engineering.md) — threat boundaries, identity, secrets and supply chain.
- [`threat-modeling.md`](threat-modeling.md) — concrete threat-modeling workflow and security verification.
- [`testing-and-quality.md`](testing-and-quality.md) — unit/integration/contract/E2E, failure, load, security and AI evaluation strategy.
- [`observability.md`](observability.md) — logs, metrics, traces and OpenTelemetry.
- [`reliability.md`](reliability.md) — timeouts, retries, idempotency, backpressure, SLOs and failure handling.
- [`performance-and-capacity.md`](performance-and-capacity.md) — workload models, bottlenecks and load testing.
- [`incident-response.md`](incident-response.md) — production diagnosis, mitigation, recovery and post-incident learning.
- [`disaster-recovery.md`](disaster-recovery.md) — RPO/RTO, backup/restore and recovery architecture.

## Production loop

```text
Build
 ↓
Test
 ↓
Secure
 ↓
Deploy
 ↓
Observe
 ↓
Detect
 ↓
Diagnose
 ↓
Mitigate
 ↓
Recover
 ↓
Improve
```

## Required controls

- testing strategy
- authentication and authorization
- secrets/key lifecycle
- structured logging
- metrics and tracing
- SLOs/error budgets
- timeouts/retries/idempotency
- rate/resource limits
- graceful degradation
- capacity planning
- failure injection
- rollback
- backup/restore
- incident response

A feature is not complete when it works locally. It is complete when the team can operate it safely and understand how it behaves under failure, attack, scale and change.

## Final verification

See [`../docs/production-verification.md`](../docs/production-verification.md) for the end-to-end evidence standard.
