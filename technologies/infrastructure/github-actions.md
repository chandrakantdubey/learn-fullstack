# GitHub Actions

**Role:** Primary | **Layer:** CI/CD

## Mental model
GitHub Actions executes event-triggered workflows on runners. A reliable pipeline turns source changes into repeatable validation, artifacts and deployments.

## Learn
- workflows, jobs and steps
- triggers and permissions
- matrix builds
- caching
- artifacts
- environments and approvals
- reusable workflows
- OIDC/cloud authentication

## Production
Use least-privilege workflow permissions, pin or control action versions, avoid long-lived cloud credentials, cache safely, separate build/test/deploy concerns, and make deployments observable and reversible.

## Related
Git, Docker, Terraform, Kubernetes, security.
