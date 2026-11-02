"""Search this on Facebook tonight (find shops posting Small Business Saturday plans without a flyer)."""
from reel_flyer import *

ACC = (150, 235, 120)   # lime
GOLD = (255, 214, 92)
FLY = (60, 160, 90)
Q = "small business saturday + your town"
bg = Background(top=(6, 28, 14), bottom=(18, 64, 34), blobs=[(40, 170, 90), (230, 190, 60), (30, 120, 150)], seed=3063)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Search this on", "Facebook tonight"], t, -0.3, 470, 110, (WHITE, ACC), gap=0.06, highlight={"facebook", "tonight"})
        kp = p(t, 0.7, 0.35)
        pill(sub, W / 2, 720, "Find shops that need a flyer", F_XB, 50, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="🎯")
        fb_search(sub, t, 0.9, 900, Q, type_dur=1.4)
        place_emoji(sub, "👆", W / 2 + 260, 1060 + 18 * math.sin(t * 8), 110, alpha=out_cubic(p(t, 1.6, 0.4)))
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Tap Posts. Spot", "the plain-text ones"], t, s1 + 0.1, 270, 76, (WHITE, ACC), gap=0.07, highlight={"plain-text"})
        fb_search(sub, t, s1 + 0.3, 420, Q, type_dur=0.01)
        fb_chips(sub, t, s1 + 0.6, 550, ["All", "Posts", "Pages", "Groups"], active=1, act_at=s1 + 1.3)
        rows = [("🪴", (170, 220, 180), "Leaf & Pot", "2 days ago", "We're open Saturday, come by!", False),
                ("🧁", (250, 200, 220), "Sweet Rise", "3 days ago", "Small Biz Sat deals!", True),
                ("📚", (200, 210, 250), "Paper Lantern Books", "1 day ago", "Open 9-6 on the 28th", False)]
        for i, (em, col, shop, ago, body, has) in enumerate(rows):
            fb_post(sub, t, s1 + 1.6 + i * 0.4, 720 + i * 262, em, col, shop, ago, body, has, s1 + 3.2 + i * 0.4, FLY, h=240)
        kx = p(t, s1 + 4.8, 0.4)
        pill(sub, W / 2, 1470, "Red = your lead", F_XB, 50, GOLD, INK, alpha=out_cubic(kx), scale=out_back(kx), icon="📌")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Send a 3-line DM"], t, s2 + 0.1, 290, 88, (WHITE, ACC), gap=0.07, highlight={"3-line"})
        phone_chat(sub, t, s2 + 0.6, W / 2, 400, [
            ("me", "Hi! Saw you're open for Small Business Saturday.", s2 + 1.2, None),
            ("me", "I make simple flyers for print + Facebook.", s2 + 2.6, None),
            ("me", "Want a free sample with your shop on it?", s2 + 4.0, "Sent"),
        ], header="Leaf & Pot", h=1000)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Show the sample,", "then the price"], t, s3 + 0.1, 280, 86, (WHITE, ACC), gap=0.07, highlight={"sample,"})
        flyer_card(sub, t, s3 + 0.6, W / 2, 760, FLY, w=380, rot=-3)
        k2 = p(t, s3 + 1.8, 0.45)
        if k2 > 0:
            draw_text(sub, "Example price", F_XB, 40, W / 2, 1130, SOFT, alpha=out_cubic(k2))
            draw_text(sub, "$50", F_BLACK, 160, W / 2, 1250, GOLD, alpha=out_cubic(k2), scale=0.7 + 0.3 * out_back(k2))
            draw_text(sub, "print + social sizes", F_XB, 44, W / 2, 1370, WHITE, alpha=out_cubic(k2))
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 34, W / 2, 1460, SOFT, alpha=out_cubic(p(t, s3 + 3.0, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel3.mp4")
