#!/usr/bin/env python3
"""
Fetch official Microsoft Sentinel OOB detections defined in manifest.json and store them locally.
- Preserves filename from the source path.
- Writes into ./detections/oob/azure-sentinel/{analytics|hunting}/
- Adds a simple provenance header to each file.
"""
import json, os, sys, time, hashlib
from pathlib import Path

try:
    import requests
except Exception as e:
    print("ERROR: requests not installed. Run: pip install -r requirements.txt", file=sys.stderr)
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "detections/sentinel/oob/manifest.json"
OUT_ANALYTICS = ROOT / "detections/sentinel/oob/analytics"
OUT_HUNTING = ROOT / "detections/sentinel/oob/hunting"

def sha256_bytes(b: bytes) -> str:
    h = hashlib.sha256(); h.update(b); return h.hexdigest()

def fetch(url: str, timeout=30):
    # Use raw.githubusercontent.com where possible for consistent content
    # manifest already points to raw URLs
    r = requests.get(url, timeout=timeout)
    r.raise_for_status()
    return r.content

def main():
    if not MANIFEST.exists():
        print(f"Manifest not found at {MANIFEST}", file=sys.stderr)
        sys.exit(1)
    items = json.loads(MANIFEST.read_text())["items"]
    OUT_ANALYTICS.mkdir(parents=True, exist_ok=True)
    OUT_HUNTING.mkdir(parents=True, exist_ok=True)

    written = []
    for it in items:
        url = it["raw_url"]
        name = it["name"]
        kind = it["kind"]
        raw = fetch(url)
        digest = sha256_bytes(raw)
        header = (
            f"# Source: {url}\n"
            f"# Retrieved: {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\n"
            f"# SHA256: {digest}\n"
        ).encode("utf-8")

        # Try to preserve original filename from path
        src_filename = Path(it["path"]).name
        if not src_filename.endswith(".yaml"):
            src_filename += ".yaml"

        out_dir = OUT_ANALYTICS if kind.lower()=="analytics" else OUT_HUNTING
        out_path = out_dir / src_filename

        out_path.write_bytes(header + raw)
        written.append(str(out_path.relative_to(ROOT)))

    print("Fetched OOB files:")
    for w in written:
        print(" -", w)

if __name__ == "__main__":
    main()
