# Fullstack Engineer — Technology Foundation

This document is the original Fullstack Engineer technology model we defined before restructuring the repository.

The target should be: **someone who can take a system from browser → API → database → infrastructure → production**, not someone who merely knows React + Node.

---

# Fullstack Engineer — Technology Foundation

Think of the engineer as having this stack:

```text
                    ┌──────────────────────────┐
                    │     Product / System     │
                    └────────────┬─────────────┘
                                 │
              ┌──────────────────┴──────────────────┐
              │                                     │
        Frontend Engineering                 Backend Engineering
              │                                     │
       Browser / Web APIs                     APIs / Services
       React / UI Architecture                Business Logic
       State / Forms                           Async / Workers
       Performance                             Distributed Systems
              │                                     │
              └──────────────────┬──────────────────┘
                                 │
                         Data Engineering
                                 │
                ┌────────────────┼────────────────┐
                │                │                │
             SQL/DB           Cache          Messaging
                │                │                │
                └────────────────┼────────────────┘
                                 │
                          Operating Systems
                                 │
                         Linux / Networking
                                 │
                       Infrastructure / Cloud
                                 │
                    Docker / Kubernetes / IaC
                                 │
                       CI/CD / Observability
                                 │
                         Security / Reliability
```

The important thing is that **frameworks sit on top of these fundamentals**.

---

# 1. Programming Fundamentals

Before discussing Python or JS specifically, a Fullstack Engineer should be comfortable with:

### Core programming

- Data structures
- Algorithms
- Complexity
- Memory management concepts
- Error handling
- Exceptions
- Concurrency
- Parallelism
- Async programming
- Functional programming concepts
- Object-oriented programming
- Modules/packages
- Dependency management
- Type systems
- Generics
- Interfaces
- Immutability
- Serialization/deserialization
- Testing

### Engineering practices

- Clean code
- SOLID
- DRY / KISS
- Composition over inheritance
- Separation of concerns
- Design patterns
- Refactoring
- Code review
- Version control
- Git workflows

You don't need to memorize design patterns.

You **do** need to recognize:

> "This code is becoming tightly coupled; I need to introduce a boundary."

That's the actual skill.

---

# 2. Web / Internet Fundamentals

This is one of the biggest gaps in framework-heavy engineers.

They should understand:

### HTTP

- HTTP/1.1
- HTTP/2
- HTTP/3
- HTTP methods
- Status codes
- Headers
- Cookies
- Sessions
- Caching
- Content negotiation
- Compression
- Multipart
- Streaming
- SSE
- WebSockets

### URLs / DNS

- DNS
- Domain resolution
- A / AAAA
- CNAME
- TXT
- MX
- TTL
- DNS propagation
- CDN routing

### TLS

- HTTPS
- Certificates
- Certificate chains
- TLS handshake
- Certificate renewal
- mTLS

### Browser fundamentals

- DOM
- Rendering
- JavaScript runtime
- Event loop
- Web APIs
- Storage
- Cookies
- CORS
- CSP
- Same-origin policy
- Service workers
- Web Workers

This layer makes everything above it easier.

---

# 3. Frontend Engineering

Not merely "React".

A serious Fullstack Engineer should understand frontend architecture.

### Browser

- DOM
- CSSOM
- Rendering pipeline
- Layout
- Paint
- Composite
- Browser storage
- Browser security
- Event loop
- Network waterfall

### HTML

- Semantic HTML
- Forms
- Accessibility
- SEO
- Metadata
- Progressive enhancement

### CSS

- Cascade
- Specificity
- Box model
- Flexbox
- Grid
- Responsive design
- Animations
- CSS architecture
- Design systems

### JavaScript / TypeScript

- ES modules
- Closures
- Prototypes
- Promises
- async/await
- Event loop
- Web APIs
- Error handling
- TypeScript
- Generics
- Type narrowing
- Type inference

### UI architecture

