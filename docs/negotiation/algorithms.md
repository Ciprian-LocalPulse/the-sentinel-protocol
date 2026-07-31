# Negotiation Intelligence — Algorithms

*Governs: `prototype/python/negotiation/leverage.py`. Consumes: deal
context + market signals. Produces: a `LeverageScore` and pricing
suggestion, always with justification attached.*

*Renamed from the whitepaper's "Ghost Negotiation Matrix" — see
[`philosophy.md`](../philosophy.md) for the specific mechanisms changed and
why. The underlying leverage mathematics is preserved in full.*

## The Leverage Score

```
Lv = (Urgency × Uniqueness) / (SubstituteCount × TimeBuffer)
```

| Variable | Meaning | Source |
|---|---|---|
| `Urgency` | How time-sensitive the counterparty's need appears | Cortex sentiment/urgency signal (`cortex/scoring.md`), from their own messages |
| `Uniqueness` | How differentiated the offering is perceived to be | Configured per-offering, not inferred covertly |
| `SubstituteCount` | Number of competitors the counterparty has mentioned | Extracted from actual conversation content, never assumed |
| `TimeBuffer` | Time remaining until a real deadline (quarter-end, stated decision date) | Calendar/CRM data, must be a real date |

```python
def generate_offer(context):
    leverage = (context.urgency * context.uniqueness) / (
        context.substitute_count * context.time_buffer
    )
    if leverage > 2.5:
        return {"price_multiplier": 1.4, "rationale": "high measured leverage",
                "mask": "executive"}
    return {"price_multiplier": 1.1, "rationale": "standard market alignment",
            "mask": "diplomat"}
```

Reference: [`prototype/python/negotiation/leverage.py`](../../prototype/python/negotiation/leverage.py).

## What Changed From the Original Formula, and Why It Doesn't Weaken It

The math is identical to the whitepaper's `Lv` formula. What changed is
**what's allowed to feed it**: every input must trace to something real —
an actual stated deadline, an actual competitor the counterparty named,
actual uniqueness the founder has configured — never an inferred or
fabricated value designed to nudge the score. A leverage score built from
real signals is *more* useful than one partly built from invented ones,
not less: it degrades gracefully as circumstances change, instead of
collapsing the moment a fabricated input is discovered to be false.

## Market Intelligence Inputs

Legitimate, publicly available signals only:

- Public funding announcements (relevant to `Urgency`/`Uniqueness` framing)
- Public leadership changes at a counterparty organization
- Aggregated, published market-sentiment indicators

Scraping or acquiring non-public information about a counterparty is out
of scope for this module.
