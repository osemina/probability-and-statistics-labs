import math
from common import write

NAVY, BLUE, LIGHT, PALE, GOLD, GOLDPALE, PANEL, RED, TEXT, MUTED = (
    '#003e67', '#1f5f99', '#c9d6e3', '#eef2f6', '#c39a3d', '#f1e4c6', '#f3f3f0', '#b34739', '#202020', '#5f6368')
ORANGE = '#e8a33d'


def phi(z):
    return math.exp(-z * z / 2) / math.sqrt(2 * math.pi)


def Phi(z):
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


class Axes:
    """Maps data coordinates to pixels inside a plotting box."""
    def __init__(self, x0, y0, w, h, xmin, xmax, ymin, ymax):
        self.x0, self.y0, self.w, self.h = x0, y0, w, h
        self.xmin, self.xmax, self.ymin, self.ymax = xmin, xmax, ymin, ymax

    def X(self, x):
        return self.x0 + (x - self.xmin) / (self.xmax - self.xmin) * self.w

    def Y(self, y):
        return self.y0 + self.h - (y - self.ymin) / (self.ymax - self.ymin) * self.h

    def curve(self, f, a, b, n=160):
        pts = [(a + (b - a) * i / n) for i in range(n + 1)]
        return 'M' + ' L'.join(f'{self.X(x):.1f},{self.Y(f(x)):.1f}' for x in pts)

    def area(self, f, a, b, n=120):
        pts = [(a + (b - a) * i / n) for i in range(n + 1)]
        top = ' L'.join(f'{self.X(x):.1f},{self.Y(f(x)):.1f}' for x in pts)
        return f'M{self.X(a):.1f},{self.Y(0):.1f} L{top} L{self.X(b):.1f},{self.Y(0):.1f} Z'

    def axis(self, ticks, fmt=str, color=MUTED):
        y = self.Y(self.ymin)
        s = f'<line x1="{self.x0}" y1="{y}" x2="{self.x0 + self.w}" y2="{y}" stroke="{color}" stroke-width="3"/>'
        for t in ticks:
            x = self.X(t)
            s += f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y + 10}" stroke="{color}" stroke-width="2"/>'
            s += f'<text x="{x}" y="{y + 36}" font-family="Open Sans" font-weight="600" font-size="22" fill="{TEXT}" text-anchor="middle">{fmt(t)}</text>'
        return s


def svg(inner, defs=''):
    return f'        <svg class="abs" style="left:0;top:0" width="1640" height="740"><defs>{defs}</defs>{inner}</svg>\n'


def clip(cid, x, y, h):
    return f'<clipPath id="{cid}"><rect id="{cid}r" x="{x}" y="{y}" width="0" height="{h}"/></clipPath>'


def text(id_, x, y, html, cls='sub', style=''):
    return f'        <div id="{id_}" class="{cls} abs" style="left:{x}px;top:{y}px;opacity:0;{style}">{html}</div>\n'


def card(x, y, w, h):
    return f'        <div class="abs card" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px"></div>\n'


def show(ids, t, dur=0.4, dy=0):
    ids = ids if isinstance(ids, list) else [ids]
    sel = ', '.join(f'"#{i}"' for i in ids)
    if dy:
        return f'      tl.fromTo([{sel}], {{ opacity: 0, y: {dy} }}, {{ opacity: 1, y: 0, duration: {dur} }}, {t});\n'
    return f'      tl.to([{sel}], {{ opacity: 1, duration: {dur} }}, {t});\n'


def draw(id_, t, dur=1.2):
    return f'      tl.fromTo("#{id_}", {{ attr: {{ "stroke-dashoffset": 3000 }} }}, {{ attr: {{ "stroke-dashoffset": 0 }}, duration: {dur}, ease: "power1.inOut" }}, {t});\n'


def reveal(cid, width, t, dur=1.2):
    return f'      tl.to("#{cid}r", {{ attr: {{ width: {width} }}, duration: {dur}, ease: "power1.inOut" }}, {t});\n'


