# Optional STE-informed writing

Read this reference only when the user explicitly activates the technical / STE mode described in SKILL.md.

## Sources and level of application

ASD-STE100 combines writing rules with a controlled dictionary. The guidance below is a practical adaptation for completion reports, not a complete reproduction of the standard.

- [Official ASD-STE100 site](https://www.asd-ste100.org/index.html)
- [Official Issue 9 standard, dated January 15, 2025](https://www.asd-ste100.org/assets/files/ASD-STE100_ISSUE9.pdf)
- [Official downloads and current-issue information](https://asd-ste100.org/STE_downloads.html)

For “write technically” or “use STE,” apply the guidance below as an STE-informed style. Do not claim formal compliance. If the user requests strict ASD-STE100 compliance, consult the applicable official edition, check both the writing rules and dictionary, and apply its provisions for technical terms. Use the edition the user specifies; otherwise verify the current edition through the official site. If the standard is unavailable or the check is incomplete, describe the result as STE-informed and state the verification limit briefly.

## Apply to the report

- Use short, direct sentences. Keep one main idea in each sentence; split a change, its verification, and its unfinished work when combining them makes the result difficult to follow.
- Identify the actor or object clearly. Prefer active voice when it clarifies who did what. Use commands for requested next actions, and factual statements for completed work.
- Use the same term for the same concept throughout. Retain necessary domain terms and define unfamiliar terms or abbreviations on first use. Technical writing does not mean adding jargon.
- Prefer concrete verbs and literal language. Remove ornamental wording, idioms, and vague claims such as “optimized the workflow” when the actual change can be named.
- State conditions, exceptions, and dependencies explicitly. Replace ambiguous pronouns with the relevant noun when needed.
- Preserve numbers, units, identifiers, negation, uncertainty, and causal qualifications. Do not simplify a sentence in a way that changes its technical meaning or overstates completion.
- Preserve exact quotations, code, file paths, and official names. Apply the style to the explanatory prose around them.
- Keep related sentences in their task sub-point. Sentence simplification must not scatter one task across multiple top-level sections or remove evidence the user needs for review.

## Example

Before:

- **Partial — Validation.** The validation framework has been enhanced to facilitate the identification of problematic records, with further verification pending.

STE-informed rewrite, assuming the work record supports these details:

- **Partial — Validation.** Added a check for records with missing dates. The check passed on the sample file. Remaining: run the check on the full dataset.

The rewrite is illustrative, not certified STE. Never invent the specific change or test result to make a vague report sound precise; inspect the evidence or mark the detail as unverified.
