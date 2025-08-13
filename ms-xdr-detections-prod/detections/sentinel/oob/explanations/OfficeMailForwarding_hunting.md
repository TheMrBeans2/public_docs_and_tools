# Hunting – Office Mail Forwarding (Per‑Mailbox)

**What this detection does**  
Shows mailboxes configured with forwarding (including `Set-Mailbox -ForwardingSmtpAddress`). Source: `OfficeActivity`.

**Why we use the official OOB rule (not custom)**  
OOB query tracks common admin ops and parameters; better than brittle custom regex over ‘Parameters’ fields.

**Tier‑1 triage guide (what to look for)**  
1) Identify forwarding targets and who set the change.
2) Validate whether forwarding is required for business.
3) Remove/disable forwarding and notify the owner if suspicious.

**Tuning & prerequisites**  
• Connector: Office 365 audit.
• Consider tagging sanctioned forwarding destinations.
• Pair with DLP and ExO transport checks.

**How to enable**  
Run as a hunting query; consider turning into a scheduled analytic for high‑risk groups.

**References**  
Microsoft Sentinel GitHub: OfficeMailForwarding_hunting.yaml
