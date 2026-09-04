# Docker

**Role:** Primary | **Layer:** Infrastructure

## Mental model
Docker packages an application filesystem and runtime configuration into images executed as isolated containers using Linux kernel primitives.

## Learn
- images, layers and registries
- Dockerfile instructions and build cache
- multi-stage builds
- networking and volumes
- resource limits
- signals and PID 1
- health checks
- rootless/least-privilege execution

## Production
Use minimal trusted base images, deterministic builds, non-root users, pinned dependencies, secret-free images, health checks and resource limits. Scan images and keep build context small.

## Related
Docker Compose, Kubernetes, Helm, Linux, Trivy.
