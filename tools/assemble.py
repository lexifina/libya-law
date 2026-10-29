"""Assemble corpus.json from the parsed Civil Code and Law No. 6 of 2016 (cache only, no network)."""
import json
import re
from pathlib import Path

import parse
from parse import HERE, PARA_RE, LET_RE, SHA, fix

PAGE = ('https://aladel.gov.ly/home/%d8%a7%d9%84%d9%82%d8%a7%d9%86%d9%88%d9%86-%d8%a7%d9%84%d9%85%d8%af%d9%86%d9%8a-'
        '%d9%88%d8%a7%d9%84%d9%85%d9%84%d8%ad%d9%82-%d8%a7%d9%84%d9%85%d8%b9%d8%af%d9%84-%d8%a7%d9%84%d8%ac%d8%b2%d8%a1-%d8%a7/')
PDF_URL = parse.URL


def head_units(order, heads):
    """Structural headings (book, chapter, section ...) as 'sec-<next article>' units, in front of the next article."""
    out = {}
    for k, lines in heads.items():
        i = order.index(k) + 1
        if i >= len(order):
            continue
        nxt = order[i]
        lines = [fix(l) for l in lines if fix(l)]
        out['sec-' + nxt[4:]] = {'label': lines[0], 'kind': 'heading',
                                  'text': '# ' + lines[0] + '\n' + ''.join(l + '\n' for l in lines[1:])}
    return out


