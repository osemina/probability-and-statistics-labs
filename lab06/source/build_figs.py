import math, random
from common import write

NAVY, BLUE, LIGHT, PALE, GOLD, GOLDPALE, PANEL, RED, TEXT, MUTED = (
    '#003e67', '#1f5f99', '#c9d6e3', '#eef2f6', '#c39a3d', '#f1e4c6', '#f3f3f0', '#b34739', '#202020', '#5f6368')
MID = '#7fa7cc'


def phi(z):
    return math.exp(-z * z / 2) / math.sqrt(2 * math.pi)


class Axes:
    """Maps data coordinates to pixels inside a plotting box."""
    def __init__(self, x0, y0, w, h, xmin, xmax, ymin, ymax):
        self.x0, self.y0, self.w, self.h = x0, y0, w, h
        self.xmin, self.xmax, self.ymin, self.ymax = xmin, xmax, ymin, ymax

    def X(self, x):
        return self.x0 + (x - self.xmin) / (self.xmax - self.xmin) * self.w

    def Y(self, y):
        return self.y0 + self.h - (y - self.ymin) / (self.ymax - self.ymin) * self.h

    def curve(self, f, a, b, n=200):
        pts = [(a + (b - a) * i / n) for i in range(n + 1)]
        return 'M' + ' L'.join(f'{self.X(x):.1f},{self.Y(min(f(x), self.ymax)):.1f}' for x in pts)

    def area(self, f, a, b, n=160):
        pts = [(a + (b - a) * i / n) for i in range(n + 1)]
        top = ' L'.join(f'{self.X(x):.1f},{self.Y(min(f(x), self.ymax)):.1f}' for x in pts)
        return f'M{self.X(a):.1f},{self.Y(0):.1f} L{top} L{self.X(b):.1f},{self.Y(0):.1f} Z'

    def axis(self, ticks, fmt=str, color=MUTED, size=22):
        y = self.Y(self.ymin)
        s = f'<line x1="{self.x0}" y1="{y}" x2="{self.x0 + self.w}" y2="{y}" stroke="{color}" stroke-width="3"/>'
        for t in ticks:
            x = self.X(t)
            s += f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y + 10}" stroke="{color}" stroke-width="2"/>'
            s += f'<text x="{x}" y="{y + 34}" font-family="Open Sans" font-weight="600" font-size="{size}" fill="{TEXT}" text-anchor="middle">{fmt(t)}</text>'
        return s


def svg(inner, defs=''):
    return f'        <svg class="abs" style="left:0;top:0" width="1640" height="740"><defs>{defs}</defs>{inner}</svg>\n'


def text(id_, x, y, html, cls='sub', style=''):
    return f'        <div id="{id_}" class="{cls} abs" style="left:{x}px;top:{y}px;opacity:0;{style}">{html}</div>\n'


def card(x, y, w, h):
    return f'        <div class="abs card" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"></div>\n'


def show(ids, t, dur=0.4, dy=0, op=1):
    ids = ids if isinstance(ids, list) else [ids]
    sel = ', '.join(f'"#{i}"' for i in ids)
    if dy:
        return f'      tl.fromTo([{sel}], {{ opacity: 0, y: {dy} }}, {{ opacity: {op}, y: 0, duration: {dur} }}, {t});\n'
    return f'      tl.to([{sel}], {{ opacity: {op}, duration: {dur} }}, {t});\n'


def draw(id_, t, dur=1.2):
    return f'      tl.fromTo("#{id_}", {{ attr: {{ "stroke-dashoffset": 3000 }} }}, {{ attr: {{ "stroke-dashoffset": 0 }}, duration: {dur}, ease: "power1.inOut" }}, {t});\n'


# ---------------------------------------------------------------- Fig 1: the Central Limit Theorem in three populations
def normal_pdf(m, s):
    return lambda x: phi((x - m) / s) / s


