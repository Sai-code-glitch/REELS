"""Stop charging $5: find your price floor (calculator mock)."""
from reel_common import *

ACC = (60, 230, 160)    # mint
GOLD = (255, 214, 92)
RED = (255, 84, 96)
bg = Background(top=(4, 26, 26), bottom=(6, 44, 40), blobs=[(40, 200, 150), (30, 120, 200), (120, 220, 90)], seed=21)


def gig_card(sub, cx, cy, t, start):
    w, h = 800, 330
    k = out_back(p(t, start, 0.5))
    if k <= 0: return
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=32, fill=(250, 250, 252, 255))
    d.rounded_rectangle([30, 30, 230, 230], radius=24, fill=(210, 216, 228, 255))
    d.text((130, 130), "LOGO", font=font(F_BLACK, 44), fill=(150, 156, 172, 255), anchor="mm")
    d.text((260, 60), "I will design your", font=font(F_SEMI, 40), fill=INK, anchor="lm")
    d.text((260, 110), "logo in 24 hours", font=font(F_SEMI, 40), fill=INK, anchor="lm")
    d.text((260, 170), "★★★★★  (0)", font=font(DEJAVU, 34), fill=(240, 170, 40, 255), anchor="lm")
    d.text((w - 40, 270), "$5", font=font(F_BLACK, 80), fill=INK, anchor="rm")
    d.text((40, 280), "Starting at", font=font(F_MED, 32), fill=(130, 136, 150, 255), anchor="lm")
    ks = p(t, start + 0.9, 0.35)
    if ks > 0:
        x1 = w - 160 + 130 * ks
        d.line([w - 160, 270, x1, 270], fill=(*RED, 255), width=12)
    card = card.resize((int(w * k), int(h * k)))
    sub.alpha_composite(card, (int(cx - card.width / 2), int(cy - card.height / 2)))


def calculator(sub, cx, cy, t, start):
    w, h = 820, 560
    k = p(t, start, 0.5)
    if k <= 0: return
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=40, fill=(18, 24, 34, 245), outline=(*ACC, 255), width=4)
    d.text((w / 2, 60), "PRICE FLOOR CALCULATOR", font=font(F_XB, 36), fill=(*ACC, 255), anchor="mm")
    rows = [("Monthly goal", "$600", 0.6), ("Hours you can work", "÷ 40", 1.4)]
    for i, (lab, val, at) in enumerate(rows):
        kk = out_cubic(p(t, start + at, 0.4))
        if kk > 0:
            y = 150 + i * 100
            d.text((50 + 40 * (1 - kk), y), lab, font=font(F_SEMI, 44), fill=(255, 255, 255, int(255 * kk)), anchor="lm")
            d.text((w - 50, y), val, font=font(F_BLACK, 56), fill=(255, 255, 255, int(255 * kk)), anchor="rm")
    kl = p(t, start + 2.2, 0.4)
    if kl > 0:
        d.line([50, 320, 50 + (w - 100) * out_cubic(kl), 320], fill=(255, 255, 255, 120), width=4)
    kf = p(t, start + 2.5, 1.2)
    if kf > 0:
        val = int(round(15 * out_cubic(kf)))
        d.text((50, 430), "Your floor", font=font(F_XB, 52), fill=(*GOLD, 255), anchor="lm")
        d.text((w - 50, 430), f"${val}/hr", font=font(F_BLACK, 96), fill=(*GOLD, 255), anchor="rm")
    card = with_alpha(card, out_cubic(k))
    sub.alpha_composite(card, (int(cx - w / 2), int(cy - h / 2 + 80 * (1 - out_cubic(k)))))


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, 0.0, 0.35)
        place_emoji(sub, "🛑", W / 2, 560 - 20 * math.sin(t * 6) * (1 - p(t, 1.5, 1)), 200 * out_back(k), alpha=k)
        pop_words(sub, ["Stop charging", "$5 for your", "first gig"], t, 0.0, 1000, 124, (WHITE, ACC), gap=0.08, highlight={"$5", "stop"})
        pill(sub, W / 2, 1400, "Do this 10-second math instead", F_SEMI, 44, WHITE, INK, alpha=out_cubic(p(t, 1.5, 0.4)), scale=out_back(p(t, 1.5, 0.4)))
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Cheap gigs lead", "to burnout"], t, s1 + 0.1, 360, 84, (WHITE, RED), gap=0.08, highlight={"burnout"})
        gig_card(sub, W / 2, 720, t, s1 + 0.7)
        tags = [("20 orders just to make $100", 2.6, "😩"), ("Clients expect endless edits", 3.4, "🔁"), ("No time left to improve", 4.2, "⏳")]
        for i, (lab, at, ic) in enumerate(tags):
            kk = p(t, s1 + at, 0.35)
            pill(sub, W / 2, 1050 + i * 118, lab, F_SEMI, 44, (255, 236, 238), (190, 30, 50), alpha=out_cubic(kk), scale=out_back(kk), icon=ic)
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Find your", "price floor"], t, s2 + 0.1, 340, 92, (WHITE, ACC), gap=0.08, highlight={"floor"})
        calculator(sub, W / 2, 780, t, s2 + 0.6)
        checklist(sub, t, s2 + 4.8, ["Add tool + platform fees", "Round up, never down"], 1180, 110, ACC, size=50, x0=150, every=0.8)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Example math"], t, s3 + 0.1, 340, 100, (WHITE, GOLD), highlight={"math"})
        k1 = p(t, s3 + 0.6, 0.4)
        pill(sub, W / 2, 540, "Logo job ≈ 4 hours", F_XB, 56, WHITE, INK, alpha=out_cubic(k1), scale=out_back(k1), pad=(44, 24), icon="🎨")
        k2 = p(t, s3 + 1.4, 0.4)
        draw_text(sub, "× $15 floor", F_BLACK, 84, W / 2, 700, ACC, alpha=out_cubic(k2), scale=out_back(k2))
        money_counter(sub, t, s3 + 2.1, 60, 930, GOLD, label="minimum quote, not $5")
        draw_text(sub, "Example pricing. Results depend on your work.", F_MED, 36, W / 2, 1320, SOFT, alpha=out_cubic(p(t, s3 + 3.0, 0.5)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel1.mp4")