# ---------------------------------------------------------------- Fig 1: PDF and the area under the curve
f = lambda x: 2 * (x + 2) / 5
A = Axes(130, 150, 760, 430, -0.05, 1.05, 0, 1.4)
inner = A.axis([0, 0.2, 0.4, 0.6, 0.8, 1.0], lambda t: f'{t:.1f}')
for yv in (0.4, 0.8, 1.2):
    inner += f'<line x1="{A.x0}" y1="{A.Y(yv)}" x2="{A.x0 + A.w}" y2="{A.Y(yv)}" stroke="{LIGHT}" stroke-width="1.5" stroke-dasharray="6 6"/>'
    inner += f'<text x="{A.x0 - 14}" y="{A.Y(yv) + 7}" font-family="Open Sans" font-size="19" fill="{MUTED}" text-anchor="end">{yv}</text>'
inner += f'<path id="tot" d="{A.area(f, 0, 1)}" fill="{PALE}" opacity="0"/>'
inner += f'<path d="{A.area(f, 0.2, 0.6)}" fill="{BLUE}" opacity="0.55" clip-path="url(#c1)"/>'
inner += f'<path id="pdf" d="{A.curve(f, 0, 1)}" fill="none" stroke="{NAVY}" stroke-width="5" stroke-dasharray="3000" stroke-dashoffset="3000"/>'
inner += f'<line id="pt" x1="{A.X(0.85)}" y1="{A.Y(0)}" x2="{A.X(0.85)}" y2="{A.Y(f(0.85))}" stroke="{RED}" stroke-width="4" opacity="0"/>'
defs = clip('c1', A.X(0.2), A.Y(1.4), A.h + 5)
body = card(40, 40, 900, 660) + svg(inner, defs)
body += '        <div class="lbl abs" style="left:80px;top:66px;color:#003e67;font-size:28px">f(x) = 2(x + 2)/5,  0 &lt; x &lt; 1</div>\n'
body += text('lx', 860, 610, 'x', 'sub', 'font-size:22px')
body += text('ar', A.X(0.4) - 110, A.Y(0.55), 'P(0.2 &lt; X &lt; 0.6)', 'rt', 'width:220px;text-align:center;color:#fff;font-size:22px')
body += text('r1', 1000, 90, 'Probability = area under the curve', 'step')
body += text('r2', 1000, 140, 'P(0.2 &lt; X &lt; 0.6) is the blue area between 0.2 and 0.6. Here it equals 0.384.', 'note', 'width:580px')
body += text('r3', 1000, 290, 'Rule 1:  f(x) ≥ 0', 'eq')
body += text('r4', 1000, 345, 'The curve never goes below the x-axis.', 'sub')
body += text('r5', 1000, 410, 'Rule 2:  total area = 1', 'eq')
body += text('r6', 1000, 465, 'The whole shaded region below the line has area 1 (100%).', 'sub', 'white-space:normal;width:580px')
body += text('r7', 1000, 545, 'P(X = 0.85) = 0', 'eq', f'color:{RED}')
body += text('r8', 1000, 600, 'A single line has no width, so it has no area.', 'sub')
js = draw('pdf', 0.4, 1.4) + show('lx', 0.6)
js += reveal('c1', A.X(0.6) - A.X(0.2), 2.0, 1.4) + show('ar', 3.2) + show(['r1', 'r2'], 2.4, dy=8)
js += show(['r3', 'r4'], 4.8, dy=8)
js += f'      tl.to("#tot", {{ opacity: 1, duration: 0.8 }}, 6.4);\n' + show(['r5', 'r6'], 6.4, dy=8)
js += f'      tl.to("#pt", {{ opacity: 1, duration: 0.3, repeat: 3, yoyo: true }}, 8.4);\n      tl.to("#pt", {{ opacity: 1, duration: 0.2 }}, 9.6);\n' + show(['r7', 'r8'], 8.4, dy=8)
write('fig1_pdf_area', 12, body, js)

