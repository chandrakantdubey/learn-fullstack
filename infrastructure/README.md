# Infrastructure Engineering

Infrastructure is the execution environment for the software we build.

## Core areas

- Linux operations and resource management
- Containers, Docker and registries
- Networking, reverse proxies and load balancing
- Kubernetes architecture and operations
- Cloud architecture and AWS service selection
- Infrastructure as Code with Terraform
- CI/CD, GitHub Actions and GitOps concepts
- Secrets and configuration management
- Deployment strategies: rolling, blue/green and canary
- Scaling, capacity planning and graceful degradation
- Backup, recovery, RPO/RTO and disaster recovery

## AWS primary map

Understand the role and trade-offs of:

`IAM · VPC · EC2 · ECS · EKS · Lambda · S3 · CloudFront · Route 53 · ALB · RDS · DynamoDB · ElastiCache · SQS · SNS · EventBridge · CloudWatch · Secrets Manager · KMS · ECR`

GCP and Azure remain secondary/awareness paths unless a project requires deeper implementation.

## Kubernetes boundary

Understand:

`Pods · Deployments · StatefulSets · DaemonSets · Jobs · CronJobs · Services · Ingress · Gateway API · ConfigMaps · Secrets · PV/PVC · RBAC · ServiceAccounts · NetworkPolicies · probes · requests/limits · scheduling · taints/tolerations · HPA · Helm · Operators · troubleshooting`

The question is always **why this operational mechanism is justified**, not how much YAML can be written.

## Terraform / delivery

The integrated path is:

```text
Terraform
  ↓
network / IAM / data / compute / observability
  ↓
GitHub Actions
  ↓
lint → typecheck → tests → security scan → build
  ↓
container → registry → staging
  ↓
smoke tests → production
  ↓
rolling / canary / blue-green → rollback
```

Know Terraform state, remote state, locking, modules, variables, outputs, providers, data sources, import and drift. Understand GitOps and ArgoCD conceptually.

## Fullstack boundary

`learn-docker` owns container/Kubernetes mechanics. This layer owns architecture and deployment choices. `learn-fullstack` production material owns SLOs, observability, security, cost, incident response and recovery.

Kubernetes is not the goal. Reliable, reproducible software delivery is the goal.
