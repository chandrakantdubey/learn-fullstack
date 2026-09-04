# FastAPI

**Role:** Primary | **Layer:** Python backend

## Mental model
FastAPI maps HTTP requests to Python functions using type-aware dependency injection and schema generation, commonly backed by Pydantic.

## Learn
- routing and dependency injection
- request/response models
- async endpoints
- middleware and exception handlers
- OpenAPI generation
- background work and lifespan
- authentication dependencies

## Production
Keep API models separate from domain models when necessary, validate all untrusted input, define stable error contracts, set timeouts, instrument requests, and avoid blocking operations in async handlers.

## Related
Python, Pydantic, SQLAlchemy, OpenAPI, pytest.
