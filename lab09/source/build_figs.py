import random
from figlib import *

# ---------------------------------------------------------------- Fig 1: three scatter plots (positive, negative, none)
random.seed(7)


def corr(xs, ys):
    n = len(xs); mx = sum(xs) / n; my = sum(ys) / n
    sxy = sum((a - mx) * (b - my) for a, b in zip(xs, ys))
    sxx = sum((a - mx) ** 2 for a in xs); syy = sum((b - my) ** 2 for b in ys)
    return sxy / (sxx * syy) ** 0.5, sxy / sxx, my - sxy / sxx * mx


PANELS = [('pos', 'Positive relationship', lambda x: 2 + 0.75 * x, 0.9, 'hours studied', 'exam score'),
          ('neg', 'Negative relationship', lambda x: 9 - 0.7 * x, 1.0, 'screen time', 'GPA'),
          ('non', 'No relationship', lambda x: 5, 2.0, 'shoe size', 'exam score')]
body, inner, js = '', '', ''
for i, (k, title, f, noise, xl, yl) in enumerate(PANELS):
    x0 = 30 + i * 535
    body += card(x0, 30, 515, 640)
    A = Axes(x0 + 50, 130, 430, 400, 0, 10, 0, 10)
    xs = [0.6 + 8.8 * j / 17 + random.uniform(-0.25, 0.25) for j in range(18)]
    while True:
        ys = [min(9.6, max(0.4, f(x) + random.gauss(0, noise))) for x in xs]
        r, b1, b0 = corr(xs, ys)
        if k != 'non' or abs(r) < 0.06:
            break
    inner += f'<line x1="{A.X(0)}" y1="{A.Y(0)}" x2="{A.X(10)}" y2="{A.Y(0)}" stroke="{MUTED}" stroke-width="3"/>'
    inner += f'<line x1="{A.X(0)}" y1="{A.Y(0)}" x2="{A.X(0)}" y2="{A.Y(10)}" stroke="{MUTED}" stroke-width="3"/>'
    inner += f'<text x="{A.X(5)}" y="{A.Y(0) + 40}" font-family="Open Sans" font-weight="600" font-size="22" fill="{TEXT}" text-anchor="middle">X: {xl}</text>'
    inner += f'<text x="{A.X(0) - 14}" y="{A.Y(10) - 14}" font-family="Open Sans" font-weight="600" font-size="22" fill="{TEXT}" text-anchor="start">Y: {yl}</text>'
    g = f'<g id="p{k}" opacity="0">' + ''.join(f'<circle cx="{A.X(a):.1f}" cy="{A.Y(b):.1f}" r="9" fill="{BLUE}" opacity="0.85"/>' for a, b in zip(xs, ys)) + '</g>'
    inner += g
    inner += (f'<line id="l{k}" x1="{A.X(0.3):.1f}" y1="{A.Y(b0 + b1 * 0.3):.1f}" x2="{A.X(9.7):.1f}" y2="{A.Y(b0 + b1 * 9.7):.1f}" '
              f'stroke="{RED}" stroke-width="5" stroke-dasharray="3000" stroke-dashoffset="3000"/>')
    body += text(f't{k}', x0 + 30, 58, title, 'lbl', f'color:{NAVY}')
    body += text(f'r{k}', x0 + 30, 600, f'r = {r:.2f}', 'eq', f'color:{RED}')
    js += show(f't{k}', 0.2 + i * 0.3, dy=8)
    js += show(f'p{k}', 0.8 + i * 1.6, 0.8)
    js += draw(f'l{k}', 1.6 + i * 1.6, 0.9)
    js += show(f'r{k}', 2.3 + i * 1.6, dy=8)
body = svg(inner).replace('<svg ', '<svg style="z-index:1" ', 1) + body
write('fig1_scatter_types', 8, body, js)

# ---------------------------------------------------------------- Fig 2: the regression line and its parts
B0, B1, XI_, YI = 2.0, 0.6, 6.5, 8.6
A = Axes(120, 80, 980, 560, 0, 10, 0, 10)
f = lambda x: B0 + B1 * x
inner = f'<line x1="{A.X(0)}" y1="{A.Y(0)}" x2="{A.X(10)}" y2="{A.Y(0)}" stroke="{MUTED}" stroke-width="3"/>'
inner += f'<line x1="{A.X(0)}" y1="{A.Y(0)}" x2="{A.X(0)}" y2="{A.Y(10)}" stroke="{MUTED}" stroke-width="3"/>'
inner += f'<text x="{A.X(10)}" y="{A.Y(0) + 40}" font-family="Montserrat" font-weight="700" font-size="26" fill="{TEXT}" text-anchor="end">X</text>'
inner += f'<text x="{A.X(0) - 24}" y="{A.Y(10)}" font-family="Montserrat" font-weight="700" font-size="26" fill="{TEXT}" text-anchor="end">Y</text>'
random.seed(3)
pts = [(x, f(x) + random.gauss(0, 0.9)) for x in [0.8, 1.6, 2.5, 3.1, 4.0, 4.8, 5.6, 7.4, 8.2, 9.0, 9.6]]
inner += '<g id="pts" opacity="0">' + ''.join(f'<circle cx="{A.X(a):.1f}" cy="{A.Y(b):.1f}" r="9" fill="{BLUE}" opacity="0.55"/>' for a, b in pts) + '</g>'
inner += (f'<line id="ln" x1="{A.X(0)}" y1="{A.Y(f(0))}" x2="{A.X(10)}" y2="{A.Y(f(10))}" stroke="{RED}" stroke-width="5" '
          f'stroke-dasharray="3000" stroke-dashoffset="3000"/>')
