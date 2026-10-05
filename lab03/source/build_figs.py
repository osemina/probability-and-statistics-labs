from common import write

NAVY, BLUE, LIGHT, PALE, GOLD, GOLDPALE, PANEL, RED, TEXT, MUTED = (
    '#003e67', '#1f5f99', '#c9d6e3', '#eef2f6', '#c39a3d', '#f1e4c6', '#f3f3f0', '#b34739', '#202020', '#5f6368')

# ---------------------------------------------------------------- Fig 1: probability scale
pts = [(0.0, '0', 'Impossible', 'Rolling a 7 with one die', 'up'),
       (0.5, '0.5', 'Even chance', 'Heads on a fair coin', 'down'),
       (0.7, '0.7', 'Likely', 'Weather app: 70% chance of rain', 'up'),
       (1.0, '1', 'Certain', 'Rolling a number from 1 to 6', 'down')]
X0, X1, Y = 170, 1470, 370
body = f'''
        <div class="abs" style="left:{X0}px;top:{Y-9}px;width:{X1-X0}px;height:18px;border-radius:9px;background:linear-gradient(90deg,{LIGHT},{NAVY})"></div>
        <div class="lbl abs" style="left:{X0}px;top:600px;color:{MUTED};font-size:20px">less likely</div>
        <div class="lbl abs" style="left:{X1-140}px;top:600px;color:{NAVY};font-size:20px">more likely</div>
        <div class="abs" style="left:{X0+150}px;top:612px;width:{X1-X0-320}px;height:3px;background:{LIGHT}"></div>
        <div class="abs" style="left:{X1-180}px;top:604px;width:0;height:0;border-left:16px solid {LIGHT};border-top:10px solid transparent;border-bottom:10px solid transparent"></div>
        <div id="mk" class="abs" style="left:{X0-22}px;top:{Y-22}px;width:44px;height:44px;border-radius:50%;background:{GOLD};border:5px solid #fff;box-shadow:0 2px 8px rgba(0,0,0,.25)"></div>
'''
js = ''
for i, (p, v, lab, ex, side) in enumerate(pts):
    x = X0 + p * (X1 - X0)
    w = 330
    left = min(max(x - w / 2, 20), 1620 - w)
    top = Y - 230 if side == 'up' else Y + 50
    body += f'''        <div class="abs" style="left:{x-2}px;top:{Y-26}px;width:4px;height:52px;background:{TEXT}"></div>
        <div class="lbl abs" style="left:{x-60}px;top:{Y+(-70 if side=='down' else 34)}px;width:120px;text-align:center;color:{NAVY}">{v}</div>
        <div id="c{i}" class="abs card" style="left:{left}px;top:{top}px;width:{w}px;height:150px;opacity:0;padding:22px 24px;border-left:6px solid {GOLD}">
          <div class="lbl" style="color:{GOLD};font-size:24px">{lab}</div>
          <div class="rt" style="margin-top:12px;font-size:23px;line-height:1.35;white-space:normal">{ex}</div>
        </div>
'''
    t = 0.6 + i * 2.2
    js += f'      tl.to("#mk", {{ x: {x-X0}, duration: {0.3 if i == 0 else 1.0}, ease: "power2.inOut" }}, {t});\n'
    js += f'      tl.fromTo("#c{i}", {{ opacity: 0, y: {12 if side=="up" else -12} }}, {{ opacity: 1, y: 0, duration: 0.5 }}, {t + (0.3 if i == 0 else 1.0)});\n'
write('fig1_probability_scale', 10, body, js)

# ---------------------------------------------------------------- Fig 2: die events
pips = {1: [(1, 1)], 2: [(0, 0), (2, 2)], 3: [(0, 0), (1, 1), (2, 2)], 4: [(0, 0), (2, 0), (0, 2), (2, 2)],
        5: [(0, 0), (2, 0), (1, 1), (0, 2), (2, 2)], 6: [(0, 0), (2, 0), (0, 1), (2, 1), (0, 2), (2, 2)]}
