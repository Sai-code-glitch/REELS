"""Don't pitch Etsy shops in Etsy messages (Holiday Etsy listing refresh, part 3)."""
from reel_common import *

ACC = (170, 120, 255)   # violet
GOLD = (255, 214, 92)
GREEN = (60, 205, 130)
RED = (255, 96, 110)
bg = Background(top=(14, 12, 44), bottom=(30, 20, 80), blobs=[(150, 90, 255), (60, 140, 255), (255, 120, 200)], seed=2893)

MSG = ["Hi Maya! Love your candles.", "I rewrote one listing title", "for holiday searches.", "Free, no strings.", "Want to see it?"]


def phone_dm(t, start, w=720, h=900):
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=60, fill=(250, 250, 252, 255))
    d.rounded_rectangle([0, 0, w - 1, 150], radius=60, fill=(240, 240, 246, 255))
    d.rectangle([0, 100, w - 1, 150], fill=(240, 240, 246, 255))
    d.ellipse([40, 40, 120, 120], fill=(255, 190, 120, 255))
    im.alpha_composite(emoji_img("🕯️", 50), (60, 52))
    d.text((140, 65), "maya.candle.co", font=font(F_XB, 38), fill=(*INK, 255), anchor="lm")
    d.text((140, 105), "Instagram", font=font(F_MED, 28), fill=(120, 120, 130, 255), anchor="lm")
    # typed bubble
    full = " ".join(MSG)
    n = int(len(full) * clamp((t - start) / 3.0))
    shown, lines, cnt = [], [], 0
    for line in MSG:
        take = max(0, min(len(line), n - cnt)); cnt += len(line) + 1
        if take > 0: lines.append(line[:take])
    if lines:
        bh = 60 + 58 * len(lines)
        d.rounded_rectangle([90, 200, w - 40, 200 + bh], radius=36, fill=(120, 80, 240, 255))
        for i, ln in enumerate(lines):
            d.text((130, 260 + i * 58), ln, font=font(F_SEMI, 37), fill=(255, 255, 255, 255), anchor="lm")
    if t > start + 3.6:
        k = p(t, start + 3.6, 0.4)
        d.rounded_rectangle([40, 600, 470, 700], radius=36, fill=(228, 228, 236, int(255 * out_cubic(k))))
        d.text((80, 650), "Yes please! 🙌"[:-2], font=font(F_SEMI, 40), fill=(*INK, int(255 * out_cubic(k))), anchor="lm")
        if k > 0.5:
            im.alpha_composite(emoji_img("🙌", 48), (380, 626))
    return im


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, 0.0, 0.3)
        place_emoji(sub, "🚫", W / 2, 500 + 12 * math.sin(t * 6), 200 * out_back(k), alpha=k, rot=6 * math.sin(t * 4))
        pop_words(sub, ["Stop pitching", "Etsy shops in", "Etsy messages"], t, 0.0, 930, 96, (WHITE, GOLD), gap=0.07, highlight={"stop"})
        kk = p(t, 1.3, 0.4)
        pill(sub, W / 2, 1290, "Do this instead", F_SEMI, 50, WHITE, INK, alpha=out_cubic(kk), scale=out_back(kk), icon="👇")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Etsy's rules ban", "unsolicited promo", "messages"], t, s1 + 0.1, 400, 80, (WHITE, RED), gap=0.07, highlight={"ban"})
        kk = p(t, s1 + 1.8, 0.45)
        if kk > 0:
            w, h = 760, 300
            im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
            d.rounded_rectangle([0, 0, w - 1, h - 1], radius=40, fill=(255, 255, 255, 240))
            d.text((50, 70), "Etsy shop page", font=font(F_XB, 44), fill=(*INK, 255), anchor="lm")
            d.text((50, 150), "About  ·  Shop members", font=font(F_SEMI, 36), fill=(110, 110, 120, 255), anchor="lm")
            ks = p(t, s1 + 2.8, 0.4)
            d.rounded_rectangle([40, 200, 520, 270], radius=35, fill=(*ACC, int(255 * out_cubic(ks))))
            d.text((80, 235), "Instagram · Website", font=font(F_XB, 36), fill=(255, 255, 255, int(255 * out_cubic(ks))), anchor="lm")
            sub.alpha_composite(with_alpha(im, out_cubic(kk)), (int(W / 2 - w / 2), int(820 + 60 * (1 - out_cubic(kk)))))
            if ks > 0:
                place_emoji(sub, "👈", W / 2 + 260, 1055 + 10 * math.sin(t * 8), 90 * out_back(ks), alpha=out_cubic(ks))
        kk = p(t, s1 + 3.8, 0.4)
        pill(sub, W / 2, 1300, "Find their Instagram or email", F_XB, 50, GOLD, INK, alpha=out_cubic(kk), scale=out_back(kk), icon="🔗")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Lead with a free sample"], t, s2 + 0.1, 290, 72, (WHITE, GOLD), gap=0.07, highlight={"free", "sample"})
        k = p(t, s2 + 0.5, 0.45)
        if k > 0:
            im = phone_dm(t, s2 + 1.0)
            sub.alpha_composite(with_alpha(im, out_cubic(k)), (int(W / 2 - im.width / 2), int(400 + 80 * (1 - out_cubic(k)))))
        kk = p(t, s2 + 5.4, 0.4)
        pill(sub, W / 2, 1420, "Show, don't sell", F_BLACK, 56, ACC, WHITE, alpha=out_cubic(kk), scale=out_back(kk), icon="✨")
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Then offer the package"], t, s3 + 0.1, 300, 76, (WHITE, ACC), gap=0.07, highlight={"package"})
        steps = [("1 free title", "🎁", WHITE), ("5-listing refresh", "📝", GOLD), ("$50 example price", "💵", GREEN)]
        for i, (lab, ic, col) in enumerate(steps):
            kk = p(t, s3 + 0.7 + i * 0.9, 0.45)
            if kk <= 0: continue
            y = 500 + i * 230
            pill(sub, W / 2, y, lab, F_BLACK, 60, col, INK, alpha=out_cubic(kk), scale=out_back(kk), icon=ic, pad=(46, 26))
            if i < 2:
                ka = p(t, s3 + 1.1 + i * 0.9, 0.3)
                draw_text(sub, "↓", DEJAVU, 80, W / 2, y + 118, WHITE, alpha=out_cubic(ka))
        checklist(sub, t, s3 + 3.6, ["Polite, short, specific"], 1210, 100, ACC, size=50, x0=230)
        draw_text(sub, "Example pricing. Results depend on your work.", F_MED, 36, W / 2, 1380, SOFT, alpha=out_cubic(p(t, s3 + 4.4, 0.5)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel3.mp4")
