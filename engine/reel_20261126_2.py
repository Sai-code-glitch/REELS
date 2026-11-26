"""Your first swipe file: 10 minutes, $0 (free Google Doc table: subject / offer / deadline from 3 saved
Black Friday emails, spot the pattern, write your own subject line with it)."""
from reel_swipe import *

ACC = (90, 200, 255)
GOLD = (255, 214, 92)
bg = Background(top=(8, 18, 40), bottom=(14, 60, 100), blobs=[(30, 90, 160), (90, 200, 255), (40, 30, 110)], seed=1262)

TABLE = [("48 hours only:\n30% off beans", "30% off", "Sunday"),
         ("Doors open:\ncandles from $12", "From $12", "Monday"),
         ("Ends midnight.\nFree shipping", "Free ship", "Tonight")]


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Your first swipe file:", "10 minutes, $0"], t, -0.3, 360, 96, (WHITE, ACC), gap=0.06,
                  highlight={"swipe", "file:", "10", "minutes,", "$0"})
        clock(sub, t, 0.4, 3.0, 800, 10, ACC)
        swipe_table(sub, t, 0.8, 1010, TABLE[:2], row_at=1.2, every=0.6, w=880)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Copywriters keep one.", "It's just saved emails"], t, s1 + 0.1, 290, 80, (WHITE, ACC), gap=0.07,
                  highlight={"copywriters", "saved", "emails"})
        inbox(sub, t, s1 + 0.9, 470, [("Brew Lab Coffee", "48 hours only: 30% off beans", s1 + 1.1, "hot"),
                                     ("Pine & Wick", "Doors open: candles from $12", s1 + 1.4, "hot"),
                                     ("Trail Socks Co.", "Ends midnight. Free shipping", s1 + 1.7, "hot")], title="Label: Swipe")
        draw_text(sub, "(sample emails)", F_SEMI, 34, W / 2, 1110, SOFT, alpha=out_cubic(p(t, s1 + 2.2, 0.4)))
        kb = p(t, s1 + 3.4, 0.4)
        pill(sub, W / 2, 1260, "Free Google Doc + 3 emails", F_BLACK, 48, GOLD, INK, alpha=out_cubic(kb), scale=out_back(kb), icon="📄")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Copy 3 parts", "into a table"], t, s2 + 0.1, 280, 90, (WHITE, ACC), gap=0.07,
                  highlight={"3", "parts", "table"})
        swipe_table(sub, t, s2 + 0.6, 450, TABLE, row_at=s2 + 1.4, every=0.9, w=900)
        checklist(sub, t, s2 + 4.4, ["Subject = the hook", "Offer = the reason", "Deadline = the push"], 1140, 84, ACC, size=46, every=0.5)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Spot the pattern.", "Use it on your own."], t, s3 + 0.1, 280, 86, (WHITE, ACC), gap=0.07,
                  highlight={"pattern.", "own."})
        build_row(sub, t, s3 + 0.9, 520, ["Time", "Offer", "Deadline"], [GOLD, ACC, (255, 150, 120)], size=46, gap=0.5)
        draw_text(sub, "Your practice subject line:", F_XB, 46, W / 2, 680, WHITE, alpha=out_cubic(p(t, s3 + 2.4, 0.4)))
        email_card(sub, t, s3 + 2.8, W / 2, 900, "PRACTICE", "Draft", "3 days: free gift wrap, ends Sun",
                   "For a small shop you like. Keep it short and true.", GOLD)
        kb = p(t, s3 + 4.6, 0.4)
        pill(sub, W / 2, 1200, "Do 1 a day. Save the best.", F_BLACK, 46, ACC, INK, alpha=out_cubic(kb), scale=out_back(kb), icon="📌")
        draw_text(sub, "Borrow the structure, never the words.", F_SEMI, 36, W / 2, 1350, SOFT, alpha=out_cubic(p(t, s3 + 5.2, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel2.mp4")
