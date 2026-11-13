"""Search this on eBay before you sell anything (Sold items filter = real price check)."""
from reel_market import *

ACC = (90, 225, 210)    # teal
GOLD = (255, 214, 92)
bg = Background(top=(4, 26, 34), bottom=(8, 62, 70), blobs=[(20, 140, 150), (90, 225, 210), (40, 80, 180)], seed=3171)
SOLD = [("🪑", (230, 220, 200), "IKEA Poäng armchair, beige", "$52", "Sold Nov 9"),
        ("🪑", (220, 210, 190), "IKEA Poäng chair + cushion", "$48", "Sold Nov 8"),
        ("🪑", (235, 225, 205), "Poäng armchair, light wear", "$45", "Sold Nov 6"),
        ("🪑", (225, 215, 195), "IKEA Poäng, like new", "$55", "Sold Nov 3")]


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Search this on eBay", "before you sell", "anything"], t, -0.3, 390, 100, (WHITE, ACC), gap=0.06, highlight={"ebay", "anything"})
        ebay_search(sub, t, 0.4, 760, "ikea poang chair", type_dur=0.8)
        filter_toggle(sub, t, 1.2, 930, 2.0, tap=False)
        sold_row(sub, t, 2.3, 1110, *SOLD[0])
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Most people", "guess the price"], t, s1 + 0.1, 290, 90, (WHITE, ACC), gap=0.07, highlight={"guess"})
        item_tile(sub, t, s1 + 0.6, 330, 680, "🪑", "Same chair", (230, 220, 200), size=360, price=("$120", s1 + 1.0))
        item_tile(sub, t, s1 + 1.2, 750, 680, "🪑", "Same chair", (230, 220, 200), size=360, price=("$10", s1 + 1.6))
        ka = p(t, s1 + 2.3, 0.4)
        pill(sub, 330, 940, "No messages", F_XB, 40, (255, 92, 104), WHITE, alpha=out_cubic(ka), scale=out_back(ka), icon="🦗")
        kb = p(t, s1 + 2.9, 0.4)
        pill(sub, 750, 940, "Gone in 5 min", F_XB, 40, (255, 92, 104), WHITE, alpha=out_cubic(kb), scale=out_back(kb), icon="💸")
        draw_text(sub, "Too high = ignored. Too low = money lost.", F_XB, 44, W / 2, 1100, WHITE, alpha=out_cubic(p(t, s1 + 3.8, 0.4)))
        kq = p(t, s1 + 4.8, 0.4)
        pill(sub, W / 2, 1260, "Check real sold prices", F_XB, 52, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="🔎")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Filter → Sold items"], t, s2 + 0.1, 270, 86, (WHITE, ACC), gap=0.07, highlight={"sold", "items"})
        ebay_search(sub, t, s2 + 0.4, 440, "ikea poang chair", type_dur=0.5)
        filter_toggle(sub, t, s2 + 0.9, 610, s2 + 1.9)
        for i, row in enumerate(SOLD):
            sold_row(sub, t, s2 + 2.4 + i * 0.55, 800 + i * 185, *row)
        kq = p(t, s2 + 5.0, 0.4)
        pill(sub, W / 2, 1510, "Green = what buyers paid", F_XB, 46, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="✅")
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["10-second math", "(example)"], t, s3 + 0.1, 280, 86, (WHITE, ACC), gap=0.07, highlight={"math"})
        for i, pr in enumerate(["$52", "$48", "$45", "$55"]):
            kk = p(t, s3 + 0.6 + i * 0.25, 0.35)
            pill(sub, 225 + i * 210, 470, pr, F_BLACK, 50, WHITE, SOLD_G, alpha=out_cubic(kk), scale=out_back(kk))
        money_counter(sub, t, s3 + 1.8, 50, 720, ACC, label="average sold price")
        kq = p(t, s3 + 4.2, 0.4)
        pill(sub, W / 2, 1060, "List at about $45 to sell fast", F_XB, 50, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="🏷️")
        draw_text(sub, "Example numbers. Results depend on your item.", F_SEMI, 36, W / 2, 1190, SOFT, alpha=out_cubic(p(t, s3 + 4.8, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel1.mp4")
