"""Summarise the pilot once the times and catches are filled in.

Usage:  python pilot_summary.py pilot_scenarios_illustrative.csv
Fill in manual_seconds and ai_seconds (whole seconds, AI time includes
verification and corrections) and manual_caught / ai_caught (Y or N) for
every scenario before running. Applies the reversal sentence in the brief:
keep the check manual if the AI-assisted median time is >= the manual median,
or if the AI-assisted workflow misses even one material discrepancy.
"""
import csv
import statistics
import sys

path = sys.argv[1] if len(sys.argv) > 1 else "pilot_scenarios_illustrative.csv"
with open(path, newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

missing = [r["scenario_id"] for r in rows
           if not all(r[c].strip() for c in ("manual_seconds", "ai_seconds", "manual_caught", "ai_caught"))]
if missing:
    sys.exit(f"Not run yet: fill in times and catches for {', '.join(missing)}")

manual_median = statistics.median([float(r["manual_seconds"]) for r in rows])
ai_median = statistics.median([float(r["ai_seconds"]) for r in rows])
material = [r for r in rows if r["material"].strip().upper() == "Y"]
manual_missed = [r["scenario_id"] for r in material if r["manual_caught"].strip().upper() != "Y"]
ai_missed = [r["scenario_id"] for r in material if r["ai_caught"].strip().upper() != "Y"]

print(f"Scenarios: {len(rows)}  (material discrepancies: {len(material)})")
print(f"Median seconds - manual: {manual_median:g}   AI-assisted: {ai_median:g}")
print(f"Material discrepancies missed - manual: {manual_missed or 'none'}   AI-assisted: {ai_missed or 'none'}")

if ai_median >= manual_median or ai_missed:
    print("Result under the reversal sentence: keep the check manual.")
else:
    print("Result under the reversal sentence: hypothesis supported for this pilot.")
