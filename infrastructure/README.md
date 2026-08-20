# Infrastructure Engineering

Infrastructure is the execution environment for the software we build.

## Core areas

- Linux operations
- Containers and Docker
- Container registries
- Networking and load balancing
- Kubernetes
- Cloud architecture
- AWS services
- Infrastructure as Code with Terraform
- CI/CD
- Secrets and configuration
- Deployment strategies
- Scaling and capacity planning
- Disaster recovery

## Deployment progression

```text
Local process
   ↓
Docker container
   ↓
Container registry
   ↓
Cloud compute
   ↓
Load balancing
   ↓
Database / cache / queues
   ↓
Kubernetes when justified
   ↓
Terraform-managed environment
   ↓
Automated delivery
```

Kubernetes is not the goal. Reliable, reproducible software delivery is the goal.
