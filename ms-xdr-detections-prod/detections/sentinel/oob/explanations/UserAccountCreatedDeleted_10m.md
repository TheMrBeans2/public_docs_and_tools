# User Account Created & Deleted within 10 Minutes (On‑prem AD)

**What this detection does**  
Detects on-premises AD user accounts created and then deleted within ~10 minutes. Source: `SecurityEvent` Windows security logs.

**Why we use the official OOB rule (not custom)**  
Microsoft’s OOB logic handles common field inconsistencies and entity mapping in Windows events. It’s more portable than bespoke rules that break on parser changes.

**Tier‑1 triage guide (what to look for)**  
1) Pull the Subject/Target accounts; validate if this was lab/test automation.
2) Check for lateral movement or group membership changes in between.
3) Hunt for similar fast create/delete across DCs.

**Tuning & prerequisites**  
• Connector: Windows Security Events (via MMA/AMA).
• Normalize DC clocks; out-of-order timestamps can cause misses.
• Consider excluding OU paths used by automated tests.

**How to enable**  
Enable the template and scope to Domain Controllers; verify event IDs are flowing.

**References**  
Microsoft Sentinel GitHub: UserAccountCreatedDeleted_10m.yaml