body = f'''        <div class="abs card" style="left:40px;top:50px;width:960px;height:640px"></div>
        <div class="lbl abs" style="left:85px;top:90px;color:{NAVY};font-size:30px">Roll one die</div>
        <div class="sub abs" style="left:85px;top:138px;font-size:24px">Sample space S = {{1, 2, 3, 4, 5, 6}}</div>
'''
FX, FY, FS, FG = 92, 270, 120, 30
for n in range(1, 7):
    x = FX + (n - 1) * (FS + FG)
    dots = ''.join(f'<div class="abs" style="left:{20+c*30}px;top:{20+r*30}px;width:20px;height:20px;border-radius:50%;background:{TEXT}"></div>' for c, r in pips[n])
    body += f'''        <div id="f{n}" class="abs" style="left:{x}px;top:{FY}px;width:{FS}px;height:{FS}px;border-radius:24px;background:#fff;border:4px solid {LIGHT};opacity:0">{dots}</div>
        <div id="ba{n}" class="abs" style="left:{x}px;top:{FY+145}px;width:{FS}px;height:14px;border-radius:7px;background:{BLUE};opacity:0"></div>
        <div id="bb{n}" class="abs" style="left:{x}px;top:{FY+170}px;width:{FS}px;height:14px;border-radius:7px;background:{GOLD};opacity:0"></div>
'''
body += f'''        <div class="sub abs" id="la" style="left:{FX}px;top:{FY+205}px;color:{BLUE};opacity:0">blue bar: in A</div>
        <div class="sub abs" id="lb" style="left:{FX+250}px;top:{FY+205}px;color:#8a6d1f;opacity:0">gold bar: in B</div>
        <div id="jt" class="lbl abs" style="left:{FX+3*(FS+FG)-10}px;top:{FY-60}px;width:{3*FS+2*FG+20}px;text-align:center;color:{NAVY};font-size:22px;opacity:0">A &#8745; B</div>
        <div id="s1" class="abs" style="left:1060px;top:110px;opacity:0"><div class="lbl" style="color:{BLUE}">A = even = {{2, 4, 6}}</div></div>
        <div id="s2" class="abs" style="left:1060px;top:200px;opacity:0"><div class="lbl" style="color:#8a6d1f">B = greater than 3 = {{4, 5, 6}}</div></div>
        <div id="s3" class="abs" style="left:1060px;top:290px;opacity:0"><div class="lbl" style="color:{NAVY}">A &#8745; B = {{4, 6}}</div><div class="sub" style="margin-top:8px">joint event: even AND greater than 3</div></div>
        <div id="s4" class="abs" style="left:1060px;top:420px;opacity:0"><div class="lbl" style="color:{NAVY}">A&#8242; = {{1, 3, 5}}</div><div class="sub" style="margin-top:8px">complement: every outcome NOT in A</div></div>
        <div id="s5" class="note abs" style="left:1060px;top:560px;width:540px;opacity:0">An event is just a set of outcomes, so we can combine events like sets.</div>
'''
js = ''.join(f'      tl.fromTo("#f{n}", {{ opacity: 0, scale: 0.6 }}, {{ opacity: 1, scale: 1, duration: 0.4, ease: "back.out(2)" }}, {0.2 + n*0.12});\n' for n in range(1, 7))
js += '      tl.to("#s1", { opacity: 1, duration: 0.4 }, 1.8);\n      tl.to("#la", { opacity: 1, duration: 0.4 }, 1.9);\n'
js += ''.join(f'      tl.to("#f{n}", {{ backgroundColor: "#dce5ee", borderColor: "{BLUE}", duration: 0.4 }}, {2.0 + k*0.15});\n      tl.to("#ba{n}", {{ opacity: 1, duration: 0.4 }}, {2.0 + k*0.15});\n' for k, n in enumerate([2, 4, 6]))
js += '      tl.to("#s2", { opacity: 1, duration: 0.4 }, 3.6);\n      tl.to("#lb", { opacity: 1, duration: 0.4 }, 3.7);\n'
js += ''.join(f'      tl.to("#bb{n}", {{ opacity: 1, duration: 0.4 }}, {3.8 + k*0.15});\n' for k, n in enumerate([4, 5, 6]))
js += f'      tl.to(["#f4", "#f6"], {{ scale: 1.12, borderColor: "{NAVY}", borderWidth: 6, duration: 0.35, yoyo: true, repeat: 1 }}, 5.6);\n'
js += '      tl.to("#jt", { opacity: 1, duration: 0.4 }, 5.6);\n      tl.to("#s3", { opacity: 1, duration: 0.4 }, 5.8);\n'
js += f'      tl.to(["#f2", "#f4", "#f6"], {{ opacity: 0.3, duration: 0.5 }}, 7.8);\n      tl.to(["#bb4", "#bb5", "#bb6", "#ba2", "#ba4", "#ba6", "#jt"], {{ opacity: 0.15, duration: 0.5 }}, 7.8);\n'
js += f'      tl.to(["#f1", "#f3", "#f5"], {{ backgroundColor: "{PALE}", borderColor: "{NAVY}", borderWidth: 6, duration: 0.5 }}, 8.0);\n'
js += '      tl.to("#s4", { opacity: 1, duration: 0.4 }, 8.1);\n      tl.to("#s5", { opacity: 1, duration: 0.5 }, 9.2);\n'
write('fig2_die_events', 12, body, js)

