# Identity - XDR - DEX-025 - OOB - Service Principal Authentication Attempt from New Country - Rule

**Audience:** Tier 1 SOC  
**Goal:** Fast triage, minimize false positives, escalate correctly.

## Why it matters
- Service principals authenticating from novel geos can indicate abuse of app credentials outside expected environments.

## Signals / When it triggers
- AAD service principal sign-in attempt from a country with no successful sign-ins in ~14 days.

## Tier‑1 triage workflow
1. Identify the app (SPN) owner and intended hosting location.
2. Check IP ownership (Azure vs non-Azure); validate network paths.
3. Review permissions and recent changes to credentials (cert/secrets).

## What to collect for escalation
- ServicePrincipalName, IPs, Locations, Result codes.

## Common false positives
- New private egress, self-hosted runner IPs, or new Azure regions.

## Implementation notes
- OOB coverage: DEX-002 OOB – Service Principal Authentication Attempt from New Country.

_Last updated: 2025-08-13_

