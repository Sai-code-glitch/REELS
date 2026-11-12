"""Check 1 café's Instagram tonight (lead search + 3-line DM for the holiday menu gig)."""
from reel_menu import *

ACC = (190, 150, 255)   # lavender
GOLD = (255, 214, 92)
bg = Background(top=(16, 8, 40), bottom=(40, 20, 84), blobs=[(110, 60, 220), (190, 150, 255), (60, 140, 200)], seed=3163)
ROWS = [
    ("☕", (250, 214, 165), "@beanandbell", "blurry board photo", False),
    ("🥐", (220, 200, 180), "@northcup", "clean graphic", True),
    ("🍁", (245, 190, 140), "@mapleroast", "no prices", False),
    ("🫖", (200, 230, 200), "@dripdropcafe", "last year's", False),
]


def rows(sub, t, start, y0, items, every, flag_delay, step=190):
    for i, (em, col, h, lab, good) in enumerate(items):
        st = start + i * every
        cafe_row(sub, t, st, y0 + i * step, em, col, h, lab, good, st + flag_delay)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Check 1 café's", "Instagram tonight"], t, -0.3, 360, 108, (WHITE, ACC), gap=0.06, highlight={"instagram", "tonight"})
        ig_search(sub, t, 0.5, 620, "coffee + your town", type_dur=0.9)
        rows(sub, t, 1.5, 820, ROWS[:2], 0.3, 0.8)
        kx = p(t, 2.7, 0.35)
        pill(sub, W / 2, 1230, "Blurry menu = lead", F_XB, 50, GOLD, INK, alpha=out_cubic(kx), scale=out_back(kx), icon="👀")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Find their latest", "menu post"], t, s1 + 0.1, 280, 86, (WHITE, ACC), gap=0.07, highlight={"menu"})
        rows(sub, t, s1 + 0.6, 520, ROWS, 0.55, 0.7)
        kx = p(t, s1 + 4.2, 0.4)
        pill(sub, W / 2, 1390, "Pick the ones flagged LEAD", F_XB, 50, GOLD, INK, alpha=out_cubic(kx), scale=out_back(kx), icon="🎯")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Send this DM"], t, s2 + 0.1, 250, 90, (WHITE, ACC), gap=0.07, highlight={"dm"})
        phone_chat(sub, t, s2 + 0.6, W / 2, 360, [
            ("me", "Hi! Your peppermint mocha looks so good.", s2 + 1.1, None),
            ("me", "I turned your holiday drinks into a clean menu post. Free, it's attached.", s2 + 2.2, None),
            ("me", "Want a story + print size too?", s2 + 3.6, "Sent"),
        ], header="Bean & Bell", h=980)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["If they say yes", "(example)"], t, s3 + 0.1, 280, 86, (WHITE, ACC), gap=0.07, highlight={"yes"})
        offer_card(sub, t, s3 + 0.6, 760, [
            ("1 menu post", "Free", s3 + 1.1),
            ("Story + print size", "$25", s3 + 1.7),
        ], "$25", ACC, title="Holiday menu set", h=560)
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 34, W / 2, 1110, SOFT, alpha=out_cubic(p(t, s3 + 3.0, 0.4)))
        kq = p(t, s3 + 3.8, 0.4)
        pill(sub, W / 2, 1260, "DM 3 cafés tonight", F_XB, 50, WHITE, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="🌙")
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel3.mp4")
