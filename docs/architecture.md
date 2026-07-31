# System Architecture

*Status: Normative. Governs every document in `docs/`. See [`philosophy.md`](philosophy.md) for the design-ethics decisions this architecture encodes structurally.*

---

## 1. Layered View

```
┌─────────────────────────────────────────────────────────────────┐
│  CHANNELS            Gmail · Slack · Calendar · Webhooks         │
└───────────────────────────────┬───────────────────────────────────┘
                                  │ raw event
┌───────────────────────────────▼───────────────────────────────────┐
│  CORTEX (docs/cortex/)                                             │
│    Ingestion → Sanitization → Fingerprinting → Scoring             │
└───────────────────────────────┬───────────────────────────────────┘
                                  │ scored, prioritized event
                ┌────────────────┼────────────────┬──────────────────┐
                ▼                ▼                ▼                  ▼
┌───────────────────┐ ┌───────────────────┐ ┌──────────────────┐ ┌──────────────┐
│ PERSONA            │ │ NEGOTIATION        │ │ ENERGY            │ │ AUDIT LOG    │
│ (docs/persona/)     │ │ (docs/negotiation/)│ │ (docs/energy/)     │ │              │
│ style-matched draft │ │ pricing/leverage   │ │ capacity check     │ │ every        │
│                     │ │ (transparent only) │ │ (own data only)    │ │ decision     │
└─────────┬───────────┘ └─────────┬──────────┘ └─────────┬──────────┘ └──────────────┘
          └────────────────────────┼──────────────────────┘
                                    ▼
                     ┌───────────────────────────┐
                     │   HUMAN REVIEW / SEND      │
                     │   (always the final gate)  │
                     └───────────────────────────┘
```

Cross-cutting, applied to every layer above: **SECURITY** (`docs/security/` —
anonymization, encryption, local-first storage) and **DEPLOYMENT**
(`docs/deployment/` — how each layer is actually run).

## 2. Design Principles

1. **The human is always the final gate.** No layer sends, commits, or acts
   on the founder's behalf without an explicit send/approve step — this is
   the one invariant every other design decision is subordinate to.
2. **Every score is explainable.** Scoring (§Cortex) and leverage
   calculations (§Negotiation) return the inputs that produced the output,
   not just a number — an unexplainable score cannot be trusted or debugged.
3. **Nothing is invented.** No component fabricates facts, deadlines, or
   pretexts about the world to influence a counterparty's behavior. See
   `philosophy.md` for the specific mechanisms this rules out.
4. **Own-data-only for sensitive inference.** Biometric and cognitive-load
   inference (§Energy) operates exclusively on the founder's own,
   consented data — never on a third party's inferred psychological state.
5. **Local-first, anonymized-by-default.** Raw identifying data
   (names, amounts, locations) is tokenized before it leaves the local
   environment toward any external model API (§Security).

## 3. Component Responsibilities

| Component | Input | Output | Docs |
|---|---|---|---|
| Ingestion | Raw message/event | Cleaned text + metadata + fingerprint | [`cortex/ingestion.md`](cortex/ingestion.md) |
| Scoring | Cleaned text + metadata | Priority tier, urgency score, sentiment | [`cortex/scoring.md`](cortex/scoring.md) |
| Persona | Scored message + writing-style profile | Drafted response | [`persona/mirror.md`](persona/mirror.md), [`persona/stylometry.md`](persona/stylometry.md) |
| Masks | Context (relationship type, DEFCON tier) | Selected tone/register for drafting | [`persona/masks.md`](persona/masks.md) |
| Negotiation | Deal context + market data | Price/leverage suggestion, with justification | [`negotiation/algorithms.md`](negotiation/algorithms.md) |
| Energy | Founder's biometric/behavioral data | Capacity score, pacing recommendation | [`energy/biometrics.md`](energy/biometrics.md), [`energy/decision-fatigue.md`](energy/decision-fatigue.md) |
| Security | All of the above | Anonymized payloads, encrypted storage | [`security/`](security/) |

## 4. Data Flow (Single Message, End to End)

1. A message arrives via a channel connector (`docs/examples/`).
2. **Ingestion** sanitizes it and computes a fingerprint (dedup key).
3. **Scoring** assigns urgency/sentiment/priority (`reference/formulas.md`
   §Scoring).
4. Based on priority tier, the message is routed:
   - High priority + commercial context → **Negotiation** module attaches
     data-driven pricing context.
   - Any priority, if a reply is warranted → **Persona** drafts a response
     in the appropriate mask.
5. Before the draft is surfaced, **Energy** checks whether this is a good
   moment to interrupt the founder (capacity score) — if not, it's queued,
   never silently dropped or misrepresented.
6. The founder reviews and sends. The entire path — score, draft rationale,
   capacity check — is logged for audit (`security/privacy.md`).

## 5. Trust Boundaries

```
[ External channel APIs ]  ── untrusted input
          │
[ Anonymization layer ]     ── strips identifying data before this line
          │
[ Scoring / Persona / Negotiation models ]  ── may call external LLM APIs
          │                                     with anonymized payload only
[ Local store: Iron Vault ] ── encrypted at rest, never leaves local env
          │
[ Founder's review UI ]     ── trusted, full de-anonymized context
```

Full threat model: [`security/threat-model.md`](security/threat-model.md).

## 6. What This Architecture Does Not Include

Per `philosophy.md`: no component fabricates calendar events, artificial
scarcity claims, or covert response-delay penalties. Where the original
whitepaper described these as features, this architecture implements the
underlying legitimate need (focus protection, fair prioritization, honest
urgency signaling) without the deceptive mechanism.
