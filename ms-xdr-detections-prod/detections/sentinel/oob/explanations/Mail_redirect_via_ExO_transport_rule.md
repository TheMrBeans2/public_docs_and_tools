# Mail Redirect via Exchange Online Transport Rule

**What this detection does**  
Alerts when an Exchange Online **transport rule** is configured to forward/redirect mail—common in BEC.
Source: `OfficeActivity` (Exchange admin operations).

**Why we use the official OOB rule (not custom)**  
Microsoft aligns this rule with evolving Exchange telemetry and includes entity mapping and sample suppressions. Prefer OOB so you inherit fixes and additional operation coverage.

**Tier‑1 triage guide (what to look for)**  
1) Identify who created/modified the rule and when.
2) Review the rule’s conditions and destination(s).
3) Check for related inbox rules and sign-in anomalies for the same admin/user.

**Tuning & prerequisites**  
• Connector: M365/Office 365 audit (Unified Audit Log).
• Tune: exclude known org-wide journaling/archiving rules; use allowlist for known gateways.
• Pair with ‘Malicious Inbox Rule’ for per‑mailbox coverage.

**How to enable**  
Enable under the Microsoft 365 solution templates; validate the audit pipeline and role assignments.

**References**  
Microsoft Sentinel GitHub: Mail_redirect_via_ExO_transport_rule.yaml
