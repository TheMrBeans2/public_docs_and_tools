# Microsoft XDR & Sentinel Detections (Production)

This repository contains a curated set of **production‑ready** detections and Tier‑1 guides for Microsoft Defender XDR + Microsoft Sentinel.

- **Custom analytic rules** (YAML) under `detections/sentinel/rules` – ready to import.
- **Out‑of‑the‑box (OOTB) coverage** documented in `mappings/ootb_mapping.csv` (use Sentinel templates or product‑native alerts).
- **Tier‑1 runbooks** for every detection under `docs/detections/` (no placeholders).

## Contents
- `detections/sentinel/rules/` – YAML rules for the following scenarios:
  - Potential government email spoof (.gov/.mil) with authentication failures
  - Successful sign‑in from risky countries
  - Interesting external successful authentication (new ASN per user)
  - Unblocked malware delivered to users
  - Suspicious large outbound email to external recipients
  - Inbound email from newly first‑seen sender domains
  - Mailbox rights delegation (FullAccess/SendAs/SendOnBehalf)
  - File interactions from risky countries (CloudAppEvents)
  - Possible user injection (new country sign‑in then mail forwarding rule)
  - Expired credential authentications (AADSTS50055)
  - Outbound email to first‑seen recipient domains
  - Email activity involving a watchlist of addresses (disabled by default)
  - Malware emailed to users (any delivery action)
  - Administrator‑set mailbox forwarding

- `mappings/` – detection catalog + OOTB mapping
- `docs/detections/` – Tier‑1 triage guides

## Prerequisites
Enable the relevant data connectors in Microsoft Sentinel and Defender XDR:
- **Microsoft 365 Defender (Email & Collaboration)** – for `EmailEvents`, `EmailAttachmentInfo`, `EmailPostDeliveryEvents`.
- **Microsoft Entra ID (Sign‑in & Audit logs)** – for `SigninLogs`, `AuditLogs`.
- **Microsoft Defender for Cloud Apps (MDCA)** – for `CloudAppEvents`.

## Deploy (YAML)
1. In Microsoft Sentinel, go to **Analytics** → **Create** → **Import from YAML** and upload the files from `detections/sentinel/rules/`.
2. Review **Query Period** and **Frequency**; adjust if you have longer ingestion delays.
3. For `Email Activity with Watchlist Address`, edit the `MonitoredAddresses` array in the query and **enable** the rule.
4. Verify alerts by running each query in **Logs** to ensure tables are populated in your tenant.

## Data sources & Columns
Queries rely on the public schema for:
- **EmailEvents** (DeliveryAction, ThreatTypes, SenderFromDomain, RecipientEmailAddress, AuthenticationDetails) – Microsoft Defender XDR.  
- **SigninLogs** (LocationDetails.countryOrRegion, AutonomousSystemNumber, Status.errorCode) – Azure Monitor Logs.  
- **OfficeActivity** (Operation, Parameters, UserId, MailboxOwnerUPN) – Microsoft 365 audit logs.  
- **CloudAppEvents** (CountryCode, ActivityType) – Microsoft Defender for Cloud Apps.

## MITRE ATT&CK
Each rule includes tactics & techniques (e.g., `T1566` Phishing, `T1098` Account Manipulation, `T1114` Email Collection). Treat them as best‑effort mappings – tune to your org’s threat model.

## Quality
- No TODOs or placeholders – rules either ship enabled with sensible defaults, or are clearly disabled until configured (watchlist).
- Queries prefer **baseline plus left‑anti joins** for “first‑seen” signals to reduce false positives.
- Performance: windows are scoped (24h/30d) and projections limit columns.

## Legal
Licensed under MIT. See `LICENSE`.

_Last updated: 2025-08-12_
