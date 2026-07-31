import pytest

from prototype.python.persona.masks import select_mask
from prototype.python.persona.stylometry import build_style_profile


def test_build_style_profile_requires_consent():
    with pytest.raises(ValueError):
        build_style_profile("p1", ["Hello there."], owner_consent=False)


def test_build_style_profile_basic_stats():
    corpus = ["We should scale this. It is a strong deliverable.", "Great work team!"]
    profile = build_style_profile("p1", corpus, owner_consent=True)
    assert profile.owner_consent is True
    assert profile.avg_sentence_length > 0
    assert profile.punctuation_profile["!"] == 1
    assert len(profile.top_keywords) > 0


def test_select_mask_boundary_request_returns_firewall():
    assert select_mask(tier="P2", detected_intent="boundary_request") == "firewall"


def test_select_mask_internal_operational_returns_executive():
    assert select_mask(tier="P3", context="internal_operational") == "executive"


def test_select_mask_default_is_diplomat():
    assert select_mask(tier="P4", context="external") == "diplomat"
