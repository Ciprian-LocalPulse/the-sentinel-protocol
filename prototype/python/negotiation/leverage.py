"""
Negotiation Intelligence — Leverage
Reference implementation for docs/negotiation/algorithms.md

All inputs must trace to real, sourced signals. Never fabricated.
See docs/philosophy.md and docs/negotiation/pricing.md#honest-scarcity-signaling.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class DealContext:
    urgency: float          # 0-10, from real counterparty language (Cortex EV)
    uniqueness: float       # 0-10, configured per offering
    substitute_count: int   # count of competitors the counterparty actually named
    time_buffer_days: int   # days until a REAL, sourced deadline


@dataclass
class OfferSuggestion:
    price_multiplier: float
    rationale: str
    mask: str
    leverage_score: float


def calculate_leverage(context: DealContext) -> float:
    """Lv = (Urgency x Uniqueness) / (SubstituteCount x TimeBuffer)
    See docs/negotiation/algorithms.md."""
    substitutes = max(1, context.substitute_count)  # avoid div-by-zero
    time_buffer = max(1, context.time_buffer_days)
    return (context.urgency * context.uniqueness) / (substitutes * time_buffer)


def generate_offer(context: DealContext, base_price: float) -> OfferSuggestion:
    leverage = calculate_leverage(context)
    if leverage > 2.5:
        return OfferSuggestion(
            price_multiplier=1.4,
            rationale=(
                f"High measured leverage ({leverage:.2f}) based on real urgency, "
                f"uniqueness, and limited stated substitutes."
            ),
            mask="executive",
            leverage_score=round(leverage, 2),
        )
    return OfferSuggestion(
        price_multiplier=1.1,
        rationale=f"Standard market alignment (leverage {leverage:.2f}).",
        mask="diplomat",
        leverage_score=round(leverage, 2),
    )


def scarcity_signal(real_capacity_remaining: int | None, real_deadline: str | None) -> str | None:
    """Returns a scarcity message ONLY if a real constraint exists.
    See docs/negotiation/pricing.md#honest-scarcity-signaling."""
    if real_capacity_remaining is None or real_deadline is None:
        return None
    return f"We have {real_capacity_remaining} slots open before {real_deadline}."
