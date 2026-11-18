"""Exact EIN lookup: compare fictional intake details with the IRS EO BMF record.

Usage:  python lookup.py eo1.csv pilot_scenarios_illustrative.csv
Writes lookup_results.csv and prints one summary per scenario.
Uses only Python's built-in csv module. Flags are for a person to review;
they are not decisions.
"""
import csv
import re
import sys

eo_path = sys.argv[1] if len(sys.argv) > 1 else "eo1.csv"
intake_path = sys.argv[2] if len(sys.argv) > 2 else "pilot_scenarios_illustrative.csv"
out_path = "lookup_results.csv"

with open(intake_path, newline="", encoding="utf-8") as f:
    intake = list(csv.DictReader(f))
wanted = {row["intake_ein"].strip().zfill(9) for row in intake}

# Read only the EINs we need from the IRS file (ICO and STREET are never read out).
irs = {}
with open(eo_path, newline="", encoding="utf-8") as f:
    for row in csv.DictReader(f):
        if row["EIN"] in wanted:
            irs[row["EIN"]] = row


def norm(name):
    """Upper-case, '&' to AND, drop punctuation and common legal suffixes."""
    name = name.upper().replace("&", " AND ")
    name = re.sub(r"[^A-Z0-9 ]", " ", name)
    words = [w for w in name.split() if w not in {"INC", "CORP", "CORPORATION", "CO", "LLC", "THE"}]
    return " ".join(words)


def exempt_type(subsection):
    return f"501(c)({int(subsection)})" if subsection.strip().isdigit() else "UNKNOWN"


results = []
for row in intake:
    ein = row["intake_ein"].strip().zfill(9)
    rec = irs.get(ein)
    flags = []
    if rec is None:
        flags.append("NO_MATCH: EIN not in this extract; check the EIN and state coverage")
        irs_name = irs_type = irs_state = tax_period = assets = revenue = ""
    else:
        irs_name, irs_state = rec["NAME"], rec["STATE"]
        irs_type = exempt_type(rec["SUBSECTION"])
        tax_period, assets, revenue = rec["TAX_PERIOD"], rec["ASSET_AMT"], rec["REVENUE_AMT"]
        if norm(row["intake_org_name"]) != norm(irs_name):
            flags.append("NAME_DIFFERS")
        if row["intake_exempt_type"].strip() != irs_type:
            flags.append("EXEMPT_TYPE_DIFFERS")
        if row["intake_state"].strip() != irs_state:
            flags.append("STATE_DIFFERS")
    results.append({
        "scenario_id": row["scenario_id"],
        "intake_ein": ein,
        "intake_org_name": row["intake_org_name"],
        "irs_name": irs_name,
        "intake_exempt_type": row["intake_exempt_type"],
        "irs_exempt_type": irs_type,
        "irs_state": irs_state,
        "irs_tax_period": tax_period,
        "irs_asset_amt": assets if (rec is None or assets != "") else "(blank)",
        "irs_revenue_amt": revenue if (rec is None or revenue != "") else "(blank)",
        "flags": "; ".join(flags) if flags else "NONE",
    })

with open(out_path, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=list(results[0]))
    writer.writeheader()
    writer.writerows(results)

for r in results:
    print(f"{r['scenario_id']}  EIN {r['intake_ein']}  ->  {r['flags']}")
    if r["irs_name"]:
        print(f"     IRS: {r['irs_name']} | {r['irs_exempt_type']} | {r['irs_state']} | "
              f"tax period {r['irs_tax_period']} | assets {r['irs_asset_amt']} | revenue {r['irs_revenue_amt']}")
print(f"\nWrote {out_path}")
