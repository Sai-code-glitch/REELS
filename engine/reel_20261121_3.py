"""Check 1 Etsy shop's FAQs tonight (empty FAQ lead check, niche search, Instagram pitch, example pricing)."""
from reel_replies import *
from reel_chat import phone_chat

ACC = (255, 120, 200)   # pink
GOLD = (255, 214, 92)
bg = Background(top=(30, 10, 44), bottom=(70, 20, 90), blobs=[(150, 40, 170), (255, 120, 200), (80, 30, 140)], seed=3121)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Check 1 Etsy shop's", "FAQs tonight"], t, -0.3, 360, 104, (WHITE, ACC), gap=0.06, highlight={"FAQs", "tonight"})
        shop_faq_page(sub, t, 0.5, 620, scroll_at=1.2, flag_at=2.2, h=900)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Search your niche:"], t, s1 + 0.1, 280, 88, (WHITE, ACC), gap=0.07, highlight={"niche:"})
        etsy_search(sub, t, s1 + 0.5, 470, "christmas ornament")
        rows = [("🎄", (255, 214, 205), "Pine & Paper Co.", 0), ("⭐", (255, 236, 170), "Little Star Studio", 6), ("❄️", (205, 230, 255), "Snowberry Gifts", 0)]
        for i, (em, col, shop, n) in enumerate(rows):
            faq_row(sub, t, s1 + 1.9 + i * 0.5, 680 + i * 200, em, col, shop, n, flag_at=s1 + 3.6 + i * 0.4)
        draw_text(sub, "Shop page → scroll to FAQs", F_XB, 46, W / 2, 1320, WHITE, alpha=out_cubic(p(t, s1 + 5.2, 0.4)))
        draw_text(sub, "(sample shops)", F_SEMI, 32, W / 2, 1390, SOFT, alpha=out_cubic(p(t, s1 + 5.5, 0.4)))
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["DM them on Instagram"], t, s2 + 0.1, 250, 78, (WHITE, ACC), gap=0.07, highlight={"Instagram"})
        msgs = [
            ("me", "Hi! Love your ornaments. Your Etsy shop has no FAQs yet.", s2 + 0.9, None),
            ("me", "I wrote you 1 free reply for 'Will it arrive by Dec 24?'", s2 + 2.2, None),
            ("me", "Want the full pack of 5 for December?", s2 + 3.5, "Example DM"),
        ]
        phone_chat(sub, t, s2 + 0.4, W / 2, 340, msgs, header="Pine & Paper Co.", h=860)
        kb = p(t, s2 + 5.2, 0.4)
        pill(sub, W / 2, 1330, "Don't pitch in Etsy messages", F_BLACK, 46, GOLD, INK, alpha=out_cubic(kb), scale=out_back(kb), icon="🚫")
        draw_text(sub, "Use their public Instagram or email", F_XB, 40, W / 2, 1440, WHITE, alpha=out_cubic(p(t, s2 + 5.8, 0.4)))
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Example math"], t, s3 + 0.1, 260, 92, (WHITE, ACC), gap=0.07, highlight={"math"})
        bar_chart(sub, t, s3 + 0.4, 360, [("Shop 1", 40), ("Shop 2", 40), ("Shop 3", 40)], (230, 90, 180), title="Holiday reply packs", h=680, every=0.6)
        kq = p(t, s3 + 3.2, 0.4)
        pill(sub, W / 2, 1160, "3 shops × $40 = $120", F_BLACK, 56, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="💵")
        draw_text(sub, "Most shops will say no. Keep asking.", F_XB, 42, W / 2, 1280, WHITE, alpha=out_cubic(p(t, s3 + 4.0, 0.4)))
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 34, W / 2, 1370, SOFT, alpha=out_cubic(p(t, s3 + 4.6, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel3.mp4")
