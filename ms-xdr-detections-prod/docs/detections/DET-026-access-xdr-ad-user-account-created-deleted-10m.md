# Access - XDR - DEX-026 - OOB - AD User Account Created and Deleted within 10 Minutes - Rule

**Audience:** Tier 1 SOC  
**Goal:** Fast triage, minimize false positives, escalate correctly.

## Why it matters
- Short‑lived on‑prem AD accounts are a common attacker pattern to gain and discard access quickly.

## Signals / When it triggers
- Windows SecurityEvent/WindowsEvent shows 4720 then 4726 for same account within ~10 minutes.

## Tier‑1 triage workflow
1. Identify creator/deleter accounts, host, and timing.
2. Review actions by the transient account in between.
3. Validate against change windows or automation jobs.

## What to collect for escalation
- Host, Subject/Target accounts, timestamps, correlated activities.

## Common false positives
- Lab/test automation and bulk user lifecycle scripts.

## Implementation notes
- OOB coverage: DEX-004 OOB – UserAccountCreatedDeleted_10m (Windows event sources).

_Last updated: 2025-08-13_

