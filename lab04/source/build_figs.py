from common import write

NAVY, BLUE, LIGHT, PALE, GOLD, GOLDPALE, PANEL, RED, TEXT, MUTED = (
    '#003e67', '#1f5f99', '#c9d6e3', '#eef2f6', '#c39a3d', '#f1e4c6', '#f3f3f0', '#b34739', '#202020', '#5f6368')
YELLOW = '#f5c400'


def chart(pid, x0, base, vals, xlabels, maxv, H, bw, gap, color=BLUE, vlabels=None, ticks=()):
    """Bar chart. Returns body html; bars are #{pid}b{i}, value labels #{pid}v{i}."""
    W = len(vals) * (bw + gap) - gap
    h = f'        <div class="abs" style="left:{x0-10}px;top:{base}px;width:{W+20}px;height:3px;background:{MUTED}"></div>\n'
    for t, tl in ticks:
        y = base - t / maxv * H
        h += (f'        <div class="abs" style="left:{x0-10}px;top:{y}px;width:{W+20}px;height:0;border-top:2px dashed {LIGHT}"></div>\n'
              f'        <div class="sub abs" style="left:{x0-80}px;top:{y-14}px;width:62px;text-align:right;font-size:19px">{tl}</div>\n')
    for i, v in enumerate(vals):
        x = x0 + i * (bw + gap)
        bh = max(v / maxv * H, 2)
        h += f'        <div id="{pid}b{i}" class="abs" style="left:{x}px;top:{base-bh}px;width:{bw}px;height:{bh}px;border-radius:8px 8px 0 0;background:{color};transform-origin:50% 100%;transform:scaleY(0)"></div>\n'
        h += f'        <div class="abs" style="left:{x-20}px;top:{base+10}px;width:{bw+40}px;text-align:center;font:600 22px \'Open Sans\';color:{TEXT}">{xlabels[i]}</div>\n'
        if vlabels:
            h += f'        <div id="{pid}v{i}" class="abs" style="left:{x-30}px;top:{base-bh-32}px;width:{bw+60}px;text-align:center;font:600 19px \'Open Sans\';color:{MUTED};opacity:0">{vlabels[i]}</div>\n'
    return h


def grow(pid, n, t0, step, dur=0.45):
    js = ''
    for i in range(n):
        js += f'      tl.to("#{pid}b{i}", {{ scaleY: 1, duration: {dur}, ease: "power2.out" }}, {t0 + i*step:.2f});\n'
        js += f'      tl.to("#{pid}v{i}", {{ opacity: 1, duration: 0.3 }}, {t0 + i*step + 0.25:.2f});\n'
    return js


def card(x, y, w, h, extra=''):
    return f'        <div class="abs card" style="left:{x}px;top:{y}px;width:{w}px;height:{h}px;{extra}"></div>\n'


def text(id_, x, y, html, cls='sub', style=''):
    return f'        <div id="{id_}" class="{cls} abs" style="left:{x}px;top:{y}px;opacity:0;{style}">{html}</div>\n'


def show(ids, t, dur=0.4, dy=0):
    ids = ids if isinstance(ids, list) else [ids]
    sel = ', '.join(f'"#{i}"' for i in ids)
    if dy:
        return f'      tl.fromTo([{sel}], {{ opacity: 0, y: {dy} }}, {{ opacity: 1, y: 0, duration: {dur} }}, {t});\n'
    return f'      tl.to([{sel}], {{ opacity: 1, duration: {dur} }}, {t});\n'


