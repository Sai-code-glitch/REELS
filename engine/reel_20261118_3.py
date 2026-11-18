"""Why do shops pay for 1 page of colors? (consistency, messy -> on-brand grid, example pricing)."""
from reel_brand import *

ACC = (255, 150, 90)    # warm orange
GOLD = (255, 214, 92)
bg = Background(top=(40, 12, 10), bottom=(86, 30, 22), blobs=[(150, 50, 30), (255, 150, 90), (120, 40, 90)], seed=3223)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Why do shops pay", "for 1 page", "of colors?"], t, -0.3, 380, 100, (WHITE, ACC), gap=0.06, highlight={"pay", "1", "colors?"})
        guide_card(sub, t, 0.6, W / 2, 1190, w=460, rot=-4)
        kp = p(t, 1.3, 0.4)
        pill(sub, W / 2 + 250, 960, "$60", F_BLACK, 64, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="🏷️")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Because it saves them…"], t, s1 + 0.1, 290, 80, (WHITE, ACC), gap=0.07, highlight={"saves"})
        checklist(sub, t, s1 + 0.8, ["Guessing colors every post", "Re-explaining to helpers", "A feed that looks random"], 480, 150, ACC, size=50, x0=130, every=0.9)
        kb = p(t, s1 + 4.0, 0.4)
        pill(sub, W / 2, 1050, "You sell consistency", F_XB, 54, GOLD, INK, alpha=out_cubic(kb), scale=out_back(kb), icon="🎯")
        draw_text(sub, "Busy season = more posts to make", F_SEMI, 42, W / 2, 1175, SOFT, alpha=out_cubic(p(t, s1 + 4.8, 0.4)))
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Same feed, 1 guide"], t, s2 + 0.1, 270, 88, (WHITE, ACC), gap=0.07, highlight={"1", "guide"})
        kl = p(t, s2 + 0.6, 0.3)
        pill(sub, W / 2, 420, "BEFORE", F_BLACK, 44, RED2, WHITE, alpha=out_cubic(kl) * (1 - p(t, s2 + 3.6, 0.2)))
        ka = p(t, s2 + 3.8, 0.3)
        pill(sub, W / 2, 420, "AFTER", F_BLACK, 44, OKG, WHITE, alpha=out_cubic(ka), scale=out_back(ka))
        ig_grid(sub, t, s2 + 0.4, 1000, w=760, consistent_at=s2 + 3.6)
        draw_text(sub, "Sample account, fictional shop", F_SEMI, 34, W / 2, 1520, SOFT, alpha=out_cubic(p(t, s2 + 5.0, 0.4)))
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Example pricing"], t, s3 + 0.1, 270, 84, (WHITE, ACC), gap=0.07, highlight={"pricing"})
        rows = [("1-page brand guide", "$60", s3 + 0.9), ("3 matching post templates", "$40", s3 + 1.5)]
        quote_card(sub, t, s3 + 0.4, 380, "Maple & Co. (sample)", rows, "$100", None, ACC)
        kq = p(t, s3 + 3.0, 0.4)
        pill(sub, W / 2, 1010, "On Fiverr: 20% fee → $80", F_BLACK, 52, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="💵")
        draw_text(sub, "Direct client: you keep more", F_XB, 44, W / 2, 1130, WHITE, alpha=out_cubic(p(t, s3 + 3.8, 0.4)))
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 34, W / 2, 1240, SOFT, alpha=out_cubic(p(t, s3 + 4.4, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel3.mp4")
