# SQLAlchemy

**Role:** Primary | **Layer:** Python data access

## Mental model
SQLAlchemy separates SQL/database concepts from Python application objects and provides an engine, connection pool, SQL expression system and ORM.

## Learn
- engines and connection pools
- transactions and isolation
- Core expressions
- ORM mappings and relationships
- eager/lazy loading
- sessions and unit-of-work
- migrations with Alembic

## Production
Control pool sizes, transaction scope and query count. Inspect generated SQL, avoid accidental lazy-load waterfalls, use explicit transactions, and handle serialization/deadlock retries appropriately.

## Related
PostgreSQL, Alembic, FastAPI, psycopg.
