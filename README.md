# Libya: law history in git

The Libyan Civil Code as a git history: one file per article, one commit per law on the day its change took effect, and the law that made each change as the commit's author. `git blame` names the law behind every line; `git log` lists every change to an article; picking a date gives the text in force that day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `ly/`.

**First build, and small on purpose.** This is a first, quick build of one act. The text is in **Arabic**, the official language; there is no official English text.

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `civil-code/` | القانون المدني (the Civil Code, 1,151 articles) | 2 | The Code as the Ministry of Justice prints it before 2016, then Law No. 6 of 2016 (in force 19 January 2016): 60 articles replaced, article 290 bis added, 16 articles repealed |

## A lawyer's questions as git commands

| Question | Command |
| --- | --- |
| What did article 1 say on 1 January 2016? | `python tools/on.py 2016-01-01 civil-code art-0001` |
| Which law wrote each line of article 1? | `git blame civil-code/art-0001.md` |
| Every change to article 217 | `git log -p --word-diff civil-code/art-0217.md` |
| Every law in the record, in order | `git log --reverse --format="%ad %an" --date=short main` |

## Dates

- The first version is "oldest version available", credited to the publisher (the Ministry of Justice), and dated 18 January 2016, the day before Law No. 6 of 2016 took effect. The volume does not say when that earlier text took effect; the Code itself was promulgated on 28 November 1953 and published on 20 February 1954.
- Law No. 6 of 2016 (General National Congress, issued 19 January 2016) took effect on its date of issue (its article 4).

## What it does not show

- **Anything before 2016.** The Code was amended many times from 1954; those versions are not online in one place, and none is in this record.
- **Other Libyan laws**, the Constitutional Declaration of 2011 and later amendments, and the Official Gazette. The Ministry publishes them as separate PDFs or images.
- **Footnotes and page numbers** of the Ministry's PDF are left out. Headings (book, part, chapter, section) are in `sec-*.md` files in front of the article they precede.
- **Text-layer quality.** The text comes from the PDF's text layer (no OCR). Some words contain a stray space where the PDF was justified, and heading detection is heuristic. For anything that matters, read the Ministry's original.

## How it is built

Lexifina reads the sources listed here and records each act's dated versions, and the laws that made each change, in one corpus file. `tools/build.py` writes this repository from that file, and the same corpus always gives the same commit hashes; `REPRODUCE.md` gives the details and the checks. A model (Claude) wrote Lexifina's code; it wrote no legal text, and no model runs when the history is built.

`REPRODUCE.md` records the source file's hash, every command and every decision. No AI model wrote or changed legal text.

## Sources

| Source | Kind | Past versions | Names the amending act | Bulk | Notes |
| --- | --- | --- | --- | --- | --- |
| [Ministry of Justice of Libya](https://aladel.gov.ly), Civil Code PDF | Official legislation | no | the volume prints the text of the amending law | no | Used: the text of both versions |

Research guides that cover every country: [GlobaLex](https://www.nyulawglobal.org/globalex/) and the [Law Library of Congress Guide to Law Online](https://www.loc.gov/research-centers/law-library-of-congress/researcher-resources/guide-to-law-online/).

## Licence

Official legislation of Libya, published by the Ministry of Justice (aladel.gov.ly). The Ministry's site states no terms of reuse. The arrangement, commit messages and tools are by Lexifina, under the terms in `LICENSE`. This repository is not legal advice and not an official publication.

## بالعربية

تاريخ القانون المدني الليبي في git: ملف لكل مادة، وإيداع (commit) لكل قانون في يوم نفاذه. النص مأخوذ من الملف الذي تنشره وزارة العدل الليبية (القانون المدني، 1,151 مادة) ثم القانون رقم 6 لسنة 2016 بتعديل بعض أحكام القانون المدني (نافذ من 19 يناير 2016). لم يكتب أي نموذج ذكاء اصطناعي نصاً قانونياً.