# ---------------------------------------------------------------- Fig 3: Venn operations
panels = [('A &#8746; B', '&#8220;A or B&#8221;', 'union'), ('A &#8745; B', '&#8220;A and B&#8221;', 'inter'),
          ('A&#8242;', '&#8220;not A&#8221;', 'comp'), ('A &#8745; B = &#8709;', '&#8220;mutually exclusive&#8221;', 'mutex')]
body = ''
js = ''
for i, (t, s, kind) in enumerate(panels):
    x0 = 30 + i * 400
    ca, cb, r = ((130, 150), (230, 150), 85) if kind != 'mutex' else ((100, 150), (260, 150), 70)
    shade = ''
    if kind == 'union':
        shade = f'<circle cx="{ca[0]}" cy="{ca[1]}" r="{r}" fill="{NAVY}" fill-opacity="0.75"/><circle cx="{cb[0]}" cy="{cb[1]}" r="{r}" fill="{NAVY}" fill-opacity="0.75"/>'
    elif kind == 'inter':
        shade = f'<clipPath id="cp{i}"><circle cx="{ca[0]}" cy="{ca[1]}" r="{r}"/></clipPath><circle cx="{cb[0]}" cy="{cb[1]}" r="{r}" fill="{NAVY}" fill-opacity="0.8" clip-path="url(#cp{i})"/>'
    elif kind == 'comp':
        shade = f'<mask id="mk{i}"><rect x="0" y="0" width="360" height="300" fill="#fff"/><circle cx="{ca[0]}" cy="{ca[1]}" r="{r}" fill="#000"/></mask><rect x="8" y="8" width="344" height="284" rx="14" fill="{NAVY}" fill-opacity="0.72" mask="url(#mk{i})"/>'
    else:
        shade = f'<circle cx="{ca[0]}" cy="{ca[1]}" r="{r}" fill="{NAVY}" fill-opacity="0.75"/><circle cx="{cb[0]}" cy="{cb[1]}" r="{r}" fill="{GOLD}" fill-opacity="0.85"/>'
    body += f'''        <div id="t{i}" class="abs" style="left:{x0}px;top:70px;width:360px;text-align:center;opacity:0"><div class="lbl" style="color:{NAVY};font-size:30px">{t}</div><div class="sub" style="margin-top:6px">{s}</div></div>
        <svg id="p{i}" class="abs" style="left:{x0}px;top:200px;opacity:0" width="360" height="300" viewBox="0 0 360 300">
          <rect x="8" y="8" width="344" height="284" rx="14" fill="#fff" stroke="{NAVY}" stroke-width="3"/>
          <g id="sh{i}" opacity="0">{shade}</g>
          <circle cx="{ca[0]}" cy="{ca[1]}" r="{r}" fill="none" stroke="{TEXT}" stroke-width="3"/>
          <circle cx="{cb[0]}" cy="{cb[1]}" r="{r}" fill="none" stroke="{TEXT}" stroke-width="3"/>
          <text x="26" y="40" font-family="Montserrat" font-weight="700" font-size="22" fill="{NAVY if kind!='comp' else '#fff'}">S</text>
          <text x="{ca[0]-r+4}" y="{ca[1]-r+12}" font-family="Montserrat" font-weight="700" font-size="24" fill="{TEXT}" stroke="#fff" stroke-width="5" paint-order="stroke">A</text>
          <text x="{cb[0]+r-22}" y="{cb[1]-r+12}" font-family="Montserrat" font-weight="700" font-size="24" fill="{TEXT}" stroke="#fff" stroke-width="5" paint-order="stroke">B</text>
        </svg>
'''
    js += f'      tl.to("#p{i}", {{ opacity: 1, duration: 0.4 }}, {0.2 + i*0.15});\n'
    js += f'      tl.to("#t{i}", {{ opacity: 1, duration: 0.4 }}, {1.4 + i*1.6});\n'
    js += f'      tl.fromTo("#sh{i}", {{ opacity: 0 }}, {{ opacity: 1, duration: 0.8 }}, {1.5 + i*1.6});\n'
