# -*- coding: utf-8 -*-
"""Lab 9 workbooks (Students / Solutions), modelled on the original "Lab 9 for Students / with Solutions" files:
task on top, data table, how to run Data Analysis -> Regression, the Regression output (Solutions) or an empty
area for it (Students), the scatter chart, then one box per question (answers in Solutions, blanks in Students).
Headings and colours follow the Lab 6-8 workbooks."""
import math, os, re, sys
import numpy as np
from scipy import stats
import xlsxwriter
from PIL import Image
import xl_images as XI
import sol
import part4, part5, part6, part7, part8, part9, part10, part11

NAVY, BLUE, GOLD, MUTED, GREEN, RED = '#003E67', '#1F5F99', '#C39A3D', '#5F6368', '#1C7D3A', '#B34739'
INPUT, GIVEN, HEAD = '#FFF2CC', '#DDEBF7', '#003E67'
BOX_LINE, BOX_HELP = '#C9D6E3', '#F3F6F9'
PX_ROW = 20
LW, RW = 860, 440
LCH, RCH = 135, 66
NAME = 'Lab 9 – Simple Linear Regression'
OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'excel')
FCOUNT = [0]


def plain(s):
    s = re.sub(r'_\{([^}]+)\}', r'\1', s)
    return s.replace('**', '')


def lines(text, ch):
    return sum(max(1, math.ceil(len(t) / ch)) for t in text.split('\n'))


def box_h(text, ch, extra=20):
    return lines(text, ch) * 15 + extra


# ------------------------------------------------------------------ Analysis ToolPak regression (same numbers and layout)
def regress(x, y, const=True, conf=95, labels=('X', 'Y')):
    x, y = np.asarray(x, float), np.asarray(y, float)
    n = len(x)
    if const:
        r = stats.linregress(x, y)
        b0, b1 = r.intercept, r.slope
        yh = b0 + b1 * x
        sse = ((y - yh) ** 2).sum(); sst = ((y - y.mean()) ** 2).sum()
        dfr = n - 2; dft = n - 1
        s = math.sqrt(sse / dfr)
        sxx = ((x - x.mean()) ** 2).sum()
        se1 = s / math.sqrt(sxx); se0 = s * math.sqrt(1 / n + x.mean() ** 2 / sxx)
    else:
        b0 = 0.0; b1 = (x * y).sum() / (x * x).sum()
        yh = b1 * x
        sse = ((y - yh) ** 2).sum(); sst = (y * y).sum()
        dfr = n - 1; dft = n
        s = math.sqrt(sse / dfr)
        se1 = s / math.sqrt((x * x).sum()); se0 = None
    ssr = sst - sse
    R2 = ssr / sst
    adj = 1 - (sse / dfr) / (sst / dft)
    F = ssr / (sse / dfr)
    tc = stats.t.ppf(0.975, dfr); tcl = stats.t.ppf(0.5 + conf / 200, dfr)

    def row(b, se):
        t = b / se; p = 2 * stats.t.sf(abs(t), dfr)
        return [b, se, t, p, b - tc * se, b + tc * se, b - tcl * se, b + tcl * se]
    e = y - yh
    return dict(n=n, multR=math.sqrt(R2), R2=R2, adj=adj, s=s, dfr=dfr, dft=dft, ssr=ssr, sse=sse, sst=sst,
                msr=ssr, mse=sse / dfr, F=F, sigF=stats.f.sf(F, 1, dfr), conf=conf, const=const,
                inter=row(b0, se0) if const else None, slope=row(b1, se1), yh=yh, e=e,
                z=e / math.sqrt(sse / (n - 1)), labels=labels)


