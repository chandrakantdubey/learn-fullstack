# Fullstack Task System

A production-oriented reference application for learning how a browser, API, database, cache, worker, containers, CI/CD, and observability fit together.

## Goals

Build the same product architecture in two backend variants:

- Python + FastAPI
- TypeScript + Node.js

The frontend remains TypeScript + React/Next.js.

## System

```text
Browser
  │
  ▼
Next.js UI
  │ HTTPS
  ▼
API
  ├── PostgreSQL ─── source of truth
  ├── Redis ───────── cache / rate-limit / job transport
  └── Queue
        │
        ▼
     Worker
        │
        └── async side effects

All services
  └── OpenTelemetry → metrics / traces / logs
```

## Repository shape

```text
02-fullstack-task-system/
├── README.md
├── docs/
│   ├── architecture.md
│   ├── api-contract.md
│   └── data-model.md
├── frontend/
├── api-python/
├── api-typescript/
├── worker-python/
├── worker-typescript/
├── infra/
│   ├── docker-compose.yml
│   ├── postgres/
│   └── redis/
└── .github/
    └── workflows/
```

## Functional requirements

- email/password sign-up and sign-in
- authenticated task CRUD
- task ownership enforced server-side
- pagination and filtering by status
- optimistic UI update where safe
- idempotent task mutation support
- background audit/notification job
- Redis-backed rate limiting
- structured logs
- trace correlation across API → DB/Redis → worker
- health and readiness endpoints
- local Docker Compose environment
- CI for lint, type checks, tests, and build

## Non-functional requirements

- API must remain stateless
- PostgreSQL is the source of truth
- Redis failures must not corrupt task state
- background jobs are at-least-once and therefore idempotent
- secrets never live in source control
- migrations are backward-compatible during rolling deployments
- service timeouts are explicit
- authorization happens on every resource access

## Build order

1. data model
2. API contract
3. Python API
4. TypeScript API
5. worker
6. frontend
7. Redis rate limiting/cache
8. observability
9. Docker Compose
10. CI/CD
11. Kubernetes deployment
12. AWS/Terraform deployment
