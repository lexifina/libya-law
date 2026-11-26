# Structure of libya-law

Folder names are in Arabic, the language people search Libyan law in (as in egypt-law). Years and numbers use
Western digits. Every folder holds at most 1,000 entries.

| Folder | What | One file is |
| --- | --- | --- |
| `الإعلان-الدستوري/` | The Constitutional Declaration of 3 August 2011 (Libya's interim constitution): the text as issued, then the text with its amendments | one article (`مادة-001.md`) |
| `نصوص-دستورية/<السنة>/<الرقم>-<الموضوع>/` | Constitutional texts: the Constitution of 1951, the constitutional declarations of 1969 and 1977, the Green Charter of 1988, and the amendments to the Declaration of 2011 | one article |
| `إعلانات/<السنة>/<الموضوع>/` | Declarations (such as the Declaration of Liberation of 2011) | one article |
| `قوانين/<السنة>/<الرقم>-<الموضوع>/` | Laws, codes and law-decrees, by the year the law was made and its number (no number: the subject only) | one article |
| `قرارات/<السنة>/<الرقم>-<الموضوع>/` | Decisions and decrees of the Council of Ministers, ministers and other bodies with regulatory power | one article |
| `قرارات-برلمانية/<السنة>/<الرقم>-<الموضوع>/` | Decisions of the House of Representatives, the General National Congress and the National Transitional Council | one article |
| `لوائح/<السنة>/<الرقم>-<الموضوع>/` | Executive regulations of laws | one article |
| `اتفاقيات-دولية/<السنة>/<الرقم>-<الموضوع>/` | International agreements as Libya published them | one article |
| `data/`, `tools/` | Tables, charts and the tools to read the history | |

Inside an act folder, `ديباجة.md` holds the title, the preamble and the front matter (title, type, number, date, the
issuing body, the source), and each article is `مادة-<n>.md` (`مادة-012-مكرر.md` for an article bis). An act with more
than 900 files keeps its articles in folders of 500 (`مواد-0001-0500/`). The Civil Code
(`قوانين/1953/القانون-المدني/`) keeps its headings in `عناوين/`.

## Versions and dates

- One commit per version of a text: the text as issued, then each later text (a consolidated text "مع تعديلاته")
  at the same path.
- The author date is 12:00 Tripoli time on the day of the version. Before 1970 the date is 1970-01-01 and the real
  day starts the commit subject.
- A text as issued is dated by the day it was made (the source's field "تاريخ النص"). Where its last article puts
  it in force from its issue, `In-force-basis` says so; otherwise the day it applied (often its publication in the
  Official Gazette) is not given by the source, and `In-force-basis` says that too.
- A consolidated text is dated by the newest amending text the source links to it.
- Every commit carries the trailers `Kind:`, `In-force:`, `In-force-basis:`, `Act:`, `Source:` and
  `Source-status:`. The author is the body that made the text.
- A text whose day cannot be read is held, not committed. Nothing is dated by the day it was downloaded.

## Sources

- Ministry of Justice (aladel.gov.ly): the Civil Code (PDF text layer, 2016).
- DCAF Libya Security Sector Legal Database (security-legislation.ly): Arabic texts of laws, decisions, regulations,
  constitutional texts and agreements. DCAF marks them "un-official transcription" and refers to the original as
  published by the Libyan authorities; every commit says so (`Source-status: unofficial transcription`). Laws and
  official texts are not protected by copyright.
- Not used: the Law Society of Libya (lawsociety.ly), whose terms require written permission to copy its digitised
  texts.

`civil-code/` was renamed `قوانين/1953/القانون-المدني/` on 2026-11-26 (a rename only; no text changed).
