# CI/CD

CI/CD is the automated path from source change to a verified deployable artifact and then to a controlled production release.

## Mental model

```text
Commit / PR
   ↓
Lint + Type Check
   ↓
Unit Tests
   ↓
Integration Tests
   ↓
Security / Dependency Checks
   ↓
Build Artifact
   ↓
Container Image
   ↓
Registry
   ↓
Staging
   ↓
Smoke / Contract Tests
   ↓
Production Release
   ↓
Observe / Roll Back
```

## CI principles

- every change should be reproducible from a clean checkout
- lock dependencies
- keep pipelines deterministic
- fail fast on cheap checks
- run expensive integration tests after basic validation
- publish immutable artifacts
- never build different source for staging and production

## CD principles

A deployment should be a controlled state transition, not a shell script that happens to copy files.

Important strategies:

- rolling deployment
- blue/green
- canary
- feature flags
- automated rollback

Choose based on blast radius, traffic shape, compatibility, and operational maturity.

## GitHub Actions baseline

Typical workflow stages:

```yaml
jobs:
  validate:
    - lint
    - typecheck
    - unit-tests
  integration:
    - services: postgres, redis
    - integration-tests
  build:
    - build application
    - build image
    - push image
  deploy:
    - deploy staging
    - smoke tests
    - promote
```

## Secrets

- repository secrets for CI credentials
- OIDC federation to cloud providers where possible
- short-lived credentials preferred over static cloud keys
- application secrets belong in a runtime secret manager, not GitHub Actions variables copied into images

## Production controls

Require:

- protected main branch
- required CI checks
- pinned actions where practical
- dependency update automation
- deployment audit trail
- rollback procedure
- smoke tests after deployment

## Project proof

Build a pipeline for the task system that runs tests, builds the frontend and API images, pushes versioned images, deploys a staging environment, executes smoke tests, and only then promotes the same artifacts to production.