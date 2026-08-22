# Learn Fullstack

A production-oriented Fullstack Engineering knowledge base.

The goal is not to memorize frameworks. The goal is to understand how modern software systems are designed, built, tested, secured, deployed, observed, and evolved.

## What This Repository Is

`learn-fullstack` is the integration layer across the existing specialized learning repositories:

| Repository | Role |
| --- | --- |
| `learn-python` | Python language and ecosystem depth |
| `learn-js-ts` | JavaScript and TypeScript depth |
| `learn-frontend` | Frontend, browser, React, and Next.js depth |
| `learn-backend` | Backend, APIs, distributed systems, and services depth |
| `learn-sql` | SQL and database depth |
| `learn-docker` | Containerization and deployment depth |
| `learn-ai` | AI/ML/LLM engineering depth |
| `learn-dsa` | Data structures and algorithms depth |

This repository connects those subjects into one engineering mental model.

## Core Principle

Learn in this order:

**Principles → Mental Models → Systems → Technologies → Tools/Libraries → Production Patterns → Projects**

A framework is never the starting point.

## The Fullstack Engineer Model

```text
                         PRODUCT / SYSTEM
                                │
          ┌─────────────────────┼─────────────────────┐
          │                     │                     │
       FRONTEND              BACKEND                DATA
          │                     │                     │
    Browser / UI          APIs / Services       SQL / NoSQL
    React / Next          Async / Workers       Cache / Search
    State / UX            Domain Logic          Queues / Events
          │                     │                     │
          └─────────────────────┼─────────────────────┘
                                │
                         SYSTEMS FOUNDATION
                                │
                   Linux / Networking / OS
                                │
                         INFRASTRUCTURE
                                │
                 Docker / Kubernetes / Cloud
                         Terraform / CI/CD
                                │
                       PRODUCTION ENGINEERING
                                │
              Security / Testing / Observability
                       Reliability / Performance
                                │
                              AI
                                │
              ML / LLMs / RAG / Agents / Serving
```

## Repository Structure

```text
learn-fullstack/
├── foundations/       # programming, CS, web, networking, Linux
├── web/               # HTTP, DNS, TLS, browser and internet fundamentals
├── frontend/          # frontend engineering and architecture
├── backend/           # APIs, services, async, distributed systems
├── data/              # SQL, PostgreSQL, Redis, search, NoSQL, vectors
├── systems/           # OS, networking, concurrency, performance
├── infrastructure/    # Docker, Kubernetes, cloud, Terraform, CI/CD
├── production/        # security, testing, observability, reliability
├── python/            # Python as the primary backend/AI implementation stack
├── typescript/        # TypeScript as the primary browser/server implementation stack
├── architecture/      # system design and architectural trade-offs
├── fullstack-patterns/ # cross-layer patterns used in real applications
├── projects/          # production-oriented end-to-end projects
└── docs/              # curriculum, source map, decisions, glossary
```

## Canonical Stacks

### Primary

- **Frontend:** TypeScript, React, Next.js
- **Backend:** Python/FastAPI and TypeScript/Node.js
- **Database:** PostgreSQL
- **Cache:** Redis
- **Search:** OpenSearch/Elasticsearch concepts
- **Messaging:** Kafka and cloud queues
- **Containers:** Docker
- **Orchestration:** Kubernetes
- **Cloud:** AWS
- **Infrastructure:** Terraform
- **CI/CD:** GitHub Actions
- **Observability:** OpenTelemetry, Prometheus, Grafana
- **Testing:** pytest, Vitest/Jest, Playwright

### AI extension

- PyTorch and scikit-learn foundations
- Transformers and model APIs
- Embeddings and vector search
- RAG
- Evaluation
- Agents/workflows
- Model serving and inference infrastructure

## Learning Style

This is deliberately **not a conventional course**.

A topic should answer:

1. What problem does this solve?
2. What mental model explains it?
3. What are the important invariants and trade-offs?
4. How is it implemented?
5. What can fail in production?
6. Which technology/tool implements it?
7. How do Python and TypeScript differ in implementation?
8. Where does it fit into an end-to-end system?
9. What should I build to prove I understand it?

## Source Repositories

Existing material is treated as source material, not copied blindly. The consolidation rules are documented in [`docs/source-map.md`](docs/source-map.md).

## Status

Initial repository architecture. Content is being consolidated and rewritten around engineering capabilities rather than isolated technologies.


