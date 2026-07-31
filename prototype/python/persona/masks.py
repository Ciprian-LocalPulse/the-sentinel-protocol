"""
Persona — Mask Selection
Reference implementation for docs/persona/masks.md

A mask changes tone only, never truth-value. See docs/philosophy.md.
"""
from __future__ import annotations

from typing import Literal

Mask = Literal["diplomat", "executive", "firewall"]


def select_mask(
    tier: str,
    relationship_stage: str = "established",
    context: str = "external",
    detected_intent: str | None = None,
) -> Mask:
    """Deterministic mask-selection logic per docs/persona/masks.md.

    tier: priority tier from Cortex scoring (P1-P5)
    relationship_stage: "new" | "established"
    context: "internal_operational" | "external"
    detected_intent: e.g. "boundary_request", or None
    """
    if detected_intent == "boundary_request":
        return "firewall"
    if context == "internal_operational":
        return "executive"
    if tier in ("P1", "P2") and relationship_stage == "new":
        return "diplomat"
    return "diplomat"  # safe default, see docs/persona/masks.md#selection-logic


MASK_PROMPT_FILES = {
    "diplomat": "prompts/diplomat.md",
    "executive": "prompts/executive.md",
    "firewall": "prompts/firewall.md",
}
