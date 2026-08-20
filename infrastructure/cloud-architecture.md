# Cloud Architecture

Cloud architecture is the mapping from application requirements to managed compute, storage, networking, identity, and operational services.

## Reference AWS shape

```text
Route 53
   ↓
CloudFront / WAF
   ↓
Load Balancer
   ↓
ECS/EKS or Lambda
   ├── API
   └── Worker
      ↓
  RDS PostgreSQL
  ElastiCache Redis
  S3
  SQS
  EventBridge
```

## Networking

Understand:

- VPC
- public vs private subnets
- route tables
- internet/NAT gateways
- security groups vs network ACLs
- DNS
- load balancers
- TLS termination
- multi-AZ topology

Application services and databases should not share the same public exposure model.

## Identity

IAM should follow least privilege. Prefer workload identities/roles over static access keys. Separate human administrative access from service runtime permissions.

## Compute choices

Choose based on operational burden, workload shape, and scaling behavior:

- Lambda for event/request workloads with suitable execution constraints
- ECS/Fargate for containers without Kubernetes operational overhead
- EKS when Kubernetes capabilities or platform standardization justify the cost

## Data services

RDS provides managed relational operations. ElastiCache provides managed caching. S3 is the default durable object store for blobs/artifacts. SQS decouples asynchronous work.

## Reliability

Start with multi-AZ deployment for production-critical services. Define RTO/RPO before designing disaster recovery. Cross-region replication is justified by business requirements, not by default fashion.

## Cost

Track:

- compute utilization
- database size and IOPS
- network egress
- NAT gateway usage
- log/trace volume
- idle development environments
- storage lifecycle

Architecture is incomplete if the cost model is unknown.

## Project mapping

The task system should first run locally, then map to a small AWS topology before any multi-region design is attempted.
