"""Stop using flash on product photos -- the window + white paper setup that makes phone shots look clean."""
from reel_photo import *

ACC = (80, 210, 255)    # sky cyan
GOLD = (255, 214, 92)
RED = (255, 96, 110)
MINT = (90, 230, 170)
bg = Background(top=(6, 22, 40), bottom=(10, 12, 30), blobs=[(40, 150, 255), (60, 220, 200), (120, 100, 255)], seed=2962)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, 0.0, 0.3)
        place_emoji(sub, "⚡", W / 2, 450, 190 * out_back(k), alpha=k)
        d = ImageDraw.Draw(sub)
        if k > 0:  # big red "no" ring + slash over the flash
            r = 150 * out_back(k)
            d.ellipse([W / 2 - r, 450 - r, W / 2 + r, 450 + r], outline=(*RED, int(255 * k)), width=22)
            d.line([W / 2 - r * .7, 450 - r * .7, W / 2 + r * .7, 450 + r * .7], fill=(*RED, int(255 * k)), width=22)
        pop_words(sub, ["Stop using flash", "on product photos"], t, 0.0, 830, 100, (WHITE, ACC), gap=0.07, highlight={"stop", "flash"})
        kp = p(t, 1.4, 0.4)
        pill(sub, W / 2, 1100, "Do this by a window instead", F_XB, 50, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), pad=(40, 22), icon="🪟")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Flash makes products", "look cheap"], t, s1 + 0.1, 330, 88, (WHITE, RED), gap=0.08, highlight={"cheap"})
        photo_card(sub, t, s1 + 0.8, W / 2, 790, 480, "flash", tag="With flash", tag_color=RED)
        d = ImageDraw.Draw(sub)
        k1 = p(t, s1 + 2.0, 0.4)
        pill(sub, W / 2 - 230, 1175, "Glare", F_XB, 50, (245, 246, 250), INK, alpha=out_cubic(k1), scale=out_back(k1), icon="✨")
        k2 = p(t, s1 + 2.6, 0.4)
        pill(sub, W / 2 + 190, 1175, "Hard shadow", F_XB, 50, (245, 246, 250), INK, alpha=out_cubic(k2), scale=out_back(k2), icon="🌑")
        kq = p(t, s1 + 3.8, 0.4)
        pill(sub, W / 2, 1330, "Free fix: one window", F_XB, 52, ACC, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="☀️")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["The $0 setup"], t, s2 + 0.1, 290, 96, (WHITE, ACC), gap=0.08, highlight={"$0"})
        window_setup(sub, t, s2 + 0.5, 640, ACC)
        checklist(sub, t, s2 + 3.0, ["Window light from the side", "White paper bounces it back", "Flash off, phone on 2x", "Tap the product to focus"], 1030, 100, ACC, size=48, x0=150, every=0.8)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Tap, hold, shoot"], t, s3 + 0.1, 290, 92, (WHITE, ACC), gap=0.08, highlight={"hold"})
        if t < s3 + 4.2:
            camera_ui(sub, t, s3 + 0.5, W / 2, 400, mode="hero", focus_at=s3 + 1.4, shot_at=s3 + 3.0)
            kh = p(t, s3 + 1.1, 0.3)
            place_emoji(sub, "👆", W / 2 + 40, 900 + 20 * math.sin(t * 7), 110, alpha=out_cubic(kh) * (1 - p(t, s3 + 2.6, 0.3)))
        else:
            photo_card(sub, t, s3 + 4.2, W / 2 - 220, 780, 340, "flash", tag="Flash", tag_color=RED, rot=4)
            photo_card(sub, t, s3 + 4.6, W / 2 + 220, 780, 340, "hero", tag="Window", tag_color=MINT, rot=-4)
            kq = p(t, s3 + 5.4, 0.4)
            pill(sub, W / 2, 1120, "Same phone. Same candle.", F_XB, 52, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="📱")
            kc = p(t, s3 + 6.0, 0.4)
            draw_text(sub, "Shoot in daylight, mid-morning is easiest", F_SEMI, 40, W / 2, 1260, SOFT, alpha=out_cubic(kc))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel2.mp4")
