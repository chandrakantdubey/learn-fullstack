# Technology Registry

This is the working list of technologies for which we will create and maintain notes.

`Primary` means the repository's default technology. `Alternative` means a technology worth knowing when its trade-offs matter. Alternatives stay in the inventory until we decide to create dedicated notes for them.

## Shared

| Technology | Role | Status |
| --- | --- | --- |
| TypeScript | Typed application language | Primary |
| JavaScript | Runtime/language foundation | Primary |
| Zod | TypeScript runtime schemas and validation | Primary |
| OpenAPI | REST API contract | Primary |
| Git | Version control | Primary |
| Linux | Operating-system foundation | Primary |

## Frontend

| Technology | Role | Status |
| --- | --- | --- |
| React | UI library | Primary |
| Next.js | React fullstack framework | Primary |
| Tailwind CSS | Styling system | Primary |
| Radix UI | Accessible component primitives | Primary |
| shadcn/ui | Application component system | Primary |
| Zustand | Client state | Primary |
| TanStack Query | Server state/data fetching | Primary |
| React Hook Form | Form state | Primary |
| Vite | Standalone frontend build tool | Primary |
| pnpm | Package manager | Primary |

## Backend

| Technology | Role | Status |
| --- | --- | --- |
| Node.js | JavaScript runtime | Primary |
| Fastify | TypeScript HTTP framework | Primary |
| Python | Backend/AI language | Primary |
| FastAPI | Python API framework | Primary |
| Pydantic | Python runtime validation | Primary |
| SQLAlchemy | Python database toolkit/ORM | Primary |
| Alembic | Python database migrations | Primary |
| httpx | Python HTTP client | Primary |
| Celery | Python background work | Primary |
| Pino | Node.js structured logging | Primary |

## Data

| Technology | Role | Status |
| --- | --- | --- |
| PostgreSQL | Relational database | Primary |
| Redis | Cache / key-value / coordination | Primary |
| pgvector | Vector search in PostgreSQL | Primary |
| OpenSearch | Search | Primary |
| MongoDB | Document database | Awareness |

## Distributed Systems / Messaging

| Technology | Role | Status |
| --- | --- | --- |
| Kafka | Event streaming | Primary |
| Amazon SQS | Queue | Primary |
| Amazon EventBridge | Event routing | Primary |
| RabbitMQ | Message broker | Alternative |
| Temporal | Durable workflows | Awareness |

## Infrastructure

| Technology | Role | Status |
| --- | --- | --- |
| Docker | Containers | Primary |
| Docker Compose | Local multi-service orchestration | Primary |
| Kubernetes | Container orchestration | Primary |
| Helm | Kubernetes packaging | Primary |
| AWS | Primary cloud | Primary |
| Terraform | Infrastructure as Code | Primary |
| GitHub Actions | CI/CD | Primary |

## Observability

| Technology | Role | Status |
| --- | --- | --- |
| OpenTelemetry | Telemetry standard/instrumentation | Primary |
| Prometheus | Metrics | Primary |
| Grafana | Dashboards | Primary |
| Loki | Logs | Awareness |
| Jaeger | Tracing backend | Awareness |
| Tempo | Tracing backend | Awareness |

## Security

| Technology | Role | Status |
| --- | --- | --- |
| OWASP | Application security guidance | Primary |
| CodeQL | Code security analysis | Primary |
| Trivy | Container/dependency scanning | Primary |
| SOPS | Encrypted configuration/secrets | Awareness |
| Vault | Secrets management | Awareness |

## Testing

| Technology | Role | Status |
| --- | --- | --- |
| Vitest | TypeScript unit/component testing | Primary |
| Playwright | Browser E2E testing | Primary |
| Testing Library | UI testing principles/tools | Primary |
| pytest | Python testing | Primary |
| Testcontainers | Integration testing with real dependencies | Primary |
| k6 | Load testing | Primary |

## AI / ML

| Technology | Role | Status |
| --- | --- | --- |
| PyTorch | Deep learning | Primary |
| scikit-learn | Classical ML | Primary |
| Hugging Face Transformers | Transformer models | Primary |
| sentence-transformers | Embeddings | Primary |
| OpenAI SDK | Model APIs | Primary |
| LiteLLM | Model provider abstraction | Primary |
| LangGraph | Agent/workflow orchestration | Primary |
| pgvector | Vector retrieval | Primary |
| Langfuse | LLM observability/evaluation | Primary |
| vLLM | Model serving | Primary |
| MCP | Tool/context interoperability | Primary |

## Principle

Do not create a separate note for every library that appears in the ecosystem inventory.

Create a note when the technology is part of the engineering model we actually want to learn. Keep alternatives visible without allowing the repository to become a library catalog.
