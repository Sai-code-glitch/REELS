"""Etsy shops get the same 5 questions (holiday message rush -> Saved replies -> shops pay for the words)."""
from reel_replies import *

ACC = (255, 150, 70)    # Etsy-ish orange
GOLD = (255, 214, 92)
bg = Background(top=(40, 16, 10), bottom=(92, 36, 18), blobs=[(200, 80, 30), (255, 150, 70), (130, 40, 30)], seed=1121)

ROWS = [(NAMES[i], q, em, 0.6 + i * 0.25) for i, (q, em) in enumerate(QUESTIONS[:4])]


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Etsy shops get", "the same 5", "questions"], t, -0.3, 390, 110, (WHITE, ACC), gap=0.06, highlight={"same", "5"})
        etsy_inbox(sub, t, 0.5, 700, ROWS, count_from=3, count_to=38, count_dur=2.6)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Every December:"], t, s1 + 0.1, 290, 92, (WHITE, ACC), gap=0.07, highlight={"December:"})
        for i, (q, em) in enumerate(QUESTIONS):
            kk = p(t, s1 + 0.7 + i * 0.6, 0.4)
            if kk <= 0: continue
            y = 470 + i * 130
            x = 150 + 60 * (1 - out_cubic(kk))
            place_emoji(sub, em, x, y, 72 * out_back(kk), alpha=out_cubic(kk))
            draw_text(sub, q, F_XB, 54, x + 66, y, WHITE, alpha=out_cubic(kk), anchor="lm")
        kb = p(t, s1 + 4.4, 0.4)
        pill(sub, W / 2, 1180, "Typing each one by hand adds up", F_BLACK, 46, GOLD, INK, alpha=out_cubic(kb), scale=out_back(kb), icon="⏳")
        draw_text(sub, "Same answer. Over and over.", F_XB, 46, W / 2, 1300, WHITE, alpha=out_cubic(p(t, s1 + 5.2, 0.4)))
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Etsy has a fix:", "Saved replies"], t, s2 + 0.1, 250, 84, (WHITE, ACC), gap=0.07, highlight={"Saved", "replies"})
        saved_picker(sub, t, s2 + 0.6, 440, "Will it arrive by Dec 24?",
                     [(q[:22] if len(q) <= 22 else q[:21] + "…", em) for q, em in QUESTIONS[:4]],
                     pick=0, open_at=s2 + 2.0, pick_at=s2 + 3.6,
                     reply="Hi Emma! Order by Dec 15 for Dec 24 delivery. I'll send tracking the day it ships!",
                     h=820)
        draw_text(sub, "Write it once. Send it in 2 taps.", F_XB, 50, W / 2, 1380, WHITE, alpha=out_cubic(p(t, s2 + 5.0, 0.4)))
        draw_text(sub, "(sample shop and buyer)", F_SEMI, 32, W / 2, 1450, SOFT, alpha=out_cubic(p(t, s2 + 5.4, 0.4)))
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Shops pay you", "to write them"], t, s3 + 0.1, 260, 88, (WHITE, ACC), gap=0.07, highlight={"pay", "write"})
        offer_card(sub, t, s3 + 0.8, 840, [("5 holiday saved replies", "$25", s3 + 1.4), ("5 shop FAQs", "$15", s3 + 2.0), ("Done in 1-2 days", "", s3 + 2.6)],
                   "$40", ACC, title="Holiday reply pack", h=620)
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 34, W / 2, 1250, SOFT, alpha=out_cubic(p(t, s3 + 4.4, 0.4)))
        kq = p(t, s3 + 5.0, 0.4)
        pill(sub, W / 2, 1380, "Start with 1 shop this week", F_XB, 46, WHITE, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="🎯")
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel1.mp4")
