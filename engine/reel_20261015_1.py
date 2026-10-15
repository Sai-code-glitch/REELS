"""Make it once in Canva, sell it all season (Canva templates to sell before the holidays, part 1)."""
from reel_common import *

ACC = (40, 220, 190)    # teal
GOLD = (255, 214, 92)
RED = (255, 96, 110)
CORAL = (255, 120, 90)
bg = Background(top=(6, 30, 36), bottom=(8, 52, 58), blobs=[(30, 200, 170), (40, 120, 255), (255, 200, 80)], seed=2881)

VARIANTS = [(214, 40, 60), (20, 110, 80), (30, 40, 90), (240, 160, 40), (120, 50, 160)]


def sale_post(w, h, col, k=1.0, title="HOLIDAY SALE"):
    """A square promo graphic; k (0..1) controls how many layers have been built."""
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    s = w / 520
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=int(22 * s), fill=(*col, 255))
    if k > 0.15:
        for i in range(6):
            x = (60 + i * 85) * s; y = (60 + (i % 3) * 30) * s
            d.text((x, y), "*", font=font(F_BLACK, 40 * s), fill=(255, 255, 255, 120), anchor="mm")
    if k > 0.35:
        d.text((w / 2, h * 0.36), title, font=font(F_BLACK, 62 * s), fill=(255, 255, 255, 255), anchor="mm")
    if k > 0.55:
        d.text((w / 2, h * 0.53), "UP TO 30% OFF", font=font(F_XB, 40 * s), fill=(255, 230, 150, 255), anchor="mm")
    if k > 0.75:
        bw, bh = 230 * s, 64 * s
        d.rounded_rectangle([w / 2 - bw / 2, h * 0.72 - bh / 2, w / 2 + bw / 2, h * 0.72 + bh / 2], radius=int(bh / 2), fill=(255, 255, 255, 255))
        d.text((w / 2, h * 0.72), "SHOP NOW", font=font(F_XB, 30 * s), fill=(*col, 255), anchor="mm")
    return im


