# Authentication Attempt from New Country (Entra ID sign-ins)

**What this detection does**  
Flags sign-in attempts from a country/region that has not had a **successful** sign-in for the same account in the previous ~14 days. Source: `SigninLogs`.

**Why we use the official OOB rule (not custom)**  
Maintained by Microsoft with ongoing geo-IP logic improvements and entity mappings (Account/IP). Lower maintenance than custom queries and benefits from community QA in the official repo.

**Tier‑1 triage guide (what to look for)**  
1) Verify the user and geo-IP context in the alert details.
2) Check preceding successful sign-ins for the same user and device.
3) Correlate with MFA prompts or risky sign-in signals (Identity Protection) if available.
4) If user is traveling or using VPN/egress from a new POP, mark as benign with watchlist exception.

**Tuning & prerequisites**  
• Connector: Entra ID sign-in logs (AAD). Ensure `SigninLogs` are ingested.
• Expect false positives for VPN/egress IPs and CDNs—define an allowed egress IP watchlist.
• Consider time-window/threshold adjustments per your org’s travel patterns.

**How to enable**  
Deploy the rule from the template in Sentinel (Analytics → Rule templates). Map entities and set the frequency/lookback per policy.

**References**  
Microsoft Sentinel GitHub: AuthenticationAttemptfromNewCountry.yaml
