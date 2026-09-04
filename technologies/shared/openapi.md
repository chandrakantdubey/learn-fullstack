# OpenAPI

**Role:** Primary | **Layer:** Shared/API

## What it is
OpenAPI is a machine-readable description of HTTP APIs: paths, operations, parameters, request bodies, responses, authentication and schemas.

## Mental model
Treat the API description as an executable contract between producers and consumers. It should explain what crosses the network, not duplicate internal domain design.

## Core areas
- paths and operations
- parameters and request/response schemas
- reusable components
- security schemes
- examples and error responses
- versioning and compatibility
- documentation and client generation

## Production patterns
Design stable resource and command contracts, document errors, pagination, idempotency and authentication explicitly. Validate generated clients and specifications in CI. Keep internal fields out of public schemas.

## Relationship to validation
OpenAPI describes the contract; runtime validators enforce it. In TypeScript, Zod can provide runtime schemas and JSON Schema/OpenAPI integration. In Python, Pydantic commonly plays the validation role.

## Common mistakes
Treating generated documentation as automatically correct, exposing implementation details, changing response shapes casually, or documenting only happy paths.

## Related
Zod, Pydantic, Fastify, FastAPI, HTTP, API versioning.
