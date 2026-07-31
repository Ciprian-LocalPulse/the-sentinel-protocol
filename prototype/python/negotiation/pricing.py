"""
Negotiation Intelligence — Pricing Tiers
Reference implementation for docs/negotiation/pricing.md
"""
from __future__ import annotations


def build_offer_tiers(base_price: float, leverage_score: float) -> dict:
    """Three-offer structure (premium / target / reduced).
    See docs/negotiation/pricing.md#the-three-offer-structure."""
    return {
        "premium": {"price": round(base_price * 1.8, 2), "scope": "full"},
        "target": {
            "price": round(base_price * (1 + 0.1 * leverage_score), 2),
            "scope": "standard",
        },
        "reduced": {"price": round(base_price * 0.6, 2), "scope": "reduced"},
    }
