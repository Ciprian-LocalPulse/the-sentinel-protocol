# Security — Privacy & Audit

## Anonymization Before External API Calls

Any payload sent to an external LLM API (for scoring, drafting, or
negotiation support) passes through the Scrubber (`encryption.md` §Layer
1) first. A typical transformation:

```
Before:  "John Smith from Acme Corp offered €45,000 for the Q3 contract"
After:   "[ENTITY_012] from [ORG_004] offered [AMOUNT_001] for the [ITEM_002]"
```

The mapping between tokens and real values is stored only in the local
Iron Vault, and is re-applied locally after the model responds — the
external provider never sees real names, amounts, or organizations.

## Audit Log

Every scored message, drafted response, mask selection, and capacity
check is logged, append-only, locally:

```json
{
  "timestamp": "2026-07-31T10:15:00Z",
  "event": "message_scored",
  "fingerprint": "a1b2c3...",
  "tier": "P2",
  "factors": {"FC": 8, "EV": 6, "TD": 3, "SA": 5}
}
```

This log is the accountability backbone referenced throughout `docs/` — if
a draft or score is ever questioned, the audit log shows exactly what
produced it, per [`design-principles.md`](../design-principles.md) §1.

## Third-Party Data Handling

Sentiment/urgency analysis is performed on inbound messages to route the
founder's *own* attention. It is:

- **Never** stored as a persistent psychological profile of the sender.
- **Never** shared with or surfaced to any party other than the founder.
- **Purged** along with the message's normal retention lifecycle — it is
  a processing artifact, not a permanent dossier.

## Data Subject Rights

Where applicable jurisdiction requires it (e.g., GDPR for EU
counterparties), the founder — as the data controller for their own
business communications — remains responsible for honoring access/erasure
requests. This system's local-first, tokenized design is intended to make
that easier, not to create a compliance obligation of its own beyond what
the founder's business already carries.
