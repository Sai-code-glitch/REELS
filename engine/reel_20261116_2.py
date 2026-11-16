"""Your first gift tag sheet: 15 minutes, $0 (Canva build of an 8-per-page printable)."""
from reel_tags import *

ACC = (190, 160, 255)   # lavender
GOLD = (255, 214, 92)
bg = Background(top=(24, 10, 52), bottom=(54, 24, 104), blobs=[(110, 60, 220), (190, 160, 255), (230, 80, 140)], seed=3202)
NEIGH = THEMES["neighbor"]


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Your first", "gift tag sheet:", "15 minutes, $0"], t, -0.3, 400, 104, (WHITE, ACC), gap=0.06, highlight={"15", "minutes,", "$0"})
        sheet_card(sub, t, 0.8, W / 2, 1150, NEIGH, w=420, rot=4)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["1 page. 8 tags."], t, s1 + 0.1, 280, 96, (WHITE, ACC), gap=0.07, highlight={"8"})
        sheet_card(sub, t, s1 + 0.6, W / 2, 800, THEMES["plain"], w=430, steps=[s1 + 1.0, s1 + 1.8, s1 + 2.4, s1 + 3.0, s1 + 3.4])
        kq = p(t, s1 + 4.2, 0.4)
        pill(sub, W / 2, 1180, "Free Canva account is enough", F_XB, 46, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="🎨")
        draw_text(sub, "US Letter size, so buyers print it easily", F_SEMI, 38, W / 2, 1300, SOFT, alpha=out_cubic(p(t, s1 + 4.9, 0.4)))
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Build it in 4 steps"], t, s2 + 0.1, 250, 84, (WHITE, ACC), gap=0.07, highlight={"4"})
        st = [s2 + 1.0, s2 + 2.6, s2 + 4.0, s2 + 5.4, s2 + 6.2]
        canva_tags(sub, t, s2 + 0.4, 930, st, NEIGH,
                   labels=["1. Grid + dashed cut lines", "2. One color band", "3. One cute element", "4. Title + To/From lines", "4. Title + To/From lines"])
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Same layout,", "3 products"], t, s3 + 0.1, 270, 88, (WHITE, ACC), gap=0.07, highlight={"3"})
        for i, (key, x, rot) in enumerate([("teacher", 250, -6), ("neighbor", W / 2, 0), ("coworker", W - 250, 6)]):
            sheet_card(sub, t, s3 + 0.7 + i * 0.5, x, 760 + (30 if i != 1 else 0), THEMES[key], w=300, rot=rot)
        kq = p(t, s3 + 2.6, 0.4)
        pill(sub, W / 2, 1120, "Swap color, element, title", F_XB, 48, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="🔁")
        kx = p(t, s3 + 3.4, 0.4)
        pill(sub, W / 2, 1250, "Download: PDF Print", F_XB, 46, ACC, INK, alpha=out_cubic(kx), scale=out_back(kx), icon="📄")
        draw_text(sub, "Use only your own or free-to-use elements", F_SEMI, 36, W / 2, 1375, SOFT, alpha=out_cubic(p(t, s3 + 4.2, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel2.mp4")