# ---------------------------------------------------------------- Fig 2: standard normal and the empirical rule
A = Axes(120, 120, 1080, 470, -3.6, 3.6, 0, 0.44)
inner = A.axis([-3, -2, -1, 0, 1, 2, 3], lambda t: f'{t:d}')
cols = [('b3', 3, '#f6e7c9'), ('b2', 2, '#c9d6e3'), ('b1', 1, '#7fa7cc')]
defs = ''
for bid, k, col in cols:
    inner += f'<path id="{bid}" d="{A.area(phi, -k, k)}" fill="{col}" opacity="0"/>'
inner += f'<path id="nc" d="{A.curve(phi, -3.6, 3.6)}" fill="none" stroke="{NAVY}" stroke-width="5" stroke-dasharray="3000" stroke-dashoffset="3000"/>'
inner += f'<line id="mu" x1="{A.X(0)}" y1="{A.Y(0.42)}" x2="{A.X(0)}" y2="{A.Y(0)}" stroke="{TEXT}" stroke-width="2.5" stroke-dasharray="8 6" opacity="0"/>'
for bid, k, y, lab in (('l1', 1, 0.20, '68%'), ('l2', 2, 0.11, '95%'), ('l3', 3, 0.04, '99.7%')):
    x1, x2 = A.X(-k), A.X(k)
    inner += f'<g id="{bid}" opacity="0"><line x1="{x1}" y1="{A.Y(y)}" x2="{x2}" y2="{A.Y(y)}" stroke="{NAVY}" stroke-width="3"/>'
    inner += f'<line x1="{x1}" y1="{A.Y(y) - 10}" x2="{x1}" y2="{A.Y(y) + 10}" stroke="{NAVY}" stroke-width="3"/><line x1="{x2}" y1="{A.Y(y) - 10}" x2="{x2}" y2="{A.Y(y) + 10}" stroke="{NAVY}" stroke-width="3"/>'
    inner += f'<rect x="{A.X(0) - 52}" y="{A.Y(y) - 17}" width="104" height="34" rx="8" fill="#fff"/><text x="{A.X(0)}" y="{A.Y(y) + 8}" font-family="Montserrat" font-weight="700" font-size="24" fill="{NAVY}" text-anchor="middle">{lab}</text></g>'
body = card(40, 40, 1200, 660) + svg(inner)
body += '        <div class="lbl abs" style="left:80px;top:66px;color:#003e67;font-size:28px">Standard normal distribution:  μ = 0,  σ = 1</div>\n'
body += text('mut', A.X(0) + 12, 140, 'μ = 0', 'rt', 'font-size:22px')
body += text('zl', 640, 650, 'z (number of standard deviations from the mean)', 'sub', 'font-size:19px')
body += text('e1', 1280, 160, '±1σ → about 68%', 'eq', 'font-size:28px;color:#1f5f99')
body += text('e2', 1280, 230, '±2σ → about 95%', 'eq', 'font-size:28px;color:#5f86ad')
body += text('e3', 1280, 300, '±3σ → about 99.7%', 'eq', 'font-size:28px;color:#8a6d1f')
body += text('e4', 1280, 400, 'Most values are close to the mean; values beyond ±3σ are very rare.', 'note', 'width:320px')
js = draw('nc', 0.3, 1.6) + show(['mu', 'mut', 'zl'], 1.6)
js += f'      tl.to("#b1", {{ opacity: 0.9, duration: 0.6 }}, 2.8);\n' + show(['l1', 'e1'], 3.1)
js += f'      tl.to("#b2", {{ opacity: 0.9, duration: 0.6 }}, 4.6);\n' + show(['l2', 'e2'], 4.9)
js += f'      tl.to("#b3", {{ opacity: 0.9, duration: 0.6 }}, 6.4);\n' + show(['l3', 'e3'], 6.7)
js += show('e4', 8.4, dy=8)
write('fig2_empirical_rule', 12, body, js)

