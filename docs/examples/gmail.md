# Integration Example — Gmail

*Status: Planned. Illustrates how a real Gmail message maps onto the
Cortex pipeline (`docs/cortex/`).*

## Flow

```
Gmail API (push notification or poll)
   │
   ▼
Extract: subject, body (HTML), headers (From, X-Priority, DKIM)
   │
   ▼
MessageIngestor(raw_data=body_html, headers=gmail_headers).run()
   │
   ▼
score_message(ingested, crm_value=..., days_since_last_contact=...)
   │
   ▼
If tier in (P1, P2) and reply warranted → drafting pipeline (docs/persona/mirror.md)
```

## Example Header Mapping

| Gmail field | Sentinel metadata field |
|---|---|
| `From` | `sender_domain` (parsed) |
| `X-Priority` (if present) | `priority_header` |
| `Authentication-Results` | `auth_status` |
| Thread-ID (Gmail's own) | Used alongside the content fingerprint for thread continuity |

## Sample Code

```python
from prototype.python.cortex.ingestion import MessageIngestor
from prototype.python.cortex.scoring import score_message

def handle_gmail_message(gmail_msg: dict):
    headers = {h["name"]: h["value"] for h in gmail_msg["payload"]["headers"]}
    body = extract_body_html(gmail_msg)  # Gmail API helper, not shown

    ingested = MessageIngestor(body, headers=headers).run()
    scored = score_message(ingested)
    return scored
```

## Required Gmail OAuth Scopes

`gmail.readonly` for ingestion; `gmail.send` is only requested if the
founder explicitly enables the send step (`docs/design-principles.md` §2)
— never requested by default.
