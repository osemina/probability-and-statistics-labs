from figlib import *

# ---------------------------------------------------------------- Fig 1: the three types of tests
PANELS = [('two', 'Two-tailed test', 'H₁: μ ≠ μ₀', [(-3.6, -1.96), (1.96, 3.6)], ['α/2', 'α/2'], [-1.96, 1.96]),
          ('right', 'Right-tailed test', 'H₁: μ > μ₀', [(1.645, 3.6)], ['α'], [1.645]),
          ('left', 'Left-tailed test', 'H₁: μ < μ₀', [(-3.6, -1.645)], ['α'], [-1.645])]
body, inner, js, cards = '', '', '', ''
for i, (k, title, h1, tails, labs, crit) in enumerate(PANELS):
    x0 = 30 + i * 535
    cards += card(x0, 30, 515, 600)
    body += text(f't{k}', x0 + 30, 58, title, 'step', 'font-size:26px')
    body += text(f'h{k}', x0 + 30, 102, h1, 'eq', 'font-size:28px')
    A = Axes(x0 + 30, 200, 455, 300, -3.6, 3.6, 0, 0.42)
    inner += A.axis([-3, -2, -1, 0, 1, 2, 3], lambda t: f'{t:d}', size=19)
    inner += f'<path id="a{k}" d="{A.area(phi, -3.6, 3.6)}" fill="{MID}" opacity="0"/>'
    g = f'<g id="r{k}" opacity="0">'
    for (a, b), lab in zip(tails, labs):
        g += f'<path d="{A.area(phi, a, b)}" fill="{GOLD}" opacity="0.95"/>'
        xm = (a + b) / 2
        g += f'<text x="{A.X(xm)}" y="{A.Y(0.11)}" font-family="Open Sans" font-weight="600" font-size="21" fill="#8a6d1f" text-anchor="middle">{lab}</text>'
    for z in crit:
        g += f'<line x1="{A.X(z)}" y1="{A.Y(0.31)}" x2="{A.X(z)}" y2="{A.Y(0)}" stroke="{NAVY}" stroke-width="3" stroke-dasharray="8 6"/>'
    g += '</g>'
    inner += g
    inner += (f'<text id="k{k}" opacity="0" x="{A.X(0)}" y="{A.Y(0.21)}" font-family="Montserrat" font-weight="700" font-size="20" fill="#fff" text-anchor="middle">'
              f'<tspan x="{A.X(0)}">do not</tspan><tspan x="{A.X(0)}" dy="26">reject H₀</tspan></text>')
    inner += f'<path id="c{k}" d="{A.curve(phi, -3.6, 3.6)}" fill="none" stroke="{NAVY}" stroke-width="4.5" stroke-dasharray="3000" stroke-dashoffset="3000"/>'
    where = {'two': 'both tails', 'right': 'right tail only', 'left': 'left tail only'}[k]
    body += text(f'w{k}', x0 + 30, 568, f'Rejection region: <b style="color:#8a6d1f">{where}</b>', 'rt', 'font-size:22px')
    t0 = 0.3 + i * 2.2
    js += show([f't{k}', f'h{k}'], t0, dy=8) + draw(f'c{k}', t0 + 0.3, 1.0)
    js += show(f'a{k}', t0 + 1.1, 0.5, op=0.6) + show(f'r{k}', t0 + 1.4, 0.5) + show([f'k{k}', f'w{k}'], t0 + 1.7, dy=6)
body = cards + svg(inner) + body
body += text('foot', 30, 660, 'The shaded areas are the rejection regions. If the test statistic falls there, we reject H₀. Their total area is α.', 'note', 'font-size:24px;color:#003e67;font-weight:600')
js += show('foot', 7.2, dy=8)
write('fig1_types_of_tests', 11, body, js)


