"""Your first 'order by' banner: 10 minutes, $0 (date math + Canva story build)."""
from reel_shipby import *

ACC = (110, 200, 255)   # ice blue
GOLD = (255, 214, 92)
bg = Background(top=(6, 12, 42), bottom=(16, 36, 90), blobs=[(50, 110, 240), (110, 210, 255), (140, 80, 220)], seed=3142)
KW = dict(shop="Oak & Wick", emoji="🕯️")


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Your first", "“order by” banner:", "10 minutes, $0"], t, -0.3, 420, 100, (WHITE, ACC), gap=0.06, highlight={"10", "minutes,", "$0"})
        kp = p(t, 0.8, 0.35)
        pill(sub, W / 2, 710, "For 1 online shop", F_XB, 50, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="🛒")
        story_card(sub, t, 1.0, W / 2, 1180, ACC, w=380, rot=-4, **KW)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Step 1: work out", "the date"], t, s1 + 0.1, 290, 84, (WHITE, ACC), gap=0.07, highlight={"date"})
        date_math(sub, t, s1 + 0.6, 430, GOLD, [
            ("📦", "USPS Ground Advantage", "Dec 17", s1 + 1.0),
            ("⏳", "Shop packs in 2 days", "− 2", s1 + 1.9),
        ], ("Order by", "Tue Dec 15"), s1 + 2.9)
        draw_text(sub, "Example. Use the shop's own packing time.", F_SEMI, 36, W / 2, 1000, SOFT, alpha=out_cubic(p(t, s1 + 3.6, 0.4)))
        kx = p(t, s1 + 4.3, 0.4)
        pill(sub, W / 2, 1140, "Check usps.com for the latest dates", F_XB, 42, WHITE, INK, alpha=out_cubic(kx), scale=out_back(kx), icon="🔎")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Step 2: build", "it in Canva"], t, s2 + 0.1, 250, 84, (WHITE, ACC), gap=0.07, highlight={"canva"})
        st = [s2 + 0.9, s2 + 2.0, s2 + 3.1, s2 + 4.2, s2 + 5.4]
        canva_story(sub, t, s2 + 0.5, 960, ACC, st, labels=["Pick a story template", "LAST DAY TO ORDER", "The date, huge", "Where it ships", "Shop name. Download"], **KW)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Done in about", "10 minutes"], t, s3 + 0.1, 290, 90, (WHITE, ACC), gap=0.07, highlight={"10", "minutes"})
        timer(sub, t, s3 + 0.6, 2.0, W / 2, 500, 10, GOLD)
        checklist(sub, t, s3 + 2.0, ["Free Canva account", "Story + 1 website line", "Check the date twice"], 660, 100, ACC, size=50, x0=150, every=0.6)
        kq = p(t, s3 + 4.0, 0.4)
        pill(sub, W / 2, 1050, "Send it as a free sample", F_XB, 48, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="🎁")
        draw_text(sub, "Example: $40 for the full set.", F_SEMI, 36, W / 2, 1170, SOFT, alpha=out_cubic(p(t, s3 + 4.6, 0.4)))
        draw_text(sub, "Results depend on your work.", F_SEMI, 36, W / 2, 1225, SOFT, alpha=out_cubic(p(t, s3 + 4.9, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel2.mp4")
