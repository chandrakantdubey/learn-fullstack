# Cryptography for Fullstack Engineers

The goal is not to become a cryptographer. The goal is to know which primitive solves which problem, what security property it provides, and where application engineers commonly misuse it.

## Security properties

- **Confidentiality:** unauthorized parties cannot read data.
- **Integrity:** unauthorized modification can be detected.
- **Authenticity:** a key or identity can be verified as the source.
- **Non-repudiation:** signatures can provide evidence of key-controlled signing, subject to the trust model.

## Core primitives

### Hashes

A cryptographic hash maps arbitrary input to a fixed-size digest. It is designed to make finding collisions or reversing the input computationally difficult. Hashes are useful for content addressing, integrity checks and fingerprints.

A hash is **not encryption** and should not be used as a password-storage algorithm.

### Password hashing

Passwords should be processed with a password-specific, intentionally expensive and salted KDF such as Argon2id, scrypt or bcrypt. Each password needs a unique salt. The application stores the resulting verifier, not the password.

### Symmetric encryption

The same secret key protects encryption and decryption. Modern authenticated encryption such as AES-GCM or ChaCha20-Poly1305 provides confidentiality and integrity together.

Nonce/IV handling is critical: never reuse a nonce with the same key where the algorithm forbids it. Use a well-tested library and let it generate/manage nonces when possible.

### Public-key cryptography

A key pair separates private-key control from public verification/encryption. Common uses include TLS, signatures, key exchange and identity systems. Private keys must remain secret; public keys are designed to be distributed.

### Digital signatures

A private key signs data and a public key verifies the signature. Signatures provide integrity and authenticity relative to the key-distribution/trust model.

## TLS mental model

Application security often depends on TLS rather than directly implementing encryption:

```text
HTTP request
   ↓
TLS handshake / certificate validation / key agreement
   ↓
Encrypted authenticated transport
   ↓
HTTP application protocol
```

TLS protects data in transit between the endpoints that actually terminate TLS. It does not make a compromised server trustworthy, and it does not automatically encrypt data at rest.

## Key management

Cryptography fails operationally more often than mathematically. Treat keys as lifecycle-managed secrets:

```text
generate → store → authorize → rotate → revoke → audit → destroy
```

Do not hard-code secrets, commit them to Git, print them in logs, or put long-lived credentials into client-side bundles.

## Common mistakes

- Encrypting passwords instead of hashing them with a password KDF.
- Rolling custom crypto.
- Reusing nonces incorrectly.
- Using predictable random values for security tokens.
- Confusing encoding with encryption.
- Assuming base64 provides confidentiality.
- Logging bearer tokens or encryption keys.
- Designing key storage separately from the application threat model.

## Fullstack boundaries

Frontend code may use Web Crypto for specific browser-side operations, but secrets embedded in browser code are not secret from the user. Server-side secrets belong behind a trusted backend boundary. Authentication tokens, cookies, session identifiers, password reset links and signed URLs should be designed as security-sensitive protocols, not merely strings.

## Production checklist

- Use standard libraries and primitives.
- Threat-model key compromise and token theft.
- Use a cryptographically secure random source.
- Rotate keys without breaking active traffic unnecessarily.
- Separate encryption keys from encrypted data when the threat model requires it.
- Audit access to secrets.
- Test expiry, rotation, revocation and failure paths.
