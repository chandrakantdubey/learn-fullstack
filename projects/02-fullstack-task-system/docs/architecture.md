# Architecture

## Boundary map

```text
                 Internet
                    │
              CDN / TLS edge
                    │
               Next.js app
                    │
                  HTTPS
                    ▼
              API service
          ┌─────────┼─────────┐
          │         │         │
       AuthZ     PostgreSQL  Redis
          │         │         │
          │         │         └── rate limits / cache / queue
          │         │
          │         └── source of truth
          │
          └── every resource access
                    │
                    ▼
                  Queue
                    │
                    ▼
                  Worker
                    │
                side effects
```

## Services

### Frontend

Responsible for presentation, navigation, form state, server-state fetching, accessibility, and user feedback. It is never the authority for authorization or business invariants.

### API

Responsible for authentication, authorization, validation, business rules, transactions, persistence, rate limits, and emitting durable work requests.

### Worker

Consumes asynchronous jobs. Every handler must be safe to retry because queue delivery is at-least-once.

### PostgreSQL

Canonical state. Constraints protect invariants even if another application path writes the data.

### Redis

Performance and coordination layer. Redis loss may reduce availability or performance but must not create false database state.

## Request path

1. Validate TLS and route request to the API.
2. Authenticate the caller.
3. Authorize access to the requested tenant/resource.
4. Validate the request schema.
5. Execute the smallest transaction that protects the business invariant.
6. Commit durable state.
7. Publish asynchronous work using a reliable pattern such as an outbox when the event must not be lost.
8. Return a response with stable error semantics.

## Failure behavior

- PostgreSQL unavailable: fail closed for writes; return retryable 503 where appropriate.
- Redis unavailable: bypass non-critical cache; reject or degrade rate limiting based on policy.
- Queue unavailable: commit durable state only when the system can guarantee eventual work publication; otherwise fail the operation rather than silently losing work.
- Worker crash: job becomes visible again and is retried.
- Duplicate job: idempotency key prevents duplicate side effects.

## Scaling

Start as a modular monolith. Scale API instances horizontally, keep them stateless, use PostgreSQL connection pooling, and move long work to workers. Split services only when ownership, scaling characteristics, or failure isolation justify it.