def main():
    units, order, heads = parse.parse_body()
    amend, tail = parse.parse_appendix()
    m = re.search(r'تضاف مادة جديدة تحت رقم\s*\)\s*(\d+)\s*[: ]*مكرر\s*[)(]\s*ويكون نصها كما يلي\s*-?\s*\n(.*?)\nالمادة الثالثة', tail, re.S)
    new290 = fix(m.group(2))
    rep = re.search(r'تلغى المواد(.*?)\nالمادة الرابعة', tail, re.S)
    nums = re.findall(r'\d+', re.sub(r'\s+', ' ', rep.group(1)))
    assert [int(x) for x in nums] == [229, 236, 388, 391, 541, 543, 921, 1109], nums
    repealed = list(range(229, 237)) + list(range(388, 392)) + [541, 543, 921, 1109]
    v1 = dict(units)
    v1.update(head_units(order, heads))
    changes, credits = {}, {}
    law = 'law-6-2016'
    for k, text in amend.items():
        old = units[k]['text'].split('\n')
        body = text.rstrip('\n').split('\n')[1:]
        if len(body) > 1 and not PARA_RE.match(body[0]) and not LET_RE.match(body[0]) and PARA_RE.match(body[1]):
            body = body[1:]    # the amendment prints the caption on its own line; keep the Code's caption
        new = '\n'.join([old[0]] + [fix(b) for b in body]) + '\n'
        changes[k] = {'label': units[k]['label'], 'kind': 'art', 'text': new}
        credits[k] = [law]
    changes['art-0290-bis'] = {'label': 'المادة 290 مكرر', 'kind': 'art', 'text': '# المادة 290 مكرر\n' + new290 + '\n'}
    credits['art-0290-bis'] = [law]
    for n in repealed:
        assert 'art-%04d' % n in units
        changes['art-%04d' % n] = None
        credits['art-%04d' % n] = [law]
    corpus = {
        'country': {
            'code': 'LY', 'name': 'Libya', 'slug': 'libya', 'lang': 'ar', 'tz': 'Africa/Tripoli', 'future_branch': 'future',
            'publisher': {'name': 'Ministry of Justice of Libya', 'email': 'moj@aladel.invalid'},
            'default_in_force_rule': {
                'text': 'Law No. 6 of 2016, art. 4: the law applies from the date of its issue.',
                'source': PAGE},
            'licence_note': 'Text published by the Ministry of Justice of Libya (aladel.gov.ly), retrieved 29 October 2026. Official legislation; the Ministry site carries only a general "all rights reserved" footer and states no reuse terms.',
        },
        'sources': [{
            'name': 'Ministry of Justice of Libya, Civil Code volume (PDF, 14 April 2016)',
            'url': PAGE, 'retrieved': '2026-10-29', 'requests': 1,
            'licence': 'No reuse terms stated; official legislation',
            'notes': 'One PDF of 323 pages: the Civil Code (articles 1-1151) as the Ministry prints it before Law No. 6 of 2016, followed by the text of that Law. The PDF has a text layer; no OCR.'}],
        'laws': {law: {
            'label': 'Law No. 6 of 2016', 'title': 'بشأن تعديل بعض أحكام القانون المدني', 'kind': 'law',
            'enacted': '2016-01-19', 'published': None, 'url': PAGE,
            'temporary_until': None, 'restores': None, 'note': None}},
        'acts': [{
            'slug': 'civil-code', 'short': 'CC', 'title': 'القانون المدني الليبي (Libyan Civil Code)',
            'url': PAGE, 'first_law': None, 'earlier_laws': [],
            'versions': [
                {'from': '2016-01-18', 'source_url': PDF_URL, 'sha256': SHA, 'units': v1,
                 'note': 'The Code as the Ministry prints it before Law No. 6 of 2016 (promulgated 28 November 1953, published 20 February 1954, in force 15 days after publication, with its amendments to 2015). Earlier states of the Code are not in the record.'},
                {'from': '2016-01-19', 'source_url': PDF_URL, 'sha256': SHA, 'changes': changes, 'credits': credits,
                 'note': 'Law No. 6 of 2016 (General National Congress, issued 19 January 2016): %d articles replaced, art. 290 bis added, %d articles repealed (229-236, 388-391, 541, 543, 921, 1109).' % (len(amend), len(repealed))}]}],
        'applies': [],
        'decisions': [
            'Scope: the Civil Code only (1,151 articles plus one added article), from the single PDF the Ministry of Justice publishes. Other Libyan laws on the Ministry site are separate PDFs or images and are not in this first build.',
            'The Ministry volume prints the Code as it stood before Law No. 6 of 2016 and then the text of that Law. The first version is therefore "oldest version available" (first_law null) and is dated 18 January 2016, the day before Law No. 6 took effect; the volume does not say when that earlier text took effect, and the Code itself dates from 1953-54.',
            'Law No. 6 of 2016 took effect on the date of its issue, 19 January 2016 (its art. 4), the date printed under its signature (9 Rabi II 1437 AH).',
            'The PDF prints article 870 with the number 780 (a typo in the volume, between 869 and 871); it is stored as article 870.',
            'Footnotes at the foot of the PDF pages (publication notes and cross-references) and page numbers are left out. Headings (book, part, chapter, section, sub-section) are kept as heading units placed in front of the next article.',
            'The PDF text layer was normalised: Arabic presentation forms were converted to standard letters (Unicode NFKC) and the Persian yeh and kaf glyphs to Arabic yeh and kaf. Lines were joined into paragraphs at each paragraph number or letter. Some words keep stray spaces from the PDF text layer.',
            'The repealed articles 229-236, 388-391, 541, 543, 921 and 1109 are removed files from 19 January 2016; the added article 290 bis is a new file.',
        ],
        'ai_use': ['Claude Code (Claude Sonnet 5.5) wrote the scripts. No model wrote, edited or summarised legal text, and no model runs at data-build or git-build time.'],
    }
    out = HERE / 'corpus.json'
    tmp = out.with_suffix('.tmp')
    tmp.write_text(json.dumps(corpus, ensure_ascii=False, indent=1) + '\n', encoding='utf8', newline='\n')
    tmp.replace(out)
    print('articles', len(units), 'headings', len(v1) - len(units), 'amended', len(amend), 'repealed', len(repealed))


if __name__ == '__main__':
    main()
