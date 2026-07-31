# Negotiation Intelligence — Strategy Patterns

*Consumes: conversation history + `LeverageScore`. Produces: mask
selection and follow-up timing recommendations.*

## Sentiment Drift Tracking

Tracking how a counterparty's language evolves across a thread is
legitimate, observable signal — it's the same thing an attentive human
negotiator does manually:

| Pattern | Signal | System response |
|---|---|---|
| Increasing use of possessive language ("our project," "when we start") | Positive drift | Consider surfacing relevant add-on options |
| Shift to shorter, more formal replies | Negative drift | Switch to Diplomat mask; consider surfacing a relevant case study or reference, if genuinely relevant |

## Follow-Up Timing

Reasonable, non-deceptive follow-up cadence:

- **Days 1–3:** No follow-up — let the counterparty process the proposal.
- **Day 4+:** If the counterparty has engaged (e.g., opened the proposal
  document repeatedly per real tracking data) without replying, a check-in
  message is appropriate — because the underlying behavior (repeated
  engagement, no reply) is real and worth naming honestly: *"Wanted to
  check whether you had any questions on the proposal"* — not a fabricated
  resource-withdrawal pretext.

## Recovery / Re-Engagement (Existing Clients)

For clients showing inactivity signals, honest re-engagement is
appropriate: sharing a genuinely relevant update, insight, or new
offering — never a manufactured "secret" urgency.

## What This Document Deliberately Omits

The whitepaper's silence-as-"psychological torture" framing and the
described adversarial-AI training loop for maximizing extracted price are
not included here as specified. Data-driven pricing (`pricing.md`) already
captures the legitimate underlying goal — pricing well — without framing
the counterparty as an adversary to be defeated by any means.