def mean_unif(n):
    if n == 1:
        return lambda x: 1.0 if 0 <= x <= 1 else 0.0
    if n == 2:
        return lambda x: 4 * x if 0 <= x <= 0.5 else (4 * (1 - x) if 0.5 < x <= 1 else 0.0)
    if n == 5:
        def ih(t):
            if t < 0 or t > n:
                return 0.0
            return sum((-1) ** k * math.comb(n, k) * (t - k) ** (n - 1) for k in range(int(math.floor(t)) + 1)) / math.factorial(n - 1)
        return lambda x: n * ih(n * x)
    return normal_pdf(0.5, math.sqrt(1 / 12 / n))


def mean_exp(n):
    return lambda x: 0.0 if x <= 0 else math.exp(n * math.log(n) + (n - 1) * math.log(x) - n * x - math.lgamma(n))


panels = [
    ('A', 'Normal population', normal_pdf(0, 1), lambda n: normal_pdf(0, 1 / math.sqrt(n)), -3, 3, [-2, 0, 2]),
    ('B', 'Uniform population', mean_unif(1), mean_unif, 0, 1, [0, 0.5, 1]),
    ('C', 'Exponential population', mean_exp(1), mean_exp, 0, 3.5, [0, 1, 2, 3]),
]
NS = [(2, LIGHT, '8 6'), (5, MID, '10 5'), (30, NAVY, '')]
inner, body = '', ''
js = ''
for i, (tag, name, pop, samp, a, b, ticks) in enumerate(panels):
    x0 = 40 + i * 530
    body += card(x0, 40, 510, 600)
    fmt = (lambda t: f'{t:g}')
    P = Axes(x0 + 40, 120, 430, 120, a, b, 0, 1.25 * max(pop(a + (b - a) * k / 200) for k in range(201)))
    inner += P.axis(ticks, fmt, size=18)
    inner += f'<path id="pa{i}" d="{P.area(pop, a, b)}" fill="{PALE}" opacity="0"/>'
    inner += f'<path id="pc{i}" d="{P.curve(pop, a, b)}" fill="none" stroke="{GOLD}" stroke-width="4" stroke-dasharray="3000" stroke-dashoffset="3000"/>'
    peak = max(samp(30)(a + (b - a) * k / 400) for k in range(401))
    S = Axes(x0 + 40, 360, 430, 230, a, b, 0, 1.12 * peak)
    inner += S.axis(ticks, fmt, size=18)
    for j, (n, col, dash) in enumerate(NS):
        inner += f'<path id="s{i}{j}" d="{S.curve(samp(n), a, b, 400)}" fill="none" stroke="{col}" stroke-width="{4 if n == 30 else 3.5}" ' \
                 f'{"stroke-dasharray=" + chr(34) + dash + chr(34) if dash else ""} opacity="0"/>'
    body += f'        <div class="lbl abs" style="left:{x0 + 30}px;top:58px;color:#003e67;font-size:24px">Panel {tag}: {name}</div>\n'
    body += f'        <div class="sub abs" style="left:{x0 + 30}px;top:96px;font-size:18px">population: values of X</div>\n'
    body += f'        <div class="sub abs" style="left:{x0 + 30}px;top:300px;font-size:18px">sampling distribution of the sample mean X̄</div>\n'
body += text('n2', 60, 668, 'n = 2', 'rt', f'font-size:22px;color:{MUTED}')
body += text('n5', 180, 668, 'n = 5', 'rt', f'font-size:22px;color:{BLUE}')
body += text('n30', 300, 668, 'n = 30', 'rt', f'font-size:22px;color:{NAVY}')
body += text('msg', 600, 668, 'The larger n, the more bell-shaped and the narrower the distribution of X̄.', 'rt', 'font-size:22px;color:#003e67')
for i in range(3):
    js += f'      tl.to("#pa{i}", {{ opacity: 1, duration: 0.6 }}, {0.3 + 0.2 * i});\n' + draw(f'pc{i}', 0.3 + 0.2 * i, 1.2)
js += show(['s00', 's10', 's20', 'n2'], 2.2, 0.6)
js += show(['s01', 's11', 's21', 'n5'], 4.4, 0.6)
js += show(['s02', 's12', 's22', 'n30'], 6.6, 0.6)
js += show('msg', 8.4, dy=8)
write('fig1_clt_three_populations', 11, body + svg(inner), js)

