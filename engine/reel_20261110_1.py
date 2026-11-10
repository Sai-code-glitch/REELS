"""Online shops need this 1 banner before Dec 17 (holiday 'order by' cutoff banner gig)."""
from reel_shipby import *

ACC = (255, 110, 110)   # berry coral
GOLD = (255, 214, 92)
bg = Background(top=(4, 30, 22), bottom=(10, 70, 50), blobs=[(30, 160, 100), (220, 60, 80), (80, 200, 160)], seed=3141)
SITE = dict(url="oakandwick.shop", shop="Oak & Wick", emoji="🕯️", color=(250, 220, 180))
DMS = [("Jess", "Will it arrive by Christmas?"), ("Mark", "Do you ship in time for the 25th?"),
       ("Priya", "Last day to order??"), ("Tom", "Is it too late for Xmas?"), ("Ana", "When do I need to order by?")]


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Online shops need", "this 1 banner", "before Dec 17"], t, -0.3, 400, 104, (WHITE, ACC), gap=0.06, highlight={"banner", "dec", "17"})
        kp = p(t, 0.7, 0.35)
        pill(sub, W / 2, 690, "USPS Ground: ship by Dec 17", F_XB, 48, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="📦")
        shop_site(sub, t, 0.9, 820, bar_at=1.5, h=640, **SITE)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Without it, shops", "get this all day"], t, s1 + 0.1, 290, 84, (WHITE, ACC), gap=0.07, highlight={"all", "day"})
        dm_pile(sub, t, s1 + 0.8, 520, DMS, every=0.55)
        kx = p(t, s1 + 4.0, 0.4)
        pill(sub, W / 2, 1300, "Same question, over and over", F_XB, 50, GOLD, INK, alpha=out_cubic(kx), scale=out_back(kx), icon="😩")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["The fix: 1 line,", "3 places"], t, s2 + 0.1, 280, 88, (WHITE, ACC), gap=0.07, highlight={"1", "line,", "3"})
        shop_site(sub, t, s2 + 0.5, 410, bar_at=s2 + 1.0, type_bar=True, h=520, **SITE)
        checklist(sub, t, s2 + 2.8, ["Top of their website", "An Instagram story", "A pinned post"], 1060, 115, ACC, size=52, x0=150, every=0.7)
        kq = p(t, s2 + 5.4, 0.4)
        pill(sub, W / 2, 1450, "Customers stop guessing", F_XB, 48, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="✅")
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["What to charge", "(example)"], t, s3 + 0.1, 280, 86, (WHITE, ACC), gap=0.07, highlight={"charge"})
        offer_card(sub, t, s3 + 0.6, 760, [
            ("Website cutoff banner", "$20", s3 + 1.1),
            ("Story + post graphic", "$20", s3 + 1.7),
        ], "$40", ACC, title="Holiday 'order by' set", h=560)
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 34, W / 2, 1110, SOFT, alpha=out_cubic(p(t, s3 + 3.0, 0.4)))
        kq = p(t, s3 + 3.8, 0.4)
        pill(sub, W / 2, 1260, "Use the shop's real cutoff date", F_XB, 46, WHITE, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="📅")
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel1.mp4")