# ---------------------------------------------------------------- Fig 3: the z-score as distance in standard deviations
mu, sd = 100, 10
g = lambda x: phi((x - mu) / sd)
A = Axes(120, 150, 1000, 400, 62, 138, 0, 0.44)
inner = A.axis([70, 80, 90, 100, 110, 120, 130], lambda t: f'{t:d}')
inner += f'<path id="nc" d="{A.curve(g, 62, 138)}" fill="none" stroke="{NAVY}" stroke-width="5" stroke-dasharray="3000" stroke-dashoffset="3000"/>'
inner += f'<line id="mu" x1="{A.X(100)}" y1="{A.Y(0.42)}" x2="{A.X(100)}" y2="{A.Y(0)}" stroke="{TEXT}" stroke-width="2.5" stroke-dasharray="8 6" opacity="0"/>'
inner += f'<line id="xl" x1="{A.X(115)}" y1="{A.Y(g(115))}" x2="{A.X(115)}" y2="{A.Y(0)}" stroke="{GOLD}" stroke-width="5" opacity="0"/>'
yb = A.Y(0) + 70
for i, (a, b, lab) in enumerate(((100, 110, '1σ = 10'), (110, 115, '0.5σ = 5'))):
    inner += f'<g id="s{i}" opacity="0"><line x1="{A.X(a)}" y1="{yb}" x2="{A.X(b)}" y2="{yb}" stroke="{BLUE if i == 0 else GOLD}" stroke-width="8" stroke-linecap="round"/>'
    inner += f'<text x="{(A.X(a) + A.X(b)) / 2}" y="{yb + 34}" font-family="Open Sans" font-weight="600" font-size="20" fill="{TEXT}" text-anchor="middle">{lab}</text></g>'
body = card(40, 40, 1140, 660) + svg(inner)
body += '        <div class="lbl abs" style="left:80px;top:66px;color:#003e67;font-size:28px">μ = 100,  σ = 10,  x = 115</div>\n'
body += text('mut', A.X(100) + 12, 160, 'μ = 100', 'rt', 'font-size:22px')
body += text('xt', A.X(115) + 12, 300, 'x = 115', 'rt', f'font-size:22px;color:{GOLD}')
body += text('z1', 1220, 150, 'How many σ is x away from μ?', 'step')
body += text('z2', 1220, 220, 'z = (x − μ) / σ', 'eq')
body += text('z3', 1220, 285, 'z = (115 − 100) / 10', 'eq', 'font-size:26px')
body += text('z4', 1220, 345, 'z = 1.5', 'eq', f'font-size:40px;color:{GOLD}')
body += text('z5', 1220, 430, '115 is 1.5 standard deviations above the mean. A negative z would mean below the mean.', 'note', 'width:360px')
js = draw('nc', 0.3, 1.4) + show(['mu', 'mut'], 1.4) + show(['xl', 'xt'], 2.2) + show('z1', 2.6)
js += show('s0', 3.4) + show('s1', 4.4) + show('z2', 5.2, dy=8) + show('z3', 6.0, dy=8) + show('z4', 6.8, dy=8) + show('z5', 8.0)
write('fig3_z_score', 12, body, js)

# ---------------------------------------------------------------- Fig 4: reading the Z-table
rows = [1.3, 1.4, 1.5, 1.6, 1.7]
cols = [0, 1, 2, 3, 4]
x0, y0, cw, ch, lw = 90, 170, 128, 62, 110
body = card(40, 40, 840, 660)
body += '        <div class="lbl abs" style="left:80px;top:66px;color:#003e67;font-size:28px">Z-table: P(Z &lt; z)</div>\n'
body += '        <div class="sub abs" style="left:80px;top:110px">part of the table</div>\n'
body += f'        <div class="abs" style="left:{x0}px;top:{y0}px;width:{lw}px;height:{ch}px;background:{NAVY};color:#fff;font:700 24px Montserrat;text-align:center;line-height:{ch}px">z</div>\n'
for j, c in enumerate(cols):
    body += f'        <div id="ch{j}" class="abs" style="left:{x0 + lw + j * cw}px;top:{y0}px;width:{cw}px;height:{ch}px;background:{NAVY};color:#fff;font:700 24px Montserrat;text-align:center;line-height:{ch}px">.0{c}</div>\n'
