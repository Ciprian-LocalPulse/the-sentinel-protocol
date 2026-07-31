# Reference — Formulas

## Priority Score (Cortex)

```
PriorityScore = (FC × 0.45) + (EV × 0.25) + (TD × 0.20) + (SA × 0.10)
```
See [`docs/cortex/scoring.md`](../docs/cortex/scoring.md). Implementation:
[`prototype/python/cortex/scoring.py`](../prototype/python/cortex/scoring.py).

**Worked example:** FC=8, EV=6, TD=3, SA=5
→ (8×0.45)+(6×0.25)+(3×0.20)+(5×0.10) = 3.6+1.5+0.6+0.5 = **6.2 → P3**
(just under the P2 threshold of 6.5 — illustrates why explanations matter:
a small factor shift changes the tier).

## Capacity Score (Energy Shield)

```
Capacity = (HRV_current / HRV_baseline) × (SleepScore / 100)
```
See [`docs/energy/biometrics.md`](../docs/energy/biometrics.md).

**Worked example:** HRV_current=52, HRV_baseline=65, SleepScore=80
→ (52/65) × (80/100) = 0.8 × 0.8 = **0.64** (moderate capacity)

## Decision Fatigue Score (Energy Shield)

```
DFS = (InputToxicity × 1.5) + (SwitchingCost × 0.8) + (CognitiveLoad × 2.0)
```
See [`docs/energy/decision-fatigue.md`](../docs/energy/decision-fatigue.md).
Focus Mode triggers when `DFS > 85`.

## Leverage Score (Negotiation)

```
Lv = (Urgency × Uniqueness) / (SubstituteCount × TimeBuffer)
```
See [`docs/negotiation/algorithms.md`](../docs/negotiation/algorithms.md).

**Worked example:** Urgency=7, Uniqueness=8, SubstituteCount=2, TimeBuffer=5
→ (7×8) / (2×5) = 56/10 = **5.6** (leverage > 2.5 → premium pricing path)

## Recalibration

Per [`docs/design-principles.md`](../docs/design-principles.md) §6, weight
changes to any formula above are versioned (`model_version` field in
`schemas/analysis.schema.json`) and reviewed monthly against logged
outcomes — see [`scoring.md`](scoring.md) §Recalibration.
