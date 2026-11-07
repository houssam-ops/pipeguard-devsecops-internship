# Security and publication policy

## Scope

This is an internship portfolio and partial source archive. It is not a supported production security product. Recovered examples require review before use; known shortcomings are documented in `docs/prototype-review.md`.

## Sensitive material

Do not commit academic reports, original private guides, unreviewed screenshots of administrative interfaces, real logs, packet captures, organization-specific inventories, credentials, kubeconfigs, Vault tokens/unseal material, private keys, webhooks, database dumps or personal information.

The `.gitignore` excludes common sensitive paths and file types. The repository validator rejects report/document/archive payloads, unapproved images and common credential markers in tracked files. Exactly three reviewed PNG screenshots are allowed by path and SHA-256 checksum; changed or additional images require a new visual and OCR review. These checks complement manual review; they cannot prove that all possible sensitive content is absent. Ignore rules do not remove previously committed material.

Before publishing new files, review their content and metadata, run repository checks, scan both files and full history with a maintained secret scanner, and inspect `git diff --cached`. Use documentation-only hostnames and synthetic fixtures. Never use a real secret as a scanner test fixture.

## Reporting a concern

Do not paste credentials, private infrastructure details or exploit payloads into public issues. If GitHub private vulnerability reporting is enabled, use the repository's **Security → Report a vulnerability** flow. Otherwise request a private contact route without disclosing sensitive details.

If a credential is exposed, revoke or rotate it first, then coordinate cleanup of the repository and its history. Removing the current file alone is insufficient.
