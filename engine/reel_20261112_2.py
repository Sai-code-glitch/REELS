"""Your first holiday menu: 10 minutes, $0 (Canva build for 1 café)."""
from reel_menu import *

ACC = (120, 225, 160)   # holly green
GOLD = (255, 214, 92)
bg = Background(top=(6, 30, 20), bottom=(14, 64, 40), blobs=[(30, 140, 80), (120, 220, 150), (200, 60, 60)], seed=3162)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Your first", "holiday menu:", "10 minutes, $0"], t, -0.3, 400, 104, (WHITE, ACC), gap=0.06, highlight={"10", "minutes,", "$0"})
        kp = p(t, 0.8, 0.35)
        pill(sub, W / 2, 700, "For 1 local café", F_XB, 50, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="☕")
        menu_card(sub, t, 1.0, W / 2, 1180, ACC, w=480, rot=-4)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Step 1: grab", "their real info"], t, s1 + 0.1, 290, 86, (WHITE, ACC), gap=0.07, highlight={"real"})
        checklist(sub, t, s1 + 0.8, ["Their holiday drinks", "Their exact prices", "Their name + colors"], 520, 120, ACC, size=56, x0=170, every=0.7)
        kx = p(t, s1 + 3.2, 0.4)
        pill(sub, W / 2, 1010, "From their posts or menu", F_XB, 50, GOLD, INK, alpha=out_cubic(kx), scale=out_back(kx), icon="📱")
        draw_text(sub, "Never guess a price.", F_XB, 52, W / 2, 1160, WHITE, alpha=out_cubic(p(t, s1 + 4.0, 0.4)))
        kz = p(t, s1 + 4.6, 0.4)
        place_emoji(sub, "🚫", W / 2, 1320, 130 * out_back(kz), alpha=out_cubic(kz))
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Step 2: build", "it in Canva"], t, s2 + 0.1, 250, 84, (WHITE, ACC), gap=0.07, highlight={"canva"})
        st = [s2 + 0.9, s2 + 2.0, s2 + 3.1, s2 + 4.4, s2 + 5.5]
        canva_menu(sub, t, s2 + 0.5, 960, ACC, st, labels=["Search “holiday menu”", "Title: HOLIDAY DRINKS", "5 drinks + prices", "Add 1 “NEW” badge", "Name. Download"])
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Done in about", "10 minutes"], t, s3 + 0.1, 290, 90, (WHITE, ACC), gap=0.07, highlight={"10", "minutes"})
        timer(sub, t, s3 + 0.6, 2.0, W / 2, 500, 10, GOLD)
        checklist(sub, t, s3 + 2.0, ["Free Canva account", "Post + story size", "Check every price"], 660, 100, ACC, size=50, x0=150, every=0.6)
        kq = p(t, s3 + 4.0, 0.4)
        pill(sub, W / 2, 1050, "Send it as a free sample", F_XB, 48, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="🎁")
        draw_text(sub, "Example: $40-65 for the full set.", F_SEMI, 36, W / 2, 1170, SOFT, alpha=out_cubic(p(t, s3 + 4.6, 0.4)))
        draw_text(sub, "Results depend on your work.", F_SEMI, 36, W / 2, 1225, SOFT, alpha=out_cubic(p(t, s3 + 4.9, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel2.mp4")
