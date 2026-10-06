"""Hyperframes compositions for the Lab 3 solutions (same visual language as build_figs.py)."""
import math
from common import write

NAVY, BLUE, LIGHT, PALE, GOLD, GOLDPALE, PANEL, RED, TEXT, MUTED = (
    '#003e67', '#1f5f99', '#c9d6e3', '#eef2f6', '#c39a3d', '#f1e4c6', '#f3f3f0', '#b34739', '#202020', '#5f6368')


def panel_steps(steps, left=960, top=70, width=640):
    """Right-hand explanation panel: one div per step, shown one at a time."""
    html = ''
    for i, (h, t, e) in enumerate(steps):
        if h[0] == 'ANSWERS': t, e = '', t
        html += f'''        <div id="s{i}" class="abs" style="left:{left}px;top:{top}px;width:{width}px;opacity:0">
          <div class="lbl" style="color:{GOLD};font-size:21px;letter-spacing:2px">{h[0]}</div>
          <div class="lbl" style="color:{NAVY};font-size:31px;margin-top:10px;white-space:normal;line-height:1.25">{h[1]}</div>
          <div class="rt" style="margin-top:20px;font-size:24px;line-height:1.45;color:{TEXT}">{t}</div>
          <div class="eq" style="margin-top:24px;font-size:33px;white-space:normal;line-height:1.35">{e}</div>
        </div>
'''
    return html


def step_js(times, first_fade=0.4):
    js = ''
    for i, t in enumerate(times):
        js += f'      tl.to("#s{i}", {{ opacity: 1, duration: {first_fade} }}, {t});\n'
        if i < len(times) - 1:
            js += f'      tl.to("#s{i}", {{ opacity: 0, duration: 0.3 }}, {times[i + 1] - 0.35});\n'
    return js


# ---------------------------------------------------------------- S1: Problem 1, element chips
EL = ['copper', 'sodium', 'nitrogen', 'potassium', 'uranium', 'oxygen', 'zinc']
MEM = {'copper': 'A', 'sodium': 'A B', 'nitrogen': 'B', 'potassium': 'B', 'uranium': '', 'oxygen': 'C', 'zinc': 'A'}
body = f'        <div class="lbl abs" style="left:60px;top:40px;color:{NAVY};font-size:28px">S = all seven elements</div>\n'
CW, GAP, X0, Y0 = 200, 18, 60, 95
for i, el in enumerate(EL):
    x = X0 + i * (CW + GAP)
    tags = ''.join(f'<span style="display:inline-block;margin:0 4px;padding:2px 12px;border-radius:8px;background:'
                   f'{ {"A": "#dce5ee", "B": GOLDPALE, "C": PALE}[m] };color:{ {"A": BLUE, "B": "#8a6d1f", "C": NAVY}[m] }">{m}</span>'
                   for m in MEM[el].split()) or f'<span style="color:{MUTED}">none</span>'
    body += f'''        <div id="c{i}" class="abs chip" style="left:{x}px;top:{Y0}px;width:{CW}px;height:86px;line-height:86px;text-align:center">{el}</div>
        <div class="abs" style="left:{x}px;top:{Y0 + 100}px;width:{CW}px;text-align:center;font:700 19px Montserrat">{tags}</div>
'''
P1 = [  # label, expression, working, answer, members
    ('a', "A'", 'Everything in S that is <b>not</b> in A = {copper, sodium, zinc}.', '{nitrogen, potassium, uranium, oxygen}', [2, 3, 4, 5]),
    ('b', 'A &#8746; C', 'Everything in A, in C, or in both.', '{copper, sodium, zinc, oxygen}', [0, 1, 6, 5]),
    ('c', "(A &#8745; B') &#8746; C'", "A &#8745; B' = {copper, zinc}.&#8195;C' = everything except oxygen.<br>The union is just C'.", '{copper, sodium, nitrogen, potassium, uranium, zinc}', [0, 1, 2, 3, 4, 6]),
    ('d', "B' &#8745; C'", "B' = {copper, uranium, oxygen, zinc}.&#8195;Now remove oxygen (not in C').", '{copper, uranium, zinc}', [0, 4, 6]),
    ('e', 'A &#8745; B &#8745; C', 'A &#8745; B = {sodium}, but sodium is not in C.', '&#8709;&#8195;(the empty set)', []),
    ('f', "(A' &#8746; B') &#8745; (A' &#8745; C)", "A' &#8745; C = {oxygen}, and oxygen is also in A' &#8746; B'.", '{oxygen}', [5]),
]
for i, (k, ex, w, a, m) in enumerate(P1):
    body += f'''        <div id="s{i}" class="abs" style="left:60px;top:300px;width:1520px;opacity:0">
          <div class="lbl" style="color:{GOLD};font-size:22px;letter-spacing:2px">PART {k.upper()}</div>
          <div class="eq" style="margin-top:8px;font-size:46px">{ex}</div>
          <div class="rt" style="margin-top:22px;font-size:27px;color:{TEXT}">{w}</div>
          <div class="eq" style="margin-top:26px;font-size:34px;color:{NAVY}">= {a}</div>
        </div>
'''
SUMMARY = ''.join(f'<div style="margin-top:12px"><span style="color:{GOLD}">{k}.</span>&#8195;{ex} = {a}</div>' for k, ex, w, a, m in P1)
body += f'''        <div id="s{len(P1)}" class="abs" style="left:60px;top:290px;width:1520px;opacity:0">
          <div class="lbl" style="color:{GOLD};font-size:22px;letter-spacing:2px">ALL ANSWERS</div>
          <div class="rt" style="margin-top:6px;font-size:28px;color:{NAVY}">{SUMMARY}</div>
        </div>
'''
css = f'.chip {{ border-radius: 18px; background: {PANEL}; border: 3px solid {LIGHT}; font: 600 26px "Open Sans"; color: {TEXT}; }}'
js = '      tl.from(".chip", { y: 20, opacity: 0, duration: 0.4, stagger: 0.08 }, 0.2);\n'
T = [1.4 + 3.4 * i for i in range(len(P1) + 1)]
js += step_js(T)
for i, (k, ex, w, a, m) in enumerate(P1):
    t = T[i] + 0.9
    js += f'      tl.to(".chip", {{ backgroundColor: "{PANEL}", color: "{TEXT}", borderColor: "{LIGHT}", opacity: 0.45, duration: 0.3 }}, {t});\n'
    if m:
        js += f'      tl.to([{", ".join(f"{chr(34)}#c{j}{chr(34)}" for j in m)}], {{ backgroundColor: "{NAVY}", color: "#ffffff", borderColor: "{NAVY}", opacity: 1, duration: 0.35, stagger: 0.07 }}, {t + 0.35});\n'
