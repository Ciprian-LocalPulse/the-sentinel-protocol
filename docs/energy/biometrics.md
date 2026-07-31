# Energy Shield — Biometrics

*Governs: `prototype/python/energy/biometrics.py`. Consumes: founder's own
wearable data (opt-in). Produces: a `CapacityScore` used by
`decision-fatigue.md` and the drafting pipeline (`persona/mirror.md`).*

## Purpose

Treat the founder's own cognitive capacity as a real, monitorable
resource — the same way infrastructure monitors uptime — and let the
system pace itself accordingly, rather than surfacing every message the
instant it arrives regardless of whether this is a good moment.

## Scope Boundary (Important)

This module processes **only the founder's own, explicitly-consented
biometric stream.** It never infers or models a third party's physiological
or psychological state. This is a hard boundary, not a configuration
option — see [`design-principles.md`](../design-principles.md) §4.

## Signals

| Signal | Source | What it indicates |
|---|---|---|
| HRV (Heart Rate Variability) | Oura / Garmin / Apple Watch / Whoop API | Autonomic stress load — low HRV correlates with reduced decision quality |
| RHR (Resting Heart Rate) | Same | Elevated RHR can indicate fatigue or oncoming illness |
| Sleep architecture | Same | Deep vs. REM ratio — physical vs. cognitive recovery |
| Interaction patterns | Local (typing cadence, correction rate) | A behavioral proxy when wearable data isn't available |

## Capacity Score

```python
def calculate_capacity(hrv_current, baseline_hrv, sleep_score):
    """
    Returns a 0-1 capacity estimate.
    Deliberately conservative: penalizes low inputs more than it
    rewards high ones, since the cost of surfacing something to a
    depleted founder is higher than the cost of a slightly delayed
    non-urgent message.
    """
    capacity = (hrv_current / baseline_hrv) * (sleep_score / 100)
    return max(0.0, min(1.0, capacity))
```

Reference: [`prototype/python/energy/biometrics.py`](../../prototype/python/energy/biometrics.py).

## Data Handling

- **Local-only storage.** Raw biometric time series never leaves the local
  environment; only the derived capacity score (a single float) is used
  by other components (`security/encryption.md`).
- **Auto-purge.** Detailed biometric history older than 30 days is deleted
  by default, configurable but never disabled by default — this limits the
  damage of a potential breach without requiring the founder to remember
  to do it manually.
- **Opt-in, revocable.** Biometric integration is off by default; enabling
  it is a deliberate action, and disabling it purges the stored history.