# ---------------------------------------------------------------- Fig 2: the parts of a confidence interval
A = Axes(140, 300, 1360, 10, 166, 178, 0, 1)
y = 330
inner = A.axis(list(range(166, 179)), lambda t: f'{t}', size=22)
inner = inner.replace(f'y1="{A.Y(0)}"', f'y1="{y + 120}"', 1)
inner = f'<line x1="{A.x0}" y1="{y + 120}" x2="{A.x0 + A.w}" y2="{y + 120}" stroke="{MUTED}" stroke-width="3"/>'
for t in range(166, 179):
    x = A.X(t)
    inner += f'<line x1="{x}" y1="{y + 120}" x2="{x}" y2="{y + 132}" stroke="{MUTED}" stroke-width="2"/>'
    inner += f'<text x="{x}" y="{y + 160}" font-family="Open Sans" font-weight="600" font-size="22" fill="{TEXT}" text-anchor="middle">{t}</text>'
inner += f'<line id="bar" x1="{A.X(170)}" y1="{y}" x2="{A.X(174)}" y2="{y}" stroke="{BLUE}" stroke-width="12" stroke-linecap="round" stroke-dasharray="3000" stroke-dashoffset="3000"/>'
for k, v in (('lo', 170), ('hi', 174)):
    inner += f'<line id="{k}" x1="{A.X(v)}" y1="{y - 40}" x2="{A.X(v)}" y2="{y + 120}" stroke="{NAVY}" stroke-width="4" opacity="0"/>'
inner += f'<polygon id="pe" points="{A.X(172)},{y - 22} {A.X(172) + 22},{y} {A.X(172)},{y + 22} {A.X(172) - 22},{y}" fill="{GOLD}" stroke="#fff" stroke-width="3" opacity="0"/>'
for k, (a, b) in (('me1', (170, 172)), ('me2', (172, 174))):
    inner += f'<g id="{k}" opacity="0"><line x1="{A.X(a) + 4}" y1="{y + 60}" x2="{A.X(b) - 4}" y2="{y + 60}" stroke="{GOLD}" stroke-width="3"/>' \
             f'<line x1="{A.X(a) + 4}" y1="{y + 50}" x2="{A.X(a) + 4}" y2="{y + 70}" stroke="{GOLD}" stroke-width="3"/><line x1="{A.X(b) - 4}" y1="{y + 50}" x2="{A.X(b) - 4}" y2="{y + 70}" stroke="{GOLD}" stroke-width="3"/>' \
             f'<text x="{(A.X(a) + A.X(b)) / 2}" y="{y + 92}" font-family="Open Sans" font-weight="600" font-size="20" fill="#8a6d1f" text-anchor="middle">margin of error = 2</text></g>'
inner += f'<g id="wd" opacity="0"><line x1="{A.X(170)}" y1="{y + 210}" x2="{A.X(174)}" y2="{y + 210}" stroke="{NAVY}" stroke-width="3" marker-start="url(#ar)" marker-end="url(#ar)"/>' \
         f'<text x="{A.X(172)}" y="{y + 245}" font-family="Montserrat" font-weight="700" font-size="24" fill="{NAVY}" text-anchor="middle">width = 4 cm</text></g>'
defs = f'<marker id="ar" viewBox="0 0 10 10" refX="5" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="{NAVY}"/></marker>'
body = card(40, 40, 1560, 660) + svg(inner, defs)
body += '        <div class="lbl abs" style="left:80px;top:66px;color:#003e67;font-size:28px">95% confidence interval for the mean height of students</div>\n'
body += text('t0', 80, 112, 'sample mean x̄ = 172 cm,  interval from 170 cm to 174 cm', 'sub', 'font-size:22px')
body += text('tpe', A.X(172) - 150, y - 86, 'point estimate x̄ = 172', 'rt', f'font-size:22px;color:#8a6d1f;width:300px;text-align:center')
body += text('tlo', A.X(170) - 250, y - 70, 'lower confidence<br>limit = 170', 'rt', f'font-size:22px;color:{NAVY};text-align:right;width:230px;white-space:normal')
body += text('thi', A.X(174) + 20, y - 70, 'upper confidence<br>limit = 174', 'rt', f'font-size:22px;color:{NAVY};width:230px;white-space:normal')
body += text('msg', 80, 640, '“We are 95% confident that the true mean height μ is between 170 and 174 cm.”', 'rt', 'font-size:23px;color:#003e67')
js = show(['pe', 'tpe'], 0.5) + draw('bar', 1.4, 1.0) + show(['lo', 'tlo'], 2.6) + show(['hi', 'thi'], 3.2)
js += show('me1', 4.2) + show('me2', 4.8) + show('wd', 5.8) + show('t0', 6.6) + show('msg', 7.4, dy=8)
write('fig2_ci_parts', 10, body, js)

