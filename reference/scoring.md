# Reference — Scoring Recalibration

*Extends [`docs/cortex/emotional-cortex.md`](../docs/cortex/emotional-cortex.md)
§Maintenance with the concrete monthly procedure.*

## Monthly Recalibration Checklist

1. **False-positive rate on P1.** Pull all messages scored P1 in the
   audit log (`docs/security/privacy.md`). For each, check whether the
   founder actually treated it as critical (fast response, escalation) or
   not. A false-positive rate above 15% triggers a weight review.
2. **Missed-urgency rate.** Pull messages the founder manually flagged as
   urgent that the Cortex scored P3 or below. A rate above 10% triggers a
   weight review.
3. **Style-match drift (Persona).** Sample 5 recent founder-authored
   messages; compare against the current `StyleProfile`
   (`schemas/persona.schema.json`). If style-match scores
   (`prompts/verifier.md`) trend downward, rebuild the profile with the
   new samples included.
4. **Leverage-score outcome check (Negotiation).** For closed deals,
   compare the leverage-score-suggested price multiplier against the
   actually negotiated outcome. Large, consistent deviations suggest a
   weight adjustment, not a one-off exception.

## Weight Adjustment Process

A weight change is a versioned, reviewable pull request against
`prototype/python/cortex/scoring.py::WEIGHTS` (or the equivalent constant
in the relevant module), with the recalibration data that motivated it
linked in the PR description — never a silent, undocumented tuning
change, per [`docs/design-principles.md`](../docs/design-principles.md) §6.
