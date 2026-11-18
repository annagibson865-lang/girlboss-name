# PROJECT BRIEF

## Me and my domain
Staff accountant at a mid-sized public accounting firm (firm name withheld). MBA student in data analytics. My portfolio will be public.

## The situation (anonymised)
Before the firm performs a review, compilation or audit for a prospective nonprofit client, it needs to know whether taking the client on could pose a risk to the firm's reputation. Public IRS records can be used to check the prospective client before the firm accepts it. The example client is fictional and based in New York, one of the 8 states covered by eo1.csv (illustrative).

## Who decides, and what
- **Decider (role):** The prospective engagement partner. Approval from the firm's risk or quality management lead is needed if firm policy requires it.
- **Decision:** Accept the engagement, defer it while gathering information or resolving concerns, or decline it.
- **By when:** Before the firm signs the engagement letter or begins engagement work.
- **One action:** The partner records accept, defer or decline after reviewing the IRS check and the follow-up.

## The job to be done (how I know)
*My guess, not confirmed by them. I have not spoken to an engagement partner; this is my own assumption.*
- **Their real question:** "Do we have enough information to accept this nonprofit as a client, or is there something we need to resolve first?"
- **What they already know:** The nonprofit's name, what it does, the service requested and its deadline. They may also have its EIN, most recent financial statements or Form 990.
- **Their time:** 30–60 minutes of staff and partner time combined for a straightforward acceptance review (my planning estimate; firms vary). The IRS lookup is one small step within it, about 2–5 minutes (my estimate). Elapsed time can be several business days while waiting on documents, clarification or approval.

## Data I can use
Source: eo1.csv, a public IRS Exempt Organizations Business Master File extract covering CT, ME, MA, NH, NJ, NY, RI and VT. **Scope: these 8 states only.**

| Number or check | Result | Status |
|---|---|---|
| Records (excluding header) | 281,266 | Measured by me (Python csv module) |
| Distinct EINs | 281,266 | Measured by me |
| Records with STATE = PA | 0 | Measured by me |
| ASSET_AMT blank / zero | 58,305 / 101,537 | Measured by me |
| REVENUE_AMT blank / zero | 82,236 / 104,263 | Measured by me |
| Client assets and revenue, with TAX_PERIOD | — | Planned |
| Exact EIN match and name check | — | Planned (needs a fictional client's EIN and name) |

Blanks are kept separate from zeros.

## The AI idea
1. **Look up the client:** An exact EIN lookup retrieves the IRS record. If there is no match, the tool reports that and prompts staff to check the EIN and the state coverage.
2. **Flag and summarise:** AI compares the IRS record with the intake details, highlights differences in name or exemption classification, and summarises listed assets and revenue alongside the tax period.
3. **Draft a follow-up:** If the names differ, AI drafts a question asking the client to confirm its current legal name and whether it has changed.

**Human judgment:** Staff verify flagged differences against the underlying records. The partner decides, weighing the findings alongside independence, engagement risk and the firm's ability to do the work.

## Constraints
- **Deadline:** Tuesday, November 24, 2026 (course deadline).
- **Tools:** Python's csv module for the counts. Excel is possible for a demonstration if the course allows it.
- **AI and client data:** The course allows AI use; the project instructions require it. Firm AI rules are UNKNOWN. The prototype uses only public IRS records and fictional intake details labelled illustrative. No real client intake forms, financial statements or internal acceptance notes go into AI tools unless their use is explicitly authorised.
- **Public portfolio:** Includes the method, aggregate counts, a sample AI output with fictional intake details (labelled illustrative) and a link to the IRS source. Excludes the raw CSV, real client records, internal firm procedures and actual acceptance decisions.

## What a hiring manager should conclude
That I can take a real accounting problem, verify the data, and build a practical tool that helps an engagement partner make a better-informed decision. And that I know where AI can save time and where professional judgment matters.

## Unknowns
- Firm rules on AI use.
- Whether firm policy requires risk or quality lead approval in this case.
- Whether an engagement partner would agree with the job to be done (not yet confirmed by anyone in the role).

## Public-safe check
- **Data choice:** Option (c). Public IRS records plus fictional intake details, labelled illustrative. (I first chose (a); I corrected that to (c).)
- **Withheld:** No real names, employers or clients. One earlier abbreviation is withheld.
- **Columns:** ICO (in-care-of) names and STREET addresses stay out of public outputs.

## My ask, claim and reversal sentence (I add these later)
- **Ask:**
- **Claim:**
- **Reversal sentence:**
