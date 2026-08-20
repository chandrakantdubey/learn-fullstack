# Python API

FastAPI reference implementation for the Fullstack Task System.

Initial vertical slice:

- health endpoint
- PostgreSQL connection
- migrations
- task ownership model
- typed request/response contracts
- structured error handling

Implementation order:

1. application bootstrap
2. database session
3. migration
4. task model
5. repository/service boundary
6. CRUD endpoints
7. auth
8. Redis rate limiting/cache
9. background job publishing
10. tests and observability
