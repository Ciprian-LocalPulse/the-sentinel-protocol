"""
Cortex — Ingestion
Reference implementation for docs/cortex/ingestion.md

Turns a raw channel payload into clean text + structured metadata.
Pure function style: no side effects, no scoring, no routing decisions.
"""
from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone


BOILERPLATE_PATTERN = re.compile(
    r"(Disclaimer|Unsubscribe|Confidentiality Notice).*", re.DOTALL | re.IGNORECASE
)
HTML_TAG_PATTERN = re.compile(r"<[^<]+?>")


@dataclass
class IngestedMessage:
    """Output of the ingestion pipeline. See docs/cortex/ingestion.md."""

    clean_text: str
    fingerprint: str
    metadata: dict = field(default_factory=dict)
    received_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))


class MessageIngestor:
    """Pipeline: sanitize -> fingerprint -> extract_metadata.

    Deliberately has no dependency on scoring or drafting logic —
    keeping ingestion pure makes it trivially unit-testable
    (see tests/test_ingestion.py).
    """

    def __init__(self, raw_data: str, headers: dict | None = None):
        self.raw_data = raw_data
        self.headers = headers or {}

    def sanitize(self) -> str:
        """Strip HTML markup and common legal/boilerplate blocks."""
        text = HTML_TAG_PATTERN.sub("", self.raw_data)
        text = BOILERPLATE_PATTERN.sub("", text)
        return text.strip()

    def fingerprint(self, clean_text: str) -> str:
        """SHA-256 of the cleaned body. Used for dedup + thread tracking."""
        return hashlib.sha256(clean_text.encode("utf-8")).hexdigest()

    def extract_metadata(self) -> dict:
        """Extract channel-agnostic metadata. Never used for silent
        auto-decisions — see docs/cortex/ingestion.md#metadata-fields."""
        sender = self.headers.get("From", "")
        return {
            "priority_header": self.headers.get("X-Priority", "3 (Normal)"),
            "sender_domain": sender.split("@")[-1] if "@" in sender else "",
            "auth_status": self.headers.get("Authentication-Results", "unknown"),
            "channel": self.headers.get("X-Sentinel-Channel", "email"),
        }

    def run(self) -> IngestedMessage:
        clean_text = self.sanitize()
        return IngestedMessage(
            clean_text=clean_text,
            fingerprint=self.fingerprint(clean_text),
            metadata=self.extract_metadata(),
        )


if __name__ == "__main__":
    sample = (
        "<p>Hi there, following up on our proposal.</p>"
        "<div>Disclaimer: This email is confidential...</div>"
    )
    ingestor = MessageIngestor(sample, headers={"From": "client@example.com"})
    result = ingestor.run()
    print(result)
