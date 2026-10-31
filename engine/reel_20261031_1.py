"""Small Business Saturday is Nov 28. Shops need this 1 card (Google review QR card gig)."""
from reel_reviews import *

ACC = (255, 200, 60)    # amber
GOLD = (120, 200, 255)
bg = Background(top=(8, 16, 44), bottom=(20, 40, 96), blobs=[(40, 80, 200), (230, 170, 40), (90, 50, 180)], seed=3041)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Small Business", "Saturday is Nov 28"], t, -0.3, 470, 108, (WHITE, ACC), gap=0.06, highlight={"Nov", "28"})
        kp = p(t, 0.7, 0.35)
        pill(sub, W / 2, 680, "Shops need this 1 card", F_XB, 54, ACC, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="👇")
        table_card(sub, t, 1.0, W / 2, 1120, "Rosa's Bakery", "🧁", (220, 80, 120), w=540, h=756, rot=-4)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Happy shoppers leave", "without a review"], t, s1 + 0.1, 320, 74, (WHITE, ACC), gap=0.07, highlight={"without"})
        review_row(sub, t, s1 + 0.8, 600, "☕", (120, 80, 50), "Main St Coffee", "4.6", "312", "2 days ago", s1 + 2.0, False)
        review_row(sub, t, s1 + 1.3, 840, "🧁", (220, 80, 120), "Rosa's Bakery", "4.9", "11", "5 months ago", s1 + 2.6, True)
        kx = p(t, s1 + 3.8, 0.4)
        pill(sub, W / 2, 1060, "Shoppers compare reviews", F_XB, 50, WHITE, INK, alpha=out_cubic(kx), scale=out_back(kx), icon="👀")
        pop_words(sub, ["Most shops just", "never ask"], t, s1 + 4.8, 1260, 70, (WHITE, GOLD), gap=0.07, highlight={"never", "ask"})
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Make them a", "review QR card"], t, s2 + 0.1, 300, 88, (WHITE, ACC), gap=0.07, highlight={"QR", "card"})
        checklist(sub, t, s2 + 0.8, ["Copy their review link", "Turn it into a QR code", "Design a counter card", "Print it for the register"], 500, 100, ACC, size=50, x0=140, every=0.6)
        table_card(sub, t, s2 + 3.4, W / 2, 1225, "Rosa's Bakery", "🧁", (220, 80, 120), w=430, h=602, rot=3)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Sell it as a", "holiday review kit"], t, s3 + 0.1, 300, 84, (WHITE, ACC), gap=0.07, highlight={"review", "kit"})
        offer_card(sub, t, s3 + 0.6, 760, [
            ("Review link + QR code", "$15", s3 + 1.2),
            ("Counter card design", "$35", s3 + 1.8),
            ("Receipt-size version", "$20", s3 + 2.4),
        ], "$70", ACC, title="Holiday review card kit", h=620)
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 36, W / 2, 1140, SOFT, alpha=out_cubic(p(t, s3 + 3.8, 0.4)))
        kq = p(t, s3 + 4.4, 0.4)
        pill(sub, W / 2, 1290, "Never offer rewards for reviews", F_XB, 42, WHITE, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="🚫")
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel1.mp4")
