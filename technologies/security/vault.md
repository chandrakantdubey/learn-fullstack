# HashiCorp Vault

**Role:** Awareness | **Layer:** Secrets/identity

## Mental model
Vault centralizes secret storage and access policies, supporting dynamic credentials, encryption services and identity-based access.

## Learn
- policies and auth methods
- secret engines
- dynamic database/cloud credentials
- leases and renewal
- transit encryption
- audit logging

## Production
Prefer short-lived credentials, least privilege, audited access and automated rotation. Avoid creating a single operational dependency without HA, recovery and incident plans.

## Related
SOPS, AWS IAM, Kubernetes, secrets management.
