# Developers — Contribution Guide (Deep Dive)

*Complements the top-level [`CONTRIBUTING.md`](../../CONTRIBUTING.md) with
more detail for engineering contributions specifically.*

## Architecture Change Process

1. Open an issue describing the change and which `docs/` file(s) it
   touches.
2. If it touches `docs/philosophy.md` or `docs/design-principles.md`,
   flag this explicitly in the issue — these require maintainer sign-off
   per `GOVERNANCE.md`.
3. Draft the doc change first, as a PR to the relevant `docs/*.md` file.
   Code follows the spec, not the other way around — this keeps `docs/`
   trustworthy as the source of truth referenced throughout the repo.
4. Implement in `prototype/python/`, with tests.
5. Update `schemas/` if the data contract changed.
6. Update `CHANGELOG.md`.

## Release Process

This project does not yet have a formal release cadence (see
`ROADMAP.md`). Until one exists:

- `CITATION.cff` version bumps when a meaningful, stable set of changes
  lands on `main`.
- Tag releases as `vX.Y.Z` following semver: breaking schema changes are
  major, new pillars/endpoints are minor, fixes are patch.

## Architecture Decision Records

See [`adr/`](adr/) for the log of significant, hard-to-reverse decisions
and their rationale — start there before proposing a change that
resembles a decision already made and recorded.