body += f'        <div id="nt" class="note abs" style="left:30px;top:560px;width:1580px;text-align:center;opacity:0">The rectangle is the sample space S. The shaded part is the event named above each diagram.</div>\n'
js += '      tl.to("#nt", { opacity: 1, duration: 0.5 }, 8.2);\n'
write('fig3_venn_operations', 10, body, js)

# ---------------------------------------------------------------- Fig 4: red or king (addition rule)
ranks = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suits = [('&#9829;', True), ('&#9830;', True), ('&#9827;', False), ('&#9824;', False)]
GX, GY, CW, CH, GAP = 60, 170, 58, 80, 8
body = f'''        <div class="lbl abs" style="left:{GX}px;top:80px;color:{NAVY};font-size:28px">A standard deck: 52 cards</div>
'''
for r, (s, red) in enumerate(suits):
    for c, rk in enumerate(ranks):
        x, y = GX + c * (CW + GAP), GY + r * (CH + GAP)
        col = RED if red else TEXT
        body += f'        <div id="k{r}_{c}" class="abs" style="left:{x}px;top:{y}px;width:{CW}px;height:{CH}px;border-radius:9px;background:#fff;border:2px solid {LIGHT};opacity:0;text-align:center;font:700 19px Montserrat;color:{col};padding-top:12px;line-height:1.25">{rk}<br/>{s}</div>\n'
kx = GX + 12 * (CW + GAP)
body += f'''        <div id="kcol" class="abs" style="left:{kx-7}px;top:{GY-7}px;width:{CW+14}px;height:{4*(CH+GAP)+6}px;border-radius:14px;border:5px solid {GOLD};opacity:0"></div>
        <div id="twice" class="abs" style="left:{kx-230}px;top:{GY+4*(CH+GAP)+18}px;width:310px;text-align:right;opacity:0"><div class="lbl" style="color:{RED};font-size:22px">2 red Kings: counted twice!</div></div>
        <div id="r1" class="abs" style="left:1000px;top:150px;opacity:0"><span class="lbl" style="color:{RED}">Red cards: 26</span><span class="sub" style="margin-left:14px">(hearts and diamonds)</span></div>
        <div id="r2" class="abs" style="left:1000px;top:215px;opacity:0"><span class="lbl" style="color:#8a6d1f">Kings: 4</span></div>
        <div id="r3" class="note abs" style="left:1000px;top:285px;width:600px;opacity:0">Adding 26 + 4 counts the King of hearts and the King of diamonds two times, so we subtract them once.</div>
        <div id="r4" class="abs" style="left:1000px;top:430px;opacity:0"><div class="eq">P(Red &#8746; King)</div><div class="eq" style="margin-top:14px">= 26/52 + 4/52 &#8722; 2/52</div><div class="eq" style="margin-top:14px">= 28/52 = 7/13</div></div>
'''
js = ''.join(f'      tl.to("#k{r}_{c}", {{ opacity: 1, duration: 0.25 }}, {0.2 + c*0.04 + r*0.12});\n' for r in range(4) for c in range(13))
js += ''.join(f'      tl.to("#k{r}_{c}", {{ backgroundColor: "#f6dcd8", borderColor: "{RED}", duration: 0.3 }}, {2.0 + c*0.03 + r*0.1});\n' for r in range(2) for c in range(13))
js += '      tl.to("#r1", { opacity: 1, duration: 0.4 }, 2.2);\n'
js += '      tl.to("#kcol", { opacity: 1, duration: 0.4 }, 4.0);\n      tl.to("#r2", { opacity: 1, duration: 0.4 }, 4.2);\n'
js += f'      tl.to(["#k0_12", "#k1_12"], {{ scale: 1.2, duration: 0.3, yoyo: true, repeat: 3 }}, 5.8);\n'
js += '      tl.to("#twice", { opacity: 1, duration: 0.4 }, 5.9);\n      tl.to("#r3", { opacity: 1, duration: 0.5 }, 6.3);\n'
js += '      tl.fromTo("#r4", { opacity: 0, y: 14 }, { opacity: 1, y: 0, duration: 0.6 }, 8.4);\n'
write('fig4_red_or_king', 12, body, js)

