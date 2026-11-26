"""Save 10 Black Friday emails this weekend (free copywriting practice: Gmail search + 'Swipe' label,
note 4 parts of each email, then write 1 sample for a small shop + example math)."""
from reel_swipe import *

ACC = (255, 92, 92)
GOLD = (255, 222, 120)
bg = Background(top=(26, 10, 22), bottom=(96, 18, 42), blobs=[(180, 30, 60), (255, 92, 92), (70, 20, 90)], seed=1261)

ROWS = [("Brew Lab Coffee", "48 hours only: 30% off beans", "hot"),
        ("Oak & Thread", "Our biggest sale starts NOW", None),
        ("Pine & Wick", "Doors open: candles from $12", "hot"),
        ("Trail Socks Co.", "Ends midnight. Free shipping", None)]


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Save 10 Black Friday", "emails this weekend"], t, -0.3, 360, 98, (WHITE, ACC), gap=0.06,
                  highlight={"10", "black", "friday", "weekend"})
        inbox(sub, t, 0.5, 600, [(a, b, 0.7 + i * 0.35, s) for i, (a, b, s) in enumerate(ROWS)], title="Promotions")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Your inbox is a", "free copywriting class"], t, s1 + 0.1, 290, 86, (WHITE, ACC), gap=0.07,
                  highlight={"free", "copywriting", "class"})
        email_open(sub, t, s1 + 0.9, 500, "Brew Lab Coffee", "48 hours only: 30% off",
                   ["Hi Sam,", "Our holiday beans are back.", "30% off every bag.", "Ends Sunday at midnight."],
                   marks=[(2, "", GOLD, s1 + 2.4), (3, "", ACC, s1 + 3.0)])
        draw_text(sub, "(sample email)", F_SEMI, 34, W / 2, 1080, SOFT, alpha=out_cubic(p(t, s1 + 1.6, 0.4)))
        kb = p(t, s1 + 4.0, 0.4)
        pill(sub, W / 2, 1230, "Brands pay pros to write these", F_BLACK, 46, GOLD, INK, alpha=out_cubic(kb), scale=out_back(kb), icon="✍️")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Search it. Label it", "\"Swipe\"."], t, s2 + 0.1, 280, 86, (WHITE, ACC), gap=0.07,
                  highlight={"\"swipe\".", "label", "search"})
        gmail_bar(sub, t, s2 + 0.6, 470, "black friday", type_dur=0.8)
        label_menu(sub, t, s2 + 1.6, 580, ["Receipts", "Travel"], "Swipe", new_at=s2 + 2.2, check_at=s2 + 3.0)
        draw_text(sub, "Note 4 parts of each:", F_XB, 52, W / 2, 1060, WHITE, alpha=out_cubic(p(t, s2 + 3.6, 0.4)))
        checklist(sub, t, s2 + 4.0, ["Subject line", "First line", "The offer", "The deadline"], 1160, 82, ACC, size=48, every=0.45)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Then write 1 sample", "for a small shop"], t, s3 + 0.1, 280, 86, (WHITE, ACC), gap=0.07,
                  highlight={"1", "sample", "small", "shop"})
        email_card(sub, t, s3 + 0.8, W / 2, 600, "YOUR SAMPLE", "Dec 10", "Gifts under $25, ready Friday",
                   "Hand-poured candles, gift-wrapped. Order by Dec 15.", GOLD)
        draw_text(sub, "Example: 3 emails × $40", F_XB, 50, W / 2, 830, WHITE, alpha=out_cubic(p(t, s3 + 1.8, 0.4)))
        money_counter(sub, t, s3 + 2.2, 120, 1020, GOLD, label="example, 1 shop")
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 34, W / 2, 1390, SOFT, alpha=out_cubic(p(t, s3 + 4.6, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel1.mp4")
