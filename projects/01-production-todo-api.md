# Project 01 — Production Todo API

The first integration project proves the path from HTTP to persistence, caching, security, testing, and operations.

## Goal

Build the same service twice:

- Python + FastAPI
- TypeScript + Node.js

The API manages users, projects, and tasks.

## Required architecture

```text
Client
  ↓
HTTP API
  ↓
Authentication / Authorization
  ↓
Application layer
  ↓
PostgreSQL
  ↓
Redis cache

Background work
  ↓
Queue/worker
  ↓
Notifications or audit processing
```

## Core endpoints

- `POST /auth/login`
- `POST /projects`
- `GET /projects/:id`
- `POST /projects/:id/tasks`
- `GET /projects/:id/tasks`
- `PATCH /tasks/:id`
- `DELETE /tasks/:id`

## Engineering requirements

### Data

- PostgreSQL schema with foreign keys and constraints
- migrations
- indexed access paths
- explicit transaction boundaries

### Cache

Cache the project/task summary where useful.

Document:

- key format
- TTL
- invalidation
- Redis outage behavior

### API

- request validation
- consistent error contract
- pagination
- authentication
- authorization
- idempotency for selected mutation endpoints

### Reliability

- timeouts on outbound calls
- bounded retries where safe
- graceful shutdown
- health/readiness checks
- structured logs
- request correlation ID

### Testing

- unit tests for domain behavior
- integration tests against PostgreSQL
- API tests
- authorization tests
- cache failure tests
- Playwright smoke test for the UI/API integration when a frontend is added

## Productionization

Containerize the application and PostgreSQL for local development. Add CI that runs linting, type checks, tests, build, and a migration check.

Deploy a staging environment before production.

## Acceptance criteria

You can explain every layer without looking at the framework documentation, demonstrate where consistency is guaranteed, show what happens during a PostgreSQL outage, and identify the bottleneck using logs/metrics rather than intuition.
