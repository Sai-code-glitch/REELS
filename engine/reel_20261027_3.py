"""Sell this 3-text pack to 1 shop tonight -- who to pitch, the DM, the example math."""
from reel_sms import *

ACC = (255, 170, 60)    # amber
GOLD = (255, 220, 110)
MINT = (90, 220, 170)
bg = Background(top=(34, 16, 6), bottom=(64, 32, 12), blobs=[(255, 150, 50), (230, 90, 60), (255, 200, 90)], seed=3003)

PITCH = "Hi Rosa! I write Black Friday texts for small shops: 3 short texts, ready to paste. Want a free sample for your pie sale?"


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, -0.2, 0.3)
        place_emoji(sub, "🌙", W / 2, 450 - 16 * math.sin(t * 6), 180 * out_back(k), alpha=k, rot=8 * math.sin(t * 3))
        pop_words(sub, ["Sell this", "3-text pack to", "1 shop tonight"], t, -0.3, 820, 100, (WHITE, ACC), gap=0.06, highlight={"3-text", "1", "tonight"})
        kp = p(t, 1.4, 0.4)
        pill(sub, W / 2, 1170, "Black Friday is 31 days away", F_XB, 48, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), pad=(40, 22), icon="🗓️")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Pick 1 shop that has:"], t, s1 + 0.1, 290, 76, (WHITE, ACC), gap=0.07, highlight={"1", "shop"})
        checklist(sub, t, s1 + 0.8, ["A text club sign-up", "A holiday sale coming", "No marketing team"],
                  520, 150, ACC, size=56, every=0.7)
        kx = p(t, s1 + 4.2, 0.4)
        pill(sub, W / 2, 1150, "Check their site or Instagram bio", F_XB, 44, WHITE, INK, alpha=out_cubic(kx), scale=out_back(kx), icon="🔍")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Send this DM"], t, s2 + 0.1, 260, 88, (WHITE, ACC), gap=0.07, highlight={"dm"})
        sms_thread(sub, t, s2 + 0.4, W / 2, 360, [
            ("me", PITCH, s2 + 1.0, "TODAY 7:12 PM"),
            ("them", "Ooh yes, send it!", s2 + 3.6, None),
            ("me", "Here you go. If you like it, the full 3-text pack is $75", s2 + 4.8, None),
        ], header="Rosa's Bakery", h=860, avatar=(255, 140, 90))
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Example math"], t, s3 + 0.1, 270, 88, (WHITE, GOLD), gap=0.07, highlight={"math"})
        pop_words(sub, ["2 shops × $75"], t, s3 + 0.6, 470, 76, (WHITE, ACC), gap=0.12, highlight={"2", "$75"})
        money_counter(sub, t, s3 + 1.8, 150, 760, GOLD, label="example total")
        kr = p(t, s3 + 4.4, 0.4)
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 36, W / 2, 1100, SOFT, alpha=out_cubic(kr))
        kq = p(t, s3 + 5.0, 0.4)
        pill(sub, W / 2, 1230, "Free sample first = easier yes", F_XB, 46, WHITE, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="🤝")
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel3.mp4")
