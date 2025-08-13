# Repository Guidelines

## Project Structure & Organization
- `detections/sentinel/rules/`: Production-ready Microsoft Sentinel analytic rules in YAML (e.g., `DET-014-access-xdr-possible-user-injection-activity.yaml`).
- `docs/detections/`: Tier‑1 triage/runbook markdown for each rule (e.g., `DET-014-… .md`).
- `mappings/`: Catalog and OOTB coverage CSVs (e.g., `detections_catalog.csv`, `ootb_mapping.csv`).

## Contribution Workflow
- Add a new rule: create a YAML in `detections/sentinel/rules/`, a matching doc in `docs/detections/`, and a row in `mappings/detections_catalog.csv`.
- Keep IDs stable: use the `DET-###` prefix consistently across YAML filename, doc filename, and catalog.
- Validate locally: run the query in Sentinel Logs, confirm required tables (e.g., `EmailEvents`, `SigninLogs`) are populated, then import YAML via Sentinel “Analytics → Import from YAML” as a dry run.

## Coding Style & Naming
- Filenames: `DET-###-<category>-xdr-<concise-hyphenated-title>.yaml` and matching `.md`.
- YAML keys: follow Sentinel schema (e.g., `id`, `name`, `kind`, `severity`, `enabled`, `query`, `queryFrequency`, `queryPeriod`, `tactics`, `relevantTechniques`).
- Queries: prefer scoped windows, explicit projections, and baseline + left‑anti joins for first‑seen logic.
- Docs: concise purpose, prerequisites, triage steps, and false‑positive notes.

## Testing Guidelines
- Query correctness: execute KQL in Sentinel to verify results and performance on real data.
- Rule behavior: import YAML to validate frequency, period, and thresholds; confirm alerts fire with sample data.
- Traceability: ensure every YAML has a corresponding doc and catalog entry; keep `severity`, `tactics`, and description aligned.

## Commit & Pull Requests
- Commit messages: start with the detection ID and scope, e.g., `DET-014: tighten anti-join baseline`.
- PRs must include: summary, impacted files, test evidence (query screenshots or counts), and any mapping updates.
- Avoid sensitive data: scrub tenant IDs, emails, IPs, and message subjects from examples.

## Security & Data Hygiene
- Never commit credentials or tenant-specific artifacts.
- Keep watchlists and org-specific indicators out of version control; document how to configure them in the rule doc.

