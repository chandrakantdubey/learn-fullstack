# Fullstack Competency Coverage

This is the implementation index for the canonical 20-section master skill universe in `docs/master-skill-universe.md`.

| # | Master section | Primary home | Fullstack role |
|---|---|---|---|
| 1 | CS / Engineering Fundamentals | `learn-dsa`, `learn-js-ts`, `learn-python` | cross-language mental models, runtime/resource implications |
| 2 | Networking | `learn-fullstack` | protocols, topology, service boundaries |
| 3 | Linux | `learn-fullstack` | OS/resource mental models and troubleshooting |
| 4 | Databases | `learn-sql` | application consistency, cache/search integration |
| 5 | Backend | `learn-backend` | end-to-end service architecture |
| 6 | Frontend | `learn-frontend` | browser/API/system boundaries |
| 7 | Fullstack Engineering | `learn-fullstack` | primary owner |
| 8 | AI Engineering | `learn-ai` | AI product/system integration |
| 9 | Cloud | `learn-fullstack` + `learn-docker` | architecture, service selection and deployment |
| 10 | Containers | `learn-docker` | application-to-runtime deployment path |
| 11 | Kubernetes | `learn-docker` | architecture and trade-offs in Fullstack |
| 12 | IaC / DevOps | `learn-fullstack` + `learn-docker` | infrastructure/release synthesis |
| 13 | Observability / SRE | `learn-fullstack` | primary owner |
| 14 | Security | `learn-fullstack` + specialized implementations | cross-stack threat model and controls |
| 15 | System Design | `learn-fullstack` | primary owner |
| 16 | Architecture / Code Design | `learn-fullstack` | primary owner |
| 17 | Testing / Quality | `learn-fullstack` + specialized implementations | strategy and quality gates |
| 18 | Developer Tooling | each specialized repo | integrated workflow and standards |
| 19 | Engineering Practices | `learn-fullstack` | primary owner |
| 20 | Interview Skills | `learn-fullstack` + `learn-dsa` | verification and defense |

## Status semantics

**Primary home** means the repository is responsible for the deep implementation material.

**Fullstack role** means the integrated repository explains how that capability interacts with the rest of the system. It is not a duplicate course.

## Canonical technology rule

A technology has one canonical note under `technologies/`. Concepts are separate from technology notes. For example, Zod is shared through `technologies/shared/zod.md` rather than duplicated across frontend/backend sections.

## Completion gate

Coverage is not a keyword checklist. Each important capability must ultimately support:

**Understand → Implement → Debug → Measure → Secure → Test → Scale → Operate → Defend trade-offs.**

The master list, source maps, projects and interview map are the verification chain.