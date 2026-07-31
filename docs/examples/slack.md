# Integration Example — Slack

*Status: Planned. Slack messages map to the same `MessageIngestor` +
`score_message` pipeline as email, with channel-specific metadata.*

## Mapping

| Slack field | Sentinel metadata field |
|---|---|
| `channel` | `channel` (e.g. `#deals`, `#team-ops`) — feeds `context` for mask selection (`docs/persona/masks.md`) |
| `user` | `sender_domain` equivalent — internal team member ID |
| Thread `ts` | Used for `thread_id` continuity |

## Internal vs. External Routing

Slack messages from internal team channels are routed with
`context="internal_operational"`, which `select_mask()`
(`prototype/python/persona/masks.py`) maps to the Executive mask by
default — brief, action-oriented, per `docs/persona/masks.md#executive`.

## Sample Code

```python
from prototype.python.cortex.ingestion import MessageIngestor
from prototype.python.persona.masks import select_mask

def handle_slack_message(event: dict):
    headers = {"X-Sentinel-Channel": "slack", "From": event["user"]}
    ingested = MessageIngestor(event["text"], headers=headers).run()
    mask = select_mask(tier="P3", context="internal_operational")
    return ingested, mask
```
