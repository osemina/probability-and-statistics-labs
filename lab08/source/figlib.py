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


