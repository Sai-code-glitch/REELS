"""Shops pay for this flyer before Nov 28 (Small Business Saturday flyer gig)."""
from reel_flyer import *

ACC = (255, 110, 120)   # cranberry pink
GOLD = (255, 214, 92)
FLY = (230, 70, 80)
bg = Background(top=(40, 6, 16), bottom=(92, 18, 36), blobs=[(220, 50, 80), (255, 150, 90), (120, 30, 120)], seed=3061)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Shops pay for", "this flyer", "before Nov 28"], t, -0.3, 420, 108, (WHITE, ACC), gap=0.06, highlight={"flyer", "nov", "28"})
        kp = p(t, 0.7, 0.35)
        pill(sub, W / 2, 720, "Small Business Saturday", F_XB, 52, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="🛍️")
        flyer_card(sub, t, 0.9, W / 2, 1170, FLY, w=430, rot=-4)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Most shops post", "this instead"], t, s1 + 0.1, 290, 84, (WHITE, ACC), gap=0.07, highlight={"this", "instead"})
        plain_post(sub, t, s1 + 0.6, 440, ACC, scroll_at=s1 + 3.6)
        a1 = out_cubic(p(t, s1 + 2.0, 0.4)) * (1 - p(t, s1 + 3.5, 0.3))
        if a1 > 0:
            pill(sub, W / 2, 1110, "Easy to scroll right past", F_XB, 48, WHITE, INK, alpha=a1, scale=out_back(p(t, s1 + 2.0, 0.4)), icon="😴")
        flyer_card(sub, t, s1 + 4.4, W / 2, 760, FLY, w=380, rot=3)
        k2 = p(t, s1 + 5.2, 0.4)
        pill(sub, W / 2, 1210, "A bright flyer stops the scroll", F_XB, 46, GOLD, INK, alpha=out_cubic(k2), scale=out_back(k2), icon="👀")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Put just 4 things", "on it"], t, s2 + 0.1, 280, 86, (WHITE, ACC), gap=0.07, highlight={"4", "things"})
        st = [s2 + 0.6, s2 + 1.2, s2 + 2.6, s2 + 3.9, s2 + 5.3]
        flyer_card(sub, t, s2 + 0.5, W / 2, 860, FLY, w=450, steps=st)
        labels = [None, "1. The date, big", "2. What they sell", "3. One simple offer", "4. Hours + address"]
        idx = sum(1 for x in st if t >= x) - 1
        if idx >= 1:
            kk = p(t, st[idx], 0.3)
            pill(sub, W / 2, 1400, labels[idx], F_XB, 50, GOLD, INK, alpha=out_cubic(kk), scale=out_back(kk))
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["What to charge", "(example)"], t, s3 + 0.1, 280, 86, (WHITE, ACC), gap=0.07, highlight={"charge"})
        offer_card(sub, t, s3 + 0.6, 790, [
            ("Printable flyer (PDF)", "$35", s3 + 1.1),
            ("Instagram + Facebook size", "$15", s3 + 1.7),
        ], "$50", ACC, title="Small Biz Saturday flyer", h=560)
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 34, W / 2, 1150, SOFT, alpha=out_cubic(p(t, s3 + 3.0, 0.4)))
        kq = p(t, s3 + 3.8, 0.4)
        pill(sub, W / 2, 1300, "Deliver by Nov 20 so they can print", F_XB, 44, WHITE, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="🖨️")
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel1.mp4")
