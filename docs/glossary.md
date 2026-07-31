# Glossary

| Term | Definition |
|---|---|
| **Cortex** | The ingestion + scoring pipeline that turns a raw message into a prioritized, structured event. |
| **Fingerprint** | A SHA-256 hash of a sanitized message body, used to deduplicate and track conversation threads. |
| **Priority Tier** | One of five levels (P1–P5) a scored message is assigned to; replaces the whitepaper's "DEFCON" naming (kept functionally identical, renamed to avoid military-crisis framing for what is, functionally, an inbox triage label). |
| **Persona / Mirror** | The stylometric model of the founder's own writing, used to draft responses that match their voice. |
| **Mask** | A tone/register preset (Diplomat, Executive, Firewall) selected based on context, applied to drafting — never used to misrepresent facts. |
| **Turing Gate → Voice-Consistency Check** | The verification step that scores whether a drafted message matches the founder's established voice, renamed from "Turing Gate" to describe what it actually measures (style match, not deception success). |
| **Energy Shield** | The subsystem that paces workload against the founder's own biometric/cognitive capacity signals. |
| **Capacity Score** | A 0–1 value representing estimated current decision-making capacity, derived from HRV, sleep, and interaction patterns. |
| **Negotiation Intelligence** | Data-driven pricing/leverage suggestions based on real market and deal signals — renamed from "Ghost Negotiation Matrix" to remove the deception framing; the underlying leverage math is preserved. |
| **Leverage Score (Lv)** | See [`reference/formulas.md`](../reference/formulas.md) — a weighted score of urgency, uniqueness, substitute availability, and time pressure. |
| **Iron Vault** | The local, encrypted storage layer; see [`security/encryption.md`](security/encryption.md). |
| **Anonymization Layer** | The tokenization step that strips identifying data (names, amounts, locations) before any payload reaches an external model API. |
| **Audit Log** | The append-only record of every scored event, drafted message, and capacity check — the accountability backbone (§Security). |
