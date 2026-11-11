"""Stop writing Etsy titles like this (Etsy listing-title rewrite gig)."""
from reel_etsy import *

ACC = (255, 150, 70)    # Etsy-ish orange
GOLD = (255, 214, 92)
bg = Background(top=(36, 14, 8), bottom=(80, 32, 14), blobs=[(200, 80, 30), (240, 140, 60), (150, 40, 60)], seed=3151)
BAD = "Candle Gift for Her Christmas Gift Candle Best Gift Perfect Candle Mom Gift Holiday Candle Soy Candle Free Shipping"
BAD_IDX = {5, 6, 7, 8, 9, 10, 12, 14, 16, 17, 18}
GOOD = "Soy Candle, Pine and Cedar Scent, 8 oz Amber Glass Jar"
LIST = dict(price="$24.00", shop="PineHollowCo · Etsy shop", emoji="🕯️", color=(250, 226, 190))


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Stop writing", "Etsy titles", "like this"], t, -0.3, 380, 112, (WHITE, ACC), gap=0.06, highlight={"etsy", "titles"})
        etsy_listing(sub, t, 0.6, 650, BAD, size=38, photo_h=260, bad=BAD_IDX, bad_at=1.5, **LIST)
        kx = p(t, 2.1, 0.35)
        place_emoji(sub, "❌", 880, 700, 150 * out_back(kx), alpha=out_cubic(kx), rot=-10)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Etsy's own tip:", "keep it short"], t, s1 + 0.1, 290, 86, (WHITE, ACC), gap=0.07, highlight={"short"})
        word_meter(sub, t, s1 + 0.7, W / 2, 520, 19, dur=1.2)
        checklist(sub, t, s1 + 2.0, ["Same word 4 times", "“Best”, “Perfect”", "“Free Shipping”"], 700, 115, ACC, size=56, x0=170, every=0.7, icon="❌")
        kx = p(t, s1 + 4.4, 0.4)
        pill(sub, W / 2, 1080, "Say what it is, first", F_XB, 54, GOLD, INK, alpha=out_cubic(kx), scale=out_back(kx), icon="🎯")
        draw_text(sub, "Etsy adds shipping info for you", F_SEMI, 38, W / 2, 1200, SOFT, alpha=out_cubic(p(t, s1 + 5.0, 0.4)))
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["The fix:", "1 simple formula"], t, s2 + 0.1, 280, 86, (WHITE, ACC), gap=0.07, highlight={"formula"})
        formula_rows(sub, t, s2 + 0.6, 410, [
            ("🕯️", "What it is", "Soy Candle"),
            ("🌲", "Scent / color", "Pine & Cedar"),
            ("📏", "Size", "8 oz"),
            ("🫙", "Material", "Amber Glass Jar"),
        ], ACC, every=0.55)
        title_box(sub, t, s2 + 3.0, 930, GOOD, 1.6, ACC)
        kq = p(t, s2 + 5.4, 0.4)
        pill(sub, W / 2, 1400, "“Gift for her” goes in tags", F_XB, 50, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="🏷️")
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Sell it as a gig", "(example)"], t, s3 + 0.1, 280, 86, (WHITE, ACC), gap=0.07, highlight={"gig"})
        offer_card(sub, t, s3 + 0.6, 760, [
            ("10 titles rewritten", "$30", s3 + 1.1),
            ("13 tags per listing", "$20", s3 + 1.7),
        ], "$50", ACC, title="Holiday Etsy title refresh", h=560)
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 34, W / 2, 1110, SOFT, alpha=out_cubic(p(t, s3 + 3.0, 0.4)))
        kq = p(t, s3 + 3.8, 0.4)
        pill(sub, W / 2, 1260, "Before Black Friday traffic", F_XB, 48, WHITE, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="🛍️")
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel1.mp4")
