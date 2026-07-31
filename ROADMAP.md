# Roadmap

## Phase 0 — Foundation (this phase)
- [x] Repository scaffold
- [x] README (engineering-first framing)
- [x] `docs/philosophy.md` — design ethics and the whitepaper→spec mapping
- [ ] GOVERNANCE.md, CONTRIBUTING.md, CODE_OF_CONDUCT.md, SECURITY.md

## Phase 1 — Architecture
- [ ] `docs/architecture.md` — full system architecture
- [ ] `docs/design-principles.md`
- [ ] `docs/diagrams/` — architecture, sequence, pipeline, trust-boundary, deployment diagrams

## Phase 2 — Domain Specifications (the five pillars)
- [ ] `docs/cortex/` — ingestion, scoring, emotional-cortex
- [ ] `docs/persona/` — stylometry, mirror, masks
- [ ] `docs/energy/` — biometrics, decision-fatigue
- [ ] `docs/negotiation/` — algorithms, pricing, strategy (transparent-by-design)
- [ ] `docs/security/` — threat model, encryption, privacy

## Phase 3 — Schemas & Prompts
- [ ] `schemas/analysis.schema.json`, `context.schema.json`, `persona.schema.json`
- [ ] `prompts/` — versioned, reviewable prompt specifications

## Phase 4 — Reference Prototype
- [ ] `prototype/python/` — ingestion, scoring, drafting reference implementation
- [ ] `tests/` — test suite
- [ ] `docs/api/` — endpoints and schemas for a service wrapper

## Phase 5 — Deployment & Examples
- [ ] `docs/deployment/` — local, Docker, cloud
- [ ] `docs/examples/` — Gmail, Slack, Calendar integration patterns
