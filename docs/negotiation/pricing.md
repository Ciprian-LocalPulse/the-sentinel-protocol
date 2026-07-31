# Negotiation Intelligence — Pricing Architecture

*Governs: `prototype/python/negotiation/pricing.py`. Consumes:
`LeverageScore` (`algorithms.md`) + base pricing config. Produces: a
structured multi-option offer.*

## The Three-Offer Structure

Preserved from the whitepaper's "Anchor Strategy" — this is standard,
well-established pricing psychology (decoy-effect / choice architecture),
not a manipulation technique specific to this system, and is used
transparently:

1. **Premium option** — full-scope offering, sets the upper anchor.
2. **Target option** — what the founder actually wants to sell most often,
   optimized for margin and typically the mid-priced option.
3. **Reduced option** — a genuinely reduced-scope offering (fewer
   deliverables, not fewer promises kept) — never a stripped-down version
   presented as equivalent to the others.

```python
def build_offer_tiers(base_price, leverage_score):
    return {
        "premium": {"price": round(base_price * 1.8, 2), "scope": "full"},
        "target": {"price": round(base_price * (1 + 0.1 * leverage_score), 2), "scope": "standard"},
        "reduced": {"price": round(base_price * 0.6, 2), "scope": "reduced"},
    }
```

## Honest Scarcity Signaling

Where the whitepaper's follow-up sequence used a fabricated pretext ("I
have withdrawn the resource allocation..."), this architecture only
signals scarcity that is real:

```python
def scarcity_signal(real_capacity_remaining, real_deadline):
    """
    Returns a scarcity message ONLY if a real constraint exists.
    Never fabricates capacity or deadline pressure.
    """
    if real_capacity_remaining is None or real_deadline is None:
        return None  # no fabricated urgency — silence is the correct output
    return f"We have {real_capacity_remaining} slots open before {real_deadline}."
```

If there is no real constraint, the function returns nothing — an honest
absence of urgency framing, rather than an invented one. This is the
concrete implementation of `philosophy.md`'s core rule.

## Contract & Payment Automation

On detecting explicit agreement in a message thread (Cortex intent
classification), the system can generate a contract from a template
(e.g., via a document-automation API) and a payment link — always
presented to the founder for review before sending, per
[`design-principles.md`](../design-principles.md) §2.
