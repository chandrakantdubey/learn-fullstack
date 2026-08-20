# AWS

Cloud architecture is the application system mapped onto managed infrastructure primitives. Learn the primitives and failure boundaries, not memorized service names.

## Canonical production shape

```text
Route 53
   ↓
CloudFront
   ↓
ALB / API Gateway
   ↓
ECS / EKS / Lambda
   ├── RDS PostgreSQL
   ├── ElastiCache Redis
   ├── S3
   ├── SQS / EventBridge
   └── CloudWatch / OpenTelemetry
```

## Core domains

### Identity

- IAM users and roles
- role assumption
- least privilege
- workload identity
- KMS
- Secrets Manager

### Networking

- VPC
- subnets
- route tables
- security groups
- NAT
- public vs private subnets
- load balancers

### Compute

- ECS/Fargate for managed containers
- EKS for Kubernetes workloads
- Lambda for event-driven/serverless workloads
- EC2 when direct host control is justified

### Data

- RDS PostgreSQL
- ElastiCache Redis
- S3 object storage

### Messaging

- SQS for durable queues
- SNS/EventBridge for event distribution

## Architecture rule

Prefer managed services for undifferentiated operational work unless there is a strong technical or economic reason to self-host.

## Multi-region

Do not add multi-region only because it sounds resilient. Establish the requirement first:

- RTO
- RPO
- geographic availability
- regulatory constraints
- dependency topology
- operational team capability

A practical progression is single-region multi-AZ → tested disaster recovery → active/passive multi-region → active/active only when justified.

## Production concerns

- use private subnets for internal services
- restrict security groups by dependency
- enable encryption by default
- centralize audit logging
- avoid long-lived static credentials
- define backup retention and restore tests
- budget and monitor resource spend

## Project proof

Design the task platform across two availability zones with public ingress, private application workloads, managed PostgreSQL, Redis, object storage, queue-backed workers, IAM roles, and centralized observability.