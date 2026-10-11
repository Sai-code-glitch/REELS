"""Holiday inbox helper for online sellers (phone notifications + saved replies)."""
from reel_common import *

ACC = (64, 224, 208)    # teal
GOLD = (255, 210, 90)
BLUE = (90, 150, 255)
bg = Background(top=(6, 16, 34), bottom=(4, 36, 48), blobs=[(40, 200, 200), (60, 90, 255), (120, 255, 200)], seed=21)

MSGS = [("Where's my order?? 📦", "2m"), ("Do you gift wrap?", "4m"), ("Can I swap to size M?", "6m"),
        ("Ships by Dec 20?", "9m"), ("Promo code not working", "12m")]


def phone(sub, cx, cy, t, start, n_show):
    w, h = 620, 860
    ph = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(ph)
    d.rounded_rectangle([0, 0, w, h], radius=70, fill=(18, 20, 28, 255))
    d.rounded_rectangle([18, 18, w - 18, h - 18], radius=56, fill=(234, 238, 246, 255))
    d.rounded_rectangle([w / 2 - 80, 34, w / 2 + 80, 70], radius=18, fill=(18, 20, 28, 255))
    d.text((60, 110), "Shop inbox", font=font(F_XB, 44), fill=(*INK, 255), anchor="lm")
    unread = 0
    for i, (msg, ago) in enumerate(MSGS):
        k = p(t, start + i * 0.45, 0.35)
        if k <= 0: continue
        unread = 12 + i * 9
        y = 170 + i * 128 - 30 * (1 - out_cubic(k))
        a = int(255 * out_cubic(k))
        d.rounded_rectangle([40, y, w - 40, y + 110], radius=26, fill=(255, 255, 255, a))
        d.ellipse([60, y + 25, 120, y + 85], fill=(*BLUE, a))
        d.text((90, y + 55), "@", font=font(F_XB, 30), fill=(255, 255, 255, a), anchor="mm")
        d.text((140, y + 40), "Customer", font=font(F_SEMI, 26), fill=(120, 126, 140, a), anchor="lm")
        d.text((w - 64, y + 40), ago, font=font(F_SEMI, 24), fill=(150, 156, 170, a), anchor="rm")
        d.text((140, y + 78), msg.replace(" 📦", ""), font=font(F_SEMI, 32), fill=(*INK, a), anchor="lm")
    if unread:
        bx = w - 70
        d.ellipse([bx - 44, 110 - 44, bx + 44, 110 + 44], fill=(255, 70, 90, 255))
        d.text((bx, 110), str(unread), font=font(F_BLACK, 40), fill=(255, 255, 255, 255), anchor="mm")
    sub.alpha_composite(ph, (int(cx - w / 2), int(cy - h / 2)))


def reply_card(sub, cx, cy, t, start):
    w, h = 860, 400
    c = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(c)
    d.rounded_rectangle([0, 0, w, h], radius=34, fill=(250, 251, 253, 255))
    d.text((40, 52), "Saved reply: Shipping", font=font(F_XB, 40), fill=(*INK, 255), anchor="lm")
    d.rounded_rectangle([w - 170, 26, w - 36, 78], radius=26, fill=(*ACC, 255))
    d.text((w - 103, 52), "#1 of 10", font=font(F_SEMI, 26), fill=(*INK, 255), anchor="mm")
    full = ["Hi! Thanks for your order 🎁", "It ships in 1-2 days and you'll", "get a tracking link by email."]
    n = int(clamp((t - start) / 2.2) * sum(len(s) for s in full))
    y = 130
    for line in full:
        line = line.replace(" 🎁", "")
        part = line[:max(0, n)]; n -= len(line)
        d.text((40, y), part, font=font(F_MED, 38), fill=(60, 66, 80, 255), anchor="lm")
        y += 62
    k = p(t, start + 2.4, 0.4)
    if k > 0:
        d.rounded_rectangle([40, h - 90, 260, h - 30], radius=30, fill=(*BLUE, int(255 * k)))
        d.text((150, h - 60), "Send ➤".replace(" ➤", ""), font=font(F_XB, 32), fill=(255, 255, 255, int(255 * k)), anchor="mm")
        place_emoji(c, "⚡", 300, h - 60, 50 * out_back(k), alpha=k)
    sub.alpha_composite(c, (int(cx - w / 2), int(cy - h / 2)))


