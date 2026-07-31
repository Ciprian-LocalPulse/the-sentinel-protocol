"""
Security — Iron Vault
Reference implementation for docs/security/encryption.md

Requires: pip install cryptography
"""
from __future__ import annotations

from cryptography.fernet import Fernet


class IronVault:
    """Local encryption layer. The master key never leaves the
    founder's environment and is never transmitted to any external
    service, including LLM providers. See docs/security/encryption.md."""

    def __init__(self, master_key: bytes):
        self.cipher = Fernet(master_key)

    @staticmethod
    def generate_key() -> bytes:
        """Generates a new local master key. Should be run once,
        during setup, and stored in an OS-level secret store —
        never committed to version control."""
        return Fernet.generate_key()

    def lock(self, plaintext: str) -> bytes:
        return self.cipher.encrypt(plaintext.encode("utf-8"))

    def unlock(self, ciphertext: bytes) -> str:
        """Decrypts only into volatile memory for the duration of
        active processing."""
        return self.cipher.decrypt(ciphertext).decode("utf-8")


class Scrubber:
    """Layer 1 anonymization: tokenizes identifying entities before
    any payload reaches an external model API.
    See docs/security/privacy.md#anonymization-before-external-api-calls."""

    def __init__(self):
        self._token_map: dict[str, str] = {}
        self._reverse_map: dict[str, str] = {}
        self._counter = 0

    def tokenize(self, value: str, kind: str = "ENTITY") -> str:
        if value in self._token_map:
            return self._token_map[value]
        self._counter += 1
        token = f"[{kind}_{self._counter:03d}]"
        self._token_map[value] = token
        self._reverse_map[token] = value
        return token

    def detokenize(self, text: str) -> str:
        for token, value in self._reverse_map.items():
            text = text.replace(token, value)
        return text