- Component architecture
- State management
- Server state
- Client state
- Forms
- Validation
- Routing
- Data fetching
- Error boundaries
- Loading states
- Optimistic updates
- Pagination
- Infinite scrolling

### Frontend performance

- Code splitting
- Lazy loading
- Bundle optimization
- Caching
- CDN
- Image optimization
- Core Web Vitals
- SSR
- SSG
- ISR
- Streaming

### Frontend security

- XSS
- CSRF
- Clickjacking
- CSP
- Token handling
- Secure cookies
- OAuth/OIDC

---

# 4. Backend Engineering

This is where a Fullstack Engineer becomes substantially different from a frontend engineer who knows APIs.

### API design

- REST
- RPC
- GraphQL
- gRPC
- WebSockets
- SSE
- API versioning
- Pagination
- Filtering
- Sorting
- Idempotency
- Rate limiting
- Error contracts

### Application architecture

- Layered architecture
- Clean architecture
- Hexagonal architecture
- Modular monolith
- Microservices
- Domain-driven design
- Dependency injection
- Service boundaries

### Runtime concepts

- Processes
- Threads
- Async I/O
- Event loops
- Worker pools
- Connection pools
- Background jobs
- Scheduling

### Reliability

- Timeouts
- Retries
- Exponential backoff
- Circuit breakers
- Bulkheads
- Idempotency
- Dead-letter queues
- Graceful shutdown
- Health checks
- Readiness/liveness

### Performance

- Profiling
- CPU bottlenecks
- Memory leaks
- N+1 queries
- Connection pools
- Caching
- Batching
- Async processing
- Streaming

---

# 5. Database Engineering

This should be a **major competency**, not "I know PostgreSQL".

## Relational databases

At least one deeply:

**PostgreSQL** would be my choice.

Understand:

- Tables
- Relations
- Primary keys
- Foreign keys
- Constraints
- Indexes
- Composite indexes
- Unique indexes
- Partial indexes
- Transactions
- ACID
- Isolation levels
- MVCC
- Locks
- Deadlocks
- Query planner
- EXPLAIN
- Joins
- CTEs
- Window functions
- Views
- Materialized views
- Partitioning
- Replication
- Backups
- Migrations

### Data modeling

- Normalization
- Denormalization
- Access patterns
- Cardinality
- Aggregates
- Audit trails
- Soft deletes
- Temporal data

---

# 6. NoSQL / Distributed Data

Understand the **why**, rather than collecting databases.

### Redis

- Cache
- Key/value
- TTL
- Distributed locks
- Rate limiting
- Pub/Sub
- Streams
- Sessions

### Document databases

Understand something like:

- MongoDB

Concepts:

- Document modeling
- Embedded vs referenced data
- Indexes
- Aggregation
- Transactions

### Search

- Elasticsearch/OpenSearch
- Inverted indexes
- Full-text search
- Relevance
- Filtering
- Aggregations

### Vector databases

Especially relevant for AI engineering:

- pgvector
- Qdrant
- Weaviate
- Milvus

Understand:

- Embeddings
- Similarity search
- ANN
- HNSW
- Metadata filtering
- Hybrid search
- Reranking

---

# 7. Messaging & Event-Driven Systems

A production Fullstack Engineer should eventually understand:

### Messaging

- RabbitMQ
- Kafka
- SQS
- SNS
- Pub/Sub

But again, concepts first:

- Queue
- Topic
- Consumer
- Producer
- Partition
- Offset
- Consumer groups
- Ordering
- Delivery semantics
- At-most-once
- At-least-once
- Exactly-once implications
- Dead-letter queues
- Retry queues
- Backpressure

### Event architecture

```text
Request
   │
   ▼
API
   │
   ├──── DB transaction
   │
   └──── Event
           │
           ├── Email worker
           ├── Analytics
           ├── Search indexing
           └── Notifications
```

This is where backend engineering starts becoming distributed systems engineering.

---

# 8. Linux

**Absolutely essential.**

A Fullstack Engineer shouldn't be dependent on someone else to understand what's happening on a Linux server.

