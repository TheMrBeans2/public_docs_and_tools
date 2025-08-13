# Access - XDR - Successful AzureAD Login from Risk Country - Rule

**Audience:** Tier 1 SOC  
**Goal:** Fast triage, minimize false positives, escalate correctly.

## Why it matters
- Successful sign-in from high-risk country (policy defined).

## Signals / When it triggers
- SigninLogs: Result success + country in risk list
- Optionally: new country for the user

## Tier‑1 triage workflow
1. Validate travel/remote context; check MFA.
2. Review recent mailbox rules and OAuth consents.
3. Inspect session tokens/devices.

## What to collect for escalation
- Alert/Incident link
- Users/Devices/IPs/Message IDs
- Screenshots/log extracts

## Common false positives
- - VPN egress, roaming, CDNs

## Immediate response actions
- Revoke sessions; require password reset; block sign-in if compromise likely (Entra-Block-SignIn).

## Escalation criteria
- VIP/sensitive data involved
- Malware confirmed or active exfiltration
- Unclear attribution or repeated recurrence

_Last updated: 2025-08-12_
