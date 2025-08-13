# Access - XDR - Interesting External Successful Authentication - Rule

**Audience:** Tier 1 SOC  
**Goal:** Fast triage, minimize false positives, escalate correctly.

## Why it matters
- Login success from unfamiliar ASN/IP for the user.

## Signals / When it triggers
- SigninLogs: success + new ASN for user
- Public IP, not seen in baseline

## Tier‑1 triage workflow
1. Check ASN/IP reputation and history.
2. Confirm MFA and device compliance.
3. Look for concurrent anomalies.

## What to collect for escalation
- Alert/Incident link
- Users/Devices/IPs/Message IDs
- Screenshots/log extracts

## Common false positives
- - Home networks for remote staff

## Immediate response actions
- Revoke sessions; reset credentials if suspicious; allowlist benign ASNs.

## Escalation criteria
- VIP/sensitive data involved
- Malware confirmed or active exfiltration
- Unclear attribution or repeated recurrence

_Last updated: 2025-08-12_
