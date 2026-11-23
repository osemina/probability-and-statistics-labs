"""Pictures for the Lab 6 Excel workbooks: formula images (like the original Lab 6 workbooks) and chart images."""
import os, math, re
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from scipy import stats

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'xl_img')
os.makedirs(OUT, exist_ok=True)

NAVY, BLUE, MID, PALE, GOLD, RED, TEXT, MUTED = '#003e67', '#1f5f99', '#7fa7cc', '#eef2f6', '#c39a3d', '#b34739', '#202020', '#5f6368'
plt.rcParams.update({'font.family': 'DejaVu Sans', 'mathtext.fontset': 'cm', 'font.size': 11,
                     'axes.edgecolor': MUTED, 'axes.labelcolor': TEXT, 'xtick.color': TEXT, 'ytick.color': TEXT})


def formula(name, tex, size=17):
    """Render one LaTeX formula (mathtext) to a tight PNG; returns (path, width_px, height_px)."""
    tex = re.sub(r'\\ge(?![a-z])', r'\\geq', tex)
    tex = re.sub(r'\\le(?![a-z])', r'\\leq', tex)
    fig = plt.figure(figsize=(0.01, 0.01))
    fig.text(0, 0, f'${tex}$', fontsize=size, color='#111111')
    path = os.path.join(OUT, name + '.png')
    fig.savefig(path, dpi=110, bbox_inches='tight', pad_inches=0.06, facecolor='white')
    plt.close(fig)
    from PIL import Image
    w, h = Image.open(path).size
    return path, w, h


def _save(fig, name):
    path = os.path.join(OUT, name + '.png')
    fig.savefig(path, dpi=100, facecolor='white')
    plt.close(fig)
    return path


def _clean(ax):
    for s in ('top', 'right', 'left'):
        ax.spines[s].set_visible(False)
    ax.set_yticks([])


def sampling_curve(name, mu, se, lo, hi, below, unit, title):
    """Normal curve of X-bar with the 'between' area (blue) and the 'below' tail (gold)."""
    fig, ax = plt.subplots(figsize=(6.4, 2.9))
    x = [mu - 4 * se + i * 8 * se / 400 for i in range(401)]
    y = [stats.norm.pdf(v, mu, se) for v in x]
    ax.plot(x, y, color=NAVY, lw=2.2)
    xb = [v for v in x if lo <= v <= hi]
    ax.fill_between(xb, [stats.norm.pdf(v, mu, se) for v in xb], color=MID, alpha=0.8, label=f'b) {lo:g} < X̄ < {hi:g}')
    xt = [v for v in x if v <= below]
    ax.fill_between(xt, [stats.norm.pdf(v, mu, se) for v in xt], color=GOLD, alpha=0.9, label=f'c) X̄ < {below:g}')
    ax.axvline(mu, color=TEXT, ls='--', lw=1)
    pb = stats.norm.cdf(hi, mu, se) - stats.norm.cdf(lo, mu, se)
    pc = stats.norm.cdf(below, mu, se)
    ax.text(mu, max(y) * 0.45, f'{pb:.4f}', ha='center', color='white', fontsize=12, fontweight='bold')
    ax.annotate(f'{pc:.4f}', xy=(below - se * 0.3, stats.norm.pdf(below, mu, se) * 0.4), xytext=(mu - 3.6 * se, max(y) * 0.45),
                color='#8a6d1f', fontsize=11, fontweight='bold', arrowprops=dict(arrowstyle='->', color='#8a6d1f'))
    _clean(ax)
    ax.set_xlabel(f'sample mean X̄ ({unit})')
    ax.set_title(title, color=NAVY, fontsize=12, fontweight='bold', loc='left')
    ax.legend(frameon=False, fontsize=9, loc='upper right')
    fig.tight_layout()
    return _save(fig, name)


def t_claim(name, t, df, tc, title):
    fig, ax = plt.subplots(figsize=(6.4, 2.9))
    x = [-4 + i * 8 / 400 for i in range(401)]
    y = [stats.t.pdf(v, df) for v in x]
    ax.plot(x, y, color=NAVY, lw=2.2)
    xm = [v for v in x if -tc <= v <= tc]
    ax.fill_between(xm, [stats.t.pdf(v, df) for v in xm], color=MID, alpha=0.7)
    ax.text(0, 0.15, 'claim accepted', ha='center', color='white', fontsize=11, fontweight='bold')
    for s in (-1, 1):
        ax.axvline(s * tc, color=NAVY, ls='--', lw=1.2)
        ax.text(s * tc, 0.41, f'{"−" if s < 0 else "+"}{tc:.3f}', ha='center', color=NAVY, fontsize=10, fontweight='bold')
    ax.axvline(t, color=RED, lw=2.5)
    ax.text(t, 0.30, f't = {t:g}', ha='right' if t < 0 else 'left', color=RED, fontsize=11, fontweight='bold')
    _clean(ax)
    ax.set_ylim(0, 0.45)
    ax.set_xlabel(f't (df = {df})')
    ax.set_title(title, color=NAVY, fontsize=12, fontweight='bold', loc='left')
    fig.tight_layout()
    return _save(fig, name)