for i, r in enumerate(rows):
    y = y0 + (i + 1) * ch
    body += f'        <div id="rh{i}" class="abs" style="left:{x0}px;top:{y}px;width:{lw}px;height:{ch}px;background:{PALE};border:1px solid {LIGHT};font:700 24px Montserrat;color:{NAVY};text-align:center;line-height:{ch}px">{r:.1f}</div>\n'
    for j, c in enumerate(cols):
        v = Phi(r + c / 100)
        body += f'        <div id="c{i}{j}" class="abs" style="left:{x0 + lw + j * cw}px;top:{y}px;width:{cw}px;height:{ch}px;background:#fff;border:1px solid {LIGHT};font:600 23px \'Open Sans\';color:{TEXT};text-align:center;line-height:{ch - 2}px">{v:.4f}</div>\n'
body += f'        <div id="rowhl" class="abs" style="left:{x0 - 4}px;top:{y0 + 3 * ch - 4}px;width:{lw + 5 * cw + 8}px;height:{ch + 8}px;border:4px solid {BLUE};border-radius:8px;opacity:0"></div>\n'
body += f'        <div id="colhl" class="abs" style="left:{x0 + lw - 4}px;top:{y0 - 4}px;width:{cw + 8}px;height:{6 * ch + 8}px;border:4px solid {GOLD};border-radius:8px;opacity:0"></div>\n'
body += text('st1', 90, 570, '1. Row 1.5 (first decimal)', 'rt', f'color:{BLUE}')
body += text('st2', 90, 610, '2. Column .00 (second decimal)', 'rt', f'color:{GOLD}')
body += text('st3', 90, 650, '3. Read the value: 0.9332', 'rt', f'color:{NAVY}')
A = Axes(960, 200, 600, 300, -3.4, 3.4, 0, 0.44)
inner = A.axis([-3, -2, -1, 0, 1, 2, 3], lambda t: f'{t:d}')
inner += f'<path d="{A.area(phi, -3.4, 1.5)}" fill="{BLUE}" opacity="0.55" clip-path="url(#c4)"/>'
inner += f'<path id="nc" d="{A.curve(phi, -3.4, 3.4)}" fill="none" stroke="{NAVY}" stroke-width="4" stroke-dasharray="3000" stroke-dashoffset="3000"/>'
inner += f'<line id="zl" x1="{A.X(1.5)}" y1="{A.Y(0.36)}" x2="{A.X(1.5)}" y2="{A.Y(0)}" stroke="{GOLD}" stroke-width="4" opacity="0"/>'
body += card(920, 40, 680, 660) + svg(inner, clip('c4', A.X(-3.4), A.Y(0.44), A.h + 5))
body += '        <div class="lbl abs" style="left:960px;top:66px;color:#003e67;font-size:26px">The table gives the area to the LEFT</div>\n'
body += text('zt', A.X(1.5) - 40, 150, 'z = 1.5', 'rt', f'color:{GOLD};font-size:22px')
body += text('pa', 960, 580, 'P(Z &lt; 1.5) = 0.9332', 'eq')
body += text('pb', 960, 635, 'P(Z &gt; 1.5) = 1 − 0.9332 = 0.0668', 'rt', f'color:{MUTED}')
js = show('st1', 0.6) + f'      tl.to("#rowhl", {{ opacity: 1, duration: 0.4 }}, 0.8);\n'
js += f'      tl.to(["#rh2"], {{ backgroundColor: "{BLUE}", color: "#fff", duration: 0.4 }}, 0.8);\n'
js += show('st2', 2.2) + f'      tl.to("#colhl", {{ opacity: 1, duration: 0.4 }}, 2.4);\n'
js += f'      tl.to(["#ch0"], {{ backgroundColor: "{GOLD}", duration: 0.4 }}, 2.4);\n'
js += show('st3', 3.8) + f'      tl.to("#c20", {{ backgroundColor: "{YELLOW if False else "#f5c400"}", scale: 1.15, duration: 0.4 }}, 4.0);\n'
js += draw('nc', 4.6, 1.0) + show(['zl', 'zt'], 5.4) + reveal('c4', A.X(1.5) - A.X(-3.4), 5.8, 1.4) + show('pa', 7.0, dy=8) + show('pb', 8.4, dy=8)
write('fig4_z_table', 12, body, js)

