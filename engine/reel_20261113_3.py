"""5 things to sell before December (10-minute room sweep -> 5 listings, example math)."""
from reel_market import *

ACC = (255, 175, 80)    # amber
GOLD = (255, 214, 92)
bg = Background(top=(36, 16, 6), bottom=(86, 44, 12), blobs=[(220, 120, 40), (255, 175, 80), (180, 60, 60)], seed=3173)
ITEMS = [("🎮", "Old games", (200, 215, 255)), ("🎄", "Holiday decor", (200, 240, 210)), ("🧸", "Kids' toys", (255, 225, 200)),
         ("🪑", "Small furniture", (235, 225, 205)), ("🧰", "Tools", (255, 210, 210))]
POS = [(250, 820), (540, 820), (830, 820), (395, 1110), (685, 1110)]


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["5 things to sell", "before December"], t, -0.3, 400, 106, (WHITE, ACC), gap=0.06, highlight={"5", "december"})
        for i, ((em, lab, col), (x, y)) in enumerate(zip(ITEMS, POS)):
            item_tile(sub, t, 0.5 + i * 0.22, x, y, em, lab, col, size=270)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Do a 10-minute", "room sweep"], t, s1 + 0.1, 290, 90, (WHITE, ACC), gap=0.07, highlight={"10-minute"})
        timer(sub, t, s1 + 0.6, 2.4, W / 2, 500, 10, GOLD)
        checklist(sub, t, s1 + 1.2, ["Not used in a year", "Works + clean", "Easy to pick up"], 660, 110, ACC, size=56, x0=180, every=0.7)
        kq = p(t, s1 + 3.8, 0.4)
        pill(sub, W / 2, 1060, "Start with 1 room", F_XB, 52, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="🚪")
        draw_text(sub, "Holiday decor + toys are in season now.", F_SEMI, 38, W / 2, 1200, SOFT, alpha=out_cubic(p(t, s1 + 4.6, 0.4)))
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["List all 5 tonight"], t, s2 + 0.1, 260, 90, (WHITE, ACC), gap=0.07, highlight={"5", "tonight"})
        listings_panel(sub, t, s2 + 0.5, 380, [
            ("🎮", (200, 215, 255), "Video game bundle", "$40 · example", s2 + 4.0),
            ("🎄", (200, 240, 210), "Holiday decor box", "$25 · example", s2 + 4.7),
            ("🧸", (255, 225, 200), "Toy bundle", "$20 · example", None),
            ("🪑", (235, 225, 205), "IKEA armchair", "$45 · example", s2 + 5.4),
            ("🧰", (255, 210, 210), "Drill + bits", "$30 · example", None),
        ])
        kq = p(t, s2 + 6.0, 0.4)
        pill(sub, W / 2, 1320, "Daylight photos + clear titles", F_XB, 46, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="📸")
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["If all 5 sell", "(example)"], t, s3 + 0.1, 280, 86, (WHITE, ACC), gap=0.07, highlight={"5", "sell"})
        money_counter(sub, t, s3 + 0.6, 160, 620, ACC, label="from stuff you don't use")
        draw_text(sub, "Example prices. Results depend on your items.", F_SEMI, 36, W / 2, 940, SOFT, alpha=out_cubic(p(t, s3 + 3.0, 0.4)))
        kq = p(t, s3 + 3.6, 0.4)
        pill(sub, W / 2, 1090, "Check eBay sold prices first", F_XB, 48, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="🔎")
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel3.mp4")
