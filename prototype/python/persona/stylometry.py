"""
Persona — Stylometry
Reference implementation for docs/persona/stylometry.md

Builds a StyleProfile from the founder's OWN opt-in corpus only.
See docs/persona/stylometry.md#consent-and-data-handling.
"""
from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass, field
from datetime import datetime, timezone

STOPWORDS = {
    "the", "a", "an", "and", "or", "but", "to", "of", "in", "on", "for",
    "is", "are", "was", "were", "be", "i", "you", "we", "it", "that",
}


@dataclass
class StyleProfile:
    profile_id: str
    owner_consent: bool
    avg_sentence_length: float
    punctuation_profile: dict
    pos_distribution: dict
    top_keywords: list
    corpus_category: str = "golden_sentences"
    built_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def __post_init__(self):
        if not self.owner_consent:
            raise ValueError(
                "StyleProfile cannot be built without explicit owner consent. "
                "See docs/persona/stylometry.md#consent-and-data-handling."
            )


def _split_sentences(text: str) -> list[str]:
    return [s.strip() for s in re.split(r"[.!?]+", text) if s.strip()]


def _tokenize(text: str) -> list[str]:
    return re.findall(r"[A-Za-z']+", text.lower())


def build_style_profile(
    profile_id: str,
    corpus: list[str],
    owner_consent: bool,
    corpus_category: str = "golden_sentences",
) -> StyleProfile:
    """Note: this is a lightweight, dependency-free reference
    implementation. A production build would use a full NLP pipeline
    (e.g., spaCy) for POS tagging, per docs/persona/stylometry.md."""
    if not owner_consent:
        raise ValueError("Cannot build a style profile without owner consent.")

    full_text = " ".join(corpus)
    sentences = _split_sentences(full_text)
    avg_len = (
        sum(len(_tokenize(s)) for s in sentences) / len(sentences) if sentences else 0.0
    )

    punctuation_profile = {
        "!": full_text.count("!"),
        "?": full_text.count("?"),
        "—": full_text.count("—"),
        "...": full_text.count("..."),
    }

    tokens = _tokenize(full_text)
    keyword_candidates = [t for t in tokens if t not in STOPWORDS and len(t) > 2]
    top_keywords = Counter(keyword_candidates).most_common(20)

    # Lightweight POS approximation without a full tagger dependency.
    pos_distribution = {
        "long_words_ratio": round(
            sum(1 for t in tokens if len(t) > 6) / len(tokens), 3
        ) if tokens else 0.0,
    }

    return StyleProfile(
        profile_id=profile_id,
        owner_consent=owner_consent,
        avg_sentence_length=round(avg_len, 2),
        punctuation_profile=punctuation_profile,
        pos_distribution=pos_distribution,
        top_keywords=top_keywords,
        corpus_category=corpus_category,
    )
