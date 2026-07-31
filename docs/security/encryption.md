# Security — Encryption (The Iron Vault)

*Governs: `prototype/python/security/vault.py`. This is the local storage
and encryption layer referenced throughout `docs/`.*

## Three-Layer Model

Preserved directly from the whitepaper's "Iron Vault" architecture — this
part was already sound engineering:

1. **Layer 1 — The Scrubber.** A local, pre-network tokenization step that
   replaces names, amounts, and locations with stable tokens (e.g.,
   `[ENTITY_042]`) before anything leaves the local environment.
2. **Layer 2 — Encrypted Transport.** All communication between local
   components uses TLS; any inter-service calls (if deployed beyond a
   single machine, see `deployment/docker.md`) go through encrypted
   tunnels only.
3. **Layer 3 — Encrypted-at-Rest Storage.** Vector embeddings and stored
   context are encrypted at rest using a founder-held key — not
   recoverable by anyone without that key, including the maintainers of
   this project.

## Reference Implementation

```python
from cryptography.fernet import Fernet

class IronVault:
    """Local encryption layer. The master key never leaves the
    founder's environment and is never transmitted to any external
    service, including LLM providers."""

    def __init__(self, master_key: bytes):
        self.cipher = Fernet(master_key)

    def lock(self, plaintext: str) -> bytes:
        return self.cipher.encrypt(plaintext.encode())

    def unlock(self, ciphertext: bytes) -> str:
        """Decrypts only into volatile memory for the duration of
        active processing — never written back to disk unencrypted."""
        return self.cipher.decrypt(ciphertext).decode()
```

Full implementation: [`prototype/python/security/vault.py`](../../prototype/python/security/vault.py).

## Key Management

- The master key is generated locally on first setup
  (`deployment/local.md` §Setup) and stored in an OS-level secret store
  (e.g., macOS Keychain, Windows Credential Manager) — never in a
  plaintext config file, never committed to version control.
- Losing the key means losing access to encrypted history by design —
  there is no backdoor or recovery mechanism, which is the correct
  trade-off for data this sensitive.
