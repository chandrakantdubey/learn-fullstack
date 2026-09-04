# Helm

**Role:** Primary | **Layer:** Kubernetes packaging

## Mental model
Helm packages Kubernetes manifests into versioned charts with templates and values, allowing repeatable environment-specific releases.

## Learn
- chart structure
- templates and functions
- values and overrides
- dependencies
- release history and rollback
- schema validation

## Production
Keep templates readable, validate rendered manifests in CI, avoid hiding critical behavior behind excessive templating, and treat values as configuration rather than application secrets.

## Related
Kubernetes, Terraform, GitHub Actions.
