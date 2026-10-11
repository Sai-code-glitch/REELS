"""Black Friday promo graphics for small online shops (Canva-style mock)."""
from reel_common import *

ACC = (255, 138, 61)    # orange
GOLD = (255, 214, 92)
PINK = (255, 92, 160)
bg = Background(top=(22, 8, 34), bottom=(48, 10, 40), blobs=[(255, 120, 60), (170, 60, 255), (255, 60, 140)], seed=11)


def calendar(sub, cx, cy, s, t, start):
    w, h = 760 * s, 560 * s
    card = Image.new("RGBA", (int(w) + 4, int(h) + 4), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, w, h], radius=36 * s, fill=(250, 250, 252, 255))
    d.rounded_rectangle([0, 0, w, 110 * s], radius=36 * s, fill=(*PINK, 255))
    d.rectangle([0, 70 * s, w, 110 * s], fill=(*PINK, 255))
    d.text((w / 2, 55 * s), "NOVEMBER", font=font(F_BLACK, 56 * s), fill=(255, 255, 255, 255), anchor="mm")
    cw = (w - 60 * s) / 7
    for i, dn in enumerate("SMTWTFS"):
        d.text((30 * s + cw * (i + .5), 150 * s), dn, font=font(F_SEMI, 32 * s), fill=(140, 144, 160, 255), anchor="mm")
    # Nov 2026 starts on Sunday
    for day in range(1, 31):
        r, c = divmod(day - 1, 7)
        x = 30 * s + cw * (c + .5); y = 210 * s + r * 72 * s
        if day == 27:
            k = out_back(p(t, start, 0.5))
            if k > 0:
                rr = 34 * s * k
                d.ellipse([x - rr, y - rr, x + rr, y + rr], fill=(*ACC, 255))
            d.text((x, y), str(day), font=font(F_BLACK, 34 * s), fill=(255, 255, 255, 255) if k > .5 else (*INK, 255), anchor="mm")
        else:
            d.text((x, y), str(day), font=font(F_SEMI, 32 * s), fill=(*INK, 255), anchor="mm")
    sub.alpha_composite(card, (int(cx - w / 2), int(cy - h / 2)))