# ---------------------------------------------------------------- Fig 3: critical values and the confidence level
A = Axes(110, 170, 1000, 400, -3.6, 3.6, 0, 0.44)
inner = A.axis([-3, -2, -1, 0, 1, 2, 3], lambda t: f'{t:d}')
LEVELS = [('95', 1.96, '0.025'), ('90', 1.645, '0.05'), ('99', 2.576, '0.005')]
for k, z, half in LEVELS:
    inner += f'<g id="g{k}" opacity="0"><path d="{A.area(phi, -z, z)}" fill="{MID}" opacity="0.75"/>'
    inner += f'<path d="{A.area(phi, -3.6, -z)}" fill="{GOLD}" opacity="0.85"/><path d="{A.area(phi, z, 3.6)}" fill="{GOLD}" opacity="0.85"/>'
    for s in (-1, 1):
        inner += f'<line x1="{A.X(s * z)}" y1="{A.Y(0.30)}" x2="{A.X(s * z)}" y2="{A.Y(0)}" stroke="{NAVY}" stroke-width="3" stroke-dasharray="8 6"/>'
        inner += f'<text x="{A.X(s * z)}" y="{A.Y(0.30) - 12}" font-family="Montserrat" font-weight="700" font-size="22" fill="{NAVY}" text-anchor="middle">{"−" if s < 0 else "+"}{z:g}</text>'
    inner += f'<text x="{A.X(0)}" y="{A.Y(0.17)}" font-family="Montserrat" font-weight="700" font-size="34" fill="#fff" text-anchor="middle">{k}%</text>'
    for s, xx in ((-1, -3.05), (1, 3.05)):
        inner += f'<text x="{A.X(xx)}" y="{A.Y(0.075)}" font-family="Open Sans" font-weight="600" font-size="20" fill="#8a6d1f" text-anchor="middle">α/2 = {half}</text>'
    inner += '</g>'
inner += f'<path id="nc" d="{A.curve(phi, -3.6, 3.6)}" fill="none" stroke="{NAVY}" stroke-width="5" stroke-dasharray="3000" stroke-dashoffset="3000"/>'
body = card(40, 40, 1120, 660) + svg(inner)
body += '        <div class="lbl abs" style="left:80px;top:66px;color:#003e67;font-size:28px">Standard normal curve and the critical value Z<sub>α/2</sub></div>\n'
body += text('zl', 520, 640, 'z', 'sub', 'font-size:22px')
body += card(1190, 40, 410, 660)
body += text('r0', 1220, 70, 'Confidence level → Z<sub>α/2</sub>', 'step')
for j, (k, z, half) in enumerate([('90', 1.645, '0.05'), ('95', 1.96, '0.025'), ('99', 2.576, '0.005')]):
    body += text(f'row{k}', 1220, 130 + j * 60, f'{k}%:  α/2 = {half},  Z<sub>α/2</sub> = {z:g}', 'rt', 'font-size:23px')
