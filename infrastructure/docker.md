# Docker

Docker is the packaging boundary between an application and the machine that runs it.

## Mental model

```text
Source
  ↓
Dockerfile
  ↓
Image
  ↓
Registry
  ↓
Container
  ↓
Network / Volume / Runtime
```

A container is a process with filesystem, network, resource, and isolation boundaries. The image is the immutable artifact used to create that process.

## Understand

- image layers
- build context
- Dockerfile instructions
- entrypoint vs command
- ports
- environment variables
- volumes and bind mounts
- bridge networks
- health checks
- resource limits
- registries
- multi-stage builds
- build cache
- rootless containers
- image provenance and scanning

## Production image baseline

```dockerfile
FROM python:3.12-slim AS runtime
WORKDIR /app
COPY pyproject.toml uv.lock ./
RUN pip install --no-cache-dir uv && uv sync --frozen --no-dev
COPY app ./app
USER 10001
CMD ["uv", "run", "python", "-m", "app"]
```

The exact runtime changes by stack, but the principles do not: small image, deterministic dependency installation, non-root execution, explicit startup, no secrets baked into layers.

## Failure modes

- container exits immediately
- wrong architecture image
- missing environment variable
- file permission problems
- DNS/network assumptions that only work on a developer laptop
- dependency installed during build but missing from runtime stage
- state written to an ephemeral filesystem
- image drift caused by floating tags

## Production rules

- pin important base images and dependencies
- use `.dockerignore`
- run as non-root
- separate build and runtime stages
- keep secrets outside images
- log to stdout/stderr
- define health checks where appropriate
- treat containers as disposable
- keep persistent state in managed services or explicit volumes

## Python vs TypeScript

Python commonly uses `uv` or a lockfile-aware package workflow before copying application code. TypeScript commonly uses `pnpm`/npm with a lockfile and a dedicated build stage.

## Project proof

Containerize the fullstack task system with separate frontend, API, worker, PostgreSQL, and Redis services. Verify startup ordering, health checks, persistent database storage, and production-style images.