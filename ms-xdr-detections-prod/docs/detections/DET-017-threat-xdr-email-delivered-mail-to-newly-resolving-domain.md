# Threat - XDR - Email - Delivered Mail to Newly Resolving Domain - Rule

**Audience:** Tier 1 SOC  
**Goal:** Fast triage, minimize false positives, escalate correctly.

## Why it matters
- Outbound email to a first-seen recipient domain (possible exfil/test).

## Signals / When it triggers
- EmailEvents: outbound recipients with first-seen domain

## Tier‑1 triage workflow
1. Validate business need; check DLP.
2. Review sign-in context and forwarding rules.

## What to collect for escalation
- Alert/Incident link
- Users/Devices/IPs/Message IDs
- Screenshots/log extracts

## Common false positives
- - New customer/vendor onboarding

## Immediate response actions
- Throttle if needed; notify owner/manager if suspicious.

## Escalation criteria
- VIP/sensitive data involved
- Malware confirmed or active exfiltration
- Unclear attribution or repeated recurrence

_Last updated: 2025-08-12_
