# Technology Notes

This directory is the **canonical home for technology-specific notes**.

## Canonical rule

**One technology = one canonical note.**

Examples:

- Zod → `shared/zod.md`
- React → `frontend/react.md`
- Fastify → `backend/fastify.md`
- PostgreSQL → `data/postgresql.md`
- Docker → `infrastructure/docker.md`

Concepts such as validation, caching, authentication, queues and API design belong in concept/pattern documents. Technology notes explain the technology and its operational trade-offs.

## Required depth standard

A **Primary** technology note should cover the relevant parts of:

1. What it is and what problem it solves
2. Mental model
3. Core primitives
4. How it works
5. Setup and idiomatic usage
6. Production architecture/patterns
7. Security
8. Performance and resource behavior
9. Failure modes and recovery
10. Testing
11. Observability/debugging
12. Common mistakes
13. Alternatives and trade-offs
14. When to use / when not to use
15. Useful commands/APIs
16. Small implementation example
17. Production-shaped example
18. Related concepts

Not every technology needs equal depth. Primary technologies used in the canonical stack deserve the deepest treatment. Awareness/alternative technologies should stay concise unless an implementation exercise makes deeper study necessary.

## Technology mastery gate

A technology is not mastered by reading its API.

For a primary technology, prove:

```text
understand mechanism
→ build a small version
→ use idiomatic APIs
→ debug a real failure
→ test important behavior
→ observe it
→ measure resource/performance behavior
→ secure it
→ explain alternatives
→ defend the trade-off
```

## Avoid duplication

Do not create another technology note merely because the technology appears in another layer. Link the canonical note and add cross-layer behavior to the appropriate concept document.

## Categories

- `shared/` — cross-layer technologies
- `frontend/` — browser/UI/application technologies
- `backend/` — server/API technologies
- `data/` — databases, caches, search and vectors
- `infrastructure/` — Linux, containers, Kubernetes, cloud, IaC and CI/CD
- `observability/` — telemetry technologies
- `security/` — security tooling and identity technologies
- `ai/` — AI/ML/LLM technologies
- `testing/` — testing tools
- `developer-tools/` — API, CLI, build and development tooling

The broad inventory lives in `docs/technology-inventory.md`. The registry in `technologies/registry.md` decides which technologies are Primary, Alternative or Awareness.
