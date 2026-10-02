"""Visuals for the improved FENMS 0021 Lab 1 (Fundamentals of Statistics)."""
import io
import os
import random

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
plt.rcParams["mathtext.fontset"] = "dejavusans"
from matplotlib import font_manager as fm
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch, Ellipse
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "fonts")
OUT = os.path.join(HERE, "img2")
os.makedirs(OUT, exist_ok=True)
for f in os.listdir(FONTS):
    if "-" in f:
        fm.fontManager.addfont(os.path.join(FONTS, f))


def F(family, weight=400, size=12):
    return fm.FontProperties(fname=os.path.join(FONTS, f"{family}-{weight}.ttf"), size=size)


NAVY, BLUE, GOLD, RED, TEAL = "#003E67", "#1F5F99", "#C39A3D", "#B3473A", "#14917A"
INK, MUTED, SURF, LIGHT, WHITE = "#202020", "#6B6B6B", "#F7F7F5", "#C9D6E3", "#FFFFFF"


def card(ax, x, y, w, h, fc, r=0.1, ec=None, lw=0, alpha=1):
    ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle=f"round,pad=0,rounding_size={r}",
                                fc=fc, ec=ec or fc, lw=lw, alpha=alpha))


def arrow(ax, p0, p1, color, lw=2.2):
    ax.add_patch(FancyArrowPatch(p0, p1, arrowstyle="-|>", mutation_scale=18, color=color, lw=lw))


def to_pil(fig, dpi=110):
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=dpi, facecolor=fig.get_facecolor())
    plt.close(fig)
    buf.seek(0)
    return Image.open(buf).convert("RGB")