# ---------------------------------------------------------------- Fig 1: PMF and CDF of a die
body = card(40, 40, 760, 660) + card(840, 40, 760, 660)
body += '        <div class="lbl abs" style="left:80px;top:70px;color:#003e67;font-size:30px">PMF: P(X = x)</div>\n'
body += '        <div class="sub abs" style="left:80px;top:116px">the probability of each single value</div>\n'
body += '        <div class="lbl abs" style="left:880px;top:70px;color:#003e67;font-size:30px">CDF: F(x) = P(X &#8804; x)</div>\n'
body += '        <div class="sub abs" style="left:880px;top:116px">add up all probabilities up to x</div>\n'
body += chart('p', 180, 590, [1/6]*6, list('123456'), 0.25, 380, 72, 30, BLUE, ['1/6']*6, [(1/6, '1/6')])
cdf = [k/6 for k in range(1, 7)]
body += chart('c', 980, 590, cdf, list('123456'), 1.0, 380, 72, 30, LIGHT, [f'{k}/6' for k in range(1, 7)], [(0.5, '0.5'), (1, '1')])
body += '        <div class="sub abs" style="left:420px;top:640px;font-size:20px">face x</div>\n'
body += '        <div class="sub abs" style="left:1220px;top:640px;font-size:20px">face x</div>\n'
body += text('f3', 975, 232, 'F(3) = 1/6 + 1/6 + 1/6 = 0.5', 'eq', 'font-size:24px')
body += text('f6', 975, 274, 'F(6) = 1', 'eq', f'font-size:24px;color:{GOLD}')
js = grow('p', 6, 0.3, 0.15)
for k in range(6):
    js += f'      tl.to("#cb{k}", {{ scaleY: 1, duration: 0.5, ease: "power2.out" }}, {2.0 + k*0.45:.2f});\n'
    js += f'      tl.to("#cv{k}", {{ opacity: 1, duration: 0.3 }}, {2.3 + k*0.45:.2f});\n'
    js += f'      tl.to("#pb{k}", {{ backgroundColor: "{NAVY}", duration: 0.3, yoyo: true, repeat: 1 }}, {2.0 + k*0.45:.2f});\n'
js += f'      tl.to(["#cb0", "#cb1", "#cb2"], {{ backgroundColor: "{BLUE}", duration: 0.4 }}, 5.6);\n'
js += f'      tl.to(["#pb0", "#pb1", "#pb2"], {{ backgroundColor: "{NAVY}", duration: 0.4 }}, 5.6);\n'
js += f'      tl.to("#cb2", {{ backgroundColor: "{NAVY}", duration: 0.4 }}, 6.0);\n'
js += show('f3', 6.0, dy=10)
js += f'      tl.to("#cb5", {{ backgroundColor: "{GOLD}", duration: 0.4 }}, 8.0);\n'
js += show('f6', 8.0, dy=10)
write('fig1_die_pmf_cdf', 12, body, js)

# ---------------------------------------------------------------- Fig 2: expected value as balance point
X0, PX, BY = 140, 120, 430      # x position of face 1, pixels per unit, beam top
fx = lambda v: X0 + (v - 1) * PX
body = card(40, 40, 960, 660)
body += '        <div class="lbl abs" style="left:80px;top:70px;color:#003e67;font-size:30px">E(X) is the balance point</div>\n'
body += '        <div class="sub abs" style="left:80px;top:116px">each face of a fair die has the same weight, 1/6</div>\n'
body += f'        <div id="beam" class="abs" style="left:{fx(1)-50}px;top:{BY}px;width:{5*PX+100}px;height:14px;border-radius:7px;background:{NAVY};transform-origin:50px 7px"></div>\n'
for v in range(1, 7):
    body += f'        <div id="w{v}" class="abs" style="left:{fx(v)-35}px;top:{BY-74}px;width:70px;height:70px;border-radius:16px;background:{GOLDPALE};border:4px solid {GOLD};text-align:center;font:700 30px Montserrat;line-height:62px;color:{NAVY};opacity:0">{v}</div>\n'
    body += f'        <div class="sub abs" style="left:{fx(v)-35}px;top:{BY+26}px;width:70px;text-align:center;font-size:19px">1/6</div>\n'
