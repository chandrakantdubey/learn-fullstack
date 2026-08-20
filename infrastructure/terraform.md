# Terraform

Terraform turns infrastructure into versioned, reviewable desired state.

## Mental model

```text
Configuration
   ↓
Provider / Data Sources
   ↓
Plan
   ↓
State
   ↓
Apply
   ↓
Cloud Resources
```

Terraform is not a general-purpose deployment script. Its strength is resource lifecycle management and dependency modeling.

## Core concepts

- resources
- data sources
- variables
- locals
- outputs
- modules
- providers
- state
- remote state
- state locking
- dependency graph
- import
- drift

## State

State is critical coordination data. For team environments use remote encrypted state with locking and controlled access.

Never commit production state containing secrets or sensitive resource data into a public repository.

## Modules

Use modules around stable infrastructure concepts such as:

```text
network
postgres
redis
cluster
service
observability
```

Do not create a module for every three-line resource. Abstraction should reduce duplication without hiding important infrastructure behavior.

## Environments

Keep environment differences explicit. A common pattern is separate state per environment with shared modules and environment-specific variables.

## Safety

Before applying:

1. review the plan
2. verify account and region
3. inspect destructive changes
4. ensure backups/retention policies exist
5. verify IAM scope

## Drift

Resources can change outside Terraform. Detect drift regularly and decide whether Terraform should own the change, the external change should be reverted, or the resource should be imported/re-modeled.

## Project proof

Provision the task system's network, database, cache, container runtime, queue, IAM roles, and observability resources using reusable Terraform modules. Store state remotely and run plan validation in CI.