js += f'      tl.to(".chip", {{ backgroundColor: "{PANEL}", color: "{TEXT}", borderColor: "{LIGHT}", opacity: 1, duration: 0.4 }}, {T[-1]});\n'
write('sol1_problem1_sets', round(T[-1] + 4.5, 1), body, js, css)


# ---------------------------------------------------------------- table helper (S2, S3, S4)
def table_fig(name, title, cols, rows, vals, tot_row, tot_col, grand, steps, colw=170, rowh=92, x0=50, y0=140, labw=190):
    """steps: list of ((kicker, heading), text, eq, highlight cells [(r,c)], show_totals)."""
    nr, nc = len(rows), len(cols)
    html = f'        <div class="lbl abs" style="left:{x0}px;top:60px;color:{NAVY};font-size:28px">{title}</div>\n'
    def cell(id_, x, y, w, txt, cls):
        return f'        <div id="{id_}" class="abs {cls}" style="left:{x}px;top:{y}px;width:{w}px;height:{rowh}px;line-height:{rowh}px">{txt}</div>\n'
    for c, h in enumerate(cols + ['Total']):
        html += cell(f'h{c}', x0 + labw + c * colw, y0, colw - 6, h, 'hd' + (' tot' if c == nc else ''))
    for r, h in enumerate(rows + ['Total']):
        y = y0 + (r + 1) * rowh
        html += cell(f'r{r}', x0, y, labw - 6, h, 'rl' + (' tot' if r == nr else ''))
        for c in range(nc + 1):
            if r < nr and c < nc: txt, cls = vals[r][c], 'v'
            elif r < nr: txt, cls = tot_col[r], 'v tot tc'
            elif c < nc: txt, cls = tot_row[c], 'v tot tc'
            else: txt, cls = grand, 'v tot tc'
            html += cell(f'v{r}_{c}', x0 + labw + c * colw, y, colw - 6, txt, cls)
    html += panel_steps([(s[0], s[1], s[2]) for s in steps], left=x0 + labw + (nc + 1) * colw + 40,
                        width=1640 - (x0 + labw + (nc + 1) * colw + 40) - 40)
    css = (f'.hd {{ background: {NAVY}; color: #fff; text-align: center; border-radius: 10px; font: 700 25px Montserrat; }}'
           f'.rl {{ background: {PALE}; color: {NAVY}; text-align: center; border-radius: 10px; font: 700 25px Montserrat; }}'
           f'.v {{ background: {PANEL}; color: {TEXT}; text-align: center; border-radius: 10px; font: 600 31px "Open Sans"; }}'
           f'.tc {{ background: {GOLDPALE}; }}')
    js = '      tl.set(".tot", { opacity: 0 }, 0);\n'
    js += '      tl.from([".hd:not(.tot)", ".rl:not(.tot)", ".v:not(.tot)"], { opacity: 0, y: 12, duration: 0.35, stagger: 0.03 }, 0.2);\n'
    T, t = [], 1.2
    for s in steps:
        T.append(t); t += s[5] if len(s) > 5 else 3.6
    js += step_js(T)
    shown = False
    for i, s in enumerate(steps):
        t0 = T[i] + 0.6
        if s[4] and not shown:
            js += f'      tl.to(".tot", {{ opacity: 1, duration: 0.4, stagger: 0.05 }}, {t0});\n'; shown = True
        js += f'      tl.to(".v", {{ scale: 1, boxShadow: "0 0 0 0 rgba(0,0,0,0)", opacity: 1, duration: 0.25 }}, {t0});\n'
        if s[3]:
            ids = ', '.join(f'"#v{r}_{c}"' for r, c in s[3])
            js += f'      tl.to(".v", {{ opacity: 0.35, duration: 0.3 }}, {t0 + 0.3});\n'
            js += f'      tl.to([{ids}], {{ opacity: 1, boxShadow: "0 0 0 5px {NAVY}", scale: 1.04, duration: 0.35, stagger: 0.08 }}, {t0 + 0.4});\n'
    write(name, round(T[-1] + (steps[-1][5] if len(steps[-1]) > 5 else 3.6) + 0.4, 1), html, js, css)


