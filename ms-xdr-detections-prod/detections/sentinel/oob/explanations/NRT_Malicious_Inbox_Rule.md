# NRT – Malicious Inbox Rule (Mailbox‑level)

**What this detection does**  
Near‑real‑time detection for malicious inbox rules (e.g., delete/divert messages, auto‑forward). Source: `OfficeActivity` with NRT scheduling.

**Why we use the official OOB rule (not custom)**  
The NRT rule is performance‑tuned and vetted by Microsoft. Custom NRT queries are error‑prone due to ‘no join/union’ constraints and throttling limits; use OOB.

**Tier‑1 triage guide (what to look for)**  
1) Confirm mailbox owner and recent sign‑ins.
2) Review rule actions (delete/move/forward) and keywords.
3) Check for concurrent MFA fatigue or OAuth app consents.

**Tuning & prerequisites**  
• Connector: Office 365 audit.
• NRT constraints: avoid adding joins; keep rule unmodified if possible.
• Suppress benign workflow rules with explicit watchlists.

**How to enable**  
Enable as NRT in Sentinel. Leverage automation to disable rule and notify mailbox owner.

**References**  
Microsoft Sentinel GitHub: NRT_Malicious_Inbox_Rule.yaml
