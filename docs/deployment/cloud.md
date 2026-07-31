# Deployment — Cloud

*Status: Future (`ROADMAP.md`). Sketches the multi-user/team deployment
model — not required for single-founder use.*

## When This Applies

Only relevant once the Sentinel Protocol is scaled to support an
executive's whole team (`docs/persona/mirror.md`'s sub-mask concept for
delegated drafting), not for a single founder running the local setup.

## Target Shape

- Managed container hosting (any provider) running the API service
  (`docs/api/`) from `docker.md`.
- Per-user Iron Vault instances — **never** a shared encryption key
  across users; each founder/team-member's data is isolated
  (`docs/security/threat-model.md` — insider-risk mitigation).
- Wearable and email/calendar API credentials stored in a managed secrets
  service, not environment variables, at this scale.

## Explicit Non-Goal

This is not designed to become a data-sharing platform across
organizations. Each deployment serves one founder/team's own data, full
stop — consistent with the local-first principle carried through from the
single-user setup.
