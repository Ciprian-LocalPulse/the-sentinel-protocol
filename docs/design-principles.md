# Design Principles

These are the rules every pull request is reviewed against. If a change
violates one of these, it doesn't merge, regardless of how useful it seems
in isolation.

## 1. Explainability over cleverness
Every score, classification, or suggestion must return *why*, not just
*what*. `{"priority": "high"}` is not an acceptable output; `{"priority":
"high", "factors": {"urgency": 0.8, "sender_weight": 0.6}}` is.

## 2. The founder approves; nothing auto-sends by default
Auto-send is an opt-in configuration a user explicitly enables per
channel/context, never the default. See [`reference/terminology.md`](reference/terminology.md)
for the distinction between "draft" and "send" actions throughout the docs.

## 3. No fabricated facts, ever
No component generates a false pretext, a fake calendar entry, or an
invented deadline to influence anyone's behavior — counterparty or the
founder's own household/team. See [`philosophy.md`](philosophy.md).

## 4. Own-data-only for biometric and cognitive inference
The Energy Shield never models a third party's psychological or physical
state. It only ever processes the founder's own, explicitly-consented
biometric stream.

## 5. Anonymize before you leave the boundary
Any payload sent to an external LLM API is tokenized first
(`security/encryption.md`). Identifying data is decoded only inside the
founder's local environment.

## 6. Everything is versioned, nothing is silently swapped
Model versions, prompt versions, and scoring-weight changes are tracked
(`prompts/` uses semantic versioning headers) — a scoring change that
shifts what counts as "urgent" is a reviewable change, not a silent drift.

## 7. Simple first, elastic later
The reference prototype (`prototype/`) starts with the simplest working
version of each pillar (rule-based + a single LLM call) before adding
orchestration complexity. See `docs/deployment/local.md` for the
recommended starting setup.

## 8. Every claim about accuracy is measured, not asserted
If a document states a model's precision, recall, or false-positive rate,
it must reference an actual evaluation run (`tests/`), not an estimate.
Until such an evaluation exists, documents say "target" or "design
assumption," not a measured number.
