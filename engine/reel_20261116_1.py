"""Type "gift tags" on Etsy tonight (printables sell until Dec 24, go niche, example listing)."""
from reel_tags import *

ACC = (255, 120, 110)   # warm coral
GOLD = (255, 214, 92)
bg = Background(top=(6, 34, 26), bottom=(14, 70, 48), blobs=[(20, 110, 70), (255, 110, 100), (40, 80, 150)], seed=3201)
TEACH = THEMES["teacher"]


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ['Type "gift tags"', "on Etsy tonight"], t, -0.3, 360, 108, (WHITE, ACC), gap=0.06, highlight={"etsy", "tonight", '"gift', 'tags"'})
        etsy_search(sub, t, 0.3, 640, "gift tags printable", type_dur=0.7)
        big_tag(sub, t, 1.1, W / 2, 1150, TEACH, w=400, rot=-5)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Printables sell", "right up to Christmas"], t, s1 + 0.1, 290, 84, (WHITE, ACC), gap=0.07, highlight={"christmas"})
        dec_timeline(sub, t, s1 + 0.8, 690, ACC)
        kb = p(t, s1 + 4.0, 0.4)
        pill(sub, W / 2, 1040, "Instant download = no shipping", F_XB, 46, GOLD, INK, alpha=out_cubic(kb), scale=out_back(kb), icon="⚡")
        draw_text(sub, "Buyers print them at home", F_XB, 46, W / 2, 1165, WHITE, alpha=out_cubic(p(t, s1 + 4.8, 0.4)))
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Add who it's for"], t, s2 + 0.1, 270, 90, (WHITE, ACC), gap=0.07, highlight={"who"})
        rows = [("🎁", (220, 224, 234), "gift tags", "Too broad", False),
                ("🍎", (255, 205, 205), "teacher gift tags", "Specific", True),
                ("🏡", (200, 236, 210), "neighbor gift tags", "Specific", True),
                ("☕", (236, 214, 196), "coworker gift tags", "Specific", True)]
        for i, (em, col, q, v, g) in enumerate(rows):
            niche_row(sub, t, s2 + 0.6 + i * 0.6, 470 + i * 175, em, col, q, v, g, s2 + 3.2 + i * 0.35)
        kq = p(t, s2 + 5.0, 0.4)
        pill(sub, W / 2, 1230, "Pick 1 person people shop for", F_XB, 50, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="🎯")
        draw_text(sub, "Then check what's already listed", F_SEMI, 40, W / 2, 1350, SOFT, alpha=out_cubic(p(t, s2 + 5.6, 0.4)))
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Your listing", "(example)"], t, s3 + 0.1, 270, 84, (WHITE, ACC), gap=0.07, highlight={"listing"})
        etsy_listing(sub, t, s3 + 0.5, 400, "Teacher Christmas Gift Tags, Printable PDF, 8 per Page, Instant Download",
                     "$3.00", "YourShop · Digital download", "🍎", (255, 205, 205), size=40, photo_h=300)
        checklist(sub, t, s3 + 2.2, ["8 tags per page", "Dashed cut lines", "Instant download"], 1130, 100, ACC, size=50, x0=220)
        draw_text(sub, "Example price. Results depend on your work.", F_SEMI, 34, W / 2, 1460, SOFT, alpha=out_cubic(p(t, s3 + 4.6, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel1.mp4")