def intervals(name, rows, title, unit, ref=None, ref_label=None, ref_up=0.0):
    """rows: list of (label, lower, center, upper, color)."""
    fig, ax = plt.subplots(figsize=(6.4, 0.9 + 0.62 * len(rows) + ref_up))
    for i, (lab, lo, c, hi, col) in enumerate(rows):
        yy = len(rows) - 1 - i
        ax.plot([lo, hi], [yy, yy], color=col, lw=7, solid_capstyle='round')
        ax.plot([c], [yy], 'o', color=GOLD, ms=9, mec='white', mew=1.5)
        ax.text(lo, yy + 0.28, f'{lo:g}', ha='center', fontsize=9, color=TEXT)
        ax.text(hi, yy + 0.28, f'{hi:g}', ha='center', fontsize=9, color=TEXT)
    ax.set_yticks(range(len(rows)))
    ax.set_yticklabels([r[0] for r in rows][::-1], fontsize=10)
    if ref is not None:
        ax.axvline(ref, color=RED, ls='--', lw=1.8)
        ax.text(ref, len(rows) - 0.35 + ref_up, ref_label, color=RED, fontsize=10, ha='center', fontweight='bold')
    for s in ('top', 'right', 'left'):
        ax.spines[s].set_visible(False)
    ax.tick_params(axis='y', length=0)
    ax.set_ylim(-0.6, len(rows) - 0.1 + ref_up)
    span = max(r[3] for r in rows) - min(r[1] for r in rows)
    ax.set_xlim(min(r[1] for r in rows + ([('', ref, ref, ref, '')] if ref is not None else [])) - 0.15 * span,
                max(r[3] for r in rows + ([('', ref, ref, ref, '')] if ref is not None else [])) + 0.15 * span)
    ax.set_xlabel(unit)
    ax.set_title(title, color=NAVY, fontsize=12, fontweight='bold', loc='left')
    fig.tight_layout()
    return _save(fig, name)


def ratings(name, counts, lo, hi, title):
    fig, (a1, a2) = plt.subplots(1, 2, figsize=(6.4, 2.6), gridspec_kw={'width_ratios': [1, 1.4]})
    labs = ['0\ndo not like', '1\nlike', '2\nindifferent']
    cols = [MUTED, BLUE, MID]
    a1.bar(labs, counts, color=cols, width=0.6)
    for i, c in enumerate(counts):
        a1.text(i, c + 0.6, str(c), ha='center', fontsize=10, fontweight='bold', color=TEXT)
    a1.set_ylim(0, max(counts) * 1.25)
    for s in ('top', 'right'):
        a1.spines[s].set_visible(False)
    a1.set_title('Ratings of 50 players', fontsize=10, color=NAVY, fontweight='bold')
    a1.tick_params(labelsize=8)
    a2.plot([lo, hi], [0, 0], color=BLUE, lw=8, solid_capstyle='round')
    a2.plot([0.30], [0], 'o', color=GOLD, ms=10, mec='white', mew=1.5)
    a2.axvline(0.40, color=RED, ls='--', lw=1.8)
    a2.text(0.40, 0.55, 'required 40%', color=RED, ha='center', fontsize=9, fontweight='bold')
    a2.text(lo, 0.2, f'{lo:.3f}', ha='center', fontsize=9)
    a2.text(hi, 0.2, f'{hi:.3f}', ha='center', fontsize=9)
    a2.set_xlim(0.15, 0.45)
    a2.set_ylim(-0.6, 0.8)
    a2.set_yticks([])
    for s in ('top', 'right', 'left'):
        a2.spines[s].set_visible(False)
    a2.set_title('80% interval for π', fontsize=10, color=NAVY, fontweight='bold')
    a2.set_xlabel('proportion who like the game', fontsize=9)
    fig.suptitle(title, color=NAVY, fontsize=12, fontweight='bold', x=0.02, ha='left')
    fig.tight_layout()
    return _save(fig, name)


