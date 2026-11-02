"""Your first holiday flyer: 10 minutes, $0 (Canva build)."""
from reel_flyer import *
from reel_portfolio import timer

ACC = (110, 200, 255)   # sky blue
GOLD = (255, 214, 92)
FLY = (255, 140, 80)
KW = dict(shop="Bean There", emoji="☕", offer="Free cookie with any drink", foot="7am-3pm · 48 Oak Ave")
bg = Background(top=(6, 14, 44), bottom=(14, 40, 92), blobs=[(40, 110, 240), (90, 210, 255), (130, 70, 220)], seed=3062)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Your first", "holiday flyer:", "10 minutes, $0"], t, -0.3, 470, 104, (WHITE, ACC), gap=0.06, highlight={"10", "minutes,", "$0"})
        kp = p(t, 0.8, 0.35)
        pill(sub, W / 2, 780, "Make it for 1 local shop", F_XB, 50, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="🏪")
        flyer_card(sub, t, 1.0, W / 2, 1210, FLY, w=420, rot=5, **KW)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Step 1: grab 4 facts", "from their page"], t, s1 + 0.1, 300, 80, (WHITE, ACC), gap=0.07, highlight={"4", "facts"})
        checklist(sub, t, s1 + 0.9, ["Shop name", "Saturday hours", "Address", "An offer they already run"], 500, 120, ACC, size=52, x0=140, every=0.7)
        kx = p(t, s1 + 4.3, 0.4)
        pill(sub, W / 2, 1080, "All on their Google or Facebook page", F_XB, 42, WHITE, INK, alpha=out_cubic(kx), scale=out_back(kx), icon="🔎")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Step 2: build", "it in Canva"], t, s2 + 0.1, 260, 84, (WHITE, ACC), gap=0.07, highlight={"Canva"})
        st = [s2 + 0.9, s2 + 2.0, s2 + 3.1, s2 + 4.3, s2 + 5.5]
        canva_flyer(sub, t, s2 + 0.5, 960, FLY, st, labels=["Pick a flyer template", "Big date: Sat Nov 28", "Add what they sell", "1 offer in a bold box", "Hours + address. Download"], **KW)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Done in about", "10 minutes"], t, s3 + 0.1, 290, 90, (WHITE, ACC), gap=0.07, highlight={"10", "minutes"})
        timer(sub, t, s3 + 0.6, 2.0, W / 2, 500, 10, GOLD)
        checklist(sub, t, s3 + 2.0, ["Free Canva account", "Download PDF + PNG", "Check the date twice"], 660, 100, ACC, size=50, x0=150, every=0.6)
        kq = p(t, s3 + 4.0, 0.4)
        pill(sub, W / 2, 1050, "Send it as a free sample", F_XB, 48, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="🎁")
        draw_text(sub, "Example: $35-$50 for the full set.", F_SEMI, 36, W / 2, 1170, SOFT, alpha=out_cubic(p(t, s3 + 4.6, 0.4)))
        draw_text(sub, "Results depend on your work.", F_SEMI, 36, W / 2, 1225, SOFT, alpha=out_cubic(p(t, s3 + 4.9, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel2.mp4")
