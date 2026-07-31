# Developers — Coding Standards

## Python

- Python 3.11+, type hints on all public functions.
- `dataclasses` for structured return values (see any module in
  `prototype/python/` for the pattern) — every score/result object is a
  typed dataclass, never a bare dict, so IDEs and reviewers can see the
  contract.
- No bare `except:` — catch specific exceptions.
- Every module that implements a `docs/*.md` spec has a docstring
  referencing that doc, e.g. `"""Reference implementation for
  docs/cortex/scoring.md"""`. Keep this pointer accurate when either
  side changes.

## Explainability (see `docs/design-principles.md` #1)

Any function that returns a score MUST return the contributing factors
alongside it. This is enforced by convention and by the JSON Schemas in
`schemas/` (e.g. `analysis.schema.json` requires `factors` and
`explanation` as mandatory fields, not optional).

## Testing

- Every new function in `prototype/python/` gets at least one test in
  `tests/`.
- Tests should assert behavior *and*, where the module implements a
  `docs/philosophy.md` boundary, explicitly assert the boundary holds —
  see `tests/test_energy.py::test_focus_block_label_is_honest` and
  `tests/test_api.py::test_negotiation_offer_no_fabricated_scarcity` for
  the pattern: don't just test the happy path, test that the system
  refuses to fabricate.

## Prompts (`prompts/`)

- Every prompt spec file has a `Version:` header and a changelog table
  at the bottom (see `prompts/cortex.md` for the format).
- A prompt change that alters model behavior in a way that could affect
  scoring/drafting output requires a version bump and a note in
  `CHANGELOG.md`.

## Documentation

- Every `docs/*.md` file that specifies a data contract should link to
  its JSON Schema (`schemas/`) and to its reference implementation
  (`prototype/python/`) — the three should never drift out of sync
  silently. If you change one, check the other two.
- Follow the "Status:" convention at the top of normative docs
  (`OPERATIONAL` / `PLANNED` / `FUTURE`, or "Reference implementation
  available at...") so a reader always knows what's real today.

## Commit Messages

Short imperative summary line, then (if non-obvious) a short body
explaining *why*, not just *what* — especially for anything touching
`docs/philosophy.md` boundaries, where the "why" is the whole point.