body += text('m1', 1220, 330, 'Middle area = confidence level (1 − α).', 'note', 'width:350px')
body += text('m2', 1220, 420, 'Each tail = α/2.', 'note', 'width:350px')
body += text('m3', 1220, 490, 'Higher confidence → larger Z<sub>α/2</sub> → wider interval.', 'note', f'width:350px;color:{NAVY};font-weight:600')
js = draw('nc', 0.3, 1.4) + show('zl', 1.0)
js += show('g95', 1.8, 0.6) + show(['r0', 'row95', 'm1', 'm2'], 2.2, dy=8)
js += f'      tl.to("#g95", {{ opacity: 0, duration: 0.4 }}, 4.6);\n' + show(['g90', 'row90'], 4.8, 0.5)
js += f'      tl.to("#g90", {{ opacity: 0, duration: 0.4 }}, 6.4);\n' + show(['g99', 'row99'], 6.6, 0.5)
js += f'      tl.to("#g99", {{ opacity: 0, duration: 0.4 }}, 8.2);\n' + show('g95', 8.4, 0.5) + show('m3', 8.8, dy=8)
write('fig3_critical_values', 11, body, js)

# ---------------------------------------------------------------- Fig 4: what “95% confident” means (20 samples)
mu, se = 50, 2
me = 1.96 * se
rnd = random.Random(7)
means = []
while True:
    means = [round(rnd.gauss(mu, se), 1) for _ in range(20)]
    miss = [m for m in means if abs(m - mu) > me]
    if len(miss) == 1 and abs(miss[0] - mu) > me + 0.6:
        break
A = Axes(140, 120, 940, 10, 40, 60, 0, 1)
inner = f'<line id="mul" x1="{A.X(mu)}" y1="118" x2="{A.X(mu)}" y2="640" stroke="{TEXT}" stroke-width="3" stroke-dasharray="8 6" opacity="0"/>'
for t in range(40, 61, 2):
    x = A.X(t)
    inner += f'<line x1="{x}" y1="640" x2="{x}" y2="650" stroke="{MUTED}" stroke-width="2"/><text x="{x}" y="678" font-family="Open Sans" font-weight="600" font-size="20" fill="{TEXT}" text-anchor="middle">{t}</text>'
inner += f'<line x1="{A.x0}" y1="640" x2="{A.x0 + A.w}" y2="640" stroke="{MUTED}" stroke-width="3"/>'
for i, m in enumerate(means):
    yy = 130 + i * 25
    hit = abs(m - mu) <= me
    col = BLUE if hit else RED
    inner += f'<g id="iv{i}" opacity="0"><line x1="{A.X(m - me)}" y1="{yy}" x2="{A.X(m + me)}" y2="{yy}" stroke="{col}" stroke-width="5" stroke-linecap="round"/>' \
             f'<circle cx="{A.X(m)}" cy="{yy}" r="6" fill="{GOLD}"/></g>'
body = card(40, 40, 1080, 660) + svg(inner)
body += '        <div class="lbl abs" style="left:80px;top:50px;color:#003e67;font-size:26px">20 samples, 20 different 95% intervals for μ = 50</div>\n'
body += text('mut', A.X(mu) + 10, 88, 'true mean μ = 50', 'rt', 'font-size:20px')
body += card(1150, 40, 450, 660)
body += text('k1', 1180, 80, 'Each sample gives its own x̄ (gold) and its own interval x̄ ± 1.96·σ/√n.', 'note', 'width:390px')
body += text('k2', 1180, 230, '<span style="color:#1f5f99">Blue:</span> the interval contains μ.', 'rt', 'width:390px;white-space:normal')
body += text('k3', 1180, 290, '<span style="color:#b34739">Red:</span> the interval misses μ.', 'rt', 'width:390px;white-space:normal')
body += text('k4', 1180, 380, '19 of 20 intervals contain μ, which is about 95%.', 'eq', 'font-size:26px;width:390px;white-space:normal;line-height:1.35')
body += text('k5', 1180, 500, '“95% confident” describes the method: in the long run, 95% of such intervals catch μ.', 'note', 'width:390px')
js = show(['mul', 'mut'], 0.3) + show('k1', 0.6)
for i in range(20):
    js += show(f'iv{i}', 1.2 + 0.25 * i, 0.25)
js += show(['k2', 'k3'], 3.4) + show('k4', 6.6, dy=8) + show('k5', 7.6, dy=8)
write('fig4_twenty_intervals', 10.5, body, js)
print('ok', means)
