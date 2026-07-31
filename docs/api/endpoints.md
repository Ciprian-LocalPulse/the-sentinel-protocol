# API — Endpoints

*Status: Planned (see `ROADMAP.md` Phase 4). Documents the intended
service wrapper around `prototype/python/`. Not yet implemented as a
running service — the modules in `prototype/python/` are currently
called directly, not over HTTP.*

## Design Notes

The API surface mirrors the pillar structure so the mapping from
architecture (`docs/architecture.md`) to endpoint is always obvious. Every
endpoint that returns a score or draft includes the same `factors` /
`explanation` shape used throughout this repo — no endpoint returns a bare
number or a bare draft with no rationale.

## Endpoints

### `POST /v1/ingest`
Body: raw message payload + headers.
Returns: `IngestedMessage` (see `schemas.md`).

### `POST /v1/score`
Body: an `IngestedMessage` fingerprint, plus optional CRM context.
Returns: `ScoredMessage` — conforms to `schemas/analysis.schema.json`.

### `POST /v1/draft`
Body: a `ScoredMessage` + mask override (optional) + context.
Returns: a draft object `{ "draft_text": str, "mask": str, "style_match_score": int, "verification_flags": [str] }`.
Never sends — drafting only. See `docs/design-principles.md` §2.

### `POST /v1/negotiation/offer`
Body: `DealContext` (see `schemas/context.schema.json`).
Returns: `OfferSuggestion` (see `docs/negotiation/algorithms.md`).

### `GET /v1/energy/capacity`
Returns: current `CapacityScore` for the authenticated founder.

### `POST /v1/send`
Body: a reviewed draft + explicit founder confirmation token.
The only endpoint that transmits anything externally. Requires
confirmation unless the specific channel/context has been explicitly
configured for auto-send (`reference/terminology.md`).

## Authentication

All endpoints require founder-scoped authentication (see
`docs/deployment/local.md` for the reference single-user setup;
multi-user/team deployment is `docs/deployment/cloud.md`, Planned).
