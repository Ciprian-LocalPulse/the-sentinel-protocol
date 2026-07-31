# Contributing

## Before You Start

Read [`docs/philosophy.md`](docs/philosophy.md) and
[`docs/design-principles.md`](docs/design-principles.md) first. Every
contribution is reviewed against those two documents specifically — a
technically correct change that reintroduces a fabricated-pretext or
covert-third-party-modeling pattern will not be merged, regardless of how
useful it seems in isolation.

## No Secret Prompts

Unlike the original whitepaper's confidential "God Prompt," every prompt
specification in this repository lives in [`prompts/`](prompts/), in the
open, versioned like code. If you're contributing a new prompt or editing
an existing one, add a changelog entry to the relevant file (see
`prompts/cortex.md` §Versioning for the format).

## Development Setup

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest tests/ -v
```

## Making a Change

1. **Docs change:** update the relevant file in `docs/`, and if it changes
   a formula or contract, update `reference/formulas.md` and the relevant
   JSON Schema in `schemas/` too — keep them in sync.
2. **Code change:** update `prototype/python/`, add/update tests in
   `tests/`, run `pytest tests/ -v` locally before opening a PR.
3. **Scoring-weight change:** per `reference/scoring.md`, include the
   recalibration data that motivated the change in your PR description.

## Pull Request Process

Use the template in `.github/PULL_REQUEST_TEMPLATE.md`. CI
(`.github/workflows/tests.yml`) must pass — tests and JSON Schema
validation.

## Code of Conduct

See [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md).
