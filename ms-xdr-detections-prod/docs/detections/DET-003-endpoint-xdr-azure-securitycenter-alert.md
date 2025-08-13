# DET-003 – Endpoint – XDR – Azure SecurityCenter Alert

**Audience:** Tier‑1 SOC  
**Goal:** Create incidents for **Microsoft Defender for Cloud** (MDC) `SecurityAlert` events without Sentinel loops or duplicates.  
**Data Source:** `SecurityAlert` (MDC providers)

## Why this matters
These alerts reflect **workload and cloud posture** threats discovered by Defender for Cloud. Our rule is scoped to MDC and dedupes by `SystemAlertId` to prevent repeats. fileciteturn0file1

## Detection logic (summary)
- Providers: `Azure Security Center`, `Microsoft Defender for Cloud` (or `ProductName` contains “Defender for Cloud”).  
- Exclude Sentinel self‑alerts; dedupe by `SystemAlertId`.  
- 15‑minute lookback; 5‑minute frequency; 15‑minute suppression.

## What Tier‑1 checks first
1. **Resource** (`CompromisedEntity`) exposure and blast radius.  
2. **Vendor guidance**: open `AlertLink`; capture recommended remediation steps.  
3. **Correlated activity**: network denies, policy changes, or VM extension installs around the same time.

## Common benign scenarios (tune carefully)
- External scanner hits on public endpoints.  
**Tuning**: add specific allowlists by resource tags or IP ranges if you routinely see known scanner noise.

## Actions (Tier‑1)
- For credible exploitation: **contain** (NSG/Firewall), page the owning team, and open IR.  
- For policy hygiene alerts: route to **cloud platform** team with a task link.

## KPIs & SLOs
- Duplicate incident rate < 5% (thanks to `SystemAlertId` dedupe).  
- MTTA < 5 minutes for P1 MDC alerts.

## Testing
- Compile‑only test (`| take 0`) and controlled MDC alert generation in a sandbox subscription.

_Last updated: 2025-08-13_
