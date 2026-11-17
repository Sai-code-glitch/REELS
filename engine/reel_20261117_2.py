"""Your first resume fix: 20 minutes, $0 (4 fixes in free Google Docs, bullet rewrites)."""
from reel_resume import *

ACC = (190, 140, 255)   # lavender
GOLD = (255, 214, 92)
bg = Background(top=(22, 10, 44), bottom=(52, 24, 90), blobs=[(110, 50, 180), (190, 140, 255), (40, 70, 160)], seed=3212)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Your first resume fix:", "20 minutes, $0"], t, -0.3, 360, 98, (WHITE, ACC), gap=0.06, highlight={"20", "minutes,", "$0"})
        resume_card(sub, t, 0.5, W / 2, 1000, w=480, good=True, rot=-3)
        timer(sub, t, 0.9, 2.6, W / 2, 1420, 20, GOLD)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Most resumes", "look like this"], t, s1 + 0.1, 290, 88, (WHITE, ACC), gap=0.07, highlight={"this"})
        flags = [("Long objective", 0.22, -0.55), ("Vague bullets", 0.47, 0.55), ("3 pages", 0.9, -0.55)]
        resume_card(sub, t, s1 + 0.6, W / 2, 940, w=600, good=False, flags=flags, flag_at=s1 + 2.0)
        kq = p(t, s1 + 4.6, 0.4)
        pill(sub, W / 2, 1460, "4 fixes change everything", F_XB, 50, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="🛠️")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Fix it in free Google Docs"], t, s2 + 0.1, 260, 72, (WHITE, ACC), gap=0.06, highlight={"free"})
        steps = [s2 + 0.9, s2 + 2.6, s2 + 4.2, s2 + 5.8]
        docs_editor(sub, t, s2 + 0.4, 960, steps, labels=["1. Name + job title on top", "2. A 2-line summary", "3. Bullets that show results", "4. Skills. Keep it 1 page"])
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Rewrite every bullet"], t, s3 + 0.1, 270, 86, (WHITE, ACC), gap=0.07, highlight={"bullet"})
        bullet_fix(sub, t, s3 + 0.5, 560, "Responsible for answering emails", "Answered 60+ emails a day", 
                   s3 + 1.8, hl="60+")
        bullet_fix(sub, t, s3 + 2.6, 900, "Worked on various team projects", "Trained 4 new teammates", s3 + 3.8, hl="4")
        kq = p(t, s3 + 5.0, 0.4)
        pill(sub, W / 2, 1190, "Use their real numbers only", F_XB, 48, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="✅")
        draw_text(sub, "Ask: how many? how often? how fast?", F_SEMI, 40, W / 2, 1310, SOFT, alpha=out_cubic(p(t, s3 + 5.6, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel2.mp4")
