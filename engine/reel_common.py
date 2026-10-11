"""Shared scene helpers for Learn & Earn reels (built on motion.py)."""
import math, sys
from PIL import Image, ImageDraw
from motion import *

WHITE = (255, 255, 255)
INK = (24, 28, 40)
SOFT = (200, 206, 220)
SCENES = [(0, 3.6), (3.6, 10.6), (10.6, 18.6), (18.6, 26.0), (26.0, 30.0)]
DEJAVU = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def new_layer():
    return Image.new("RGBA", (W, H), (0, 0, 0, 0))


def faded(layer, sub, t, start, end, slide=True):
    a_in = out_cubic(p(t, start, 0.25)) if start > 0 else 1.0
    k_out = p(t, end - 0.35, 0.35) if end < 30 else 0.0
    a = a_in * (1 - k_out)
    if a <= 0.01: return
    if a < 0.999:
        sub.putalpha(sub.getchannel("A").point(lambda v: int(v * a)))
    layer.alpha_composite(sub, (0, int(-90 * in_out(k_out))) if slide and k_out > 0 else (0, 0))


def with_alpha(im, alpha):
    if alpha < 0.999:
        im.putalpha(im.getchannel("A").point(lambda v: int(v * alpha)))
    return im


def checklist(sub, t, start, items, y0, step, acc, size=54, x0=150, every=0.7, icon="✅"):
    for i, lab in enumerate(items):
        kk = p(t, start + i * every, 0.4)
        if kk > 0:
            y = y0 + i * step
            x = x0 + 60 * (1 - out_cubic(kk))
            place_emoji(sub, icon, x, y, 70 * out_back(kk), alpha=out_cubic(kk))
            draw_text(sub, lab, F_XB, size, x + 66, y, WHITE, alpha=out_cubic(kk), anchor="lm")


def money_counter(sub, t, start, total, cy, color, label="per month", prefix="$"):
    k3 = p(t, start, 2.2)
    if k3 <= 0: return
    val = int(round(total * out_cubic(k3)))
    pulse = 1 + 0.06 * math.sin(max(0, t - (start + 2.2)) * 8) * (t > start + 2.2)
    draw_text(sub, f"{prefix}{val:,}", F_BLACK, 230, W / 2, cy, color, alpha=out_cubic(p(t, start, 0.3)), scale=pulse)
    draw_text(sub, label, F_XB, 60, W / 2, cy + 165, WHITE, alpha=out_cubic(p(t, start + 0.2, 0.3)))
    for i in range(9):
        kk = p(t, start + 2.2 + i * 0.12, 1.6)
        if 0 < kk < 1:
            ang = math.pi * (i % 2) + (i // 2 - 2) * 0.22
            dist = 480 * out_cubic(kk)
            place_emoji(sub, "💸" if i % 2 else "💵", W / 2 + math.cos(ang) * dist, cy + math.sin(ang) * dist, 90, alpha=1 - kk, rot=(i - 4) * 12 * kk)


def cta(layer, t, acc, gold):
    s4, e4 = SCENES[4]
    if t < s4: return
    sub = new_layer()
    pop_words(sub, ["Follow for more ways", "to make money online"], t, s4 + 0.1, 760, 82, (WHITE, acc), gap=0.08, highlight={"money", "online"})
    kb = p(t, s4 + 1.0, 0.45)
    bounce = 1 + 0.05 * math.sin(max(0, t - s4 - 1.5) * 7)
    pill(sub, W / 2, 1060, "Follow", F_BLACK, 66, acc, INK, alpha=out_cubic(kb), scale=out_back(kb) * bounce, pad=(70, 30), icon="➕")
    kh = p(t, s4 + 1.6, 0.4)
    place_emoji(sub, "👆", W / 2 + 150, 1200 + 22 * math.sin(t * 8), 120, alpha=out_cubic(kh))
    pop_words(sub, ["Save this for later"], t, s4 + 2.0, 1400, 50, (SOFT, gold), gap=0.06, path=F_SEMI)
    faded(layer, sub, t, s4, e4)


def watermark(layer):
    draw_text(layer, "LEARN & EARN", F_XB, 30, W / 2, H - 330, WHITE, alpha=0.5)


def main(scene, bg, default_out):
    out = sys.argv[1] if len(sys.argv) > 1 else default_out
    if len(sys.argv) > 2:
        frames = []
        for ts in [float(x) for x in sys.argv[2].split(",")]:
            fr = bg.frame(ts); lay = new_layer(); scene(lay, ts); fr.alpha_composite(lay)
            frames.append(fr.convert("RGB").resize((360, 640)))
        sheet = Image.new("RGB", (360 * len(frames), 640))
        for i, f in enumerate(frames): sheet.paste(f, (360 * i, 0))
        sheet.save(out)
    else:
        render(scene, out, bg=bg)
        print(out)