def editor(sub, cx, cy, t, start):
    """Canva-style editor: a promo graphic assembles itself."""
    w, h = 860, 760
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, w, h], radius=32, fill=(242, 243, 247, 255))
    d.rounded_rectangle([0, 0, w, 70], radius=32, fill=(124, 77, 255, 255))
    d.rectangle([0, 40, w, 70], fill=(124, 77, 255, 255))
    d.text((30, 35), "Design editor", font=font(F_SEMI, 32), fill=(255, 255, 255, 255), anchor="lm")
    d.rounded_rectangle([w - 190, 14, w - 24, 56], radius=21, fill=(255, 255, 255, 255))
    d.text((w - 107, 35), "Download", font=font(F_SEMI, 26), fill=(124, 77, 255, 255), anchor="mm")
    # side panel of template tiles
    cols = [(255, 214, 92), (255, 92, 160), (60, 200, 160), (90, 140, 255)]
    for i, c in enumerate(cols):
        d.rounded_rectangle([24, 96 + i * 160, 164, 236 + i * 160], radius=16, fill=(*c, 255))
    hi = int(clamp((t - start) / 0.4) * 1)
    if hi:
        d.rounded_rectangle([20, 92, 168, 240], radius=18, outline=(124, 77, 255, 255), width=6)
    # canvas
    x0, y0, x1, y1 = 196, 96, w - 24, h - 24
    k1 = p(t, start + 0.3, 0.5)
    base = tuple(int(lerp(255, b, out_cubic(k1))) for b in (20, 18, 30))
    d.rounded_rectangle([x0, y0, x1, y1], radius=14, fill=(*base, 255))
    cx_ = (x0 + x1) / 2
    k2 = p(t, start + 0.8, 0.4)
    if k2 > 0:
        d.text((cx_, y0 + 150), "BLACK", font=font(F_BLACK, int(110 * out_back(k2))), fill=(255, 255, 255, int(255 * out_cubic(k2))), anchor="mm")
        d.text((cx_, y0 + 270), "FRIDAY", font=font(F_BLACK, int(110 * out_back(k2))), fill=(*GOLD, int(255 * out_cubic(k2))), anchor="mm")
    k3 = p(t, start + 1.3, 0.4)
    if k3 > 0:
        r = 120 * out_back(k3)
        d.ellipse([cx_ - r, y0 + 470 - r, cx_ + r, y0 + 470 + r], fill=(*ACC, 255))
        d.text((cx_, y0 + 445), "30%", font=font(F_BLACK, int(80 * out_back(k3))), fill=(255, 255, 255, 255), anchor="mm")
        d.text((cx_, y0 + 515), "OFF", font=font(F_BLACK, int(44 * out_back(k3))), fill=(255, 255, 255, 255), anchor="mm")
    k4 = p(t, start + 1.8, 0.4)
    if k4 > 0:
        d.text((cx_, y1 - 40), "Your Shop · Logo here", font=font(F_SEMI, 30), fill=(200, 200, 215, int(255 * k4)), anchor="mm")
    sub.alpha_composite(card, (int(cx - w / 2), int(cy - h / 2)))


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, 0.0, 0.4)
        place_emoji(sub, "🛍️", W / 2, 600 - 30 * math.sin(t * 5) * (1 - p(t, 1.5, 1)), 210 * out_back(k), alpha=k, rot=8 * math.sin(t * 4))
        pop_words(sub, ["Black Friday is", "7 weeks away.", "Sell this now."], t, 0.0, 1040, 116, (WHITE, ACC), gap=0.08, highlight={"7", "weeks", "sell"})
        pill(sub, W / 2, 1440, "A gig shops need every year", F_SEMI, 44, WHITE, INK, alpha=out_cubic(p(t, 1.6, 0.4)), scale=out_back(p(t, 1.6, 0.4)))
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Small online shops", "need sale graphics"], t, s1 + 0.1, 360, 76, (WHITE, GOLD), gap=0.08, highlight={"sale", "graphics"})
        k = p(t, s1 + 0.6, 0.6)
        calendar(sub, W / 2, 800 + 120 * (1 - out_cubic(k)), 0.95 * (0.85 + 0.15 * out_back(k)), t, s1 + 1.4)
        tags = [("Busy owners, no designer", 2.4), ("Old posts, no promo plan", 3.2), ("Need it before Nov 27", 4.0)]
        for i, (lab, at) in enumerate(tags):
            kk = p(t, s1 + at, 0.35)
            pill(sub, W / 2, 1200 + i * 118, lab, F_SEMI, 44, (255, 236, 238), (200, 30, 60), alpha=out_cubic(kk), scale=out_back(kk), icon="⏰")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Make their promo pack", "with a free design app"], t, s2 + 0.1, 330, 68, (WHITE, ACC), gap=0.07, highlight={"promo", "free"})
        editor(sub, W / 2, 820, t, s2 + 0.8)
        checklist(sub, t, s2 + 3.6, ["Start from a template", "Add their logo + colors", "Post, story + banner sizes"], 1290, 118, ACC, size=50, x0=140, every=0.8)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Example math"], t, s3 + 0.1, 360, 100, (WHITE, GOLD), highlight={"math"})
        k1 = p(t, s3 + 0.6, 0.4)
        pill(sub, W / 2, 580, "10-graphic pack = $120", F_XB, 58, WHITE, INK, alpha=out_cubic(k1), scale=out_back(k1), pad=(44, 24), icon="🎨")
        k2 = p(t, s3 + 1.5, 0.4)
        draw_text(sub, "× 4 shops", F_BLACK, 84, W / 2, 750, ACC, alpha=out_cubic(k2), scale=out_back(k2))
        money_counter(sub, t, s3 + 2.3, 480, 1000, GOLD, label="before Black Friday")
        draw_text(sub, "Example pricing. Results depend on your work.", F_MED, 36, W / 2, 1420, SOFT, alpha=out_cubic(p(t, s3 + 3.0, 0.5)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel1.mp4")
