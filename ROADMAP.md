# Roadmap

## Phase 0 — Foundation — DONE
- [x] Repository scaffold
- [x] README (engineering-first framing, with artwork)
- [x] docs/philosophy.md, GOVERNANCE.md, CONTRIBUTING.md, CODE_OF_CONDUCT.md, SECURITY.md
- [x] CHANGELOG.md, FAQ.md, CITATION.cff

## Phase 1 — Architecture — DONE
- [x] docs/architecture.md
- [x] docs/design-principles.md, docs/glossary.md
- [x] docs/diagrams/ — architecture.svg, trust-boundaries.svg, sequence.svg

## Phase 2 — Domain Specifications (the five pillars) — DONE
- [x] docs/cortex/ — ingestion, scoring, emotional-cortex
- [x] docs/persona/ — stylometry, mirror, masks
- [x] docs/energy/ — biometrics, decision-fatigue
- [x] docs/negotiation/ — algorithms, pricing, strategy
- [x] docs/security/ — threat-model, encryption, privacy

## Phase 3 — Schemas & Prompts — DONE
- [x] schemas/analysis.schema.json, context.schema.json, persona.schema.json
- [x] prompts/ — cortex, verifier, diplomat, executive, firewall (versioned)

## Phase 4 — Reference Prototype — DONE
- [x] prototype/python/ — ingestion, scoring, persona, energy, negotiation, security
- [x] tests/ — full pytest suite (ingestion, scoring, persona, energy, negotiation, security)
- [x] .github/workflows/tests.yml — CI on every push/PR
- [ ] docs/api/ service actually implemented (currently spec-only, docs/api/)

## Phase 5 — Deployment & Examples — DOCS DONE, IMPLEMENTATION PENDING
- [x] docs/deployment/ — local, Docker (planned), cloud (future)
- [x] docs/examples/ — Gmail, Slack, Calendar (integration patterns documented)
- [ ] Actual channel connector implementations
- [ ] Running API service (docs/api/endpoints.md)

## Phase 6 — Diagrams
- [x] architecture.svg, trust-boundaries.svg, sequence.svg
- [ ] pipeline.svg, deployment.svg
