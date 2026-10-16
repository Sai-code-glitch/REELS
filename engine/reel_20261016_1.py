"""Etsy shops will pay for this in November (Holiday Etsy listing refresh, part 1)."""
from reel_common import *

ACC = (255, 140, 60)    # warm orange
GOLD = (255, 214, 92)
GREEN = (60, 205, 130)
RED = (255, 96, 110)
bg = Background(top=(40, 16, 8), bottom=(74, 30, 14), blobs=[(255, 120, 50), (255, 70, 90), (255, 190, 90)], seed=2891)

BEFORE = dict(title=["Handmade mug"], photos="2 photos", tags="", badge=None)
AFTER = dict(title=["Personalized Fishing Mug", "Gift for Dad, Christmas"], photos="10 photos", tags="", badge="Gift-ready")


def listing(w, h, data, glow=0.0):
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=40, fill=(255, 255, 255, 255))
    if glow > 0:
        d.rounded_rectangle([0, 0, w - 1, h - 1], radius=40, outline=(*GREEN, int(255 * glow)), width=10)
    # product photo area
    d.rounded_rectangle([40, 40, w - 40, 470], radius=28, fill=(250, 232, 214, 255))
    mug = emoji_img("☕", 230)
    im.alpha_composite(mug, (int(w / 2 - mug.width / 2), int(255 - mug.height / 2)))
    d.rounded_rectangle([60, 410, 250, 455], radius=22, fill=(24, 28, 40, 200))
    d.text((155, 432), data["photos"], font=font(F_SEMI, 28), fill=(255, 255, 255, 255), anchor="mm")
    if data["badge"]:
        d.rounded_rectangle([w - 300, 60, w - 60, 112], radius=26, fill=(*GREEN, 255))
        d.text((w - 180, 86), data["badge"], font=font(F_XB, 30), fill=(255, 255, 255, 255), anchor="mm")
    y = 530
    for line in data["title"]:
        d.text((50, y), line, font=font(F_XB, 40), fill=(*INK, 255), anchor="lm")
        y += 56
    d.text((50, y + 20), "$24.00", font=font(F_BLACK, 50), fill=(*INK, 255), anchor="lm")
    d.text((50, y + 85), "★★★★★  Star Seller", font=font(DEJAVU, 30), fill=(120, 120, 130, 255), anchor="lm")
    return im


def search_bar(sub, t, start, cy):
    k = p(t, start, 0.35)
    if k <= 0: return
    w, h = 860, 120
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=60, fill=(255, 255, 255, 255))
    q = "gift for dad who fishes"
    n = int(len(q) * clamp((t - start - 0.3) / 1.6))
    cursor = "|" if int(t * 3) % 2 == 0 else ""
    d.text((110, h / 2), q[:n] + cursor, font=font(F_SEMI, 46), fill=(*INK, 255), anchor="lm")
    e = emoji_img("🔍", 56); im.alpha_composite(e, (34, int(h / 2 - e.height / 2)))
    sub.alpha_composite(with_alpha(im, out_cubic(k)), (int(W / 2 - w / 2), int(cy - h / 2)))


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, 0.0, 0.3)
        place_emoji(sub, "🧶", W / 2, 500 + 12 * math.sin(t * 6), 200 * out_back(k), alpha=k, rot=6 * math.sin(t * 4))
        pop_words(sub, ["Etsy shops pay", "for this in", "November"], t, 0.0, 930, 100, (WHITE, GOLD), gap=0.07, highlight={"etsy", "november"})
        kk = p(t, 1.3, 0.4)
        pill(sub, W / 2, 1290, "A side gig you can start today", F_SEMI, 46, WHITE, INK, alpha=out_cubic(kk), scale=out_back(kk), icon="💡")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Holiday shoppers", "type exact searches"], t, s1 + 0.1, 330, 76, (WHITE, ACC), gap=0.07, highlight={"exact"})
        search_bar(sub, t, s1 + 0.6, 600)
        kv = p(t, s1 + 2.8, 0.45)
        if kv > 0:
            im = listing(560, 820, BEFORE).resize((420, 615))
            sub.alpha_composite(with_alpha(im, out_cubic(kv)), (int(W / 2 - 210), int(720 + 60 * (1 - out_cubic(kv)))))
        kx = p(t, s1 + 3.8, 0.35)
        if kx > 0:
            place_emoji(sub, "❌", W / 2 + 230, 790, 120 * out_back(kx), alpha=out_cubic(kx))
        kk = p(t, s1 + 4.4, 0.4)
        pill(sub, W / 2, 1470, "Vague titles get skipped", F_XB, 52, RED, WHITE, alpha=out_cubic(kk), scale=out_back(kk), icon="🙈")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["You refresh the listing"], t, s2 + 0.1, 290, 72, (WHITE, GOLD), gap=0.07, highlight={"refresh"})
        km = p(t, s2 + 1.4, 0.6)
        data = AFTER if km > 0.5 else BEFORE
        sx = 1 - abs(km - 0.5) * 2  # squash at the flip
        im = listing(560, 820, data, glow=out_cubic(p(t, s2 + 2.0, 0.4)))
        iw = max(4, int(500 * (1 - sx)))
        im = im.resize((iw, 732))
        sub.alpha_composite(im, (int(W / 2 - iw / 2), 400))
        tag = "AFTER" if km > 0.5 else "BEFORE"
        pill(sub, W / 2, 400, tag, F_BLACK, 40, GREEN if km > 0.5 else RED, WHITE, pad=(30, 12))
        checklist(sub, t, s2 + 3.0, ["Holiday words in title", "Use all 13 tags", "Gift-ready first photo"], 1230, 92, ACC, size=48, x0=190, every=0.8)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Sell it as a package"], t, s3 + 0.1, 300, 80, (WHITE, ACC), gap=0.07, highlight={"package"})
        kk = p(t, s3 + 0.6, 0.4)
        pill(sub, W / 2, 470, "5 listings  ×  $10", F_BLACK, 62, WHITE, INK, alpha=out_cubic(kk), scale=out_back(kk), icon="🧾")
        money_counter(sub, t, s3 + 1.3, 50, 780, GOLD, label="per shop")
        kk2 = p(t, s3 + 4.0, 0.4)
        pill(sub, W / 2, 1180, "3 shops = $150", F_XB, 56, ACC, INK, alpha=out_cubic(kk2), scale=out_back(kk2), icon="🛍️")
        draw_text(sub, "Example pricing. Results depend on your work.", F_MED, 36, W / 2, 1380, SOFT, alpha=out_cubic(p(t, s3 + 4.6, 0.5)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel1.mp4")