body += f'        <div id="ful" class="abs" style="left:{fx(1)-40}px;top:{BY+14}px;width:0;height:0;border-left:40px solid transparent;border-right:40px solid transparent;border-bottom:80px solid {GOLD}"></div>\n'
body += f'        <div class="abs" style="left:{fx(1)-80}px;top:{BY+94}px;width:{5*PX+160}px;height:6px;border-radius:3px;background:{LIGHT}"></div>\n'
body += text('mu', fx(3.5)-90, BY+120, 'E(X) = 3.5', 'eq', f'width:180px;text-align:center;color:{GOLD}')
body += text('s1', 1060, 110, 'Multiply each value by its probability', 'step')
body += text('s2', 1060, 165, '1&#183;&#8537; + 2&#183;&#8537; + 3&#183;&#8537; + 4&#183;&#8537; + 5&#183;&#8537; + 6&#183;&#8537;', 'rt')
body += text('s3', 1060, 225, 'and add: 21/6 = 3.5', 'eq')
body += text('s4', 1060, 330, '3.5 is not a face of the die.', 'rt', f'color:{NAVY}')
body += text('s5', 1060, 380, 'It is the long-run average: roll the die many times and the average of the results gets close to 3.5.', 'note', 'width:520px')
js = ''.join(f'      tl.fromTo("#w{v}", {{ opacity: 0, y: -40 }}, {{ opacity: 1, y: 0, duration: 0.4, ease: "bounce.out" }}, {0.3 + v*0.2:.1f});\n' for v in range(1, 7))
js += f'      tl.to("#beam", {{ rotation: 8, duration: 0.8, ease: "power2.inOut" }}, 2.0);\n'
js += ''.join(f'      tl.to("#w{v}", {{ y: {(fx(v)-fx(1))*0.139:.1f}, duration: 0.8, ease: "power2.inOut" }}, 2.0);\n' for v in range(1, 7))
js += show('s1', 2.2) + show('s2', 3.0, dy=8)
js += f'      tl.to("#ful", {{ x: {fx(3.5)-fx(1)}, duration: 2.0, ease: "power2.inOut" }}, 3.4);\n'
js += f'      tl.to("#beam", {{ x: 0, rotation: 0, duration: 1.2, ease: "back.out(1.6)" }}, 5.0);\n'
js += ''.join(f'      tl.to("#w{v}", {{ y: 0, duration: 1.2, ease: "back.out(1.6)" }}, 5.0);\n' for v in range(1, 7))
js += show('s3', 5.2, dy=8) + show('mu', 6.0, dy=10) + show('s4', 7.6) + show('s5', 8.4)
write('fig2_expected_value_balance', 12, body, js)

# ---------------------------------------------------------------- Fig 3: same mean, different spread
body = card(40, 40, 760, 560) + card(840, 40, 760, 560)
body += '        <div class="lbl abs" style="left:80px;top:70px;color:#003e67;font-size:28px">A: values 2, 3, 4</div>\n'
body += '        <div class="lbl abs" style="left:880px;top:70px;color:#8a6d1f;font-size:28px">B: values 0, 3, 6</div>\n'
xs = list(range(7))
pa = [0, 0, .25, .5, .25, 0, 0]
pb = [.25, 0, 0, .5, 0, 0, .25]
body += chart('a', 130, 470, pa, [str(x) for x in xs], 0.6, 300, 70, 26, BLUE, ['', '', '0.25', '0.50', '0.25', '', ''])
body += chart('b', 930, 470, pb, [str(x) for x in xs], 0.6, 300, 70, 26, GOLD, ['0.25', '', '', '0.50', '', '', '0.25'])
for p, x0, col in (('a', 130, NAVY), ('b', 930, NAVY)):
    mx = x0 + 3 * 96 + 35
    body += f'        <div id="{p}m" class="abs" style="left:{mx-2}px;top:224px;width:4px;height:251px;background:{col};opacity:0"></div>\n'
    body += f'        <div id="{p}mt" class="abs" style="left:{mx-60}px;top:150px;width:120px;text-align:center;font:600 22px \'Open Sans\';color:{col};background:{PANEL};opacity:0">mean = 3</div>\n'
