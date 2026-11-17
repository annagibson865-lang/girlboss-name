"""Count records, distinct EINs, PA rows, and blank/zero amounts in an IRS EO BMF extract.

Usage:  python scripts/counts.py eo1.csv
Uses only Python's built-in csv module.
"""
import csv
import sys

path = sys.argv[1] if len(sys.argv) > 1 else "eo1.csv"

records = 0
eins = set()
pa_rows = 0
blank = {"ASSET_AMT": 0, "REVENUE_AMT": 0}
zero = {"ASSET_AMT": 0, "REVENUE_AMT": 0}

with open(path, newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        records += 1
        eins.add(row["EIN"])
        if row["STATE"].strip() == "PA":
            pa_rows += 1
        for col in blank:
            value = row[col].strip()
            if value == "":
                blank[col] += 1
            elif value == "0":
                zero[col] += 1

print(f"Records (excluding header): {records:,}")
print(f"Distinct EINs:              {len(eins):,}")
print(f"Records with STATE = PA:    {pa_rows:,}")
for col in blank:
    print(f"{col} blank / zero:      {blank[col]:,} / {zero[col]:,}")
