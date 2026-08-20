# Cloud Architecture

Cloud architecture is the application of systems principles to managed infrastructure.

## Reference AWS shape

```text
Route 53
   ↓
CloudFront / CDN
   ↓
ALB
   ↓
ECS/EKS or managed compute
   ├── API
   └── Worker

API ──→ RDS PostgreSQL
   ├──→ ElastiCache Redis
   ├──→ S3
   └──→ SQS / EventBridge

IAM + KMS + Secrets Manager
CloudWatch + OpenTelemetry
```

## Networking

Understand:

- VPC
- public/private subnets
- route tables
- internet/NAT gateways
- security groups
- network ACLs
- DNS
- load balancers
- private service-to-service paths
- availability zones

Databases and internal services should not be internet-exposed by default.

## Compute choices

Choose based on workload:

- Lambda for event-driven, short-lived workloads
- ECS/Fargate for managed containers without Kubernetes complexity
- EKS when Kubernetes capabilities are actually required
- EC2 for lower-level control or specialized workloads

The cheapest operationally is not always the cheapest at scale. Include engineering and operational cost.

## IAM

Use workload identity and short-lived credentials where possible. Separate deploy identity from runtime identity. Keep policies least-privilege and auditable.

## Managed data

Understand operational implications of:

- RDS PostgreSQL
- ElastiCache Redis
- S3 durability/storage patterns
- SQS delivery semantics
- EventBridge routing

## Availability and disaster recovery

Design explicitly for:

- AZ failure
- database failure
- dependency outage
- bad deployment
- data corruption
- region outage

Define RPO and RTO before selecting replication and recovery architecture.

## Cost model

Track:

```text
Compute + storage + network + managed services + observability + human operations
```

Control cost with right-sized compute, autoscaling bounds, storage lifecycle policies, caching, batching, and removal of unnecessary always-on services.
