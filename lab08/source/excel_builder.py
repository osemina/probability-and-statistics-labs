"""Workbook builder for Lab 8 (copied from Lab 6), modelled on the original Lab 6 workbooks:
task on top, SOLUTION (Manually) on the LEFT (text + formula pictures), SOLUTION (Excel) on the RIGHT
(explanations + blue/yellow cells; yellow cells empty in the Students workbook), chart picture at the end."""
import math, os, re
import xlsxwriter
from PIL import Image
import xl_images as XI

NAVY, BLUE, GOLD, MUTED, GREEN = '#003E67', '#1F5F99', '#C39A3D', '#5F6368', '#1C7D3A'
INPUT, GIVEN, HEAD = '#FFF2CC', '#DDEBF7', '#003E67'
BOX_TASK, BOX_HELP, BOX_LINE, BOX_RED = '#FFFFFF', '#F3F6F9', '#C9D6E3', '#B34739'
PX_ROW = 20
LW, RW = 800, 470          # widths of the left (manual) and right (Excel) columns in px
LCH, RCH = 125, 72         # characters per line in the left / right text boxes
FCOUNT = [0]


def lines(text, ch):
    return sum(max(1, math.ceil(len(t) / ch)) for t in text.split('\n'))


def box_h(text, ch, extra=22):
    return lines(text, ch) * 15 + extra


def plain(s):
    s = re.sub(r'_\{([^}]+)\}', r'\1', s)
    return s.replace('**', '').replace('!!', '')


def ref(r, c):
    return xlsxwriter.utility.xl_rowcol_to_cell(r, c, row_abs=True, col_abs=True)


