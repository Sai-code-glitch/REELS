"""Search this on Etsy tonight (find long, messy titles -> pitch via the shop's Instagram)."""
from reel_etsy import *

ACC = (190, 150, 255)   # lavender
GOLD = (255, 214, 92)
bg = Background(top=(14, 8, 38), bottom=(38, 20, 86), blobs=[(110, 60, 220), (190, 150, 255), (220, 80, 160)], seed=3153)
ROWS = [
    ("🎄", (214, 240, 226), "Ornament Christmas Ornament Gift Personalized Ornament Best Christmas Gift 2026 Ornament Family Ornament Tree Decor Gift Idea"),
    ("🔴", (255, 226, 226), "Hand Painted Glass Bauble, Red, 3 inch"),
    ("☕", (240, 228, 214), "Mug Gift Christmas Mug Funny Mug Best Mug Gift for Dad Coffee Mug Dad Gift Mug Holiday"),
    ("⭐", (250, 244, 220), "Wool Felt Garland, Cream Stars, 6 ft"),
]


def rows(sub, t, start, top, items, every, flag_after, step=232):
    for i, (e, col, title) in enumerate(items):
        result_row(sub, t, start + i * every, top + i * step, e, col, title, len(title.split()), start + i * every + flag_after)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Search this", "on Etsy tonight"], t, -0.3, 360, 116, (WHITE, ACC), gap=0.06, highlight={"etsy", "tonight"})
        etsy_search(sub, t, 0.5, 600, "christmas ornament", type_dur=0.9)
        rows(sub, t, 1.5, 800, ROWS[:2], 0.3, 0.8)
        kx = p(t, 2.7, 0.35)
        pill(sub, W / 2, 1250, "Long, messy titles = leads", F_XB, 50, GOLD, INK, alpha=out_cubic(kx), scale=out_back(kx), icon="👀")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Count the words", "in each title"], t, s1 + 0.1, 280, 86, (WHITE, ACC), gap=0.07, highlight={"count", "words"})
        rows(sub, t, s1 + 0.6, 500, ROWS, 0.55, 0.7)
        kx = p(t, s1 + 4.2, 0.4)
        pill(sub, W / 2, 1390, "Etsy's tip: under 15 words", F_XB, 50, GOLD, INK, alpha=out_cubic(kx), scale=out_back(kx), icon="📏")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Where to pitch"], t, s2 + 0.1, 250, 86, (WHITE, ACC), gap=0.07, highlight={"pitch"})
        k1 = p(t, s2 + 0.5, 0.35)
        pill(sub, W / 2, 390, "Etsy messages", F_XB, 48, (255, 120, 120), INK, alpha=out_cubic(k1), scale=out_back(k1), icon="🚫")
        if t >= s2 + 1.0:
            strike(sub, t, s2 + 1.0, W / 2 - 230, W / 2 + 230, 395, (255, 255, 255), width=10)
        k2 = p(t, s2 + 1.4, 0.35)
        pill(sub, W / 2, 510, "Their Instagram (shop page)", F_XB, 48, (120, 230, 160), INK, alpha=out_cubic(k2), scale=out_back(k2), icon="✅")
        phone_chat(sub, t, s2 + 2.0, W / 2, 620, [
            ("me", "Hi! Love your ceramic ornaments.", s2 + 2.5, None),
            ("me", "I rewrote 1 of your Etsy titles to be shorter and clearer. Free, it's attached.", s2 + 3.4, None),
            ("me", "Want me to do 10 more before Black Friday?", s2 + 4.6, "Sent"),
        ], header="Kiln & Co", h=900)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["If they say yes", "(example)"], t, s3 + 0.1, 280, 86, (WHITE, ACC), gap=0.07, highlight={"yes"})
        offer_card(sub, t, s3 + 0.6, 760, [
            ("1 sample title", "Free", s3 + 1.1),
            ("10 more titles", "$30", s3 + 1.7),
        ], "$30", ACC, title="Etsy title refresh", h=560)
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 34, W / 2, 1110, SOFT, alpha=out_cubic(p(t, s3 + 3.0, 0.4)))
        kq = p(t, s3 + 3.8, 0.4)
        pill(sub, W / 2, 1260, "Pitch 3 shops tonight", F_XB, 50, WHITE, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="🌙")
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel3.mp4")
