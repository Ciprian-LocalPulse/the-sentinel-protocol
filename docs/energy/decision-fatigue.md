# Energy Shield — Decision Fatigue

*Governs: `prototype/python/energy/fatigue.py`. Consumes: capacity score
(`biometrics.md`) + interaction history from the current day. Produces: a
`FatigueScore` that gates how/when messages are surfaced.*

## The Decision Fatigue Score (DFS)

```
DFS = (InputToxicity × 1.5) + (SwitchingCost × 0.8) + (CognitiveLoad × 2.0)
```

| Variable | Meaning | Source |
|---|---|---|
| `InputToxicity` | Volume-weighted negative-sentiment load processed today | Cortex sentiment scores (`cortex/scoring.md`), aggregated |
| `SwitchingCost` | Count of context switches between channels/apps today | Local activity tracking, opt-in |
| `CognitiveLoad` | Linguistic complexity of tasks/messages handled today | Computed from response length/complexity |

When `DFS > 85`, the system enters **Focus Mode** (§below).

## Focus Mode

Renamed from the whitepaper's "Ghost Protocol" — same trigger condition,
honest mechanism (see `philosophy.md` for the specific change):

| Whitepaper mechanism | Focus Mode equivalent |
|---|---|
| Fake calendar events shown to others as real meetings | A visible **"Focus block"** calendar entry — labeled accurately, viewable by anyone who could see the calendar anyway |
| Silent downgrade of notification priority | Notification batching, disclosed in the founder's own settings — nothing hidden from the founder about what's being deferred |
| Delaying the founder's own outgoing messages for a "cold review" | Kept as-is — this one doesn't deceive anyone; it's a personal-review buffer the founder benefits from and controls |

## Why the Calendar-Entry Change Matters

A calendar entry other people rely on to plan around you is a shared
communication channel, not a private setting. Labeling a block "Focus
block — heads-down until 3pm" protects the same time without anyone
downstream making decisions based on false information (e.g., a colleague
believing you're in an external meeting when you're not, and adjusting
their own plans around a fabricated constraint).

## Burnout Prediction (Long-Horizon)

Using 90 days of capacity-score history, the system can surface a
correlational observation to the founder — for example, a pattern between
call volume and subsequent capacity drops — as a **suggestion**, never an
automated schedule override. The founder decides what to do with the
pattern; the system's role stops at surfacing it clearly, with the
underlying data available for the founder to verify.
