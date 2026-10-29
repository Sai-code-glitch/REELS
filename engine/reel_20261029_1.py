"""Search this on Instagram tonight: find local shops that went quiet before the holidays."""
from reel_insta import *

ACC = (255, 120, 190)   # IG pink
GOLD = (255, 214, 92)
bg = Background(top=(30, 6, 40), bottom=(70, 14, 70), blobs=[(200, 40, 140), (130, 60, 220), (250, 110, 60)], seed=2911)
Q = "#yourcity boutique"


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, -0.2, 0.3)
        place_emoji(sub, "🔎", W / 2, 440 - 16 * math.sin(t * 6), 180 * out_back(k), alpha=k)
        pop_words(sub, ["Search this on", "Instagram tonight"], t, -0.3, 750, 104, (WHITE, ACC), gap=0.06, highlight={"instagram", "tonight"})
        kp = p(t, 0.8, 0.35)
        pill(sub, W / 2, 960, "Find shops that went quiet", F_XB, 50, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="🤫")
        ig_search(sub, t, 1.2, 1170, Q, type_dur=1.1)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Some shops stop posting", "before their busiest month"], t, s1 + 0.1, 330, 70, (WHITE, ACC), gap=0.07, highlight={"stop", "busiest"})
        ig_profile(sub, t, s1 + 0.8, 460, "@oakwickcandles", "🕯️", (250, 214, 165), s1 + 2.6)
        kx = p(t, s1 + 4.6, 0.4)
        pill(sub, W / 2, 1470, "That's your opening", F_BLACK, 52, GOLD, INK, alpha=out_cubic(kx), scale=out_back(kx), icon="🚪")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Search, then check", "the last post date"], t, s2 + 0.1, 300, 80, (WHITE, ACC), gap=0.07, highlight={"last", "post"})
        ig_search(sub, t, s2 + 0.3, 490, "#yourcity candles", type_dur=0.7)
        rows = [("🧁", (255, 200, 210), "@rosebakeshop", "2 days ago", False),
                ("🕯️", (250, 214, 165), "@oakwickcandles", "5 weeks ago", True),
                ("🧶", (200, 220, 255), "@knitandco", "4 weeks ago", True)]
        for i, (e, col, hnd, last, stale) in enumerate(rows):
            account_row(sub, t, s2 + 1.2 + i * 0.4, 680 + i * 190, e, col, hnd, last, stale, s2 + 2.8 + i * 0.4)
        chat_bubble(sub, t, s2 + 4.6, 1360, ["Hi! Love your candles. Want 4", "ready holiday posts? Free sample"], me=True, color=(225, 48, 108), w=820)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["DM 5 quiet shops", "with 1 sample"], t, s3 + 0.1, 310, 86, (WHITE, GOLD), gap=0.07, highlight={"5", "sample"})
        offer_card(sub, t, s3 + 0.6, 770, [
            ("4 holiday sale posts", "$60", s3 + 1.2),
            ("Captions + hashtags", "$20", s3 + 1.8),
            ("Ready by Nov 20", "incl.", s3 + 2.4),
        ], "$80", ACC, title="Holiday Instagram pack", h=620)
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 36, W / 2, 1150, SOFT, alpha=out_cubic(p(t, s3 + 3.8, 0.4)))
        kq = p(t, s3 + 4.5, 0.4)
        pill(sub, W / 2, 1290, "Look for 3+ weeks of silence", F_XB, 44, WHITE, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="📅")
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel1.mp4")
