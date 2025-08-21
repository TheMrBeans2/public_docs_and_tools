# KQL Specification (Detections & Validation)

## 1) NoSyslog_24h.kql (Per‑device)
- Strict mapping: `tolower(trim(Syslog.Computer)) == tolower(trim(['Sentinel Lookup']))`.
- Lookback: 25h (24h SLA + 1h buffer).
- Missing criteria: `LastSeen < now() - 24h` or no events at all.
- Outputs: `DeviceName`, `IP`, `DeviceType`, `Site`, `LastSeen`, `Reason`.
- Intended for a **1h** schedule and **25h** query period.

## 2) FeedDown_60m.kql (Site Aggregation)
- Uses the same strict mapping.
- Lookback: 65m (60m window + 5m buffer).
- Fires when a site has `MissingCount >= minCount` OR `MissingPct >= minPercent` (defaults: 3 devices or 50%).

## 3) NoSyslog_7d.kql (Hygiene)
- Same mapping; `threshold = 7d`; `lookback = 8d`.

## 4) Validation_Watchlist_Health.kql
- Detects:
  - Duplicates of `Sentinel Lookup` (case-insensitive)
  - Devices disabled or under suppression
  - Watchlist devices **not observed** in Syslog over the past 7d
  - Syslog devices **not present** in the watchlist (inventory drift)
- Produces separate result tables by `Kind` for quick review.