def bars(sub, t, start, cx, base_y):
    vals = [("Wk 1", 210), ("Wk 2", 210), ("Wk 3", 210), ("Wk 4", 210)]
    bw, gap, maxh = 140, 50, 300
    x0 = cx - (len(vals) * bw + (len(vals) - 1) * gap) / 2
    d = ImageDraw.Draw(sub)
    for i, (lab, v) in enumerate(vals):
        k = out_cubic(p(t, start + i * 0.35, 0.6))
        if k <= 0: continue
        hh = maxh * (i + 1) / 4 * k
        x = x0 + i * (bw + gap)
        d.rounded_rectangle([x, base_y - hh, x + bw, base_y], radius=18, fill=(*ACC, 255))
        d.text((x + bw / 2, base_y + 40), lab, font=font(F_SEMI, 36), fill=(*SOFT, 255), anchor="mm")
        d.text((x + bw / 2, base_y - hh - 34), f"${v * (i + 1)}", font=font(F_XB, 36), fill=(255, 255, 255, int(255 * k)), anchor="mm")


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, 0.0, 0.4)
        place_emoji(sub, "📥", W / 2, 600 - 30 * math.sin(t * 5) * (1 - p(t, 1.5, 1)), 210 * out_back(k), alpha=k, rot=8 * math.sin(t * 4))
        pop_words(sub, ["Online sellers", "drown in messages", "every November"], t, 0.0, 1040, 96, (WHITE, ACC), gap=0.08, highlight={"drown", "november"})
        pill(sub, W / 2, 1430, "You can be the fix", F_SEMI, 46, WHITE, INK, alpha=out_cubic(p(t, 1.6, 0.4)), scale=out_back(p(t, 1.6, 0.4)), icon="🙋")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Holiday orders =", "a flooded inbox"], t, s1 + 0.1, 330, 80, (WHITE, GOLD), gap=0.08, highlight={"flooded", "inbox"})
        k = p(t, s1 + 0.5, 0.5)
        phone(sub, W / 2, 900 + 140 * (1 - out_cubic(k)), t, s1 + 1.0, 5)
        kk = p(t, s1 + 4.0, 0.4)
        pill(sub, W / 2, 1440, "Slow replies = lost sales", F_XB, 48, (255, 236, 238), (200, 30, 60), alpha=out_cubic(kk), scale=out_back(kk), icon="😬")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Offer holiday", "inbox help"], t, s2 + 0.1, 330, 92, (WHITE, ACC), gap=0.09, highlight={"inbox", "help"})
        k = p(t, s2 + 0.6, 0.5)
        reply_card(sub, W / 2, 720 + 100 * (1 - out_cubic(k)), t, s2 + 0.9)
        checklist(sub, t, s2 + 3.6, ["Write 10 saved replies", "Answer within a few hours", "Send refunds to the owner"], 1060, 118, ACC, size=50, x0=140, every=0.8)
        kp = p(t, s2 + 6.0, 0.4)
        pill(sub, W / 2, 1450, "Pitch shops you already buy from", F_SEMI, 40, WHITE, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="🎯")
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Example math"], t, s3 + 0.1, 330, 100, (WHITE, GOLD), highlight={"math"})
        k1 = p(t, s3 + 0.5, 0.4)
        pill(sub, W / 2, 520, "2 hrs/day × $15/hr", F_XB, 58, WHITE, INK, alpha=out_cubic(k1), scale=out_back(k1), pad=(44, 24), icon="⏱️")
        k2 = p(t, s3 + 1.1, 0.4)
        draw_text(sub, "× 7 days a week", F_BLACK, 70, W / 2, 660, ACC, alpha=out_cubic(k2), scale=out_back(k2))
        bars(sub, t, s3 + 1.6, W / 2, 1120)
        k4 = p(t, s3 + 3.4, 0.4)
        draw_text(sub, "≈ $840 for one busy month", F_BLACK, 64, W / 2, 1290, GOLD, alpha=out_cubic(k4), scale=out_back(k4))
        draw_text(sub, "Example pricing. Results depend on your work.", F_MED, 36, W / 2, 1420, SOFT, alpha=out_cubic(p(t, s3 + 3.8, 0.5)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel2.mp4")
