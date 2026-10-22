"""Stop writing "HUGE SALE" subject lines -- the what + deal + deadline formula."""
from reel_email import *

ACC = (64, 224, 170)    # mint
GOLD = (255, 214, 92)
RED = (255, 96, 110)
SKY = (110, 190, 255)
bg = Background(top=(4, 26, 30), bottom=(8, 52, 56), blobs=[(30, 200, 160), (40, 150, 220), (120, 230, 140)], seed=2952)

SAME = [
    ("Bloom & Co", "HUGE SALE!!!"),
    ("Pine Candles", "HUGE SALE!!!"),
    ("Mug Life", "Our BIGGEST sale ever"),
    ("Knit Corner", "HUGE SALE!!!"),
    ("Lena's Soap", "Don't miss out!!!"),
]


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, 0.0, 0.3)
        place_emoji(sub, "🛑", W / 2, 470 - 16 * math.sin(t * 6), 170 * out_back(k), alpha=k)
        pop_words(sub, ["Stop writing", "\"HUGE SALE\"", "subject lines"], t, 0.0, 820, 100, (WHITE, RED), gap=0.08, highlight={"\"huge", "sale\""})
        kp = p(t, 1.4, 0.4)
        pill(sub, W / 2, 1150, "Write this instead", F_BLACK, 56, ACC, INK, alpha=out_cubic(kp), scale=out_back(kp), pad=(46, 24), icon="✍️")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Black Friday inbox:", "they all look the same"], t, s1 + 0.1, 320, 80, (WHITE, RED), gap=0.08, highlight={"same"})
        inbox(sub, t, s1 + 0.6, 470, [(a, b, s1 + 0.9 + i * 0.35, "dim") for i, (a, b) in enumerate(SAME)])
        kx = p(t, s1 + 3.4, 0.35)
        place_emoji(sub, "😴", W / 2 + 330, 520, 120 * out_back(kx), alpha=out_cubic(kx))
        kp = p(t, s1 + 4.0, 0.4)
        pill(sub, W / 2, 1470, "Nothing to click for", F_XB, 52, (245, 246, 250), INK, alpha=out_cubic(kp), scale=out_back(kp), icon="🤷")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["The formula"], t, s2 + 0.1, 300, 96, (WHITE, ACC), gap=0.08, highlight={"formula"})
        build_row(sub, t, s2 + 0.6, 470, ["What", "Deal", "Deadline"], [GOLD, ACC, SKY], size=56)
        ex = [("What", "Soy candles", GOLD), ("Deal", "25% off", ACC), ("Deadline", "ends Sunday", SKY)]
        for i, (lab, val, col) in enumerate(ex):
            kk = p(t, s2 + 2.4 + i * 0.7, 0.4)
            y = 660 + i * 130
            draw_text(sub, lab, F_XB, 44, 330, y, col, alpha=out_cubic(kk), anchor="rm")
            draw_text(sub, "→", F_XB, 44, 375, y, WHITE, alpha=out_cubic(kk))
            pill(sub, 640, y, val, F_XB, 48, (245, 246, 250), INK, alpha=out_cubic(kk), scale=out_back(kk))
        kr = p(t, s2 + 4.8, 0.45)
        draw_text(sub, "Result:", F_XB, 46, W / 2, 1110, SOFT, alpha=out_cubic(kr))
        kq = p(t, s2 + 5.2, 0.45)
        pill(sub, W / 2, 1230, "Soy candles 25% off, ends Sunday", F_BLACK, 50, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), pad=(40, 26), icon="🕯️")
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Now it stands out"], t, s3 + 0.1, 300, 88, (WHITE, ACC), gap=0.08, highlight={"stands", "out"})
        rows = [(a, b, s3 + 0.5, "dim") for a, b in SAME]
        rows[1] = ("Pine Candles", "Soy candles 25% off, ends Sunday", s3 + 1.2, "hot")
        inbox(sub, t, s3 + 0.4, 390, rows)
        kp = p(t, s3 + 2.6, 0.4)
        pill(sub, W / 2, 1410, "Sell it: 10 subject lines = $40", F_XB, 50, ACC, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="💵")
        kq = p(t, s3 + 3.4, 0.45)
        draw_text(sub, "Example pricing. Results depend on your work.", F_MED, 36, W / 2, 1530, SOFT, alpha=out_cubic(kq))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel2.mp4")
