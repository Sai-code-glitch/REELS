"""Tap 1 shop's link in bio tonight (link-in-bio page gig: find shops whose bio link is a dead end -> free fix DM + example offer)."""
from reel_linkbio import *

ACC = (80, 220, 200)
GOLD = (255, 222, 120)
bg = Background(top=(8, 34, 42), bottom=(18, 92, 96), blobs=[(30, 140, 140), (80, 220, 200), (10, 60, 80)], seed=1241)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Tap 1 shop's", "link in bio tonight"], t, -0.3, 360, 104, (WHITE, ACC), gap=0.07, highlight={"link", "bio", "tonight"})
        bio_profile(sub, t, 0.4, 620, ACC, tap_at=2.3)
        draw_text(sub, "Where does it go?", F_XB, 56, W / 2, 1290, GOLD, alpha=out_cubic(p(t, 2.6, 0.4)))
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Lots of bio links", "lead to a dead end"], t, s1 + 0.1, 290, 84, (WHITE, ACC), gap=0.07, highlight={"dead", "end"})
        dead_page(sub, t, s1 + 1.0, 500)
        draw_text(sub, "Holiday shoppers tap it", F_XB, 50, W / 2, 1130, WHITE, alpha=out_cubic(p(t, s1 + 2.6, 0.4)))
        draw_text(sub, "and find an old summer sale", F_XB, 50, W / 2, 1195, WHITE, alpha=out_cubic(p(t, s1 + 2.6, 0.4)))
        kb = p(t, s1 + 4.2, 0.4)
        pill(sub, W / 2, 1360, "Dead link = your lead", F_BLACK, 50, GOLD, INK, alpha=out_cubic(kb), scale=out_back(kb), icon="🎯")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Check 3 things", "in 10 seconds"], t, s2 + 0.1, 270, 84, (WHITE, ACC), gap=0.07, highlight={"3", "10"})
        checklist(sub, t, s2 + 0.8, ["Does the link load?", "Is the sale still on?", "Can I find gifts fast?"], 480, 100, ACC, size=48, every=0.6)
        rows = [("🕯️", (255, 214, 170), "@pineandwick", "…/summer-sale", False),
                ("🧶", (200, 225, 255), "@loopyknits", "…/gifts", True),
                ("🌿", (200, 240, 210), "@sproutsoapco", "…/old-page", False)]
        for i, (em, col, hd, lk, ok) in enumerate(rows):
            lead_row(sub, t, s2 + 2.8 + i * 0.4, 880 + i * 200, em, col, hd, lk, ok, s2 + 4.2 + i * 0.5)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["DM them a free fix.", "Then offer the rest."], t, s3 + 0.1, 260, 80, (WHITE, ACC), gap=0.07, highlight={"free", "fix.", "offer"})
        chat_bubble(sub, t, s3 + 0.9, 560, ["Hi! Your bio link goes to an", "old summer sale page. I made", "you a free gift-links page.", "Want it?"], me=True, color=(20, 120, 130))
        draw_text(sub, "(sample DM)", F_SEMI, 32, W - 130, 740, SOFT, alpha=out_cubic(p(t, s3 + 1.3, 0.4)), anchor="rm")
        offer_card(sub, t, s3 + 2.2, 1060, [("4-button link page", "$30", s3 + 2.8), ("Holiday links swapped in", "incl.", s3 + 3.3)], "$30", ACC, title="Link-in-bio page", h=520)
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 34, W / 2, 1390, SOFT, alpha=out_cubic(p(t, s3 + 4.6, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel1.mp4")
