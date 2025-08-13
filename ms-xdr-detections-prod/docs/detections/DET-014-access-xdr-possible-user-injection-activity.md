# Access - XDR - Possible User Injection Activity - Rule

**Audience:** Tier 1 SOC  
**Goal:** Fast triage, minimize false positives, escalate correctly.

## Why it matters
- Mailbox rule/OAuth grant shortly after sign-in from new location (AiTM/session theft).

## Signals / When it triggers
- SigninLogs new country for user + OfficeActivity New/Set-InboxRule with forward/redirect

## Tier‑1 triage workflow
1. Verify with user; check MFA prompts.
2. Remove rules; check OAuth grants and token activity.

## What to collect for escalation
- Alert/Incident link
- Users/Devices/IPs/Message IDs
- Screenshots/log extracts

## Common false positives
- - Admin testing or legitimate automation

## Immediate response actions
- Revoke sessions; reset creds; remove rules; escalate for token forensics (Entra-Revoke-Sessions).

## Escalation criteria
- VIP/sensitive data involved
- Malware confirmed or active exfiltration
- Unclear attribution or repeated recurrence

_Last updated: 2025-08-12_
