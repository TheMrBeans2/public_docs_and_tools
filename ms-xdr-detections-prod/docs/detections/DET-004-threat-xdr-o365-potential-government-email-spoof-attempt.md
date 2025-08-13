# Threat - XDR - o365 - Potential Government Email Spoof Attempt - Rule

**Audience:** Tier 1 SOC  
**Goal:** Fast triage, minimize false positives, escalate correctly.

## Why it matters
- Government domain impersonation/spoof targeting users.

## Signals / When it triggers
- EmailEvents with SPF/DKIM/DMARC failure
- Sender domain ending in .gov or .mil (or lookalike)

## Tier‑1 triage workflow
1. Inspect headers; confirm auth failures.
2. Detonate links/attachments safely.
3. Verify with recipient if expected.

## What to collect for escalation
- Alert/Incident link
- Users/Devices/IPs/Message IDs
- Screenshots/log extracts

## Common false positives
- - Legit third-party sending with proper auth

## Immediate response actions
- Purge/block; warn users; open phishing incident.

## Escalation criteria
- VIP/sensitive data involved
- Malware confirmed or active exfiltration
- Unclear attribution or repeated recurrence

_Last updated: 2025-08-12_
