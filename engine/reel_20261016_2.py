"""Spot an Etsy shop that needs help in 10 seconds (Holiday Etsy listing refresh, part 2)."""
from reel_common import *

ACC = (40, 210, 190)    # teal
GOLD = (255, 214, 92)
GREEN = (60, 205, 130)
RED = (255, 96, 110)
bg = Background(top=(6, 30, 36), bottom=(10, 52, 60), blobs=[(40, 200, 190), (60, 120, 255), (120, 230, 160)], seed=2892)

FLAGS = [
    ("Title is 2-3 vague words", (40, 520, 600, 600)),
    ("Only 1-2 photos", (40, 40, 600, 470)),
    ("No gift or holiday wording", (40, 610, 600, 700)),
]


def shop_listing(w=640, h=860):
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=40, fill=(255, 255, 255, 255))
    d.rounded_rectangle([40, 40, w - 40, 470], radius=28, fill=(226, 238, 246, 255))
    e = emoji_img("🕯️", 230); im.alpha_composite(e, (int(w / 2 - e.width / 2), int(255 - e.height / 2)))
    d.rounded_rectangle([60, 410, 240, 455], radius=22, fill=(24, 28, 40, 200))
    d.text((150, 432), "1 photo", font=font(F_SEMI, 28), fill=(255, 255, 255, 255), anchor="mm")
    d.text((50, 560), "Soy candle", font=font(F_XB, 52), fill=(*INK, 255), anchor="lm")
    d.text((50, 650), "Candle. 8oz. Soy wax.", font=font(F_MED, 34), fill=(110, 110, 120, 255), anchor="lm")
    d.text((50, 740), "$18.00", font=font(F_BLACK, 50), fill=(*INK, 255), anchor="lm")
    d.text((50, 805), "★★★★★  (212 reviews)", font=font(DEJAVU, 30), fill=(120, 120, 130, 255), anchor="lm")
    return im


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, 0.0, 0.3)
        place_emoji(sub, "🔎", W / 2, 500 + 12 * math.sin(t * 6), 200 * out_back(k), alpha=k, rot=6 * math.sin(t * 4))
        pop_words(sub, ["Spot an Etsy shop", "that needs you", "in 10 seconds"], t, 0.0, 930, 96, (WHITE, GOLD), gap=0.07, highlight={"etsy", "10", "seconds"})
        kk = p(t, 1.3, 0.4)
        pill(sub, W / 2, 1290, "Your next client", F_SEMI, 48, WHITE, INK, alpha=out_cubic(kk), scale=out_back(kk), icon="🎯")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Great product.", "Weak listing."], t, s1 + 0.1, 360, 90, (WHITE, ACC), gap=0.1, highlight={"weak"})
        # two stat cards
        for i, (big, small, col, ic) in enumerate([("212", "happy reviews", GREEN, "⭐"), ("1", "photo", RED, "📷")]):
            kk = p(t, s1 + 1.2 + i * 0.6, 0.45)
            if kk <= 0: continue
            cx = W / 2 + (i * 2 - 1) * 210
            card = Image.new("RGBA", (380, 380), (0, 0, 0, 0)); d = ImageDraw.Draw(card)
            d.rounded_rectangle([0, 0, 379, 379], radius=40, fill=(255, 255, 255, 235))
            card.alpha_composite(emoji_img(ic, 80), (150, 30))
            d.text((190, 200), big, font=font(F_BLACK, 120), fill=(*col, 255), anchor="mm")
            d.text((190, 310), small, font=font(F_XB, 40), fill=(*INK, 255), anchor="mm")
            sc = out_back(kk); card = card.resize((max(4, int(380 * sc)), max(4, int(380 * sc))))
            sub.alpha_composite(with_alpha(card, out_cubic(kk)), (int(cx - card.width / 2), int(800 - card.height / 2)))
        kk = p(t, s1 + 3.6, 0.4)
        pill(sub, W / 2, 1180, "That gap is your gig", F_XB, 56, GOLD, INK, alpha=out_cubic(kk), scale=out_back(kk), icon="💡")
        draw_text(sub, "Shoppers love it. Search can't find it.", F_SEMI, 44, W / 2, 1330, SOFT, alpha=out_cubic(p(t, s1 + 4.3, 0.4)))
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Check 3 things"], t, s2 + 0.1, 280, 84, (WHITE, GOLD), gap=0.07, highlight={"3"})
        lw, lh = 640, 860
        im = shop_listing(lw, lh)
        sc = 0.72
        ox, oy = int(W / 2 - lw * sc / 2), 380
        d = ImageDraw.Draw(im)
        for i, (lab, box) in enumerate(FLAGS):
            kk = p(t, s2 + 1.0 + i * 2.0, 0.4)
            if kk <= 0: continue
            d.rounded_rectangle(box, radius=24, outline=(*RED, int(255 * out_cubic(kk))), width=10)
        im = im.resize((int(lw * sc), int(lh * sc)))
        sub.alpha_composite(im, (ox, oy))
        # labels under the card
        for i, (lab, box) in enumerate(FLAGS):
            kk = p(t, s2 + 1.2 + i * 2.0, 0.4)
            if kk <= 0: continue
            y = 1070 + i * 95
            x = 170 + 60 * (1 - out_cubic(kk))
            place_emoji(sub, "🚩", x, y, 64 * out_back(kk), alpha=out_cubic(kk))
            draw_text(sub, lab, F_XB, 48, x + 56, y, WHITE, alpha=out_cubic(kk), anchor="lm")
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Your shop scorecard"], t, s3 + 0.1, 300, 80, (WHITE, ACC), gap=0.07, highlight={"scorecard"})
        rows = [("Candle shop", 3, "Reach out"), ("Mug shop", 2, "Reach out"), ("Print shop", 0, "Skip")]
        for i, (name, n, verdict) in enumerate(rows):
            kk = p(t, s3 + 0.7 + i * 0.8, 0.45)
            if kk <= 0: continue
            w, h = 860, 170
            row = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(row)
            d.rounded_rectangle([0, 0, w - 1, h - 1], radius=36, fill=(255, 255, 255, 240))
            d.text((40, 58), name, font=font(F_XB, 46), fill=(*INK, 255), anchor="lm")
            d.text((40, 118), f"{n}/3 red flags", font=font(F_SEMI, 34), fill=(110, 110, 120, 255), anchor="lm")
            col = GREEN if n >= 2 else (150, 150, 160)
            d.rounded_rectangle([w - 300, 50, w - 40, 120], radius=35, fill=(*col, 255))
            d.text((w - 170, 85), verdict, font=font(F_XB, 38), fill=(255, 255, 255, 255), anchor="mm")
            sub.alpha_composite(with_alpha(row, out_cubic(kk)), (int(W / 2 - w / 2 + 80 * (1 - out_cubic(kk))), 450 + i * 210))
        kk = p(t, s3 + 3.6, 0.4)
        pill(sub, W / 2, 1180, "2+ flags = worth a pitch", F_BLACK, 54, ACC, INK, alpha=out_cubic(kk), scale=out_back(kk), icon="✅")
        draw_text(sub, "Takes about 10 seconds per shop", F_SEMI, 42, W / 2, 1330, SOFT, alpha=out_cubic(p(t, s3 + 4.2, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel2.mp4")
