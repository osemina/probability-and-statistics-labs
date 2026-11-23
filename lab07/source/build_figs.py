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
