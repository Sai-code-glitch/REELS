"""Black Friday is 31 days away. Shops need 3 texts -- sell a 3-text sale pack."""
from reel_sms import *

ACC = (90, 225, 140)    # text-message green
GOLD = (255, 214, 92)
RED = (255, 96, 110)
bg = Background(top=(6, 18, 40), bottom=(10, 40, 60), blobs=[(40, 200, 140), (40, 120, 220), (90, 220, 200)], seed=3001)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, -0.2, 0.3)
        place_emoji(sub, "📱", W / 2, 460 - 16 * math.sin(t * 6), 190 * out_back(k), alpha=k, rot=6 * math.sin(t * 4))
        pop_words(sub, ["Black Friday is", "31 days away.", "Shops need 3 texts"], t, -0.3, 830, 94, (WHITE, ACC), gap=0.06, highlight={"31", "days", "3", "texts"})
        kp = p(t, 1.4, 0.4)
        pill(sub, W / 2, 1160, "A gig you can sell this week", F_XB, 48, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), pad=(40, 22), icon="💼")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Sale emails get buried.", "Texts hit the lock screen"], t, s1 + 0.1, 270, 70, (WHITE, ACC), gap=0.07, highlight={"buried.", "lock", "screen"})
        lock_screen(sub, t, s1 + 0.6, 420, ACC, h=760, banners=[
            ("Messages", "Rosa's Bakery", "Pie sale is LIVE. 20% off today", SMS_GREEN, "💬", s1 + 1.6),
            ("Mail", "Promotions (48)", "Mega deals inside...", (120, 126, 140), "📧", s1 + 2.6),
        ])
        kx = p(t, s1 + 4.2, 0.4)
        pill(sub, W / 2, 1290, "Only text customers who opted in", F_XB, 44, WHITE, INK, alpha=out_cubic(kx), scale=out_back(kx), icon="✅")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["The 3-text pack"], t, s2 + 0.1, 260, 84, (WHITE, ACC), gap=0.07, highlight={"3-text"})
        sms_thread(sub, t, s2 + 0.4, W / 2, 340, [
            ("them", "Tomorrow: 20% off pies for text club only. Reply STOP to opt out", s2 + 1.2, "MON 11/23 · TEASER"),
            ("them", "Pie sale is LIVE! 20% off today. Order: rosas.co/bf", s2 + 2.8, "FRI 11/27 · SALE DAY"),
            ("them", "Last chance: sale ends at 8pm tonight", s2 + 4.4, "MON 11/30 · LAST CALL"),
        ], h=900)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["What you sell"], t, s3 + 0.1, 260, 84, (WHITE, GOLD), gap=0.07, highlight={"sell"})
        offer_card(sub, t, s3 + 0.4, 700, [
            ("3 texts, written", "", s3 + 1.0),
            ("Dates + times to send", "", s3 + 1.6),
            ("Opt-out line included", "", s3 + 2.2),
        ], "$75", ACC, title="Black Friday text pack", h=660)
        kr = p(t, s3 + 3.8, 0.4)
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 36, W / 2, 1130, SOFT, alpha=out_cubic(kr))
        kq = p(t, s3 + 4.5, 0.4)
        pill(sub, W / 2, 1260, "They paste them into their text tool", F_XB, 42, WHITE, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="📲")
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel1.mp4")
