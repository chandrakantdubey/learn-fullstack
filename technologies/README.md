# Technology Notes

This directory is the **canonical home for technology-specific notes**.

The important rule is **one technology = one canonical note file**.

A technology that is used across multiple layers is not duplicated. For example:

- Zod has one note: `shared/zod.md`.
- React has one note: `frontend/react.md`.
- Fastify has one note: `backend/fastify.md`.
- PostgreSQL has one note: `data/postgresql.md`.
- Docker has one note: `infrastructure/docker.md`.

Concepts such as validation, caching, authentication, queues, and API design belong in concept/pattern documents. Technology files explain the technology itself and link back to those concepts.

## Technology note template

Each technology note will eventually cover:

1. What it is
2. Why it exists
3. Mental model
4. Core primitives
5. How it works
6. Installation / setup
7. Idiomatic usage
8. Production patterns
9. Security
10. Performance
11. Failure modes
12. Testing
13. Observability
14. Common mistakes
15. Alternatives and trade-offs
16. When to use / when not to use
17. Useful commands / APIs
18. Small examples
19. Production example
20. Related concepts and technologies

The notes are deliberately not tutorials. They are a durable engineering reference that we will fill progressively.

## Categories

- `shared/` — technologies used across frontend and backend or multiple layers
- `frontend/` — browser/UI/application technologies
- `backend/` — server/API technologies
- `data/` — databases, caches, search, vectors
- `infrastructure/` — Linux, containers, Kubernetes, cloud, IaC, CI/CD
- `observability/` — telemetry and monitoring technologies
- `security/` — security tooling and identity technologies
- `ai/` — AI/ML/LLM technologies
- `testing/` — testing tools
- `developer-tools/` — API, CLI, build and development tooling

The broader inventory remains in `docs/technology-inventory.md`. This directory is where we build the actual notes for the selected technologies.