def write_output(ws, r, c, R, F, residuals=False, std=False):
    """Write the SUMMARY OUTPUT block exactly as Data Analysis -> Regression does; returns cell map and last row."""
    f_t = F(italic=True, top=2, bottom=1, align='center')
    f_ital = F(italic=True, bottom=1, align='center')
    f_lab = F(); f_lab_b = F(bottom=2)
    f_num = F(num_format='General'); f_num_b = F(num_format='General', bottom=2)
    ws.write(r, c, 'SUMMARY OUTPUT', F())
    ws.merge_range(r + 2, c, r + 2, c + 1, 'Regression Statistics', f_t)
    rs = [('Multiple R', R['multR']), ('R Square', R['R2']), ('Adjusted R Square', R['adj']), ('Standard Error', R['s']), ('Observations', R['n'])]
    cells = {}
    for i, (a, v) in enumerate(rs):
        last = i == 4
        ws.write(r + 3 + i, c, a, f_lab_b if last else f_lab); ws.write_number(r + 3 + i, c + 1, v, f_num_b if last else f_num)
        cells[a] = (r + 3 + i, c + 1)
    ws.write(r + 9, c, 'ANOVA', F())
    for j, h in enumerate(['', 'df', 'SS', 'MS', 'F', 'Significance F']):
        ws.write(r + 10, c + j, h, F(italic=True, top=2, bottom=1, align='center'))
    ws.write(r + 11, c, 'Regression'); ws.write_number(r + 11, c + 1, 1); ws.write_number(r + 11, c + 2, R['ssr']); ws.write_number(r + 11, c + 3, R['msr'])
    ws.write_number(r + 11, c + 4, R['F']); ws.write_number(r + 11, c + 5, R['sigF'])
    ws.write(r + 12, c, 'Residual'); ws.write_number(r + 12, c + 1, R['dfr']); ws.write_number(r + 12, c + 2, R['sse']); ws.write_number(r + 12, c + 3, R['mse'])
    for j in range(6):
        f_ = F(bottom=2)
        if j == 0: ws.write(r + 13, c, 'Total', f_)
        elif j == 1: ws.write_number(r + 13, c + 1, R['dft'], f_)
        elif j == 2: ws.write_number(r + 13, c + 2, R['sst'], f_)
        else: ws.write_blank(r + 13, c + j, None, f_)
    cells.update({'df_reg': (r + 11, c + 1), 'SSR': (r + 11, c + 2), 'MSR': (r + 11, c + 3), 'F': (r + 11, c + 4), 'SigF': (r + 11, c + 5),
                  'df_res': (r + 12, c + 1), 'SSE': (r + 12, c + 2), 'MSE': (r + 12, c + 3), 'df_tot': (r + 13, c + 1), 'SST': (r + 13, c + 2)})
    lo = f"{R['conf']:.1f}%"
    heads = ['', 'Coefficients', 'Standard Error', 't Stat', 'P-value', 'Lower 95%', 'Upper 95%', f'Lower {lo}', f'Upper {lo}']
    for j, h in enumerate(heads):
        ws.write(r + 15, c + j, h, F(italic=True, top=2, bottom=1, align='center'))
    ws.write(r + 16, c, 'Intercept')
    if R['inter'] is None:
        ws.write_number(r + 16, c + 1, 0)
        for j in range(2, 9): ws.write(r + 16, c + j, '#N/A')
    else:
        for j, v in enumerate(R['inter']): ws.write_number(r + 16, c + 1 + j, v)
    ws.write(r + 17, c, R['labels'][0], F(bottom=2))
    for j, v in enumerate(R['slope']): ws.write_number(r + 17, c + 1 + j, v, F(bottom=2))
    cells.update({'b0': (r + 16, c + 1), 'b1': (r + 17, c + 1), 'se_b1': (r + 17, c + 2), 't_b1': (r + 17, c + 3), 'p_b1': (r + 17, c + 4),
                  'lo_b1': (r + 17, c + 5), 'hi_b1': (r + 17, c + 6), 'p_b0': (r + 16, c + 4), 'lo_b0': (r + 16, c + 5), 'hi_b0': (r + 16, c + 6)})
    last = r + 17
    if residuals:
        rr = r + 21
        ws.write(rr, c, 'RESIDUAL OUTPUT')
        hd = ['Observation', f"Predicted {R['labels'][1]}", 'Residuals'] + (['Standard Residuals'] if std else [])
        for j, h in enumerate(hd): ws.write(rr + 2, c + j, h, F(italic=True, top=2, bottom=1, align='center'))
        for i in range(R['n']):
            fb = F(bottom=2) if i == R['n'] - 1 else F()
            ws.write_number(rr + 3 + i, c, i + 1, fb); ws.write_number(rr + 3 + i, c + 1, R['yh'][i], fb); ws.write_number(rr + 3 + i, c + 2, R['e'][i], fb)
            if std: ws.write_number(rr + 3 + i, c + 3, R['z'][i], fb)
        cells['res_first'] = rr + 3
        last = rr + 3 + R['n'] - 1
    return cells, last


