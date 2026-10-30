"""Search "gift card" on 1 shop's site tonight: find shops with no online gift cards."""
from reel_giftcard import *

ACC = (255, 150, 60)    # orange
GOLD = (255, 214, 92)
bg = Background(top=(10, 14, 44), bottom=(30, 30, 90), blobs=[(60, 80, 220), (240, 120, 50), (150, 60, 200)], seed=3032)
NAV = ["Home", "Menu", "Visit"]


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, -0.2, 0.3)
        place_emoji(sub, "🔎", W / 2, 340 - 14 * math.sin(t * 6), 160 * out_back(k), alpha=k)
        pop_words(sub, ["Search “gift card”", "on 1 shop's site", "tonight"], t, -0.3, 620, 100, (WHITE, ACC), gap=0.05, highlight={"“gift", "card”", "tonight"})
        browser(sub, t, 1.0, 860, "knitandco.shop", "Knit & Co", "🧶", (200, 220, 255), NAV, find=("gift card", 1.3, False), h=640)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["0 results means", "no 11pm gift buyers"], t, s1 + 0.1, 320, 80, (WHITE, ACC), gap=0.07, highlight={"0", "results", "11pm"})
        night_clock(sub, t, s1 + 0.9, 560)
        notification(sub, t, s1 + 1.8, 800, "Reminders", "Sam's party tomorrow", "Still need a gift!", (255, 200, 80), icon="🎉")
        kx = p(t, s1 + 3.2, 0.4)
        pill(sub, W / 2, 1020, "They search... and leave", F_XB, 50, GOLD, INK, alpha=out_cubic(kx), scale=out_back(kx), icon="🚪")
        ky = p(t, s1 + 4.4, 0.4)
        pop_words(sub, ["That shop is", "your next lead"], t, s1 + 4.4, 1270, 84, (WHITE, ACC), gap=0.07, highlight={"lead"})
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Check 3 local sites", "with Ctrl+F"], t, s2 + 0.1, 300, 84, (WHITE, ACC), gap=0.07, highlight={"ctrl+f", "3"})
        rows = [("🧁", (255, 205, 215), "rosasbakery.com", False),
                ("🕯️", (250, 214, 165), "oakwick.com", True),
                ("🧶", (200, 220, 255), "knitandco.shop", False)]
        for i, (e, col, site, has) in enumerate(rows):
            site_row(sub, t, s2 + 0.9 + i * 0.5, 540 + i * 200, e, col, site, has, s2 + 2.6 + i * 0.6)
        kq = p(t, s2 + 4.8, 0.4)
        pill(sub, W / 2, 1220, "0 results = write it down", F_XB, 50, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="📝")
        kr = p(t, s2 + 5.6, 0.4)
        pill(sub, W / 2, 1360, "On phone: browser menu › Find", F_XB, 40, WHITE, INK, alpha=out_cubic(kr), scale=out_back(kr), icon="📱")
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Then offer to", "set it up for them"], t, s3 + 0.1, 300, 84, (WHITE, GOLD), gap=0.07, highlight={"set", "up"})
        gift_card(sub, t, s3 + 0.7, W / 2, 610, "Rosa's Bakery", "$25", (90, 110, 240), "🧁", w=600, h=330, rot=3)
        offer_card(sub, t, s3 + 1.6, 1110, [
            ("Online gift cards on", "$60", s3 + 2.1),
            ("Menu button + 1 post", "$40", s3 + 2.6),
        ], "$100", ACC, title="Gift card setup", h=580)
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 36, W / 2, 1460, SOFT, alpha=out_cubic(p(t, s3 + 4.2, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel2.mp4")
