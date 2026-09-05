# Master Engineering Handbook

This is the operating handbook for the complete nine-repository Senior/Staff Fullstack + AI engineering system.

It is not another course. It tells you how to navigate the knowledge base, how to make architecture decisions, how to build proof, and how to know when a capability is actually complete.

## 1. The system

```text
learn-js-ts      ── language/runtime depth
learn-frontend   ── browser/React/Next depth
learn-backend    ── API/service/distributed depth
learn-python     ── Python depth
learn-sql        ── SQL/PostgreSQL depth
learn-docker     ── container/Kubernetes depth
learn-ai         ── AI/ML/LLM depth
learn-dsa        ── algorithms/interview depth
                         │
                         ▼
                 learn-fullstack
             connection + architecture
          production + projects + defense
```

`learn-fullstack` is the integration layer. It must explain relationships and trade-offs without copying the specialized repositories.

## 2. The canonical path

When learning an unfamiliar capability, follow:

```text
Problem
 ↓
Mental model
 ↓
Mechanism
 ↓
Invariant / contract
 ↓
Canonical technology
 ↓
Small implementation
 ↓
Failure analysis
 ↓
Security analysis
 ↓
Performance / capacity
 ↓
Testing
 ↓
Observability
 ↓
Production operation
 ↓
Architecture defense
```

The `docs/` maps tell you where the capability lives. The concept documents explain cross-layer behavior. The technology notes explain implementation choices. The projects prove integration.

## 3. Dependency order

Use the following dependency chain when rebuilding fundamentals:

```text
Programming
  ↓
OS + processes + memory
  ↓
Networking
  ↓
HTTP + browser
  ↓
Frontend
  ↓
Backend + API contracts
  ↓
SQL + transactions
  ↓
Redis + caching
  ↓
Queues + events + workers
  ↓
Distributed failure models
  ↓
Containers
  ↓
Cloud + Kubernetes + IaC
  ↓
Security + testing + observability + SRE
  ↓
AI/LLM foundations
  ↓
RAG + tools + agents + evaluation
  ↓
Fullstack production systems
  ↓
System design + interview defense
```

This is a dependency graph, not a rigid calendar.

## 4. Canonical stack

### Application

`TypeScript → React → Next.js`

`Python → FastAPI`

### Services

`Node.js → Fastify → OpenAPI`

`FastAPI → Pydantic → SQLAlchemy`

### Data

`PostgreSQL → Redis → pgvector → OpenSearch when search requirements justify it`

### Async

`transaction/outbox → queue/event stream → worker → idempotent effect`

### Infrastructure

`Linux → Docker → Kubernetes → AWS → Terraform → GitHub Actions`

### Production

`OpenTelemetry → metrics/logs/traces → SLOs → incident response → recovery`

### AI

`model APIs/open models → structured output → RAG → bounded tools/workflows → evaluation → routing/serving`

Frameworks are replaceable. Mechanisms and invariants are not.

## 5. The architecture method

For every system, answer these in order:

1. Who are the users and actors?
2. What are the functional requirements?
3. What are the non-functional requirements?
4. What is the workload and peak factor?
5. What must never become inconsistent?
6. What is the source of truth?
7. What are the trust boundaries?
8. Which operations must be synchronous?
9. Which work should be asynchronous?
10. What data store matches each access pattern?
11. What happens on timeout?
12. What happens on duplicate execution?
13. What happens on partial failure?
14. How is the system observed?
15. How does it scale?
16. How much does it cost?
17. How is it deployed and rolled back?
18. How is it recovered?
19. Which component is unnecessary?
20. Which assumption is most likely to fail?

If these questions cannot be answered, the architecture is not finished.

## 6. Security is a boundary property

Treat all of these as potentially hostile:

- browser input
- headers and cookies
- uploads
- webhooks
- queue messages
- third-party responses
- model output
- retrieved documents
- tool arguments

Authorization is not a frontend feature. It must be enforced at the protected resource boundary.

For multi-tenant systems, prove that an attacker cannot move from:

`user → tenant → resource → retrieved data → tool side effect`

without passing an explicit authorization decision at every sensitive boundary.

## 7. Reliability is explicit behavior

Every remote dependency needs a deliberate policy for:

```text
deadline
retryability
backoff/jitter
idempotency
concurrency limit
fallback/degraded mode
telemetry
```

Do not add retries merely because an error is transient. Model the effect of retries on the dependency and your own resource pools.

