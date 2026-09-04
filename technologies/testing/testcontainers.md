# Testcontainers

**Role:** Primary | **Layer:** Integration testing

## Mental model
Testcontainers starts real infrastructure dependencies in disposable containers so tests exercise realistic database, queue or service behavior.

## Learn
- container lifecycle
- wait strategies
- reusable vs isolated containers
- networked dependencies
- test data setup/cleanup
- CI runtime considerations

## Production testing
Use real dependencies where mocks would hide integration failures. Keep test data deterministic and control startup cost with appropriate fixture/container scope.

## Related
Docker, PostgreSQL, Redis, pytest, Vitest integration tests.
