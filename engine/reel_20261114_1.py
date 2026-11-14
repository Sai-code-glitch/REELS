"""Search "2027 calendar" on Etsy tonight (broad = crowded, go niche, example listing)."""
from reel_calendar import *

ACC = (255, 150, 80)    # warm orange
GOLD = (255, 214, 92)
bg = Background(top=(30, 12, 44), bottom=(70, 24, 70), blobs=[(150, 50, 140), (255, 140, 80), (80, 40, 170)], seed=3181)
DOG = dict(emoji="🐶", title_extra="Dog Mom")


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Search this", "on Etsy tonight"], t, -0.3, 360, 108, (WHITE, ACC), gap=0.06, highlight={"etsy", "tonight"})
        etsy_search(sub, t, 0.3, 640, "2027 calendar", type_dur=0.7)
        page_card(sub, t, 1.2, W / 2, 1180, (232, 120, 70), w=440, rot=-4, **DOG)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["People buy next", "year's calendar now"], t, s1 + 0.1, 290, 84, (WHITE, ACC), gap=0.07, highlight={"calendar", "now"})
        kp = p(t, s1 + 0.9, 0.4)
        pill(sub, W / 2, 470, "A printable = 1 PDF, no shipping", F_XB, 44, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="📄")
        crowd_grid(sub, t, s1 + 1.6, 590, ACC)
        kb = p(t, s1 + 3.4, 0.4)
        pill(sub, W / 2, 1215, "Plain \"2027 calendar\" = crowded", F_XB, 46, (255, 92, 104), WHITE, alpha=out_cubic(kb), scale=out_back(kb), icon="😬")
        draw_text(sub, "So don't compete there. Go specific.", F_XB, 46, W / 2, 1345, WHITE, alpha=out_cubic(p(t, s1 + 4.4, 0.4)))
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Add who it's for"], t, s2 + 0.1, 270, 90, (WHITE, ACC), gap=0.07, highlight={"who"})
        rows = [("🗓️", (220, 224, 234), "2027 calendar", "Too broad", False),
                ("🐶", (255, 214, 170), "2027 dog mom calendar", "Specific", True),
                ("🌱", (200, 236, 200), "2027 garden planner", "Specific", True),
                ("🍎", (255, 200, 200), "2027 teacher calendar", "Specific", True)]
        for i, (em, col, q, v, g) in enumerate(rows):
            niche_row(sub, t, s2 + 0.6 + i * 0.6, 470 + i * 175, em, col, q, v, g, s2 + 3.2 + i * 0.35)
        kq = p(t, s2 + 5.0, 0.4)
        pill(sub, W / 2, 1230, "Pick a niche you know", F_XB, 52, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="🎯")
        draw_text(sub, "Your hobby, job or pet works", F_SEMI, 40, W / 2, 1350, SOFT, alpha=out_cubic(p(t, s2 + 5.6, 0.4)))
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Your listing", "(example)"], t, s3 + 0.1, 270, 84, (WHITE, ACC), gap=0.07, highlight={"listing"})
        etsy_listing(sub, t, s3 + 0.5, 400, "2027 Dog Mom Calendar, Printable PDF, 12 Months, US Letter",
                     "$4.00", "YourShop · Instant download", "🐶", (255, 214, 170), size=40, photo_h=300)
        checklist(sub, t, s3 + 2.2, ["12 month pages", "Real 2027 dates", "Instant download"], 1130, 100, ACC, size=50, x0=220)
        draw_text(sub, "Example price. Results depend on your work.", F_SEMI, 34, W / 2, 1460, SOFT, alpha=out_cubic(p(t, s3 + 4.6, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel1.mp4")
