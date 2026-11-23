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


# ---------------------------------------------------------------- Fig 3: least squares - the line with the smallest SSE
XS, YS = [1, 2, 3, 4, 5], [52, 58, 61, 70, 74]
A = Axes(120, 70, 960, 580, 0, 6, 40, 86)
pxu = 580 / (86 - 40)          # pixels per point on the Y axis
inner = A.axis([0, 1, 2, 3, 4, 5, 6], lambda t: f'{t:d}', size=20)
inner += f'<line x1="{A.X(0)}" y1="{A.Y(40)}" x2="{A.X(0)}" y2="{A.Y(86)}" stroke="{MUTED}" stroke-width="3"/>'
for v in (50, 60, 70, 80):
    inner += f'<text x="{A.X(0) - 12}" y="{A.Y(v) + 7}" font-family="Open Sans" font-weight="600" font-size="20" fill="{TEXT}" text-anchor="end">{v}</text>'
inner += f'<text x="{A.X(6)}" y="{A.Y(40) + 62}" font-family="Open Sans" font-weight="600" font-size="22" fill="{TEXT}" text-anchor="end">x: hours studied</text>'
inner += f'<text x="{A.X(0) + 12}" y="{A.Y(86) + 6}" font-family="Open Sans" font-weight="600" font-size="22" fill="{TEXT}">y: exam score</text>'
STATES = [('s0', 0.0, '#9aa7b4'), ('s1', 3.0, '#9aa7b4'), ('s2', 8.0, '#9aa7b4'), ('s3', 5.6, RED)]
for sid, b1, colr in STATES:
    b0 = 63 - b1 * 3
    g = f'<g id="{sid}" opacity="0">'
    for x, y in zip(XS, YS):
        yh = b0 + b1 * x
        e = y - yh
        side = abs(e) * pxu
        top = A.Y(max(y, yh))
        g += f'<rect x="{A.X(x)}" y="{top:.1f}" width="{side:.1f}" height="{side:.1f}" fill="{GOLD}" opacity="0.30" stroke="{GOLD}" stroke-width="2"/>'
        g += f'<line x1="{A.X(x)}" y1="{A.Y(y)}" x2="{A.X(x)}" y2="{A.Y(yh)}" stroke="{GOLD}" stroke-width="3.5"/>'
    g += f'<line x1="{A.X(0.2)}" y1="{A.Y(b0 + b1 * 0.2)}" x2="{A.X(5.8)}" y2="{A.Y(b0 + b1 * 5.8)}" stroke="{colr}" stroke-width="5"/>'
    g += '</g>'
    inner += g
inner += '<g id="pts">' + ''.join(f'<circle cx="{A.X(x)}" cy="{A.Y(y)}" r="11" fill="{NAVY}"/>' for x, y in zip(XS, YS)) + '</g>'
inner += f'<circle id="mean" opacity="0" cx="{A.X(3)}" cy="{A.Y(63)}" r="12" fill="#ffffff" stroke="{RED}" stroke-width="4"/>'
body = card(40, 30, 1120, 680) + card(1190, 30, 410, 680) + svg(inner)
body += text('h0', 1220, 60, 'Try different lines', 'step')
body += text('h1', 1220, 105, 'Each gold square has area e² (residual²).<br>SSE = the total area of the squares.', 'note', 'width:350px;white-space:normal')
for i, (sid, b1, _) in enumerate(STATES):
    sse = sum((y - (63 - b1 * 3) - b1 * x) ** 2 for x, y in zip(XS, YS))
    col = RED if i == 3 else NAVY
    body += text(f'v{i}', 1220, 275 + i * 75, f'b₁ = {b1:g}: &nbsp; SSE = {sse:.1f}', 'rt', f'color:{col};font-size:26px')
body += text('fin', 1220, 590, 'The smallest SSE: the least squares line ŷ = 46.2 + 5.6x. It passes through (x̄, ȳ) = (3, 63).', 'note', f'width:350px;white-space:normal;color:{RED};font-weight:600')
js = show(['h0', 'h1'], 0.2, dy=8)
for i, (sid, _, _) in enumerate(STATES):
    t0 = 0.9 + i * 2.2
    js += show(sid, t0, 0.5) + show(f'v{i}', t0 + 0.3, dy=8)
    if i < 3:
        js += f'      tl.to("#{sid}", {{ opacity: 0, duration: 0.5 }}, {t0 + 1.8});\n'
js += show('mean', 8.2, 0.4) + show('fin', 8.4, dy=8)
write('fig3_least_squares', 11, body, js)


# ---------------------------------------------------------------- Fig 4: SST = SSR + SSE
A = Axes(120, 70, 960, 580, 0, 6, 40, 86)
inner = A.axis([0, 1, 2, 3, 4, 5, 6], lambda t: f'{t:d}', size=20)
inner += f'<line x1="{A.X(0)}" y1="{A.Y(40)}" x2="{A.X(0)}" y2="{A.Y(86)}" stroke="{MUTED}" stroke-width="3"/>'
for v in (50, 60, 70, 80):
    inner += f'<text x="{A.X(0) - 12}" y="{A.Y(v) + 7}" font-family="Open Sans" font-weight="600" font-size="20" fill="{TEXT}" text-anchor="end">{v}</text>'
