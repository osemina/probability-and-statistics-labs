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
