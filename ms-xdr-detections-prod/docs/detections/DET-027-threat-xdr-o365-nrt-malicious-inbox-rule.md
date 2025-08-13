# Threat - XDR - DEX-027 - OOB - NRT Malicious Inbox Rule - Rule

**Audience:** Tier 1 SOC  
**Goal:** Fast triage, minimize false positives, escalate correctly.

## Why it matters
- Malicious inbox rules can hide incident notifications and exfiltrate data during BEC.

## Signals / When it triggers
- O365 audit of inbox rule changes containing suspicious keywords/actions (NRT schedule).

## Tier‑1 triage workflow
1. Confirm mailbox owner and recent sign‑ins/MFA prompts.
2. Review rule actions and keywords; disable if suspicious.
3. Correlate with transport rules and forwarding settings.

## What to collect for escalation
- UserId, client IP, rule name/details, keyword matched, originating server.

## Common false positives
- Legitimate automation rules with approved keywords.

## Implementation notes
- OOB coverage: DEX-006 OOB – NRT Malicious Inbox Rule (OfficeActivity).

_Last updated: 2025-08-13_