def editor(sub, t, start, cy=900):
    k = p(t, start, 0.45)
    if k <= 0: return
    w, h = 880, 820
    ed = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(ed)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=40, fill=(242, 244, 248, 255))
    d.rounded_rectangle([0, 0, w - 1, 90], radius=40, fill=(124, 77, 255, 255))
    d.rectangle([0, 50, w - 1, 90], fill=(124, 77, 255, 255))
    d.text((40, 45), "Design editor", font=font(F_XB, 34), fill=(255, 255, 255, 255), anchor="lm")
    d.rounded_rectangle([w - 190, 22, w - 30, 68], radius=23, fill=(255, 255, 255, 255))
    d.text((w - 110, 45), "Share", font=font(F_XB, 28), fill=(124, 77, 255, 255), anchor="mm")
    # left toolbar
    tools = [("T", "Text"), ("■", "Shapes"), ("✦", "Elements"), ("▣", "Photos")]
    for i, (ic, lab) in enumerate(tools):
        y = 150 + i * 120
        active = int(p(t, start + 0.6, 3.2) * 4) == i
        d.rounded_rectangle([20, y - 40, 140, y + 50], radius=18, fill=(225, 214, 255, 255) if active else (255, 255, 255, 255))
        d.text((80, y - 6), ic, font=font(DEJAVU, 34), fill=(*INK, 255), anchor="mm")
        d.text((80, y + 30), lab, font=font(F_MED, 20), fill=(90, 96, 110, 255), anchor="mm")
    kb = p(t, start + 0.5, 3.2)
    post = sale_post(640, 640, VARIANTS[0], kb)
    ed.alpha_composite(post, (190, 130))
    sub.alpha_composite(with_alpha(ed, out_cubic(k)), (int(W / 2 - w / 2), int(cy - h / 2 + 60 * (1 - out_cubic(k)))))


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, 0.0, 0.3)
        place_emoji(sub, "🎨", W / 2, 500 + 12 * math.sin(t * 6), 200 * out_back(k), alpha=k, rot=6 * math.sin(t * 4))
        pop_words(sub, ["Make it once", "in Canva.", "Sell it all season."], t, 0.0, 930, 112, (WHITE, GOLD), gap=0.07, highlight={"once", "season."})
        kk = p(t, 1.3, 0.4)
        pill(sub, W / 2, 1300, "Digital = no stock, no shipping", F_SEMI, 46, WHITE, INK, alpha=out_cubic(kk), scale=out_back(kk), icon="📦")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Every small shop needs", "holiday sale posts"], t, s1 + 0.1, 380, 76, (WHITE, ACC), gap=0.07, highlight={"holiday", "sale", "posts"})
        probs = [("No designer", "🙅", 1.4), ("No time in November", "⏰", 2.2), ("Needs it before Black Friday", "📅", 3.0)]
        for i, (lab, ic, at) in enumerate(probs):
            kk = p(t, s1 + at, 0.35)
            pill(sub, W / 2, 650 + i * 150, lab, F_XB, 52, (255, 236, 238), (170, 30, 50), alpha=out_cubic(kk), scale=out_back(kk), icon=ic)
        kk = p(t, s1 + 4.3, 0.45)
        if kk > 0:
            pop_words(sub, ["So they buy", "ready-made templates"], t, s1 + 4.3, 1270, 78, (WHITE, GOLD), gap=0.07, highlight={"ready-made", "templates"})
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Here's how to make one"], t, s2 + 0.1, 290, 76, (WHITE, ACC), gap=0.07, highlight={"make", "one"})
        if t < s2 + 4.6:
            editor(sub, t, s2 + 0.3, cy=880)
        else:
            # five colour versions pop in
            for i, col in enumerate(VARIANTS):
                kk = p(t, s2 + 4.6 + i * 0.22, 0.4)
                if kk <= 0: continue
                im = sale_post(300, 300, col, 1.0)
                sc = out_back(kk)
                im = im.resize((max(1, int(300 * sc)), max(1, int(300 * sc))))
                r, c = divmod(i, 3)
                cx = (W / 2 - 330 + c * 330) if r == 0 else (W / 2 - 165 + (c) * 330)
                cy = 700 + r * 340
                sub.alpha_composite(with_alpha(im, out_cubic(kk)), (int(cx - im.width / 2), int(cy - im.height / 2)))
        steps = [("1. Design 1 sale post", 0.6, 2.2), ("2. Leave text easy to edit", 2.4, 4.4), ("3. Make 5 color versions", 4.6, 6.0)]
        for lab, a, b in steps:
            kk = p(t, s2 + a, 0.3)
            if kk > 0 and t < s2 + b:
                al = out_cubic(kk) * (1 - p(t, s2 + b - 0.3, 0.3))
                pill(sub, W / 2, 1440, lab, F_XB, 52, GOLD, INK, alpha=al, scale=out_back(kk), icon="👉")
        kk = p(t, s2 + 6.1, 0.4)
        pill(sub, W / 2, 1440, "4. Bundle = Holiday Sale Pack", F_XB, 52, ACC, INK, alpha=out_cubic(kk), scale=out_back(kk), icon="🎁")
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Example math"], t, s3 + 0.1, 300, 84, (WHITE, GOLD), gap=0.07, highlight={"math"})
        kk = p(t, s3 + 0.4, 0.4)
        pill(sub, W / 2, 470, "Holiday Sale Pack  ·  $9", F_XB, 56, WHITE, INK, alpha=out_cubic(kk), scale=out_back(kk), icon="🏷️")
        kk = p(t, s3 + 1.0, 0.4)
        draw_text(sub, "Made once. Sold as a download.", F_SEMI, 46, W / 2, 590, SOFT, alpha=out_cubic(kk))
        money_counter(sub, t, s3 + 1.6, 180, 860, ACC, label="if it sells 20 times")
        kk = p(t, s3 + 4.2, 0.4)
        pill(sub, W / 2, 1230, "Minus platform fees", F_SEMI, 44, (255, 236, 238), (170, 30, 50), alpha=out_cubic(kk), scale=out_back(kk), icon="💳")
        draw_text(sub, "Example pricing. Results depend on your work.", F_MED, 36, W / 2, 1370, SOFT, alpha=out_cubic(p(t, s3 + 4.8, 0.5)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel1.mp4")
