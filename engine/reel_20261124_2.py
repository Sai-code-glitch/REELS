"""Your first link-in-bio page: 10 minutes, $0 (free Linktree plan or Instagram's 5 bio links, 4 buttons, test, example offer)."""
from reel_linkbio import *

ACC = (190, 150, 255)
GOLD = (255, 214, 110)
bg = Background(top=(26, 14, 52), bottom=(78, 40, 130), blobs=[(120, 70, 200), (190, 150, 255), (50, 20, 90)], seed=1242)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Your first", "link-in-bio page:", "10 minutes, $0"], t, -0.3, 440, 100, (WHITE, ACC), gap=0.07, highlight={"link-in-bio", "page:", "10", "$0"})
        clock(sub, t, 1.0, 2.0, 830, 10, GOLD)
        for i, (em, lab) in enumerate(BUTTONS[:3]):
            kk = p(t, 1.4 + i * 0.25, 0.4)
            pill(sub, W / 2, 1000 + i * 120, lab, F_XB, 44, WHITE, INK, alpha=out_cubic(kk), scale=out_back(kk), icon=em)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Pick 1 free tool"], t, s1 + 0.1, 300, 88, (WHITE, ACC), gap=0.07, highlight={"free"})
        tool_tile(sub, t, s1 + 0.8, W / 2 - 215, 680, "🌳", "Linktree", "free plan", ACC)
        tool_tile(sub, t, s1 + 1.3, W / 2 + 215, 680, "📸", "Instagram", "up to 5 bio links", ACC)
        draw_text(sub, "Practice on a shop you love.", F_XB, 52, W / 2, 1020, WHITE, alpha=out_cubic(p(t, s1 + 2.6, 0.4)))
        draw_text(sub, "Use their real links.", F_XB, 52, W / 2, 1090, WHITE, alpha=out_cubic(p(t, s1 + 2.9, 0.4)))
        kb = p(t, s1 + 4.0, 0.4)
        pill(sub, W / 2, 1260, "That's your free sample", F_BLACK, 48, GOLD, INK, alpha=out_cubic(kb), scale=out_back(kb), icon="🎁")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Add 4 buttons", "in this order"], t, s2 + 0.1, 250, 80, (WHITE, ACC), gap=0.07, highlight={"4", "order"})
        link_page(sub, t, s2 + 0.6, 390, ACC, [s2 + 1.4, s2 + 2.6, s2 + 3.8, s2 + 5.0])
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Test it, then", "show 1 shop"], t, s3 + 0.1, 260, 84, (WHITE, ACC), gap=0.07, highlight={"test", "show"})
        checklist(sub, t, s3 + 0.8, ["Open it on your phone", "Tap every button", "Swap links each season"], 470, 100, ACC, size=48, every=0.6)
        offer_card(sub, t, s3 + 2.8, 1060, [("4-button link page", "$30", s3 + 3.3), ("Seasonal link swap", "$10", s3 + 3.8)], "$40", ACC, title="Link page offer", h=520)
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 34, W / 2, 1390, SOFT, alpha=out_cubic(p(t, s3 + 5.0, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel2.mp4")
