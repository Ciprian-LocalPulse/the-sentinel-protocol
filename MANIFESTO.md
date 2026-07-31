# MANIFESTO

## The Sentinel Protocol — An Open Reference Architecture for Emotionally-Aware Business Automation

*Ciprian Ștefan Pleșca (Stefano D'angelo)*
*Version 1.0 — July 2026*

---

## Abstract

Business communication carries signal that purely rule-based automation
discards: urgency, sentiment, relational history, and the operator's own
cognitive capacity to act on it well. The Sentinel Protocol is a reference
architecture — five composable subsystems, a formal data model, a tested
Python implementation, and a documented set of design invariants — for
automation that carries this context through every stage of handling a
message, a negotiation, or a schedule, while remaining accountable to a
single, non-negotiable constraint: the system does not fabricate
information that another person relies on as true. This document states
what the system is, why it is built the way it is, what it is for, and
why its engineering choices are what they are.

## 1. What This System Helps With

Three concrete failure modes motivate this architecture:

1. **Undifferentiated response.** A stateless automation replies
   identically to a message that closes a contract and to a message that
   asks for a discount. This is not efficiency; it is a category error
   about what the message actually requires.
2. **Decision fatigue as an unmanaged resource.** Every unscored message
   a person opens consumes a measurable amount of decision-making
   capacity before its content is even read. Left unmanaged, this
   capacity degrades the quality of every subsequent decision that day.
3. **Negotiation conducted reactively, under time pressure, without
   the benefit of aggregated signal a single human cannot hold in
   working memory at once** — deal history, market context, and
   counterparty behavior across a relationship, not just the current
   message.

The system helps by making all three legible and actionable: it scores
what arrives (Cortex), drafts in a consistent, appropriate voice
(Persona), paces workload against real capacity (Energy Shield), and
supports pricing decisions with real, sourced signal (Negotiation
Intelligence) — all under a security model that keeps the operator's data
local-first and anonymized before it ever reaches a third-party model
provider (Sovereign Path).

## 2. Architecture, Restated

The system is a pipeline, not a monolith: ingestion produces a clean,
fingerprinted message; scoring produces an explainable priority; routing
sends the scored event to whichever of Persona, Energy, or Negotiation is
relevant; and every path converges on a single invariant — a human
reviews and approves before anything is sent. This shape is documented in
full in [`docs/architecture.md`](docs/architecture.md) and diagrammed in
[`docs/diagrams/`](docs/diagrams/); it is restated here only to establish
the two properties this manifesto argues for:

- **Explainability is structural, not incidental.** Every score returned
  by this system carries its contributing factors and a plain-language
  explanation as a *schema-enforced requirement*
  ([`schemas/analysis.schema.json`](schemas/analysis.schema.json)), not a
  documentation convention that code can silently drift away from.
- **The trust boundary is drawn before any external network call.**
  Identifying data is tokenized locally before any payload reaches an
  LLM provider ([`docs/security/privacy.md`](docs/security/privacy.md)).
  A full provider-side data breach, in this design, exposes tokens, not
  the underlying business.

## 3. On the Choice of Programming Language and Tooling

The reference implementation is written in Python 3.11+, exposed over an
HTTP API built with FastAPI. This choice is stated and defended, not
assumed:

- **Python** was chosen for the reference implementation because the
  system's core operations — text processing, scoring, data
  transformation — are I/O- and readability-bound, not
  compute-bound; Python's ecosystem for NLP, cryptography
  (`cryptography`), and schema validation (`jsonschema`) let the
  reference implementation stay close to the specification in
  `docs/`, which matters more here than raw execution speed. Nothing in
  the *architecture* (§2) is Python-specific — the JSON Schemas in
  `schemas/` are the actual language-independent contract, and a
  conforming implementation in another language is equally valid.
- **FastAPI** was chosen for the service layer because it generates its
  interactive API documentation (`/docs`) directly from the same type
  annotations that define the request/response contracts — reducing the
  distance between what the code does and what the code says it does,
  which is the same principle behind §2's explainability requirement,
  applied to the API layer itself.
- **JSON Schema**, rather than a language-specific type system, was
  chosen for the canonical data contracts (`schemas/`) precisely so that
  a JavaScript, Go, or Rust implementation of any pillar could validate
  against the same source of truth without reimplementing it — a
  concrete, checkable form of the interoperability this manifesto argues
  for in §5.

## 4. The Ethical Architecture

The system's five pillars are inherited from its original conceptual
design; three specific mechanisms from that original design are not
implemented as originally specified, because they require fabricating
information a third party — a client, a colleague, a family member —
would rely on as true. This is documented in full, with the reasoning
made explicit rather than asserted, in
[`docs/philosophy.md`](docs/philosophy.md) and
[`docs/developers/adr/ADR-001.md`](docs/developers/adr/ADR-001.md). The
position this manifesto takes is narrow and falsifiable: **a system that
never has to be caught lying is a more durable system than one that
lies well**, because its outputs remain valid under scrutiny instead of
collapsing the moment a fabricated claim is checked. This is offered as
an engineering argument, not only a moral one — see ADR-001 for the
consequences analysis.

## 5. A Call for Interoperability, Not Exclusivity

This architecture is published under the MIT license
([`LICENSE`](LICENSE)) specifically so that its data contracts
(`schemas/`), not just its Python implementation, can be adopted
independently. A negotiation-support tool, a triage system, or a
biometric pacing tool that conforms to `schemas/analysis.schema.json` or
`schemas/context.schema.json` is compatible with this architecture
whether or not it shares a single line of the reference Python code. The
authors consider this more valuable than a system that can only be
extended by its original authors — the opposite of what "impossible to
copy" would have meant, and a deliberate rejection of that framing.

## 6. What This Document Is Not

This is not a claim of uniqueness, of infinite ROI, or of exclusivity to
an elite population of users — see
[`docs/developers/adr/ADR-003.md`](docs/developers/adr/ADR-003.md) for
the explicit decision to remove that framing from this repository's
technical documentation. It is a statement of what was built, why it was
built this way, and an invitation to extend, audit, or fork it under the
terms of the license. The original whitepaper, preserved in
[`papers/sentinel-whitepaper.pdf`](papers/sentinel-whitepaper.pdf), remains
available as the historical source of the project's vision; this
manifesto is the engineering community's entry point into what that
vision became.

## Citation

See [`CITATION.cff`](CITATION.cff) for the machine-readable citation
record.

```
Pleșca, C. Ș. (2026). The Sentinel Protocol: A Reference Architecture
for Emotionally-Aware Business Automation. Version 1.0.
https://github.com/Ciprian-LocalPulse/the-sentinel-protocol
```
