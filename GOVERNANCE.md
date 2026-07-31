# Governance

## Maintainership

The Sentinel Protocol is currently maintained by its original author,
Ciprian Ștefan Pleșca (Stefano D'angelo). Architectural decisions that
touch [`docs/philosophy.md`](docs/philosophy.md) or
[`docs/design-principles.md`](docs/design-principles.md) require
maintainer sign-off; other documentation and prototype contributions
follow the standard review process in
[`CONTRIBUTING.md`](CONTRIBUTING.md).

## Decision Scope

| Decision type | Who decides |
|---|---|
| New feature / pillar extension | Maintainer, informed by community proposals via Issues |
| Bug fixes, test additions | Any contributor, standard PR review |
| Changes to `docs/philosophy.md` ethical boundaries | Maintainer only, with public rationale in the PR |
| Scoring-weight recalibration | Maintainer, per the process in `reference/scoring.md` |

## Why the Ethical Boundaries in `philosophy.md` Are Not Up for a Simple
## Majority Vote

The specific reframing decisions documented in `philosophy.md` (no
fabricated calendar events, no fabricated negotiation pretexts, no
third-party psychological profiling for manipulation) are treated as a
project invariant, not a configurable preference — consistent with how
they're enforced structurally in the code (`docs/design-principles.md`),
not just described in prose. A PR proposing to relax one of these is
welcome as a discussion, but will not be merged as a silent or
majority-vote change.

## Path to Broader Governance

As the contributor base grows, this document will be revisited to
introduce a steering structure — this is intentionally a living document,
not a final one.
