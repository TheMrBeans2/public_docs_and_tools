# DET-002 – Audit – XDR – O365 – eDiscovery Export Alert

**Audience:** Tier‑1 SOC  
**Goal:** Detect and triage potentially unauthorized Microsoft Purview/SCC **exports** that could exfiltrate data.  
**Data Source:** `OfficeActivity` (Unified Audit Log)

## Why this matters
eDiscovery and Purview exports can move large volumes of sensitive content off‑tenant. We alert on concrete **export actions** (e.g., `Export-ComplianceSearch`, `CreateExport`) with **actor** and **client IP** to accelerate first‑response. fileciteturn0file0

## Detection logic (summary)
- Match against a curated list of **export/search action verbs** across Purview/SCC.
- Deduplicate using a stable **ExportKey** (prefers `SourceRecordId`, falls back to a hashed parameter signature).
- 30‑minute sliding lookback; 5‑minute frequency; 30‑minute suppression to avoid repeat spam.

## What Tier‑1 checks first
1. **Actor legitimacy**: Is `UserId` a Legal/Compliance account with an active ticket?  
2. **Scope/size**: Open `Parameters` to see case/search and expected volume.  
3. **Origin**: Is `ClientIP` expected? Any unusual geo or TOR/VPN indicators?  
4. **Parallel signals**: MDO purge requests, DLP events, or risky sign‑ins around the same time.

## Common benign scenarios (tune carefully)
- Approved eDiscovery exports executed by Legal.  
- Training/UAT tenants mirroring production.  
**Tuning**: if desired, maintain a **watchlist** of sanctioned service accounts and add a filter `| where UserId !in (watchlist)`.

## Actions (Tier‑1)
- If **approved**: attach the ticket to the incident and close as informational.  
- If **unapproved or unclear**: **halt export**, notify Legal/Compliance, preserve evidence, and escalate to IR.

## KPIs & SLOs
- False‑positive rate < 10% after allowlisting sanctioned actors.  
- MTTA < 10 minutes; time‑to‑halt < 30 minutes for unauthorized exports.

## Testing
- Compile‑only test (`| take 0`) with the repo’s validator.  
- In lower env, execute a harmless **test export** to validate fields and suppression.

_Last updated: 2025-08-13_