for p, x0, d, col in (('a', 130, 1, BLUE), ('b', 930, 3, GOLD)):
    mx = x0 + 3 * 96 + 35
    w = d * 96
    body += f'        <div id="{p}l" class="abs" style="left:{mx-w}px;top:520px;width:{w}px;height:6px;background:{col};transform-origin:100% 50%;transform:scaleX(0)"></div>\n'
    body += f'        <div id="{p}r" class="abs" style="left:{mx}px;top:520px;width:{w}px;height:6px;background:{col};transform-origin:0 50%;transform:scaleX(0)"></div>\n'
    body += text(f'{p}d', mx - 150, 540, f'distance from the mean: {d}', 'sub', 'width:300px;text-align:center;font-size:19px')
body += text('va', 80, 625, 'Var(A) = 0.25&#183;1&#178; + 0.25&#183;1&#178; = 0.5,   &#963; &#8776; 0.71', 'rt', f'color:{BLUE}')
body += text('vb', 880, 625, 'Var(B) = 0.25&#183;3&#178; + 0.25&#183;3&#178; = 4.5,   &#963; &#8776; 2.12', 'rt', 'color:#8a6d1f')
body += text('nt', 80, 680, 'Same expected value, but B is much more spread out, so it has the larger variance.', 'note', f'color:{NAVY};font-weight:600')
js = grow('a', 7, 0.3, 0.1) + grow('b', 7, 0.6, 0.1)
js += show(['am', 'amt', 'bm', 'bmt'], 2.2)
js += '      tl.to(["#al", "#ar"], { scaleX: 1, duration: 0.7 }, 3.4);\n' + show('ad', 3.8)
js += '      tl.to(["#bl", "#br"], { scaleX: 1, duration: 0.9 }, 4.6);\n' + show('bd', 5.1)
js += show('va', 6.4, dy=8) + show('vb', 7.4, dy=8) + show('nt', 8.8, dy=8)
write('fig3_same_mean_spread', 12, body, js)

# ---------------------------------------------------------------- Fig 4: binomial, 3 coin flips
outs = ['HHH', 'HHT', 'HTH', 'THH', 'HTT', 'THT', 'TTH', 'TTT']
body = card(40, 40, 820, 660) + card(900, 40, 700, 660)
body += '        <div class="lbl abs" style="left:80px;top:70px;color:#003e67;font-size:30px">Flip a fair coin 3 times</div>\n'
body += '        <div class="sub abs" style="left:80px;top:116px">8 equally likely outcomes, each with probability 0.5&#179; = 0.125</div>\n'
for i, o in enumerate(outs):
    r, c = divmod(i, 2)
    x, y = 90 + c * 390, 175 + r * 120
    coins = ''.join(f'<div style="display:inline-block;width:62px;height:62px;margin-right:12px;border-radius:50%;background:{YELLOW if ch=="H" else LIGHT};color:{NAVY};font:700 28px Montserrat;text-align:center;line-height:62px">{ch}</div>' for ch in o)
    body += f'        <div id="o{i}" class="abs" style="left:{x}px;top:{y}px;width:360px;height:96px;padding:17px 18px;border-radius:18px;background:#fff;border:4px solid {PALE};opacity:0">{coins}<span style="font:600 20px \'Open Sans\';color:{MUTED}">{o.count("H")} H</span></div>\n'
