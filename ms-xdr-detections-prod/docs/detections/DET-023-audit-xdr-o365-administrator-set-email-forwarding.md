# Audit - XDR - o365 - Administrator Set Email Forwarding - Rule

**Audience:** Tier 1 SOC  
**Goal:** Fast triage, minimize false positives, escalate correctly.

## Why it matters
- Admin configured mailbox-level forwarding (high risk if external).

## Signals / When it triggers
- OfficeActivity: Set-Mailbox where ForwardingAddress/ForwardingSmtpAddress changed

## Tier‑1 triage workflow
1. Verify ticket and destination domain.
2. Review mailbox rules and sign-ins.

## What to collect for escalation
- Alert/Incident link
- Users/Devices/IPs/Message IDs
- Screenshots/log extracts

## Common false positives
- - Planned migrations/service routing

## Immediate response actions
- Revert if unauthorized; notify leadership; review admin activity.

## Escalation criteria
- VIP/sensitive data involved
- Malware confirmed or active exfiltration
- Unclear attribution or repeated recurrence

_Last updated: 2025-08-12_
