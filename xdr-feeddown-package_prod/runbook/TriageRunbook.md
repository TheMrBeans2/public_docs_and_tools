# Triage Runbook — Syslog Missing / Feed‑Down

## Inputs
Incident details include: DeviceName, IP, DeviceType, Site, LastSeen, Reason.

## Steps
1) **Scope**: Check if this is isolated (single device) or site-wide (feed‑down).  
2) **Quick reachability**: Ping/SSH/HTTPS to device; NMS status.  
3) **Collector path**: Syslog daemon (rsyslog/syslog‑ng) up, VM health, firewall/NAT paths, AMA/CEF connector status.  
4) **Device config**: Verify logging enabled and forwarding target/port/protocol correct; check recent config changes.  
5) **Recovery**: When logs resume, link confirming events and close with RCA.  
6) **Follow‑up**: If frequent feed‑down, review network path capacity or collector scaling.
