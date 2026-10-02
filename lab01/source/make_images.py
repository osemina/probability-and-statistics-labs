"""Illustrations for [Lab 1] Fundamentals of Statistics (IBU 014).

Palette follows the lab template: navy, gold, warning red, teal (validated for CVD).
"""
import io
import os
import random

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams["mathtext.fontset"] = "dejavusans"
from matplotlib import font_manager as fm
from matplotlib.patches import FancyBboxPatch, Rectangle, Circle, FancyArrowPatch
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "fonts")
OUT = os.path.join(HERE, "img")
os.makedirs(OUT, exist_ok=True)

for f in os.listdir(FONTS):
    if "-" in f:
        fm.fontManager.addfont(os.path.join(FONTS, f))


def F(family, weight=400, size=12):
    return fm.FontProperties(fname=os.path.join(FONTS, f"{family}-{weight}.ttf"), size=size)


NAVY = "#003E67"
BLUE = "#1F5F99"
GOLD = "#C39A3D"
RED = "#B3473A"
TEAL = "#14917A"
INK = "#202020"
MUTED = "#6B6B6B"
GRID = "#E6E6E6"
SURF = "#F7F7F5"
LIGHT = "#C9D6E3"
WHITE = "#FFFFFF"


def save_png(fig, name):
    fig.savefig(os.path.join(OUT, name), dpi=200, facecolor=fig.get_facecolor())
    plt.close(fig)


def fig_to_pil(fig, dpi=100):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=dpi, facecolor=fig.get_facecolor())
    plt.close(fig)
    buf.seek(0)
    return Image.open(buf).convert("RGB")


def save_gif(frames, name, durations):
    # One shared adaptive palette keeps colors stable across frames.
    pal = frames[-1].quantize(colors=64, method=Image.Quantize.MEDIANCUT)
    q = [fr.quantize(palette=pal, dither=Image.Dither.NONE) for fr in frames]
    q[0].save(os.path.join(OUT, name), save_all=True, append_images=q[1:],
              duration=durations, loop=0, optimize=True, disposal=1)


def card(ax, x, y, w, h, fc, ec=None, r=0.02, lw=0):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}",
                                fc=fc, ec=ec or fc, lw=lw))


def arrow(ax, p0, p1, color, rad=0.0, lw=2.2):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=18, color=color, lw=lw,
                                 connectionstyle=f"arc3,rad={rad}"))


