# Cortex — Ingestion

*Governs: `prototype/python/cortex/ingestion.py`. Consumes: raw channel
payloads. Produces: `IngestedMessage` objects consumed by `scoring.md`.*

## Purpose

Turn a raw, noisy channel payload (an email with HTML, signatures,
tracking pixels; a Slack message with formatting artifacts) into clean
text plus structured metadata, before anything is scored or shown to a
model.

## Pipeline

```
raw payload
   │
   ▼
1. Strip markup (HTML tags, CSS, tracking pixels)
   │
   ▼
2. Strip boilerplate (legal disclaimers, unsubscribe links, signatures)
   │
   ▼
3. Compute fingerprint (SHA-256 of cleaned body) — dedup + thread tracking
   │
   ▼
4. Extract metadata (sender domain, priority header, SPF/DKIM status,
   channel-specific fields)
   │
   ▼
IngestedMessage { clean_text, fingerprint, metadata, received_at }
```

## Reference Implementation

See [`prototype/python/cortex/ingestion.py`](../../prototype/python/cortex/ingestion.py).
The reference class is `MessageIngestor`, with methods `sanitize()`,
`fingerprint()`, and `extract_metadata()` — each independently unit-tested
(`tests/test_ingestion.py`).

## Metadata Fields

| Field | Type | Notes |
|---|---|---|
| `sender_domain` | string | Used for sender-weight scoring, never for automated blocking without review |
| `priority_header` | string | `X-Priority` or channel-equivalent, treated as a signal, not ground truth |
| `auth_status` | string | SPF/DKIM pass/fail — feeds a spam/spoofing confidence signal, not a silent auto-archive decision |
| `channel` | string | `email` \| `slack` \| `calendar` \| ... |
| `thread_id` | string | Derived from fingerprint continuity across a conversation |

## What Ingestion Explicitly Does Not Do

It does not classify, score, or make any routing decision — that's
`scoring.md`'s responsibility. Keeping ingestion pure (input → clean
structured output, no side effects) makes it trivially testable and safe
to re-run.
