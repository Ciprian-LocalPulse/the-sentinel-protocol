# Cortex — Scoring

*Governs: `prototype/python/cortex/scoring.py`. Consumes: `IngestedMessage`.
Produces: `ScoredMessage` with priority tier and explainable factors.*

## Purpose

Assign a message a priority tier and an explanation for that tier, using
four weighted signals. This is the direct, renamed descendant of the
whitepaper's "S.P.S." formula — same structure, same intent (turn
subjective urgency into a comparable number), fully preserved.

## The Priority Score Formula

```
PriorityScore = (FC × 0.45) + (EV × 0.25) + (TD × 0.20) + (SA × 0.10)
```

| Variable | Name | Range | Source |
|---|---|---|---|
| `FC` | Financial Clout | 0–10 | Estimated deal/contract value relevance, from CRM context if available, else a conservative default |
| `EV` | Emotional Volatility | 0–10 | Sentiment-analysis magnitude (how strong the detected emotion is, not which direction) |
| `TD` | Time Decay | 0–10 | Time elapsed since last interaction without a response, normalized |
| `SA` | Strategic Alignment | 0–10 | Similarity between message content and the founder's stated current objectives |

Full derivation and worked examples: [`reference/formulas.md`](../reference/formulas.md).

## Priority Tiers

Renamed from the whitepaper's "DEFCON 1–5" (see `glossary.md` for why) to
a plain P1–P5 scale — same thresholds, same behavior, no crisis-response
framing for what is, functionally, inbox triage:

| Tier | PriorityScore | Meaning | Behavior |
|---|---|---|---|
| P1 | > 8.5 | Critical — major deal, crisis, or time-sensitive relationship event | Immediate surface to founder, bypasses batching |
| P2 | 6.5–8.5 | High-value opportunity or significant negative signal | Surfaced at top of next review batch |
| P3 | 3.5–6.5 | Normal operational message | Batched into scheduled review windows |
| P4 | 1.5–3.5 | Low priority, likely FYI | Batched, lower position |
| P5 | < 1.5 | Newsletter/spam-adjacent | Auto-archived, never shown unless searched for |

## Sentiment Analysis

`EV` is computed via a standard NLP sentiment/emotion classifier (see
`prototype/python/cortex/scoring.py::analyze_sentiment`), returning a
magnitude, not a covert psychological profile of the sender — the output
is used only to route the founder's *own* attention, never surfaced to or
used against the sender.

## Output Shape

```json
{
  "fingerprint": "a1b2c3...",
  "priority_score": 7.8,
  "tier": "P2",
  "factors": { "FC": 8, "EV": 6, "TD": 3, "SA": 5 },
  "explanation": "High financial clout (8/10) and moderate emotional volatility (6/10) drove this to P2."
}
```

Every score always includes `factors` and a plain-language `explanation`
— per [`design-principles.md`](../design-principles.md) §1.
