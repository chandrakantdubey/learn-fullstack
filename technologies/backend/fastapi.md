# FastAPI

**Role:** Primary | **Layer:** Python backend

## What it is

FastAPI is an ASGI web framework for building typed Python HTTP APIs. It combines routing, dependency injection, request/response handling and OpenAPI generation with Pydantic-based validation.

## Mental model

Think of FastAPI as the transport adapter around an application:

```text
HTTP request
  → routing
  → dependencies / authentication
  → boundary validation
  → application service
  → domain logic
  → repositories / external adapters
  → response model
```

FastAPI should not become the place where business rules, database transactions, provider retries, or authorization policy are scattered.

## Core primitives

- path, query, header and cookie parameters
- request and response models
- dependency injection
- middleware
- exception handlers
- lifespan hooks
- background tasks
- OpenAPI generation
- async ASGI execution

## Request validation

Use Pydantic models for untrusted request data. Validate shape, bounds, enums and cross-field constraints at the boundary. Keep domain invariants in application/domain code when they require database state or business context.

Define response models intentionally. Do not accidentally serialize ORM objects or internal fields as public API contracts.

## Dependency injection

Use dependencies for cross-cutting request context such as authentication, tenant resolution, database sessions and reusable policy checks. Keep dependencies composable and avoid hiding expensive work inside a dependency that every route invokes.

Authentication should establish a trusted principal. Authorization should still be evaluated against the requested resource/action.

## Async execution

`async def` is useful when the handler spends time awaiting non-blocking I/O. It does not make blocking work asynchronous. Avoid blocking filesystem, CPU-heavy or synchronous network/database calls on the event loop; isolate them appropriately.

Use cancellation and deadlines for long-running outbound operations. Client disconnects and shutdown should have explicit semantics.

## Lifespan and resources

Create shared clients, pools and other process-level resources with explicit startup/shutdown lifecycle management. Avoid creating a new expensive connection pool or HTTP client for every request.

## Errors

Define stable API error contracts and centralize transport mapping. Domain/application errors should not depend on HTTP. Do not return stack traces, SQL, provider payloads or secrets to clients.

## OpenAPI

Treat generated OpenAPI as an API contract artifact. Keep request/response schemas stable, version breaking changes deliberately, and use contract tests where multiple clients depend on the API.

## Background work

Small non-critical work may use framework background tasks, but durable or retryable work belongs in a real job/queue design. A process-local background task can disappear during restart or deployment.

## Production checklist

- explicit request/response schemas
- authentication and authorization separated
- bounded payloads and pagination
- stable error schema
- outbound timeouts/deadlines
- structured logs and tracing
- database transactions with controlled scope
- non-blocking async handlers
- graceful startup/shutdown
- health/readiness semantics
- durable jobs for long-running work
- integration and contract tests

## Failure modes

Watch for N+1 queries, blocking the event loop, creating clients per request, unbounded request bodies, leaking internal models, missing authorization on routes, swallowing cancellation, and using process-local background tasks for durable work.

## Performance

Measure p50/p95/p99 latency, event-loop lag, request concurrency, dependency latency, DB pool utilization and response sizes. Scale based on bottlenecks rather than simply increasing worker count.

## Security

Validate all external input. Limit body sizes and upload paths. Configure trusted proxy behavior carefully. Protect cookies and CSRF-sensitive browser flows. Redact secrets from logs. Treat OpenAPI exposure as an API-surface decision rather than assuming documentation is harmless.

## Testing

Use unit tests for application logic, API tests for routing and validation, integration tests for PostgreSQL/Redis/dependencies, and contract/E2E tests for externally visible behavior. Inject failure cases for timeouts, dependency errors and authorization boundaries.

## Related

Pydantic, SQLAlchemy, PostgreSQL, OpenAPI, httpx, pytest, Docker and OpenTelemetry.
