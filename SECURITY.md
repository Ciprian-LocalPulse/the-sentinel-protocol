# Security Policy

## Reporting a Vulnerability

If you find a security issue in this repository (in the reference
prototype, prompt specifications, or the deployment guidance), please
report it privately rather than opening a public issue. Contact the
maintainer directly via GitHub.

Please include:
- Which component is affected (`prototype/python/...` file, or a
  specific `docs/` guidance you believe is unsafe as specified)
- Steps to reproduce, if applicable
- Potential impact

## Scope

This covers:
- The reference prototype code (`prototype/python/`)
- The security architecture as documented (`docs/security/`)
- The prompt specifications (`prompts/`), specifically around prompt-
  injection resistance (`docs/security/threat-model.md` §3)

It does not cover third-party services this project integrates with
(Gmail, Slack, wearable APIs, LLM providers) — report those issues to the
respective provider.

## Our Commitment

Reported vulnerabilities will be acknowledged, and a fix or mitigation
plan will be shared before any public disclosure, consistent with
standard responsible-disclosure practice.

## Design-Level Security Reference

For the architecture-level threat model (not a vulnerability report, but
background), see [`docs/security/threat-model.md`](docs/security/threat-model.md).