# ---------------------------------------------------------------- Fig 5: unusual values (IQ)
mu, sd = 100, 15
g = lambda x: phi((x - mu) / sd)
A = Axes(120, 150, 1000, 420, 45, 155, 0, 0.44)
inner = A.axis([55, 70, 85, 100, 115, 130, 145], lambda t: f'{t:d}')
inner += f'<path id="mid" d="{A.area(g, 70, 130)}" fill="{PALE}" opacity="0"/>'
inner += f'<path id="tl" d="{A.area(g, 45, 70)}" fill="{ORANGE}" opacity="0"/>'
inner += f'<path id="tr" d="{A.area(g, 130, 155)}" fill="{ORANGE}" opacity="0"/>'
inner += f'<path id="nc" d="{A.curve(g, 45, 155)}" fill="none" stroke="{NAVY}" stroke-width="5" stroke-dasharray="3000" stroke-dashoffset="3000"/>'
inner += f'<line id="mu" x1="{A.X(100)}" y1="{A.Y(0.42)}" x2="{A.X(100)}" y2="{A.Y(0)}" stroke="{TEXT}" stroke-width="2.5" stroke-dasharray="8 6" opacity="0"/>'
for bid, v in (('bl', 70), ('br', 130)):
    inner += f'<line id="{bid}" x1="{A.X(v)}" y1="{A.Y(0.42)}" x2="{A.X(v)}" y2="{A.Y(0)}" stroke="{RED}" stroke-width="3" stroke-dasharray="10 6" opacity="0"/>'
body = card(40, 40, 1140, 660) + svg(inner)
body += '        <div class="lbl abs" style="left:80px;top:66px;color:#003e67;font-size:28px">IQ scores:  μ = 100,  σ = 15</div>\n'
body += text('mut', A.X(100) + 12, 160, 'μ = 100', 'rt', 'font-size:22px')
body += text('blt', A.X(70) - 150, 180, 'μ − 2σ = 70', 'rt', f'font-size:21px;color:{RED}')
body += text('brt', A.X(130) + 12, 180, 'μ + 2σ = 130', 'rt', f'font-size:21px;color:{RED}')
body += text('nm', A.X(100) - 130, 430, 'normal: about 95%', 'rt', f'font-size:22px;width:260px;text-align:center;color:{NAVY};white-space:nowrap;background:{PALE}')
body += text('ul', A.X(55) - 70, 470, 'unusual', 'rt', f'font-size:20px;color:#a86a12')
body += text('ur', A.X(140) - 30, 470, 'unusual', 'rt', f'font-size:20px;color:#a86a12')
body += text('u1', 1220, 150, 'Unusual = more than 2σ from the mean', 'step', 'white-space:normal;width:360px')
body += text('u2', 1220, 250, 'Upper border: 100 + 2·15 = 130', 'rt')
body += text('u3', 1220, 300, 'Lower border: 100 − 2·15 = 70', 'rt')
body += text('u4', 1220, 380, 'IQ below 70 or above 130 is unusual: only about 5% of people.', 'note', 'width:360px')
js = draw('nc', 0.3, 1.4) + show(['mu', 'mut'], 1.4) + show('u1', 1.8)
js += show(['br', 'brt', 'u2'], 2.8) + show(['bl', 'blt', 'u3'], 3.8)
js += f'      tl.to("#mid", {{ opacity: 1, duration: 0.6 }}, 5.0);\n' + show('nm', 5.2)
js += f'      tl.to(["#tl", "#tr"], {{ opacity: 0.85, duration: 0.6 }}, 6.4);\n' + show(['ul', 'ur'], 6.6) + show('u4', 7.6, dy=8)
write('fig5_unusual_values', 12, body, js)
print('ok')
