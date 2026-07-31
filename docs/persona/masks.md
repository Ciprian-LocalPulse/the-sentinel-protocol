# Persona — Masks

*Governs: `prompts/diplomat.md`, `prompts/executive.md`, `prompts/firewall.md`.
Consumes: message context + relationship type. Produces: a selected tone
preset for `mirror.md` to draft in.*

## Purpose

A single tone doesn't fit every context. Masks are tone/register presets
— they change *how* something is said, never *what is true* about it.

## The Three Masks

### Diplomat
- **Use for:** relationship maintenance, networking, early-stage
  conversations.
- **Characteristics:** open questions, validation, collaborative framing.
- **Prompt spec:** [`prompts/diplomat.md`](../../prompts/diplomat.md).

### Executive
- **Use for:** internal execution, deadlines, operational coordination.
- **Characteristics:** brief, structured (lists/bullets where natural),
  explicit call to action.
- **Prompt spec:** [`prompts/executive.md`](../../prompts/executive.md).

### Firewall
- **Use for:** boundary-setting, declining requests, holding a position in
  a difficult conversation.
- **Characteristics:** short, calm, references the actual constraint
  (capacity, policy, prior agreement) rather than manufactured urgency.
- **Prompt spec:** [`prompts/firewall.md`](../../prompts/firewall.md).

## Selection Logic

Mask selection is a function of the Cortex's scored context, not a random
or purely stylistic choice:

```python
def select_mask(scored_message, relationship_stage):
    if scored_message.tier in ("P1", "P2") and relationship_stage == "new":
        return "diplomat"
    if scored_message.context == "internal_operational":
        return "executive"
    if scored_message.detected_intent == "boundary_request":
        return "firewall"
    return "diplomat"  # safe default
```

Reference: [`prototype/python/persona/masks.py`](../../prototype/python/persona/masks.py).

## The One Rule That Applies to All Three Masks

A mask changes tone, never truth-value. The Firewall mask, in particular,
is explicitly specified to decline or hold a boundary using **real**
constraints — current capacity, actual policy, a prior commitment — never
a fabricated one. See [`philosophy.md`](../philosophy.md) for why this
line is enforced structurally rather than left to prompt discipline alone.
