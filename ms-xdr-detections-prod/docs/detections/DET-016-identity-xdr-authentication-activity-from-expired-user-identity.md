# Identity - XDR - Authentication Activity from Expired User Identity - Rule

**Audience:** Tier 1 SOC  
**Goal:** Fast triage, minimize false positives, escalate correctly.

## Why it matters
- Repeated authentication with expired password (probing / stale creds).

## Signals / When it triggers
- SigninLogs: ResultType 50055 (expired password) followed by success

## Tier‑1 triage workflow
1. Determine if user reset vs. suspicious retry.
2. Review subsequent activity.

## What to collect for escalation
- Alert/Incident link
- Users/Devices/IPs/Message IDs
- Screenshots/log extracts

## Common false positives
- - Users returning from leave

## Immediate response actions
- Force reset; monitor; investigate follow-on actions.

## Escalation criteria
- VIP/sensitive data involved
- Malware confirmed or active exfiltration
- Unclear attribution or repeated recurrence

_Last updated: 2025-08-12_
