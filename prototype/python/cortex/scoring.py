"""
Cortex — Scoring
Reference implementation for docs/cortex/scoring.md

Every score returns its contributing factors and a plain-language
explanation, per docs/design-principles.md #1 (explainability over
cleverness). No score is ever returned as a bare number.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone

from .ingestion import IngestedMessage

WEIGHTS = {"FC": 0.45, "EV": 0.25, "TD": 0.20, "SA": 0.10}

TIER_THRESHOLDS = [
    (8.5, "P1"),
    (6.5, "P2"),
    (3.5, "P3"),
    (1.5, "P4"),
    (0.0, "P5"),
]

MODEL_VERSION = "scoring-weights-v1.0"


@dataclass
class ScoredMessage:
    fingerprint: str
    priority_score: float
    tier: str
    factors: dict
    explanation: str
    scored_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    model_version: str = MODEL_VERSION


def analyze_sentiment(text: str) -> float:
    """Placeholder sentiment-magnitude estimator (0-10).

    In production this calls a real NLP sentiment/emotion model.
    Returns MAGNITUDE only — how strong the detected emotion is —
    never a covert psychological profile of the sender
    (see docs/cortex/scoring.md#sentiment-analysis).
    """
    strong_markers = ["urgent", "asap", "furious", "disappointed", "thrilled", "!"]
    hits = sum(text.lower().count(m) for m in strong_markers)
    return min(10.0, hits * 2.0)


def estimate_financial_clout(metadata: dict, crm_value: float | None = None) -> float:
    """Estimated deal/contract relevance. Uses CRM context if available,
    else a conservative default per docs/cortex/scoring.md."""
    if crm_value is not None:
        return min(10.0, crm_value / 10_000)
    return 3.0  # conservative default, not zero and not high


def time_decay_score(days_since_last_contact: float) -> float:
    return min(10.0, days_since_last_contact * 1.5)


def strategic_alignment_score(text: str, objectives: list[str]) -> float:
    if not objectives:
        return 5.0  # neutral default when no objectives configured
    text_lower = text.lower()
    hits = sum(1 for obj in objectives if obj.lower() in text_lower)
    return min(10.0, hits * (10.0 / max(1, len(objectives))))


def score_message(
    message: IngestedMessage,
    crm_value: float | None = None,
    days_since_last_contact: float = 0.0,
    objectives: list[str] | None = None,
) -> ScoredMessage:
    """Implements the PriorityScore formula from docs/cortex/scoring.md."""
    fc = estimate_financial_clout(message.metadata, crm_value)
    ev = analyze_sentiment(message.clean_text)
    td = time_decay_score(days_since_last_contact)
    sa = strategic_alignment_score(message.clean_text, objectives or [])

    priority_score = (
        fc * WEIGHTS["FC"] + ev * WEIGHTS["EV"] + td * WEIGHTS["TD"] + sa * WEIGHTS["SA"]
    )

    tier = next(t for threshold, t in TIER_THRESHOLDS if priority_score >= threshold)

    explanation = (
        f"Financial clout {fc:.1f}/10, emotional volatility {ev:.1f}/10, "
        f"time decay {td:.1f}/10, strategic alignment {sa:.1f}/10 "
        f"-> priority score {priority_score:.2f} ({tier})."
    )

    return ScoredMessage(
        fingerprint=message.fingerprint,
        priority_score=round(priority_score, 2),
        tier=tier,
        factors={"FC": round(fc, 2), "EV": round(ev, 2), "TD": round(td, 2), "SA": round(sa, 2)},
        explanation=explanation,
    )
