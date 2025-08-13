# Rare Office Operations (Admin Ops Anomaly)

**What this detection does**  
Detects rare administrative operations in Microsoft 365 (e.g., `Set-Mailbox`, `New-InboxRule`, `Set-InboxRule`). Source: `OfficeActivity`. Flags operations that are uncommon in your tenant.

**Why we use the official OOB rule (not custom)**  
Microsoft’s OOB baselines operation frequency across tenants and data schemas. Custom ‘rarity’ logic is easy to misconfigure; OOB gets continuous updates and fixes.

**Tier‑1 triage guide (what to look for)**  
1) Identify the operator (UserId, AppId) and the operation.
2) Validate change window/justification with the service owner.
3) Roll back or lock down permissions if unauthorized.

**Tuning & prerequisites**  
• Connector: Office 365 audit.
• Maintain allowlists for automation/service accounts.
• Consider reduced sensitivity during known maintenance windows.

**How to enable**  
Enable from Microsoft 365 solution templates; link to change management references in alert details.

**References**  
Microsoft Sentinel GitHub: RareOfficeOperations.yaml