# ---------------------------------------------------------------- Fig 5: playlist without repeats
order = ['P', 'R', 'P', 'P', 'R', 'P', 'R', 'P']
TW, TH, TX, TY, TS = 150, 104, 80, 170, 172
body = f'''        <div class="lbl abs" style="left:{TX}px;top:80px;color:{NAVY};font-size:28px">Shuffle queue: 8 songs, each played only once</div>
        <div class="abs" style="left:{TX}px;top:410px;width:{TW}px;height:{TH}px;border-radius:16px;border:3px dashed {LIGHT}"></div>
        <div class="abs" style="left:{TX+190}px;top:410px;width:{TW}px;height:{TH}px;border-radius:16px;border:3px dashed {LIGHT}"></div>
        <div class="step abs" style="left:{TX}px;top:528px;width:{TW}px;text-align:center">Song 1</div>
        <div class="step abs" style="left:{TX+190}px;top:528px;width:{TW}px;text-align:center">Song 2</div>
'''
for i, k in enumerate(order):
    pop = k == 'P'
    body += f'        <div id="t{i}" class="abs" style="left:{TX+i*TS}px;top:{TY}px;width:{TW}px;height:{TH}px;border-radius:16px;background:{GOLDPALE if pop else "#dce5ee"};border:3px solid {GOLD if pop else BLUE};opacity:0;text-align:center;padding-top:16px"><div style="font:700 34px Montserrat;color:{"#8a6d1f" if pop else BLUE}">&#9835;</div><div style="font:700 22px Montserrat;color:{"#8a6d1f" if pop else BLUE}">{"Pop" if pop else "Rock"}</div></div>\n'
body += f'''        <div id="m1" class="abs" style="left:560px;top:395px;width:1040px;opacity:0"><div class="rt">Song 1: <b style="color:#8a6d1f">5</b> of 8 songs are pop&#8195;&#8594;&#8195;5/8</div></div>
        <div id="m2" class="abs" style="left:560px;top:455px;width:1040px;opacity:0"><div class="rt">Song 2: only <b style="color:#8a6d1f">4</b> of the 7 songs left are pop&#8195;&#8594;&#8195;4/7</div></div>
        <div id="m3" class="abs" style="left:560px;top:530px;opacity:0"><div class="eq">P(Pop&#8321; &#8745; Pop&#8322;) = 5/8 &#215; 4/7 = 20/56 = 5/14 &#8776; 0.36</div></div>
        <div id="m4" class="note abs" style="left:560px;top:600px;width:1040px;opacity:0">No repeats: the first song changes what is left, so the two events are dependent.</div>
'''
js = ''.join(f'      tl.fromTo("#t{i}", {{ opacity: 0, y: -20 }}, {{ opacity: 1, y: 0, duration: 0.35 }}, {0.2 + i*0.1});\n' for i in range(8))
pops = [i for i, k in enumerate(order) if k == 'P']
js += f'      tl.to({[f"#t{i}" for i in pops]}, {{ scale: 1.08, duration: 0.25, yoyo: true, repeat: 1 }}, 1.8);\n'
js += '      tl.to("#m1", { opacity: 1, duration: 0.4 }, 1.9);\n'
js += f'      tl.to("#t0", {{ x: 0, y: {410-TY}, duration: 0.9, ease: "power2.inOut" }}, 2.8);\n'
rest = [i for i in range(8) if i != 0]
js += ''.join(f'      tl.to("#t{i}", {{ x: {(k-i)*TS}, duration: 0.6, ease: "power2.inOut" }}, 4.2);\n' for k, i in enumerate(rest))
pops2 = [i for i in rest if order[i] == 'P']
js += f'      tl.to({[f"#t{i}" for i in pops2]}, {{ scale: 1.08, duration: 0.25, yoyo: true, repeat: 1 }}, 5.1);\n'
js += '      tl.to("#m2", { opacity: 1, duration: 0.4 }, 5.2);\n'
js += f'      tl.to("#t2", {{ x: {190-2*TS}, y: {410-TY}, duration: 0.9, ease: "power2.inOut" }}, 6.2);\n'
rest2 = [i for i in rest if i != 2]
js += ''.join(f'      tl.to("#t{i}", {{ x: {(k-i)*TS}, duration: 0.6, ease: "power2.inOut" }}, 7.3);\n' for k, i in enumerate(rest2))
js += '      tl.fromTo("#m3", { opacity: 0, y: 12 }, { opacity: 1, y: 0, duration: 0.5 }, 8.3);\n      tl.to("#m4", { opacity: 1, duration: 0.5 }, 9.4);\n'
write('fig5_playlist_no_repeats', 12, body, js)

