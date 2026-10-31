"""Check 1 shop's Google reviews tonight (lead search + 3-line DM + example kit)."""
from reel_reviews import *

ACC = (255, 150, 60)    # orange
GOLD = (255, 214, 92)
bg = Background(top=(4, 30, 22), bottom=(10, 64, 44), blobs=[(30, 150, 90), (240, 140, 50), (40, 120, 160)], seed=3043)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Check 1 shop's", "Google reviews", "tonight"], t, -0.3, 500, 112, (WHITE, ACC), gap=0.06, highlight={"Google", "reviews"})
        kp = p(t, 0.8, 0.35)
        pill(sub, W / 2, 810, "It can be your first gig", F_XB, 50, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="💡")
        review_row(sub, t, 1.1, 1080, "🍝", (200, 70, 50), "Nonna's Kitchen", "4.8", "9", "7 months ago", 1.8, True)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Look for great ratings", "but few reviews"], t, s1 + 0.1, 300, 72, (WHITE, ACC), gap=0.07, highlight={"few", "reviews"})
        review_row(sub, t, s1 + 0.7, 540, "🍕", (230, 120, 40), "Slice House", "4.5", "486", "1 day ago", s1 + 2.2, False)
        review_row(sub, t, s1 + 1.0, 770, "🍝", (200, 70, 50), "Nonna's Kitchen", "4.8", "9", "7 months ago", s1 + 2.6, True)
        review_row(sub, t, s1 + 1.3, 1000, "✂️", (90, 110, 220), "Fade Lab Barbers", "5.0", "14", "4 months ago", s1 + 3.0, True)
        kx = p(t, s1 + 4.2, 0.4)
        pill(sub, W / 2, 1220, "Under 30 reviews = a lead", F_XB, 50, GOLD, INK, alpha=out_cubic(kx), scale=out_back(kx), icon="🎯")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Send a 3-line DM"], t, s2 + 0.1, 290, 88, (WHITE, ACC), gap=0.07, highlight={"3-line"})
        phone_chat(sub, t, s2 + 0.6, W / 2, 400, [
            ("me", "Hi! Your pasta reviews are all 5 stars.", s2 + 1.2, None),
            ("me", "I make QR cards so happy guests can review you in 1 scan.", s2 + 2.4, None),
            ("me", "Want a free sample card with your link?", s2 + 3.8, "Sent"),
        ], header="Nonna's Kitchen", h=960)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Sample first,", "then the price"], t, s3 + 0.1, 290, 88, (WHITE, ACC), gap=0.07, highlight={"Sample", "first,"})
        table_card(sub, t, s3 + 0.6, 300, 800, "Nonna's", "🍝", (200, 70, 50), w=360, h=504, rot=-4, seed=23)
        k2 = p(t, s3 + 1.4, 0.45)
        if k2 > 0:
            draw_text(sub, "Example price", F_XB, 40, 740, 690, SOFT, alpha=out_cubic(k2))
            draw_text(sub, "$40", F_BLACK, 170, 740, 820, GOLD, alpha=out_cubic(k2), scale=0.7 + 0.3 * out_back(k2))
            draw_text(sub, "card + QR + PDF", F_XB, 40, 740, 950, WHITE, alpha=out_cubic(k2))
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 36, W / 2, 1160, SOFT, alpha=out_cubic(p(t, s3 + 2.6, 0.4)))
        kq = p(t, s3 + 3.4, 0.4)
        pill(sub, W / 2, 1300, "Never offer rewards for reviews", F_XB, 42, WHITE, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="🚫")
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel3.mp4")
