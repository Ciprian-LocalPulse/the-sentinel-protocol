from prototype.python.cortex.ingestion import IngestedMessage
from prototype.python.cortex.scoring import (
    analyze_sentiment,
    score_message,
    strategic_alignment_score,
    time_decay_score,
)


def make_message(text="Hello", metadata=None):
    return IngestedMessage(clean_text=text, fingerprint="a" * 64, metadata=metadata or {})


def test_analyze_sentiment_higher_for_strong_markers():
    calm = analyze_sentiment("Let's meet next week to review.")
    urgent = analyze_sentiment("This is URGENT!! Need this ASAP, I'm furious!")
    assert urgent > calm


def test_analyze_sentiment_capped_at_ten():
    text = "urgent " * 20
    assert analyze_sentiment(text) <= 10.0


def test_time_decay_scales_with_days():
    assert time_decay_score(0) == 0.0
    assert time_decay_score(5) == 7.5
    assert time_decay_score(100) == 10.0  # capped


def test_strategic_alignment_neutral_without_objectives():
    assert strategic_alignment_score("anything", []) == 5.0


def test_strategic_alignment_scores_matching_objectives():
    score = strategic_alignment_score(
        "We should discuss the Q3 roadmap and scaling plan.",
        ["roadmap", "scaling"],
    )
    assert score == 10.0


def test_score_message_returns_explainable_output():
    msg = make_message("This is urgent, need this ASAP!")
    scored = score_message(msg, crm_value=50_000, days_since_last_contact=2)
    assert scored.fingerprint == msg.fingerprint
    assert 0 <= scored.priority_score <= 10
    assert scored.tier in ("P1", "P2", "P3", "P4", "P5")
    assert set(scored.factors.keys()) == {"FC", "EV", "TD", "SA"}
    assert "priority score" in scored.explanation.lower()


def test_score_message_high_value_deal_scores_higher_tier():
    msg = make_message("This is urgent, need this ASAP! Furious about delays!")
    scored = score_message(msg, crm_value=200_000, days_since_last_contact=10)
    assert scored.tier in ("P1", "P2")