# ---------------------------------------------------------------- Fig 6: delivery tree + Bayes
N = {'O': (150, 330), 'Bk': (520, 175), 'Cr': (520, 485), 'BL': (880, 95), 'BO': (880, 255), 'CL': (880, 415), 'CO': (880, 575)}
E = [('O', 'Bk', '0.70'), ('O', 'Cr', '0.30'), ('Bk', 'BL', '0.05'), ('Bk', 'BO', '0.95'), ('Cr', 'CL', '0.15'), ('Cr', 'CO', '0.85')]
lines = ''
labels = ''
import math
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
body += node('O', 'Order', GOLD, '#fff') + node('Bk', 'Bike', NAVY, '#fff') + node('Cr', 'Car', NAVY, '#fff')
body += node('BL', 'Late', '#f5c400', NAVY) + node('BO', 'On time', '#dce5ee', NAVY) + node('CL', 'Late', '#f5c400', NAVY) + node('CO', 'On time', '#dce5ee', NAVY)
prods = [('BL', '0.70 &#215; 0.05 = 0.035'), ('BO', '0.70 &#215; 0.95 = 0.665'), ('CL', '0.30 &#215; 0.15 = 0.045'), ('CO', '0.30 &#215; 0.85 = 0.255')]
for i, (k, t) in enumerate(prods):
    x, y = N[k]
    body += f'        <div id="pr{i}" class="abs" style="left:{x+105}px;top:{y-18}px;font:600 25px \'Open Sans\';color:{NAVY if k[1]=="L" else MUTED};white-space:nowrap;opacity:0">{t}</div>\n'
body += f'''        <div id="sum" class="abs" style="left:985px;top:660px;opacity:0"><span class="eq" style="font-size:28px">P(Late) = 0.035 + 0.045 = 0.08</span></div>
        <div id="bay" class="abs card" style="left:1290px;top:95px;width:330px;height:470px;padding:26px;border-left:6px solid {NAVY};opacity:0">
          <div class="lbl" style="color:{NAVY};font-size:24px">Bayes: flip it</div>
          <div class="sub" style="margin-top:10px;white-space:normal">The order was late. Did it come by bike?</div>
          <div style="margin-top:22px;font:600 25px 'Open Sans';color:{NAVY}">P(Bike | Late)</div>
          <div style="margin-top:10px;font:600 25px 'Open Sans';color:{NAVY}">= 0.035 / 0.08</div>
          <div style="margin-top:10px;font:700 30px Montserrat;color:{NAVY}">&#8776; 0.44</div>
          <div class="note" style="margin-top:18px;font-size:20px">Bikes carry 70% of all orders but only about 44% of the late ones.</div>
        </div>
'''
js = '      tl.to("#nO", { opacity: 1, duration: 0.4 }, 0.2);\n'
for i in range(2):
    js += f'      tl.to("#e{i}", {{ attr: {{ "stroke-dashoffset": 0 }}, duration: 0.7 }}, 0.6);\n      tl.to("#pl{i}", {{ opacity: 1, duration: 0.3 }}, 1.1);\n'
