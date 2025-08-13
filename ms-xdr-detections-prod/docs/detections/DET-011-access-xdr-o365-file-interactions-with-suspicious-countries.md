# Access - XDR - o365 - File Interactions with Suspicious Countries - Rule

**Audience:** Tier 1 SOC  
**Goal:** Fast triage, minimize false positives, escalate correctly.

## Why it matters
- File access/sharing from countries outside policy.

## Signals / When it triggers
- CloudAppEvents: file ops with CountryCode in risk list

## Tier‑1 triage workflow
1. Validate travel context; check sign-in risk and device posture.
2. Review sensitivity labels and DLP.

## What to collect for escalation
- Alert/Incident link
- Users/Devices/IPs/Message IDs
- Screenshots/log extracts

## Common false positives
- - VPN egress anomalies

## Immediate response actions
- Revoke sessions; restrict access; engage data protection for sensitive content.

## Escalation criteria
- VIP/sensitive data involved
- Malware confirmed or active exfiltration
- Unclear attribution or repeated recurrence

_Last updated: 2025-08-12_
