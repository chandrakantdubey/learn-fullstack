# Kubernetes

Kubernetes is an orchestration layer for running distributed workloads with declarative desired state, service discovery, scheduling, health management, and controlled rollouts.

## Mental model

```text
Container Image
      ↓
Pod
      ↓
Deployment / StatefulSet / Job
      ↓
Service
      ↓
Ingress / Gateway
      ↓
External Traffic
```

Kubernetes answers operational questions such as:

- where should this workload run?
- how many replicas should exist?
- how is traffic routed?
- what happens when a process dies?
- how do we roll out a new version?
- how do we scale based on demand?

## Core resources

- Pod
- Deployment
- StatefulSet
- Job / CronJob
- Service
- Ingress / Gateway
- ConfigMap
- Secret
- ServiceAccount
- Role / RoleBinding
- PersistentVolume / PersistentVolumeClaim
- HorizontalPodAutoscaler

## Probes

- liveness: should this process be restarted?
- readiness: should this instance receive traffic?
- startup: has the process finished initializing?

A readiness failure should normally remove a pod from service rather than restart it.

## Resources

Requests participate in scheduling; limits bound consumption. Set them from measured workload behavior rather than arbitrary defaults.

## Deployment

Prefer immutable images and declarative manifests. A deployment should change the desired image/version and let the platform reconcile the state.

## Failure modes

- image pull failure
- crash loop
- readiness never becomes true
- CPU/memory saturation
- OOM kill
- insufficient cluster capacity
- broken service selectors
- DNS/service discovery failures
- configuration or secret mismatch
- storage attachment problems

## Security

- least-privilege RBAC
- dedicated service accounts
- network policies
- non-root containers
- read-only filesystems where practical
- image scanning and provenance
- secrets from an external secret manager where practical

## When not to use Kubernetes

A small application with simple traffic, one or two services, and a low operational budget may be better on a managed container platform or serverless runtime. Kubernetes is valuable when its scheduling, deployment, scaling, networking, or platform abstractions justify the operational complexity.

## Project proof

Deploy the fullstack task system to a local cluster first, then a managed cluster. Implement rolling deployment, readiness probes, resource requests, HPA, service discovery, and centralized logs.