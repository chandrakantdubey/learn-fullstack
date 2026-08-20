# Concepts → Frameworks → Tools → Libraries

This repository uses four implementation layers after the engineering concepts.

## Concepts

Explain the problem, mental model, mechanism, contracts, trade-offs, failure modes, security, performance, and operational behavior.

Examples:

- HTTP semantics
- relational modeling
- transactions
- caching
- concurrency
- authentication
- distributed consistency
- container isolation

## Frameworks

Provide an opinionated application or infrastructure structure.

Examples:

- React
- Next.js
- FastAPI
- Django
- Fastify
- Kubernetes

## Tools

Standalone tools used to develop, inspect, test, package, deploy, or operate systems.

Examples:

- Git
- curl
- Docker CLI
- kubectl
- Helm
- Terraform CLI
- GitHub Actions
- k6

## Libraries

Reusable packages embedded in an application or service.

Examples:

- Pydantic
- SQLAlchemy
- psycopg
- redis-py
- Zod
- OpenTelemetry SDK
- Playwright

## Placement test

Ask:

> If I removed the framework, would the underlying engineering concept still exist?

If yes, the concept belongs in `concepts/`.

Ask:

> Does this package provide application structure and conventions across a broad part of the system?

If yes, it is probably a framework.

Ask:

> Is this primarily a standalone executable, CLI, build/deployment/debugging system, or operational service?

If yes, it belongs in `tools/`.

Otherwise, when it is imported into application code to provide focused capability, it belongs in `libraries/`.
