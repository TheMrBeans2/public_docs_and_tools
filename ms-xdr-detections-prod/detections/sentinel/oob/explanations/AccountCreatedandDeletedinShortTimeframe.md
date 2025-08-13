# Account Created and Deleted in Short Timeframe (Entra ID)

**What this detection does**  
Looks for Entra ID accounts created and then deleted within a short period (e.g., <24h). Sources: `AuditLogs` and related identity tables.

**Why we use the official OOB rule (not custom)**  
Lifecycle anomalies benefit from vendor-maintained joins across audit payloads. OOB template is tuned for common attack patterns (throwaway accounts).

**Tier‑1 triage guide (what to look for)**  
1) Identify creator and deleter principals; verify automation vs. human.
2) Review any resource access in between create/delete.
3) If malicious, search for other transient accounts or app registrations.

**Tuning & prerequisites**  
• Connectors: Entra ID Audit Logs.
• If you use identity lifecycle automation (e.g., HR driven), add service account allowlists.
• Consider decreasing lookback if noise is high.

**How to enable**  
Enable from the Microsoft Entra ID solution templates; configure suppression windows aligned to HR processes.

**References**  
Microsoft Sentinel GitHub: AccountCreatedandDeletedinShortTimeframe.yaml
