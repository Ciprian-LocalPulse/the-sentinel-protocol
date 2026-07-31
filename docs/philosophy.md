# Philosophy & Design Ethics

## What This Document Is

The original Sentinel Protocol whitepaper describes five pillars: the
Cortex, the Neural Persona, the Energy Shield, the Ghost Negotiation
Matrix, and the Sovereign Path. This document restates that same
five-pillar structure as an actual engineering specification — and is
explicit about the handful of places where the engineering diverges from
the whitepaper's language, and why.

## The Core Idea, Kept Intact

Business communication carries emotional and contextual signal that
purely rule-based automation discards. A system that triages, drafts, and
schedules with awareness of urgency, sentiment, and the founder's own
cognitive capacity is a legitimate and valuable thing to build. Nothing in
this reframing weakens that premise.

## Where the Engineering Diverges From the Whitepaper, and Why

Three mechanisms in the original text are not included as specified,
because they are designed to alter a third party's beliefs about reality
in ways that party has not consented to — that is the definition of
deception, independent of how well-intentioned the deceiver is:

| Whitepaper mechanism | What it does | Reframed as |
|---|---|---|
| "Calendar Hijacking" — fake events shown to family/team | Creates false information in a shared calendar that others rely on to be true | **Do Not Disturb windows** — a real, visible status ("Focus block — will resume at HH:MM") that communicates the true state, not a fabricated one |
| "Punish toxic clients" via deliberately slower replies, framed as strategy | Uses response latency as a covert weapon against someone unaware they're being penalized | **Transparent SLA tiers** — response-time expectations that are the same, honestly, for everyone; a difficult conversation gets *more* deliberate handling, not a secret penalty |
| Ghost Follow-up: "I have withdrawn the resource allocation..." when nothing was withdrawn | A fabricated pretext used to manufacture urgency | **Evidence-based urgency signaling** — if a real deadline, real capacity constraint, or real competing demand exists, the system surfaces it; it never invents one |

Everything else in the five pillars — sentiment analysis, stylometric
voice-matching, biometric-aware workload management, negotiation-support
scoring, layered security — is kept, because none of it requires deceiving
a person who hasn't agreed to the interaction on those terms. Biometric
monitoring and stylometric cloning both operate on the founder's *own*
data, with the founder's own consent, which is a different ethical
category from covertly modeling and manipulating a counterparty.

## Why This Matters Technically, Not Just Ethically

A system built on fabricated pretexts is brittle in a way a system built
on real signal is not: the moment a client discovers the "withdrawn
allocation" was never real, every future message from the system loses
credibility — including the honest ones. Chapter IV's own closing section
(§4.10, "Ethics of Algorithmic Manipulation") already states the principle
this document enforces literally: *"Sentinel does not lie."* This
architecture makes that a property the code actually guarantees, not only
a stated intention.

## The Five Pillars, Restated as Engineering Scope

1. **The Cortex** (`docs/cortex/`) — ingestion, sentiment/urgency scoring,
   prioritization. See `emotional-cortex.md`, `ingestion.md`, `scoring.md`.
2. **The Neural Persona** (`docs/persona/`) — stylometric voice-matching,
   response drafting, tone adaptation. See `stylometry.md`, `mirror.md`,
   `masks.md`.
3. **The Energy Shield** (`docs/energy/`) — biometric-informed workload
   pacing, decision-fatigue tracking, for the founder's own data only. See
   `biometrics.md`, `decision-fatigue.md`.
4. **The Negotiation Intelligence Engine** (`docs/negotiation/`) —
   data-driven pricing and leverage scoring, transparent scarcity signaling
   only. See `algorithms.md`, `pricing.md`, `strategy.md`.
5. **The Sovereign Path** (`docs/security/`, `docs/deployment/`) — layered
   anonymization, local-first data sovereignty, self-hosting.

## A Note on the Whitepaper Itself

`papers/sentinel-whitepaper.pdf` is preserved as the original conceptual
document — the vision, in the author's own voice. It sits in `papers/`
specifically so it is clearly framed as the *pitch*, while `docs/` is the
*specification a developer implements*. Keeping both, clearly separated,
is more credible than either alone: readers can see the ambition and the
engineering discipline applied to it.
