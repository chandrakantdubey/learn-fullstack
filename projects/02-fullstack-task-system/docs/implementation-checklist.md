# Implementation Checklist

## Phase 1 — Database

- [ ] initialize migration tooling
- [ ] create users/tasks/outbox tables
- [ ] add constraints and indexes
- [ ] add seed data for local development
- [ ] verify rollback and repeatability

## Phase 2 — API

- [ ] health endpoint
- [ ] readiness endpoint
- [ ] structured request logging
- [ ] request ID / trace propagation
- [ ] auth registration/login/refresh/logout
- [ ] task CRUD
- [ ] cursor pagination
- [ ] optimistic concurrency
- [ ] idempotency keys
- [ ] rate limiting
- [ ] consistent error envelope

## Phase 3 — Worker

- [ ] durable queue consumption
- [ ] retry policy with exponential backoff
- [ ] idempotent handler
- [ ] dead-letter handling
- [ ] graceful shutdown
- [ ] metrics for queue depth and job latency

## Phase 4 — Frontend

- [ ] authenticated shell
- [ ] task list and filters
- [ ] create/edit/delete flows
- [ ] loading/error/empty states
- [ ] optimistic update where safe
- [ ] conflict handling
- [ ] keyboard accessibility
- [ ] responsive layout

## Phase 5 — Production

- [ ] Docker images
- [ ] Compose local environment
- [ ] CI lint/typecheck/test/build
- [ ] container vulnerability scan
- [ ] Kubernetes manifests
- [ ] Terraform modules
- [ ] managed PostgreSQL
- [ ] managed Redis
- [ ] secrets management
- [ ] OpenTelemetry traces
- [ ] Prometheus metrics
- [ ] dashboards and alerts
- [ ] backup/restore test
- [ ] load test
- [ ] rollback procedure

## Definition of done

The project is not complete when it works on a laptop. It is complete when the system can be deployed, observed, degraded safely, upgraded without breaking active traffic, restored from backup, and explained in terms of explicit trade-offs.
