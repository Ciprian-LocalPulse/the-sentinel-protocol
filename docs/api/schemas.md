# API — Schemas

The API's request/response bodies are defined by the canonical JSON
Schemas in [`schemas/`](../../schemas/), not duplicated here:

| Schema | Used by | File |
|---|---|---|
| `ScoredMessage` | `POST /v1/score` response | [`schemas/analysis.schema.json`](../../schemas/analysis.schema.json) |
| `ConversationContext` | `POST /v1/draft`, `POST /v1/negotiation/offer` request | [`schemas/context.schema.json`](../../schemas/context.schema.json) |
| `StyleProfile` | Internal, used by drafting | [`schemas/persona.schema.json`](../../schemas/persona.schema.json) |

Keeping schemas in one canonical location (`schemas/`) rather than
re-specified per-document is deliberate — a schema drifting between two
places it's defined is a correctness bug waiting to happen.

## Validation

Every API implementation MUST validate request/response bodies against
these schemas before processing. Example (Python, using `jsonschema`):

```python
import json
from jsonschema import validate

with open("schemas/analysis.schema.json") as f:
    schema = json.load(f)

validate(instance=scored_message_dict, schema=schema)
```