# ---------------------------------------------------------------- S2: Problem 3, accidents
table_fig('sol2_problem3_accidents', 'Accidents by shift and cause (% of 300)',
          ['Unsafe', 'Human error'], ['Day', 'Evening', 'Graveyard'],
          [['5%', '32%'], ['6%', '25%'], ['2%', '30%']], ['13%', '87%'], ['37%', '31%', '32%'], '100%',
          [(('STEP 1', 'Add a Total row and column'), 'Every accident sits in exactly one cell, so the cells add up to 100%.', '', [], True),
           (('PART A', 'Graveyard shift'), 'Read the Graveyard row total.', 'P(G) = 2% + 30% = 0.32', [(2, 0), (2, 1), (2, 2)], True),
           (('PART B', 'Human error'), 'Read the Human error column total.', 'P(H) = 32% + 25% + 30% = 0.87', [(0, 1), (1, 1), (2, 1), (3, 1)], True),
           (('PART C', 'Unsafe conditions'), 'The other cause. Check: 0.13 + 0.87 = 1.', 'P(U) = 1 &#8722; 0.87 = 0.13', [(0, 0), (1, 0), (2, 0), (3, 0)], True),
           (('PART D', 'Evening or graveyard'), 'One accident cannot happen on two shifts, so just add the row totals.', 'P(E &#8746; G) = 0.31 + 0.32 = 0.63', [(1, 2), (2, 2)], True),
           (('ANSWERS', 'Problem 3'), '(a) 0.32&#8195;(b) 0.87<br>(c) 0.13&#8195;(d) 0.63', '', [], True, 4.2)],
          colw=190)

# ---------------------------------------------------------------- S3: Problem 4, smoking and hypertension
table_fig('sol3_problem4_given', 'Hypertension and smoking (180 people)',
          ['Non', 'Moderate', 'Heavy'], ['H', 'NH'],
          [['21', '36', '30'], ['48', '26', '19']], ['69', '62', '49'], ['87', '93'], '180',
          [(('STEP 1', 'Find the group totals'), 'Add each row and each column. The totals are the sizes of the groups we may condition on.', '', [], True),
           (('PART A', 'H, given heavy smoker'), '"Given heavy smoker" means: only look at the Heavy column (49 people).', 'P(H | Heavy) = 30/49 &#8776; 0.612', [(0, 2), (2, 2)], True, 4.2),
           (('PART B', 'Nonsmoker, given NH'), '"Given no hypertension" means: only look at the NH row (93 people).', 'P(Non | NH) = 48/93 &#8776; 0.516', [(1, 0), (1, 3)], True, 4.2),
           (('ANSWERS', 'Problem 4'), '(a) 30/49 &#8776; 0.612<br>(b) 48/93 &#8776; 0.516<br><span style="color:#b34739">Divide by the group total, not by 180.</span>', '', [], True, 4.4)],
          colw=165, labw=120)

