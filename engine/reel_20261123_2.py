"""Your first thank-you card: 10 minutes, $0 (Canva postcard 6x4 -> 4 parts -> print 2 per page -> first sample)."""
from reel_insert import *

ACC = (110, 200, 255)
GOLD = (255, 214, 92)
bg = Background(top=(8, 20, 54), bottom=(28, 64, 140), blobs=[(40, 90, 200), (110, 200, 255), (20, 40, 110)], seed=1232)

KW = dict(shop="Loopy Knits", emoji="🧶", name="Ana", tip="Hand wash cold, lay flat", handle="@loopyknits")


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Your first", "thank-you card:", "10 minutes, $0"], t, -0.3, 360, 100, (WHITE, ACC), gap=0.06, highlight={"thank-you", "10", "minutes,", "$0"})
        clock(sub, t, 0.3, 2.6, 640, 10, GOLD)
        card_float(sub, t, 0.5, W / 2, 1010, ACC, w=780, rot=-3, steps=[0.6, 1.0, 1.4, 1.8, 2.2], **KW)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["You need 2 free things"], t, s1 + 0.1, 290, 84, (WHITE, ACC), gap=0.07, highlight={"2", "free"})
        tool_tile(sub, t, s1 + 0.8, W / 2 - 215, 680, "🎨", "Canva (free)", "Postcard 6 x 4 in", ACC)
        tool_tile(sub, t, s1 + 1.4, W / 2 + 215, 680, "🛍️", "1 real shop", "to design for", ACC)
        kb = p(t, s1 + 3.0, 0.4)
        pill(sub, W / 2, 1050, "No paid apps needed", F_BLACK, 48, GOLD, INK, alpha=out_cubic(kb), scale=out_back(kb), icon="✅")
        draw_text(sub, "Copy their name, colors", F_XB, 50, W / 2, 1180, WHITE, alpha=out_cubic(p(t, s1 + 3.8, 0.4)))
        draw_text(sub, "and @ from their Instagram.", F_XB, 50, W / 2, 1250, WHITE, alpha=out_cubic(p(t, s1 + 3.8, 0.4)))
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Add 4 things.", "Nothing else."], t, s2 + 0.1, 260, 88, (WHITE, ACC), gap=0.07, highlight={"4", "nothing"})
        st = [s2 + 0.6, s2 + 1.4, s2 + 3.0, s2 + 4.6, s2 + 6.2]
        canva_card(sub, t, s2 + 0.4, 900, ACC, st, labels=["Postcard · 6 x 4 in", "1. \"Thank you, [name]!\"", "2. One care tip", "3. Their @ + QR code", "4. 10% off next order"], **KW)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Print 2 per page", "on cardstock"], t, s3 + 0.1, 260, 88, (WHITE, ACC), gap=0.07, highlight={"2", "cardstock"})
        print_sheet(sub, t, s3 + 0.6, 830, ACC, s3 + 1.8, w=560, **KW)
        kb = p(t, s3 + 3.8, 0.4)
        pill(sub, W / 2, 1300, "That's your first sample", F_BLACK, 50, GOLD, INK, alpha=out_cubic(kb), scale=out_back(kb), icon="🎁")
        draw_text(sub, "Post it. Show it in every DM.", F_XB, 48, W / 2, 1430, WHITE, alpha=out_cubic(p(t, s3 + 4.6, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel2.mp4")
