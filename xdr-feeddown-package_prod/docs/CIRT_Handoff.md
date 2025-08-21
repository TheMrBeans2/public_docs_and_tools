# CIRT Handoff — Network Device Syslog Monitoring (Production Package)
**Version:** 1.0  
**Last Updated:** 2025-08-21 13:48 UTC  
**Owner:** SOC Engineering

This handoff contains everything required for the CIRT team to **operate, maintain, and extend** the solution that verifies **Syslog receipt** for all expected network devices and detects **feed‑down** outages.

---

## 1. What the solution does
- **Per‑device monitoring (24h):** Creates an alert when any device in the **watchlist** has not produced **`Syslog`** in the last **24 hours**.
- **Feed‑down monitoring (60m):** Creates a site‑scoped alert when **multiple devices at the same site** have not produced Syslog in the last **60 minutes**.
- **Coverage visibility:** Workbook shows **watchlist vs. active devices** and **LastSeen** per device/site.

> **Mapping contract (authoritative):** `Syslog.Computer` **equals** (case‑insensitive, trimmed) **watchlist column** `Sentinel Lookup`. This equality mapping is the basis of all detections.

---

## 2. What’s included
- **KQL** for detections and validation (see `/kql`).  
- **ARM templates** to deploy analytics rules with correct schedules and entity mappings (see `/sentinel`).  
- **Workbook** to visualize coverage (see `/workbook`).  
- **Watchlist specification** and example CSV (see `/watchlist` and `/docs/Watchlist_Spec.md`).  
- **Operations documentation** (this file) and the **triage runbook**.

Directory map:
```
xdr-feeddown-package/
├─ docs/
│  ├─ CIRT_Handoff.md             # THIS FILE
│  ├─ Deployment_Guide.md
│  ├─ Watchlist_Spec.md
│  ├─ KQL_Spec.md
│  └─ Validation_Checklist.md
├─ kql/
│  ├─ NoSyslog_24h.kql            # Strict equality mapping
│  ├─ FeedDown_60m.kql            # Strict equality + site aggregation
│  ├─ NoSyslog_7d.kql             # Optional hygiene
│  ├─ Validation_Watchlist_Health.kql
│  └─ Workbook_Coverage.kql
├─ sentinel/
│  ├─ analytics_rule_NoSyslog_24h.json
│  └─ analytics_rule_FeedDown_60m.json
├─ workbook/
│  └─ CoverageWorkbook.json
├─ watchlist/
│  ├─ sample.csv
│  └─ constraints.md
└─ runbook/
   └─ TriageRunbook.md
```

---

## 3. High‑level deployment (summary)
1. **Create/verify watchlist** named **`NetworkDevices_Watchlist`** using `/watchlist/sample.csv` as the schema.  
2. **Deploy analytics rules** via ARM templates under `/sentinel` (or paste the KQL into new rules in the portal).  
3. **Import the workbook** from `/workbook/CoverageWorkbook.json`.  
4. Configure **Automation rules** for routing and tags (`NoLogs24h`, `FeedDown`).

> For detailed steps, see `/docs/Deployment_Guide.md`.

---

## 4. Operating the solution
- Use the **Coverage workbook** to verify health and quickly spot site patterns.  
- Follow the **Triage Runbook** during incidents.  
- Maintain the **watchlist** under change control (adds/removes, `suppress_until`, `enabled`).  
- Use the **Validation queries** to detect duplicates, mismatches, and stray Syslog sources.

---

## 5. Support
- Primary: SOC Engineering On‑Call  
- Secondary: Network Engineering On‑Call  
- Escalation: CIRT Duty Manager
