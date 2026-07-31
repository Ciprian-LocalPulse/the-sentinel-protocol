# API — Endpoints

*Status: Reference implementation available at
[`prototype/python/api/server.py`](../../prototype/python/api/server.py)
(FastAPI). Run locally with `uvicorn prototype.python.api.server:app --reload`.
The drafting endpoint returns mask selection only — full LLM-backed draft
generation requires wiring a live model provider, per
`docs/deployment/local.md`, and is intentionally not hardcoded to one
provider in this reference server.*

## Design Notes

The API surface mirrors the pillar structure so the mapping from
architecture (`docs/architecture.md`) to endpoint is always obvious. Every
endpoint that returns a score or draft includes the same `factors` /
`explanation` shape used throughout this repo — no endpoint returns a bare
number or a bare draft with no rationale.

## Endpoints (Implemented)

### `POST /v1/ingest`
Body: `{ "raw_data": str, "headers": dict }`.
Returns: cleaned text, fingerprint, metadata. Conforms to the
`IngestedMessage` shape from `docs/cortex/ingestion.md`.

### `POST /v1/score`
Body: cleaned text + fingerprint + optional CRM/objectives context.
Returns: `ScoredMessage` — conforms to `schemas/analysis.schema.json`.

### `POST /v1/draft/mask`
Body: tier + relationship stage + context + detected intent.
Returns: the selected mask and its prompt spec path. (Full draft text
generation is not wired to a live LLM call in this reference server —
see the status note above.)

### `POST /v1/negotiation/offer`
Body: `DealContext` fields + base price + optional real
capacity/deadline.
Returns: `OfferSuggestion` + a `scarcity_signal` that is `null` unless a
real constraint was supplied — see `docs/negotiation/pricing.md#honest-scarcity-signaling`.

### `POST /v1/energy/capacity`
Body: `{ hrv_current, baseline_hrv, sleep_score }`.
Returns: capacity score, per `docs/energy/biometrics.md`.

### `POST /v1/energy/fatigue`
Body: `{ input_toxicity, switching_cost, cognitive_load }`.
Returns: DFS score + whether Focus Mode is triggered, per
`docs/energy/decision-fatigue.md`.

### `GET /v1/schemas/{schema_name}`
Serves the canonical JSON Schema from `schemas/` — single source of
truth, per `docs/api/schemas.md`.

### `GET /healthz`
Liveness check.

## Endpoints (Specified, Not Yet Implemented)

### `POST /v1/send`
Body: a reviewed draft + explicit founder confirmation token.
The only endpoint that would transmit anything externally. Requires
confirmation unless the specific channel/context has been explicitly
configured for auto-send (`reference/terminology.md`). Not implemented
in the reference server — sending requires per-channel OAuth
(`docs/examples/`) that is deployment-specific.

## Authentication

All endpoints require founder-scoped authentication (see
`docs/deployment/local.md` for the reference single-user setup;
multi-user/team deployment is `docs/deployment/cloud.md`, Planned).
