# Threat - XDR - o365 - Email Activity with Watchlist Address - Rule

**Audience:** Tier 1 SOC  
**Goal:** Fast triage, minimize false positives, escalate correctly.

## Why it matters
- Email activity involving organization watchlist addresses.

## Signals / When it triggers
- EmailEvents joined with watchlist of addresses/domains

## Tier‑1 triage workflow
1. Confirm subject is in scope.
2. Assess threat and user engagement.

## What to collect for escalation
- Alert/Incident link
- Users/Devices/IPs/Message IDs
- Screenshots/log extracts

## Common false positives
- - Routine vendor communications

## Immediate response actions
- Purge malicious mail; notify VIP handlers; open incident.

## Escalation criteria
- VIP/sensitive data involved
- Malware confirmed or active exfiltration
- Unclear attribution or repeated recurrence

_Last updated: 2025-08-12_