# ---------------------------------------------------------------- Fig 2: alpha, beta and power
from math import erf, sqrt
Phi = lambda z: 0.5 * (1 + erf(z / sqrt(2)))
MU1 = 2.6
f0 = phi
f1 = lambda x: phi(x - MU1)
A = Axes(90, 150, 1020, 420, -3.4, 6.2, 0, 0.44)
inner = A.axis([-3, -2, -1, 0, 1, 2, 3, 4, 5, 6], lambda t: f'{t:d}', size=20)
DARK = '#1f5f99'
for key, c, a_lab in (('a', 1.645, '0.05'), ('b', 2.326, '0.01')):
    beta = Phi(c - MU1)
    g = f'<g id="g{key}" opacity="0">'
    g += f'<path d="{A.area(f1, c, 6.2)}" fill="{MID}" opacity="0.55"/>'
    g += f'<path d="{A.area(f1, -3.4, c)}" fill="{DARK}" opacity="0.85"/>'
    g += f'<path d="{A.area(f0, c, 6.2)}" fill="{GOLD}" opacity="0.95"/>'
    g += f'<line x1="{A.X(c)}" y1="{A.Y(0.43)}" x2="{A.X(c)}" y2="{A.Y(0)}" stroke="{TEXT}" stroke-width="3" stroke-dasharray="8 6"/>'
    g += f'<text x="{A.X(c)}" y="{A.Y(0.43) - 10}" font-family="Montserrat" font-weight="700" font-size="21" fill="{TEXT}" text-anchor="middle">critical value {c}</text>'
    g += f'<text x="{A.X(c + 0.55)}" y="{A.Y(0.035)}" font-family="Open Sans" font-weight="600" font-size="20" fill="#8a6d1f" text-anchor="start">α = {a_lab}</text>'
    g += f'<text x="{A.X(c - 0.12)}" y="{A.Y(0.022)}" font-family="Montserrat" font-weight="700" font-size="20" fill="#fff" text-anchor="end">β ≈ {beta:.2f}</text>'
    g += f'<text x="{A.X(MU1 + 0.55)}" y="{A.Y(0.16)}" font-family="Montserrat" font-weight="700" font-size="20" fill="{NAVY}" text-anchor="middle">power ≈ {1 - beta:.2f}</text>'
    g += '</g>'
    inner += g
inner += f'<path id="c0" d="{A.curve(f0, -3.4, 6.2)}" fill="none" stroke="{NAVY}" stroke-width="4.5" stroke-dasharray="3000" stroke-dashoffset="3000"/>'
inner += f'<path id="c1" d="{A.curve(f1, -3.4, 6.2)}" fill="none" stroke="{RED}" stroke-width="4.5" stroke-dasharray="3000" stroke-dashoffset="3000"/>'
inner += f'<text id="l0" opacity="0" x="{A.X(-1.3)}" y="{A.Y(0.36)}" font-family="Montserrat" font-weight="700" font-size="22" fill="{NAVY}" text-anchor="end">if H₀ is true</text>'
inner += f'<text id="l1" opacity="0" x="{A.X(MU1 + 1.3)}" y="{A.Y(0.36)}" font-family="Montserrat" font-weight="700" font-size="22" fill="{RED}" text-anchor="start">if H₁ is true</text>'
body = card(40, 40, 1120, 660) + card(1190, 40, 410, 660) + svg(inner)
body += '        <div class="lbl abs" style="left:80px;top:66px;color:#003e67;font-size:28px">Two errors and the power of a right-tailed test</div>\n'
body += text('lab', 560, 640, 'test statistic', 'sub', 'font-size:22px')
body += text('r0', 1220, 70, 'What the areas mean', 'step')
body += text('ra', 1220, 125, '<span style="color:#c39a3d">■</span> α: reject H₀ although it is true (Type I error)', 'note', 'width:350px;white-space:normal')
body += text('rb', 1220, 230, '<span style="color:#1f5f99">■</span> β: keep H₀ although it is false (Type II error)', 'note', 'width:350px;white-space:normal')
body += text('rp', 1220, 335, '<span style="color:#7fa7cc">■</span> Power = 1 − β: correctly reject a false H₀', 'note', 'width:350px;white-space:normal')
body += text('rs', 1220, 470, 'Smaller α (0.05 → 0.01) → critical value moves right → β grows, power falls.', 'note', f'width:350px;white-space:normal;color:{NAVY};font-weight:600')
js = draw('c0', 0.3, 1.2) + show('l0', 1.0) + show('lab', 1.0)
js += draw('c1', 1.6, 1.2) + show('l1', 2.4)
js += show('ga', 3.0, 0.6) + show('r0', 3.0, dy=8) + show('ra', 3.4, dy=8) + show('rb', 4.0, dy=8) + show('rp', 4.6, dy=8)
js += f'      tl.to("#ga", {{ opacity: 0, duration: 0.6 }}, 7.0);\n' + show('gb', 7.2, 0.6) + show('rs', 7.4, dy=8)
write('fig2_errors_and_power', 11, body, js)