js += '      tl.to(["#nBk", "#nCr"], { opacity: 1, duration: 0.4 }, 1.2);\n'
for i in range(2, 6):
    js += f'      tl.to("#e{i}", {{ attr: {{ "stroke-dashoffset": 0 }}, duration: 0.7 }}, 2.0);\n      tl.to("#pl{i}", {{ opacity: 1, duration: 0.3 }}, 2.5);\n'
js += '      tl.to(["#nBL", "#nBO", "#nCL", "#nCO"], { opacity: 1, duration: 0.4 }, 2.6);\n'
js += ''.join(f'      tl.fromTo("#pr{i}", {{ opacity: 0, x: -12 }}, {{ opacity: 1, x: 0, duration: 0.4 }}, {3.6 + i*0.5});\n' for i in range(4))
js += '      tl.to(["#nBO", "#nCO", "#pr1", "#pr3", "#e3", "#e5", "#pl3", "#pl5"], { opacity: 0.3, duration: 0.5 }, 6.0);\n'
js += '      tl.to(["#nBL", "#nCL"], { scale: 1.12, duration: 0.3, yoyo: true, repeat: 1 }, 6.1);\n'
js += '      tl.fromTo("#sum", { opacity: 0, y: 10 }, { opacity: 1, y: 0, duration: 0.5 }, 6.7);\n'
js += f'      tl.to(["#e1", "#e4", "#nCr", "#nCL", "#pr2", "#pl1", "#pl4"], {{ opacity: 0.35, duration: 0.5 }}, 8.6);\n'
js += f'      tl.to(["#e0", "#e2"], {{ attr: {{ stroke: "{NAVY}", "stroke-width": 8 }}, duration: 0.5 }}, 8.6);\n'
js += '      tl.fromTo("#bay", { opacity: 0, x: 20 }, { opacity: 1, x: 0, duration: 0.6 }, 9.0);\n'
write('fig6_delivery_tree_bayes', 14, body, js)

# ---------------------------------------------------------------- Fig 7: given Spotify
dots = ''
GX7, GY7, ST = 105, 125, 54
for r in range(10):
    for c in range(10):
        cls = ['dot']
        if r <= 6: cls.append('spot')
        if 5 <= r <= 6: cls.append('both')
        if 7 <= r <= 8: cls.append('nonly')
        if r >= 7: cls.append('out')
        dots += f'<div class="abs {" ".join(cls)}" style="left:{GX7+c*ST}px;top:{GY7+r*ST}px"></div>'
body = f'''        <div class="abs card" style="left:50px;top:70px;width:640px;height:640px"></div>
        <div class="abs">{dots}</div>
        <div id="frame" class="abs" style="left:{GX7-14}px;top:{GY7-14}px;width:{9*ST+38+28}px;height:{6*ST+38+28}px;border-radius:18px;border:5px solid {GOLD};opacity:0"></div>
        <div class="lbl abs" style="left:780px;top:70px;color:{GOLD};font-size:22px;letter-spacing:2px">CONDITIONAL PROBABILITY</div>
        <div class="lbl abs" style="left:780px;top:106px;color:{NAVY};font-size:34px">&#8220;Given&#8221; shrinks the sample space</div>
'''
steps = [
    ('100 students are surveyed', 'Each dot is one student. Pick one at random.', ''),
    ('Spotify users: 70', f'<span style="color:{NAVY}">&#9679;</span> uses Spotify (S)', 'P(S) = 70/100 = 0.70'),
    ('Netflix users: 40', f'<span style="color:{GOLD}">&#9679;</span> Spotify and Netflix: 20&#8195;<span style="color:#e8cf8f">&#9679;</span> Netflix only: 20', 'P(N) = 40/100 = 0.40'),
    ('We are told: the student uses Spotify', 'Everyone outside S is now impossible. The new sample space has only 70 students.', ''),
    ('Netflix, given Spotify', 'Of the 70 Spotify users, 20 also use Netflix.', 'P(N | S) = 20/70 &#8776; 0.29'),
]
for i, (h, t, e) in enumerate(steps):
    body += f'''        <div id="s{i}" class="abs" style="left:780px;top:220px;width:820px;opacity:0">
          <div class="lbl" style="color:{NAVY};font-size:30px">{h}</div>
          <div class="rt" style="margin-top:22px;font-size:26px;line-height:1.45;color:{TEXT}">{t}</div>
          <div class="eq" style="margin-top:30px;font-size:38px">{e}</div>
        </div>
'''
css = f'.dot {{ width: 36px; height: 36px; border-radius: 50%; background: {LIGHT}; }}'
js = '      tl.from(".dot", { scale: 0, duration: 0.4, stagger: 0.006, ease: "back.out(2)" }, 0.2);\n'
T = [0.4, 2.8, 5.4, 8.2, 11.0]
for i, t in enumerate(T):
    js += f'      tl.to("#s{i}", {{ opacity: 1, duration: 0.4 }}, {t});\n'
    if i < 4: js += f'      tl.to("#s{i}", {{ opacity: 0, duration: 0.3 }}, {T[i+1]-0.35});\n'
