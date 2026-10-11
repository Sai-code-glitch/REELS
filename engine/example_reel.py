import math, sys
from PIL import Image, ImageDraw
from motion import *

ACC = (46, 230, 140)     # money green
GOLD = (255, 204, 64)
RED = (255, 84, 96)
WHITE = (255, 255, 255)
INK = (24, 28, 40)
SCENES = [(0, 3.6), (3.6, 10.6), (10.6, 18.6), (18.6, 26.0), (26.0, 30.0)]

bg = Background(top=(9, 11, 26), bottom=(6, 34, 26), blobs=[(30, 200, 120), (60, 90, 255), (255, 190, 60)])


def faded(layer, sub, t, start, end, slide=True):
    """Composite a scene layer with an enter fade and an exit fade+lift."""
    a_in = out_cubic(p(t, start, 0.25)) if start > 0 else 1.0
    k_out = p(t, end - 0.35, 0.35) if end < 30 else 0.0
    a = a_in * (1 - k_out)
    if a <= 0.01: return
    if a < 0.999:
        sub.putalpha(sub.getchannel("A").point(lambda v: int(v * a)))
    layer.alpha_composite(sub, (0, int(-90 * in_out(k_out))) if slide and k_out > 0 else (0, 0))


def listing_card(layer, cx, cy, s, alpha, fix):
    """Mock Google Maps listing. fix: 0 = neglected, 1 = optimized."""
    if alpha <= 0.01: return
    w, h = 860 * s, 430 * s
    x0, y0 = cx - w / 2, cy - h / 2
    card = Image.new("RGBA", (int(w) + 4, int(h) + 4), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, w, h], radius=34 * s, fill=(250, 250, 252, 255))
    # photo tile
    ph = 230 * s
    px, py = 34 * s, 34 * s
    tile = tuple(int(lerp(a, b, fix)) for a, b in zip((214, 217, 224), (210, 246, 228)))
    d.rounded_rectangle([px, py, px + ph, py + ph], radius=24 * s, fill=(*tile, 255))
    if fix < 0.5:
        d.text((px + ph / 2, py + ph / 2), "?", font=font(F_BLACK, 120 * s), fill=(150, 155, 168, int(255 * (1 - fix * 2))), anchor="mm")
    else:
        e = emoji_img("🔧", 120 * s * out_back(clamp((fix - 0.5) * 2)))
        card.alpha_composite(e, (int(px + ph / 2 - e.width / 2), int(py + ph / 2 - e.height / 2)))
    tx = px + ph + 34 * s
    d.text((tx, py + 10 * s), "Joe's Plumbing", font=font(F_XB, 54 * s), fill=(*INK, 255))
    # rating row
    reviews = int(round(lerp(12, 12, fix)))
    d.text((tx, py + 92 * s), "3.8", font=font(F_SEMI, 40 * s), fill=(80, 84, 96, 255))
    sx = tx + 80 * s
    for i in range(5):
        col = GOLD if i < 4 else (205, 208, 216)
        d.text((sx + i * 44 * s, py + 90 * s), "★", font=font("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 42 * s), fill=(*col, 255))
    d.text((sx + 5 * 44 * s + 10 * s, py + 92 * s), f"({reviews})", font=font(F_SEMI, 40 * s), fill=(110, 114, 126, 255))
    # category line: wrong -> right
    if fix < 0.5:
        d.text((tx, py + 160 * s), "Swimming pool", font=font(F_SEMI, 40 * s), fill=(*RED, int(255 * (1 - fix * 2))))
    else:
        d.text((tx, py + 160 * s), "Plumber · Open 24h", font=font(F_SEMI, 40 * s), fill=(20, 150, 90, int(255 * (fix - 0.5) * 2)))
    # bottom buttons
    by = py + ph + 40 * s
    for i, lab in enumerate(["Call", "Directions", "Website"]):
        bx = 34 * s + i * 270 * s
        d.rounded_rectangle([bx, by, bx + 250 * s, by + 76 * s], radius=38 * s, outline=(26, 115, 232, 255), width=max(2, int(4 * s)))
        d.text((bx + 125 * s, by + 38 * s), lab, font=font(F_SEMI, 34 * s), fill=(26, 115, 232, 255), anchor="mm")
    if alpha < 1:
        card.putalpha(card.getchannel("A").point(lambda v: int(v * alpha)))
    layer.alpha_composite(card, (int(x0), int(y0)))


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)

    # ---- A: hook ----
    s0, e0 = SCENES[0]
    if t < e0:
        sub = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        k = p(t, 0.0, 0.5)
        place_emoji(sub, "💰", W / 2, 640 - 30 * math.sin(t * 5) * (1 - p(t, 1.5, 1)), 220 * out_back(k), alpha=k, rot=8 * math.sin(t * 4))
        pop_words(sub, ["This $0 side", "hustle can pay", "you monthly"], t, 0.25, 1060, 118, (WHITE, ACC), highlight={"$0", "monthly"})
        pill(sub, W / 2, 1440, "Start with free tools", F_SEMI, 44, (255, 255, 255), INK, alpha=out_cubic(p(t, 1.9, 0.4)), scale=out_back(p(t, 1.9, 0.4)))
        faded(layer, sub, t, s0, e0)

    # ---- B: the problem ----
    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        pop_words(sub, ["Most local businesses", "look like this on Google"], t, s1 + 0.1, 400, 66, (WHITE, GOLD), gap=0.07, highlight={"google"})
        k = p(t, s1 + 0.6, 0.6)
        listing_card(sub, W / 2, 860 + 120 * (1 - out_cubic(k)), 1.0 * (0.85 + 0.15 * out_back(k)), out_cubic(k), 0)
        tags = [("Wrong category", 2.0), ("No photos", 2.7), ("Only 12 reviews", 3.4), ("No replies to reviews", 4.1)]
        for i, (lab, at) in enumerate(tags):
            kk = p(t, s1 + at, 0.35)
            pill(sub, W / 2, 1210 + i * 118, lab, F_SEMI, 44, (255, 236, 238), (200, 30, 50), alpha=out_cubic(kk), scale=out_back(kk), icon="❌")
        faded(layer, sub, t, s1, e1)

    # ---- C: the fix ----
    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        pop_words(sub, ["You fix it. Online.", "With free tools."], t, s2 + 0.1, 380, 80, (WHITE, ACC), gap=0.09, highlight={"free", "online."})
        fix = in_out(p(t, s2 + 1.2, 1.0))
        listing_card(sub, W / 2, 770, 0.86, 1.0, fix)
        # glow ring when fixed
        if fix > 0:
            d = ImageDraw.Draw(sub)
            r = 20 * out_cubic(fix)
        items = ["Fix the category", "Add real photos", "Reply to every review", "Set up a review system"]
        for i, lab in enumerate(items):
            kk = p(t, s2 + 2.2 + i * 0.75, 0.4)
            if kk > 0:
                y = 1110 + i * 128
                x = 170 + 60 * (1 - out_cubic(kk))
                place_emoji(sub, "✅", x, y, 74 * out_back(kk), alpha=out_cubic(kk))
                draw_text(sub, lab, F_XB, 56, x + 70, y, WHITE, alpha=out_cubic(kk), anchor="lm")
        faded(layer, sub, t, s2, e2)

    # ---- D: the math ----
    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        pop_words(sub, ["The math"], t, s3 + 0.1, 380, 110, (WHITE, GOLD))
        k1 = p(t, s3 + 0.6, 0.4)
        pill(sub, W / 2, 620, "1 client = $150 / month", F_XB, 58, (255, 255, 255), INK, alpha=out_cubic(k1), scale=out_back(k1), pad=(44, 24))
        k2 = p(t, s3 + 1.6, 0.4)
        draw_text(sub, "× 5 clients", F_BLACK, 84, W / 2, 790, ACC, alpha=out_cubic(k2), scale=out_back(k2))
        k3 = p(t, s3 + 2.4, 2.2)
        val = int(round(150 * 5 * out_cubic(k3) / 10) * 10)
        if k3 > 0:
            pulse = 1 + 0.06 * math.sin(max(0, t - (s3 + 4.6)) * 8) * (t > s3 + 4.6)
            draw_text(sub, f"${val:,}", F_BLACK, 250, W / 2, 1050, GOLD, alpha=out_cubic(p(t, s3 + 2.4, 0.3)), scale=pulse)
            draw_text(sub, "per month", F_XB, 64, W / 2, 1220, WHITE, alpha=out_cubic(p(t, s3 + 2.6, 0.3)))
        # money burst
        for i in range(9):
            st = s3 + 4.6 + i * 0.12
            kk = p(t, st, 1.6)
            if 0 < kk < 1:
                ang = -math.pi / 2 + (i - 4) * 0.28
                dist = 520 * out_cubic(kk)
                place_emoji(sub, "💸" if i % 2 else "💵", W / 2 + math.cos(ang) * dist, 1050 + math.sin(ang) * dist, 96, alpha=1 - kk, rot=(i - 4) * 12 * kk)
        draw_text(sub, "Example pricing. Results depend on your work.", F_MED, 36, W / 2, 1440, (200, 206, 220), alpha=out_cubic(p(t, s3 + 3.0, 0.5)))
        faded(layer, sub, t, s3, e3)

    # ---- E: CTA ----
    s4, e4 = SCENES[4]
    if t >= s4:
        sub = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        pop_words(sub, ["Follow for more ways", "to make money online"], t, s4 + 0.1, 760, 82, (WHITE, ACC), gap=0.08, highlight={"money", "online"})
        kb = p(t, s4 + 1.0, 0.45)
        bounce = 1 + 0.05 * math.sin(max(0, t - s4 - 1.5) * 7)
        pill(sub, W / 2, 1060, "Follow", F_BLACK, 66, ACC, INK, alpha=out_cubic(kb), scale=out_back(kb) * bounce, pad=(70, 30), icon="➕")
        kh = p(t, s4 + 1.6, 0.4)
        place_emoji(sub, "👆", W / 2 + 150, 1200 + 22 * math.sin(t * 8), 120, alpha=out_cubic(kh))
        pop_words(sub, ["Save this for later"], t, s4 + 2.0, 1400, 50, ((200, 206, 220), GOLD), gap=0.06, path=F_SEMI)
        faded(layer, sub, t, s4, e4)

    # watermark
    draw_text(layer, "LEARN & EARN", F_XB, 30, W / 2, H - 210, (255, 255, 255), alpha=0.55)


if __name__ == "__main__":
    out = sys.argv[1] if len(sys.argv) > 1 else "earn_01_google_profile_hustle.mp4"
    if len(sys.argv) > 2:  # preview frames
        for ts in [float(x) for x in sys.argv[2].split(",")]:
            fr = bg.frame(ts); lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); scene(lay, ts); fr.alpha_composite(lay)
            fr.convert("RGB").resize((360, 640)).save(f"prev_{ts:05.1f}.png")
    else:
        render(scene, out, bg=bg)
        print(out)
