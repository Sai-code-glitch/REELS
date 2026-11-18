"""Your first brand style guide: 20 minutes, $0 (4 parts, free Canva build, hex codes via color picker)."""
from reel_brand import *

ACC = (80, 220, 200)    # teal
GOLD = (255, 214, 92)
bg = Background(top=(4, 28, 34), bottom=(8, 58, 66), blobs=[(20, 110, 120), (80, 220, 200), (30, 70, 140)], seed=3222)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Your first brand", "style guide:", "20 minutes, $0"], t, -0.3, 380, 96, (WHITE, ACC), gap=0.05, highlight={"20", "minutes,", "$0"})
        guide_card(sub, t, 0.5, W / 2, 1180, w=460, rot=3)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Only 4 things", "on 1 page"], t, s1 + 0.1, 320, 92, (WHITE, ACC), gap=0.07, highlight={"4", "1"})
        checklist(sub, t, s1 + 1.0, ["Logo + name", "3 colors with hex codes", "2 fonts: headline + body", "1 do, 1 don't"], 620, 150, ACC, size=54, x0=150, every=0.8)
        kb = p(t, s1 + 4.6, 0.4)
        pill(sub, W / 2, 1290, "Simple beats fancy", F_XB, 54, GOLD, INK, alpha=out_cubic(kb), scale=out_back(kb), icon="✨")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Build it in free Canva"], t, s2 + 0.1, 260, 76, (WHITE, ACC), gap=0.07, highlight={"free", "canva"})
        canva_guide(sub, t, s2 + 0.4, 960, [s2 + 1.2, s2 + 2.8, s2 + 4.4, s2 + 6.0],
                    labels=["1. Logo + name", "2. Colors + hex codes", "3. Two fonts", "4. Do / Don't"], w=860, h=1140)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Get exact hex codes"], t, s3 + 0.1, 270, 84, (WHITE, ACC), gap=0.07, highlight={"hex", "codes"})
        hex_picker(sub, t, s3 + 0.4, 700, ACC)
        checklist(sub, t, s3 + 3.4, ["Pick from their logo", "Save as a 1-page PDF"], 1110, 120, ACC, size=50, x0=190, every=0.8)
        draw_text(sub, "Free: Canva's color picker or any eyedropper tool", F_SEMI, 34, W / 2, 1400, SOFT, alpha=out_cubic(p(t, s3 + 5.0, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel2.mp4")
