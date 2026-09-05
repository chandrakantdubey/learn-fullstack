# Deployment Reference Architecture

This is the integrated deployment model. `learn-docker` owns container/Kubernetes mechanics; this document owns the application-to-production decisions.

## Baseline

```text
Internet
  ↓
DNS
  ↓
CDN / WAF
  ↓
Load balancer / gateway
  ↓
Web + API replicas
  ├── PostgreSQL
  ├── Redis
  ├── object storage
  └── queue → workers
```

Add components only when requirements justify them.

## Environment model

Use separate configuration and state for:

`local → CI → staging → production`

Production secrets should come from a runtime secret manager. Environment configuration must be explicit and validated at startup.

## Artifact model

```text
source
 ↓
commit SHA
 ↓
CI verification
 ↓
immutable image/artifact
 ↓
registry
 ↓
staging
 ↓
smoke/contract tests
 ↓
progressive production rollout
```

Never rebuild the application differently for production after staging verification.

## AWS decision points

### Compute

- **Lambda:** suitable for compatible event/request workloads with simple operational requirements.
- **ECS/Fargate:** strong default for containerized services without Kubernetes platform overhead.
- **EKS:** use when Kubernetes scheduling/platform capabilities or organizational standardization justify the additional operational complexity.

### Data

- RDS PostgreSQL for relational business state.
- ElastiCache/Redis for bounded acceleration and coordination use cases.
- S3 for durable blobs.
- SQS for durable asynchronous work.
- EventBridge for event routing/integration patterns.

### Networking

Prefer:

```text
public edge
  ↓
public load-balancing layer
  ↓
private application services
  ↓
private data services
```

Use security groups and IAM as explicit boundaries rather than assuming private networking alone provides authorization.

## IAM

For every workload identity define:

- actions
- resources
- conditions where useful
- environment
- owner
- rotation/revocation path

Prefer workload roles/federation over long-lived access keys.

## Release strategies

### Rolling

Replace instances gradually. Simple default when compatibility is maintained.

### Blue/green

Keep two environments and shift traffic. Useful when rollback speed and isolation justify duplicate capacity.

### Canary

Expose a small fraction of traffic to the new version and compare health/quality signals before expanding.

Feature flags can separate deployment from feature activation.

## Database migrations

A safe migration should tolerate mixed application versions during rollout.

Prefer:

```text
expand
 ↓
backfill
 ↓
read new + old safely
 ↓
switch writes/reads
 ↓
verify
 ↓
contract/remove old
```

Avoid destructive schema changes that require every running process to upgrade simultaneously.

## Health model

- **startup:** initialization is complete
- **readiness:** instance can safely receive traffic
- **liveness:** process should be restarted

Do not use liveness to represent dependency health in a way that creates restart storms.

## Recovery

Define before production:

- RPO
- RTO
- backup retention
- restore procedure
- dependency recovery order
- rollback procedure
- degraded mode

Test restore and rollback rather than documenting them only.

## Cost model

Track:

`requests → compute → DB load → storage → network → observability → third-party/API spend`

For AI systems also track:

`requests → tokens → model/provider cost → retrieval cost → tool calls`

## Deployment proof

For a portfolio project, demonstrate local Compose, CI verification, immutable image promotion, staging smoke tests, production rollout, rollback, health checks, telemetry verification and a documented recovery drill.
