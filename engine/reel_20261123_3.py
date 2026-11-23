"""Why would a shop pay for a 4x6 card? (what the card does -> 2-version package -> example math)."""
from reel_insert import *

ACC = (130, 230, 140)
GOLD = (255, 214, 92)
bg = Background(top=(8, 36, 22), bottom=(26, 96, 58), blobs=[(40, 140, 80), (130, 230, 140), (10, 70, 40)], seed=1233)

KW = dict(shop="Sprout Soap Co", emoji="🧼", name="Leo", tip="Keep dry between uses", handle="@sproutsoapco")


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Why would a shop", "pay for a 4x6 card?"], t, -0.3, 340, 96, (WHITE, ACC), gap=0.06, highlight={"pay", "4x6", "card?"})
        ship_box(sub, t, 0.3, W / 2, 1000, ACC, 0.9, 1.3, w=600, card_kw=KW)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["The buyer opens", "the box and sees:"], t, s1 + 0.1, 290, 84, (WHITE, ACC), gap=0.07, highlight={"opens", "box"})
        rows = [("💌", "A personal thank-you"), ("🧴", "How to care for it"), ("🏷️", "A reason to order again"), ("📱", "Where to tag the shop")]
        for i, (em, lab) in enumerate(rows):
            kk = p(t, s1 + 1.0 + i * 0.6, 0.4)
            if kk <= 0: continue
            y = 520 + i * 130
            x = 150 + 60 * (1 - out_cubic(kk))
            place_emoji(sub, em, x, y, 72 * out_back(kk), alpha=out_cubic(kk))
            draw_text(sub, lab, F_XB, 54, x + 66, y, WHITE, alpha=out_cubic(kk), anchor="lm")
        kb = p(t, s1 + 4.0, 0.4)
        pill(sub, W / 2, 1130, "Owners are busy packing, not designing", F_BLACK, 40, GOLD, INK, alpha=out_cubic(kb), scale=out_back(kb), icon="📦")
        draw_text(sub, "So they pay someone else.", F_XB, 50, W / 2, 1260, WHITE, alpha=out_cubic(p(t, s1 + 4.8, 0.4)))
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Sell 2 versions", "in 1 package"], t, s2 + 0.1, 260, 92, (WHITE, ACC), gap=0.07, highlight={"2", "versions"})
        card_float(sub, t, s2 + 0.7, W / 2 - 50, 615, ACC, w=560, rot=4, label="Everyday", label_col=ACC, **KW)
        card_float(sub, t, s2 + 1.6, W / 2 + 50, 1115, (240, 90, 90), w=560, rot=-4, label="Holiday", label_col=(255, 150, 150), holiday=True, **KW)
        kb = p(t, s2 + 3.4, 0.4)
        pill(sub, W / 2, 1470, "Send a print-ready PDF", F_BLACK, 46, WHITE, INK, alpha=out_cubic(kb), scale=out_back(kb), icon="📄")
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Example math"], t, s3 + 0.1, 280, 96, (WHITE, ACC), gap=0.07, highlight={"math"})
        draw_text(sub, "$25 card pack  ×  4 shops", F_XB, 58, W / 2, 470, WHITE, alpha=out_cubic(p(t, s3 + 0.6, 0.4)))
        money_counter(sub, t, s3 + 1.2, 100, 760, GOLD, label="example, 4 shops")
        draw_text(sub, "Start with 1 shop. Then repeat.", F_SEMI, 44, W / 2, 1120, SOFT, alpha=out_cubic(p(t, s3 + 3.6, 0.4)))
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 34, W / 2, 1400, SOFT, alpha=out_cubic(p(t, s3 + 4.4, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel3.mp4")