def build(solutions, T, FIG, NAME, OUT):
    fn = os.path.join(OUT, f'{NAME} – {"Solutions" if solutions else "Students"}.xlsx')
    wb = xlsxwriter.Workbook(fn, {'use_future_functions': True})
    wb.set_properties({'title': f'{NAME} – {"Solutions" if solutions else "Students"}', 'author': 'Emina Osmić'})
    F = lambda **k: wb.add_format(dict({'font_name': 'Arial', 'font_size': 10, 'valign': 'vcenter'}, **k))
    f_title = F(bold=True, font_size=16, font_color=NAVY)
    f_focus = F(italic=True, font_color=MUTED)
    f_sec = F(bold=True, font_size=11, font_color=NAVY, bottom=2, bottom_color=GOLD)
    f_lab = F(border=1, border_color=BOX_LINE, bg_color=GIVEN)
    f_head = F(bold=True, font_color='#FFFFFF', bg_color=HEAD, border=1, border_color=HEAD, align='center')
    f_tag = F(bold=True, font_size=8, font_color=GOLD, align='center')
    f_ans = F(bg_color=INPUT, border=1, border_color=GOLD, text_wrap=True, valign='top')
    num = {}

    def fmt(kind, nf):
        key = (kind, nf)
        if key not in num:
            base = dict(num_format=nf, border=1, align='center')
            if kind == 'given': base.update(bg_color='#FFFFFF', border_color='#9DC3E6')
            elif kind == 'input': base.update(bg_color=INPUT, border_color=GOLD)
            num[key] = F(**base)
        return num[key]

    def setup(ws):
        ws.set_column('A:A', 2); ws.set_column('B:F', 12); ws.set_column('G:G', 52); ws.set_column('H:H', 2); ws.set_column('I:N', 12)

    def textbox(ws, row, col, text, width, h, fill=BOX_TASK, line=BOX_LINE, bold=False, color='#202020', size=10):
        ws.insert_textbox(row, col, text, {'width': width, 'height': h, 'x_offset': 2, 'y_offset': 3,
                                           'font': {'name': 'Arial', 'size': size, 'color': color, 'bold': bold},
                                           'align': {'vertical': 'top'}, 'fill': {'color': fill},
                                           'line': {'color': line, 'width': 1}, 'object_position': 1})
        return math.ceil((h + 8) / PX_ROW)

    def picture(ws, row, col, path, scale=1.0, xo=8):
        w, h = Image.open(path).size
        ws.insert_image(row, col, path, {'x_offset': xo, 'y_offset': 2, 'x_scale': scale, 'y_scale': scale, 'object_position': 1})
        return math.ceil((h * scale + 6) / PX_ROW)

    # ---------------- Start sheet
    ws = wb.add_worksheet('Start'); setup(ws)
    ws.write('B2', NAME + (' – SOLUTIONS' if solutions else ''), f_title)
    ws.write('B3', 'FENMS 0021 Probability and Statistics  ·  International Burch University', f_focus)
    intro = ("HOW TO USE THIS WORKBOOK\n"
             "Each task has its own sheet. Under the task the solution goes step by step:\n"
             "•  first the manual calculation, with the formula and the numbers;\n"
             "•  then the same step in Excel: yellow cells, and a blue box that tells you which function to use.\n"
             "Tips are on the RIGHT, next to the step they explain. Every sheet ends with a chart of the result.\n\n"
             "Every task follows the five steps of a hypothesis test: hypotheses, α and the critical value, test statistic, p-value, decision.\n"
             "Work through Tasks 1–6 in order. Tasks 7–10 are extra practice if you have time left.\n\n"
             + ("This is the SOLUTIONS workbook: every yellow cell contains the formula used. Click a cell and read the formula bar."
                if solutions else "Type a formula (starting with =) in every yellow cell and compare your results with the manual calculation above it."))
    r = 4 + textbox(ws, 4, 1, intro, LW, box_h(intro, LCH, 26)) + 1
    ws.write(r, 1, 'Cell colours', f_sec)
    ws.write(r + 1, 1, '', fmt('given', '0')); ws.write(r + 1, 2, 'given data (do not change)', F())
    ws.write(r + 2, 1, '', fmt('input', '0')); ws.write(r + 2, 2, 'YOUR FORMULA / RESULT', F(bold=True))
    ws.write(r + 3, 1, '', f_ans); ws.write(r + 3, 2, 'YOUR INTERPRETATION (write in words)', F(bold=True))
    r1 = r + 6
    ws.write(r1, 1, 'Standard symbols', f_sec)
    sym = [('Concept', 'Symbol', 'Meaning'), ('Two groups', 'X and Y', 'the first and the second sample / population'),
           ('Paired differences', 'd, d̄, sd', 'd = y − x for each pair, their mean and SD'),
           ('Pooled variance', 'sp²', 'one common variance for the pooled t-test'),
           ('Welch degrees of freedom', 'ν', 'df of Welch’s t-test (may be a decimal)'),
           ('Pooled proportion', 'p₀', '(xX + xY) / (nX + nY)'),
           ('F statistic', 'F, v₁, v₂', 'sX² / sY², v₁ = nX − 1, v₂ = nY − 1')]
    fl = F(border=1, border_color=BOX_LINE)
    for i, (a, b, c) in enumerate(sym):
        f = f_head if i == 0 else fl
        ws.merge_range(r1 + 1 + i, 1, r1 + 1 + i, 2, '', f); ws.write_string(r1 + 1 + i, 1, a, f)
        ws.merge_range(r1 + 1 + i, 3, r1 + 1 + i, 4, '', f); ws.write_string(r1 + 1 + i, 3, b, f)
        ws.merge_range(r1 + 1 + i, 5, r1 + 1 + i, 6, '', f); ws.write_string(r1 + 1 + i, 5, c, f)
    r2 = r1 + 9
    ws.write(r2, 1, 'Excel functions for this lab', f_sec)
    funcs = [('Function', 'What it returns'), ('=AVERAGE(range), =STDEV.S(range)', 'd̄ and s_d of the paired differences'),
             ('=NORM.S.INV(1 − α), =NORM.S.INV(1 − α/2)', 'critical value of a one- / two-tailed z-test'),
             ('=NORM.S.DIST(z, TRUE)', 'P(Z ≤ z); use 1 − … for the right tail'),
             ('=T.INV(1 − α, df), =T.INV.2T(α, df)', 'critical value of a one- / two-tailed t-test'),
             ('=T.DIST.RT(t, df), =T.DIST(t, df, TRUE)', 'p-value of a right- / left-tailed t-test'),
             ('=T.DIST.2T(|t|, df)', 'p-value of a two-tailed t-test'),
             ('=F.INV.RT(α, v₁, v₂), =F.INV(α, v₁, v₂)', 'upper / lower critical value of the F-test'),
             ('=F.DIST.RT(F, v₁, v₂), =F.DIST(F, v₁, v₂, TRUE)', 'p-value of a right- / left-tailed F-test'),
             ('=SQRT(x)', 'square root, for the standard errors')]
    for i, (a, b) in enumerate(funcs):
        f = f_head if i == 0 else fl
        ws.merge_range(r2 + 1 + i, 1, r2 + 1 + i, 4, '', f); ws.write_string(r2 + 1 + i, 1, a, f)
        ws.merge_range(r2 + 1 + i, 5, r2 + 1 + i, 7, '', f); ws.write_string(r2 + 1 + i, 5, b, f)
    r3 = r2 + len(funcs) + 2
    ws.write(r3, 1, 'Tasks', f_sec)
    for i, t in enumerate(T):
        ws.write_url(r3 + 1 + i, 1, f"internal:'{t['sheet']}'!A1", F(font_color=BLUE, underline=1), t['title'])
    ws.activate(); ws.set_landscape(); ws.fit_to_pages(1, 1); ws.set_paper(9); ws.print_area(0, 0, r3 + 12, 9)

    # ---------------- task sheets: step by step (manual -> formula -> Excel cells), tips on the right
    import steps as STP
    import typed as TY
    f_code = F(font_name='Consolas', font_color=NAVY, border=1, border_color=BOX_LINE, bg_color='#F7F9FC')
    f_tag2 = F(bold=True, font_size=8, font_color=GOLD)
    f_cell = F(border=1, border_color=BOX_LINE, bg_color=GIVEN)
    for k, t in enumerate(T, start=1):
        ws = wb.add_worksheet(t['sheet']); setup(ws)
        ws.write('B2', t['title'], f_title)
        ws.write('B3', 'Learning focus:  ' + t['focus'], f_focus)
        row = 4 + textbox(ws, 4, 1, t['task'], LW + RW + 30, box_h(t['task'], 150, 26), line=NAVY) + 1
        names, rng, ans = {}, {}, {}
        for blk in t['blocks']:
            if blk[0] == 'answers':
                for a in blk[1]: ans[a[0]] = a
        ws.write(row, 1, f'SOLUTION {k}.', f_sec)
        ws.write(row, 8, 'TIPS', f_sec); row += 1
        # given data
        for blk in t['blocks']:
            if blk[0] == 'params':
                for key, label, val, nf in blk[1]:
                    ws.merge_range(row, 1, row, 4, label, f_cell)
                    ws.write_number(row, 5, val, fmt('given', nf)); names[key] = ref(row, 5); row += 1
                row += 1
            elif blk[0] == 'data':
                heads, rows_, nfs, keys = blk[1], blk[2], blk[3], blk[4]
                for j2, h in enumerate(heads): ws.write(row, 1 + j2, h, f_head)
                row += 1; r_first = row
                for rr_ in rows_:
                    for j2, v in enumerate(rr_): ws.write_number(row, 1 + j2, v, fmt('given', nfs[j2]))
                    row += 1
                rel = lambda r_, c_: xlsxwriter.utility.xl_rowcol_to_cell(r_, c_)
                for j2, kk in enumerate(keys): rng[kk] = f'{rel(r_first, 1 + j2)}:{rel(row - 1, 1 + j2)}'
                rng['_all'] = f'{rel(r_first, 1)}:{rel(row - 1, len(heads))}'
                row += 1

        def sub(s_):
            return re.sub(r'\{([^{}]+)\}', lambda m: names.get(m.group(1)) or rng[m.group(1)], s_)
        for st in STP.STEPS[k]:
            start = row
            if st['text']:
                txt_ = re.sub(r'([nsxσ])_([XY])', lambda m: m.group(1) + m.group(2), st['text'])
                row += textbox(ws, row, 1, txt_, LW, box_h(txt_, LCH, 18))
            for tex in st['f']:
                FCOUNT[0] += 1
                p, w, h = XI.formula(f'm{FCOUNT[0]:03d}', tex, size=15)
                row += picture(ws, row, 1, p, min(1.0, (LW - 40) / w), xo=30)
            cells = [c for c in st['cells'] if c in ans]
            if cells:
                ws.write(row, 5, 'EXCEL', f_tag); ws.write(row, 6, 'TYPE THIS IN THE YELLOW CELL', f_tag2); row += 1
                for c in cells:
                    key, label, fm, val, nf = ans[c]
                    ws.merge_range(row, 1, row, 4, label, f_cell)
                    typed = re.sub(r'\{([^{}]+)\}', lambda m: rng[m.group(1)], TY.TYPED[k][key])
                    if solutions: ws.write_formula(row, 5, typed, fmt('input', nf), val)
                    else: ws.write_blank(row, 5, None, fmt('input', nf))
                    ws.write_string(row, 6, typed, f_code)
                    names[key] = ref(row, 5); row += 1
            if st['xl']:
                row += textbox(ws, row, 1, st['xl'], LW, box_h(st['xl'], LCH, 12), fill='#EAF2FA', line='#9DC3E6', color=NAVY)
            if st['ans']:
                row += textbox(ws, row, 1, st['ans'], LW, box_h(st['ans'], LCH - 8, 14), fill='#F1F8F3', line='#9CCBA8', color=GREEN, bold=True)
            if st['tip']:
                th_ = box_h(st['tip'], RCH, 18)
                end = start + textbox(ws, start, 8, st['tip'], RW, th_, fill='#F7F7F5', line=BOX_RED if st['tipred'] else GOLD)
                row = max(row, end)
            row += 1
        if solutions:
            row += textbox(ws, row, 1, 'SOLUTION: click a yellow cell to see the formula in the formula bar.', LW, 28, fill=BOX_HELP, color=NAVY)
        row += 1
        ws.write(row, 1, 'Chart of the result', f_sec); row += 1
        row += picture(ws, row, 1, FIG[t['fig']], 1.0) + 2
        ws.set_landscape(); ws.fit_to_pages(1, 0); ws.set_paper(9)
        ws.print_area(0, 0, row, 15)
    wb.close()
    return fn
