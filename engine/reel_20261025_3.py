"""A 10-minute gig local shops need in November -- pitch one specific fix (holiday hours + 2 posts), example offer + math."""
from reel_maps import *

ACC = (120, 235, 150)   # mint green
GOLD = (255, 205, 80)
PINK = (255, 140, 190)
bg = Background(top=(6, 26, 20), bottom=(10, 18, 36), blobs=[(40, 200, 130), (60, 140, 255), (120, 230, 170)], seed=2983)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, 0.0, 0.3)
        place_emoji(sub, "🏪", W / 2, 470 - 16 * math.sin(t * 5), 210 * out_back(k), alpha=k, rot=6 * math.sin(t * 4))
        pop_words(sub, ["A 10-minute gig", "local shops need", "in November"], t, 0.0, 860, 104, (WHITE, ACC), gap=0.07, highlight={"10-minute", "gig", "november"})
        kp = p(t, 1.5, 0.4)
        pill(sub, W / 2, 1150, "Holiday hours on Google", F_XB, 50, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="📍")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Don't pitch", "\"I do marketing\""], t, s1 + 0.1, 300, 84, (WHITE, PINK), gap=0.08, highlight={"don't", "\"i", "do", "marketing\""})
        pop_words(sub, ["Pitch 1 thing you spotted:"], t, s1 + 1.3, 470, 56, (WHITE, ACC), gap=0.06, path=F_XB, highlight={"1", "thing"})
        phone_chat(sub, t, s1 + 1.8, W / 2, 560, [
            ("me", "Hi Rosa! Your Google listing has no Thanksgiving hours yet. Want me to add your holiday hours this week?", s1 + 2.3, "typed"),
        ], header="Rosa's Bakery", h=620)
        kx = p(t, s1 + 5.2, 0.4)
        pill(sub, W / 2, 1290, "Specific + easy to say yes to", F_XB, 46, ACC, INK, alpha=out_cubic(kx), scale=out_back(kx), icon="🎯")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Make it a small", "holiday package"], t, s2 + 0.1, 300, 82, (WHITE, GOLD), gap=0.07, highlight={"holiday", "package"})
        offer_card(sub, t, s2 + 0.8, 790, [
            ("Holiday hours (5 dates)", "$25", s2 + 1.4),
            ("2 holiday posts on Google", "$30", s2 + 2.1),
            ("Check 1 week later", "$0", s2 + 2.8),
        ], "$55", ACC)
        kp = p(t, s2 + 4.8, 0.4)
        pill(sub, W / 2, 1230, "Ask the owner for real hours + photos", F_SEMI, 40, WHITE, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="📸")
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["The math"], t, s3 + 0.1, 290, 86, (WHITE, ACC), gap=0.07, highlight={"math"})
        kl = p(t, s3 + 0.5, 0.4)
        draw_text(sub, "Example: $55 × 4 shops in November", F_XB, 46, W / 2, 420, WHITE, alpha=out_cubic(kl))
        money_counter(sub, t, s3 + 0.9, 220, 700, GOLD, label="example pricing")
        kq = p(t, s3 + 3.8, 0.4)
        pill(sub, W / 2, 1110, "Start with 1 shop this week", F_XB, 46, ACC, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="🚀")
        kr = p(t, s3 + 4.5, 0.4)
        draw_text(sub, "Results depend on your work.", F_SEMI, 40, W / 2, 1250, SOFT, alpha=out_cubic(kr))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel3.mp4")
