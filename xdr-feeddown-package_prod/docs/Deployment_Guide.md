# Deployment Guide
**Workspace:** Microsoft Sentinel (Log Analytics)  
**Mapping contract:** `Syslog.Computer` ⇄ **watchlist** `Sentinel Lookup` (case‑insensitive equality, trimmed).

## 1) Prerequisites
- Sentinel enabled on the target **Log Analytics workspace**.
- Devices forwarding Syslog to the correct collector/workspace.
- RBAC: Sentinel Contributor/Responder; Watchlist Contributor.
- Change control established for watchlist edits.

## 2) Create the Watchlist
1. Sentinel → **Configuration** → **Watchlists** → **Add new**.  
2. Name it **`NetworkDevices_Watchlist`** exactly.  
3. Upload CSV based on `/watchlist/sample.csv`.  
4. Map columns exactly as documented in `/docs/Watchlist_Spec.md`.  
5. Publish.

## 3) Deploy Analytics Rules (ARM)
Replace resource values and run:

```bash
az deployment group create   -g <resource-group>   --template-file sentinel/analytics_rule_NoSyslog_24h.json   --parameters workspaceResourceId="/subscriptions/<sub>/resourceGroups/<rg>/providers/Microsoft.OperationalInsights/workspaces/<workspaceName>"
```

```bash
az deployment group create   -g <resource-group>   --template-file sentinel/analytics_rule_FeedDown_60m.json   --parameters workspaceResourceId="/subscriptions/<sub>/resourceGroups/<rg>/providers/Microsoft.OperationalInsights/workspaces/<workspaceName>"
```

## 4) Workbook
Sentinel → **Workbooks** → **+ New** → **Advanced Editor** → import `/workbook/CoverageWorkbook.json`. Save and share.

## 5) Post‑Deploy Validation
- Run `/kql/Validation_Watchlist_Health.kql` to detect duplicates or mapping issues.  
- Verify counts: **watchlist entries ≈ healthy devices** in the workbook.  
- Simulate: mute a test device (or adjust thresholds temporarily) to confirm alerts.
