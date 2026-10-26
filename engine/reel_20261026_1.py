"""Your first quote: 5 minutes, $0 -- a 4-line quote with a deposit line."""
from reel_quote import *

ACC = (120, 230, 170)   # mint
GOLD = (255, 210, 90)
bg = Background(top=(6, 30, 26), bottom=(8, 46, 40), blobs=[(30, 200, 140), (60, 220, 200), (20, 120, 160)], seed=2991)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, 0.0, 0.3)
        place_emoji(sub, "🧾", W / 2, 470 - 16 * math.sin(t * 5), 210 * out_back(k), alpha=k, rot=6 * math.sin(t * 4))
        pop_words(sub, ["Your first quote:", "5 minutes,", "$0"], t, 0.0, 860, 116, (WHITE, ACC), gap=0.07, highlight={"5", "minutes,", "$0"})
        kp = p(t, 1.5, 0.4)
        pill(sub, W / 2, 1160, "Copy these 4 lines", F_XB, 50, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="✍️")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Client asks", "\"How much?\""], t, s1 + 0.1, 300, 84, (WHITE, GOLD), gap=0.08, highlight={"\"how", "much?\""})
        chat_bubble(sub, t, s1 + 0.9, 560, ["Hey! How much for a logo?"], me=False)
        chat_bubble(sub, t, s1 + 1.8, 720, ["Umm... maybe $50?", "Whatever works for you!"], me=True, color=(120, 126, 140))
        kx = p(t, s1 + 3.0, 0.4)
        pill(sub, W / 2, 940, "Vague = lowball + endless changes", F_XB, 46, (255, 230, 232), (200, 30, 50), alpha=out_cubic(kx), scale=out_back(kx), icon="⚠️")
        kq = p(t, s1 + 4.0, 0.4)
        draw_text(sub, "Send a written quote instead", F_XB, 52, W / 2, 1100, ACC, alpha=out_cubic(kq))
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["4 lines. That's it."], t, s2 + 0.1, 260, 80, (WHITE, ACC), gap=0.07, highlight={"4", "lines."})
        rows = [("1. What you'll make", "1 logo, 3 ideas", s2 + 1.0),
                ("2. Revisions", "2 rounds", s2 + 1.9),
                ("3. Deadline", "7 days", s2 + 2.8),
                ("4. Price", "$150", s2 + 3.7)]
        quote_card(sub, t, s2 + 0.5, 380, "For: Rosa's Bakery", rows, "$150", None, ACC)
        kp = p(t, s2 + 5.0, 0.4)
        pill(sub, W / 2, 1200, "Free: a Google Doc or Canva", F_XB, 46, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="🆓")
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Add 1 more line:", "deposit first"], t, s3 + 0.1, 280, 78, (WHITE, GOLD), gap=0.07, highlight={"deposit", "first"})
        rows = [("Logo, 2 revisions, 7 days", "$150", s3 + 0.6)]
        quote_card(sub, t, s3 + 0.4, 440, "Example pricing", rows, "$150", "$75", ACC, accept_at=s3 + 2.4, deposit_at=s3 + 1.5)
        kr = p(t, s3 + 3.6, 0.4)
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 36, W / 2, 1150, SOFT, alpha=out_cubic(kr))
        kq = p(t, s3 + 4.3, 0.4)
        pill(sub, W / 2, 1290, "Clear quote = easier yes", F_XB, 48, WHITE, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="🤝")
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel1.mp4")
