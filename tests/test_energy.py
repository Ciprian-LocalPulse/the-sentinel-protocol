import pytest

from prototype.python.energy.biometrics import calculate_capacity
from prototype.python.energy.fatigue import build_focus_block_label, calculate_dfs


def test_calculate_capacity_basic():
    capacity = calculate_capacity(hrv_current=52, baseline_hrv=65, sleep_score=80)
    assert capacity.value == 0.64
    assert not capacity.is_depleted


def test_calculate_capacity_flags_depleted():
    capacity = calculate_capacity(hrv_current=20, baseline_hrv=65, sleep_score=40)
    assert capacity.is_depleted


def test_calculate_capacity_rejects_invalid_baseline():
    with pytest.raises(ValueError):
        calculate_capacity(hrv_current=50, baseline_hrv=0, sleep_score=80)


def test_calculate_capacity_clamped_to_one():
    capacity = calculate_capacity(hrv_current=200, baseline_hrv=65, sleep_score=100)
    assert capacity.value == 1.0


def test_calculate_dfs_triggers_focus_mode_above_threshold():
    fatigue = calculate_dfs(input_toxicity=20, switching_cost=10, cognitive_load=20)
    # (20*1.5) + (10*0.8) + (20*2.0) = 30 + 8 + 40 = 78 -> below threshold
    assert not fatigue.focus_mode_triggered

    fatigue_high = calculate_dfs(input_toxicity=30, switching_cost=15, cognitive_load=25)
    # (30*1.5) + (15*0.8) + (25*2.0) = 45 + 12 + 50 = 107 -> above threshold
    assert fatigue_high.focus_mode_triggered


def test_focus_block_label_is_honest():
    label = build_focus_block_label("3:00 PM")
    assert label == "Focus block — heads-down until 3:00 PM"
    # Explicitly assert it does NOT fabricate a fake meeting title
    assert "Strategic Alignment" not in label
    assert "Client" not in label