# --------------------------------------------------------------------------------------------
# Figure 1: population -> sample -> inference
# --------------------------------------------------------------------------------------------
def figure_population_sample():
    random.seed(7)
    fig = plt.figure(figsize=(8, 3.9), facecolor=WHITE)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 8); ax.set_ylim(0, 3.9); ax.axis("off")

    # population panel
    card(ax, 0.2, 0.35, 4.1, 3.3, SURF, r=0.12)
    ax.text(0.45, 3.35, "POPULATION", fontproperties=F("Montserrat", 700, 11), color=NAVY)
    ax.text(0.45, 3.08, "all 2,440 cans in the shipment  ·  size N", fontproperties=F("OpenSans", 400, 8.5), color=MUTED)
    cols, rows = 26, 12
    picked = set(random.sample(range(cols * rows), 22))
    for i in range(cols * rows):
        cx = 0.5 + (i % cols) * 0.138
        cy = 0.62 + (i // cols) * 0.192
        ax.add_patch(Circle((cx, cy), 0.045, fc=GOLD if i in picked else LIGHT, ec="none"))
    ax.text(0.45, 0.12, "Parameter  μ = true mean weight of all cans (unknown)",
            fontproperties=F("OpenSans", 600, 8.5), color=NAVY)

    # sample panel
    card(ax, 5.35, 1.2, 2.45, 2.45, SURF, r=0.12)
    ax.text(5.6, 3.35, "SAMPLE", fontproperties=F("Montserrat", 700, 11), color=NAVY)
    ax.text(5.6, 3.08, "50 cans that were weighed  ·  size n", fontproperties=F("OpenSans", 400, 8.5), color=MUTED)
    for i in range(50):
        cx = 5.72 + (i % 10) * 0.2
        cy = 1.5 + (i // 10) * 0.3
        ax.add_patch(Circle((cx, cy), 0.06, fc=GOLD, ec="none"))
    ax.text(5.6, 0.85, r"Statistic  $\bar{x}$ = mean weight of the 50 cans",
            fontproperties=F("OpenSans", 600, 8.5), color=NAVY)
    ax.text(5.6, 0.6, "(computed from data)", fontproperties=F("OpenSans", 400, 8.5), color=MUTED)

    # arrows
    arrow(ax, (4.4, 3.0), (5.25, 3.0), NAVY, rad=-0.0)
    ax.text(4.83, 3.12, "select", ha="center", fontproperties=F("OpenSans", 600, 8.5), color=NAVY)
    arrow(ax, (5.25, 1.6), (4.4, 1.6), RED)
    ax.text(4.83, 1.72, "infer", ha="center", fontproperties=F("OpenSans", 600, 8.5), color=RED)
    ax.text(4.83, 1.3, r"$\bar{x}$ estimates μ", ha="center", fontproperties=F("OpenSans", 400, 7.5), color=MUTED)
    save_png(fig, "fig1_population_sample.png")


# --------------------------------------------------------------------------------------------
# Figure 2: types of data tree
# --------------------------------------------------------------------------------------------
def figure_data_types():
    fig = plt.figure(figsize=(8, 4.1), facecolor=WHITE)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 8); ax.set_ylim(0, 4.1); ax.axis("off")

    def node(x, y, w, h, title, sub, fc, tc=WHITE, sc=None):
        card(ax, x - w / 2, y - h / 2, w, h, fc, r=0.08)
        ax.text(x, y + (0.1 if sub else 0), title, ha="center", va="center",
                fontproperties=F("Montserrat", 700, 10.5), color=tc)
        if sub:
            ax.text(x, y - 0.17, sub, ha="center", va="center",
                    fontproperties=F("OpenSans", 400, 8), color=sc or tc)

    def link(x0, y0, x1, y1):
        ym = (y0 + y1) / 2
        ax.plot([x0, x0, x1, x1], [y0, ym, ym, y1], color="#9AA5B1", lw=1.4, solid_capstyle="round")

    node(4, 3.65, 1.7, 0.5, "DATA", None, INK)
    link(4, 3.4, 2, 2.92); link(4, 3.4, 6, 2.92)
    node(2, 2.65, 3.0, 0.62, "Categorical", "qualitative  ·  labels or groups", BLUE)
    node(6, 2.65, 3.0, 0.62, "Numerical", "quantitative  ·  counts or measurements", TEAL)
    for px, cx, fc in ((2, 1.15, BLUE), (2, 2.85, BLUE), (6, 5.15, TEAL), (6, 6.85, TEAL)):
        link(px, 2.34, cx, 1.88)

    leaves = [
        (1.15, "Nominal", "no natural order", ["eye colour", "fish species", "programme: IT, EEE"]),
        (2.85, "Ordinal", "categories have an order", ["satisfaction 1–5", "grade A–F", "small / medium / large"]),
        (5.15, "Discrete", "counted · whole numbers", ["number of siblings", "defects per hour", "cars per hour"]),
        (6.85, "Continuous", "measured · any value", ["can weight (lb)", "voltage (V)", "waiting time (s)"]),
    ]
    for x, t, s, ex in leaves:
        card(ax, x - 0.78, 0.2, 1.56, 1.68, SURF, r=0.08)
        ax.text(x, 1.62, t, ha="center", fontproperties=F("Montserrat", 700, 10), color=NAVY)
        ax.text(x, 1.38, s, ha="center", fontproperties=F("OpenSans", 400, 7.5), color=MUTED)
        for i, e in enumerate(ex):
            ax.text(x, 1.0 - i * 0.26, e, ha="center", fontproperties=F("OpenSans", 400, 8), color=INK)
    save_png(fig, "fig2_data_types.png")


# --------------------------------------------------------------------------------------------
# Figure 3: four probability sampling methods
# --------------------------------------------------------------------------------------------
def figure_sampling_methods():
    random.seed(3)
    fig = plt.figure(figsize=(8, 5.2), facecolor=WHITE)
    cols, rows = 10, 6
    strata_colors = [BLUE, TEAL, RED]
    titles = [
        ("Simple random", "every group of n units is equally likely"),
        ("Systematic", "random start, then every k-th unit (k = 6)"),
        ("Stratified", "split into strata, random sample from each"),
        ("Cluster", "pick whole clusters at random, take everyone"),
    ]
    srs = set(random.sample(range(60), 10))
    start = random.randrange(6)
    syst = set(range(start, 60, 6))
    strat = set()
    for s in range(3):  # strata = pairs of rows
        strat |= set(random.sample(range(s * 20, s * 20 + 20), 4 if s < 2 else 2))
    clusters_chosen = {1, 4}  # 6 clusters of 2 rows x 5 cols
    def cluster_of(i):
        r, c = divmod(i, cols)
        return (r // 2) * 2 + (c // 5)

    for k, (t, sub) in enumerate(titles):
        ax = fig.add_axes([0.03 + (k % 2) * 0.49, 0.06 + (1 - k // 2) * 0.48, 0.45, 0.4])
        ax.set_xlim(-0.8, cols - 0.2); ax.set_ylim(-0.8, rows + 1.2); ax.axis("off"); ax.set_aspect("equal")
        ax.text(-0.6, rows + 0.75, t, fontproperties=F("Montserrat", 700, 10.5), color=NAVY)
        ax.text(-0.6, rows + 0.15, sub, fontproperties=F("OpenSans", 400, 7.8), color=MUTED)
        if k == 2:
            for s in range(3):
                ax.add_patch(FancyBboxPatch((-0.5, (2 - s) * 2 - 0.45 - 0.05), cols, 1.9,
                                            boxstyle="round,pad=0,rounding_size=0.25",
                                            fc=strata_colors[s], ec="none", alpha=0.10))
        if k == 3:
            for cidx in range(6):
                rr, cc = divmod(cidx, 2)
                ax.add_patch(FancyBboxPatch((cc * 5 - 0.42, (2 - rr) * 2 - 0.42 - 0.05), 4.84, 1.84,
                                            boxstyle="round,pad=0,rounding_size=0.25",
                                            fc=GOLD if cidx in clusters_chosen else "none",
                                            alpha=0.18 if cidx in clusters_chosen else 1,
                                            ec="#9AA5B1", lw=1, ls=(0, (3, 2))))
        for i in range(60):
            r, c = divmod(i, cols)
            y = rows - 1 - r - 0.0
            chosen = (i in srs, i in syst, i in strat, cluster_of(i) in clusters_chosen)[k]
            base = LIGHT
            if k == 2:
                base = strata_colors[r // 2]
                fc = base if chosen else WHITE
                ax.add_patch(Circle((c, y), 0.3, fc=fc, ec=base, lw=1.4))
                continue
            ax.add_patch(Circle((c, y), 0.3, fc=GOLD if chosen else base, ec="none"))
            if k == 1 and chosen:
                ax.text(c, y, str(i + 1), ha="center", va="center", fontproperties=F("OpenSans", 700, 5.5), color=WHITE)
    fig.text(0.03, 0.015, "Gold or filled circle = unit chosen for the sample.  Stratified panel: colour = stratum.",
             fontproperties=F("OpenSans", 400, 7.8), color=MUTED)
    save_png(fig, "fig3_sampling_methods.png")


# --------------------------------------------------------------------------------------------
# Figure 4 (GIF): repeated samples of 50 cans, sample means pile up around mu
# --------------------------------------------------------------------------------------------
def gif_sampling_distribution():
    rnd = random.Random(14)
    population = [round(rnd.gauss(9.97, 0.04), 4) for _ in range(2440)]
    mu = sum(population) / len(population)
    rows, cols = 40, 61
    bins = [9.940 + i * 0.004 for i in range(16)]  # 9.940 .. 10.000
    means = []
    frames, durs = [], []
    n_frames = 48
    for f in range(n_frames):
        idx = rnd.sample(range(2440), 50)
        m = sum(population[i] for i in idx) / 50
        means.append(m)
        fig = plt.figure(figsize=(8, 3.6), facecolor=WHITE)
        # left: population grid
        ax = fig.add_axes([0.02, 0.06, 0.40, 0.78])
        ax.set_xlim(-1, cols); ax.set_ylim(-1, rows); ax.axis("off"); ax.set_aspect("equal")
        xs = [i % cols for i in range(2440)]; ys = [i // cols for i in range(2440)]
        ax.scatter(xs, ys, s=2.2, c=LIGHT, linewidths=0)
        sel = set(idx)
        ax.scatter([i % cols for i in sel], [i // cols for i in sel], s=14, c=GOLD, linewidths=0)
        fig.text(0.03, 0.9, "Population: 2,440 cans", fontproperties=F("Montserrat", 700, 10.5), color=NAVY)
        fig.text(0.03, 0.845, f"sample {f + 1}: 50 cans chosen at random (gold)", fontproperties=F("OpenSans", 400, 8), color=MUTED)
        # right: histogram of sample means
        hx = fig.add_axes([0.52, 0.17, 0.45, 0.62])
        counts = [0] * (len(bins) - 1)
        for v in means:
            for b in range(len(bins) - 1):
                if bins[b] <= v < bins[b + 1]:
                    counts[b] += 1
        for b, c in enumerate(counts):
            for j in range(c):
                hx.add_patch(Rectangle((bins[b] + 0.0003, j + 0.1), 0.0034, 0.8, fc=BLUE, ec="none"))
        last_b = next((b for b in range(len(bins) - 1) if bins[b] <= m < bins[b + 1]), None)
        if last_b is not None:
            hx.add_patch(Rectangle((bins[last_b] + 0.0003, counts[last_b] - 1 + 0.1), 0.0034, 0.8, fc=GOLD, ec="none"))
        hx.axvline(mu, color=RED, lw=2)
        hx.text(mu + 0.0006, 15.2, f"μ = {mu:.4f} lb", fontproperties=F("OpenSans", 600, 8.5), color=RED)
        hx.set_xlim(bins[0], bins[-1]); hx.set_ylim(0, 16)
        for s in ("top", "right", "left"):
            hx.spines[s].set_visible(False)
        hx.spines["bottom"].set_color("#9AA5B1")
        hx.set_yticks([])
        hx.set_xticks([9.94, 9.95, 9.96, 9.97, 9.98, 9.99, 10.0])
        for lab in hx.get_xticklabels():
            lab.set_fontproperties(F("OpenSans", 400, 7.5)); lab.set_color(MUTED)
        hx.tick_params(axis="x", colors="#9AA5B1", length=3)
        hx.set_xlabel(r"sample mean weight $\bar{x}$ (lb)", fontproperties=F("OpenSans", 400, 8), color=MUTED)
        fig.text(0.52, 0.9, "Each sample gives a different mean", fontproperties=F("Montserrat", 700, 10.5), color=NAVY)
        fig.text(0.52, 0.845, rf"this sample: $\bar{{x}}$ = {m:.4f} lb   ·   samples so far: {f + 1}",
                 fontproperties=F("OpenSans", 400, 8), color=MUTED)
        frames.append(fig_to_pil(fig, dpi=110))
        durs.append(900 if f < 4 else (450 if f < 12 else 160))
    durs[-1] = 3500
    save_gif(frames, "fig4_sampling_distribution.gif", durs)
    return mu


# --------------------------------------------------------------------------------------------
# Figure 5 (GIF): bias and variability as darts on a target
# --------------------------------------------------------------------------------------------
def gif_bias_variability():
    rnd = random.Random(21)
    cases = [  # (title, centre offset, spread)
        ("Low bias, low variability", (0, 0), 0.10),
        ("Low bias, high variability", (0, 0), 0.32),
        ("High bias, low variability", (0.45, 0.35), 0.10),
        ("High bias, high variability", (0.45, 0.35), 0.32),
    ]
    shots = []
    for _, (ox, oy), sd in cases:
        pts = []
        while len(pts) < 12:
            x, y = rnd.gauss(ox, sd), rnd.gauss(oy, sd)
            if x * x + y * y < 0.98:
                pts.append((x, y))
        shots.append(pts)
    frames, durs = [], []
    for n in range(0, 13):
        fig = plt.figure(figsize=(8, 2.6), facecolor=WHITE)
        for k, (t, _, _) in enumerate(cases):
            ax = fig.add_axes([0.01 + k * 0.25, 0.1, 0.23, 0.68])
            ax.set_xlim(-1.1, 1.1); ax.set_ylim(-1.1, 1.1); ax.set_aspect("equal"); ax.axis("off")
            for r, c in ((1.0, "#EEF2F6"), (0.7, "#DCE5EE"), (0.4, "#C9D6E3"), (0.13, RED)):
                ax.add_patch(Circle((0, 0), r, fc=c, ec=WHITE, lw=1.2))
            for i, (x, y) in enumerate(shots[k][:n]):
                ax.add_patch(Circle((x, y), 0.065, fc=GOLD if i == n - 1 else NAVY, ec=WHITE, lw=0.8))
            fig.text(0.01 + k * 0.25 + 0.115, 0.86, t, ha="center",
                     fontproperties=F("Montserrat", 700, 8.3), color=NAVY)
        fig.text(0.5, 0.025, "bullseye = true parameter      dot = one sample statistic",
                 ha="center", fontproperties=F("OpenSans", 400, 7.5), color=MUTED)
        frames.append(fig_to_pil(fig, dpi=110))
        durs.append(450)
    durs[-1] = 3500
    save_gif(frames, "fig5_bias_variability.gif", durs)


# --------------------------------------------------------------------------------------------
# Figure 6: the "random rectangles" sheet (100 numbered rectangles)
# --------------------------------------------------------------------------------------------
def figure_rectangles():
    rnd = random.Random(2026)
    # Skewed area distribution: many small rectangles, a few large ones.
    shapes = ([(1, 1)] * 14 + [(1, 2)] * 14 + [(2, 1)] * 6 + [(1, 3)] * 8 + [(2, 2)] * 12 + [(1, 4)] * 6 +
              [(2, 3)] * 9 + [(3, 2)] * 3 + [(2, 4)] * 6 + [(3, 3)] * 6 + [(4, 4)] * 4 + [(3, 5)] * 3 +
              [(4, 5)] * 3 + [(2, 8)] * 2 + [(5, 6)] * 2 + [(6, 6)] * 2)
    assert len(shapes) == 100, len(shapes)
    rnd.shuffle(shapes)
    W, H = 40, 52
    occ = [[False] * W for _ in range(H)]
    placed = []

    def free(x, y, w, h):
        if x + w > W or y + h > H:
            return False
        for yy in range(max(0, y - 1), min(H, y + h + 1)):
            for xx in range(max(0, x - 1), min(W, x + w + 1)):
                if occ[yy][xx]:
                    return False
        return True

    order = sorted(range(100), key=lambda i: -shapes[i][0] * shapes[i][1])
    pos = {}
    for i in order:
        w, h = shapes[i]
        for _ in range(20000):
            x, y = rnd.randrange(0, W - w + 1), rnd.randrange(0, H - h + 1)
            if free(x, y, w, h):
                for yy in range(y, y + h):
                    for xx in range(x, x + w):
                        occ[yy][xx] = True
                pos[i] = (x, y)
                break
        else:
            raise RuntimeError("could not place rectangle")
    # number rectangles top-to-bottom, left-to-right so the sheet is easy to scan
    ids = sorted(range(100), key=lambda i: (pos[i][1] // 4, pos[i][0]))
    fig = plt.figure(figsize=(7.4, 9.4), facecolor=WHITE)
    ax = fig.add_axes([0.03, 0.03, 0.94, 0.94 * (7.4 / 9.4) * (H / W)])
    ax.set_xlim(-0.3, W + 0.3); ax.set_ylim(H + 0.3, -0.3); ax.set_aspect("equal"); ax.axis("off")
    for x in range(W + 1):
        ax.plot([x, x], [0, H], color="#F0F0F0", lw=0.4, zorder=0)
    for y in range(H + 1):
        ax.plot([0, W], [y, y], color="#F0F0F0", lw=0.4, zorder=0)
    areas = {}
    for num, i in enumerate(ids, start=1):
        w, h = shapes[i]
        x, y = pos[i]
        areas[num] = w * h
        ax.add_patch(Rectangle((x, y), w, h, fc="#EEF2F6", ec=NAVY, lw=0.9))
        for xx in range(x + 1, x + w):
            ax.plot([xx, xx], [y, y + h], color="#B9C6D3", lw=0.5)
        for yy in range(y + 1, y + h):
            ax.plot([x, x + w], [yy, yy], color="#B9C6D3", lw=0.5)
        ax.text(x + w / 2, y + h / 2, str(num), ha="center", va="center",
                fontproperties=F("OpenSans", 700, 6.2 if num >= 10 else 6.8), color=NAVY)
    save_png(fig, "fig6_random_rectangles.png")
    return areas


if __name__ == "__main__":
    figure_population_sample()
    figure_data_types()
    figure_sampling_methods()
    mu = gif_sampling_distribution()
    gif_bias_variability()
    areas = figure_rectangles()
    vals = list(areas.values())
    print("mu", round(mu, 4))
    print("rect mean area", sum(vals) / 100, "max", max(vals))
    with open(os.path.join(OUT, "rectangle_areas.txt"), "w") as fh:
        for k in sorted(areas):
            fh.write(f"{k}\t{areas[k]}\n")
    for f in sorted(os.listdir(OUT)):
        print(f, os.path.getsize(os.path.join(OUT, f)) // 1024, "KB")
