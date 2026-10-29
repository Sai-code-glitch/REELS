"""Cyber Monday is Nov 30. Shops need 4 posts (dated holiday post schedule)."""
from reel_insta import *

ACC = (255, 150, 60)    # warm orange
GOLD = (255, 224, 110)
bg = Background(top=(36, 6, 8), bottom=(84, 22, 12), blobs=[(220, 60, 40), (255, 140, 40), (180, 30, 90)], seed=2912)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, -0.2, 0.3)
        place_emoji(sub, "🗓️", W / 2, 450 - 14 * math.sin(t * 6), 180 * out_back(k), alpha=k, rot=5 * math.sin(t * 4))
        pop_words(sub, ["Cyber Monday is", "Nov 30. Shops", "need 4 posts"], t, -0.3, 820, 100, (WHITE, ACC), gap=0.06, highlight={"nov", "30.", "4", "posts"})
        kp = p(t, 1.0, 0.4)
        pill(sub, W / 2, 1130, "Not 1 sale post. 4.", F_XB, 54, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="📲")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["One sale post is", "easy to scroll past"], t, s1 + 0.1, 330, 84, (WHITE, ACC), gap=0.07, highlight={"one", "scroll"})
        mini_calendar(sub, t, s1 + 0.7, 820, ACC, {23: ("Teaser", s1 + 1.7), 27: ("BF", s1 + 2.3), 28: ("SBS", s1 + 2.9), 30: ("CM", s1 + 3.5)})
        kx = p(t, s1 + 4.4, 0.4)
        pill(sub, W / 2, 1260, "Remind followers 4 times", F_BLACK, 50, GOLD, INK, alpha=out_cubic(kx), scale=out_back(kx), icon="🔁")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["The 4-post schedule"], t, s2 + 0.1, 290, 84, (WHITE, ACC), gap=0.07, highlight={"4-post"})
        timeline(sub, t, s2 + 0.7, 480, [
            ("MON NOV 23", "Teaser: sale Friday", "👀"),
            ("FRI NOV 27", "Black Friday deal", "🛍️"),
            ("SAT NOV 28", "Small Biz Saturday", "🏪"),
            ("MON NOV 30", "Cyber Monday: last call", "⏰"),
        ], ACC, every=0.9, row=170)
        kc = p(t, s2 + 4.8, 0.4)
        pill(sub, W / 2, 1250, "1 design, 4 versions", F_XB, 48, GOLD, INK, alpha=out_cubic(kc), scale=out_back(kc), icon="🎨")
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Sell the whole", "schedule as 1 pack"], t, s3 + 0.1, 310, 86, (WHITE, GOLD), gap=0.07, highlight={"schedule", "pack"})
        offer_card(sub, t, s3 + 0.6, 770, [
            ("4 dated sale posts", "$60", s3 + 1.2),
            ("4 captions + hashtags", "$20", s3 + 1.8),
            ("Posting calendar", "incl.", s3 + 2.4),
        ], "$80", ACC, title="Black Friday to Cyber Monday", h=620)
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 36, W / 2, 1150, SOFT, alpha=out_cubic(p(t, s3 + 3.8, 0.4)))
        kq = p(t, s3 + 4.5, 0.4)
        pill(sub, W / 2, 1290, "Pitch it in early November", F_XB, 44, WHITE, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="📬")
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel2.mp4")
