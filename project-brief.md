# PROJECT BRIEF

## Me and my domain
Staff accountant at a mid-sized public accounting firm (firm name withheld). MBA student in data analytics. My portfolio will be public.

## The situation (anonymised)
Before the firm performs a review, compilation or audit for a prospective nonprofit client, it needs to know whether taking the client on could pose a risk to the firm's reputation. Public IRS records can be used to check the prospective client before the firm accepts it. The example client is fictional and based in New York, one of the 8 states covered by eo1.csv (illustrative).

## Who decides, and what
The engagement partner decides whether to approve a limited pilot of the AI-assisted IRS records check for prospective nonprofit clients. In the pilot, staff will compare the manual and AI-assisted workflows on 10 fictional intake scenarios. The engagement partner retains responsibility for accepting, deferring, or declining individual clients.

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
- **Public portfolio:** Includes the method, aggregate counts, a sample AI output with fictional intake details (labelled illustrative) and a link to the IRS source. Excludes the raw IRS CSV (eo1.csv), real client records, internal firm procedures and actual acceptance decisions.

## What a hiring manager should conclude
That I can take a real accounting problem, verify the data, and build a practical tool that helps an engagement partner make a better-informed decision. And that I know where AI can save time and where professional judgment matters.

## Unknowns
- Firm rules on AI use.
- Whether firm policy requires risk or quality lead approval in this case.
- Whether an engagement partner would agree with the job to be done (not yet confirmed by anyone in the role).
- By when the engagement partner must decide on the pilot.
- Whether the partner's real question (in The job to be done) is about accepting a client or about approving the pilot.

## Public-safe check
- **Data choice:** Option (c). Public IRS records plus fictional intake details, labelled illustrative. (I first chose (a); I corrected that to (c).)
- **Withheld:** No real names, employers or clients. One earlier abbreviation is withheld.
- **Columns:** ICO (in-care-of) names and STREET addresses stay out of public outputs.

## My ask, hypothesis and reversal sentence
- **Ask:** Should the engagement partner approve a pilot of an AI-assisted IRS records check for prospective nonprofit clients?
- **Hypothesis:** An exact EIN lookup paired with an AI-generated summary will reduce the median time staff spend checking the IRS record and drafting any needed follow-up questions compared with a fully manual check, while catching all material discrepancies built into the test cases.
- **Reversal sentence:** I’d recommend keeping the check manual if the AI-assisted workflow takes as long as or longer than the manual workflow at the median, or if it misses even one material discrepancy.

I’d run both workflows on 10 fictional intake scenarios using public IRS records. I’d time each check from lookup through final review, including time spent verifying and correcting the AI output. I’d define material discrepancies before testing, such as an EIN tied to a different organization or a conflicting exemption classification. The 10 cases are a proposed pilot size, and the time savings are still unmeasured.

**How I’ll document the test:** I’ll save a CSV in the repository with one row per scenario, the time in seconds for each workflow, the expected discrepancies, and which discrepancies each workflow caught. The AI-assisted time will include verification and corrections. I’ll calculate the medians from that file once the test is run.
