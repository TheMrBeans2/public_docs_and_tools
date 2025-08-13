# Audit - XDR - o365 - Rights Delegation - Rule

**Audience:** Tier 1 SOC  
**Goal:** Fast triage, minimize false positives, escalate correctly.

## Why it matters
- Mailbox rights delegated (potential covert access).

## Signals / When it triggers
- OfficeActivity: Add-MailboxPermission/Add-MailboxFolderPermission

## Tier‑1 triage workflow
1. Validate ticket/intent and delegate identity.
2. Review mailbox for new rules and access history.

## What to collect for escalation
- Alert/Incident link
- Users/Devices/IPs/Message IDs
- Screenshots/log extracts

## Common false positives
- - Helpdesk-approved delegation

## Immediate response actions
- Remove delegation if unauthorized; rotate creds; notify mailbox owner.

## Escalation criteria
- VIP/sensitive data involved
- Malware confirmed or active exfiltration
- Unclear attribution or repeated recurrence

_Last updated: 2025-08-12_
