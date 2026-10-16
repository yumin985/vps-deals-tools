#!/usr/bin/env python3
"""Convert vps-deals offers.json into a CSV snapshot using only the stdlib."""
import csv, json, sys
from pathlib import Path

src = Path(sys.argv[1] if len(sys.argv) > 1 else "offers.json")
out = Path(sys.argv[2] if len(sys.argv) > 2 else "offers.csv")
rows = json.loads(src.read_text(encoding="utf-8")).get("offers", [])
fields = ["provider", "title", "price", "currency", "offer_url", "valid_until", "source_url", "fetched_at"]
with out.open("w", encoding="utf-8", newline="") as handle:
    writer = csv.DictWriter(handle, fieldnames=fields)
    writer.writeheader()
    writer.writerows({field: row.get(field, "") for field in fields} for row in rows)
print(f"wrote {len(rows)} rows to {out}")
