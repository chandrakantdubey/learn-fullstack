# Docker Compose

**Role:** Primary | **Layer:** Local orchestration

## Mental model
Compose declares a multi-container application: services, networks, volumes, environment and dependencies.

## Learn
- service definitions
- networks and DNS
- volumes
- health checks
- profiles
- environment configuration
- build vs image

## Production use
Use Compose mainly for local development, integration tests and reproducible multi-service environments. Do not mistake `depends_on` for application readiness; services still need retry/readiness behavior.

## Related
Docker, PostgreSQL, Redis, Testcontainers.
