"""Block -> Google Docs requests builder for Lab 7 (IBU Lab Document Template style).
Markup inside text: **bold**.  Placeholders: ('table', key) and ('figure', key) become a paragraph '[[key]]'."""
import re, json

def rgb(h):
    h = h.lstrip('#'); return {"red": round(int(h[0:2], 16)/255, 3), "green": round(int(h[2:4], 16)/255, 3), "blue": round(int(h[4:6], 16)/255, 3)}
NAVY, GOLD, YEL, TEXT, MUTED, RED, BLUE = '#003e67', '#c3a45d', '#f5c400', '#202020', '#5f6368', '#b34739', '#1f5f99'
BOX = {'tip': ('#fbf6ea', GOLD), 'mistake': ('#fbeeec', RED), 'note': ('#eef2f6', NAVY)}

def u16(s): return len(s.encode('utf-16-le')) // 2
def col(h): return {"color": {"rgbColor": rgb(h)}}
def pt(x): return {"magnitude": x, "unit": "PT"}

def parse(t):
    """returns plain text and list of (start,end) bold spans (utf16 offsets)"""
    out, spans, pos = '', [], 0
    for i, part in enumerate(re.split(r'\*\*', t)):
        if i % 2 == 1: spans.append((u16(out), u16(out) + u16(part)))
        out += part
    return out, spans

