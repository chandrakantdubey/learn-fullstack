# Production Verification Playbook

This is the final execution layer for the Fullstack + AI skill graph. Reading a concept is not evidence of mastery. Each capability must be demonstrated in code, failure testing and architecture defense.

## Universal completion loop

```text
Understand
  ↓
Implement
  ↓
Debug
  ↓
Measure
  ↓
Secure
  ↓
Test
  ↓
Scale
  ↓
Operate
  ↓
Recover
  ↓
Defend
```

## Vertical slice A — request lifecycle

Build:

`Next.js → HTTPS → gateway → FastAPI/Fastify → validation → auth → domain → PostgreSQL → response`

Prove:

- stable API contract
- server-side authorization
- validation at trust boundaries
- transaction boundary
- structured errors
- trace propagation
- timeout behavior
- browser loading/error/retry states

Break it deliberately:

- malformed input
- expired credentials
- unauthorized resource
- slow database
- dropped client connection
- backend process restart

## Vertical slice B — asynchronous work

Build:

`API → PostgreSQL transaction → outbox → queue → worker → external dependency`

Prove:

- durable state transition
- idempotency key/effect
- retry policy
- dead-letter behavior
- bounded concurrency
- backpressure
- graceful shutdown
- trace continuation

Break it:

- commit succeeds before publish
- duplicate delivery
- poison message
- worker dies mid-job
- dependency timeout
- queue backlog

## Vertical slice C — realtime

Build:

`browser → authenticated connection → WebSocket/SSE → service → Redis/pubsub → durable state`

Prove:

- connection authentication
- authorization
- reconnect behavior
- event ordering expectations
- duplicate handling
- slow-client behavior
- cancellation
- fan-out limits

Break it:

- network disconnect
- reconnect storm
- slow consumer
- server restart
- duplicate event

## Vertical slice D — file pipeline

Build:

`browser → signed upload → object storage → queue → worker → status API → UI`

Prove:

- upload size/type limits
- safe object naming
- authorization
- durable processing state
- progress/status model
- cleanup/retention
- worker retry behavior

Break it:

- abandoned upload
- malformed file
- oversized file
- worker crash
- duplicate job
- storage outage

## Vertical slice E — authorization-aware RAG

Build:

`upload → parse → normalize → chunk → embed → pgvector → ACL filter → retrieve/rerank → model → citations → stream`

Prove:

- tenant/resource ownership
- document provenance
- retrieval filters applied before model context
- malicious-document handling
- empty/low-quality retrieval behavior
- citation provenance
- model timeout/fallback
- token/cost accounting
- evaluation regression tests

Break it:

- cross-tenant query
- prompt injection inside a document
- stale index
- embedding failure
- provider outage
- empty retrieval
- high token cost

## Vertical slice F — bounded agent

Build:

`browser → API/auth → model → explicit workflow/state → validated tool → policy check → optional approval → execution → audit`

Prove:

- narrow tool contracts
- allowlists
- argument validation
- authorization on every side effect
- iteration/time/token budgets
- idempotency
- human approval for high-impact actions
- complete audit trail
- trajectory evaluation

Break it:

- malicious tool arguments
- prompt injection
- repeated tool calls
- stale state
- partial execution
- downstream timeout
- approval timeout

## Production verification matrix

| Capability | Build proof | Failure proof | Measurement |
|---|---|---|---|
| API contracts | versioned endpoint | incompatible client | contract pass rate |
| Auth/RBAC | protected resource | IDOR/tenant crossing | denied unauthorized attempts |
| Transactions | atomic mutation | dependency failure | invariant preservation |
| Cache | cache-aside path | stale/outage | hit rate + latency |
| Queue | durable job | duplicate/crash | queue age + throughput |
| Realtime | reconnecting client | slow/disconnected client | connection/error rate |
| Files | signed upload | malformed/oversized file | processing latency |
| Search | indexed query | stale/partial index | recall/latency |
| RAG | grounded answer | malicious/empty retrieval | retrieval + answer quality |
| Agent | bounded tool workflow | unsafe/repeated tool | success + unsafe-call rate |
| Observability | traces/logs/metrics | missing dependency | detection time |
| Security | threat controls | abuse test | blocked attack cases |
| Deployment | progressive release | bad version | rollback time |
| DR | restore procedure | data/service loss | RPO/RTO achieved |

## Architecture defense checklist

For each major project answer without notes:

1. What are the functional requirements?
2. What are the non-functional requirements?
3. What is the workload: users, RPS, data volume, peak factor?
4. Which data is authoritative?
5. Which invariants must never be violated?
6. Where are the trust boundaries?
7. Which operations are synchronous?
8. Which operations are asynchronous and why?
9. What happens when each dependency times out?
10. What happens when a message is delivered twice?
11. What fails first at 10× load?
12. What is the scaling bottleneck?
13. What does the operator observe?
14. What is the rollback procedure?
15. What is the recovery procedure?
16. What does the system cost at the target workload?
17. What security assumption is most dangerous?
18. Which technology could be removed without breaking the design?
19. What trade-off did you intentionally accept?
20. What would change at the next order of magnitude?

## Evidence artifacts

A completed project should leave behind:

```text
README
architecture diagram
ADRs
threat model
API/event contracts
schema + migrations
unit tests
integration tests
contract tests
E2E tests
failure-injection tests
load-test results
observability dashboard definitions
runbook
rollback procedure
recovery procedure
cost estimate
known trade-offs
```

## Final standard

The portfolio is complete when at least one serious project demonstrates every major boundary and the engineer can defend the architecture under normal operation, partial failure, security attack, scale pressure and cost constraints.

Do not manufacture evidence. If a capability has not been implemented or tested, mark it incomplete and build the missing proof.
