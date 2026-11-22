"""Find 3 typos on 1 shop's site tonight (proofreading gig: where typos hide -> read aloud + circle -> free fix DM + example offer)."""
from reel_proof import *

ACC = (60, 220, 190)
GOLD = (255, 214, 92)
bg = Background(top=(6, 34, 40), bottom=(12, 84, 82), blobs=[(20, 140, 130), (60, 220, 190), (10, 70, 90)], seed=1221)

LINES = ["{Free shiping|Free shipping} on orders $50+",
         "Order by Dec 15 for {Chrismas|Christmas}",
         "Our {2025|2026} holiday sale is live!"]


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Find 3 typos on", "1 shop's site", "tonight"], t, -0.3, 330, 108, (WHITE, ACC), gap=0.06, highlight={"3", "typos", "tonight"})
        site_page(sub, t, 0.4, 640, LINES, [(1.0, None), (1.4, None), (1.8, None)], h=880)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Small shops write", "their own websites"], t, s1 + 0.1, 290, 86, (WHITE, ACC), gap=0.07, highlight={"own"})
        draw_text(sub, "Typos hide in:", F_XB, 50, W / 2, 470, SOFT, alpha=out_cubic(p(t, s1 + 0.7, 0.4)))
        rows = [("🏠", "The homepage banner"), ("📦", "The shipping page"), ("🏷️", "Product titles"), ("📅", "Old dates like \"2025\"")]
        for i, (em, lab) in enumerate(rows):
            kk = p(t, s1 + 1.0 + i * 0.6, 0.4)
            if kk <= 0: continue
            y = 590 + i * 130
            x = 150 + 60 * (1 - out_cubic(kk))
            place_emoji(sub, em, x, y, 72 * out_back(kk), alpha=out_cubic(kk))
            draw_text(sub, lab, F_XB, 54, x + 66, y, WHITE, alpha=out_cubic(kk), anchor="lm")
        kb = p(t, s1 + 4.0, 0.4)
        pill(sub, W / 2, 1200, "Owners read past their own typos", F_BLACK, 44, GOLD, INK, alpha=out_cubic(kb), scale=out_back(kb), icon="👀")
        draw_text(sub, "Fresh eyes catch them.", F_XB, 50, W / 2, 1320, WHITE, alpha=out_cubic(p(t, s1 + 4.8, 0.4)))
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Read every line", "out loud. Slowly."], t, s2 + 0.1, 250, 88, (WHITE, ACC), gap=0.07, highlight={"out", "loud.", "slowly."})
        site_page(sub, t, s2 + 0.5, 430, LINES,
                  [(s2 + 1.4, s2 + 2.4), (s2 + 2.9, s2 + 3.9), (s2 + 4.4, s2 + 5.4)], h=880)
        kb = p(t, s2 + 5.9, 0.4)
        pill(sub, W / 2, 1420, "Circle it. Write the fix.", F_BLACK, 48, ACC, INK, alpha=out_cubic(kb), scale=out_back(kb), icon="✍️")
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Send 1 free fix,", "then offer the rest"], t, s3 + 0.1, 260, 84, (WHITE, ACC), gap=0.07, highlight={"free", "offer"})
        chat_bubble(sub, t, s3 + 0.9, 600, ["Hi! Love your candles.", "I spotted 3 small typos", "on your site. Here they", "are, free. Want me to", "check every page?"], me=True, color=(40, 120, 230))
        draw_text(sub, "(sample DM)", F_SEMI, 32, W - 130, 800, SOFT, alpha=out_cubic(p(t, s3 + 1.3, 0.4)), anchor="rm")
        offer_card(sub, t, s3 + 2.2, 1100, [("Full-site typo check", "$30", s3 + 2.8), ("Fix list (PDF)", "incl.", s3 + 3.3)], "$30", ACC, title="Typo check", h=520)
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 34, W / 2, 1420, SOFT, alpha=out_cubic(p(t, s3 + 4.6, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel1.mp4")
