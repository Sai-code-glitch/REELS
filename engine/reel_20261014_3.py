"""Only give a discount if you get something back (client asks for a discount, part 3)."""
from reel_common import *

ACC = (255, 165, 60)    # amber
GOLD = (255, 220, 110)
RED = (255, 85, 95)
GREEN = (60, 205, 130)
bg = Background(top=(40, 18, 6), bottom=(70, 34, 12), blobs=[(255, 150, 50), (255, 80, 120), (255, 220, 90)], seed=2873)


def price_tag(sub, t, start, cx, cy, strike_at, new_at):
    w, h = 640, 300
    k = p(t, start, 0.45)
    if k <= 0: return
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=40, fill=(252, 250, 246, 255))
    d.ellipse([36, h / 2 - 22, 80, h / 2 + 22], fill=(70, 34, 12, 255))
    d.text((w / 2 + 30, 70), "Logo design (example)", font=font(F_SEMI, 36), fill=(110, 110, 120, 255), anchor="mm")
    ks = p(t, strike_at, 0.35)
    kn = p(t, new_at, 0.4)
    old_x = w / 2 + 30 - 150 * out_cubic(kn)
    d.text((old_x, 180), "$200", font=font(F_BLACK, 110 - 30 * out_cubic(kn)), fill=INK if kn == 0 else (150, 150, 160, 255), anchor="mm")
    if ks > 0:
        tw = 250 - 70 * out_cubic(kn)
        d.line([old_x - tw / 2, 185, old_x - tw / 2 + tw * out_cubic(ks), 175], fill=(*RED, 255), width=10)
    if kn > 0:
        d.text((w / 2 + 170, 180), "$180", font=font(F_BLACK, 110), fill=(*RED, int(255 * out_cubic(kn))), anchor="mm")
    rot = -4 + 2 * math.sin(t * 2)
    card = card.rotate(rot, resample=Image.BICUBIC, expand=True)
    s = out_back(k)
    card = card.resize((max(1, int(card.width * s)), max(1, int(card.height * s))), Image.LANCZOS)
    sub.alpha_composite(with_alpha(card, out_cubic(k)), (int(cx - card.width / 2), int(cy - card.height / 2)))


def trade_card(sub, t, start, cx, cy, rows, every=0.9):
    w, h = 880, 230 + 150 * len(rows)
    k = p(t, start, 0.45)
    if k <= 0: return
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=36, fill=(252, 250, 246, 255))
    d.text((w / 2, 80), "You give: 10% off", font=font(F_BLACK, 54), fill=(*RED, 255), anchor="mm")
    d.text((w / 2, 160), "They give ONE of these:", font=font(F_XB, 44), fill=INK, anchor="mm")
    for i, (ic, lab) in enumerate(rows):
        kk = p(t, start + 0.8 + i * every, 0.4)
        if kk <= 0: continue
        y = 250 + i * 150
        a = int(255 * out_cubic(kk))
        d.rounded_rectangle([40, y, w - 40, y + 120], radius=26, fill=(255, 240, 220, a))
        e = with_alpha(emoji_img(ic, 74), out_cubic(kk))
        card.alpha_composite(e, (int(115 - e.width / 2), y + 23))
        d.text((195, y + 60), lab, font=font(F_XB, 48), fill=(*INK, a), anchor="lm")
    sub.alpha_composite(with_alpha(card, out_cubic(k)), (int(cx - w / 2), int(cy - h / 2 + 70 * (1 - out_cubic(k)))))


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, 0.0, 0.3)
        place_emoji(sub, "🤝", W / 2, 520 + 12 * math.sin(t * 6), 200 * out_back(k), alpha=k, rot=5 * math.sin(t * 4))
        pop_words(sub, ["Only give a", "discount if you", "get this"], t, 0.0, 920, 112, (WHITE, ACC), gap=0.07, highlight={"discount", "this"})
        pill(sub, W / 2, 1300, "The fair-trade rule for freelancers", F_SEMI, 44, WHITE, INK, alpha=out_cubic(p(t, 1.2, 0.4)), scale=out_back(p(t, 1.2, 0.4)), icon="⚖️")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["A free discount", "for nothing back?"], t, s1 + 0.1, 360, 84, (WHITE, RED), gap=0.07, highlight={"nothing"})
        price_tag(sub, t, s1 + 0.6, W / 2, 800, s1 + 1.6, s1 + 2.2)
        tags = [("They'll ask again next time", 3.4, "🔁"), ("Your work looks worth less", 4.4, "📉")]
        for i, (lab, at, ic) in enumerate(tags):
            kk = p(t, s1 + at, 0.35)
            pill(sub, W / 2, 1120 + i * 130, lab, F_SEMI, 46, (255, 236, 238), (190, 30, 50), alpha=out_cubic(kk), scale=out_back(kk), icon=ic)
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Trade it, don't gift it"], t, s2 + 0.1, 290, 84, (WHITE, ACC), gap=0.07, highlight={"trade"})
        trade_card(sub, t, s2 + 0.4, W / 2, 860, [("💳", "100% paid upfront"), ("⭐", "A written review"), ("🙋", "A referral to a friend")], every=1.0)
        kk = p(t, s2 + 4.6, 0.4)
        pill(sub, W / 2, 1420, "No trade? Offer a smaller package", F_XB, 44, GOLD, INK, alpha=out_cubic(kk), scale=out_back(kk), icon="📦")
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Example: $200 job"], t, s3 + 0.1, 300, 84, (WHITE, GOLD), gap=0.07, highlight={"$200"})
        money_counter(sub, t, s3 + 0.5, 180, 620, GOLD, label="paid in full today (10% off)")
        rows = [("⏰", "No chasing late payments"), ("⭐", "+1 review for your profile")]
        for i, (ic, lab) in enumerate(rows):
            kk = p(t, s3 + 3.0 + i * 0.7, 0.4)
            pill(sub, W / 2, 1050 + i * 130, lab, F_XB, 46, WHITE, INK, alpha=out_cubic(kk), scale=out_back(kk), icon=ic)
        draw_text(sub, "Example pricing. Results depend on your work.", F_MED, 36, W / 2, 1380, SOFT, alpha=out_cubic(p(t, s3 + 4.4, 0.5)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel3.mp4")
