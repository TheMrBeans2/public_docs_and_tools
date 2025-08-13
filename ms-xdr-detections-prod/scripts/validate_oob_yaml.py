#!/usr/bin/env python3
"""
Validate YAML syntax for files under detections/oob/azure-sentinel/{analytics,hunting}.
This is not a full schema validator but catches syntax errors early.
"""
import sys, os
from pathlib import Path

try:
    import yaml
except Exception as e:
    print("ERROR: PyYAML not installed. Run: pip install -r requirements.txt", file=sys.stderr)
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[1]
BASE = ROOT / "detections/oob/azure-sentinel"

def validate_dir(d: Path) -> int:
    rc = 0
    for p in sorted(d.rglob("*.yaml")):
        try:
            with p.open("r", encoding="utf-8") as f:
                yaml.safe_load(f)
            print(f"OK: {p.relative_to(ROOT)}")
        except Exception as e:
            print(f"ERROR: {p.relative_to(ROOT)} -> {e}", file=sys.stderr)
            rc = 1
    return rc

def main():
    rc = 0
    rc |= validate_dir(BASE / "analytics")
    rc |= validate_dir(BASE / "hunting")
    sys.exit(rc)

if __name__ == "__main__":
    main()
