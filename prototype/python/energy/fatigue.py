"""
Energy Shield — Decision Fatigue
Reference implementation for docs/energy/decision-fatigue.md
"""
from __future__ import annotations

from dataclasses import dataclass

FATIGUE_THRESHOLD = 85.0


@dataclass
class FatigueScore:
    value: float
    focus_mode_triggered: bool


def calculate_dfs(input_toxicity: float, switching_cost: float, cognitive_load: float) -> FatigueScore:
    """DFS = (InputToxicity x 1.5) + (SwitchingCost x 0.8) + (CognitiveLoad x 2.0)
    See docs/energy/decision-fatigue.md#the-decision-fatigue-score-dfs."""
    dfs = (input_toxicity * 1.5) + (switching_cost * 0.8) + (cognitive_load * 2.0)
    return FatigueScore(value=round(dfs, 2), focus_mode_triggered=dfs > FATIGUE_THRESHOLD)


def build_focus_block_label(until_time: str) -> str:
    """Honest calendar-block label. See docs/energy/decision-fatigue.md
    for why this replaces the whitepaper's fabricated-event mechanism.

    Never generates a false meeting title — always a transparent,
    accurately-labeled focus block.
    """
    return f"Focus block — heads-down until {until_time}"