Every asynchronous operation needs an answer to:

- can it execute twice?
- how is progress represented?
- what happens after worker death?
- how is poison work isolated?
- how can an operator replay or reconcile it?

## 8. Data is about invariants

Start from business rules, not tables.

```text
business invariant
 ↓
authoritative state
 ↓
transaction boundary
 ↓
derived state
 ↓
propagation
 ↓
reconciliation
```

Caches, search indexes, embeddings, analytics and notifications are commonly derived state. Their staleness and rebuild strategy must be explicit.

## 9. AI is a subsystem, not an authority

A production AI feature normally looks like:

```text
identity/auth
 ↓
validated request
 ↓
context construction
 ↓
retrieval / tools
 ↓
model inference
 ↓
validated output
 ↓
state transition / response
```

The model does not own:

- identity
- authorization
- database invariants
- tool permissions
- spend limits
- approval policy
- release policy

For RAG, authorization filters belong before protected content enters model context. For agents, every side effect requires deterministic policy enforcement.

## 10. Technology selection rule

Choose a technology only after defining the problem and constraints.

```text
requirement
 → workload
 → invariant
 → access pattern
 → failure model
 → operational constraint
 → technology
```

Prefer the simplest solution that satisfies the requirement. A technology is justified by measurable need, not popularity.

## 11. Project strategy

The ten projects are integration tests for the graph:

1. Multi-tenant SaaS
2. Realtime collaboration
3. Event-driven order platform
4. Background job platform
5. Media/file processing
6. High-throughput URL service
7. Search platform
8. AI knowledge assistant
9. Agentic operations assistant
10. Production AI application platform

Use the project specifications and build playbook rather than inventing another tutorial sequence.

The final platform should combine:

`browser + auth + APIs + PostgreSQL + Redis + async work + search/RAG + tools + evaluation + observability + deployment + recovery`.

## 12. Evidence standard

For each important capability, retain evidence for:

```text
explanation
implementation
unit/integration tests
failure experiment
security test
performance/load result
telemetry
deployment
rollback
recovery
trade-off
```

A README saying “supports retries” is not evidence. A test that forces a dependency timeout and demonstrates bounded retry behavior is evidence.

## 13. Interview standard

Every project should be defensible without notes.

You should be able to explain:

- why the architecture is shaped this way;
- what invariant each important component protects;
- why the chosen data store fits;
- why work is sync or async;
- what happens during partial failure;
- what breaks first under 10× load;
- how security is enforced;
- how operators detect problems;
- how rollback and recovery work;
- how cost changes with workload;
- what you would simplify or replace.

Do not invent metrics, incidents or production experience. Distinguish implemented evidence from theoretical reasoning.

## 14. What not to do

Do not:

- merge nine repositories into duplicated course material;
- create a new note when an existing canonical note can be strengthened;
- add a framework without understanding the mechanism it abstracts;
- introduce infrastructure before workload or failure requirements justify it;
- claim mastery from reading;
- confuse a passing happy-path test with production readiness;
- treat benchmarks as substitutes for task-specific evaluation;
- make the model responsible for deterministic security policy.

## 15. Definition of complete

### Repository complete

The repository is complete when:

- all 20 master capabilities have an owner;
- every cross-layer gap has a canonical explanation;
- technology notes have a single canonical location;
- architecture patterns connect the domains;
- production concerns are explicit;
- projects exercise the graph;
- interview verification maps to real evidence;
- no major document contradicts the canonical model.

### Capability complete

A capability is complete only after:

**Understand → Implement → Debug → Measure → Secure → Test → Scale → Operate → Recover → Defend.**

### Learning system complete

The system is complete when new knowledge is handled by this rule:

```text
new problem
 ↓
identify existing concept
 ↓
strengthen canonical note if needed
 ↓
connect source repository
 ↓
add project evidence
 ↓
add verification
```

That prevents the repository from becoming an ever-growing list of disconnected technologies.

## 16. Final navigation

Start with:

- `docs/master-skill-universe.md`
- `docs/skill-map.md`
- `docs/final-skill-graph.md`
- `docs/source-map.md`
- `docs/learning-model.md`

Then use:

- `architecture/` for system decisions
- `production/` for operational engineering
- `technologies/` for canonical technology references
- `projects/` for integration proof
- `docs/production-verification.md` for acceptance
- `docs/interview-map.md` for defense
- `docs/completion-ledger.md` for status

This is the final operating model for `learn-fullstack`.
