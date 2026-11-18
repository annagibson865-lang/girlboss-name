# Checking Nonprofit Clients Against IRS Records

A planned EIN lookup that compares a prospective nonprofit client with public IRS records and flags differences for the engagement partner's accept, defer or decline decision.

## Data source
IRS Exempt Organizations Business Master File Extract (EO BMF), Region 1: Northeast (eo1.csv), downloaded 11/17/2026.
https://www.irs.gov/charities-non-profits/exempt-organizations-business-master-file-extract-eo-bmf

The raw CSV is not included in this repository. Download it from the link above.
Intake details used in examples are fictional and labelled illustrative.

## Files
- `project-brief.md`: project brief
- `counts.py`: counts records, distinct EINs and blank/zero amounts. Run: `python counts.py eo1.csv`
- `pilot_scenarios_illustrative.csv`: 10 fictional intake scenarios for the pilot (times and catches blank until the pilot is run)
- `lookup.py`: exact EIN lookup that flags name, exemption-type and state differences. Run: `python lookup.py eo1.csv pilot_scenarios_illustrative.csv`
- `lookup_results.csv`: output of `lookup.py` on the 10 scenarios
- `pilot_summary.py`: medians and the reversal test once the pilot times are filled in. Run: `python pilot_summary.py pilot_scenarios_illustrative.csv`

## Status
The lookup has been run on the 10 illustrative scenarios. The pilot (manual vs AI-assisted timing) has not been run yet, so there are no time results.

## AI use
Claude (Anthropic) interviewed me to structure the project brief, wrote counts.py, lookup.py and pilot_summary.py, and drafted the 10 illustrative scenarios. The ask, hypothesis, reversal sentence and decisions are mine. I have not yet re-run the scripts myself.