body += '        <div class="lbl abs" style="left:940px;top:70px;color:#003e67;font-size:28px">X = number of heads</div>\n'
pm = [.125, .375, .375, .125]
body += chart('k', 1040, 560, pm, ['0', '1', '2', '3'], 0.5, 330, 90, 40, LIGHT, ['0.125', '0.375', '0.375', '0.125'])
body += text('cnt', 940, 120, 'Exactly 2 heads: 3 of the 8 outcomes', 'rt', f'color:{NAVY}')
body += text('frm', 940, 618, 'P(X = 2) = C(3, 2)&#183;0.5&#178;&#183;0.5 = 3 &#215; 0.125 = 0.375', 'rt', f'color:{NAVY};font-size:23px')
js = ''.join(f'      tl.fromTo("#o{i}", {{ opacity: 0, scale: 0.85 }}, {{ opacity: 1, scale: 1, duration: 0.35, ease: "back.out(2)" }}, {0.3 + i*0.18:.2f});\n' for i in range(8))
js += grow('k', 4, 2.2, 0.25)
js += '      tl.to(["#o0", "#o4", "#o5", "#o6", "#o7"], { opacity: 0.3, duration: 0.5 }, 4.0);\n'
js += f'      tl.to(["#o1", "#o2", "#o3"], {{ borderColor: "{NAVY}", backgroundColor: "{PALE}", duration: 0.5 }}, 4.0);\n'
js += show('cnt', 4.2, dy=8)
js += f'      tl.to("#kb2", {{ backgroundColor: "{NAVY}", duration: 0.5 }}, 5.6);\n'
js += f'      tl.to("#kv2", {{ color: "{NAVY}", scale: 1.25, duration: 0.5 }}, 5.6);\n'
js += show('frm', 6.4, dy=8)
write('fig4_binomial_three_flips', 12, body, js)

# ---------------------------------------------------------------- Fig 5: Poisson, emails per hour
import math
lam = 4
pk = [math.exp(-lam) * lam**k / math.factorial(k) for k in range(11)]
body = card(40, 40, 520, 660) + card(600, 40, 1000, 660)
body += '        <div class="lbl abs" style="left:80px;top:70px;color:#003e67;font-size:28px">Emails in one hour</div>\n'
body += '        <div class="sub abs" style="left:80px;top:114px">on average &#955; = 4 emails per hour</div>\n'
body += f'        <div class="abs" style="left:90px;top:300px;width:420px;height:8px;border-radius:4px;background:{LIGHT}"></div>\n'
body += '        <div class="sub abs" style="left:80px;top:320px;font-size:18px">0 min</div><div class="sub abs" style="left:450px;top:320px;font-size:18px">60 min</div>\n'
hrs = [[8, 27, 41, 52], [15, 50], [5, 19, 30, 38, 46, 57], [33, 44, 55]]
for h, ts in enumerate(hrs):
    for j, t in enumerate(ts):
        body += f'        <div id="e{h}_{j}" class="abs" style="left:{90 + t*7 - 18}px;top:{232}px;width:36px;height:26px;border-radius:4px;background:{GOLD};opacity:0"><div style="position:absolute;left:4px;top:3px;width:0;height:0;border-left:14px solid transparent;border-right:14px solid transparent;border-top:12px solid #fff"></div></div>\n'
    body += text(f'hl{h}', 90, 370, f'hour {h+1}: {len(ts)} emails', 'rt', f'color:{NAVY}')
body += text('rnd', 80, 430, 'The count changes from hour to hour. The Poisson distribution gives the probability of each count.', 'note', 'width:450px;font-size:21px')
body += '        <div class="lbl abs" style="left:640px;top:70px;color:#003e67;font-size:28px">P(X = k) for &#955; = 4</div>\n'
body += chart('q', 700, 590, pk, [str(k) for k in range(11)], 0.25, 400, 62, 22, LIGHT, [f'{v:.3f}'.lstrip('0') for v in pk])
body += text('mk', 700 + 4*84 - 30, 116, 'mean &#955; = 4', 'rt', f'color:{GOLD};width:150px;text-align:center')
body += text('fq', 1150, 116, 'P(X = 2) = e&#8315;&#8308;&#183;4&#178;/2! &#8776; 0.1465', 'rt', f'color:{NAVY}')
js = ''
t = 0.3
for h, ts in enumerate(hrs):
    for j in range(len(ts)):
        js += f'      tl.fromTo("#e{h}_{j}", {{ opacity: 0, y: -30 }}, {{ opacity: 1, y: 0, duration: 0.25, ease: "back.out(2)" }}, {t + j*0.15:.2f});\n'
    js += show(f'hl{h}', t + 0.3, 0.3)
    if h < 3:
        js += f'      tl.to([{", ".join(f"{chr(34)}#e{h}_{j}{chr(34)}" for j in range(len(ts)))}, "#hl{h}"], {{ opacity: 0, duration: 0.3 }}, {t + 1.3:.2f});\n'
    t += 1.6