inner += f'<text id="lnl" opacity="0" x="{A.X(8.9)}" y="{A.Y(f(8.9)) + 46}" font-family="Open Sans" font-weight="600" font-size="24" fill="{RED}" text-anchor="middle">Y = β₀ + β₁X</text>'
# intercept
inner += (f'<g id="b0" opacity="0"><circle cx="{A.X(0)}" cy="{A.Y(B0)}" r="11" fill="{GOLD}"/>'
          f'<text x="{A.X(0) + 22}" y="{A.Y(B0) + 34}" font-family="Montserrat" font-weight="700" font-size="24" fill="#8a6d1f">intercept β₀</text></g>')
# slope triangle between x=2 and x=3.5 (run shown as "1 unit")
xa, xb = 2.0, 3.6
inner += (f'<g id="b1" opacity="0"><path d="M{A.X(xa)},{A.Y(f(xa))} L{A.X(xb)},{A.Y(f(xa))} L{A.X(xb)},{A.Y(f(xb))}" fill="none" stroke="{GOLD}" stroke-width="3.5" stroke-dasharray="9 6"/>'
          f'<text x="{(A.X(xa) + A.X(xb)) / 2}" y="{A.Y(f(xa)) + 30}" font-family="Open Sans" font-weight="600" font-size="21" fill="#8a6d1f" text-anchor="middle">+1 unit of X</text>'
          f'<text x="{A.X(xb) + 14}" y="{(A.Y(f(xa)) + A.Y(f(xb))) / 2 + 8}" font-family="Montserrat" font-weight="700" font-size="23" fill="#8a6d1f">slope β₁</text></g>')
# observed, predicted, error at x_i
inner += f'<line id="xi" opacity="0" x1="{A.X(XI_)}" y1="{A.Y(0)}" x2="{A.X(XI_)}" y2="{A.Y(f(XI_))}" stroke="{MUTED}" stroke-width="2" stroke-dasharray="6 6"/>'
inner += f'<text id="xil" opacity="0" x="{A.X(XI_)}" y="{A.Y(0) + 34}" font-family="Montserrat" font-weight="700" font-size="24" fill="{TEXT}" text-anchor="middle">xᵢ</text>'
inner += f'<circle id="pred" opacity="0" cx="{A.X(XI_)}" cy="{A.Y(f(XI_))}" r="12" fill="{RED}"/>'
inner += f'<circle id="obs" opacity="0" cx="{A.X(XI_)}" cy="{A.Y(YI)}" r="12" fill="{NAVY}"/>'
inner += (f'<g id="err" opacity="0"><line x1="{A.X(XI_)}" y1="{A.Y(YI) + 12}" x2="{A.X(XI_)}" y2="{A.Y(f(XI_)) - 12}" stroke="{GOLD}" stroke-width="5"/>'
          f'<text x="{A.X(XI_) - 18}" y="{(A.Y(YI) + A.Y(f(XI_))) / 2 + 8}" font-family="Montserrat" font-weight="700" font-size="26" fill="#8a6d1f" text-anchor="end">εᵢ</text></g>')
body = card(40, 30, 1120, 680) + card(1190, 30, 410, 680) + svg(inner)
items = [('k0', 'The parts of the model', 'step', 60),
         ('k1', '<span style="color:#1f5f99">●</span> observed data points (xᵢ, yᵢ)', 'note', 120),
         ('k2', '<span style="color:#b34739">━</span> the regression line: the value of Y we expect for each X', 'note', 190),
         ('k3', '<span style="color:#c39a3d">●</span> β₀: the value of Y on the line when X = 0', 'note', 280),
         ('k4', '<span style="color:#c39a3d">◢</span> β₁: how much Y changes when X increases by 1 unit', 'note', 365),
         ('k5', '<span style="color:#b34739">●</span> predicted value on the line<br><span style="color:#003e67">●</span> observed value yᵢ', 'note', 455),
         ('k6', '<span style="color:#c39a3d">┃</span> εᵢ = observed − predicted: the random error', 'note', 560)]
for id_, html, cls, y in items:
    body += text(id_, 1220, y, html, cls, 'width:350px;white-space:normal')
js = show('pts', 0.2, 0.6) + show(['k0', 'k1'], 0.4, dy=8)
js += draw('ln', 1.2, 1.2) + show(['lnl', 'k2'], 2.0, dy=8)
js += show(['b0', 'k3'], 3.2, dy=8) + show(['b1', 'k4'], 4.4, dy=8)
js += show(['xi', 'xil'], 5.6, 0.4) + show('pred', 6.0, dy=-8) + show(['obs', 'k5'], 6.6, dy=-8)
js += show(['err', 'k6'], 7.6, dy=8)
write('fig2_regression_parts', 10, body, js)
