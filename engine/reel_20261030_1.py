"""Black Friday is 28 days away. Sell shops this 1 button (online gift cards)."""
from reel_giftcard import *

ACC = (60, 220, 160)    # mint
GOLD = (255, 214, 92)
bg = Background(top=(6, 34, 36), bottom=(10, 70, 60), blobs=[(30, 160, 120), (40, 110, 200), (220, 180, 60)], seed=3031)
NAV = ["Home", "Shop", "About"]


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Black Friday is", "28 days away"], t, -0.3, 520, 112, (WHITE, ACC), gap=0.06, highlight={"28", "days"})
        kp = p(t, 0.7, 0.35)
        pill(sub, W / 2, 730, "Sell shops this 1 button", F_XB, 54, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="👇")
        browser(sub, t, 1.0, 860, "rosasbakery.com", "Rosa's Bakery", "🧁", (255, 205, 215), NAV, add_at=1.9, h=640)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Many small shops sell", "gift cards only in store"], t, s1 + 0.1, 320, 70, (WHITE, ACC), gap=0.07, highlight={"only", "store"})
        browser(sub, t, s1 + 0.7, 450, "rosasbakery.com", "Rosa's Bakery", "🧁", (255, 205, 215), NAV, find=("gift card", s1 + 1.6, False), h=640)
        night_clock(sub, t, s1 + 3.6, 1250)
        kx = p(t, s1 + 4.6, 0.4)
        pill(sub, W / 2, 1440, "Late gift shoppers can't buy", F_XB, 48, GOLD, INK, alpha=out_cubic(kx), scale=out_back(kx), icon="🛒")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Set up online", "gift cards for them"], t, s2 + 0.1, 300, 84, (WHITE, ACC), gap=0.07, highlight={"online", "gift"})
        checklist(sub, t, s2 + 0.8, ["Check their shop tool", "Turn on e-gift cards", "Add a menu button", "Make 1 promo post"], 500, 105, ACC, size=52, x0=150, every=0.6)
        gift_card(sub, t, s2 + 3.6, W / 2, 1200, "Rosa's Bakery", "$50", (230, 80, 120), "🧁", rot=-4)
        kq = p(t, s2 + 5.0, 0.4)
        pill(sub, W / 2, 1490, "e.g. Square, Shopify, Wix", F_XB, 44, WHITE, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="🛠️")
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Sell it as a", "small holiday package"], t, s3 + 0.1, 300, 84, (WHITE, GOLD), gap=0.07, highlight={"package"})
        offer_card(sub, t, s3 + 0.6, 760, [
            ("E-gift cards turned on", "$60", s3 + 1.2),
            ("Gift cards menu button", "$20", s3 + 1.8),
            ("1 promo post design", "$20", s3 + 2.4),
        ], "$100", ACC, title="Holiday gift card setup", h=620)
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 36, W / 2, 1140, SOFT, alpha=out_cubic(p(t, s3 + 3.8, 0.4)))
        kq = p(t, s3 + 4.4, 0.4)
        pill(sub, W / 2, 1290, "Ask for staff access, never passwords", F_XB, 40, WHITE, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="🔑")
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel1.mp4")
