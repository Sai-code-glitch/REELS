"""Pitch this photo deal to 1 shop tonight -- find a shop with dark photos, DM a 3-shot holiday set + free sample."""
from reel_photo import *

ACC = (170, 240, 90)    # lime
GOLD = (255, 214, 92)
PINK = (255, 110, 190)
SKY = (110, 190, 255)
bg = Background(top=(30, 10, 48), bottom=(14, 8, 30), blobs=[(170, 70, 255), (255, 80, 170), (90, 160, 255)], seed=2963)


def shop_grid(sub, t, start, cy, hot_at):
    """Instagram-style shop profile grid of 6 dark product photos; one gets circled."""
    k = p(t, start, 0.4)
    if k <= 0: return
    w, h = 860, 720
    c = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(c)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=40, fill=(250, 251, 255, 255))
    d.ellipse([36, 30, 136, 130], fill=(255, 170, 90, 255))
    d.text((86, 80), "M", font=font(F_BLACK, 50), fill=(255, 255, 255, 255), anchor="mm")
    d.text((160, 62), "maya.candle.co", font=font(F_XB, 40), fill=(*INK, 255), anchor="lm")
    d.text((160, 106), "Small-batch candles", font=font(F_MED, 30), fill=(120, 126, 140, 255), anchor="lm")
    sz, gap = 252, 14
    x0 = (w - 3 * sz - 2 * gap) / 2
    for i in range(6):
        kk = p(t, start + 0.2 + i * 0.08, 0.3)
        if kk <= 0: continue
        x = x0 + (i % 3) * (sz + gap); y = 160 + (i // 3) * (sz + gap)
        candle(c, d, int(x), int(y), sz, "dark")
    kh = p(t, hot_at, 0.4)
    if kh > 0:
        x = x0 + (sz + gap); y = 160
        d.rounded_rectangle([x - 6, y - 6, x + sz + 6, y + sz + 6], radius=24, outline=(*PINK, int(255 * kh)), width=10)
    with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(cy - h / 2 + 50 * (1 - out_cubic(k)))))
    if kh > 0:
        place_emoji(sub, "🔍", W / 2 + 200, cy - 90 + 10 * math.sin(t * 6), 140 * out_back(kh), alpha=out_cubic(kh))


def package_card(sub, t, start, cy):
    k = p(t, start, 0.45)
    if k <= 0: return
    w, h = 860, 470
    c = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(c)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=40, fill=(250, 251, 255, 255))
    d.text((50, 70), "Holiday Photo Set", font=font(F_BLACK, 52), fill=(*INK, 255), anchor="lm")
    d.rounded_rectangle([w - 250, 40, w - 40, 100], radius=30, fill=(*ACC, 255))
    d.text((w - 145, 70), "EXAMPLE", font=font(F_XB, 30), fill=(*INK, 255), anchor="mm")
    rows = [("5 products x 3 shots", "15 photos"), ("Hero, close-up, gift scene", "✓"), ("Delivered in 3 days", "✓")]
    for i, (a, b) in enumerate(rows):
        kk = p(t, start + 0.4 + i * 0.35, 0.3)
        if kk <= 0: continue
        y = 160 + i * 80
        al = int(255 * out_cubic(kk))
        d.text((50, y), a, font=font(F_SEMI, 40), fill=(60, 66, 80, al), anchor="lm")
        d.text((w - 50, y), b, font=font(F_XB, 40), fill=(*INK, al), anchor="rm")
    d.line([50, 370, w - 50, 370], fill=(220, 224, 232, 255), width=3)
    kt = p(t, start + 1.6, 0.35)
    d.text((50, 420), "Price", font=font(F_XB, 44), fill=(*INK, int(255 * kt)), anchor="lm")
    d.text((w - 50, 420), "$120", font=font(F_BLACK, 56), fill=(*INK, int(255 * kt)), anchor="rm")
    with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(cy - h / 2 + 60 * (1 - out_cubic(k)))))


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, 0.0, 0.3)
        place_emoji(sub, "💬", W / 2 - 110, 460 - 14 * math.sin(t * 6), 170 * out_back(k), alpha=k)
        place_emoji(sub, "📸", W / 2 + 110, 460 + 14 * math.sin(t * 6), 170 * out_back(k), alpha=k)
        pop_words(sub, ["Pitch this photo deal", "to 1 shop tonight"], t, 0.0, 820, 96, (WHITE, ACC), gap=0.07, highlight={"pitch", "1", "shop", "tonight"})
        kp = p(t, 1.4, 0.4)
        pill(sub, W / 2, 1090, "Copy the DM in this video", F_XB, 50, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), pad=(40, 22), icon="📋")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Step 1: find a shop", "with dark photos"], t, s1 + 0.1, 320, 88, (WHITE, PINK), gap=0.08, highlight={"dark", "photos"})
        shop_grid(sub, t, s1 + 0.8, 840, s1 + 2.4)
        kp = p(t, s1 + 3.6, 0.4)
        pill(sub, W / 2, 1310, "Search: your city + candles", F_XB, 46, (245, 246, 250), INK, alpha=out_cubic(kp), scale=out_back(kp), icon="📍")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Step 2: send this"], t, s2 + 0.1, 270, 88, (WHITE, ACC), gap=0.08, highlight={"send", "this"})
        phone_chat(sub, t, s2 + 0.5, W / 2, 360, [
            ("me", "Hi Maya! Love your pine candle!", s2 + 1.0, None),
            ("me", "I shoot product photos with natural light. Holiday set: 3 clean shots per product.", s2 + 2.2, "typed"),
            ("me", "Want me to shoot 1 candle free so you can see first?", s2 + 4.6, "Delivered"),
        ], header="maya.candle.co", h=980)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Step 3: one clear offer"], t, s3 + 0.1, 290, 84, (WHITE, GOLD), gap=0.08, highlight={"clear", "offer"})
        package_card(sub, t, s3 + 0.6, 640)
        kx = p(t, s3 + 2.8, 0.4)
        pill(sub, W / 2, 960, "x 3 shops", F_XB, 56, PINK, INK, alpha=out_cubic(kx), scale=out_back(kx), icon="🏪")
        k3 = p(t, s3 + 3.2, 2.0)
        if k3 > 0:
            draw_text(sub, f"${int(round(360 * out_cubic(k3)))}", F_BLACK, 200, W / 2, 1150, GOLD, alpha=out_cubic(p(t, s3 + 3.2, 0.3)))
            draw_text(sub, "example total", F_XB, 52, W / 2, 1290, WHITE, alpha=out_cubic(p(t, s3 + 3.4, 0.3)))
        kq = p(t, s3 + 4.6, 0.5)
        draw_text(sub, "Example pricing. Results depend on your work.", F_MED, 36, W / 2, 1380, SOFT, alpha=out_cubic(kq))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel3.mp4")
