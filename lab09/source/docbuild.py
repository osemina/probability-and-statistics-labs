"""Block -> Google Docs requests builder for Lab 7, in the Lab 6 house style
(Arial, justified body, H1 20pt bold with grey bottom rule, H2 15pt bold, gold/red left-border boxes on #f7f7f5,
 captions 9.5pt with bold label, tables with grey header). Markup: **bold**. Paragraphs that start with
 **Example:** become gold boxes. ('table'|'figure', key) become '[[key]]' placeholder paragraphs.
 List kinds: 'ul' bullets, 'ol' 1. 2. 3., 'al' a) b) c) (created at nesting level 1 with a leading tab)."""
import re


def rgb(h):
    h = h.lstrip('#')
    return {"red": round(int(h[0:2], 16) / 255, 4), "green": round(int(h[2:4], 16) / 255, 4), "blue": round(int(h[4:6], 16) / 255, 4)}


GOLD, RED, GREY, SHADE, GREEN = '#c3a45d', '#b3473a', '#e6e6e6', '#f7f7f5', '#1c7d3b'
def u16(s): return len(s.encode('utf-16-le')) // 2
def col(h): return {"color": {"rgbColor": rgb(h)}}
def pt(x): return {"magnitude": x, "unit": "PT"}


BOXCOL = {'tip': GOLD, 'note': GOLD, 'ex': GOLD, 'mistake': RED}
RESET = ['shading', 'borderLeft', 'borderTop', 'borderBottom', 'borderRight', 'indentEnd', 'pageBreakBefore', 'indentStart', 'indentFirstLine']


SUBS = []   # filled by parse(): (start, end) subscript spans of the last parsed text


def parse(t):
    """**bold** and _{subscript}. Returns plain text and bold spans; subscript spans are appended to SUBS."""
    out, spans, bold_start = '', [], None
    del SUBS[:]
    for tok in re.split(r'(\*\*|_\{[^}]*\})', t):
        if tok == '**':
            if bold_start is None:
                bold_start = u16(out)
            else:
                spans.append((bold_start, u16(out)))
                bold_start = None
        elif tok.startswith('_{') and tok.endswith('}'):
            s = u16(out)
            out += tok[2:-1]
            SUBS.append((s, u16(out)))
        else:
            out += tok
    return out, spans + [('sub', a, b) for a, b in SUBS]


