"""Replace [[T#]] / [[F#]] placeholder paragraphs with styled tables and inline images.
usage: python placeholders.py DOC.json content_module out.json"""
import json, sys, importlib, re
from docbuild import u16, col, pt, NAVY, TEXT

RAW = 'https://raw.githubusercontent.com/osemina/probability-and-statistics-labs/{commit}/lab07/images/{name}'


def paragraphs(doc):
    body = doc['content']['tabs'][0]['documentTab']['body']['content'] if 'content' in doc else doc['tabs'][0]['documentTab']['body']['content']
    for el in body:
        if 'paragraph' in el:
            t = ''.join(e.get('textRun', {}).get('content', '') for e in el['paragraph']['elements'])
            yield el['startIndex'], el['endIndex'], t


def table_requests(i, rows, widths, center_cols=()):
    """Insert table after the paragraph ending at i+1 (i = caption endIndex - 1)."""
    R, C = len(rows), len(rows[0])
    reqs = [{"insertTable": {"location": {"index": i}, "rows": R, "columns": C}}]
    base = lambda r, c: i + 4 + r * (2 * C + 1) + 2 * c
    cells = [(r, c) for r in range(R) for c in range(C)]
    for r, c in reversed(cells):
        if rows[r][c]:
            reqs.append({"insertText": {"location": {"index": base(r, c)}, "text": rows[r][c]}})
    # positions after fill
    shift, pos = 0, {}
    for r, c in cells:
        p = base(r, c) + shift
        pos[(r, c)] = (p, p + u16(rows[r][c]))
        shift += u16(rows[r][c])
    tstart = i + 1
    tend = pos[(R - 1, C - 1)][1] + 2
    loc = {"tableStartLocation": {"index": tstart}}
    border = {"color": col('#c9d6e3'), "width": pt(0.75), "dashStyle": "SOLID"}
    reqs.append({"updateTableCellStyle": {"tableRange": {"tableCellLocation": {**loc, "rowIndex": 0, "columnIndex": 0}, "rowSpan": R, "columnSpan": C},
                 "tableCellStyle": {"borderTop": border, "borderBottom": border, "borderLeft": border, "borderRight": border,
                                    "paddingTop": pt(4), "paddingBottom": pt(4), "paddingLeft": pt(6), "paddingRight": pt(6), "contentAlignment": "MIDDLE"},
                 "fields": "borderTop,borderBottom,borderLeft,borderRight,paddingTop,paddingBottom,paddingLeft,paddingRight,contentAlignment"}})
    reqs.append({"updateTableCellStyle": {"tableRange": {"tableCellLocation": {**loc, "rowIndex": 0, "columnIndex": 0}, "rowSpan": 1, "columnSpan": C},
                 "tableCellStyle": {"backgroundColor": col(NAVY)}, "fields": "backgroundColor"}})
    for c, w in enumerate(widths):
        reqs.append({"updateTableColumnProperties": {"tableStartLocation": {"index": tstart}, "columnIndices": [c],
                     "tableColumnProperties": {"widthType": "FIXED_WIDTH", "width": pt(w)}, "fields": "widthType,width"}})
    first, last = pos[(0, 0)][0], pos[(R - 1, C - 1)][1]
    reqs.append({"updateParagraphStyle": {"range": {"startIndex": first, "endIndex": last + 1},
                 "paragraphStyle": {"namedStyleType": "NORMAL_TEXT"}, "fields": "namedStyleType"}})
    reqs.append({"updateParagraphStyle": {"range": {"startIndex": first, "endIndex": last + 1},
                 "paragraphStyle": {"spaceAbove": pt(0), "spaceBelow": pt(0), "lineSpacing": 115, "alignment": "START", "keepWithNext": False,
                                    "indentStart": pt(0), "indentFirstLine": pt(0)},
                 "fields": "spaceAbove,spaceBelow,lineSpacing,alignment,keepWithNext,indentStart,indentFirstLine"}})
    reqs.append({"updateTextStyle": {"range": {"startIndex": first, "endIndex": last},
                 "textStyle": {"weightedFontFamily": {"fontFamily": "Georgia", "weight": 400}, "fontSize": pt(10), "foregroundColor": col(TEXT), "bold": False},
                 "fields": "weightedFontFamily,fontSize,foregroundColor,bold"}})
    hs, he = pos[(0, 0)][0], pos[(0, C - 1)][1]
    reqs.append({"updateTextStyle": {"range": {"startIndex": hs, "endIndex": he},
                 "textStyle": {"weightedFontFamily": {"fontFamily": "Montserrat", "weight": 600}, "fontSize": pt(9.5), "foregroundColor": col('#ffffff'), "bold": True},
                 "fields": "weightedFontFamily,fontSize,foregroundColor,bold"}})
    for r in range(R):
        for c in center_cols:
            a, b = pos[(r, c)]
            reqs.append({"updateParagraphStyle": {"range": {"startIndex": a, "endIndex": b + 1}, "paragraphStyle": {"alignment": "CENTER"}, "fields": "alignment"}})
    return reqs


def build(docpath, modname, commit):
    doc = json.load(open(docpath, encoding='utf8'))
    mod = importlib.import_module(modname)
    paras = list(paragraphs(doc))
    reqs = []
    for k, (s, e, t) in reversed(list(enumerate(paras))):
        m = re.fullmatch(r'\[\[(\w+)\]\]\n', t)
        if not m:
            continue
        key = m.group(1)
        if key.startswith('F'):
            name, w, h = mod.FIGURES[key]
            reqs.append({"deleteContentRange": {"range": {"startIndex": s, "endIndex": e - 1}}})
            reqs.append({"insertInlineImage": {"location": {"index": s}, "uri": RAW.format(commit=commit, name=name),
                                               "objectSize": {"width": pt(w), "height": pt(h)}}})
        else:
            spec = mod.TABLES[key]
            rows, widths, cc = spec['rows'], spec['widths'], spec.get('center', ())
            reqs.append({"deleteContentRange": {"range": {"startIndex": s, "endIndex": e}}})
            reqs.extend(table_requests(s - 1, rows, widths, cc))
    return reqs, doc['content']['revisionId'] if 'content' in doc else doc['revisionId']


if __name__ == '__main__':
    reqs, rev = build(sys.argv[1], sys.argv[2], sys.argv[3])
    json.dump({"requests": reqs, "rev": rev}, open(sys.argv[4], 'w', encoding='utf8'), ensure_ascii=False, separators=(',', ':'))
    print(len(reqs), rev, len(json.dumps(reqs, ensure_ascii=False, separators=(',', ':'))))
