# Roadmap

## Phase 0 — Foundation — DONE
## Phase 1 — Architecture — DONE (all 5 diagrams: architecture, sequence, trust-boundaries, pipeline, deployment)
## Phase 2 — Domain Specifications (five pillars) — DONE
## Phase 3 — Schemas & Prompts — DONE
## Phase 4 — Reference Prototype — DONE
- [x] All core modules + 37 unit tests
- [x] API service (prototype/python/api/server.py, FastAPI) + 9 API tests
- [x] 46/46 tests passing, CI green
## Phase 5 — Deployment & Examples — DOCS DONE, IMPLEMENTATION PENDING
- [x] docs/deployment/ — local (runnable today), Docker (planned), cloud (future)
- [x] docs/examples/ — Gmail, Slack, Calendar (integration patterns documented)
- [ ] Actual channel connector implementations (OAuth flows, live polling)
- [ ] POST /v1/send endpoint (requires per-channel OAuth)
## Phase 6 — Developer Experience — DONE
- [x] docs/developers/ — getting-started, coding-standards, contribution-guide
- [x] docs/developers/adr/ — ADR-001 (reframing), ADR-002 (local-first), ADR-003 (renaming)
- [x] README badges (tests, license, python version, FastAPI)

## What's Left for a v1.0 Release
- [ ] Live channel connectors (Gmail/Slack/Calendar OAuth)
- [ ] POST /v1/send with per-channel auth
- [ ] LLM provider wiring for full draft-text generation (currently mask-selection only)
- [ ] docs/api/ authentication scheme, formally specified
