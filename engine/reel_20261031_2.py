"""Your first review QR card: 10 minutes, $0."""
from reel_reviews import *

ACC = (255, 120, 200)   # pink
GOLD = (255, 214, 92)
bg = Background(top=(26, 8, 48), bottom=(60, 20, 100), blobs=[(150, 60, 220), (240, 90, 170), (60, 90, 220)], seed=3042)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Your first", "review QR card:", "10 minutes, $0"], t, -0.3, 520, 104, (WHITE, ACC), gap=0.06, highlight={"10", "minutes,", "$0"})
        kp = p(t, 0.8, 0.35)
        pill(sub, W / 2, 820, "Make it for 1 local shop", F_XB, 50, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="🏪")
        table_card(sub, t, 1.1, W / 2, 1220, "Leaf & Pot", "🪴", (40, 150, 90), w=440, h=616, rot=-5, seed=11)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Step 1: get their", "review link"], t, s1 + 0.1, 300, 84, (WHITE, ACC), gap=0.07, highlight={"review", "link"})
        profile_panel(sub, t, s1 + 0.7, 450, "Leaf & Pot", "🪴", (40, 150, 90), s1 + 1.9, s1 + 2.7, s1 + 4.0, link="g.page/r/leaf-and-pot/review")
        kx = p(t, s1 + 4.8, 0.4)
        pill(sub, W / 2, 1360, "Owner taps \"Ask for reviews\"", F_XB, 46, WHITE, INK, alpha=out_cubic(kx), scale=out_back(kx), icon="📲")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Step 2: build", "the card in Canva"], t, s2 + 0.1, 290, 84, (WHITE, ACC), gap=0.07, highlight={"Canva"})
        st = [s2 + 0.9, s2 + 1.8, s2 + 2.6, s2 + 3.5, s2 + 4.6]
        table_card(sub, t, s2 + 0.6, W / 2, 900, "Leaf & Pot", "🪴", (40, 150, 90), w=520, h=728, steps=st, seed=11)
        labels = ["Pick a card size", "Add 1 friendly line", "Add 5 stars", "QR code app + paste link", "Download as PDF"]
        idx = sum(1 for x in st if t >= x) - 1
        if idx >= 0:
            kk = p(t, st[idx], 0.3)
            pill(sub, W / 2, 1370, labels[idx], F_XB, 46, GOLD, INK, alpha=out_cubic(kk), scale=out_back(kk))
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Done in about", "10 minutes"], t, s3 + 0.1, 290, 90, (WHITE, ACC), gap=0.07, highlight={"10", "minutes"})
        timer(sub, t, s3 + 0.6, 2.0, W / 2, 500, 10, GOLD)
        checklist(sub, t, s3 + 2.0, ["Free Canva account", "Their Google profile", "Test-scan with your phone"], 660, 100, ACC, size=50, x0=150, every=0.6)
        kq = p(t, s3 + 4.2, 0.4)
        pill(sub, W / 2, 1050, "Rule: no rewards for reviews", F_XB, 44, WHITE, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="🚫")
        draw_text(sub, "Google doesn't allow paying for reviews.", F_SEMI, 36, W / 2, 1160, SOFT, alpha=out_cubic(p(t, s3 + 4.8, 0.4)))
        draw_text(sub, "Just make it easy to leave one.", F_SEMI, 36, W / 2, 1215, SOFT, alpha=out_cubic(p(t, s3 + 5.2, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel2.mp4")
