# DET-001 – Threat – XDR – MS – Cloud Security Alert

**Audience:** Tier‑1 SOC  
**Goal:** Create incidents for **Microsoft SecurityAlert** signals **other than** MDE and Defender for Cloud, to avoid duplication.  
**Data Source:** `SecurityAlert` (non‑Sentinel providers; not MDE/MDC)

## Why this matters
This rule captures vendor alerts from Microsoft security products *not* handled by specialized rules, ensuring visibility without double‑paging. It excludes Sentinel self‑alerts and providers covered by DET‑021/DET‑015 (MDE) and DET‑003 (MDC). fileciteturn0file2

## Detection logic (summary)
- Include all non‑Sentinel `SecurityAlert` providers **except** MDE/MDC.  
- Dedupe by `SystemAlertId`.  
- 15‑minute lookback; 5‑minute frequency; 15‑minute suppression.

## What Tier‑1 checks first
1. **Provider/Product**: confirm the source and open `AlertLink` for steps.  
2. **Entity context**: user/host/resource in `CompromisedEntity` or `Entities`.  
3. **Overlap**: ensure we aren’t duplicating a case already opened by the specialized detectors.

## Common benign scenarios (tune carefully)
- Low‑priority hygiene alerts from integrated products.  
**Tuning**: tighten on provider names or severity if queue volume spikes.

## Actions (Tier‑1)
- Follow provider remediation; escalate based on severity and data sensitivity.  
- Link related incidents when present.

## KPIs & SLOs
- Duplication with other streams < 2%.  
- MTTA < 10 minutes for High severity.

## Testing
- Compile‑only test (`| take 0`) and replay a known alert from a lower environment.

_Last updated: 2025-08-13_