### Linux fundamentals

- Filesystem
- Processes
- Threads
- Signals
- Permissions
- Users/groups
- Environment variables
- Services
- systemd
- Logs
- File descriptors
- stdin/stdout/stderr
- Pipes
- Shell
- Bash
- Cron

### CLI

- `grep`
- `sed`
- `awk`
- `find`
- `xargs`
- `curl`
- `wget`
- `jq`
- `ssh`
- `scp`
- `rsync`
- `tar`
- `ps`
- `top`
- `htop`
- `lsof`
- `ss`
- `netstat`
- `df`
- `du`
- `free`
- `journalctl`

### Debugging

They should be able to answer:

> Why is this service returning 502?

without immediately opening Kubernetes.

---

# 9. Networking

This is another foundational layer.

Understand:

```text
Browser
   ↓
DNS
   ↓
CDN
   ↓
Load Balancer
   ↓
Reverse Proxy
   ↓
Application
   ↓
Database
```

And understand what's actually happening.

### Concepts

- TCP
- UDP
- IP
- Ports
- Sockets
- Routing
- NAT
- Subnets
- CIDR
- IPv4/IPv6
- DNS
- DHCP
- TLS
- HTTP
- Load balancing
- Reverse proxies
- Firewalls

### Tools

- `curl`
- `dig`
- `nslookup`
- `ping`
- `traceroute`
- `nc`
- `ss`
- `tcpdump`

---

# 10. Git

Not just:

```bash
git add .
git commit
git push
```

Understand:

- Branches
- Merge
- Rebase
- Cherry-pick
- Revert
- Reset
- Stash
- Tags
- Bisect
- Reflog
- Merge conflicts
- Commit history
- Conventional commits
- Release tagging

And GitHub:

- PRs
- Reviews
- CODEOWNERS
- Branch protection
- Actions
- Releases
- Dependabot
- Security scanning

---

# 11. Docker

A Fullstack Engineer should be able to containerize almost anything.

Understand:

- Images
- Containers
- Layers
- Dockerfile
- Build context
- Multi-stage builds
- Volumes
- Networks
- Environment variables
- Secrets
- Health checks
- Resource limits
- Container lifecycle

And:

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
```

---

# 12. Kubernetes

For your target level, I would treat Kubernetes as **important but not necessarily day-one**.

Understand:

- Pod
- Deployment
- Service
- Ingress
- ConfigMap
- Secret
- Namespace
- ServiceAccount
- RBAC
- Job
- CronJob
- StatefulSet
- PersistentVolume
- HPA
- Resource requests/limits
- Probes
- Rolling deployments
- Helm

More importantly:

> Why would I use Kubernetes here?

rather than:

> How many YAML manifests can I write?

---

# 13. Cloud

At least **one cloud deeply**.

For your background, AWS is a natural primary choice.

### AWS fundamentals

- IAM
- VPC
- EC2
- ECS
- EKS
- Lambda
- S3
- CloudFront
- Route 53
- ALB
- RDS
- ElastiCache
- SQS
- SNS
- EventBridge
- CloudWatch
- Secrets Manager
- KMS

And architecture:

```text
Internet
   ↓
Route53
   ↓
CloudFront
   ↓
ALB
   ↓
ECS/EKS
   ↓
RDS
   ↓
ElastiCache

       ↘ SQS → Workers
       ↘ S3
       ↘ EventBridge
```

---

# 14. Infrastructure as Code

At least:

**Terraform**

Understand:

- Resources
- Variables
- Outputs
- Modules
- State
- Remote state
- State locking
- Providers
- Data sources
- Workspaces
- Import
- Drift
- Secrets
- Environment separation

Ideally:

```text
Terraform
   │
   ├── networking
   ├── IAM
   ├── database
   ├── cache
   ├── compute
   ├── Kubernetes
   └── observability
```

---

# 15. CI/CD

A production engineer should be able to build:

```text
PR
 ↓
Lint
 ↓
Type check
 ↓