## Interview
| Area                | Interview Questions                                                                                      | Coding / Problems                                                                                  | Hands-on Practice                                                                                   |
| ------------------- | -------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- |
| **JavaScript**      | [Frontend Interview Handbook](https://www.frontendinterviewhandbook.com?utm_source=chatgpt.com)          | [BigFrontend.dev](https://bigfrontend.dev?utm_source=chatgpt.com)                                  | [Frontend Mentor](https://www.frontendmentor.io?utm_source=chatgpt.com)                             |
| **TypeScript**      | [Total TypeScript](https://www.totaltypescript.com?utm_source=chatgpt.com)                               | [TypeScript Exercises](https://typescript-exercises.github.io?utm_source=chatgpt.com)              | [TypeScript Playground](https://www.typescriptlang.org/play?utm_source=chatgpt.com)                 |
| **React**           | [GreatFrontEnd](https://www.greatfrontend.com?utm_source=chatgpt.com)                                    | [BigFrontend.dev](https://bigfrontend.dev?utm_source=chatgpt.com)                                  | [Frontend Mentor](https://www.frontendmentor.io?utm_source=chatgpt.com)                             |
| **Next.js**         | [Next.js Learn](https://nextjs.org/learn?utm_source=chatgpt.com)                                         | [Next.js Examples](https://github.com/vercel/next.js/tree/canary/examples?utm_source=chatgpt.com)  | [Vercel Templates](https://vercel.com/templates?utm_source=chatgpt.com)                             |
| **Python**          | [Real Python](https://realpython.com?utm_source=chatgpt.com)                                             | [Codewars](https://www.codewars.com?utm_source=chatgpt.com)                                        | [Exercism Python](https://exercism.org/tracks/python?utm_source=chatgpt.com)                        |
| **FastAPI**         | [FastAPI Docs](https://fastapi.tiangolo.com?utm_source=chatgpt.com)                                      | [CodeQuestions / GitHub projects](https://github.com/topics/fastapi?utm_source=chatgpt.com)        | [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/?utm_source=chatgpt.com)                   |
| **Django**          | [Django Docs](https://docs.djangoproject.com?utm_source=chatgpt.com)                                     | [Django REST Framework](https://www.django-rest-framework.org?utm_source=chatgpt.com)              | [Django Girls Tutorial](https://tutorial.djangogirls.org?utm_source=chatgpt.com)                    |
| **DSA**             | [LeetCode](https://leetcode.com?utm_source=chatgpt.com)                                                  | [LeetCode](https://leetcode.com?utm_source=chatgpt.com)                                            | [NeetCode](https://neetcode.io?utm_source=chatgpt.com)                                              |
| **SQL**             | [DataLemur](https://datalemur.com?utm_source=chatgpt.com)                                                | [StrataScratch](https://www.stratascratch.com?utm_source=chatgpt.com)                              | [SQLBolt](https://sqlbolt.com?utm_source=chatgpt.com)                                               |
| **PostgreSQL**      | [PostgreSQL Docs](https://www.postgresql.org/docs/?utm_source=chatgpt.com)                               | [PGExercises](https://pgexercises.com?utm_source=chatgpt.com)                                      | [PostgreSQL Tutorial](https://www.postgresql.org/docs/current/tutorial.html?utm_source=chatgpt.com) |
| **MongoDB**         | [MongoDB University](https://learn.mongodb.com?utm_source=chatgpt.com)                                   | [MongoDB Exercises](https://www.mongodb.com/docs/atlas/sample-data/?utm_source=chatgpt.com)        | [MongoDB University](https://learn.mongodb.com?utm_source=chatgpt.com)                              |
| **Redis**           | [Redis Docs](https://redis.io/docs/latest/?utm_source=chatgpt.com)                                       | [Redis University](https://university.redis.io?utm_source=chatgpt.com)                             | [Redis Tutorials](https://redis.io/tutorials/?utm_source=chatgpt.com)                               |
| **REST APIs**       | [REST API Tutorial](https://restfulapi.net?utm_source=chatgpt.com)                                       | [Postman Academy](https://academy.postman.com?utm_source=chatgpt.com)                              | [Postman](https://www.postman.com?utm_source=chatgpt.com)                                           |
| **GraphQL**         | [GraphQL Learn](https://graphql.org/learn/?utm_source=chatgpt.com)                                       | [How to GraphQL](https://www.howtographql.com?utm_source=chatgpt.com)                              | [Apollo](https://www.apollographql.com/docs/?utm_source=chatgpt.com)                                |
| **WebSockets**      | [MDN WebSockets](https://developer.mozilla.org/en-US/docs/Web/API/WebSockets_API?utm_source=chatgpt.com) | [Socket.IO](https://socket.io?utm_source=chatgpt.com)                                              | [Socket.IO Tutorial](https://socket.io/docs/v4/tutorial/introduction?utm_source=chatgpt.com)        |
| **System Design**   | [Hello Interview](https://www.hellointerview.com?utm_source=chatgpt.com)                                 | [System Design Primer](https://github.com/donnemartin/system-design-primer?utm_source=chatgpt.com) | [ByteByteGo](https://bytebytego.com?utm_source=chatgpt.com)                                         |
| **LLD/OOD**         | [Design Gurus](https://www.designgurus.io?utm_source=chatgpt.com)                                        | [Refactoring.Guru](https://refactoring.guru?utm_source=chatgpt.com)                                | [Excalidraw](https://excalidraw.com?utm_source=chatgpt.com)                                         |
| **Security**        | [OWASP](https://owasp.org?utm_source=chatgpt.com)                                                        | [PortSwigger Web Security Academy](https://portswigger.net/web-security?utm_source=chatgpt.com)    | [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/?utm_source=chatgpt.com)                |
| **Testing JS**      | [Testing Library](https://testing-library.com?utm_source=chatgpt.com)                                    | [Jest](https://jestjs.io?utm_source=chatgpt.com)                                                   | [Playwright](https://playwright.dev?utm_source=chatgpt.com)                                         |
| **Testing Python**  | [pytest](https://docs.pytest.org?utm_source=chatgpt.com)                                                 | [pytest docs](https://docs.pytest.org?utm_source=chatgpt.com)                                      | [Real Python Testing](https://realpython.com/pytest-python-testing/?utm_source=chatgpt.com)         |
| **Docker**          | [Docker Docs](https://docs.docker.com?utm_source=chatgpt.com)                                            | [Play with Docker](https://labs.play-with-docker.com?utm_source=chatgpt.com)                       | [Docker Labs](https://github.com/docker/labs?utm_source=chatgpt.com)                                |
| **AWS**             | [AWS Skill Builder](https://skillbuilder.aws?utm_source=chatgpt.com)                                     | [AWS Workshops](https://workshops.aws?utm_source=chatgpt.com)                                      | [AWS Free Tier](https://aws.amazon.com/free/?utm_source=chatgpt.com)                                |
| **Git/GitHub**      | [GitHub Skills](https://skills.github.com?utm_source=chatgpt.com)                                        | [Learn Git Branching](https://learngitbranching.js.org?utm_source=chatgpt.com)                     | [GitHub Skills](https://skills.github.com?utm_source=chatgpt.com)                                   |
| **CI/CD**           | [GitHub Actions Docs](https://docs.github.com/en/actions?utm_source=chatgpt.com)                         | [GitHub Skills](https://skills.github.com?utm_source=chatgpt.com)                                  | [GitHub Actions](https://docs.github.com/en/actions?utm_source=chatgpt.com)                         |
| **Kubernetes**      | [Kubernetes Docs](https://kubernetes.io/docs/?utm_source=chatgpt.com)                                    | [KillerCoda Kubernetes](https://killercoda.com/kubernetes?utm_source=chatgpt.com)                  | [Play with Kubernetes](https://labs.play-with-k8s.com?utm_source=chatgpt.com)                       |
| **Kafka**           | [Confluent Developer](https://developer.confluent.io?utm_source=chatgpt.com)                             | [Kafka Tutorials](https://kafka.apache.org/quickstart?utm_source=chatgpt.com)                      | [Confluent Developer](https://developer.confluent.io?utm_source=chatgpt.com)                        |
| **Performance**     | [web.dev](https://web.dev?utm_source=chatgpt.com)                                                        | [Chrome DevTools](https://developer.chrome.com/docs/devtools/?utm_source=chatgpt.com)              | [WebPageTest](https://www.webpagetest.org?utm_source=chatgpt.com)                                   |
| **Observability**   | [OpenTelemetry](https://opentelemetry.io?utm_source=chatgpt.com)                                         | [Grafana Labs](https://grafana.com/tutorials/?utm_source=chatgpt.com)                              | [Grafana Playground](https://play.grafana.org?utm_source=chatgpt.com)                               |
| **Behavioral**      | [Exponent](https://www.tryexponent.com?utm_source=chatgpt.com)                                           | [IGotAnOffer](https://igotanoffer.com?utm_source=chatgpt.com)                                      | [interviewing.io](https://interviewing.io?utm_source=chatgpt.com)                                   |
| **Mock Interviews** | [interviewing.io](https://interviewing.io?utm_source=chatgpt.com)                                        | [Pramp](https://www.pramp.com?utm_source=chatgpt.com)                                              | [Hello Interview](https://www.hellointerview.com?utm_source=chatgpt.com)                            |

