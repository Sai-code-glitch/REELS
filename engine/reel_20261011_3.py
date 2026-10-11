"""Holiday product-photo refresh for small online shops (phone + window light)."""
from reel_common import *

ACC = (255, 120, 170)   # pink
GOLD = (255, 200, 80)
GREEN = (60, 210, 130)
bg = Background(top=(30, 14, 8), bottom=(12, 8, 24), blobs=[(255, 150, 60), (255, 90, 150), (255, 210, 120)], seed=31)


def product_photo(c, d, x, y, sz, fix):
    """Candle product shot: dark/cluttered (fix=0) -> bright/clean (fix=1)."""
    bgc = tuple(int(lerp(a, b, fix)) for a, b in zip((70, 62, 58), (250, 244, 236)))
    d.rounded_rectangle([x, y, x + sz, y + sz], radius=int(sz * 0.08), fill=(*bgc, 255))
    if fix < 0.6:  # clutter
        a = int(255 * (1 - fix / 0.6))
        d.rectangle([x + sz * .08, y + sz * .62, x + sz * .3, y + sz * .9], fill=(95, 80, 70, a))
        d.ellipse([x + sz * .7, y + sz * .12, x + sz * .9, y + sz * .32], fill=(110, 100, 92, a))
    # candle jar
    jar = tuple(int(lerp(a, b, fix)) for a, b in zip((120, 110, 100), (255, 255, 255)))
    d.rounded_rectangle([x + sz * .34, y + sz * .4, x + sz * .66, y + sz * .82], radius=int(sz * .05), fill=(*jar, 255), outline=(200, 190, 180, 255), width=3)
    lab = tuple(int(lerp(a, b, fix)) for a, b in zip((90, 80, 75), (200, 60, 70)))
    d.rectangle([x + sz * .34, y + sz * .55, x + sz * .66, y + sz * .67], fill=(*lab, 255))
    d.line([x + sz * .5, y + sz * .4, x + sz * .5, y + sz * .33], fill=(60, 50, 40, 255), width=4)
    if fix > 0.5:
        k = (fix - .5) * 2
        e = emoji_img("🔥", int(sz * .12 * k) + 4)
        c.alpha_composite(e, (int(x + sz * .5 - e.width / 2), int(y + sz * .33 - e.height)))
        for i, ch in enumerate(["🎄", "🎁"]):
            e = emoji_img(ch, int(sz * .2 * out_back(k)) + 4)
            c.alpha_composite(e, (int(x + sz * (.12 if i == 0 else .72)), int(y + sz * .62)))


def listing(sub, cx, cy, s, alpha, fix, sales):
    w, h = 860 * s, 420 * s
    c = Image.new("RGBA", (int(w) + 4, int(h) + 4), (0, 0, 0, 0))
    d = ImageDraw.Draw(c)
    d.rounded_rectangle([0, 0, w, h], radius=34 * s, fill=(252, 252, 252, 255))
    product_photo(c, d, 30 * s, 30 * s, 360 * s, fix)
    tx = 420 * s
    d.text((tx, 70 * s), "Pine Candle", font=font(F_XB, 52 * s), fill=(*INK, 255), anchor="lm")
    d.text((tx, 140 * s), "$24.00", font=font(F_SEMI, 42 * s), fill=(80, 84, 96, 255), anchor="lm")
    d.text((tx, 210 * s), f"{sales} sold", font=font(F_SEMI, 38 * s), fill=(120, 124, 136, 255), anchor="lm")
    bc = tuple(int(lerp(a, b, fix)) for a, b in zip((180, 184, 196), GREEN))
    d.rounded_rectangle([tx, 290 * s, w - 40 * s, 370 * s], radius=40 * s, fill=(*bc, 255))
    d.text(((tx + w - 40 * s) / 2, 330 * s), "Add to cart", font=font(F_XB, 36 * s), fill=(255, 255, 255, 255), anchor="mm")
    with_alpha(c, alpha)
    sub.alpha_composite(c, (int(cx - w / 2), int(cy - h / 2)))


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, 0.0, 0.4)
        place_emoji(sub, "📱", W / 2 - 110, 600 - 26 * math.sin(t * 5) * (1 - p(t, 1.5, 1)), 190 * out_back(k), alpha=k, rot=-8 * math.sin(t * 4))
        place_emoji(sub, "🪟", W / 2 + 110, 600 + 26 * math.sin(t * 5) * (1 - p(t, 1.5, 1)), 190 * out_back(k), alpha=k, rot=8 * math.sin(t * 4))
        pop_words(sub, ["Your phone +", "a window = a", "holiday side gig"], t, 0.0, 1040, 104, (WHITE, ACC), gap=0.08, highlight={"phone", "window", "holiday"})
        pill(sub, W / 2, 1430, "No camera needed", F_SEMI, 46, WHITE, INK, alpha=out_cubic(p(t, 1.6, 0.4)), scale=out_back(p(t, 1.6, 0.4)), icon="📸")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Lots of small shops", "list gifts like this"], t, s1 + 0.1, 360, 76, (WHITE, GOLD), gap=0.08, highlight={"gifts"})
        k = p(t, s1 + 0.6, 0.6)
        listing(sub, W / 2, 760 + 120 * (1 - out_cubic(k)), 0.85 + 0.15 * out_back(k), out_cubic(k), 0, 3)
        tags = [("Dark, dull photo", 2.0), ("Messy background", 2.8), ("Nothing says holiday", 3.6)]
        for i, (lab, at) in enumerate(tags):
            kk = p(t, s1 + at, 0.35)
            pill(sub, W / 2, 1110 + i * 118, lab, F_SEMI, 46, (255, 236, 238), (200, 30, 60), alpha=out_cubic(kk), scale=out_back(kk), icon="❌")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Reshoot their best", "sellers for the holidays"], t, s2 + 0.1, 330, 70, (WHITE, ACC), gap=0.08, highlight={"best", "holidays"})
        fix = in_out(p(t, s2 + 4.4, 1.2))
        listing(sub, W / 2, 680, 0.9, 1.0, fix, 3)
        checklist(sub, t, s2 + 1.0, ["Shoot next to a window", "White poster board backdrop", "Edit in a free photo app", "Add a few holiday props"], 1000, 112, ACC, size=48, x0=140, every=0.8)
        if fix > 0.95:
            kk = p(t, s2 + 5.7, 0.4)
            pill(sub, W / 2, 1470, "Same product. Better first look.", F_XB, 42, GREEN, INK, alpha=out_cubic(kk), scale=out_back(kk), icon="✨")
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Example math"], t, s3 + 0.1, 360, 100, (WHITE, GOLD), highlight={"math"})
        k1 = p(t, s3 + 0.6, 0.4)
        pill(sub, W / 2, 580, "10 product photos = $100", F_XB, 48, WHITE, INK, alpha=out_cubic(k1), scale=out_back(k1), pad=(44, 24), icon="📸")
        k2 = p(t, s3 + 1.5, 0.4)
        draw_text(sub, "× 3 shops a week", F_BLACK, 76, W / 2, 750, ACC, alpha=out_cubic(k2), scale=out_back(k2))
        money_counter(sub, t, s3 + 2.3, 300, 1000, GOLD, label="per week")
        draw_text(sub, "Example pricing. Results depend on your work.", F_MED, 36, W / 2, 1420, SOFT, alpha=out_cubic(p(t, s3 + 3.0, 0.5)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel3.mp4")
