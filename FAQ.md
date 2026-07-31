# FAQ

**Is this the same as the whitepaper I bought/read?**
The five pillars and core mathematics (leverage score, priority score,
capacity score) are the same. A handful of specific mechanisms are
implemented differently — see [`docs/philosophy.md`](docs/philosophy.md)
for the exact list and the reasoning.

**Why were some things changed from the original document?**
Anything that fabricated information a real person (a client, a
colleague, a family member) would rely on as true was reframed to an
honest equivalent that serves the same underlying goal. Details in
`docs/philosophy.md`.

**Does this auto-send emails/messages on my behalf?**
No, not by default. Every draft goes through human review unless you
explicitly configure auto-send for a specific, low-risk context. See
`docs/design-principles.md` §2.

**Does this analyze other people's private data without their consent?**
It analyzes the sentiment/urgency of messages *sent to you*, to help you
prioritize your own attention — the same thing any inbox or CRM sentiment
feature does. It does not build persistent psychological profiles of
correspondents, and biometric monitoring is scoped exclusively to your
own data. See `docs/security/privacy.md`.

**Can I run this without sending my data to a third-party LLM provider?**
The architecture supports local model integration (`docs/deployment/local.md`);
whichever model you use, identifying data is tokenized before any
external API call (`docs/security/privacy.md`).

**Is the prototype production-ready?**
No — see `ROADMAP.md`. It's a reference implementation demonstrating the
architecture's core logic (scoring, leverage calculation, encryption),
with test coverage, but channel integrations (`docs/examples/`) and the
service API (`docs/api/`) are still specified, not yet built.

**Where's the original "God Prompt"?**
There isn't one, deliberately. Every prompt used by this system is
public and versioned in `prompts/` — see `CONTRIBUTING.md` §No Secret
Prompts.

**Can I use this commercially?**
The code and architecture are MIT-licensed (`LICENSE`). The whitepaper in
`papers/` remains separately attributed to its author.
