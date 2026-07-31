# The Emotional Cortex — Overview

*Ties together [`ingestion.md`](ingestion.md) and [`scoring.md`](scoring.md)
into the conceptual "Cortex" pillar.*

## Why a Cortex, Not a Filter

A rule-based filter ("if subject contains 'urgent', flag it") breaks the
moment senders learn the rule. The Cortex instead treats every message as
carrying multiple weak signals — sender identity, emotional tone, timing,
strategic relevance — and combines them into a single, explainable score
(`scoring.md`). No single signal dominates by itself, which is what makes
it resistant to simple gaming.

## The Decision-Fatigue Argument

Every unscored message a founder opens costs a small amount of decision
capacity: *is this important? what tone do I need? can it wait?* The
Cortex's job is to answer those three questions before the founder ever
opens the message, so their attention is spent on the content, not the
triage. This is the same argument the whitepaper makes (§1.1 of the
original document) — kept, because it's simply true of how attention
works, independent of any of the reframing done elsewhere in this repo.

## Relationship to the Other Pillars

```
Cortex ──scored event──▶ Persona (drafts a response)
       ──scored event──▶ Negotiation (if commercial context)
       ──scored event──▶ Energy (checked before surfacing to founder)
```

The Cortex does not decide *what to say* (that's Persona) or *whether now
is a good time to say it* (that's Energy) — it only decides *how important
is this, and why*.

## Maintenance

Per [`design-principles.md`](../design-principles.md) §6, scoring weights
are versioned. A monthly recalibration review (see
`reference/scoring.md` §Recalibration) checks:

- **False-positive rate on P1** — how often a message scored P1 turned out
  not to warrant immediate attention (adjust `EV`/`FC` weights).
- **Missed-urgency rate** — messages the founder manually escalated that
  the Cortex under-scored.

Both are measured against logged outcomes (`security/privacy.md` — the
audit log), never estimated.
