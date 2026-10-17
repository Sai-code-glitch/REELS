"""Write a gift guide in 1 hour (Holiday gift guide writing, part 2)."""
from reel_common import *

ACC = (60, 214, 230)    # teal
GOLD = (255, 210, 90)
GREEN = (70, 210, 140)
PINK = (255, 120, 160)
bg = Background(top=(8, 16, 42), bottom=(6, 44, 58), blobs=[(40, 160, 230), (60, 220, 200), (255, 190, 80)], seed=2902)

THEMES = ["Gifts under $30", "For coffee lovers", "Stocking stuffers"]
STEPS = [("Pick 10 products", "15m"), ("1-line 'why' each", "20m"), ("Photos + links", "15m"), ("Title + short intro", "10m")]


def timer_ring(sub, cx, cy, r, frac, label):
    ring = Image.new("RGBA", (2 * r + 40, 2 * r + 40), (0, 0, 0, 0)); d = ImageDraw.Draw(ring)
    box = [20, 20, 20 + 2 * r, 20 + 2 * r]
    d.ellipse(box, outline=(255, 255, 255, 50), width=22)
    if frac > 0.002:
        d.arc(box, -90, -90 + 360 * frac, fill=(*ACC, 255), width=22)
    d.text((r + 20, r + 10), label, font=font(F_BLACK, int(r * 0.55)), fill=(255, 255, 255, 255), anchor="mm")
    d.text((r + 20, r + 20 + r * 0.42), "minutes left", font=font(F_SEMI, int(r * 0.17)), fill=(*SOFT, 255), anchor="mm")
    sub.alpha_composite(ring, (int(cx - r - 20), int(cy - r - 20)))