Unit tests
 ↓
Integration tests
 ↓
Security scan
 ↓
Build
 ↓
Container
 ↓
Push registry
 ↓
Deploy staging
 ↓
Smoke tests
 ↓
Production
 ↓
Canary / Rolling
```

Tools:

- GitHub Actions
- GitLab CI
- ArgoCD
- Helm
- Docker
- Terraform

---

# 16. Observability

This is often ignored until production explodes.

### Three pillars

**Logs**

- Structured logging
- Correlation IDs
- Log levels
- Centralized logs

**Metrics**

- Counters
- Gauges
- Histograms
- Percentiles
- RED
- USE

**Traces**

- Distributed tracing
- Spans
- Trace IDs
- Context propagation

### Tools

- OpenTelemetry
- Prometheus
- Grafana
- Loki
- Elasticsearch/OpenSearch
- Jaeger/Tempo

---

# 17. Security

A Fullstack Engineer needs security fundamentals across the entire stack.

### Application security

- OWASP Top 10
- SQL injection
- XSS
- CSRF
- SSRF
- Path traversal
- Command injection
- Broken authorization
- Authentication flaws

### Identity

- OAuth 2.0
- OpenID Connect
- JWT
- Sessions
- Cookies
- Access tokens
- Refresh tokens
- RBAC
- ABAC

### Infrastructure security

- IAM
- Least privilege
- Secrets management
- Network segmentation
- TLS
- Encryption at rest
- Encryption in transit
- Security groups
- WAF

---

# 18. Testing

Not just unit tests.

### Testing pyramid

```text
             E2E
            /   \
       Integration
        /         \
      Unit       Contract
```

Understand:

- Unit testing
- Integration testing
- API testing
- Contract testing
- E2E
- Load testing
- Stress testing
- Security testing
- Test fixtures
- Mocking
- Testcontainers

Tools:

- pytest
- Jest/Vitest
- Playwright
- Cypress
- k6
- Locust

---

# 19. Distributed Systems

This is the level that separates a competent Fullstack Engineer from a senior one.

Understand:

- CAP
- Consistency
- Availability
- Partition tolerance
- Strong vs eventual consistency
- Distributed transactions
- Idempotency
- Ordering
- Replication
- Sharding
- Leader/follower
- Quorums
- Consensus
- Failure detection
- Backpressure
- Rate limiting
- Load shedding
- Retry storms
- Cascading failures

And practical patterns:

- Outbox pattern
- Saga
- CQRS
- Event sourcing
- Circuit breaker
- Bulkhead
- Retry with jitter

Not every application needs these.

But you should know **when not to use them**.

---

# 20. System Design

Finally, all of these pieces come together.

You should be able to design:

### Small

```text
React → API → PostgreSQL
```

### Medium

```text
React
  ↓
CDN
  ↓
Load Balancer
  ↓
API
 ├── PostgreSQL
 ├── Redis
 └── Queue → Workers
```

### Large

```text
                    CDN
                     │
              ┌──────┴──────┐
              │             │
           Frontend       API Gateway
                            │
                    ┌───────┴────────┐
                    │                │
                Services          Workers
                    │                │
             ┌──────┼──────┐         │
             │      │      │         │
           Postgres Redis Search   Kafka/SQS
             │
        Read Replicas
