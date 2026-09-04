# Fastify

**Role:** Primary | **Layer:** TypeScript backend

## Mental model
Fastify is a Node.js HTTP framework built around routes, schemas, hooks, plugins and encapsulated application contexts. Its architecture encourages explicit composition rather than a global middleware pile.

```text
request
  -> hooks
  -> validation/deserialization
  -> route handler
  -> application service
  -> persistence/external calls
  -> serialization
  -> response
```

## Routes
Keep route handlers thin. A handler should translate HTTP concerns into an application command/query and translate the result back into an HTTP response.

## Hooks
Understand lifecycle hooks and their scope. Use hooks for cross-cutting HTTP concerns such as request context, authentication prerequisites, metrics and cleanup. Avoid hiding business workflows in hooks.

## Plugins and encapsulation
Plugins are a core architectural primitive. Encapsulation controls which decorators, hooks and routes are visible to nested scopes. Use this to create explicit module boundaries.

## Validation and serialization
Fastify can use JSON Schema for validation and response serialization. The repository's TypeScript stack uses Zod as the canonical runtime schema technology where appropriate; do not create a second validation note just for Fastify.

Validate at the HTTP boundary, then pass validated data into application code.

## Error handling
Define a stable error model. Distinguish client errors, authentication/authorization failures, domain conflicts, dependency failures and unexpected server errors. Avoid leaking stack traces or internal dependency details.

## Timeouts and cancellation
Every request should have bounded execution. Propagate cancellation to downstream operations where supported. A server timeout without downstream cancellation can leave work running after the client has gone away.

## Production architecture
```text
Fastify adapter
    |
    +-- auth/authz
    +-- validation
    +-- request context
    |
application services
    |
    +-- repositories
    +-- external clients
    +-- queues
```

This separation keeps transport concerns from becoming domain logic.

## Performance
Measure route latency, serialization cost, event-loop delay, database latency and downstream calls. Response schemas can improve serialization predictability, but the dominant bottleneck is usually I/O or application work rather than routing itself.

## Security
Set body limits, timeout policies, secure headers where appropriate, request IDs, authentication and authorization. Validate untrusted input. Treat file uploads and proxy endpoints as high-risk boundaries.

## Observability
Record request duration, status, route template, trace ID and dependency latency. Avoid high-cardinality raw URLs and sensitive payloads in metrics/logs.

## Testing
Test route contracts at the HTTP boundary, application services independently and integrations against real dependencies where behavior matters. Include auth, validation, conflict and timeout cases.

## Common mistakes
- fat route handlers
- global mutable decorators
- duplicated validation logic
- missing response schemas/contracts
- no outbound timeouts
- authentication without authorization
- logging request bodies indiscriminately

## Interview-level topics
Plugin encapsulation, lifecycle hooks, validation/serialization, request context, error handling, schema-driven APIs, graceful shutdown, performance and service architecture.

## Related
Node.js, TypeScript, Zod, OpenAPI, PostgreSQL, Pino.