# ---------------------------------------------------------------- S4: Problems 5 and 6, handoffs
table_fig('sol4_problems5_6_calls', 'Call types: probabilities',
          ['H<sub>0</sub>', 'H<sub>1</sub>', 'H<sub>2</sub>'], ['Long (L)', 'Brief (B)'],
          [['0.1', '0.1', '0.2'], ['0.4', '0.1', '0.1']], ['0.5', '0.2', '0.3'], ['0.4', '0.6'], '1.0',
          [(('STEP 1', 'Marginal totals'), 'Row and column totals give P(L), P(B), P(H<sub>0</sub>), P(H<sub>1</sub>), P(H<sub>2</sub>).', '', [], True),
           (('5A', 'No handoffs'), 'Add the H<sub>0</sub> column.', 'P(H<sub>0</sub>) = 0.1 + 0.4 = 0.5', [(0, 0), (1, 0), (2, 0)], True),
           (('5B', 'Brief call'), 'Add the Brief row.', 'P(B) = 0.4 + 0.1 + 0.1 = 0.6', [(1, 0), (1, 1), (1, 2), (1, 3)], True),
           (('5C', 'Long or at least two handoffs'), 'Long row plus H<sub>2</sub> column, but the 0.2 cell is in both: count it once.', 'P(L &#8746; H<sub>2</sub>) = 0.4 + 0.3 &#8722; 0.2 = 0.5', [(0, 0), (0, 1), (0, 2), (1, 2)], True, 4.4),
           (('6A', 'No handoffs, given brief'), 'Stay inside the Brief row (total 0.6).', 'P(H<sub>0</sub> | B) = 0.4 / 0.6 &#8776; 0.667', [(1, 0), (1, 3)], True),
           (('6B', 'Long, given one handoff'), 'Stay inside the H<sub>1</sub> column (total 0.2).', 'P(L | H<sub>1</sub>) = 0.1 / 0.2 = 0.5', [(0, 1), (2, 1)], True),
           (('6C', 'One or more handoffs, given long'), 'Stay inside the Long row (total 0.4).', 'P(H<sub>1</sub> &#8746; H<sub>2</sub> | L) = 0.3 / 0.4 = 0.75', [(0, 1), (0, 2), (0, 3)], True),
           (('ANSWERS', 'Problems 5 and 6'), '5: (a) 0.5&#8195;(b) 0.6&#8195;(c) 0.5<br>6: (a) 0.667&#8195;(b) 0.5&#8195;(c) 0.75', '', [], True, 4.4)],
          colw=150, labw=170)

# ---------------------------------------------------------------- S5: Problem 7, tree + Bayes
N = {'O': (150, 330), 'F': (520, 175), 'M': (520, 485), 'FP': (880, 95), 'FN': (880, 255), 'MP': (880, 415), 'MN': (880, 575)}
E = [('O', 'F', '0.20'), ('O', 'M', '0.80'), ('F', 'FP', '0.90'), ('F', 'FN', '0.10'), ('M', 'MP', '0.85'), ('M', 'MN', '0.15')]
lines = labels = ''
for i, (a, b, p) in enumerate(E):
    (x1, y1), (x2, y2) = N[a], N[b]
    x1, x2 = x1 + 85, x2 - 85
    L = math.hypot(x2 - x1, y2 - y1)
    lines += f'<line id="e{i}" x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{BLUE}" stroke-width="4" stroke-dasharray="{L:.0f}" stroke-dashoffset="{L:.0f}"/>'
    labels += f'        <div id="pl{i}" class="abs" style="left:{(x1+x2)/2-40}px;top:{(y1+y2)/2-22}px;width:80px;text-align:center;background:#fff;border-radius:8px;font:600 24px \'Open Sans\';opacity:0">{p}</div>\n'
body = f'        <svg class="abs" style="left:0;top:0" width="1640" height="740">{lines}</svg>\n' + labels
def node(id_, text, bg, fg, w=170):
    x, y = N[id_]
    return f'        <div id="n{id_}" class="abs" style="left:{x-w/2}px;top:{y-32}px;width:{w}px;height:64px;border-radius:14px;background:{bg};color:{fg};font:700 24px Montserrat;text-align:center;line-height:64px;opacity:0">{text}</div>\n'
