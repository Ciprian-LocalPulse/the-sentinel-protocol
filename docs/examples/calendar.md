# Integration Example — Calendar

*Status: Planned. Shows how Focus Mode (`docs/energy/decision-fatigue.md`)
interacts with a real calendar API — and specifically how it differs from
the whitepaper's original mechanism.*

## Honest Focus-Block Creation

```python
from prototype.python.energy.fatigue import calculate_dfs, build_focus_block_label

def maybe_create_focus_block(calendar_client, input_toxicity, switching_cost, cognitive_load, until_time):
    fatigue = calculate_dfs(input_toxicity, switching_cost, cognitive_load)
    if not fatigue.focus_mode_triggered:
        return None

    label = build_focus_block_label(until_time)
    # Creates a REAL, accurately-labeled calendar event — never a
    # fabricated "meeting". See docs/energy/decision-fatigue.md.
    event = calendar_client.create_event(
        title=label,
        start=now(),
        end=until_time,
        visibility="busy",
    )
    return event
```

## What This Deliberately Does Not Do

It never creates an event titled to imply a fake external meeting
("Strategic Alignment Call," "Client Sync") when no such thing is
happening. Anyone viewing the founder's calendar sees an honest label —
see `docs/philosophy.md` for why this line is enforced structurally.

## Required Calendar OAuth Scopes

`calendar.events` (read/write, for the Focus Mode block only) —
`calendar.readonly` alone is sufficient for the capacity-check use case
if focus-block creation is disabled.
