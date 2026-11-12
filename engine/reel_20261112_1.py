"""Cafés pay for this 1 menu before December (holiday drink menu gig)."""
from reel_menu import *

ACC = (255, 120, 110)   # candy red
GOLD = (255, 214, 92)
bg = Background(top=(40, 10, 14), bottom=(86, 22, 30), blobs=[(200, 50, 60), (240, 120, 90), (120, 30, 70)], seed=3161)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Cafés pay for", "this 1 menu", "before December"], t, -0.3, 400, 104, (WHITE, ACC), gap=0.06, highlight={"1", "menu"})
        menu_card(sub, t, 0.5, W / 2, 1150, ACC, w=500, rot=-3)
        kx = p(t, 2.0, 0.35)
        place_emoji(sub, "☕", 880, 860, 140 * out_back(kx), alpha=out_cubic(kx), rot=12)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Most cafés post", "this instead"], t, s1 + 0.1, 280, 86, (WHITE, ACC), gap=0.07, highlight={"this"})
        chalk_photo(sub, t, s1 + 0.6, W / 2, 900, w=600, h=700, flag_at=s1 + 2.0)
        kq = p(t, s1 + 4.6, 0.4)
        pill(sub, W / 2, 1450, "Customers scroll past it", F_XB, 50, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="👀")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["A menu that works:", "4 parts"], t, s2 + 0.1, 250, 84, (WHITE, ACC), gap=0.07, highlight={"4", "parts"})
        st = [s2 + 0.8, s2 + 1.4, s2 + 2.4, s2 + 3.6, s2 + 4.6]
        checklist(sub, t, s2 + 1.4, ["Big clear title", "5 drinks, max", "Prices lined up", "1 “NEW” badge"], 420, 92, ACC, size=52, x0=170, every=1.05)
        menu_card(sub, t, s2 + 0.6, W / 2, 1190, ACC, w=470, steps=st)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Sell it as a gig", "(example)"], t, s3 + 0.1, 280, 86, (WHITE, ACC), gap=0.07, highlight={"gig"})
        offer_card(sub, t, s3 + 0.6, 760, [
            ("Menu post (4:5)", "$40", s3 + 1.1),
            ("Story + print size", "$25", s3 + 1.7),
        ], "$65", ACC, title="Holiday drink menu", h=560)
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 34, W / 2, 1110, SOFT, alpha=out_cubic(p(t, s3 + 3.0, 0.4)))
        kq = p(t, s3 + 3.8, 0.4)
        pill(sub, W / 2, 1260, "Use their real drinks + prices", F_XB, 46, WHITE, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="✅")
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel1.mp4")
