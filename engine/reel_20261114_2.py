"""Your first 2027 calendar: 30 minutes, $0 (free Canva template -> 12 pages -> check dates -> PDF)."""
from reel_calendar import *

ACC = (110, 230, 160)   # mint green
GOLD = (255, 214, 92)
bg = Background(top=(4, 30, 22), bottom=(10, 70, 52), blobs=[(20, 130, 90), (110, 230, 160), (30, 90, 150)], seed=3182)
GARDEN = dict(emoji="🌱", title_extra="Garden Planner")
PAGE_ACC = (60, 150, 90)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Your first", "2027 calendar:", "30 minutes, $0"], t, -0.3, 400, 104, (WHITE, ACC), gap=0.06, highlight={"30", "minutes,", "$0"})
        page_card(sub, t, 0.6, W / 2, 1180, PAGE_ACC, w=420, rot=-5, **GARDEN)
        timer(sub, t, 1.0, 2.4, W / 2 + 20, 700, 30, GOLD)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["You need 3 things"], t, s1 + 0.1, 280, 88, (WHITE, ACC), gap=0.07, highlight={"3"})
        checklist(sub, t, s1 + 0.8, ["Free Canva account", "Free calendar template", "1 theme you love"], 470, 130, ACC, size=56, x0=170, every=0.8)
        kq = p(t, s1 + 3.6, 0.4)
        pill(sub, W / 2, 940, "Search \"calendar\" in Canva", F_XB, 50, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="🔎")
        draw_text(sub, "Check the template's license allows resale", F_SEMI, 38, W / 2, 1060, SOFT, alpha=out_cubic(p(t, s1 + 4.3, 0.4)))
        kk = p(t, s1 + 5.0, 0.4)
        pill(sub, W / 2, 1200, "Or draw your own grid", F_XB, 46, (255, 255, 255), INK, alpha=out_cubic(kk), scale=out_back(kk), icon="✏️")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Build 1 page"], t, s2 + 0.1, 270, 90, (WHITE, ACC), gap=0.07, highlight={"1", "page"})
        st = [s2 + 0.8, s2 + 2.0, s2 + 3.2, s2 + 4.2, s2 + 5.0]
        canva_cal(sub, t, s2 + 0.4, 980, PAGE_ACC, st, h=1080, dup_at=s2 + 5.9,
                  labels=["1. Month grid", "2. Month + year", "3. Your theme", "4. Your colors", "5. Duplicate ×12"], **GARDEN)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Check every date"], t, s3 + 0.1, 270, 88, (WHITE, ACC), gap=0.07, highlight={"every", "date"})
        twelve_fan(sub, t, s3 + 0.5, 770, PAGE_ACC, w=170, **GARDEN)
        kq = p(t, s3 + 2.6, 0.4)
        pill(sub, W / 2, 1200, "Jan 1, 2027 is a Friday", F_XB, 50, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="📅")
        kd = p(t, s3 + 3.6, 0.4)
        pill(sub, W / 2, 1325, "Download → PDF Print", F_XB, 50, ACC, INK, alpha=out_cubic(kd), scale=out_back(kd), icon="📥")
        draw_text(sub, "1 wrong date = 1 bad review", F_SEMI, 40, W / 2, 1445, SOFT, alpha=out_cubic(p(t, s3 + 4.6, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel2.mp4")
