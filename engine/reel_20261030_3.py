"""Pitch this gift card fix in 3 lines: DM formula + free mockup."""
from reel_giftcard import *

ACC = (255, 110, 130)   # coral
GOLD = (255, 214, 92)
bg = Background(top=(44, 8, 22), bottom=(90, 20, 40), blobs=[(220, 50, 90), (250, 160, 60), (120, 40, 160)], seed=3033)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Pitch this", "gift card fix", "in 3 lines"], t, -0.3, 520, 116, (WHITE, ACC), gap=0.06, highlight={"gift", "card", "3"})
        kp = p(t, 0.8, 0.35)
        pill(sub, W / 2, 800, "Copy it tonight", F_XB, 54, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="✍️")
        gift_card(sub, t, 1.1, W / 2, 1150, "Rosa's Bakery", "$50", (230, 80, 120), "🧁", rot=-5)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Long pitches", "get ignored"], t, s1 + 0.1, 320, 90, (WHITE, ACC), gap=0.07, highlight={"ignored"})
        chat_bubble(sub, t, s1 + 0.8, 640, ["Hi! I'm a freelancer with many", "skills and services. I do web,", "design, marketing, social media,", "SEO, ads, writing, video and..."], me=True, color=(110, 116, 130), w=860)
        strike(sub, t, s1 + 2.6, 160, W - 160, 640, RED, width=18)
        kx = p(t, s1 + 3.4, 0.4)
        pill(sub, W / 2, 940, "Too vague. Too long.", F_XB, 52, WHITE, INK, alpha=out_cubic(kx), scale=out_back(kx), icon="😴")
        pop_words(sub, ["Use 3 lines instead"], t, s1 + 4.4, 1180, 80, (WHITE, GOLD), gap=0.07, highlight={"3", "lines"})
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        build_row(sub, t, s2 + 0.1, 300, ["Notice", "Offer", "Free mockup"], [GOLD, ACC, (120, 220, 170)], size=46, gap=0.4)
        phone_chat(sub, t, s2 + 0.9, W / 2, 420, [
            ("me", "Hi Rosa! Love your shop. I noticed your site has no online gift cards.", s2 + 1.5, None),
            ("me", "I can set them up + add a menu button before Black Friday.", s2 + 3.0, None),
            ("me", "Want a free mockup of your gift card first?", s2 + 4.5, "Sent"),
        ], header="Rosa's Bakery", h=1000)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Make the mockup", "in Canva for free"], t, s3 + 0.1, 300, 84, (WHITE, GOLD), gap=0.07, highlight={"canva", "free"})
        gift_card(sub, t, s3 + 0.7, W / 2, 610, "Rosa's Bakery", "$25", (230, 80, 120), "🧁", w=600, h=330, rot=-3)
        offer_card(sub, t, s3 + 1.6, 1110, [
            ("Online gift cards on", "$60", s3 + 2.1),
            ("Menu button + 1 post", "$40", s3 + 2.6),
        ], "$100", ACC, title="If they say yes", h=580)
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 36, W / 2, 1460, SOFT, alpha=out_cubic(p(t, s3 + 4.2, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel3.mp4")
