"""Price 3 Fiverr packages like this (Basic / Standard / Premium, make Standard the best deal, 20% fee math)."""
from reel_fiverr import *

ACC = (255, 196, 80)    # amber
GOLD = (255, 214, 92)
bg = Background(top=(8, 16, 34), bottom=(30, 34, 70), blobs=[(40, 60, 150), (255, 170, 60), (20, 120, 140)], seed=3193)
COLS = [("Basic", "$15"), ("Standard", "$35"), ("Premium", "$60")]
ROWS = [("Designs", ["1 flyer", "1 flyer", "3 flyers"]),
        ("Sizes", ["Print", "Print + IG", "Print + IG"]),
        ("Revisions", ["1", "2", "3"]),
        ("Delivery", ["3 days", "2 days", "1 day"])]


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Price 3 Fiverr", "packages like this"], t, -0.3, 380, 104, (WHITE, ACC), gap=0.06, highlight={"3", "packages"})
        packages(sub, t, 0.4, 640, ACC, COLS, ROWS[:2], every=0.3, star=1, star_at=1.8, compact=True, row_h=96)
        draw_text(sub, "Example pricing", F_SEMI, 38, W / 2, 1130, SOFT, alpha=out_cubic(p(t, 1.4, 0.4)))
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["1 price fits", "1 kind of buyer"], t, s1 + 0.1, 290, 88, (WHITE, ACC), gap=0.07, highlight={"1"})
        items = [("🙂", "Just needs 1 flyer", "Basic"), ("😃", "Wants it for Instagram too", "Standard"), ("🤩", "Needs it fast + more", "Premium")]
        for i, (em, lab, pk) in enumerate(items):
            kk = p(t, s1 + 0.9 + i * 0.7, 0.4)
            if kk <= 0: continue
            y = 520 + i * 190
            c, d = gbase(880, 160, fill=(255, 255, 255), radius=34)
            e = emoji_img(em, 80); c.alpha_composite(e, (40, int(80 - e.height / 2)))
            d.text((150, 80), lab, font=font(F_XB, 38), fill=(*INK, 255), anchor="lm")
            ff = font(F_XB, 30); tw = d.textlength(pk, font=ff) + 40
            d.rounded_rectangle([880 - 30 - tw, 52, 850, 108], radius=28, fill=(*FV, 255))
            d.text((850 - tw / 2, 80), pk, font=ff, fill=(255, 255, 255, 255), anchor="mm")
            sub.alpha_composite(with_alpha(c, out_cubic(kk)), (int(100 + 60 * (1 - out_cubic(kk))), y))
        kq = p(t, s1 + 3.6, 0.4)
        pill(sub, W / 2, 1150, "3 packages = 3 ways to say yes", F_XB, 46, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="📦")
        draw_text(sub, "Fiverr lets you offer up to 3.", F_SEMI, 38, W / 2, 1270, SOFT, alpha=out_cubic(p(t, s1 + 4.4, 0.4)))
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Make the middle", "the best deal"], t, s2 + 0.1, 290, 88, (WHITE, ACC), gap=0.07, highlight={"middle", "best"})
        packages(sub, t, s2 + 0.5, 430, ACC, COLS, ROWS, every=0.55, star=1, star_at=s2 + 4.3)
        kq = p(t, s2 + 5.0, 0.4)
        pill(sub, W / 2, 1180, "+$20 gets a lot more", F_XB, 48, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="⭐")
        draw_text(sub, "Example pricing only", F_SEMI, 36, W / 2, 1300, SOFT, alpha=out_cubic(p(t, s2 + 5.5, 0.4)))
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["What you keep", "on $35 (example)"], t, s3 + 0.1, 290, 84, (WHITE, ACC), gap=0.07, highlight={"keep", "$35"})
        formula_rows(sub, t, s3 + 0.6, 440, [
            ("📦", "Standard package", "$35.00"),
            ("✂️", "Fiverr fee 20%", "−$7.00"),
        ], FV, every=0.7, row=140)
        dollar_counter(sub, t, s3 + 2.2, 28.00, 900, ACC, "you keep per order", size=200)
        draw_text(sub, "Before taxes. Check Fiverr's current fees.", F_SEMI, 34, W / 2, 1180, SOFT, alpha=out_cubic(p(t, s3 + 4.2, 0.4)))
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 34, W / 2, 1235, SOFT, alpha=out_cubic(p(t, s3 + 4.6, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel3.mp4")
