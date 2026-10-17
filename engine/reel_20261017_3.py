"""Send this DM to one local shop today (Holiday gift guide writing, part 3)."""
from reel_common import *

ACC = (190, 120, 255)   # violet
GOLD = (255, 212, 96)
GREEN = (70, 210, 140)
RED = (255, 96, 110)
bg = Background(top=(26, 10, 44), bottom=(60, 14, 52), blobs=[(170, 90, 255), (255, 90, 170), (255, 190, 90)], seed=2903)

MSG = ["Hi! Love your candles 🙌", "I write holiday gift guides", "for small shops. Want a free", "sample 'Gifts under $30'", "using your products?"]


def wrap_bubble(lines, n_chars, w, fill, fg, size=40):
    shown, left = [], n_chars
    for ln in lines:
        if left <= 0: break
        shown.append(ln[:left]); left -= len(ln)
    h = 40 + len(lines) * int(size * 1.35)
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=36, fill=fill)
    for i, s in enumerate(shown):
        s = s.replace("🙌", "")
        d.text((34, 20 + i * size * 1.35), s, font=font(F_SEMI, size), fill=fg)
    return im


def phone(t, start, w=760, h=980):
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=70, fill=(18, 18, 24, 255))
    d.rounded_rectangle([16, 16, w - 17, h - 17], radius=58, fill=(250, 250, 252, 255))
    d.rounded_rectangle([w / 2 - 90, 34, w / 2 + 90, 64], radius=15, fill=(18, 18, 24, 255))
    d.line([40, 190, w - 40, 190], fill=(225, 226, 232, 255), width=3)
    d.ellipse([50, 92, 134, 176], fill=(255, 222, 200, 255))
    e = emoji_img("🌿", 52); im.alpha_composite(e, (int(92 - e.width / 2), int(134 - e.height / 2)))
    d.text((156, 116), "Maple & Wick", font=font(F_XB, 40), fill=(*INK, 255), anchor="lm")
    d.text((156, 156), "Local candle shop", font=font(F_MED, 28), fill=(120, 124, 136, 255), anchor="lm")
    total = sum(len(l) for l in MSG)
    n = int(total * clamp((t - start) / 3.6))
    if n > 0:
        b = wrap_bubble(MSG, n, 600, (*ACC, 255), (255, 255, 255, 255))
        im.alpha_composite(b, (w - 40 - 600, 240))
    if t > start + 3.9:
        d.text((w - 50, 240 + 40 + 5 * 54 + 30), "Sent ✓", font=font(DEJAVU, 28), fill=(120, 124, 136, 255), anchor="rm")
    # typing bar
    d.rounded_rectangle([40, h - 130, w - 40, h - 50], radius=40, fill=(238, 239, 244, 255))
    d.text((80, h - 90), "Message...", font=font(F_MED, 32), fill=(150, 154, 166, 255), anchor="lm")
    return im