js += f'      tl.to(".spot", {{ backgroundColor: "{NAVY}", duration: 0.4, stagger: 0.004 }}, 3.0);\n'
js += f'      tl.to(".both", {{ backgroundColor: "{GOLD}", duration: 0.4, stagger: 0.01 }}, 5.6);\n      tl.to(".nonly", {{ backgroundColor: "#e8cf8f", duration: 0.4, stagger: 0.01 }}, 5.8);\n'
js += '      tl.to(".out", { opacity: 0.12, scale: 0.7, duration: 0.6 }, 8.4);\n      tl.to("#frame", { opacity: 1, duration: 0.5 }, 8.7);\n'
js += '      tl.to(".spot:not(.both)", { opacity: 0.4, duration: 0.4 }, 11.1);\n      tl.to(".both", { scale: 1.18, duration: 0.3, yoyo: true, repeat: 1 }, 11.2);\n'
write('fig7_given_spotify', 15, body, js, css)

# ---------------------------------------------------------------- Fig 8: Problem 1 Venn (static illustration)
body = f'''        <svg class="abs" style="left:0;top:0" width="1640" height="740" viewBox="0 0 1640 740">
          <rect x="60" y="40" width="1060" height="660" rx="26" fill="#fff" stroke="{NAVY}" stroke-width="4"/>
          <text x="95" y="100" font-family="Montserrat" font-weight="700" font-size="40" fill="{NAVY}">S</text>
          <circle cx="400" cy="380" r="220" fill="#dce5ee" fill-opacity="0.9" stroke="{BLUE}" stroke-width="4"/>
          <circle cx="660" cy="380" r="220" fill="{GOLDPALE}" fill-opacity="0.75" stroke="{GOLD}" stroke-width="4"/>
          <circle cx="980" cy="300" r="105" fill="{PALE}" stroke="{NAVY}" stroke-width="4"/>
          <text x="245" y="160" font-family="Montserrat" font-weight="700" font-size="40" fill="{BLUE}">A</text>
          <text x="790" y="160" font-family="Montserrat" font-weight="700" font-size="40" fill="#8a6d1f">B</text>
          <text x="965" y="170" font-family="Montserrat" font-weight="700" font-size="40" fill="{NAVY}">C</text>
          <g font-family="Open Sans" font-weight="600" font-size="30" fill="{TEXT}" text-anchor="middle">
            <text x="320" y="340">copper</text><text x="320" y="440">zinc</text>
            <text x="530" y="392">sodium</text>
            <text x="745" y="340">nitrogen</text><text x="745" y="440">potassium</text>
            <text x="980" y="310">oxygen</text>
            <text x="980" y="600">uranium</text>
          </g>
        </svg>
        <div class="abs" style="left:1170px;top:150px;width:440px">
          <div class="lbl" style="color:{BLUE};font-size:26px">A = {{copper, sodium, zinc}}</div>
          <div class="lbl" style="color:#8a6d1f;font-size:26px;margin-top:26px;white-space:normal">B = {{sodium, nitrogen, potassium}}</div>
          <div class="lbl" style="color:{NAVY};font-size:26px;margin-top:26px">C = {{oxygen}}</div>
          <div class="note" style="margin-top:40px">Uranium is in S but in none of the three events.</div>
        </div>
'''
write('fig8_problem1_venn', 2, body, '      tl.to({}, { duration: 0.1 }, 0);\n')
print('ok')
