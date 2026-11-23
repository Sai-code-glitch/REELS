"""Search #packingorders on Instagram tonight (thank-you card gig: find shops with no card in the box -> free sample card -> DM + example offer)."""
from reel_insert import *

ACC = (255, 170, 80)
GOLD = (255, 222, 120)
bg = Background(top=(40, 22, 12), bottom=(112, 62, 30), blobs=[(170, 100, 50), (255, 170, 80), (90, 46, 20)], seed=1231)

KW = dict(shop="Pine & Wick", emoji="🕯️", name="Sam", tip="Burn 2 hours the first time", handle="@pineandwick")


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Search", "#packingorders", "tonight"], t, -0.3, 360, 104, (WHITE, ACC), gap=0.07, highlight={"#packingorders", "tonight"})
        ig_search(sub, t, 0.5, 680, "#packingorders", type_dur=0.9)
        post_row(sub, t, 1.1, 860, "🕯️", (255, 214, 170), "@pineandwick", "Packing 20 orders", False, 1.8)
        post_row(sub, t, 1.4, 1070, "🧶", (200, 225, 255), "@loopyknits", "Pack with me tonight", False, 2.1)
        draw_text(sub, "on Instagram", F_XB, 54, W / 2, 1260, SOFT, alpha=out_cubic(p(t, 2.3, 0.4)))
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Small shops film", "every box they pack"], t, s1 + 0.1, 290, 84, (WHITE, ACC), gap=0.07, highlight={"every", "box"})
        rows = [("🕯️", (255, 214, 170), "@pineandwick", "Packing 20 orders", False),
                ("🧶", (200, 225, 255), "@loopyknits", "Pack with me tonight", False),
                ("🌿", (200, 240, 210), "@sproutsoapco", "Order #142 going out", True)]
        for i, (em, col, hd, cap, has) in enumerate(rows):
            post_row(sub, t, s1 + 0.8 + i * 0.4, 520 + i * 215, em, col, hd, cap, has, s1 + 2.4 + i * 0.5)
        draw_text(sub, "Watch: is there a thank-you card", F_XB, 46, W / 2, 1230, WHITE, alpha=out_cubic(p(t, s1 + 4.2, 0.4)))
        draw_text(sub, "in the box?", F_XB, 46, W / 2, 1295, WHITE, alpha=out_cubic(p(t, s1 + 4.2, 0.4)))
        kb = p(t, s1 + 5.0, 0.4)
        pill(sub, W / 2, 1430, "No card = your lead", F_BLACK, 50, GOLD, INK, alpha=out_cubic(kb), scale=out_back(kb), icon="🎯")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Make them 1 free", "sample card in Canva"], t, s2 + 0.1, 260, 80, (WHITE, ACC), gap=0.07, highlight={"free", "sample", "card"})
        st = [s2 + 0.9, s2 + 1.8, s2 + 3.4, s2 + 5.0, s2 + 6.4]
        canva_card(sub, t, s2 + 0.5, 900, ACC, st, labels=["Blank 6 x 4 card", "1. Thank you + name", "2. One care tip", "3. Their @ + a QR code", "4. Next-order code"], **KW)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["DM it to them.", "Then offer the rest."], t, s3 + 0.1, 260, 84, (WHITE, ACC), gap=0.07, highlight={"dm", "offer"})
        chat_bubble(sub, t, s3 + 0.9, 600, ["Hi! Love your packing videos.", "I made a free thank-you card", "for your boxes. Want the", "print-ready file?"], me=True, color=(40, 120, 230))
        draw_text(sub, "(sample DM)", F_SEMI, 32, W - 130, 790, SOFT, alpha=out_cubic(p(t, s3 + 1.3, 0.4)), anchor="rm")
        offer_card(sub, t, s3 + 2.2, 1080, [("Card design, 2 versions", "$25", s3 + 2.8), ("Print-ready PDF", "incl.", s3 + 3.3)], "$25", ACC, title="Thank-you card", h=520)
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 34, W / 2, 1400, SOFT, alpha=out_cubic(p(t, s3 + 4.6, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel1.mp4")
