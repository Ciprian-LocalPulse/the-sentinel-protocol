# Changelog

All notable changes to this project are documented here. Format loosely
follows [Keep a Changelog](https://keepachangelog.com/).

## [Unreleased]

### Added
- Full architecture documentation (`docs/architecture.md`,
  `design-principles.md`, `glossary.md`, `philosophy.md`)
- Five-pillar specifications: Cortex, Persona, Energy Shield, Negotiation
  Intelligence, Security (`docs/cortex/`, `docs/persona/`, `docs/energy/`,
  `docs/negotiation/`, `docs/security/`)
- Reference prototype in Python (`prototype/python/`) with test coverage
  (`tests/`)
- JSON Schemas for core data structures (`schemas/`)
- Versioned prompt specifications (`prompts/`)
- CI workflow running tests and schema validation on every push
  (`.github/workflows/tests.yml`)
- Deployment guidance (`docs/deployment/`) and channel integration
  examples (`docs/examples/`)

### Changed
- Repository repositioned from a sales-page format to an engineering
  reference architecture, per `docs/philosophy.md`
- Several whitepaper mechanisms reframed to remove deception of third
  parties, with the underlying legitimate need preserved (see
  `docs/philosophy.md` for the full mapping)

## [0.1.0] — Original Whitepaper Release
- Initial conceptual whitepaper published (`papers/sentinel-whitepaper.pdf`)
