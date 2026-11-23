from figlib import *

# ---------------------------------------------------------------- Fig 1: which two-sample test?
def node(id_, x, y, w, h, html, bg, fg, size=23):
    return (f'        <div id="{id_}" class="abs" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;opacity:0;border-radius:18px;'
            f'background:{bg};color:{fg};display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;'
            f'font:700 {size}px Montserrat;line-height:1.25;padding:0 14px">{html}</div>\n')


def edge(id_, x1, y1, x2, y2, label='', lx=0, ly=0):
    m = (y1 + y2) / 2
    s = f'<g id="{id_}" opacity="0"><path d="M{x1},{y1} L{x1},{m} L{x2},{m} L{x2},{y2}" fill="none" stroke="{MUTED}" stroke-width="3"/>'
    s += f'<path d="M{x2 - 9},{y2 - 14} L{x2},{y2} L{x2 + 9},{y2 - 14}" fill="none" stroke="{MUTED}" stroke-width="3"/>'
    if label:
        s += f'<text x="{lx}" y="{ly}" font-family="Open Sans" font-weight="600" font-size="21" fill="{TEXT}" text-anchor="middle">{label}</text>'
    return s + '</g>'


def sub(t):
    return f'<span style="font:600 18px Open Sans;margin-top:4px">{t}</span>'


PALEN, GOLDP, BROWN = '#eef2f6', '#f1e4c6', '#5a4513'
body = card(20, 15, 1600, 710)
body += node('q0', 620, 30, 400, 70, 'What do we compare?', NAVY, '#fff')
body += node('pr', 60, 175, 400, 95, 'z-test for two proportions' + sub('pooled proportion p₀'), GOLDP, BROWN)
body += node('q1', 620, 175, 400, 95, 'Two means:<br>are the samples paired?', NAVY, '#fff')
body += node('va', 1180, 175, 400, 95, 'F-test for two variances' + sub('F = s²<sub>X</sub> / s²<sub>Y</sub>'), GOLDP, BROWN)
body += node('pt', 420, 330, 330, 90, 'Paired t-test' + sub('d = x − y, df = n − 1'), GOLDP, BROWN)
body += node('q2', 900, 330, 330, 90, 'Is σ known?', NAVY, '#fff')
body += node('zm', 690, 470, 350, 90, 'z-test' + sub('σ<sub>X</sub> and σ<sub>Y</sub> known'), GOLDP, BROWN)
body += node('q3', 1110, 470, 360, 90, 'Equal variances?', NAVY, '#fff')
body += node('pl', 940, 610, 320, 95, 'Pooled t-test' + sub('df = n<sub>X</sub> + n<sub>Y</sub> − 2'), GOLDP, BROWN)
body += node('we', 1290, 610, 310, 95, 'Welch’s t-test' + sub('df = ν (Welch formula)'), GOLDP, BROWN)
inner = edge('e1', 820, 100, 260, 175, 'proportions', 470, 128)
inner += edge('e2', 820, 100, 820, 175, 'means', 868, 165)
inner += edge('e3', 820, 100, 1380, 175, 'variances', 1170, 128)
inner += edge('e4', 820, 270, 585, 330, 'yes (dependent)', 640, 291)
inner += edge('e5', 820, 270, 1065, 330, 'no (independent)', 1010, 291)
inner += edge('e6', 1065, 420, 865, 470, 'yes', 930, 437)
inner += edge('e7', 1065, 420, 1290, 470, 'no', 1220, 437)
inner += edge('e8', 1290, 560, 1100, 610, 'yes', 1160, 577)
inner += edge('e9', 1290, 560, 1445, 610, 'no', 1400, 577)
body = body + svg(inner).replace('<svg ', '<svg style="z-index:0" ', 1)
js = show('q0', 0.3, dy=8)
js += show('e1', 1.0, 0.4) + show('pr', 1.3, dy=8)
js += show('e3', 2.1, 0.4) + show('va', 2.4, dy=8)
js += show('e2', 3.2, 0.4) + show('q1', 3.5, dy=8)
js += show('e4', 4.4, 0.4) + show('pt', 4.7, dy=8)
js += show('e5', 5.5, 0.4) + show('q2', 5.8, dy=8)
js += show('e6', 6.6, 0.4) + show('zm', 6.9, dy=8)
js += show('e7', 7.7, 0.4) + show('q3', 8.0, dy=8)
js += show('e8', 8.8, 0.4) + show('pl', 9.1, dy=8) + show('e9', 9.6, 0.4) + show('we', 9.9, dy=8)
write('fig1_which_test', 13, body, js)
