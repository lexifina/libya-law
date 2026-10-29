# How this repository was made (Libya)

This file is written by the build on 2026-10-29, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Ministry of Justice of Libya, Civil Code volume (PDF, 14 April 2016) | <https://aladel.gov.ly/home/%d8%a7%d9%84%d9%82%d8%a7%d9%86%d9%88%d9%86-%d8%a7%d9%84%d9%85%d8%af%d9%86%d9%8a-%d9%88%d8%a7%d9%84%d9%85%d9%84%d8%ad%d9%82-%d8%a7%d9%84%d9%85%d8%b9%d8%af%d9%84-%d8%a7%d9%84%d8%ac%d8%b2%d8%a1-%d8%a7/> | 2026-10-29 | No reuse terms stated; official legislation |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `civil-code` | القانون المدني الليبي (Libyan Civil Code) | 2 | 2016-01-18 to 2016-01-19 |

The build made 2 commits:

| Commits | Kind |
| ---: | --- |
| 1 | first version of an act |
| 1 | one law on its in-force day |
| 0 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `future`: laws not yet in force on 2026-10-29.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 1 laws in the record.
- 3 tags.

## Dates

Each commit is dated at noon (Africa/Tripoli) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: Law No. 6 of 2016, art. 4: the law applies from the date of its issue. https://aladel.gov.ly/home/%d8%a7%d9%84%d9%82%d8%a7%d9%86%d9%88%d9%86-%d8%a7%d9%84%d9%85%d8%af%d9%86%d9%8a-%d9%88%d8%a7%d9%84%d9%85%d9%84%d8%ad%d9%82-%d8%a7%d9%84%d9%85%d8%b9%d8%af%d9%84-%d8%a7%d9%84%d8%ac%d8%b2%d8%a1-%d8%a7/

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `0a9854717f874a4c9fc5a12a1eeb5d9c5d72e536d1e952a972bd8ab162cbad2f` (742550 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `6229396f41c9d7f1d6f405becfbe4097b35b82da`, `check.py` `5e112e6a33b7e93d00112e55f01fbb4fb3fdd8da`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

Not yet run for this build.

No second build of this corpus has been compared yet.

## Decisions made by hand

- Scope: the Civil Code only (1,151 articles plus one added article), from the single PDF the Ministry of Justice publishes. Other Libyan laws on the Ministry site are separate PDFs or images and are not in this first build.
- The Ministry volume prints the Code as it stood before Law No. 6 of 2016 and then the text of that Law. The first version is therefore "oldest version available" (first_law null) and is dated 18 January 2016, the day before Law No. 6 took effect; the volume does not say when that earlier text took effect, and the Code itself dates from 1953-54.
- Law No. 6 of 2016 took effect on the date of its issue, 19 January 2016 (its art. 4), the date printed under its signature (9 Rabi II 1437 AH).
- The PDF prints article 870 with the number 780 (a typo in the volume, between 869 and 871); it is stored as article 870.
- Footnotes at the foot of the PDF pages (publication notes and cross-references) and page numbers are left out. Headings (book, part, chapter, section, sub-section) are kept as heading units placed in front of the next article.
- The PDF text layer was normalised: Arabic presentation forms were converted to standard letters (Unicode NFKC) and the Persian yeh and kaf glyphs to Arabic yeh and kaf. Lines were joined into paragraphs at each paragraph number or letter. Some words keep stray spaces from the PDF text layer.
- The repealed articles 229-236, 388-391, 541, 543, 921 and 1109 are removed files from 19 January 2016; the added article 290 bis is a new file.

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- Claude Code (Claude Sonnet 5.5) wrote the scripts. No model wrote, edited or summarised legal text, and no model runs at data-build or git-build time.
