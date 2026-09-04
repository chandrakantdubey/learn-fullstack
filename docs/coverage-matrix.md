# Fullstack Competency Coverage

This matrix tracks the Fullstack Engineering model against the repository and points each capability at one canonical location.

| Domain | Status | Canonical location |
| --- | --- | --- |
| Programming fundamentals | Covered | `foundations/` |
| Web / Internet | Covered | `web/`, `systems/networking/` |
| Frontend engineering | Covered | `frontend/` |
| TypeScript application engineering | Covered | `typescript/`, `typescript-stack.md` |
| Runtime validation / Zod | Covered | `frontend/concepts/runtime-validation.md`, `backend/concepts/api-contracts-and-validation.md` |
| Backend engineering | Covered | `backend/` |
| Python engineering | Integration track | `python/`; full depth in `learn-python` |
| Relational data | Covered | `data/concepts/`, `data/postgresql.md` |
| Redis / caching | Covered | `data/concepts/redis.md` |
| NoSQL | Covered | `data/nosql-search-vectors.md` |
| Search | Covered | `data/nosql-search-vectors.md` |
| Vector databases | Covered | `data/nosql-search-vectors.md` |
| Linux | Covered | `systems/linux/` |
| Networking | Covered | `systems/networking/` |
| Distributed systems | Covered | `systems/distributed-systems.md` |
| Messaging / events | Covered | `backend/concepts/messaging-and-events.md` |
| Security | Covered | `production/security.md`, `backend/concepts/authentication-and-security.md` |
| Testing | Covered | `production/`, frontend testing notes |
| Observability | Covered | `production/observability.md` |
| Reliability | Covered | `production/reliability.md` |
| Performance | Covered | `production/performance-and-capacity.md`, frontend performance |
| Capacity planning | Covered | `production/performance-and-capacity.md` |
| Docker | Covered | `infrastructure/docker.md` |
| Kubernetes | Covered | `infrastructure/kubernetes.md` |
| Cloud | Covered | `infrastructure/aws.md`, `infrastructure/cloud-architecture.md` |
| Terraform / IaC | Covered | `infrastructure/terraform.md` |
| CI/CD | Covered | `infrastructure/ci-cd.md` |
| System design | Covered | `architecture/` |
| AI engineering bridge | Integration track | `docs/skill-map.md`, `docs/stack.md`; `learn-ai` remains the deep-dive source |
| DSA / CS | Integration track | `learn-dsa` remains the deep-dive source |

## Meaning of status

**Covered** means the integrated Fullstack repository contains a first-class explanation of the capability and its production implications.

**Integration track** means this repository defines how the capability fits Fullstack Engineering while the specialized repository remains the deeper source of truth.

## Curation rule

The repository should have a small canonical stack. Large technology inventories are reference material, not a list of things to learn simultaneously. New tools should be added to the appropriate capability first and only then included in inventories when they have a clear role.

## Original model preserved

The repository is not intended to replace specialized repositories. It is the integration layer that connects them into one production engineering mental model.
