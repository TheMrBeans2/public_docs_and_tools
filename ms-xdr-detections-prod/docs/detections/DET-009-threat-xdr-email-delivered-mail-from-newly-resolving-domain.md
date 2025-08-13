# Threat - XDR - Email - Delivered Mail from Newly Resolving Domain - Rule

**Audience:** Tier 1 SOC  
**Goal:** Fast triage, minimize false positives, escalate correctly.

## Why it matters
- Inbound email from a first-seen sender domain (NRD).

## Signals / When it triggers
- EmailEvents: SenderFromDomain first seen within lookback

## Tier‑1 triage workflow
1. Check domain age/reputation.
2. Detonate safely; examine similar mail.
3. Verify business context.

## What to collect for escalation
- Alert/Incident link
- Users/Devices/IPs/Message IDs
- Screenshots/log extracts

## Common false positives
- - New legitimate vendors

## Immediate response actions
- Block domain; purge; create TI indicator if needed.

## Escalation criteria
- VIP/sensitive data involved
- Malware confirmed or active exfiltration
- Unclear attribution or repeated recurrence

_Last updated: 2025-08-12_
