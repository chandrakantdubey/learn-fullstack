# Service Architecture

A service is a boundary around a set of behavior, state, and dependencies. The first goal is clear ownership, not microservices.

## Default starting point: modular monolith

```text
HTTP
 ↓
Application boundary
 ├── identity
 ├── users
 ├── orders
 └── billing
 ↓
PostgreSQL
```

Keep modules separated by domain responsibility while deploying them together. Extract a service only when an independent scaling, deployment, ownership, isolation, or reliability requirement justifies the complexity.

## Request path

```text
Client
 ↓
HTTP server
 ↓
Authentication
 ↓
Validation
 ↓
Application/use-case layer
 ↓
Domain logic
 ↓
Repository / external client
 ↓
Response
```

Keep transport concerns out of domain logic. The HTTP handler should not become the business rule engine.

## Dependencies

Prefer explicit dependency boundaries.

```text
handler → use case → repository
                       ↘ external service
```

This makes testing, replacement, and reasoning about failures easier.

## Database transactions

A transaction belongs around a business state transition, not automatically around every database call.

For example, creating an order may require:

```text
validate inventory
→ create order
→ reserve inventory
→ record payment intent
```

Decide which parts must be atomic and which can be asynchronous.

## Synchronous vs asynchronous

Use synchronous work when the caller needs the result before proceeding.

Use asynchronous work for:

- email
- notifications
- indexing
- analytics
- expensive processing
- retries against unreliable dependencies

```text
request
  ↓
transaction
  ↓
outbox/event
  ↓
queue
  ↓
worker
```

## Reliability boundaries

Every remote dependency needs:

- timeout
- bounded retry policy
- idempotency strategy
- error classification
- observability

Never let an unbounded dependency call hold an HTTP request indefinitely.

## Production rule

Prefer a boring architecture until a measurable requirement demands more distribution.

## Connects to

`web/http`, `data/postgresql`, `data/redis`, `systems/concurrency`, `production/reliability`, and `architecture/system-design`.
