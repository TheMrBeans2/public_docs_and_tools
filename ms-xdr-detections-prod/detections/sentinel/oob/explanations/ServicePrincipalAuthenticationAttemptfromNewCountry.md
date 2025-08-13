# Service Principal Authentication from New Country

**What this detection does**  
Detects service principal sign-in attempts from countries with no prior **successful** sign-ins in ~14 days. Source: `SigninLogs`.

**Why we use the official OOB rule (not custom)**  
Service-principal behavior baselining is tricky. The OOB logic handles entity mapping and prior-success logic. Using the OOB rule reduces fragile custom joins and time windows.

**Tier‑1 triage guide (what to look for)**  
1) Confirm the appId/SPN and owning team.
2) Check if the app runs from Azure only; investigate off-Azure IPs.
3) Validate credential hygiene (cert/secret rotations, unexpected permissions).

**Tuning & prerequisites**  
• Connector: Entra ID sign-in logs.
• Maintain allowlist for expected egress IP ranges (private agents, self-hosted runners).
• Pair with Conditional Access policies where possible.

**How to enable**  
Enable from the template; set alert grouping if your pipeline generates bursts.

**References**  
Microsoft Sentinel GitHub: ServicePrincipalAuthenticationAttemptfromNewCountry.yaml
