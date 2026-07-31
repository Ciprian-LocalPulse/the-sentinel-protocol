# Security — Threat Model

*Governs the security posture of every component in `docs/`. Cross-
referenced by `architecture.md` §5 (Trust Boundaries).*

## Assets to Protect

| Asset | Why it matters |
|---|---|
| Founder's raw communications (email/Slack content) | Highest-sensitivity business data |
| Founder's biometric stream | Health data, sensitive by definition |
| Style profile (`persona/stylometry.md`) | If exfiltrated, could be used to impersonate the founder convincingly |
| Negotiation context (deal values, deadlines) | Commercially sensitive |
| API credentials (LLM providers, wearable APIs, email/calendar) | Compromise here compromises everything above |

## Threat Actors

| Actor | Motivation | Relevant mitigations |
|---|---|---|
| External attacker (network-level) | Data theft, extortion | Encryption at rest/in transit (`encryption.md`), local-first storage |
| Malicious/compromised third-party API (LLM provider breach) | Exposure of anonymized payloads | Anonymization layer (`privacy.md`) — even a full provider breach exposes only tokenized data |
| Insider (if system is used by a team) | Unauthorized access to founder's data | Role-based access on the Sovereign Dashboard (§Deployment) |
| Social engineering against the founder | Credential theft | Standard MFA guidance, out of this repo's scope but referenced |

## Key Risks and Mitigations

1. **Style-profile exfiltration → impersonation risk.** Mitigation: the
   style profile is encrypted at rest, and no drafting request is served
   without founder authentication (`deployment/local.md`).
2. **Biometric data breach.** Mitigation: local-only storage, 30-day
   auto-purge (`energy/biometrics.md`), only derived scores (not raw
   series) ever leave the local environment.
3. **LLM prompt injection via a malicious inbound message.** An attacker
   could craft an email designed to manipulate the drafting model into
   ignoring its instructions. Mitigation: ingestion (`cortex/ingestion.md`)
   sanitizes and clearly delimits untrusted content before it reaches any
   prompt (`prompts/cortex.md` §Input Handling); the model is instructed to
   treat message content as data, never as instructions.
4. **Over-trusting AI-drafted content as fact.** Mitigation: the Fact-Check
   Pass (`persona/mirror.md`) and mandatory human review gate
   (`design-principles.md` §2).

## Out of Scope

Physical security of the founder's devices, and security of third-party
platforms (Gmail, Slack) themselves — this project secures what it
controls: the data it processes and stores locally.