# ------------------------------------------------------------------ task definitions (from the Student Lab parts)
def task_from(mod, k):
    B = mod.BLOCKS
    title = [b[1] for b in B if b[0] == 'h2'][0]
    tkey = [b[1] for b in B if b[0] == 'table'][0]
    rows = mod.TABLES[tkey]['rows']
    xs = [float(r[1].replace(',', '')) for r in rows[1:]]
    ys = [float(r[2].replace(',', '')) for r in rows[1:]]
    intro = [plain(b[1]) for b in B if b[0] == 'p' and not b[1].startswith('**Excel') and not b[1].startswith('**Sums') and not b[1].startswith('Each task')]
    sums = [plain(b[1]) for b in B if b[0] == 'p' and b[1].startswith('**Sums')]
    qs = [b[1] for b in B if b[0] == 'al'][0]
    return dict(k=k, title=title, head=rows[0], xs=xs, ys=ys, intro=intro, sums=sums, qs=[plain(q) for q in qs])


OPTS = {1: {}, 2: {}, 3: {}, 4: dict(residuals=True, rplots=True), 5: {},
        6: dict(residuals=True, std=True, lplots=True, conf=99), 7: {}, 8: dict(zero=True)}
FOCUS = {1: 'reading b₀, b₁, R², P-value and the 95% confidence interval of the slope',
         2: 'negative slope  ·  the F-test (Significance F) in the ANOVA table',
         3: 'Multiple R  ·  Adjusted R Square  ·  Standard Error s  ·  P-value of the intercept  ·  weak relationship',
         4: 'Residuals and Residual Plots  ·  ANOVA: df, MS = SS / df, F = MSR / MSE',
         5: 't Stat = Coefficient / Standard Error  ·  confidence interval of the intercept  ·  predictions',
         6: 'Standardized Residuals (outliers)  ·  Line Fit Plots  ·  Confidence Level 99%',
         7: 'one-tailed test (P-value / 2)  ·  the sign of Multiple R  ·  Labels',
         8: 'Constant is Zero (line through the origin)  ·  comparing two models'}


def sol_groups(k):
    blocks = sol.S[k][4:]
    groups, excel, mistake = [], None, None
    for b in blocks:
        if b[0] == 'p' and b[1].startswith('**Excel check'):
            excel = plain(b[1]); continue
        if b[0] == 'box':
            mistake = plain(b[2]); continue
        m = re.match(r'\*\*([a-g])\)\*\*', b[1]) if b[0] == 'p' else None
        if m:
            groups.append([m.group(1), []])
        groups[-1][1].append(b)
    return groups, excel, mistake


NUMRE = re.compile(r'(?<![A-Za-zα-ω₀-₉\(])[−-]?\$?\d[\d,]*(?:\.\d+)?(?:\s?·\s?10[⁻⁰¹²³⁴⁵⁶⁷⁸⁹]+)?%?')


def blank(text):
    return NUMRE.sub('_____', text)


