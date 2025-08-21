# Validation Checklist (Pre-Go-Live & Quarterly)

## Pre-Go-Live
- [ ] Watchlist name exactly `NetworkDevices_Watchlist` and columns conform to spec.
- [ ] Run `Validation_Watchlist_Health.kql` and resolve all `Critical` items.
- [ ] Import workbook and verify watchlist ≈ healthy devices.
- [ ] Test Rule A by temporarily lowering threshold or muting a lab device.
- [ ] Test Rule B by stopping forwarding for 10–15 minutes on a small site.

## Ongoing
- [ ] Weekly: check workbook for site/device outliers.
- [ ] Weekly: resolve devices under `suppress_until` that expired.
- [ ] Monthly: re-run validation query and remediate drift or duplicates.
- [ ] Quarterly: review thresholds (minCount, minPercent) per site size.
