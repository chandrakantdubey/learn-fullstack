# Terraform

**Role:** Primary | **Layer:** Infrastructure as code

## Mental model
Terraform manages declarative infrastructure through configuration, a state file and a provider graph. Plans describe intended changes before apply.

## Learn
- resources and data sources
- variables and outputs
- modules
- state and remote backends
- dependency graph
- plan/apply/destroy
- imports and drift
- provider/version constraints

## Production
Use remote encrypted state with locking, review plans, pin provider versions, isolate environments/states, protect secrets, and make modules small enough to understand.

## Related
AWS, Kubernetes, GitHub Actions, secrets management.
