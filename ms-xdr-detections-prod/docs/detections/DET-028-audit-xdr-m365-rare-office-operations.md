# Audit - XDR - DEX-028 - OOB - Rare Office Operations - Rule

**Audience:** Tier 1 SOC  
**Goal:** Fast triage, minimize false positives, escalate correctly.

## Why it matters
- Rare M365 administrative operations can provide persistence or enable exfiltration if abused.

## Signals / When it triggers
- OfficeActivity records uncommon admin operations (e.g., Set-Mailbox, New/Set-InboxRule, Set-TransportRule).

## Tier‑1 triage workflow
1. Verify operator identity and change window.
2. Review operation context and intended outcome.
3. Roll back or restrict permissions if unauthorized.

## What to collect for escalation
- UserId, AppId, operation, parameters, IP.

## Common false positives
- Approved maintenance windows or automation accounts.

## Implementation notes
- OOB coverage: DEX-007 OOB – RareOfficeOperations (Microsoft 365 solution).

_Last updated: 2025-08-13_

