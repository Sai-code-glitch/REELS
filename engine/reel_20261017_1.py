"""Small shops need this before Black Friday (Holiday gift guide writing, part 1)."""
from reel_common import *

ACC = (255, 92, 92)     # holiday red
GOLD = (255, 214, 92)
GREEN = (70, 210, 140)
bg = Background(top=(10, 34, 26), bottom=(44, 10, 18), blobs=[(40, 180, 110), (230, 60, 70), (255, 200, 90)], seed=2901)

PRODUCTS = [("🍫", "Chocolate box", "$12", "Easy host gift"),
            ("☕", "Hand-thrown mug", "$22", "For slow mornings"),
            ("🧦", "Wool socks", "$14", "Best stocking stuffer")]


def guide_card(t, start, w=860, h=860):
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=40, fill=(255, 255, 255, 255))
    d.rounded_rectangle([0, 0, w - 1, 170], radius=40, fill=(*ACC, 255))
    d.rectangle([0, 120, w - 1, 170], fill=(*ACC, 255))
    d.text((w / 2, 62), "HOLIDAY GIFT GUIDE", font=font(F_SEMI, 32), fill=(255, 255, 255, 230), anchor="mm")
    d.text((w / 2, 118), "Gifts Under $25", font=font(F_BLACK, 58), fill=(255, 255, 255, 255), anchor="mm")
    for i, (em, name, price, why) in enumerate(PRODUCTS):
        k = p(t, start + i * 0.9, 0.45)
        if k <= 0: continue
        y = 220 + i * 210
        dx = int(80 * (1 - out_cubic(k)))
        row = Image.new("RGBA", (w - 80, 180), (0, 0, 0, 0)); rd = ImageDraw.Draw(row)
        rd.rounded_rectangle([0, 0, w - 81, 179], radius=28, fill=(246, 241, 236, 255))
        rd.rounded_rectangle([20, 20, 160, 160], radius=22, fill=(255, 226, 214, 255))
        e = emoji_img(em, 96); row.alpha_composite(e, (int(90 - e.width / 2), int(90 - e.height / 2)))
        rd.text((190, 62), name, font=font(F_XB, 42), fill=(*INK, 255), anchor="lm")
        rd.text((190, 118), why, font=font(F_MED, 32), fill=(100, 104, 116, 255), anchor="lm")
        rd.text((w - 120, 62), price, font=font(F_BLACK, 42), fill=(*ACC, 255), anchor="rm")
        im.alpha_composite(with_alpha(row, out_cubic(k)), (40 + dx, y))
    return im


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = clamp(p(t, 0.0, 0.3) + 0.4)
        place_emoji(sub, "🎁", W / 2, 520 + 12 * math.sin(t * 6), 210 * out_back(k), alpha=k, rot=6 * math.sin(t * 4))
        pop_words(sub, ["Small shops need", "this before", "Black Friday"], t, -0.25, 930, 102, (WHITE, GOLD), gap=0.06, highlight={"black", "friday"})
        kk = p(t, 1.2, 0.4)
        pill(sub, W / 2, 1290, "A holiday side gig for writers", F_SEMI, 46, WHITE, INK, alpha=out_cubic(kk), scale=out_back(kk), icon="✍️")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Holiday shoppers", "all ask one thing"], t, s1 + 0.1, 330, 76, (WHITE, GOLD), gap=0.07, highlight={"one"})
        kb = p(t, s1 + 1.0, 0.45)
        if kb > 0:
            sc = out_back(kb)
            bw, bh = int(760 * sc), int(170 * sc)
            if bw > 10:
                b = Image.new("RGBA", (bw, bh + 40), (0, 0, 0, 0)); bd = ImageDraw.Draw(b)
                bd.rounded_rectangle([0, 0, bw - 1, bh - 1], radius=bh / 2, fill=(255, 255, 255, 255))
                bd.polygon([(bw * 0.2, bh - 2), (bw * 0.28, bh - 2), (bw * 0.18, bh + 36)], fill=(255, 255, 255, 255))
                bd.text((bw / 2, bh / 2), "What should I buy?", font=font(F_BLACK, int(62 * sc)), fill=(*INK, 255), anchor="mm")
                sub.alpha_composite(with_alpha(b, out_cubic(kb)), (int(W / 2 - bw / 2), int(560 - bh / 2)))
        place_emoji(sub, "🤔", W / 2 + 390, 450, 110 * out_back(p(t, s1 + 1.4, 0.4)), alpha=out_cubic(p(t, s1 + 1.4, 0.4)))
        subjects = ["🎁  Gifts under $25", "👨  Gifts for Dad", "⚡  Last-minute gifts"]
        draw_text(sub, "Emails that answer it:", F_XB, 48, W / 2, 790, SOFT, alpha=out_cubic(p(t, s1 + 2.2, 0.3)))
        for i, s in enumerate(subjects):
            k = p(t, s1 + 2.6 + i * 0.6, 0.4)
            if k <= 0: continue
            y = 900 + i * 135
            row = Image.new("RGBA", (820, 110), (0, 0, 0, 0)); rd = ImageDraw.Draw(row)
            rd.rounded_rectangle([0, 0, 819, 109], radius=26, fill=(255, 255, 255, 235))
            em, txt = s.split("  ")
            e = emoji_img(em, 60); row.alpha_composite(e, (30, int(55 - e.height / 2)))
            rd.text((115, 55), txt, font=font(F_XB, 44), fill=(*INK, 255), anchor="lm")
            rd.ellipse([760, 45, 780, 65], fill=(*ACC, 255))
            sub.alpha_composite(with_alpha(row, out_cubic(k)), (130 + int(60 * (1 - out_cubic(k))), y))
        kk = p(t, s1 + 4.8, 0.4)
        pill(sub, W / 2, 1400, "Busy owners rarely write them", F_XB, 46, ACC, WHITE, alpha=out_cubic(kk), scale=out_back(kk), icon="⏳")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["You write the gift guide"], t, s2 + 0.1, 290, 70, (WHITE, GOLD), gap=0.07, highlight={"gift", "guide"})
        kc = p(t, s2 + 0.6, 0.5)
        if kc > 0:
            card = guide_card(t, s2 + 1.2)
            sub.alpha_composite(with_alpha(card, out_cubic(kc)), (110, int(400 + 60 * (1 - out_cubic(kc)))))
        kk = p(t, s2 + 4.4, 0.4)
        pill(sub, W / 2, 1380, "Their products + 1 line on why", F_XB, 46, WHITE, INK, alpha=out_cubic(kk), scale=out_back(kk), icon="📝")
        kk2 = p(t, s2 + 5.0, 0.4)
        pill(sub, W / 2, 1500, "Email, blog or Instagram post", F_SEMI, 40, GREEN, INK, alpha=out_cubic(kk2), scale=out_back(kk2), icon="📬")
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Charge per guide"], t, s3 + 0.1, 300, 84, (WHITE, ACC), gap=0.07, highlight={"guide"})
        kk = p(t, s3 + 0.6, 0.4)
        pill(sub, W / 2, 470, "1 guide = 10 products", F_BLACK, 60, WHITE, INK, alpha=out_cubic(kk), scale=out_back(kk), icon="🧾")
        money_counter(sub, t, s3 + 1.3, 75, 780, GOLD, label="per guide")
        kk2 = p(t, s3 + 4.0, 0.4)
        pill(sub, W / 2, 1180, "3 shops = $225", F_XB, 56, ACC, WHITE, alpha=out_cubic(kk2), scale=out_back(kk2), icon="🛍️")
        draw_text(sub, "Example pricing. Results depend on your work.", F_MED, 36, W / 2, 1380, SOFT, alpha=out_cubic(p(t, s3 + 4.6, 0.5)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel1.mp4")
