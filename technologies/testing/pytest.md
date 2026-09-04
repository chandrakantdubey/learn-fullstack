# pytest

**Role:** Primary | **Layer:** Python testing

## Mental model
pytest is a Python testing framework built around simple test functions, fixtures, parametrization and a rich plugin ecosystem.

## Learn
- assertions and collection
- fixtures and scopes
- parametrization
- monkeypatching/mocking
- async tests
- coverage
- integration test organization

## Production
Keep fixtures explicit, isolate external resources, use real database containers for important integration behavior, and avoid globally shared mutable fixtures.

## Related
Python, FastAPI, SQLAlchemy, Testcontainers.