body += node('O', 'Student', GOLD, '#fff') + node('F', 'Female', NAVY, '#fff') + node('M', 'Male', NAVY, '#fff')
body += node('FP', 'Pass', '#f5c400', NAVY) + node('FN', 'Fail', '#dce5ee', NAVY) + node('MP', 'Pass', '#f5c400', NAVY) + node('MN', 'Fail', '#dce5ee', NAVY)
body += f'        <div id="cnt" class="abs" style="left:60px;top:40px;font:600 22px \'Open Sans\';color:{MUTED};opacity:0">50 students: 10 female, 40 male</div>\n'
prods = [('FP', '0.20 &#215; 0.90 = 0.18'), ('FN', '0.20 &#215; 0.10 = 0.02'), ('MP', '0.80 &#215; 0.85 = 0.68'), ('MN', '0.80 &#215; 0.15 = 0.12')]
for i, (k, t) in enumerate(prods):
    x, y = N[k]
    body += f'        <div id="pr{i}" class="abs" style="left:{x+105}px;top:{y-18}px;font:600 25px \'Open Sans\';color:{NAVY if k[1]=="P" else MUTED};white-space:nowrap;opacity:0">{t}</div>\n'
body += f'''        <div id="sum" class="abs" style="left:985px;top:660px;opacity:0"><span class="eq" style="font-size:28px">P(Pass) = 0.18 + 0.68 = 0.86</span></div>
        <div id="bay" class="abs card" style="left:1290px;top:95px;width:330px;height:500px;padding:26px;border-left:6px solid {NAVY};opacity:0">
          <div class="lbl" style="color:{NAVY};font-size:24px">Bayes: flip it</div>
          <div class="sub" style="margin-top:10px;white-space:normal">The student passed. Is the student female?</div>
          <div style="margin-top:22px;font:600 25px 'Open Sans';color:{NAVY}">P(F | Pass)</div>
          <div style="margin-top:10px;font:600 25px 'Open Sans';color:{NAVY}">= 0.18 / 0.86</div>
          <div style="margin-top:10px;font:700 30px Montserrat;color:{NAVY}">&#8776; 0.209</div>
          <div class="note" style="margin-top:18px;font-size:20px">In counts: 9 of the 43 students who pass are female, and 9/43 &#8776; 0.209.</div>
        </div>
'''
js = '      tl.to(["#nO", "#cnt"], { opacity: 1, duration: 0.4 }, 0.2);\n'
for i in range(2):
    js += f'      tl.to("#e{i}", {{ attr: {{ "stroke-dashoffset": 0 }}, duration: 0.7 }}, 0.6);\n      tl.to("#pl{i}", {{ opacity: 1, duration: 0.3 }}, 1.1);\n'
js += '      tl.to(["#nF", "#nM"], { opacity: 1, duration: 0.4 }, 1.2);\n'
for i in range(2, 6):
    js += f'      tl.to("#e{i}", {{ attr: {{ "stroke-dashoffset": 0 }}, duration: 0.7 }}, 2.0);\n      tl.to("#pl{i}", {{ opacity: 1, duration: 0.3 }}, 2.5);\n'
js += '      tl.to(["#nFP", "#nFN", "#nMP", "#nMN"], { opacity: 1, duration: 0.4 }, 2.6);\n'
js += ''.join(f'      tl.fromTo("#pr{i}", {{ opacity: 0, x: -12 }}, {{ opacity: 1, x: 0, duration: 0.4 }}, {3.6 + i*0.5});\n' for i in range(4))
js += '      tl.to(["#nFN", "#nMN", "#pr1", "#pr3", "#e3", "#e5", "#pl3", "#pl5"], { opacity: 0.3, duration: 0.5 }, 6.0);\n'
js += '      tl.to(["#nFP", "#nMP"], { scale: 1.12, duration: 0.3, yoyo: true, repeat: 1 }, 6.1);\n'
js += '      tl.fromTo("#sum", { opacity: 0, y: 10 }, { opacity: 1, y: 0, duration: 0.5 }, 6.7);\n'
js += '      tl.to(["#e1", "#e4", "#nM", "#nMP", "#pr2", "#pl1", "#pl4"], { opacity: 0.35, duration: 0.5 }, 8.6);\n'
js += f'      tl.to(["#e0", "#e2"], {{ attr: {{ stroke: "{NAVY}", "stroke-width": 8 }}, duration: 0.5 }}, 8.6);\n'
js += '      tl.fromTo("#bay", { opacity: 0, x: 20 }, { opacity: 1, x: 0, duration: 0.6 }, 9.0);\n'
write('sol5_problem7_tree', 14, body, js)
print('ok')
