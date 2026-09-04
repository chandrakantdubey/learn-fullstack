# Kubernetes

**Role:** Primary | **Layer:** Infrastructure

## Mental model
Kubernetes reconciles declared desired state toward observed state using controllers, scheduling and APIs. A deployment describes intent; controllers continuously converge reality.

## Learn
- Pods, Deployments, Services
- ConfigMaps and Secrets
- probes and lifecycle
- requests/limits and scheduling
- Jobs/CronJobs
- Ingress/Gateway concepts
- RBAC and service accounts
- StatefulSets and persistent volumes
- autoscaling and disruption budgets

## Production
Define requests/limits, readiness/liveness correctly, use least-privilege RBAC, separate configuration from images, design graceful shutdown, and understand rolling updates and failure domains.

## Debugging
Learn events, logs, exec, describe, resource metrics, DNS/service discovery and controller status before changing manifests blindly.

## Related
Docker, Helm, AWS, OpenTelemetry, Terraform.
