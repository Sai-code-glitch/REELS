"""Your first Etsy title fix: 5 minutes, $0 (4 questions -> title + 13 tags)."""
from reel_etsy import *

ACC = (90, 225, 190)    # mint
GOLD = (255, 214, 92)
bg = Background(top=(4, 26, 32), bottom=(10, 62, 70), blobs=[(30, 150, 140), (90, 220, 190), (40, 90, 180)], seed=3152)
BAD = "Ornament Christmas Ornament Gift Personalized Ornament Best Christmas Gift 2026 Ornament Family Ornament Tree Decor Gift Idea"
GOOD = "Personalized Ceramic Ornament, White with Gold Name, 3 inch Round"
LIST = dict(price="$18.00", shop="KilnAndCo · Etsy shop", emoji="🎄", color=(214, 240, 226))


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Your first", "Etsy title fix:", "5 minutes, $0"], t, -0.3, 390, 104, (WHITE, ACC), gap=0.06, highlight={"5", "minutes,", "$0"})
        kp = p(t, 0.6, 0.35)
        pill(sub, W / 2, 690, "For 1 Etsy shop", F_XB, 50, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="🛒")
        etsy_listing(sub, t, 0.8, 800, BAD, size=38, photo_h=240, strike_at=1.6, new_title=GOOD, swap_at=2.4, **LIST)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Step 1: answer", "4 questions"], t, s1 + 0.1, 280, 86, (WHITE, ACC), gap=0.07, highlight={"4", "questions"})
        formula_rows(sub, t, s1 + 0.7, 420, [
            ("❓", "What is it?", "Ceramic Ornament"),
            ("🎨", "Color?", "White + Gold"),
            ("📏", "Size?", "3 inch Round"),
            ("✍️", "Special?", "Personalized"),
        ], ACC, every=0.75, row=135)
        kx = p(t, s1 + 4.2, 0.4)
        pill(sub, W / 2, 1040, "Answers are in the photos", F_XB, 50, GOLD, INK, alpha=out_cubic(kx), scale=out_back(kx), icon="📸")
        draw_text(sub, "and the listing description", F_SEMI, 38, W / 2, 1150, SOFT, alpha=out_cubic(p(t, s1 + 4.7, 0.4)))
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Step 2: write it,", "then add tags"], t, s2 + 0.1, 270, 84, (WHITE, ACC), gap=0.07, highlight={"tags"})
        title_box(sub, t, s2 + 0.5, 390, GOOD, 1.8, ACC)
        tag_chips(sub, t, s2 + 3.0, 820, ["christmas ornament", "personalized gift", "family ornament", "gift for mom",
                                           "stocking stuffer", "name ornament"], GOLD, every=0.35, size=40)
        kq = p(t, s2 + 5.6, 0.4)
        pill(sub, W / 2, 1230, "Etsy allows up to 13 tags", F_XB, 50, WHITE, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="🏷️")
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Done in about", "5 minutes"], t, s3 + 0.1, 290, 90, (WHITE, ACC), gap=0.07, highlight={"5", "minutes"})
        timer(sub, t, s3 + 0.6, 2.0, W / 2, 500, 5, GOLD)
        checklist(sub, t, s3 + 2.0, ["Fix 1 title for free", "Send before and after", "Offer to do 10 more"], 660, 100, ACC, size=50, x0=150, every=0.6)
        kq = p(t, s3 + 4.0, 0.4)
        pill(sub, W / 2, 1050, "Your free sample = your pitch", F_XB, 46, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="🎁")
        draw_text(sub, "Example: $3 per title.", F_SEMI, 36, W / 2, 1170, SOFT, alpha=out_cubic(p(t, s3 + 4.6, 0.4)))
        draw_text(sub, "Results depend on your work.", F_SEMI, 36, W / 2, 1225, SOFT, alpha=out_cubic(p(t, s3 + 4.9, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel2.mp4")
