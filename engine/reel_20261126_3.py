"""Stop copying emails word for word (swipe files: keep the structure, swap in the shop's own details,
send it as a free sample, example pricing)."""
from reel_swipe import *

ACC = (255, 190, 60)
GOLD = (255, 232, 140)
bg = Background(top=(12, 26, 18), bottom=(20, 80, 52), blobs=[(30, 130, 80), (255, 190, 60), (20, 60, 90)], seed=1263)

BIG = ["Our BIGGEST sale ever.", "40% off everything.", "48 hours only."]
MINE = ["Candles, wrapped for you.", "Free gift wrap this week.", "Order by Dec 15."]


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Stop copying emails", "word for word"], t, -0.3, 360, 100, (WHITE, ACC), gap=0.06,
                  highlight={"stop", "copying", "word"})
        email_open(sub, t, 0.5, 560, "Big Brand Store", "Our BIGGEST sale ever", BIG)
        stamp(sub, t, 1.4, W / 2 + 190, 905, "COPIED", RED, size=80, rot=-12)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["A small shop can't", "say what a big brand says"], t, s1 + 0.1, 290, 76, (WHITE, ACC), gap=0.06,
                  highlight={"small", "big", "brand"})
        checklist(sub, t, s1 + 1.0, ["Different prices", "Different products", "Different customers"], 520, 100, ACC, size=52, every=0.55, icon="❌")
        draw_text(sub, "Copied lines sound fake to their buyers", F_XB, 44, W / 2, 900, WHITE, alpha=out_cubic(p(t, s1 + 3.0, 0.4)))
        kb = p(t, s1 + 4.0, 0.4)
        pill(sub, W / 2, 1060, "And copying word for word is not OK", F_BLACK, 40, (255, 120, 110), INK, alpha=out_cubic(kb), scale=out_back(kb), icon="🚫")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Keep the structure.", "Swap the details."], t, s2 + 0.1, 270, 88, (WHITE, ACC), gap=0.07,
                  highlight={"structure.", "details."})
        build_row(sub, t, s2 + 0.7, 460, ["Hook", "Offer", "Deadline"], [GOLD, ACC, (120, 220, 160)], size=46, gap=0.4)
        email_open(sub, t, s2 + 2.0, 560, "Pine & Wick", "Gifts under $25, ready Friday", MINE,
                   marks=[(0, "", GOLD, s2 + 3.4), (1, "", ACC, s2 + 4.0), (2, "", (120, 220, 160), s2 + 4.6)],
                   tag="REWRITE", tag_col=OKG, tag_at=s2 + 2.8, sender_col=(40, 150, 90))
        draw_text(sub, "Their products. Their prices. Their dates.", F_XB, 42, W / 2, 1150, WHITE, alpha=out_cubic(p(t, s2 + 5.2, 0.4)))
        draw_text(sub, "(sample shop)", F_SEMI, 32, W / 2, 1220, SOFT, alpha=out_cubic(p(t, s2 + 5.4, 0.4)))
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Send it as a", "free sample"], t, s3 + 0.1, 270, 92, (WHITE, ACC), gap=0.07, highlight={"free", "sample"})
        chat_bubble(sub, t, s3 + 0.8, 520, ["Hi! I wrote a holiday email", "for your candles, free.", "Want 2 more before Dec 15?"],
                    me=True, color=(40, 140, 90))
        draw_text(sub, "Example: 3 emails × $40", F_XB, 50, W / 2, 790, WHITE, alpha=out_cubic(p(t, s3 + 2.0, 0.4)))
        money_counter(sub, t, s3 + 2.4, 120, 990, GOLD, label="example, 1 shop")
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 34, W / 2, 1390, SOFT, alpha=out_cubic(p(t, s3 + 4.8, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel3.mp4")
