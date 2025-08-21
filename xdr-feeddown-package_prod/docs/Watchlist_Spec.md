# Watchlist Specification — `NetworkDevices_Watchlist`
**Contract:** `Syslog.Computer` **must equal** `Sentinel Lookup` (case‑insensitive, trimmed). **No partial/contains matching** is used for detection.

## Required Columns
| Column | Type | Constraints | Example |
|---|---|---|---|
| `Sentinel Lookup` | string | **Unique.** 1–128 chars. No leading/trailing spaces. Case-insensitive. | `abr1-wlc-0301` |
| `IP Address` | string | IPv4/IPv6 literal. | `10.84.233.126` |
| `device type` | string | One of: `fw`, `csw`, `dsw`, `asw`, `wlc`, `tsw`, `bgw`, `ntp`, etc. | `wlc` |

## Optional Columns
| Column | Type | Purpose |
|---|---|---|
| `site` | string | Site code; if blank, derived as the prefix before the first `-`. |
| `enabled` | bool/string | Defaults to `true`. Values like `false/0/no` disable the device. |
| `suppress_until` | datetime (UTC) | Temporarily mute device until this time. |
| `owner` | string | Owning team/contact. |
| `notes` | string | Free text (vendor, serial, etc.). |

## Data Quality Rules
- `Sentinel Lookup` must match the device’s **actual** `Syslog.Computer` value emitted to the workspace (short or FQDN).  
- Consistent casing and spacing; solution uses `tolower(trim())` normalization before equality comparison.  
- Enforce uniqueness on `Sentinel Lookup` and avoid duplicate IPs.  
- For planned maintenance, set `suppress_until` (UTC). For long‑term removal, set `enabled=false` or delete row.

## Update Procedure
1. Prepare CSV that conforms to this schema.  
2. Submit change for approval (ticket).  
3. Upload & **Publish** the updated watchlist.  
4. Run `/kql/Validation_Watchlist_Health.kql` and check the workbook for regressions.

## Example `sample.csv`
```
Sentinel Lookup,IP Address,device type,site,enabled,suppress_until,owner,notes
abr1-wlc-0301,10.84.233.126,wlc,abr1,true,,noc@example.org,Primary WLC
abr1-csw-0301,10.84.233.125,csw,abr1,true,,noc@example.org,Core switch
```