def build(blocks, at, first_page_break=True):
    """blocks: list of tuples. Returns (requests, text). Text inserted at index `at` starting with '\n'."""
    paras = []  # (text, kind, extra, boldspans)
    for b in blocks:
        k = b[0]
        if k in ('h1', 'h2', 'p', 'cap', 'box', 'eq'):
            txt = b[-1]
            t, sp = parse(txt)
            paras.append((t, k, b[1] if k == 'box' else None, sp))
        elif k in ('ul', 'ol'):
            items = b[1]
            for j, it in enumerate(items):
                t, sp = parse(it)
                paras.append((t, k, ('last' if j == len(items) - 1 else 'mid', id(b)), sp))
        elif k in ('table', 'figure'):
            paras.append((f'[[{b[1]}]]', 'ph', None, []))
    text = '\n' + '\n'.join(p[0] for p in paras)
    R = [{"insertText": {"location": {"index": at}, "text": text}}]
    pos = at + 1
    ranges = []
    for t, k, ex, sp in paras:
        s, e = pos, pos + u16(t) + 1
        ranges.append((s, e, t, k, ex, sp)); pos = e
    end = pos
    # 1) named styles
    R.append({"updateParagraphStyle": {"range": {"startIndex": at + 1, "endIndex": end}, "paragraphStyle": {"namedStyleType": "NORMAL_TEXT"}, "fields": "namedStyleType"}})
    for s, e, t, k, ex, sp in ranges:
        if k in ('h1', 'h2'):
            R.append({"updateParagraphStyle": {"range": {"startIndex": s, "endIndex": e}, "paragraphStyle": {"namedStyleType": 'HEADING_1' if k == 'h1' else 'HEADING_2'}, "fields": "namedStyleType"}})
    # 2) base text style
    R.append({"updateTextStyle": {"range": {"startIndex": at + 1, "endIndex": end - 1},
              "textStyle": {"weightedFontFamily": {"fontFamily": "Georgia", "weight": 400}, "fontSize": pt(11), "foregroundColor": col(TEXT),
                            "bold": False, "italic": False, "underline": False, "backgroundColor": {}},
              "fields": "weightedFontFamily,fontSize,foregroundColor,bold,italic,underline,backgroundColor,link"}})
    # 3) per-paragraph styles
    first_h1 = True
    TS = []
    for s, e, t, k, ex, sp in ranges:
        ps, f = {"lineSpacing": 125, "spaceAbove": pt(0), "spaceBelow": pt(8), "alignment": "START", "indentStart": pt(0), "indentFirstLine": pt(0), "keepWithNext": False}, None
        if k == 'h1':
            ps.update(spaceAbove=pt(22), spaceBelow=pt(12), lineSpacing=100, keepWithNext=True,
                      borderBottom={"color": col(GOLD), "width": pt(1.5), "padding": pt(4), "dashStyle": "SOLID"})
            if first_h1 and first_page_break: ps['pageBreakBefore'] = True; first_h1 = False
            TS.append({"updateTextStyle": {"range": {"startIndex": s, "endIndex": e - 1}, "textStyle": {"weightedFontFamily": {"fontFamily": "Montserrat", "weight": 700}, "fontSize": pt(20), "foregroundColor": col(NAVY), "bold": True}, "fields": "weightedFontFamily,fontSize,foregroundColor,bold"}})
        elif k == 'h2':
            ps.update(spaceAbove=pt(14), spaceBelow=pt(6), lineSpacing=100, keepWithNext=True)
            TS.append({"updateTextStyle": {"range": {"startIndex": s, "endIndex": e - 1}, "textStyle": {"weightedFontFamily": {"fontFamily": "Montserrat", "weight": 600}, "fontSize": pt(13.5), "foregroundColor": col(NAVY), "bold": True}, "fields": "weightedFontFamily,fontSize,foregroundColor,bold"}})
        elif k == 'cap':
            ps.update(spaceAbove=pt(6), spaceBelow=pt(6), keepWithNext=True)
            TS.append({"updateTextStyle": {"range": {"startIndex": s, "endIndex": e - 1}, "textStyle": {"fontSize": pt(9.5), "foregroundColor": col(MUTED)}, "fields": "fontSize,foregroundColor"}})
        elif k == 'box':
            bg, bc = BOX[ex]
            ps.update(spaceAbove=pt(6), spaceBelow=pt(12), indentStart=pt(10), indentFirstLine=pt(10), indentEnd=pt(4),
                      shading={"backgroundColor": col(bg)},
                      borderLeft={"color": col(bc), "width": pt(3), "padding": pt(9), "dashStyle": "SOLID"},
                      borderTop={"color": col(bg), "width": pt(0.5), "padding": pt(6), "dashStyle": "SOLID"},
                      borderBottom={"color": col(bg), "width": pt(0.5), "padding": pt(6), "dashStyle": "SOLID"},
                      borderRight={"color": col(bg), "width": pt(0.5), "padding": pt(6), "dashStyle": "SOLID"})
            TS.append({"updateTextStyle": {"range": {"startIndex": s, "endIndex": e - 1}, "textStyle": {"fontSize": pt(10.5)}, "fields": "fontSize"}})
        elif k in ('ul', 'ol'):
            ps.update(spaceBelow=pt(8 if ex[0] == 'last' else 3))
        elif k == 'eq':
            ps.update(alignment="CENTER", spaceAbove=pt(4), spaceBelow=pt(10))
            TS.append({"updateTextStyle": {"range": {"startIndex": s, "endIndex": e - 1}, "textStyle": {"fontSize": pt(12.5), "foregroundColor": col(NAVY), "bold": True}, "fields": "fontSize,foregroundColor,bold"}})
        elif k == 'ph':
            ps.update(alignment="CENTER", spaceBelow=pt(4))
        f = ','.join(ps.keys())
        prev = R[-1].get("updateParagraphStyle") if R else None
        if prev and prev["paragraphStyle"] == ps and prev["range"]["endIndex"] == s and k not in ('box',):
            prev["range"]["endIndex"] = e
        else:
            R.append({"updateParagraphStyle": {"range": {"startIndex": s, "endIndex": e}, "paragraphStyle": ps, "fields": f}})
        for a, b in sp:
            TS.append({"updateTextStyle": {"range": {"startIndex": s + a, "endIndex": s + b}, "textStyle": {"bold": True}, "fields": "bold"}})
        if k == 'cap':
            m = re.match(r'(Table|Figure) \d+\.', t)
            if m: TS.append({"updateTextStyle": {"range": {"startIndex": s, "endIndex": s + u16(m.group(0))}, "textStyle": {"bold": True, "foregroundColor": col(NAVY)}, "fields": "bold,foregroundColor"}})
        if k == 'box':
            m = re.match(r'[^:]{1,30}:', t)
            if m and (0, u16(m.group(0))) in [(a, b) for a, b in sp]:
                TS.append({"updateTextStyle": {"range": {"startIndex": s, "endIndex": s + u16(m.group(0))}, "textStyle": {"foregroundColor": col(RED if ex == 'mistake' else NAVY)}, "fields": "foregroundColor"}})
    R.extend(TS)
    # 4) lists (contiguous runs)
    runs = []
    for s, e, t, k, ex, sp in ranges:
        if k in ('ul', 'ol'):
            if runs and runs[-1][3] == ex[1]: runs[-1][1] = e
            else: runs.append([s, e, k, ex[1]])
    for s, e, k, _ in runs:
        R.append({"createParagraphBullets": {"range": {"startIndex": s, "endIndex": e}, "bulletPreset": "NUMBERED_DECIMAL_ALPHA_ROMAN" if k == 'ol' else "BULLET_DISC_CIRCLE_SQUARE"}})
    return R, text, end
