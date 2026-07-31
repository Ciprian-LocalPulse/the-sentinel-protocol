<p align="center">
  <img src="assets/sentinel-shield.png" alt="The Sentinel Protocol" width="600">
</p>

# The Sentinel Protocol

**A reference architecture for emotionally-aware business automation.**

Developed by Ciprian Ștefan Pleșca (Stefano D'angelo).

---

## What This Is

Most business automation is stateless and context-blind: the same
auto-reply goes to a client who just signed a six-figure contract and to
someone asking for a discount. The Sentinel Protocol is an architecture
for automation that carries context — urgency, sentiment, the founder's
own capacity to make good decisions right now — through every stage of
handling a message, a negotiation, or a schedule.

This repository is the engineering specification: architecture documents,
schemas, prompt specifications, and a reference prototype. The original
conceptual whitepaper is preserved in [`papers/`](papers/) as the vision
document; `docs/` is what an engineer actually implements from.

## The Five Pillars

| Pillar | What it does | Docs |
|---|---|---|
| **Cortex** | Ingests messages, scores urgency and sentiment, routes by priority | [`docs/cortex/`](docs/cortex/) |
| **Neural Persona** | Learns your writing style, drafts responses that sound like you | [`docs/persona/`](docs/persona/) |
| **Energy Shield** | Paces your workload against your own biometric/cognitive capacity | [`docs/energy/`](docs/energy/) |
| **Negotiation Intelligence** | Data-driven pricing and leverage analysis, transparent by design | [`docs/negotiation/`](docs/negotiation/) |
| **Sovereign Path** | Local-first, layered-anonymization data security | [`docs/security/`](docs/security/), [`docs/deployment/`](docs/deployment/) |

See [`docs/philosophy.md`](docs/philosophy.md) for the design principles
behind these five pillars, including the specific places where this
specification is deliberately more conservative than the original
whitepaper, and why.

## Architecture at a Glance

```
Message / Event
      │
      ▼
  Ingestion (docs/cortex/ingestion.md) — clean, fingerprint, extract metadata
      │
      ▼
  Scoring (docs/cortex/scoring.md) — urgency/sentiment/priority
      │
      ▼
  Routing (priority tiers, not covert manipulation — see philosophy.md)
      │
      ├─▶ Drafting (docs/persona/) — style-matched response, if applicable
      ├─▶ Negotiation support (docs/negotiation/) — if commercial context
      └─▶ Capacity check (docs/energy/) — is now a good time to surface this?
      │
      ▼
  Human review / send (the founder is always the final approver)
```

Full component and data-flow detail: [`docs/architecture.md`](docs/architecture.md).

## Status

This is architecture-first work: documentation and schemas are the
priority, a working prototype follows once the specification is stable.
See [`ROADMAP.md`](ROADMAP.md) for what's built vs. planned.

| Layer | Status |
|---|---|
| Architecture & design docs | In progress |
| JSON schemas (`schemas/`) | Planned |
| Reference prototype (`prototype/`) | Planned |
| Prompt specifications (`prompts/`) | Planned |

## Repository Map

```
docs/            — architecture, philosophy, per-pillar specifications
schemas/         — JSON Schemas for core data structures
prompts/         — versioned prompt specifications (no secret "God Prompt" — see CONTRIBUTING.md)
reference/       — formulas, scoring definitions, terminology
papers/          — original whitepaper and positioning document
examples/        — sample payloads
prototype/       — reference implementation
tests/           — test suite for the prototype
```

## License

MIT — see [`LICENSE`](LICENSE). The architecture and code are open. The
original whitepaper in `papers/` remains separately attributed to the
author as the source vision document.

## Contributing

See [`CONTRIBUTING.md`](CONTRIBUTING.md).
