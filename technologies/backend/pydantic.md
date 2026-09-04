# Pydantic

**Role:** Primary | **Layer:** Python validation

## Mental model
Pydantic turns Python type declarations into runtime parsing and validation models. It is the Python-side counterpart to boundary validation, not a replacement for domain rules.

## Learn
- BaseModel and field definitions
- nested models and unions
- strict vs coercive validation
- validators and serializers
- model/schema serialization
- settings/configuration
- JSON Schema/OpenAPI integration

## Production
Validate at trust boundaries, bound strings/numbers/collections, distinguish missing from null, avoid hidden coercion when unsafe, and never log sensitive validation payloads.

## Related
FastAPI, Python, OpenAPI, Zod.
