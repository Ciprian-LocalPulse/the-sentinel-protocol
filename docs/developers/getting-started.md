# Developers — Getting Started

## 1. Clone and Install

```bash
git clone https://github.com/Ciprian-LocalPulse/the-sentinel-protocol.git
cd the-sentinel-protocol
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## 2. Run the Tests

```bash
pytest tests/ -v
```

All 46 tests (37 module-level + 9 API-level) should pass with no external
services required — the reference implementation has no hard dependency
on a live LLM or wearable API for its core logic tests.

## 3. Run the API Server Locally

```bash
uvicorn prototype.python.api.server:app --reload
```

Then visit `http://localhost:8000/docs` for the interactive FastAPI
Swagger UI, generated automatically from the endpoint definitions in
[`prototype/python/api/server.py`](../../prototype/python/api/server.py).

## 4. Where to Read Next

| If you want to... | Read |
|---|---|
| Understand the overall design | [`docs/architecture.md`](../architecture.md) |
| Understand *why* certain whitepaper mechanisms were changed | [`docs/philosophy.md`](../philosophy.md) |
| Add a new scoring factor | [`docs/cortex/scoring.md`](../cortex/scoring.md) + `reference/scoring.md` |
| Add a new channel integration | [`docs/examples/`](../examples/) for the pattern, then add a new file there |
| Modify a prompt | [`prompts/`](../../prompts/) — remember to bump the version, see `coding-standards.md` |

## 5. Recommended First Contribution

Pick one of the "Specified, Not Yet Implemented" items in
[`ROADMAP.md`](../../ROADMAP.md) — the `POST /v1/send` endpoint and a real
channel connector (`docs/examples/gmail.md`) are the two highest-value
next pieces.