# ------------------------------------------------------------------------------------------
# Figure 1 (GIF): population -> sample -> statistic -> inference, using Problem 1
# ------------------------------------------------------------------------------------------
def gif_population_to_inference():
    rnd = random.Random(7)
    cols, rows = 26, 12
    picked = rnd.sample(range(cols * rows), 50)
    stages = []  # (number of cans picked, show sample, show statistic, show inference)
    for k in range(0, 51, 5):
        stages.append((k, False, False, False))
    stages += [(50, True, False, False)] * 1 + [(50, True, True, False)] + [(50, True, True, True)]
    frames, durs = [], []
    for si, (k, show_s, show_stat, show_inf) in enumerate(stages):
        fig = plt.figure(figsize=(8, 3.9), facecolor=WHITE)
        ax = fig.add_axes([0, 0, 1, 1])
        ax.set_xlim(0, 8); ax.set_ylim(0, 3.9); ax.axis("off")
        # step labels along the top
        steps = ["1  Population", "2  Sample", "3  Statistic", "4  Inference"]
        active = 0 if not show_s else (1 if not show_stat else (2 if not show_inf else 3))
        for i, s in enumerate(steps):
            ax.text(0.25 + i * 1.95, 3.62, s, fontproperties=F("Montserrat", 700, 9),
                    color=NAVY if i == active else "#B5BFCA")
        # population
        card(ax, 0.2, 0.55, 4.1, 2.75, SURF)
        ax.text(0.45, 3.0, "POPULATION: all 2,440 cans  (N = 2,440)", fontproperties=F("Montserrat", 700, 9.5), color=NAVY)
        sel = set(picked[:k])
        for i in range(cols * rows):
            cx = 0.5 + (i % cols) * 0.138
            cy = 0.8 + (i // cols) * 0.175
            ax.add_patch(Circle((cx, cy), 0.045, fc=GOLD if i in sel else LIGHT, ec="none"))
        ax.text(0.45, 0.25, f"Choosing cans at random: {k} of 50" if not show_s else "50 cans chosen at random",
                fontproperties=F("OpenSans", 400, 8.5), color=MUTED)
        if show_s:
            arrow(ax, (4.4, 2.6), (5.2, 2.6), NAVY)
            card(ax, 5.3, 1.75, 2.5, 1.55, SURF)
            ax.text(5.5, 3.0, "SAMPLE: 50 cans  (n = 50)", fontproperties=F("Montserrat", 700, 9.5), color=NAVY)
            for i in range(50):
                ax.add_patch(Circle((5.6 + (i % 10) * 0.2, 2.0 + (i // 10) * 0.18), 0.055, fc=GOLD, ec="none"))
        if show_stat:
            card(ax, 5.3, 0.95, 2.5, 0.65, WHITE, ec=GOLD, lw=1.5)
            ax.text(5.45, 1.37, "Statistic: mean weight of the 50 cans", fontproperties=F("OpenSans", 600, 8), color=INK)
            ax.text(5.45, 1.1, r"$\bar{x}$ = 9.97 lb   (target: 10 lb)", fontproperties=F("OpenSans", 400, 8), color=INK)
        if show_inf:
            arrow(ax, (5.25, 0.75), (4.4, 0.75), RED)
            ax.text(5.3, 0.45, "Inference: the whole shipment is", fontproperties=F("OpenSans", 600, 8.2), color=RED)
            ax.text(5.3, 0.2, "probably under-filled, so return it.", fontproperties=F("OpenSans", 600, 8.2), color=RED)
        frames.append(to_pil(fig))
        durs.append(450 if not show_s else 1800)
    durs[-1] = 4500
    # Start on the finished diagram so a printout or PDF shows the full picture.
    frames = [frames[-1]] + frames[:-1]
    durs = [3500] + durs[:-1]
    pal = frames[0].quantize(colors=64, method=Image.Quantize.MEDIANCUT)
    q = [fr.quantize(palette=pal, dither=Image.Dither.NONE) for fr in frames]
    q[0].save(os.path.join(OUT, "fig1_population_to_inference_v2.gif"), save_all=True, append_images=q[1:],
              duration=durs, loop=0, optimize=True, disposal=1)


# ------------------------------------------------------------------------------------------
# Figure 2: types of data as in the original lab, with a "how to decide" question per branch
# ------------------------------------------------------------------------------------------
def figure_types_of_data():
    fig = plt.figure(figsize=(8, 4.3), facecolor=WHITE)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 8); ax.set_ylim(0, 4.3); ax.axis("off")

    def node(x, y, w, h, title, sub, fc):
        card(ax, x - w / 2, y - h / 2, w, h, fc, r=0.08)
        ax.text(x, y + (0.1 if sub else 0), title, ha="center", va="center", fontproperties=F("Montserrat", 700, 10.5), color=WHITE)
        if sub:
            ax.text(x, y - 0.17, sub, ha="center", va="center", fontproperties=F("OpenSans", 400, 8), color=WHITE)

    def link(x0, y0, x1, y1):
        ym = (y0 + y1) / 2
        ax.plot([x0, x0, x1, x1], [y0, ym, ym, y1], color="#9AA5B1", lw=1.4)

    node(4, 3.95, 1.7, 0.45, "DATA", None, INK)
    link(4, 3.72, 2.3, 3.3); link(4, 3.72, 6.2, 3.3)
    node(2.3, 3.0, 3.4, 0.62, "Numerical data", "also called quantitative  ·  numbers", TEAL)
    node(6.2, 3.0, 2.9, 0.62, "Categorical data", "also called qualitative  ·  labels or groups", BLUE)
    ax.text(2.3, 2.47, "Does adding or averaging the values make sense?  Yes",
            ha="center", fontproperties=F("OpenSans", 400, 7.5), color=MUTED)
    ax.text(6.2, 2.47, "Is each value a name of a group?  Yes",
            ha="center", fontproperties=F("OpenSans", 400, 7.5), color=MUTED)
    link(2.3, 2.38, 1.35, 2.0); link(2.3, 2.38, 3.25, 2.0)
    for x, t, s, q, ex in ((1.35, "Discrete", "counted · whole numbers", "Can you count it?",
                            ["number of children", "defects per hour"]),
                           (3.25, "Continuous", "measured · any value in a range", "Do you measure it?",
                            ["weight", "voltage"])):
        card(ax, x - 0.88, 0.2, 1.76, 1.8, SURF, r=0.08)
        ax.text(x, 1.72, t, ha="center", fontproperties=F("Montserrat", 700, 10), color=NAVY)
        ax.text(x, 1.48, s, ha="center", fontproperties=F("OpenSans", 400, 7.5), color=MUTED)
        ax.text(x, 1.18, q, ha="center", fontproperties=F("OpenSans", 600, 8), color=TEAL)
        for i, e in enumerate(ex):
            ax.text(x, 0.82 - i * 0.26, e, ha="center", fontproperties=F("OpenSans", 400, 8.2), color=INK)
    link(6.2, 2.38, 6.2, 2.0)
    card(ax, 4.95, 0.2, 2.5, 1.8, SURF, r=0.08)
    ax.text(6.2, 1.72, "Examples", ha="center", fontproperties=F("Montserrat", 700, 10), color=NAVY)
    for i, e in enumerate(["marital status: single, married, divorced",
                           "political party", "eye color: blue, green, brown"]):
        ax.text(6.2, 1.3 - i * 0.3, e, ha="center", fontproperties=F("OpenSans", 400, 8.2), color=INK)
    fig.savefig(os.path.join(OUT, "fig2_types_of_data.png"), dpi=200, facecolor=WHITE)
    plt.close(fig)


# ------------------------------------------------------------------------------------------
# Figure 3: who answered the Internet addiction survey (Problem 4)
# ------------------------------------------------------------------------------------------
def figure_who_answered():
    fig = plt.figure(figsize=(8, 3.6), facecolor=WHITE)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 8); ax.set_ylim(0, 3.6); ax.axis("off")
    ax.add_patch(Ellipse((2.6, 1.8), 4.8, 3.3, fc="#EEF2F6", ec=NAVY, lw=1.2))
    ax.add_patch(Ellipse((3.3, 1.55), 2.9, 2.1, fc="#DCE5EE", ec=BLUE, lw=1.2))
    ax.add_patch(Ellipse((3.75, 1.3), 1.3, 0.95, fc=GOLD, ec="none", alpha=0.9))
    ax.text(0.55, 2.05, "All Web users", fontproperties=F("Montserrat", 700, 10), color=NAVY)
    ax.text(0.55, 1.82, "the target population", fontproperties=F("OpenSans", 400, 8), color=MUTED)
    ax.text(2.35, 2.0, "Visitors of ABCNews.com", fontproperties=F("Montserrat", 700, 9), color=BLUE)
    ax.text(3.75, 1.37, "17,251 who", ha="center", fontproperties=F("Montserrat", 700, 8.5), color=WHITE)
    ax.text(3.75, 1.15, "chose to answer", ha="center", fontproperties=F("Montserrat", 700, 8.5), color=WHITE)
    tx = 5.4
    ax.text(tx, 2.85, "Who is missing from the sample?", fontproperties=F("Montserrat", 700, 10), color=NAVY)
    for i, line in enumerate(["Web users who never visit ABCNews.com",
                              "Visitors who did not want to answer",
                              "",
                              "People choose themselves, so the",
                              "sample may not look like all Web users,",
                              "even though 17,251 is a large number."]):
        ax.text(tx, 2.45 - i * 0.27, line, fontproperties=F("OpenSans", 600 if i < 2 else 400, 8.5),
                color=INK if i < 2 else MUTED)
    fig.savefig(os.path.join(OUT, "fig3_who_answered.png"), dpi=200, facecolor=WHITE)
    plt.close(fig)


if __name__ == "__main__":
    gif_population_to_inference()
    figure_types_of_data()
    figure_who_answered()
    for f in sorted(os.listdir(OUT)):
        print(f, os.path.getsize(os.path.join(OUT, f)) // 1024, "KB")