js += show('rnd', 3.4)
js += grow('q', 11, 1.0, 0.18)
js += f'      tl.to("#qb4", {{ backgroundColor: "{GOLD}", duration: 0.4 }}, 4.0);\n' + show('mk', 4.0)
js += f'      tl.to("#qb2", {{ backgroundColor: "{NAVY}", duration: 0.5 }}, 6.6);\n'
js += f'      tl.to("#qv2", {{ color: "{NAVY}", duration: 0.5 }}, 6.6);\n'
js += f'      tl.to("#mk", {{ opacity: 0, duration: 0.3 }}, 6.4);\n'
js += show('fq', 6.8, dy=8)
write('fig5_poisson_emails', 12, body, js)

# ---------------------------------------------------------------- Fig 6: geometric, first head on 3rd flip
body = card(40, 40, 760, 660) + card(840, 40, 760, 660)
body += '        <div class="lbl abs" style="left:80px;top:70px;color:#003e67;font-size:30px">Flip until the first head</div>\n'
body += '        <div class="sub abs" style="left:80px;top:116px">p = 0.5 for heads on every flip</div>\n'
seq = [('T', 'tail', '0.5'), ('T', 'tail', '0.5'), ('H', 'head!', '0.5')]
for i, (ch, lab, pr) in enumerate(seq):
    x = 110 + i * 230
    body += f'        <div id="g{i}" class="abs" style="left:{x}px;top:200px;width:150px;height:150px;border-radius:50%;background:{YELLOW if ch=="H" else LIGHT};color:{NAVY};font:700 64px Montserrat;text-align:center;line-height:150px;opacity:0">{ch}</div>\n'
    body += text(f'gl{i}', x, 365, f'flip {i+1}: {lab}', 'rt', 'width:150px;text-align:center')
    body += text(f'gp{i}', x, 405, pr, 'eq', 'width:150px;text-align:center')
    if i < 2:
        body += text(f'gx{i}', x + 168, 405, '&#215;', 'eq', f'color:{MUTED}')
body += text('gr', 90, 490, 'P(X = 3) = (1 &#8722; p)&#178;&#183;p = 0.5&#178;&#183;0.5 = 0.125', 'eq', 'font-size:27px')
body += text('gn', 90, 560, 'Two failures first, then the first success.', 'note', 'width:660px')
body += '        <div class="lbl abs" style="left:880px;top:70px;color:#003e67;font-size:28px">P(X = k): number of flips needed</div>\n'
gk = [0.5 ** k for k in range(1, 8)]
body += chart('r', 960, 590, gk, [str(k) for k in range(1, 8)], 0.6, 400, 66, 24, LIGHT, ['0.5', '0.25', '0.125', '0.063', '0.031', '0.016', '0.008'])
body += text('ex', 1200, 170, 'E(X) = 1/p = 2 flips', 'rt', f'color:{GOLD}')
body += text('dc', 1200, 210, 'each bar is half of the one before', 'sub', 'font-size:19px')
js = ''
for i in range(3):
    js += f'      tl.fromTo("#g{i}", {{ opacity: 0, rotationY: 540 }}, {{ opacity: 1, rotationY: 0, duration: 0.8, ease: "power2.out" }}, {0.4 + i*1.1:.1f});\n'
    js += show([f'gl{i}', f'gp{i}'], 0.9 + i*1.1)
    if i < 2:
        js += show(f'gx{i}', 1.2 + i*1.1)
js += show('gr', 4.0, dy=8) + show('gn', 4.8)
js += grow('r', 7, 5.4, 0.2)
js += f'      tl.to("#rb2", {{ backgroundColor: "{NAVY}", duration: 0.5 }}, 7.2);\n'
js += f'      tl.to("#rv2", {{ color: "{NAVY}", duration: 0.5 }}, 7.2);\n'
js += show('dc', 7.8) + show('ex', 8.6, dy=8)
write('fig6_geometric_first_head', 12, body, js)
print('ok')
