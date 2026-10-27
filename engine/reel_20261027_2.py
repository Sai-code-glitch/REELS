"""Write a sale text in 160 characters -- the 5-part formula small shops can paste."""
from reel_sms import *

ACC = (255, 120, 200)   # pink
GOLD = (255, 214, 92)
RED = (255, 90, 90)
MINT = (90, 220, 170)
SKY = (120, 190, 255)
bg = Background(top=(30, 8, 44), bottom=(60, 16, 80), blobs=[(220, 80, 200), (120, 60, 220), (255, 120, 160)], seed=3002)

BAD = "HUGE SALE!!! Everything in the store is on sale this weekend so come in and shop with us, tell your friends, follow us on Instagram and Facebook, visit our website for all the details!!!"
GOOD = "Rosa's Bakery: 20% off all pies Fri 11/27 only. Order: rosas.co/bf Reply STOP to opt out"


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, -0.2, 0.3)
        place_emoji(sub, "✍️", W / 2, 450 - 16 * math.sin(t * 6), 180 * out_back(k), alpha=k)
        pop_words(sub, ["Write a sale text", "in 160 characters"], t, -0.3, 780, 104, (WHITE, ACC), gap=0.07, highlight={"sale", "160"})
        kc = p(t, 1.2, 0.5)
        if kc > 0:
            n = int(160 * out_cubic(kc))
            pill(sub, W / 2, 1060, f"{n}/160", F_BLACK, 70, SMS_GREEN, WHITE, alpha=out_cubic(p(t, 1.2, 0.2)), scale=out_back(p(t, 1.2, 0.4)), pad=(50, 22))
        kp = p(t, 2.0, 0.4)
        pill(sub, W / 2, 1230, "Small shops pay for this", F_XB, 46, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="🛍️")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Most shop texts", "look like this"], t, s1 + 0.1, 290, 80, (WHITE, RED), gap=0.07, highlight={"this"})
        compose_box(sub, t, s1 + 0.6, 720, BAD, 2.4)
        kx = p(t, s1 + 3.6, 0.4)
        pill(sub, W / 2, 1090, "Too long = split into 2 texts", F_XB, 46, (255, 230, 232), (200, 30, 50), alpha=out_cubic(kx), scale=out_back(kx), icon="⚠️")
        ky = p(t, s1 + 4.6, 0.4)
        pill(sub, W / 2, 1230, "No date, no link, no opt-out", F_XB, 46, (255, 230, 232), (200, 30, 50), alpha=out_cubic(ky), scale=out_back(ky), icon="❌")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Use 5 parts"], t, s2 + 0.1, 270, 92, (WHITE, ACC), gap=0.07, highlight={"5"})
        items = [("1", "Shop name", "Rosa's Bakery:"), ("2", "The offer", "20% off all pies"), ("3", "The deadline", "Fri 11/27 only"),
                 ("4", "One link", "rosas.co/bf"), ("5", "Opt-out", "Reply STOP to opt out")]
        cols = [ACC, GOLD, MINT, SKY, (255, 160, 110)]
        for i, (num, lab, ex) in enumerate(items):
            kk = p(t, s2 + 0.8 + i * 0.9, 0.4)
            if kk <= 0: continue
            y = 440 + i * 165
            x = 150 + 60 * (1 - out_cubic(kk))
            pill(sub, x + 40, y, num, F_BLACK, 50, cols[i], INK, alpha=out_cubic(kk), scale=out_back(kk), pad=(26, 14))
            draw_text(sub, lab, F_BLACK, 54, x + 110, y - 22, WHITE, alpha=out_cubic(kk), anchor="lm")
            draw_text(sub, ex, F_SEMI, 40, x + 110, y + 36, cols[i], alpha=out_cubic(kk), anchor="lm")
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Put together:"], t, s3 + 0.1, 270, 88, (WHITE, MINT), gap=0.07, highlight={"together:"})
        compose_box(sub, t, s3 + 0.5, 600, GOOD, 2.2)
        kc = p(t, s3 + 3.2, 0.4)
        pill(sub, W / 2, 870, "88 characters: fits in 1 text", F_XB, 46, SMS_GREEN, WHITE, alpha=out_cubic(kc), scale=out_back(kc), icon="✅")
        kp = p(t, s3 + 4.0, 0.4)
        pill(sub, W / 2, 1020, "Example: write 3 for $75", F_XB, 50, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="💵")
        kr = p(t, s3 + 4.6, 0.4)
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 36, W / 2, 1140, SOFT, alpha=out_cubic(kr))
        kq = p(t, s3 + 5.2, 0.4)
        draw_text(sub, "Only for customers who opted in to texts", F_SEMI, 36, W / 2, 1210, SOFT, alpha=out_cubic(kq))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel2.mp4")
