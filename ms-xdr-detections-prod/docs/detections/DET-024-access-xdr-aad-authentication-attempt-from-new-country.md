# Access - XDR - DEX-024 - OOB - Authentication Attempt from New Country - Rule

**Audience:** Tier 1 SOC  
**Goal:** Fast triage, minimize false positives, escalate correctly.

## Why it matters
- Sign-in attempts from previously unseen countries can indicate credential stuffing or compromised accounts.

## Signals / When it triggers
- AAD interactive or non-interactive sign-in attempt from a country with no successful sign-ins in ~14 days.

## Tier‑1 triage workflow
1. Validate the user, device, and IP geo; check recent successful sign-ins.
2. Confirm travel/VPN use with the user or service owner.
3. Review MFA status and any concurrent risky sign-ins.

## What to collect for escalation
- UserPrincipalName, IP, Location, Result codes, DeviceId.

## Common false positives
- Corporate VPN egress changes; new cloud PoPs; legitimate travel.

## Implementation notes
- OOB coverage: DEX-001 OOB – Authentication Attempt from New Country (uses SigninLogs/AAD Non-Interactive).

_Last updated: 2025-08-13_

