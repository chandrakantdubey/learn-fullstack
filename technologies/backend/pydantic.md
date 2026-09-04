# Pydantic

**Role:** Primary | **Layer:** Python validation

## What it is

Pydantic provides runtime parsing, validation and serialization models driven by Python type declarations. It is a trust-boundary tool, not a replacement for business/domain rules.

## Mental model

```text
untrusted data
  → parse
  → validate shape + bounds
  → typed model
  → application logic
  → explicit serialization
```

The important distinction is compile-time type checking versus runtime validation. Python annotations alone do not validate incoming JSON, environment variables, database rows, or provider output.

## Core primitives

- `BaseModel`
- fields and defaults
- nested models
- unions and discriminated unions
- constrained values
- validators
- serializers
- model dumping/parsing
- JSON Schema generation
- settings/configuration

## Validation design

Validate at system boundaries:

- HTTP request bodies and query parameters
- environment/configuration
- webhook payloads
- queue/job messages
- external API responses
- LLM structured output and tool arguments

Prefer explicit constraints for lengths, ranges, counts and formats. Distinguish missing fields from explicit `null` when the API contract requires it.

## Coercion vs strictness

Pydantic can coerce compatible input. That is convenient for some user-facing data but dangerous when type fidelity matters. Choose strict behavior deliberately for identifiers, security-sensitive values, money, protocol fields and other domains where silent conversion can hide defects.

## Models are not domain truth

A Pydantic model can establish that a request has the right shape. It cannot by itself establish that an order is payable, a user owns a resource, or a state transition is legal. Those require application/domain logic and often database state.

## Serialization

Define what crosses each boundary. Avoid serializing internal fields accidentally. Treat serialized schemas as contracts and version breaking changes deliberately.

Use separate input and output models when accepting and returning different fields. This is especially important for secrets, internal identifiers and mutable server-owned state.

## FastAPI integration

FastAPI uses Pydantic models for request parsing, validation, response schemas and OpenAPI generation. Keep this integration at the transport boundary and keep domain models independent when that improves separation.

## Production checklist

- bounded strings, arrays and numeric fields
- explicit required/default/null semantics
- deliberate coercion policy
- separate public DTOs where needed
- no secrets in validation errors/logs
- schema compatibility reviewed before releases
- external responses validated before use
- structured model output validated before side effects

## Failure modes

Watch for trusting annotations as runtime validation, overusing coercion, putting database/business logic in validators, exposing internal models, accepting unbounded collections, and treating successful parsing as authorization.

## Testing

Test valid, invalid, boundary and adversarial inputs. Include schema compatibility tests for public APIs and provider payloads. Verify serialization output rather than testing only Python object construction.

## Related

FastAPI, Python, OpenAPI, SQLAlchemy, Zod and the fullstack API-contract patterns.