```

Then reason about:

- Capacity
- Latency
- Availability
- Failure modes
- Consistency
- Cost
- Security
- Scaling
- Deployment
- Observability
- Disaster recovery

---

# 21. Python + JavaScript/TypeScript Stack

This is where the technology layer becomes useful.

Build a **Fullstack Engineering Stack Matrix** rather than a random list of frameworks.

| Layer | JavaScript/TS | Python |
|---|---|---|
| Language | TypeScript | Python |
| Runtime | Node.js / Bun | CPython |
| Package manager | pnpm | uv |
| Backend | Fastify / NestJS | FastAPI |
| API validation | Zod | Pydantic |
| ORM | Prisma / Drizzle | SQLAlchemy |
| DB driver | pg | psycopg |
| Async jobs | BullMQ | Celery / ARQ |
| Testing | Vitest | pytest |
| E2E | Playwright | Playwright |
| HTTP client | fetch / undici | httpx |
| CLI | Commander | Typer |
| Serialization | JSON / msgpack | msgpack / orjson |
| WebSockets | ws / Socket.IO | websockets |
| Observability | OpenTelemetry | OpenTelemetry |
| Logging | Pino | structlog |
| Linting | ESLint | Ruff |
| Formatting | Prettier | Ruff |
| Type checking | TypeScript | mypy / pyright |
| Package/build | Vite / tsup | uv / hatch |
| Frontend | React | — |
| Meta-framework | Next.js | — |
| State | Zustand / TanStack Query | — |
| Styling | Tailwind | — |
| E2E | Playwright | — |

Then infrastructure:

| Area | Primary |
|---|---|
| OS | Linux |
| Shell | Bash |
| VCS | Git |
| Containers | Docker |
| Orchestration | Kubernetes |
| IaC | Terraform |
| CI/CD | GitHub Actions |
| Cloud | AWS |
| DB | PostgreSQL |
| Cache | Redis |
| Search | OpenSearch |
| Messaging | Kafka / SQS |
| Observability | OpenTelemetry + Prometheus + Grafana |
| CDN | CloudFront |
| Reverse proxy | Nginx / Envoy |
| Secrets | AWS Secrets Manager / Vault |

---

# 22. AI Engineering Extension

Given the direction toward AI Engineering, the Fullstack foundation becomes the lower layer for AI systems:

```text
                 FULLSTACK ENGINEER
                         │
        ┌────────────────┼────────────────┐
        │                │                │
     Frontend          Backend          Data
        │                │                │
      React          APIs/Services    PostgreSQL
        │                │                │
        └────────────────┼────────────────┘
                         │
                 Infrastructure
                         │
              Linux / Docker / K8s
                         │
                  Cloud / Terraform
                         │
                 Observability
                         │
                    Security
                         │
                         ▼
                AI ENGINEERING
                         │
        ┌────────────────┼─────────────────┐
        │                │                 │
       ML              LLMs             Agents
        │                │                 │
     PyTorch          Transformers        Tools
     sklearn          Embeddings          MCP
     datasets         RAG                 Workflows
        │             Vector DB           Memory
        │             Fine-tuning         Evaluation
        │                │                 │
        └────────────────┼─────────────────┘
                         │
                 Production AI Systems
```

The person doesn't need to become a research scientist first.

They need to become very strong at:

> **software engineering + distributed systems + data + infrastructure + ML/LLM systems.**

---

# Final Competency Model

I'd divide the whole thing into **8 major domains**:

```text
1. Programming
   ├── Python
   ├── TypeScript
   ├── CS fundamentals
   └── Software engineering

2. Web & Frontend
   ├── Browser
   ├── HTML/CSS
   ├── React
   └── Frontend architecture

3. Backend
   ├── APIs
   ├── Services
   ├── Async
   ├── Workers
   └── Distributed systems

4. Data
   ├── PostgreSQL
   ├── Redis
   ├── Search
   ├── NoSQL
   └── Vector databases

5. Systems
   ├── Linux
   ├── Networking
   ├── Processes
   ├── Concurrency
   └── Performance

6. Infrastructure
   ├── Docker
   ├── Kubernetes
   ├── AWS
   ├── Terraform
   └── CI/CD

7. Production Engineering
   ├── Security
   ├── Testing
   ├── Observability
   ├── Reliability
   └── Disaster recovery

8. AI Engineering
   ├── ML
   ├── Deep Learning
   ├── NLP
   ├── Transformers
   ├── LLMs
   ├── RAG
   ├── Agents
   ├── Evaluation
   └── AI infrastructure
```

Then, under each domain, map:

**Principles → Concepts → Technologies → Tools → Libraries → Packages → Projects → Production patterns.**
