# Hunting – Multiple Users Email Forwarded to Same Destination

**What this detection does**  
Highlights when multiple user mailboxes are configured to forward mail to the **same** destination—typical BEC pattern. Source: `OfficeActivity`.

**Why we use the official OOB rule (not custom)**  
As a **hunting** query, the OOB version is broad and maintained alongside other M365 content. Use it as a base for ad-hoc sweeps and convert to scheduled if needed.

**Tier‑1 triage guide (what to look for)**  
1) Enumerate impacted mailboxes and the common destination.
2) Confirm if destination is external and unexpected.
3) Pivot to sign-in and consent logs for the same users.

**Tuning & prerequisites**  
• Connector: Office 365 audit.
• If scheduled, ensure performance limits are respected; consider summarized tables.
• Maintain an allowlist for legitimate relay/forward destinations.

**How to enable**  
Run from Hunting. Optionally wrap into a scheduled rule with tuned thresholds and alert details.

**References**  
Microsoft Sentinel GitHub: MultipleUsersEmailForwardedToSameDestination.yaml
