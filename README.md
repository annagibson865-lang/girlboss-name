# Checking Nonprofit Clients Against IRS Records

A planned EIN lookup that compares a prospective nonprofit client with public IRS records and flags differences for the engagement partner's accept, defer or decline decision.

## Data source
IRS Exempt Organizations Business Master File Extract (EO BMF), Region 1: Northeast (eo1.csv), downloaded 11/17/2026.
https://www.irs.gov/charities-non-profits/exempt-organizations-business-master-file-extract-eo-bmf

The raw CSV is not included in this repository. Download it from the link above.
Intake details used in examples are fictional and labelled illustrative.

## Files
- `case/project-brief.md`: project brief
- `scripts/counts.py`: counts records, distinct EINs and blank/zero amounts. Run: `python scripts/counts.py eo1.csv`

## AI use
Claude (Anthropic) interviewed me to structure the project brief and wrote scripts/counts.py; I re-ran the script, checked the counts, and own the content and decisions.
