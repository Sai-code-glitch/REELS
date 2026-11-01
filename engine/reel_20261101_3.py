"""Find 'DM to order' on 1 bakery's post tonight (lead search + 3-line DM + sample form link)."""
from reel_preorder import *

ACC = (120, 235, 160)   # mint
GOLD = (255, 214, 92)
bg = Background(top=(4, 32, 34), bottom=(10, 70, 66), blobs=[(30, 160, 140), (230, 150, 60), (40, 110, 170)], seed=3053)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Find \"DM to order\"", "on 1 bakery's", "post tonight"], t, -0.3, 450, 100, (WHITE, ACC), gap=0.06, highlight={"\"dm", "to", "order\""})
        kp = p(t, 0.8, 0.35)
        pill(sub, W / 2, 740, "It can be your first gig", F_XB, 50, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="💡")
        bakery_post(sub, t, 1.1, 850, [], hl_at=1.7, w=760)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Lots of order", "questions = a lead"], t, s1 + 0.1, 275, 80, (WHITE, ACC), gap=0.07, highlight={"lead"})
        bakery_post(sub, t, s1 + 0.6, 395, [
            ("jen.k", "How much for 2?", s1 + 1.6),
            ("mike_r", "Still taking orders?", s1 + 2.2),
            ("ana.b", "Can I pick up Tuesday?", s1 + 2.8),
        ], hl_at=s1 + 1.0)
        kx = p(t, s1 + 4.2, 0.4)
        pill(sub, W / 2, 1545, "They need an order form", F_XB, 48, GOLD, INK, alpha=out_cubic(kx), scale=out_back(kx), icon="🎯")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Send a 3-line DM"], t, s2 + 0.1, 290, 88, (WHITE, ACC), gap=0.07, highlight={"3-line"})
        phone_chat(sub, t, s2 + 0.6, W / 2, 400, [
            ("me", "Hi! Your pie post has so many order questions.", s2 + 1.2, None),
            ("me", "I set up free Google Forms so orders land in 1 list.", s2 + 2.5, None),
            ("me", "Want a sample form with your pies on it?", s2 + 3.9, "Sent"),
        ], header="Crumb & Co", h=1000)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Show the sample,", "then the price"], t, s3 + 0.1, 290, 88, (WHITE, ACC), gap=0.07, highlight={"sample,"})
        gform(sub, t, s3 + 0.6, 440, "Crumb & Co Pie Orders", scale=0.5, fill_at=s3 + 1.0)
        k2 = p(t, s3 + 1.8, 0.45)
        if k2 > 0:
            draw_text(sub, "Example price", F_XB, 40, W / 2, 1100, SOFT, alpha=out_cubic(k2))
            draw_text(sub, "$60", F_BLACK, 170, W / 2, 1230, GOLD, alpha=out_cubic(k2), scale=0.7 + 0.3 * out_back(k2))
            draw_text(sub, "form + sheet + bio link", F_XB, 44, W / 2, 1360, WHITE, alpha=out_cubic(k2))
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 36, W / 2, 1470, SOFT, alpha=out_cubic(p(t, s3 + 3.0, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel3.mp4")
