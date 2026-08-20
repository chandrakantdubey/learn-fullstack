# Project 02 — Production Fullstack Task System

Build a realistic task-management application that exercises the browser, API, database, cache, authentication, testing, and deployment boundaries together.

## Goal

Implement:

```text
Browser
  ↓
Next.js / React
  ↓ HTTPS
API
  ↓
Service layer
  ├── PostgreSQL
  ├── Redis
  └── Background worker
```

## Required capabilities

### Identity

- email/password authentication or an OAuth/OIDC provider
- secure session handling
- logout
- protected routes
- server-side authorization

### Tasks

- create task
- update task
- complete task
- delete task
- list with pagination
- filter by status
- sort by creation time
- optimistic completion where safe

### API

Define stable contracts for:

- authentication
- task CRUD
- pagination
- validation errors
- authorization failures

The API must not expose raw database models as its public contract.

### Data

PostgreSQL should contain:

- users
- projects
- project membership
- tasks
- audit events

Required constraints should live in the database where they represent hard invariants.

### Redis

Use Redis for one real purpose, such as:

- short-lived rate limiting
- cache of an expensive read
- idempotency record for a mutation

Document why Redis is needed and what happens if Redis is unavailable.

### Background work

Send at least one asynchronous job, for example:

- activity notification
- email notification
- audit processing

The worker must be idempotent because delivery can be duplicated.

## Frontend requirements

- accessible semantic UI
- responsive layout
- URL-driven filters/pagination
- clear loading/empty/error states
- server-state caching
- optimistic mutation only where rollback is well defined
- end-to-end tests for the critical task workflow

## Production requirements

- Dockerized services
- structured logs
- request IDs/correlation IDs
- health/readiness checks
- metrics and traces
- environment-based configuration
- secret management
- database migrations
- CI checks
- safe deployment strategy

## Failure scenarios to test

1. PostgreSQL unavailable
2. Redis unavailable
3. duplicate task mutation
4. expired session
5. unauthorized project access
6. worker receives the same job twice
7. network request times out
8. browser refresh during mutation
9. partially failed notification

## Acceptance criteria

The project is complete when a new engineer can:

- start the complete stack locally
- run migrations
- execute tests
- inspect API documentation
- observe logs and request traces
- understand the database schema
- intentionally break one dependency and diagnose the failure
- deploy the application from CI

## Suggested implementations

### Python path

Next.js + FastAPI + PostgreSQL + Redis + worker using Celery/ARQ or an equivalent queue model.

### TypeScript path

Next.js + Node.js/TypeScript API + PostgreSQL + Redis + worker using a queue library such as BullMQ.

Build the same product with both paths after the first implementation. Compare runtime model, type boundaries, error handling, dependency management, and operational behavior.

## What this project proves

This is not a CRUD demo. It proves that you can connect:

```text
Browser
→ HTTP
→ Authentication
→ API contract
→ Business logic
→ Transactional database state
→ Cache/coordination
→ Async processing
→ Testing
→ Observability
→ Deployment
```
