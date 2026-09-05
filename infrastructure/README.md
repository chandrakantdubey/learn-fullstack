# Infrastructure Engineering

Infrastructure is the execution environment for the software we build.

## Canonical guides

- [`cloud-architecture.md`](cloud-architecture.md) — AWS-oriented service selection and topology.
- [`deployment-reference.md`](deployment-reference.md) — integrated artifact, environment, rollout and recovery model.
- [`docker.md`](docker.md) — container concepts and mechanics.
- [`kubernetes.md`](kubernetes.md) — orchestration concepts and trade-offs.
- [`terraform.md`](terraform.md) — IaC state, modules, drift and safety.
- [`ci-cd.md`](ci-cd.md) — CI/CD and release pipeline.

## Core areas

- Linux operations and resource management
- containers, Docker and registries
- networking, reverse proxies and load balancing
- Kubernetes architecture and operations
- cloud architecture and AWS service selection
- Infrastructure as Code with Terraform
- CI/CD, GitHub Actions and GitOps concepts
- secrets and configuration management
- rolling, blue/green and canary deployment
- scaling, capacity and graceful degradation
- backup, recovery, RPO/RTO and disaster recovery

## AWS primary map

`IAM · VPC · EC2 · ECS · EKS · Lambda · S3 · CloudFront · Route 53 · ALB · RDS · DynamoDB · ElastiCache · SQS · SNS · EventBridge · CloudWatch · Secrets Manager · KMS · ECR`

## Boundary

`learn-docker` owns container/Kubernetes mechanics. `learn-fullstack` owns architecture, deployment decisions, security, observability, cost, recovery and application integration.

Kubernetes is not the goal. Reliable, reproducible software delivery is the goal.
