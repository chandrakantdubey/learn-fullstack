# AWS

**Role:** Primary | **Layer:** Cloud

## Mental model
AWS provides composable managed primitives for compute, networking, identity, storage, databases, messaging and observability. Architecture is mostly about selecting failure and operational boundaries.

## Learn
- IAM and least privilege
- VPC, subnets, routing, security groups
- EC2/ECS/EKS/Lambda tradeoffs
- S3 and object storage
- RDS/Aurora
- SQS/SNS/EventBridge
- CloudWatch and CloudTrail
- load balancing and DNS
- multi-AZ and multi-region design

## Production
Model quotas, failure domains, latency, data durability, recovery objectives and cost before choosing services. Prefer managed services when they reduce operational burden without creating unacceptable coupling.

## Related
Terraform, Kubernetes, SQS, EventBridge, PostgreSQL.
