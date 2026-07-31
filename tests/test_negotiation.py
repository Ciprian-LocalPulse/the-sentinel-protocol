from prototype.python.negotiation.leverage import (
    DealContext,
    calculate_leverage,
    generate_offer,
    scarcity_signal,
)
from prototype.python.negotiation.pricing import build_offer_tiers


def test_calculate_leverage_matches_formula():
    context = DealContext(urgency=7, uniqueness=8, substitute_count=2, time_buffer_days=5)
    assert calculate_leverage(context) == (7 * 8) / (2 * 5)


def test_calculate_leverage_avoids_division_by_zero():
    context = DealContext(urgency=5, uniqueness=5, substitute_count=0, time_buffer_days=0)
    # Should not raise
    result = calculate_leverage(context)
    assert result > 0


def test_generate_offer_high_leverage_path():
    context = DealContext(urgency=9, uniqueness=9, substitute_count=1, time_buffer_days=2)
    offer = generate_offer(context, base_price=1000)
    assert offer.price_multiplier == 1.4
    assert offer.mask == "executive"


def test_generate_offer_standard_path():
    context = DealContext(urgency=2, uniqueness=2, substitute_count=5, time_buffer_days=30)
    offer = generate_offer(context, base_price=1000)
    assert offer.price_multiplier == 1.1
    assert offer.mask == "diplomat"


def test_scarcity_signal_returns_none_without_real_constraint():
    assert scarcity_signal(None, None) is None
    assert scarcity_signal(3, None) is None
    assert scarcity_signal(None, "2026-08-15") is None


def test_scarcity_signal_returns_message_with_real_constraint():
    msg = scarcity_signal(3, "2026-08-15")
    assert msg == "We have 3 slots open before 2026-08-15."


def test_build_offer_tiers_structure():
    tiers = build_offer_tiers(base_price=1000, leverage_score=3.0)
    assert tiers["premium"]["price"] == 1800.0
    assert tiers["reduced"]["price"] == 600.0
    assert tiers["target"]["price"] == 1300.0
