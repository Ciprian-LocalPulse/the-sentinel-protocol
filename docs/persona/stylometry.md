# Persona — Stylometry

*Governs: `prototype/python/persona/stylometry.py`. Consumes: the
founder's own historical outbound messages (opt-in corpus). Produces: a
`StyleProfile` used by `mirror.md` for drafting.*

## Purpose

Extract a quantifiable model of the founder's own writing style, so
drafted responses feel consistent rather than generically "AI-written."
This operates exclusively on the founder's own authored text — never on a
third party's writing.

## What Gets Measured

| Feature | Method | Why it matters |
|---|---|---|
| Average sentence length | Tokenization + sentence segmentation | Short-and-punchy vs. discursive style |
| Punctuation profile | Frequency of `!`, `?`, `—`, `...` | Formality and energy signals |
| Part-of-speech distribution | POS tagging (spaCy or equivalent) | Noun-heavy vs. verb-heavy phrasing |
| Power words / recurring vocabulary | Lemma frequency, stopwords excluded | The founder's actual recurring terms, not a generic thesaurus |
| Greeting/sign-off patterns | Pattern extraction from corpus | Consistency in how messages open/close |

## Reference Implementation

See [`prototype/python/persona/stylometry.py`](../../prototype/python/persona/stylometry.py),
function `build_style_profile(corpus: list[str]) -> StyleProfile`.

## Training Corpus Guidance

The whitepaper's "Identity Corpus" concept is preserved: build the profile
from a deliberately varied sample —

1. **Best examples** — messages that achieved their goal (a close, a
   resolved conflict, a successful ask).
2. **Firm/boundary-setting examples** — how the founder writes when saying
   no or ending something.
3. **Casual/internal examples** — team-facing tone, distinct from
   external-facing tone.

Each category is tagged in `schemas/persona.schema.json` so drafting
(`mirror.md`) can select the right sub-profile for the right mask
(`masks.md`).

## Consent and Data Handling

The corpus is the founder's own authored content, provided with explicit
opt-in. It is never built from a third party's messages — cloning a
third party's writing style without consent is out of scope for this
project entirely, not just discouraged.
