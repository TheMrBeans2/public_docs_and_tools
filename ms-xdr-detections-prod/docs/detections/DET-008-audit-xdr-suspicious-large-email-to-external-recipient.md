# Audit - XDR - Suspicious Large Email to External Recipient - Rule

**Audience:** Tier 1 SOC  
**Goal:** Fast triage, minimize false positives, escalate correctly.

## Why it matters
- Unusual bulk outbound email or large attachments (data exfil risk).

## Signals / When it triggers
- EmailEvents: Outbound + high recipient count or large size

## Tier‑1 triage workflow
1. Validate business context; check DLP outcome.
2. Review forwarding/transport rules.
3. Inspect recent sign-ins.

## What to collect for escalation
- Alert/Incident link
- Users/Devices/IPs/Message IDs
- Screenshots/log extracts

## Common false positives
- - Approved newsletters

## Immediate response actions
- Throttle/block sender; notify DLP/Legal; purge if policy allows.

## Escalation criteria
- VIP/sensitive data involved
- Malware confirmed or active exfiltration
- Unclear attribution or repeated recurrence

_Last updated: 2025-08-12_
