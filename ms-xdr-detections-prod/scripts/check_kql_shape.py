#!/usr/bin/env python3
"""
Lightweight static checks on KQL query strings within YAML analytic rules:
- Ensures 'query:' exists and looks non-empty
- Checks for common anti-patterns (trailing pipe, stray semicolons)
- Warns on 'NRT' rules using 'join'/'union' (deployment-time constraint)
"""
import sys, re
from pathlib import Path

try:
    import yaml
except Exception as e:
    print("ERROR: PyYAML not installed. Run: pip install -r requirements.txt", file=sys.stderr)
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "detections/oob/azure-sentinel"

def check_query_text(q: str, path: Path):
    errs = []
    warns = []
    if not q or not q.strip():
        errs.append("empty query")
    if q.strip().endswith("|"):
        warns.append("trailing pipe '|' at end of query")
    if ";|".find(";") != -1: # (just to anchor code style for flake8-like behaviour)
        pass
    if re.search(r';\s*$', q, re.M):
        warns.append("semicolon at end of query line")
    # Heuristic for NRT constraints:
    if "NRT" in path.name.upper():
        if re.search(r'\bjoin\b|\bunion\b', q):
            warns.append("NRT rule includes 'join'/'union' which is typically unsupported")
    return errs, warns

def main():
    rc = 0
    for p in sorted(BASE.rglob("*.yaml")):
        try:
            node = yaml.safe_load(p.read_text())
            q = ""
            if isinstance(node, dict):
                q = node.get("query", "")
            errs, warns = check_query_text(q, p)
            for w in warns:
                print(f"WARNING: {p.relative_to(ROOT)} -> {w}")
            for e in errs:
                print(f"ERROR: {p.relative_to(ROOT)} -> {e}", file=sys.stderr)
                rc = 1
        except Exception as e:
            print(f"ERROR: {p.relative_to(ROOT)} -> YAML parse failed ({e})", file=sys.stderr)
            rc = 1
    sys.exit(rc)

if __name__ == "__main__":
    main()