def build(blocks, at, first_page_break=True, leading_newline=True):
    paras = []
    for b in blocks:
        k = b[0]
        if k in ('h1', 'h2', 'p', 'cap', 'box', 'eq', 'ans'):
            t, sp = (b[-1], []) if k == 'eq' else parse(b[-1])
            ex = b[1] if k == 'box' else None
            if k == 'p' and b[-1].startswith('**Example:**'):
                k, ex = 'box', 'ex'
            if k == 'cap':
                ex = 'fig' if t.startswith('Figure') else 'tab'
            paras.append((t, k, ex, sp))
        elif k in ('ul', 'ol', 'al'):
            for j, it in enumerate(b[1]):
                if k == 'al':   # lettered sub-items as text, laid out like the Lab 6 a) b) c) lists
                    it = 'abcdefgh'[j] + ')	' + it
                t, sp = parse(it)
                paras.append((t, k, ('last' if j == len(b[1]) - 1 else 'mid', id(b)), sp))
        elif k in ('table', 'figure'):
            paras.append((f'[[{b[1]}]]', 'ph', k, []))
    text = '\n'.join(p[0] for p in paras)
    if leading_newline:
        R = [{"insertText": {"location": {"index": at}, "text": '\n' + text}}]
        pos = at + 1
    else:
        R = [{"insertText": {"location": {"index": at}, "text": text}}]
        pos = at
    start = pos
    ranges = []
    for t, k, ex, sp in paras:
        s, e = pos, pos + u16(t) + 1
        ranges.append((s, e, t, k, ex, sp))
        pos = e
    end = pos
    R.append({"updateParagraphStyle": {"range": {"startIndex": start, "endIndex": end}, "paragraphStyle": {"namedStyleType": "NORMAL_TEXT"}, "fields": "namedStyleType"}})
    R.append({"deleteParagraphBullets": {"range": {"startIndex": start, "endIndex": end}}})   # text appended after a list inherits its bullets
    for s, e, t, k, ex, sp in ranges:
        if k in ('h1', 'h2'):
            R.append({"updateParagraphStyle": {"range": {"startIndex": s, "endIndex": e}, "paragraphStyle": {"namedStyleType": 'HEADING_1' if k == 'h1' else 'HEADING_2'}, "fields": "namedStyleType"}})
    R.append({"updateTextStyle": {"range": {"startIndex": start, "endIndex": end - 1},
              "textStyle": {"weightedFontFamily": {"fontFamily": "Arial", "weight": 400}, "fontSize": pt(11), "bold": False, "italic": False, "underline": False},
              "fields": "weightedFontFamily,fontSize,bold,italic,underline,foregroundColor,backgroundColor,link,baselineOffset"}})
    TS, first_h1 = [], True
    for s, e, t, k, ex, sp in ranges:
        ps = {"lineSpacing": 115, "spaceAbove": pt(0), "spaceBelow": pt(8), "alignment": "JUSTIFIED", "keepWithNext": False}
        if k == 'h1':
            ps.update(spaceAbove=pt(24), spaceBelow=pt(14), keepWithNext=True, alignment="START",
                      borderBottom={"color": col(GREY), "width": pt(1), "padding": pt(6), "dashStyle": "SOLID"})
            if first_h1 and first_page_break:
                ps.update(pageBreakBefore=True, spaceAbove=pt(0))
            first_h1 = False
            TS.append({"updateTextStyle": {"range": {"startIndex": s, "endIndex": e - 1}, "textStyle": {"bold": True, "fontSize": pt(20)}, "fields": "bold,fontSize"}})
        elif k == 'h2':
            ps.update(spaceAbove=pt(22), spaceBelow=pt(6), keepWithNext=True, alignment="START")
            TS.append({"updateTextStyle": {"range": {"startIndex": s, "endIndex": e - 1}, "textStyle": {"bold": True, "fontSize": pt(15)}, "fields": "bold,fontSize"}})
        elif k == 'cap':
            if ex == 'tab':
                ps.update(lineSpacing=110, spaceBelow=pt(0), keepWithNext=True, alignment="START")
            else:
                ps.update(spaceAbove=pt(6), spaceBelow=pt(12), alignment="START")
            TS.append({"updateTextStyle": {"range": {"startIndex": s, "endIndex": e - 1}, "textStyle": {"fontSize": pt(9.5)}, "fields": "fontSize"}})
            m = re.match(r'(Table|Figure) \d+\.', t)
            if m:
                TS.append({"updateTextStyle": {"range": {"startIndex": s, "endIndex": s + u16(m.group(0))}, "textStyle": {"bold": True}, "fields": "bold"}})
        elif k == 'box':
            ps.update(spaceAbove=pt(6), spaceBelow=pt(6), shading={"backgroundColor": col(SHADE)},
                      borderLeft={"color": col(BOXCOL[ex]), "width": pt(3), "padding": pt(10), "dashStyle": "SOLID"})
        elif k in ('ul', 'ol'):
            ps.update(spaceBelow=pt(4), alignment="START")
        elif k == 'al':
            ps.update(spaceBelow=pt(4), alignment="START", indentStart=pt(72), indentFirstLine=pt(54))
        elif k == 'eq':
            ps.update(alignment="CENTER", spaceAbove=pt(4), spaceBelow=pt(8))
        elif k == 'ans':   # green bold answer line (Solutions)
            TS.append({"updateTextStyle": {"range": {"startIndex": s, "endIndex": e - 1}, "textStyle": {"bold": True, "foregroundColor": col(GREEN)}, "fields": "bold,foregroundColor"}})
        elif k == 'ph':
            ps.update(alignment="CENTER", spaceAbove=pt(6), spaceBelow=pt(0), keepWithNext=(ex == 'figure'))
        f = ','.join(list(ps.keys()) + [x for x in RESET if x not in ps and not (k in ('ul', 'ol') and x.startswith('indent'))])
        prev = R[-1].get("updateParagraphStyle") if R else None
        if prev and prev["paragraphStyle"] == ps and prev["fields"] == f and prev["range"]["endIndex"] == s and k != 'box':
            prev["range"]["endIndex"] = e
        else:
            R.append({"updateParagraphStyle": {"range": {"startIndex": s, "endIndex": e}, "paragraphStyle": ps, "fields": f}})
        for span in sp:
            if span[0] == 'sub':
                TS.append({"updateTextStyle": {"range": {"startIndex": s + span[1], "endIndex": s + span[2]}, "textStyle": {"baselineOffset": "SUBSCRIPT"}, "fields": "baselineOffset"}})
            else:
                a, b = span
                TS.append({"updateTextStyle": {"range": {"startIndex": s + a, "endIndex": s + b}, "textStyle": {"bold": True}, "fields": "bold"}})
    R.extend(TS)
    runs = []
    for s, e, t, k, ex, sp in ranges:
        if k in ('ul', 'ol'):
            if runs and runs[-1][3] == ex[1]:
                runs[-1][1] = e
            else:
                runs.append([s, e, k, ex[1]])
    PRESET = {'ul': 'BULLET_DISC_CIRCLE_SQUARE', 'ol': 'NUMBERED_DECIMAL_ALPHA_ROMAN', 'al': 'NUMBERED_DECIMAL_ALPHA_ROMAN_PARENS'}
    for s, e, k, _ in runs:
        R.append({"createParagraphBullets": {"range": {"startIndex": s, "endIndex": e}, "bulletPreset": PRESET[k]}})
    return R, text, end