# ---------------------------------------------------------------- Fig 3: critical value vs p-value (two-tailed, z = 2.10)
Z0, ZC = 2.10, 1.96
A = Axes(90, 150, 1020, 420, -3.6, 3.6, 0, 0.44)
inner = A.axis([-3, -2, -1, 0, 1, 2, 3], lambda t: f'{t:d}', size=20)
inner += f'<path id="mid" d="{A.area(phi, -ZC, ZC)}" fill="{MID}" opacity="0"/>'
g = '<g id="al" opacity="0">'
for a, b in ((-3.6, -ZC), (ZC, 3.6)):
    g += f'<path d="{A.area(phi, a, b)}" fill="{GOLD}" opacity="0.95"/>'
for s in (-1, 1):
    g += f'<line x1="{A.X(s * ZC)}" y1="{A.Y(0.33)}" x2="{A.X(s * ZC)}" y2="{A.Y(0)}" stroke="{NAVY}" stroke-width="3" stroke-dasharray="8 6"/>'
    g += f'<text x="{A.X(s * ZC) - s * 8}" y="{A.Y(0.30)}" font-family="Montserrat" font-weight="700" font-size="21" fill="{NAVY}" text-anchor="{"start" if s < 0 else "end"}">{"−" if s < 0 else "+"}1.96</text>'
g += f'<text x="{A.X(-3.0)}" y="{A.Y(0.07)}" font-family="Open Sans" font-weight="600" font-size="20" fill="#8a6d1f" text-anchor="middle">α/2 = 0.025</text>'
g += f'<text x="{A.X(3.0)}" y="{A.Y(0.07)}" font-family="Open Sans" font-weight="600" font-size="20" fill="#8a6d1f" text-anchor="middle">α/2 = 0.025</text>'
g += '</g>'
inner += g
g = '<g id="pv" opacity="0">'
for a, b in ((-3.6, -Z0), (Z0, 3.6)):
    g += f'<path d="{A.area(phi, a, b)}" fill="{RED}" opacity="0.9"/>'
g += f'<text x="{A.X(-2.75)}" y="{A.Y(0.13)}" font-family="Open Sans" font-weight="600" font-size="20" fill="{RED}" text-anchor="middle">0.0179</text>'
g += f'<text x="{A.X(2.75)}" y="{A.Y(0.13)}" font-family="Open Sans" font-weight="600" font-size="20" fill="{RED}" text-anchor="middle">0.0179</text>'
g += '</g>'
inner += g
inner += f'<g id="zl" opacity="0"><line x1="{A.X(Z0)}" y1="{A.Y(0.40)}" x2="{A.X(Z0)}" y2="{A.Y(0)}" stroke="{RED}" stroke-width="4"/>'
inner += f'<text x="{A.X(Z0) + 10}" y="{A.Y(0.38)}" font-family="Montserrat" font-weight="700" font-size="23" fill="{RED}" text-anchor="start">z = 2.10</text></g>'
inner += f'<path id="nc" d="{A.curve(phi, -3.6, 3.6)}" fill="none" stroke="{NAVY}" stroke-width="4.5" stroke-dasharray="3000" stroke-dashoffset="3000"/>'
body = card(40, 40, 1120, 660) + card(1190, 40, 410, 660) + svg(inner)
body += '        <div class="lbl abs" style="left:80px;top:66px;color:#003e67;font-size:28px">Two-tailed test, α = 0.05, z = 2.10</div>\n'
body += text('lab', 590, 640, 'z', 'sub', 'font-size:22px')
body += text('a0', 1220, 70, 'A: Critical value', 'step')
body += text('a1', 1220, 115, '|z| = 2.10 &gt; 1.96<br>z is in the rejection region', 'note', 'width:350px;white-space:normal')
body += text('a2', 1220, 200, '→ reject H₀', 'rt', f'color:{RED}')
body += text('b0', 1220, 290, 'B: p-value', 'step')
body += text('b1', 1220, 335, 'p = 2 · 0.0179 = 0.0357<br>0.0357 &lt; α = 0.05', 'note', 'width:350px;white-space:normal')
body += text('b2', 1220, 420, '→ reject H₀', 'rt', f'color:{RED}')
body += text('c0', 1220, 520, 'Both methods always give the same decision.', 'note', f'width:350px;white-space:normal;color:{NAVY};font-weight:600')
js = draw('nc', 0.3, 1.2) + show('lab', 1.0) + show('mid', 1.2, 0.5, op=0.55)
js += show('al', 1.8, 0.5) + show('zl', 2.6, 0.4, dy=-10)
js += show(['a0', 'a1'], 3.2, dy=8) + show('a2', 4.0, dy=8)
js += f'      tl.to("#al", {{ opacity: 0.35, duration: 0.5 }}, 5.2);\n' + show('pv', 5.4, 0.6)
js += show(['b0', 'b1'], 6.0, dy=8) + show('b2', 6.8, dy=8)
js += f'      tl.to("#al", {{ opacity: 1, duration: 0.5 }}, 7.8);\n' + show('c0', 8.4, dy=8)
write('fig3_two_methods', 11, body, js)