def calendar(sub, t, start, cy):
    cw, ch = 860, 620
    k = p(t, start, 0.4)
    if k <= 0: return
    im = Image.new("RGBA", (cw, ch), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, cw - 1, ch - 1], radius=36, fill=(255, 255, 255, 255))
    d.text((cw / 2, 56), "Your next 6 weeks", font=font(F_BLACK, 44), fill=(*INK, 255), anchor="mm")
    rows = [("Day 1", "DM 5 local shops", "📩", ACC),
            ("Day 3", "Send the free sample", "🎁", GOLD),
            ("Day 6", "Offer the full guide", "🤝", GREEN),
            ("Nov 27", "Black Friday", "🛍️", RED)]
    for i, (day, lab, em, col) in enumerate(rows):
        kk = p(t, start + 0.5 + i * 0.7, 0.4)
        if kk <= 0: continue
        y = 120 + i * 120; a = int(255 * out_cubic(kk))
        d.rounded_rectangle([30, y, 230, y + 96], radius=24, fill=(*col, a))
        d.text((130, y + 48), day, font=font(F_BLACK, 38), fill=(255, 255, 255, a) if col != GOLD else (*INK, a), anchor="mm")
        e = with_alpha(emoji_img(em, 58).copy(), out_cubic(kk)); im.alpha_composite(e, (258, int(y + 48 - e.height / 2)))
        d.text((340, y + 48), lab, font=font(F_XB, 40), fill=(*INK, a), anchor="lm")
    sub.alpha_composite(with_alpha(im, out_cubic(k)), (int(W / 2 - cw / 2), int(cy - ch / 2 + 50 * (1 - out_cubic(k)))))


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = clamp(p(t, 0.0, 0.3) + 0.4)
        place_emoji(sub, "📱", W / 2, 520 + 12 * math.sin(t * 6), 200 * out_back(k), alpha=k, rot=6 * math.sin(t * 4))
        pop_words(sub, ["Send this DM", "to one local", "shop today"], t, -0.25, 930, 106, (WHITE, GOLD), gap=0.06, highlight={"dm", "today"})
        kk = p(t, 1.2, 0.4)
        pill(sub, W / 2, 1300, "Your first gift guide client", F_SEMI, 46, WHITE, INK, alpha=out_cubic(kk), scale=out_back(kk), icon="🎁")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Most beginners", "send this:"], t, s1 + 0.1, 340, 84, (WHITE, RED), gap=0.07, highlight={"this:"})
        kb = p(t, s1 + 1.0, 0.45)
        if kb > 0:
            b = wrap_bubble(["Hi, do you need", "a writer? DM me."], 99, 640, (255, 255, 255, 255), (*INK, 255), size=50)
            sub.alpha_composite(with_alpha(b, out_cubic(kb)), (int(W / 2 - 320), int(620 + 40 * (1 - out_cubic(kb)))))
        kx = p(t, s1 + 2.2, 0.35)
        place_emoji(sub, "❌", W / 2 + 320, 640, 130 * out_back(kx), alpha=out_cubic(kx))
        kk = p(t, s1 + 2.8, 0.4)
        pill(sub, W / 2, 1000, "Vague = easy to ignore", F_XB, 52, RED, WHITE, alpha=out_cubic(kk), scale=out_back(kk), icon="🙈")
        kk2 = p(t, s1 + 4.0, 0.4)
        pill(sub, W / 2, 1180, "Offer a free sample instead", F_XB, 52, GREEN, INK, alpha=out_cubic(kk2), scale=out_back(kk2), icon="💡")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Copy this DM"], t, s2 + 0.1, 270, 80, (WHITE, GOLD), gap=0.07, highlight={"copy"})
        kp = p(t, s2 + 0.4, 0.5)
        if kp > 0:
            ph = phone(t, s2 + 1.2)
            sub.alpha_composite(with_alpha(ph, out_cubic(kp)), (int(W / 2 - 380), int(380 + 80 * (1 - out_cubic(kp)))))
        kk = p(t, s2 + 5.4, 0.4)
        pill(sub, W / 2, 1470, "Name their product. Give first.", F_XB, 44, ACC, WHITE, alpha=out_cubic(kk), scale=out_back(kk), icon="🎯")
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Then follow this plan"], t, s3 + 0.1, 290, 76, (WHITE, ACC), gap=0.07, highlight={"plan"})
        calendar(sub, t, s3 + 0.5, 750)
        kk = p(t, s3 + 3.8, 0.4)
        pill(sub, W / 2, 1180, "Sample free, full guide $75", F_XB, 50, GOLD, INK, alpha=out_cubic(kk), scale=out_back(kk), icon="💰")
        draw_text(sub, "Example pricing. Results depend on your work.", F_MED, 36, W / 2, 1360, SOFT, alpha=out_cubic(p(t, s3 + 4.4, 0.5)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel3.mp4")
