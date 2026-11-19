"""Your first Reel edit: 15 minutes, $0 (free editor app, 4 clips, trim, 1 text line, export 9:16)."""
from reel_edit import *

ACC = (255, 120, 170)   # pink
GOLD = (255, 214, 92)
bg = Background(top=(36, 8, 30), bottom=(78, 18, 60), blobs=[(160, 40, 110), (255, 120, 170), (90, 40, 150)], seed=3232)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Your first Reel edit:", "15 minutes, $0"], t, -0.3, 360, 96, (WHITE, ACC), gap=0.06, highlight={"15", "minutes,", "$0"})
        phone_reel(sub, t, 0.4, W / 2, 1100, w=340)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["All you need:"], t, s1 + 0.1, 300, 88, (WHITE, ACC), gap=0.07, highlight={"need:"})
        checklist(sub, t, s1 + 0.8, ["A free editor app", "4 phone clips, 3-5 sec", "1 offer line of text"], 500, 150, ACC, size=54, x0=150, every=0.9)
        draw_text(sub, "(CapCut, InShot or Instagram Edits)", F_SEMI, 38, W / 2, 1000, SOFT, alpha=out_cubic(p(t, s1 + 3.6, 0.4)))
        kb = p(t, s1 + 4.4, 0.4)
        pill(sub, W / 2, 1160, "Practice on your own clips", F_XB, 50, GOLD, INK, alpha=out_cubic(kb), scale=out_back(kb), icon="📱")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        editor_ui(sub, t, s2 + 0.1, 860, steps=[s2 + 0.5, s2 + 2.4, s2 + 4.4, s2 + 6.0],
                  labels=["1. Import 4 clips", "2. Trim each to ~3 sec", "3. Add 1 text line", "4. Export 9:16"])
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["3 rules that help"], t, s3 + 0.1, 270, 86, (WHITE, ACC), gap=0.07, highlight={"3"})
        checklist(sub, t, s3 + 0.7, ["Text in the first 2 sec", "Under 20 seconds", "Text away from edges"], 450, 140, ACC, size=50, x0=130, every=0.8)
        phone_reel(sub, t, s3 + 2.8, W / 2, 1110, w=230, rot=3)
        draw_text(sub, "Then post it as your first sample", F_XB, 42, W / 2, 1450, WHITE, alpha=out_cubic(p(t, s3 + 4.2, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel2.mp4")