def doc_page(t, start, w=780, h=900):
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=36, fill=(255, 255, 255, 255))
    d.rounded_rectangle([40, 40, w - 40, 240], radius=26, fill=(255, 236, 214, 255))
    e = emoji_img("☕", 120); im.alpha_composite(e, (int(w / 2 - e.width / 2), int(140 - e.height / 2)))
    d.text((50, 300), "Gifts for Coffee Lovers", font=font(F_BLACK, 50), fill=(*INK, 255), anchor="lm")
    d.text((50, 358), "10 picks from our shop, all under $30", font=font(F_MED, 32), fill=(110, 114, 126, 255), anchor="lm")
    items = [("🫘", "Single-origin beans", "$16"), ("☕", "Speckled mug", "$22"), ("🍪", "Biscotti tin", "$9"), ("🧣", "Barista apron", "$28")]
    for i, (em, name, price) in enumerate(items):
        k = p(t, start + i * 0.5, 0.35)
        if k <= 0: continue
        y = 430 + i * 105
        a = int(255 * out_cubic(k))
        d.rounded_rectangle([40, y, w - 40, y + 88], radius=20, fill=(244, 246, 250, a))
        ee = with_alpha(emoji_img(em, 56).copy(), out_cubic(k)); im.alpha_composite(ee, (66, int(y + 44 - ee.height / 2)))
        d.text((140, y + 44), name, font=font(F_XB, 38), fill=(*INK, a), anchor="lm")
        d.text((w - 70, y + 44), price, font=font(F_BLACK, 38), fill=(20, 140, 150, a), anchor="rm")
    return im


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = clamp(p(t, 0.0, 0.3) + 0.4)
        place_emoji(sub, "⏱️", W / 2, 520 + 10 * math.sin(t * 6), 200 * out_back(k), alpha=k, rot=8 * math.sin(t * 5))
        pop_words(sub, ["Write a holiday", "gift guide in", "1 hour"], t, -0.25, 930, 108, (WHITE, ACC), gap=0.06, highlight={"1", "hour"})
        kk = p(t, 1.2, 0.4)
        pill(sub, W / 2, 1300, "Shops pay for these in Q4", F_SEMI, 46, WHITE, INK, alpha=out_cubic(kk), scale=out_back(kk), icon="🎁")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Step 0: pick", "ONE theme"], t, s1 + 0.1, 360, 88, (WHITE, GOLD), gap=0.07, highlight={"one"})
        chosen = p(t, s1 + 3.4, 0.4)
        for i, th in enumerate(THEMES):
            k = p(t, s1 + 1.0 + i * 0.5, 0.4)
            y = 700 + i * 170
            sel = (i == 1)
            bgc = GOLD if (sel and chosen > 0) else WHITE
            sc = out_back(k) * (1 + 0.08 * out_back(chosen) if sel else 1)
            al = out_cubic(k) * (1 - 0.6 * chosen if not sel else 1)
            pill(sub, W / 2, y, th, F_XB, 56, bgc, INK, alpha=al, scale=sc, pad=(50, 26), icon=["💲", "☕", "🧦"][i])
        kc = p(t, s1 + 3.6, 0.35)
        place_emoji(sub, "✅", W / 2 + 380, 870, 100 * out_back(kc), alpha=out_cubic(kc))
        kk = p(t, s1 + 4.3, 0.4)
        pill(sub, W / 2, 1360, "A theme = no blank page", F_XB, 48, ACC, INK, alpha=out_cubic(kk), scale=out_back(kk), icon="✨")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Then 4 timed steps"], t, s2 + 0.1, 280, 74, (WHITE, ACC), gap=0.07, highlight={"4"})
        frac = 1 - clamp((t - s2 - 0.8) / 6.6)
        mins = int(math.ceil(60 * frac))
        timer_ring(sub, W / 2, 560, 190, frac, f"{mins}")
        for i, (lab, tm) in enumerate(STEPS):
            k = p(t, s2 + 1.0 + i * 1.5, 0.4)
            if k <= 0: continue
            y = 870 + i * 130
            x = 140 + int(60 * (1 - out_cubic(k)))
            row = Image.new("RGBA", (800, 108), (0, 0, 0, 0)); rd = ImageDraw.Draw(row)
            rd.rounded_rectangle([0, 0, 799, 107], radius=30, fill=(255, 255, 255, 240))
            done = t > s2 + 1.0 + (i + 1) * 1.5
            e = emoji_img("✅" if done else "⬜", 58); row.alpha_composite(e, (28, int(54 - e.height / 2)))
            rd.text((110, 54), lab, font=font(F_XB, 42), fill=(*INK, 255), anchor="lm")
            rd.rounded_rectangle([650, 26, 772, 82], radius=28, fill=(*ACC, 255))
            rd.text((711, 54), tm, font=font(F_BLACK, 32), fill=(*INK, 255), anchor="mm")
            sub.alpha_composite(with_alpha(row, out_cubic(k)), (x, y))
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Done. Ready to send"], t, s3 + 0.1, 280, 76, (WHITE, GREEN), gap=0.07, highlight={"done."})
        kd = p(t, s3 + 0.5, 0.5)
        if kd > 0:
            pg = doc_page(t, s3 + 1.1).resize((624, 720))
            sub.alpha_composite(with_alpha(pg, out_cubic(kd)), (int(W / 2 - 312), int(380 + 60 * (1 - out_cubic(kd)))))
        ks = p(t, s3 + 3.4, 0.35)
        if ks > 0:
            pill(sub, W / 2 + 230, 470, "DONE", F_BLACK, 50, GREEN, WHITE, scale=1.6 - 0.6 * out_back(ks), alpha=out_cubic(ks), pad=(34, 14))
        kk = p(t, s3 + 4.0, 0.4)
        pill(sub, W / 2, 1230, "Example: $75 per guide", F_XB, 54, GOLD, INK, alpha=out_cubic(kk), scale=out_back(kk), icon="💰")
        draw_text(sub, "Example pricing. Results depend on your work.", F_MED, 36, W / 2, 1380, SOFT, alpha=out_cubic(p(t, s3 + 4.6, 0.5)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel2.mp4")
