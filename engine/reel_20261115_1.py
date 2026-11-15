"""Search your skill on Fiverr tonight (study the top 3 gigs, note 3 things, find your niche gap)."""
from reel_fiverr import *

ACC = (90, 230, 160)    # mint green
GOLD = (255, 214, 92)
bg = Background(top=(4, 26, 24), bottom=(10, 60, 52), blobs=[(20, 120, 90), (90, 230, 160), (30, 70, 140)], seed=3191)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Search your skill", "on Fiverr tonight"], t, -0.3, 360, 104, (WHITE, ACC), gap=0.06, highlight={"fiverr", "tonight"})
        fiverr_search(sub, t, 0.3, 620, "holiday flyer design", type_dur=0.8)
        gig_card(sub, t, 1.1, W / 2, 760, GOLD, "I will design a holiday flyer for your small business", "$15", w=700, rot=-3)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Before you make a gig,", "open the top 3"], t, s1 + 0.1, 290, 80, (WHITE, ACC), gap=0.07, highlight={"top", "3"})
        rows = [("🎄", (255, 214, 170), "I will design a Christmas flyer or poster", "$10", "Study"),
                ("🎁", (200, 230, 255), "I will create holiday sale flyers in Canva", "$20", "Study"),
                ("✨", (230, 210, 255), "I will design an event flyer in 24 hours", "$35", "Study")]
        for i, (em, col, tt, pr, nt) in enumerate(rows):
            gig_row(sub, t, s1 + 0.8 + i * 0.6, 520 + i * 215, em, col, tt, pr, nt, s1 + 2.8 + i * 0.3)
        kb = p(t, s1 + 4.0, 0.4)
        pill(sub, W / 2, 1240, "Example gigs, not real sellers", F_XB, 40, (255, 255, 255), INK, alpha=out_cubic(kb), scale=out_back(kb), icon="👀")
        draw_text(sub, "You're studying, not copying.", F_XB, 46, W / 2, 1360, WHITE, alpha=out_cubic(p(t, s1 + 4.8, 0.4)))
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Write down 3 things"], t, s2 + 0.1, 280, 88, (WHITE, ACC), gap=0.07, highlight={"3"})
        formula_rows(sub, t, s2 + 0.6, 400, [
            ("📦", "What Basic includes", "1 flyer"),
            ("⏱️", "Delivery time", "2-3 days"),
            ("🔁", "Revisions", "1-2"),
        ], FV, every=0.8, row=140)
        draw_text(sub, "Write what you saw (example notes)", F_SEMI, 36, W / 2, 860, SOFT, alpha=out_cubic(p(t, s2 + 2.8, 0.4)))
        kq = p(t, s2 + 3.4, 0.4)
        pill(sub, W / 2, 990, "Copy the structure, never the work", F_XB, 46, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="📝")
        checklist(sub, t, s2 + 4.4, ["Same size package", "Your own designs", "Your own words"], 1130, 100, ACC, size=50, x0=220, every=0.5)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Now find your gap"], t, s3 + 0.1, 280, 88, (WHITE, ACC), gap=0.07, highlight={"gap"})
        rows = [("🎨", (220, 224, 234), "holiday flyer design", "Crowded", False),
                ("🥧", (255, 214, 170), "flyer for bakeries", "Specific", True),
                ("🛍️", (200, 236, 200), "Small Business Sat. flyer", "Specific", True)]
        for i, (em, col, q, v, g) in enumerate(rows):
            niche_row(sub, t, s3 + 0.5 + i * 0.5, 450 + i * 175, em, col, q, v, g, s3 + 2.0 + i * 0.3)
        draw_text(sub, "Your title:", F_XB, 44, W / 2, 1010, SOFT, alpha=out_cubic(p(t, s3 + 3.2, 0.4)))
        pop_words(sub, ["\"I will design a holiday", "flyer for your bakery\""], t, s3 + 3.5, 1150, 60, (WHITE, GOLD), gap=0.05, highlight={"bakery\""})
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel1.mp4")
