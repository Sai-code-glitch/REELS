"""Sell packages, not hours: 3-tier pricing cards + hourly bar chart."""
from reel_common import *

ACC = (120, 170, 255)   # sky blue
GOLD = (255, 214, 92)
PURP = (170, 120, 255)
bg = Background(top=(8, 12, 40), bottom=(22, 20, 74), blobs=[(80, 120, 255), (170, 90, 255), (60, 200, 255)], seed=33)


def bar_chart(sub, cx, cy, t, start):
    w, h = 820, 560
    k = p(t, start, 0.45)
    if k <= 0: return
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=36, fill=(250, 250, 252, 255))
    d.text((w / 2, 55), "Same job, paid by the hour", font=font(F_XB, 40), fill=INK, anchor="mm")
    base = 440
    bars = [("Month 1", "10 hrs", 150, start + 0.6), ("Month 6", "4 hrs", 60, start + 1.6)]
    for i, (lab, hrs, amt, at) in enumerate(bars):
        kb = out_cubic(p(t, at, 0.9))
        x = 170 + i * 340
        bh = 230 * (amt / 150) * kb
        col = (90, 200, 140) if i == 0 else (255, 84, 96)
        if kb > 0:
            d.rounded_rectangle([x, base - bh, x + 160, base], radius=18, fill=(*col, 255))
            d.text((x + 80, base - bh - 40), f"${int(amt * kb)}", font=font(F_BLACK, 56), fill=INK, anchor="mm")
        d.text((x + 80, base + 40), lab, font=font(F_SEMI, 36), fill=INK, anchor="mm")
        d.text((x + 80, base + 85), hrs, font=font(F_MED, 32), fill=(130, 136, 150, 255), anchor="mm")
    card = with_alpha(card, out_cubic(k))
    sub.alpha_composite(card, (int(cx - w / 2), int(cy - h / 2 + 80 * (1 - out_cubic(k)))))


def tier(sub, cx, cy, t, at, name, price, lines, hi=False):
    k = p(t, at, 0.45)
    if k <= 0: return
    w, h = 270, 470
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    fill = (*GOLD, 255) if hi else (250, 250, 252, 255)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=30, fill=fill)
    if hi:
        d.rounded_rectangle([30, 18, w - 30, 64], radius=23, fill=(*INK, 255))
        d.text((w / 2, 41), "BEST VALUE", font=font(F_XB, 26), fill=(*GOLD, 255), anchor="mm")
    d.text((w / 2, 110), name, font=font(F_XB, 38), fill=INK, anchor="mm")
    d.text((w / 2, 190), price, font=font(F_BLACK, 76), fill=INK, anchor="mm")
    for i, ln in enumerate(lines):
        d.text((w / 2, 290 + i * 52), ln, font=font(F_SEMI, 30), fill=(60, 66, 84, 255), anchor="mm")
    s = out_back(k) * (1.06 if hi else 1.0)
    card = card.resize((int(w * s), int(h * s)))
    card = with_alpha(card, out_cubic(k))
    sub.alpha_composite(card, (int(cx - card.width / 2), int(cy - card.height / 2)))


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, 0.0, 0.3)
        pill(sub, W / 2, 470, "Nobody tells beginners this", F_XB, 50, ACC, INK, alpha=out_cubic(k), scale=out_back(k), icon="🤫")
        pop_words(sub, ["Sell packages,", "not hours"], t, 0.05, 860, 130, (WHITE, GOLD), gap=0.1, highlight={"packages"})
        k2 = p(t, 1.2, 0.4)
        place_emoji(sub, "📦", W / 2 - 170, 1230 + 15 * math.sin(t * 5), 150 * out_back(k2), alpha=k2, rot=-8)
        place_emoji(sub, "⏰", W / 2 + 170, 1230 - 15 * math.sin(t * 5), 150 * out_back(k2), alpha=k2, rot=8)
        draw_text(sub, ">", F_BLACK, 120, W / 2, 1230, GOLD, alpha=out_cubic(k2))
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Hourly pricing punishes", "you for getting faster"], t, s1 + 0.1, 350, 70, (WHITE, (255, 110, 120)), gap=0.07, highlight={"punishes", "faster"})
        bar_chart(sub, W / 2, 820, t, s1 + 0.9)
        kk = p(t, s1 + 3.8, 0.4)
        pill(sub, W / 2, 1230, "Better skills, less pay", F_XB, 50, (255, 236, 238), (190, 30, 50), alpha=out_cubic(kk), scale=out_back(kk), icon="📉")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Offer 3 clear", "packages"], t, s2 + 0.1, 340, 92, (WHITE, GOLD), gap=0.08, highlight={"3", "packages"})
        tier(sub, 245, 820, t, s2 + 0.8, "Basic", "$60", ["5 posts", "1 revision"])
        tier(sub, 540, 820, t, s2 + 1.5, "Standard", "$120", ["10 posts", "+ captions", "2 revisions"], hi=True)
        tier(sub, 835, 820, t, s2 + 2.2, "Premium", "$180", ["15 posts", "+ captions", "+ scheduling"])
        kk = p(t, s2 + 3.6, 0.4)
        pill(sub, W / 2, 1200, "Social media graphics, for example", F_SEMI, 42, WHITE, INK, alpha=out_cubic(kk), scale=out_back(kk), icon="🎨")
        checklist(sub, t, s2 + 4.5, ["Price by result, not time"], 1340, 110, ACC, size=50, x0=170)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Example math"], t, s3 + 0.1, 340, 100, (WHITE, GOLD), highlight={"math"})
        k1 = p(t, s3 + 0.6, 0.4)
        pill(sub, W / 2, 530, "$120 pack: 8 hrs at first", F_XB, 52, WHITE, INK, alpha=out_cubic(k1), scale=out_back(k1), pad=(40, 22), icon="🐢")
        k2 = p(t, s3 + 1.4, 0.4)
        pill(sub, W / 2, 660, "Same pack later: 4 hrs", F_XB, 52, ACC, INK, alpha=out_cubic(k2), scale=out_back(k2), pad=(40, 22), icon="⚡")
        money_counter(sub, t, s3 + 2.2, 30, 920, GOLD, label="per hour instead of $15")
        draw_text(sub, "Example pricing. Results depend on your work.", F_MED, 36, W / 2, 1320, SOFT, alpha=out_cubic(p(t, s3 + 3.0, 0.5)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel2.mp4")