def test_curve(name, stat, crits, tail, title, df=None, pval=None, label='z'):
    """Standard normal (df=None) or t curve with the rejection region (gold) and the test statistic (red line)."""
    fig, ax = plt.subplots(figsize=(6.4, 2.9))
    pdf = (lambda v: stats.norm.pdf(v)) if df is None else (lambda v: stats.t.pdf(v, df))
    lim = max(4.0, abs(stat) + 0.8)
    x = [-lim + i * 2 * lim / 600 for i in range(601)]
    y = [pdf(v) for v in x]
    ax.plot(x, y, color=NAVY, lw=2.2)
    ax.fill_between(x, y, color=MID, alpha=0.35)
    regions = {'two': [(-lim, -crits[0]), (crits[0], lim)], 'right': [(crits[0], lim)], 'left': [(-lim, crits[0])]}[tail]
    for a, b in regions:
        xs = [v for v in x if a <= v <= b]
        ax.fill_between(xs, [pdf(v) for v in xs], color=GOLD, alpha=0.95)
        c = b if a == -lim else a
        ax.axvline(c, color=NAVY, ls='--', lw=1.2)
        ax.text(c, max(y) * 1.04, f'{c:.3f}'.rstrip('0').rstrip('.'), ha='center', color=NAVY, fontsize=9, fontweight='bold')
    ax.axvline(stat, color=RED, lw=2.5)
    reject = any(a <= stat <= b for a, b in regions)
    txt = f'{label} = {stat:.2f}' + (f'\np = {pval:.4f}' if pval is not None else '')
    ax.text(stat + (0.12 if stat < lim - 1.5 else -0.12), max(y) * 0.62, txt, ha='left' if stat < lim - 1.5 else 'right', color=RED, fontsize=10, fontweight='bold')
    ax.text(0, max(y) * 0.35, 'reject H₀' if reject else 'fail to reject H₀', ha='center', color='white' if not reject else NAVY,
            fontsize=11, fontweight='bold', alpha=0.0)
    for s in ('top', 'right', 'left'):
        ax.spines[s].set_visible(False)
    ax.set_yticks([])
    ax.set_ylim(0, max(y) * 1.15)
    ax.set_xlabel(label if df is None else f'{label} (df = {df})')
    ax.set_title(title + ('  →  reject H₀' if reject else '  →  fail to reject H₀'), color=NAVY, fontsize=11.5, fontweight='bold', loc='left')
    fig.tight_layout()
    return _save(fig, name)


def f_curve(name, stat, crit, tail, title, dfs, pval=None):
    """F curve (right-skewed) with the rejection region (gold) and the F statistic (red line). tail: 'right' or 'left'."""
    d1, d2 = dfs
    pdf = lambda v: stats.f.pdf(v, d1, d2)
    lim = max(3.5, stat + 1.0, crit + 1.0)
    x = [0.001 + i * lim / 600 for i in range(601)]
    y = [pdf(v) for v in x]
    fig, ax = plt.subplots(figsize=(6.4, 2.9))
    ax.plot(x, y, color=NAVY, lw=2.2)
    ax.fill_between(x, y, color=MID, alpha=0.35)
    a, b = (crit, lim) if tail == 'right' else (0.001, crit)
    xs = [v for v in x if a <= v <= b]
    ax.fill_between(xs, [pdf(v) for v in xs], color=GOLD, alpha=0.95)
    ax.axvline(crit, color=NAVY, ls='--', lw=1.2)
    ax.text(crit, max(y) * 1.04, f'{crit:.3f}', ha='center', color=NAVY, fontsize=9, fontweight='bold')
    ax.axvline(stat, color=RED, lw=2.5)
    reject = a <= stat <= b
    txt = f'F = {stat:.3f}' + (f'\np = {pval:.4f}' if pval is not None else '')
    right_side = stat < lim - 1.2 and not (tail == 'right' and stat < crit) and not (tail == 'left' and stat < crit)
    ax.text(stat + (0.06 if right_side else -0.06), max(y) * 0.62, txt, ha='left' if right_side else 'right', color=RED, fontsize=10, fontweight='bold')
    _clean(ax)
    ax.set_ylim(0, max(y) * 1.15)
    ax.set_xlim(0, lim)
    ax.set_xlabel(f'F (v₁ = {d1}, v₂ = {d2})')
    ax.set_title(title + ('  →  reject H₀' if reject else '  →  fail to reject H₀'), color=NAVY, fontsize=11.5, fontweight='bold', loc='left')
    fig.tight_layout()
    return _save(fig, name)
