# Deployment — Local

*The recommended starting setup, per `docs/design-principles.md` §7
("simple first, elastic later").*

## Requirements

- Python 3.11+
- An LLM API key (Anthropic or OpenAI-compatible) for the model-backed
  components (`prompts/`)
- (Optional) A wearable API key (Oura/Garmin/Whoop) for the Energy Shield

## Setup

```bash
git clone https://github.com/Ciprian-LocalPulse/the-sentinel-protocol.git
cd the-sentinel-protocol
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## Generate a Local Master Key

```python
from prototype.python.security.vault import IronVault
key = IronVault.generate_key()
print(key)
# Store this in your OS secret store, e.g. environment variable
# SENTINEL_MASTER_KEY — never commit it to version control.
```

## Configuration

Copy `.env.example` to `.env` (see `prototype/python/.env.example`) and
set:

```
SENTINEL_MASTER_KEY=<generated above>
LLM_API_KEY=<your provider key>
WEARABLE_API_KEY=<optional>
```

## Running the Reference Pipeline

```bash
python -m prototype.python.cortex.ingestion
python -m prototype.python.cortex.scoring
```

See [`tests/`](../../tests/) for full pipeline usage examples.

## Data Location

By default, all local state (Iron Vault, audit log) lives under
`~/.sentinel/` — never inside the repository directory, to avoid
accidental commits of sensitive data.
