"""
Energy Shield — Biometrics
Reference implementation for docs/energy/biometrics.md

Processes ONLY the founder's own, opt-in biometric stream.
Never models a third party. See docs/design-principles.md #4.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CapacityScore:
    value: float  # 0.0 - 1.0
    hrv_ratio: float
    sleep_score: float

    @property
    def is_depleted(self) -> bool:
        return self.value < 0.4


def calculate_capacity(
    hrv_current: float, baseline_hrv: float, sleep_score: float
) -> CapacityScore:
    """
    Deliberately conservative: penalizes low inputs more than it
    rewards high ones. See docs/energy/biometrics.md#capacity-score.

    sleep_score is expected on a 0-100 scale (as most wearable APIs
    report it, e.g. Oura's readiness/sleep score).
    """
    if baseline_hrv <= 0:
        raise ValueError("baseline_hrv must be a positive, calibrated value.")

    hrv_ratio = hrv_current / baseline_hrv
    capacity = hrv_ratio * (sleep_score / 100.0)
    capacity = max(0.0, min(1.0, capacity))

    return CapacityScore(value=round(capacity, 3), hrv_ratio=round(hrv_ratio, 3), sleep_score=sleep_score)
