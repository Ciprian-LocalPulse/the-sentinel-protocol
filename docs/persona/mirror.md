# Persona — The Mirror (Drafting)

*Governs: `prototype/python/persona/mirror.py`. Consumes: `ScoredMessage`
+ `StyleProfile` + selected `Mask`. Produces: a draft response, always
routed to human review before send.*

## Purpose

Generate a response draft that (a) addresses the incoming message
appropriately and (b) sounds like the founder wrote it, using the style
profile from `stylometry.md` and the tone preset from `masks.md`.

## Drafting Pipeline

```
ScoredMessage + StyleProfile + Mask
        │
        ▼
  Prompt assembly (prompts/diplomat.md / executive.md / firewall.md)
        │
        ▼
  LLM draft generation
        │
        ▼
  Voice-Consistency Check (§below)
        │
        ▼
  Fact-Check Pass (§below)
        │
        ▼
  Draft surfaced for founder review (never auto-sent by default —
  see design-principles.md §2)
```

## Voice-Consistency Check

Renamed from the whitepaper's "Turing Gate" (see `glossary.md`) — the
purpose is unchanged, the framing is corrected: this step measures
**style match**, not deception success. A second model call scores the
draft against the style profile:

> "On a scale of 1–10, how closely does this draft match the provided
> writing-style profile (sentence length, vocabulary, tone)?"

| Score | Action |
|---|---|
| < 6 | Regenerate with adjusted temperature/prompt |
| 6–8 | Flagged for founder review with a note ("style match: moderate") |
| > 8 | Presented as high-confidence match |

This score is a QA signal for the founder, never a claim used to
represent the draft as more human-authored than it is when the founder
reviews or sends it.

## Fact-Check Pass

Any date, figure, or name in the draft that came from retrieved context
(`prompts/cortex.md` §Context Retrieval) is checked against its source
before the draft is surfaced. If confidence is below 95%, the draft
includes an inline flag (`[VERIFY: claim not confirmed in source data]`)
rather than presenting an unverified claim as fact. This directly
implements the whitepaper's own "Hallucination Shield" principle
(§2.7 of the original document) — a genuinely good idea, kept as-is.

## Historical Context Injection

If the founder's CRM/notes contain relevant history (a prior meeting, an
open item), the draft may reference it — always sourced from the
founder's own records, and always fact-checked per above, never invented.