# ---------------------------------------------------------------- Fig 4: which test should I use?
def node(id_, x, y, w, h, html, bg, fg, size=24):
    return (f'        <div id="{id_}" class="abs" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;opacity:0;border-radius:18px;'
            f'background:{bg};color:{fg};display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;'
            f'font:700 {size}px Montserrat;line-height:1.3;padding:0 14px">{html}</div>\n')


def edge(id_, x1, y1, x2, y2, label='', lx=0, ly=0):
    s = f'<g id="{id_}" opacity="0"><path d="M{x1},{y1} L{x1},{(y1 + y2) / 2} L{x2},{(y1 + y2) / 2} L{x2},{y2}" fill="none" stroke="{MUTED}" stroke-width="3"/>'
    s += f'<path d="M{x2 - 9},{y2 - 14} L{x2},{y2} L{x2 + 9},{y2 - 14}" fill="none" stroke="{MUTED}" stroke-width="3"/>'
    if label:
        s += f'<text x="{lx}" y="{ly}" font-family="Open Sans" font-weight="600" font-size="22" fill="{TEXT}" text-anchor="middle">{label}</text>'
    return s + '</g>'


PALEN, GOLDP = '#eef2f6', '#f1e4c6'
body = card(40, 40, 1560, 660)
body += node('q1', 620, 80, 400, 90, 'What is the claim about?', NAVY, '#fff')
body += node('pr', 180, 290, 380, 80, 'a proportion π', PALEN, NAVY)
body += node('mu', 1080, 290, 380, 80, 'a mean μ', PALEN, NAVY)
body += node('q2', 1080, 430, 380, 80, 'Is σ known?', NAVY, '#fff')
body += node('zp', 180, 560, 380, 100, 'z-test for a proportion<span style="font:600 19px Open Sans;margin-top:4px">z = (p − π₀) / σ<sub>p</sub></span>', GOLDP, '#5a4513', 24)
body += node('zm', 820, 580, 330, 100, 'z-test for a mean<span style="font:600 19px Open Sans;margin-top:4px">σ known</span>', GOLDP, '#5a4513', 24)
body += node('tm', 1240, 580, 330, 100, 't-test for a mean<span style="font:600 19px Open Sans;margin-top:4px">σ unknown, df = n − 1</span>', GOLDP, '#5a4513', 24)
inner = edge('e1', 820, 170, 370, 290, 'proportion', 560, 222)
inner += edge('e2', 820, 170, 1270, 290, 'mean', 1080, 222)
inner += edge('e3', 1270, 370, 1270, 430)
inner += edge('e4', 1270, 510, 985, 580, 'yes', 1110, 538)
inner += edge('e5', 1270, 510, 1405, 580, 'no', 1360, 538)
inner += edge('e6', 370, 370, 370, 560)
body = body + svg(inner).replace('<svg ', '<svg style="z-index:0" ', 1)
js = show('q1', 0.3, dy=8)
js += show('e1', 1.0, 0.4) + show('pr', 1.3, dy=8) + show('e6', 1.9, 0.4) + show('zp', 2.2, dy=8)
js += show('e2', 3.2, 0.4) + show('mu', 3.5, dy=8) + show('e3', 4.1, 0.3) + show('q2', 4.3, dy=8)
js += show('e4', 5.2, 0.4) + show('zm', 5.5, dy=8) + show('e5', 6.3, 0.4) + show('tm', 6.6, dy=8)
write('fig4_which_test', 10, body, js)