def build(solutions):
    os.makedirs(OUT, exist_ok=True)
    fn = os.path.join(OUT, f'{NAME} – {"Solutions" if solutions else "Students"}.xlsx')
    wb = xlsxwriter.Workbook(fn)
    wb.set_properties({'title': f'{NAME} – {"Solutions" if solutions else "Students"}', 'author': 'Emina Osmić'})
    F = lambda **k: wb.add_format(dict({'font_name': 'Calibri', 'font_size': 11, 'valign': 'vcenter'}, **k))
    A = lambda **k: wb.add_format(dict({'font_name': 'Arial', 'font_size': 10, 'valign': 'vcenter'}, **k))
    f_title = A(bold=True, font_size=16, font_color=NAVY)
    f_focus = A(italic=True, font_color=MUTED)
    f_sec = A(bold=True, font_size=11, font_color=NAVY, bottom=2, bottom_color=GOLD)
    f_head = A(bold=True, font_color='#FFFFFF', bg_color=HEAD, border=1, border_color=HEAD, align='center', text_wrap=True)
    f_given = A(border=1, border_color='#9DC3E6', align='center')
    fl = A(border=1, border_color=BOX_LINE, text_wrap=True)

    def setup(ws):
        ws.set_column('A:A', 2); ws.set_column('B:B', 19); ws.set_column('C:J', 13); ws.set_column('K:K', 3); ws.set_column('L:S', 10)

    def textbox(ws, row, col, text, width, h, fill='#FFFFFF', line=BOX_LINE, bold=False, color='#202020', size=10, dash=False):
        ln = {'color': line, 'width': 1.25 if dash else 1}
        if dash: ln['dash_type'] = 'dash'
        ws.insert_textbox(row, col, text, {'width': width, 'height': h, 'x_offset': 2, 'y_offset': 3,
                                           'font': {'name': 'Arial', 'size': size, 'color': color, 'bold': bold},
                                           'align': {'vertical': 'top'}, 'fill': {'color': fill},
                                           'line': ln, 'object_position': 1})
        return math.ceil((h + 8) / PX_ROW)

    def picture(ws, row, col, path, scale=1.0, xo=8):
        w, h = Image.open(path).size
        ws.insert_image(row, col, path, {'x_offset': xo, 'y_offset': 2, 'x_scale': scale, 'y_scale': scale, 'object_position': 1})
        return math.ceil((h * scale + 6) / PX_ROW)

    def eqpic(ws, row, tex):
        FCOUNT[0] += 1
        tex = tex.strip('$').replace('\\text{', '\\mathrm{').replace('\\ ', '\\;')
        p, w, h = XI.formula(f'r{FCOUNT[0]:03d}', tex, size=14)
        return picture(ws, row, 1, p, min(1.0, (LW - 40) / w), xo=30)

    def data_table(ws, row, head, xs, ys):
        ws.write(row, 1, head[0], f_head); ws.write(row, 2, head[1], f_head); ws.set_row(row, 30)
        for i, (x, y) in enumerate(zip(xs, ys)):
            ws.write_number(row + 1 + i, 1, x, f_given); ws.write_number(row + 1 + i, 2, y, f_given)
        return row + 1, row + len(xs)

    def scatter(ws, sheet, r1, r2, anchor_row, anchor_col, title, xname, yname, extra=None, trend=True):
        ch = wb.add_chart({'type': 'scatter'})
        ser = {'name': yname, 'categories': [sheet, r1, 1, r2, 1], 'values': [sheet, r1, 2, r2, 2],
               'marker': {'type': 'circle', 'size': 6, 'fill': {'color': '#5B9BD5'}, 'border': {'color': '#5B9BD5'}}}
        if trend:
            ser['trendline'] = {'type': 'linear', 'display_equation': True, 'display_r_squared': True,
                                'line': {'color': '#5B9BD5', 'dash_type': 'dash'}}
        ch.add_series(ser)
        if extra: ch.add_series(extra)
        ch.set_title({'name': title, 'name_font': {'size': 12}})
        ch.set_x_axis({'name': xname, 'major_gridlines': {'visible': False}})
        ch.set_y_axis({'name': yname, 'major_gridlines': {'visible': True, 'line': {'color': '#E0E0E0'}}})
        ch.set_legend({'none': True}); ch.set_size({'width': 620, 'height': 330})
        ws.insert_chart(anchor_row, anchor_col, ch, {'x_offset': 10, 'y_offset': 5})

    # ================================================================ Start
    ws = wb.add_worksheet('Start'); setup(ws)
    ws.write('B2', NAME + (' – SOLUTIONS' if solutions else ''), f_title)
    ws.write('B3', 'FENMS 0021 Probability and Statistics  ·  International Burch University', f_focus)
    intro = ("HOW TO USE THIS WORKBOOK\n"
             "In this lab we answer every question from the Excel Regression output: Data → Data Analysis → Regression.\n"
             "•  The sheet “Example” shows the whole procedure on the worked example from the lab (hours studied and exam score) and explains every part of the output.\n"
             "•  Each task has its own sheet: the task and the questions on top, the data, how to run the regression, the place for the output, and one box for every question.\n"
             "Tasks 1–5 are done in class; Tasks 6–8 are extra practice.\n\n"
             + ("This is the SOLUTIONS workbook: each sheet contains the Regression output, the chart, and the answer to every question (green)."
                if solutions else "Run the regression with the Output Range given on each sheet, insert the scatter chart, and fill in the blanks (_____) in every answer box."))
    r = 4 + textbox(ws, 4, 1, intro, LW, box_h(intro, LCH, 24)) + 1
    ws.write(r, 1, 'Before you start: turn on the Analysis ToolPak', f_sec); r += 1
    tp = ("File → Options → Add-ins → at the bottom “Manage: Excel Add-ins” → Go… → tick “Analysis ToolPak” → OK.\n"
          "A new button “Data Analysis” appears on the right side of the Data tab. (On a Mac: Tools → Excel Add-ins → Analysis ToolPak.)")
    r += textbox(ws, r, 1, tp, LW, box_h(tp, LCH, 16), fill='#EAF2FA', line='#9DC3E6', color=NAVY) + 1
    ws.write(r, 1, 'Excel functions for this lab', f_sec)
    funcs = [('Function', 'What it returns'), ('=SLOPE(y, x)', 'the slope b₁'), ('=INTERCEPT(y, x)', 'the intercept b₀'),
             ('=CORREL(x, y)', 'the correlation coefficient r (with its sign)'), ('=RSQ(y, x)', 'the coefficient of determination R²'),
             ('=STEYX(y, x)', 'the standard error of the estimate s'), ('=FORECAST.LINEAR(x, y, x)', 'the predicted value ŷ for a new x'),
             ('=LINEST(y, x, FALSE)', 'the slope of the line through the origin (Constant is Zero)'),
             ('=T.INV(1 − α, df), =T.INV.2T(α, df)', 'one- / two-tailed critical value of t, df = n − 2')]
    for i, (a, b) in enumerate(funcs):
        f = f_head if i == 0 else fl
        ws.merge_range(r + 1 + i, 1, r + 1 + i, 3, '', f); ws.write_string(r + 1 + i, 1, a, f)
        ws.merge_range(r + 1 + i, 4, r + 1 + i, 9, '', f); ws.write_string(r + 1 + i, 4, b, f)
    r += len(funcs) + 2
    ws.write(r, 1, 'Sheets', f_sec)
    sheets = ['Example'] + [f'Task {k}' for k in range(1, 9)]
    tasks = {k: task_from(m, k) for k, m in zip(range(1, 9), [part4, part5, part6, part7, part8, part9, part10, part11])}
    for i, s in enumerate(sheets):
        label = 'Example. Hours Studied and Exam Score (worked example)' if i == 0 else tasks[i]['title']
        ws.write_url(r + 1 + i, 1, f"internal:'{s}'!A1", A(font_color=BLUE, underline=1), label)
    ws.activate(); ws.set_landscape(); ws.fit_to_pages(1, 1); ws.set_paper(9)

    # ================================================================ Example
    ws = wb.add_worksheet('Example'); setup(ws)
    ws.write('B2', 'Example. Hours Studied and Exam Score', f_title)
    ws.write('B3', 'Learning focus:  running Data Analysis → Regression  ·  what every number in the output means', f_focus)
    t = ("Five students recorded how many hours they studied for an exam (X) and the score they got (Y). This is the worked example from Parts 3–5 of the lab.\n"
         "By hand we found ŷ = 46.2 + 5.6x, R² = 0.98, s = 1.46, t = 12.12 and the 95% CI for β₁ = [4.13, 7.07]. Now we get all of this from Excel in one step.")
    r = 4 + textbox(ws, 4, 1, t, LW + RW, box_h(t, 190, 18), line=NAVY) + 1
    ws.write(r, 1, 'Data', f_sec); r += 1
    d1, d2 = data_table(ws, r, ['Hours studied (X)', 'Exam score (Y)'], [1, 2, 3, 4, 5], [52, 58, 61, 70, 74])
    steps = ("HOW TO RUN THE REGRESSION\n"
             "1.  Data → Data Analysis → Regression → OK.\n"
             f"2.  Input Y Range: $C${d1}:$C${d2 + 1}   (the scores WITH the header)\n"
             f"3.  Input X Range: $B${d1}:$B${d2 + 1}   (the hours WITH the header)\n"
             "4.  Tick Labels (because we selected the headers).\n"
             f"5.  Output options → Output Range: $B${d2 + 4}\n"
             "6.  OK. Excel writes the SUMMARY OUTPUT below.")
    textbox(ws, r - 1, 4, steps, 560, box_h(steps, 85, 16), fill='#EAF2FA', line='#9DC3E6', color=NAVY)
    r = d2 + 3
    R = regress([1, 2, 3, 4, 5], [52, 58, 61, 70, 74], labels=('Hours studied (X)', 'Exam score (Y)'))
    cells, last = write_output(ws, r, 1, R, F)
    expl = [(r + 3, 'REGRESSION STATISTICS\nMultiple R = |r| = 0.99 (always positive: take the sign of b₁).\nR Square = R² = 0.98: 98% of the variation in Y is explained by X.\nAdjusted R Square: R² corrected for n and the number of predictors.\nStandard Error = s = 1.46: the typical size of a residual.\nObservations = n = 5.'),
            (r + 10, 'ANOVA\ndf: Regression 1, Residual n − 2 = 3, Total n − 1 = 4.\nSS: SSR = 313.6, SSE = 6.4, SST = 320 (SST = SSR + SSE).\nMS = SS / df;  F = MS Regression / MS Residual = 147.\nSignificance F = p-value of the F-test = P-value of the slope.'),
            (r + 15, 'COEFFICIENTS\nIntercept row: b₀ = 46.2;  X row: b₁ = 5.6  →  ŷ = 46.2 + 5.6x.\nt Stat = Coefficient / Standard Error (12.12 for the slope).\nP-value < 0.05 → the coefficient is significantly different from 0.\nLower / Upper 95% = the 95% confidence interval [4.13, 7.07].')]
    for rr_, tx in expl:
        textbox(ws, rr_, 11, tx, RW, box_h(tx, RCH, 14), fill='#F7F7F5', line=GOLD)
    r = last + 9
    ws.write(r, 1, 'Scatter chart with the regression line', f_sec); r += 1
    ch_txt = ("Select the data (both columns) → Insert → Scatter (only markers). Right-click a point → Add Trendline → Linear,\n"
              "and tick “Display Equation on chart” and “Display R-squared value on chart”.")
    r += textbox(ws, r, 1, ch_txt, LW, box_h(ch_txt, LCH, 14), fill='#EAF2FA', line='#9DC3E6', color=NAVY)
    scatter(ws, 'Example', d1, d2, r, 1, 'Hours studied vs Exam score', 'Hours studied', 'Exam score')
    r += 18
    ws.write(r, 1, 'Options in the Regression dialog', f_sec)
    opts = [('Option', 'What it does', 'Used in'), ('Labels', 'the first row of the selected ranges contains the headers', 'all tasks'),
            ('Confidence Level', 'adds a second confidence interval (for example 99%)', 'Task 6'),
            ('Constant is Zero', 'forces the line through the origin (b₀ = 0)', 'Task 8'),
            ('Residuals', 'the predicted value ŷ and the residual e of every observation', 'Tasks 4, 6'),
            ('Standardized Residuals', 'residuals divided by their standard deviation; |value| > 2 → possible outlier', 'Task 6'),
            ('Residual Plots', 'a chart of the residuals against X (checks the assumptions)', 'Task 4'),
            ('Line Fit Plots', 'a chart of the observed and predicted Y against X', 'Task 6')]
    for i, (a, b, c) in enumerate(opts):
        f = f_head if i == 0 else fl
        ws.write_string(r + 1 + i, 1, a, f)
        ws.merge_range(r + 1 + i, 2, r + 1 + i, 7, '', f); ws.write_string(r + 1 + i, 2, b, f)
        ws.merge_range(r + 1 + i, 8, r + 1 + i, 9, '', f); ws.write_string(r + 1 + i, 8, c, f)
    ws.set_landscape(); ws.fit_to_pages(1, 0); ws.set_paper(9)

    # ================================================================ tasks
    f_q = A(bold=True, font_color=NAVY)
    for k in range(1, 9):
        T = tasks[k]; O = OPTS[k]; sheet = f'Task {k}'
        ws = wb.add_worksheet(sheet); setup(ws)
        ws.write('B2', T['title'], f_title)
        ws.write('B3', 'Learning focus:  ' + FOCUS[k], f_focus)
        qtxt = '\n'.join(T['intro']) + '\n\nQuestions:\n' + '\n'.join(f'{chr(97 + i)})  {q}' for i, q in enumerate(T['qs']))
        r = 4 + textbox(ws, 4, 1, qtxt, LW + RW, box_h(qtxt, 200, 18), line=NAVY) + 1
        ws.write(r, 1, f'SOLUTION {k}.', f_sec); r += 1
        d1, d2 = data_table(ws, r, T['head'][1:], T['xs'], T['ys'])
        n = len(T['xs'])
        if T['sums']:
            textbox(ws, d2 + 1, 1, T['sums'][0], 330, box_h(T['sums'][0], 48, 12), fill=BOX_HELP, size=9)
        out_row = d2 + 6
        conf = O.get('conf', 95)
        ticks = ['Labels'] + (['Confidence Level: 99%'] if conf != 95 else []) + (['Residuals'] if O.get('residuals') else []) \
            + (['Standardized Residuals'] if O.get('std') else []) + (['Residual Plots'] if O.get('rplots') else []) + (['Line Fit Plots'] if O.get('lplots') else [])
        run = ("RUN THE REGRESSION\n"
               "Data → Data Analysis → Regression → OK.\n"
               f"Input Y Range: $C${d1}:$C${d2 + 1}\n"
               f"Input X Range: $B${d1}:$B${d2 + 1}\n"
               f"Tick: {', '.join(ticks)}.\n"
               f"Output Range: $B${out_row + 1}")
        if O.get('zero'):
            run += f"\nThen run it a SECOND time with Constant is Zero ticked and Output Range: $L${out_row + 1}"
        textbox(ws, d1 - 2, 4, run, 520, box_h(run, 80, 14), fill='#EAF2FA', line='#9DC3E6', color=NAVY)
        labels = (T['head'][1], T['head'][2])
        R = regress(T['xs'], T['ys'], conf=conf, labels=labels)
        height = (25 + n) if O.get('residuals') else 19
        if solutions:
            cells, last = write_output(ws, out_row, 1, R, F, residuals=O.get('residuals'), std=O.get('std'))
            if O.get('zero'):
                R0 = regress(T['xs'], T['ys'], const=False, labels=labels)
                write_output(ws, out_row, 11, R0, F)
                ws.write(out_row - 1, 1, 'Usual model', f_q); ws.write(out_row - 1, 11, 'Constant is Zero', f_q)
                ws.set_column('L:T', 13)
            if O.get('residuals'):
                rf = cells['res_first']
                if O.get('rplots'):
                    ch = wb.add_chart({'type': 'scatter'})
                    ch.add_series({'categories': [sheet, d1, 1, d2, 1], 'values': [sheet, rf, 3, rf + n - 1, 3],
                                   'marker': {'type': 'diamond', 'size': 6, 'fill': {'color': '#4472C4'}, 'border': {'color': '#4472C4'}}})
                    ch.set_title({'name': f'{labels[0]} Residual Plot', 'name_font': {'size': 11}})
                    ch.set_x_axis({'name': labels[0]}); ch.set_y_axis({'name': 'Residuals', 'major_gridlines': {'visible': False}})
                    ch.set_legend({'none': True}); ch.set_size({'width': 480, 'height': 290})
                    ws.insert_chart(out_row, 11, ch, {'x_offset': 10})
                if O.get('lplots'):
                    ch = wb.add_chart({'type': 'scatter'})
                    ch.add_series({'name': labels[1], 'categories': [sheet, d1, 1, d2, 1], 'values': [sheet, d1, 2, d2, 2],
                                   'marker': {'type': 'diamond', 'size': 6, 'fill': {'color': '#4472C4'}, 'border': {'color': '#4472C4'}}})
                    ch.add_series({'name': f'Predicted {labels[1]}', 'categories': [sheet, d1, 1, d2, 1], 'values': [sheet, rf, 2, rf + n - 1, 2],
                                   'marker': {'type': 'square', 'size': 6, 'fill': {'color': '#ED7D31'}, 'border': {'color': '#ED7D31'}}})
                    ch.set_title({'name': f'{labels[0]} Line Fit Plot', 'name_font': {'size': 11}})
                    ch.set_x_axis({'name': labels[0]}); ch.set_y_axis({'name': labels[1], 'major_gridlines': {'visible': False}})
                    ch.set_legend({'position': 'bottom'}); ch.set_size({'width': 480, 'height': 300})
                    ws.insert_chart(out_row, 11, ch, {'x_offset': 10})
            r = out_row + height + 1
        else:
            ph = f'Your Regression output goes here (Output Range: $B${out_row + 1}).'
            textbox(ws, out_row, 1, ph, LW, height * PX_ROW - 10, fill='#FAFAFA', line='#A6A6A6', color=MUTED, dash=True)
            if O.get('zero'):
                pass
            r = out_row + height + 1
        # scatter chart
        ws.write(r, 1, 'Scatter chart with the regression line', f_sec); r += 1
        ch_txt = ("Select both data columns → Insert → Scatter (only markers) → right-click a point → Add Trendline → Linear →\n"
                  "tick “Display Equation on chart” and “Display R-squared value on chart”.")
        r += textbox(ws, r, 1, ch_txt, LW, box_h(ch_txt, LCH, 14), fill='#EAF2FA', line='#9DC3E6', color=NAVY)
        if solutions:
            scatter(ws, sheet, d1, d2, r, 1, f'{labels[0]} vs {labels[1]}', labels[0], labels[1])
            r += 18
        else:
            r += 1
        # questions
        ws.write(r, 1, 'Answers', f_sec); r += 1
        groups, excel, mistake = sol_groups(k)
        ans_top = r
        for letter, blks in groups:
            i = ord(letter) - 97
            q = f'{letter})  {T["qs"][i]}'
            start = r
            r += textbox(ws, r, 1, q, LW, box_h(q, LCH, 12), fill=BOX_HELP, line=NAVY, bold=True, color=NAVY)
            for b in blks:
                if b[0] == 'p' and solutions:
                    tx = plain(re.sub(r'^\*\*[a-g]\)\*\*\s*', '', b[1]))
                    if tx: r += textbox(ws, r, 1, tx, LW, box_h(tx, LCH, 12))
                elif b[0] == 'eq' and solutions:
                    r += eqpic(ws, r, b[1])
                elif b[0] == 'ans':
                    tx = plain(b[1])
                    if not solutions:
                        tx = blank(tx)
                    r += textbox(ws, r, 1, tx, LW, box_h(tx, LCH - 8, 14), fill='#F1F8F3', line='#9CCBA8', color=GREEN, bold=solutions)
            r += 1
        if mistake:
            ws.write(ans_top - 1, 11, 'TIP', f_sec)
            textbox(ws, ans_top, 11, mistake, RW, box_h(mistake, RCH, 16), fill='#F7F7F5', line=RED)
        if excel and solutions:
            r += textbox(ws, r, 1, excel, LW, box_h(excel, LCH, 12), fill='#EAF2FA', line='#9DC3E6', color=NAVY)
        ws.set_landscape(); ws.fit_to_pages(1, 0); ws.set_paper(9)
    wb.close()
    return fn


if __name__ == '__main__':
    for s in (False, True):
        print(build(s))
