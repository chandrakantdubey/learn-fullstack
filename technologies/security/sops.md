# SOPS

**Role:** Awareness | **Layer:** Secrets

## Mental model
SOPS encrypts selected fields/files while keeping configuration structure usable in version control.

## Learn
- encrypted YAML/JSON/.env patterns
- KMS/age/PGP key management
- encrypted diffs
- CI decryption
- key rotation

## Production
Keep decryption keys outside repositories, grant least privilege, rotate keys deliberately, and avoid treating encrypted source files as permission to expose secrets broadly.