inner += f'<text x="{A.X(6)}" y="{A.Y(40) + 62}" font-family="Open Sans" font-weight="600" font-size="22" fill="{TEXT}" text-anchor="end">x: hours studied</text>'
inner += f'<text x="{A.X(0) + 12}" y="{A.Y(86) + 6}" font-family="Open Sans" font-weight="600" font-size="22" fill="{TEXT}">y: exam score</text>'
inner += (f'<g id="mline" opacity="0"><line x1="{A.X(0.2)}" y1="{A.Y(63)}" x2="{A.X(5.8)}" y2="{A.Y(63)}" stroke="#9aa7b4" stroke-width="3" stroke-dasharray="10 8"/>'
          f'<text x="{A.X(5.8)}" y="{A.Y(63) + 30}" font-family="Open Sans" font-weight="700" font-size="22" fill="#6b7a89" text-anchor="end">ȳ = 63</text></g>')
inner += (f'<g id="rline" opacity="0"><line x1="{A.X(0.2)}" y1="{A.Y(46.2 + 5.6 * 0.2)}" x2="{A.X(5.8)}" y2="{A.Y(46.2 + 5.6 * 5.8)}" stroke="{RED}" stroke-width="5"/>'
          f'<text x="{A.X(5.75)}" y="{A.Y(46.2 + 5.6 * 5.8) - 14}" font-family="Open Sans" font-weight="700" font-size="22" fill="{RED}" text-anchor="end">ŷ = 46.2 + 5.6x</text></g>')
xt = 4
def seg(id_, x, y1, y2, col, lab, side):
    tx = A.X(x) + (-14 if side == 'l' else 14)
    anc = 'end' if side == 'l' else 'start'
    return (f'<g id="{id_}" opacity="0"><line x1="{A.X(x)}" y1="{A.Y(y1)}" x2="{A.X(x)}" y2="{A.Y(y2)}" stroke="{col}" stroke-width="9"/>'
            '</g>')
inner += '<g id="pts">' + ''.join(f'<circle cx="{A.X(x)}" cy="{A.Y(y)}" r="11" fill="{NAVY}"/>' for x, y in zip(XS, YS)) + '</g>'
inner += seg('tot', xt - 0.16, 63, 70, NAVY, 'y − ȳ = 7', 'l')
inner += seg('exp', xt, 63, 68.6, GOLD, 'ŷ − ȳ = 5.6', 'r')
inner += seg('une', xt, 68.6, 70, RED, 'y − ŷ = 1.4', 'r')
# R² bar in the side card
bx, by, bw = 1220, 520, 350
inner += (f'<g id="bar" opacity="0"><rect x="{bx}" y="{by}" width="{bw}" height="36" fill="{RED}"/>'
          f'<rect x="{bx}" y="{by}" width="{bw * 0.98:.1f}" height="36" fill="{GOLD}"/>'
          f'<text x="{bx + 12}" y="{by + 25}" font-family="Open Sans" font-weight="700" font-size="20" fill="#ffffff">explained 98%</text></g>')
body = card(40, 30, 1120, 680) + card(1190, 30, 410, 680) + svg(inner)
body += text('h0', 1220, 60, 'One point: x = 4, y = 70', 'step')
body += text('t1', 1220, 115, f'<span style="color:{NAVY}">Total:</span> y − ȳ = 7', 'rt', 'font-size:24px')
body += text('t2', 1220, 165, f'<span style="color:{GOLD}">Explained by the line:</span> ŷ − ȳ = 5.6', 'rt', 'font-size:24px;width:360px;white-space:normal')
body += text('t3', 1220, 245, f'<span style="color:{RED}">Unexplained (residual):</span> y − ŷ = 1.4', 'rt', 'font-size:24px;width:360px;white-space:normal')
body += text('h1', 1220, 335, 'Square and add over all points:', 'note', 'width:350px;white-space:normal;font-weight:600')
body += text('t4', 1220, 410, 'SST = SSR + SSE<br>320 = 313.6 + 6.4', 'rt', f'font-size:26px;color:{NAVY}')
body += text('fin', 1220, 580, 'R² = 313.6 / 320 = 0.98', 'rt', f'font-size:28px;color:{RED}')
js = show('mline', 0.3) + show('rline', 0.9) + show('h0', 1.4, dy=8)
js += show('tot', 2.0) + show('t1', 2.2, dy=8)
js += show('exp', 3.2) + show('t2', 3.4, dy=8)
js += show('une', 4.4) + show('t3', 4.6, dy=8)
js += show(['h1', 't4'], 5.8, dy=8) + show('bar', 7.0, 0.6) + show('fin', 7.4, dy=8)
write('fig4_sst_split', 10, body, js)
