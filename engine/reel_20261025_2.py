"""Thanksgiving is 32 days away. Shops forget this -- set Google 'special hours' for the holidays (manager access, 3 steps)."""
from reel_maps import *

ACC = (255, 160, 70)    # pumpkin orange
GOLD = (255, 220, 110)
RED = (255, 90, 100)
bg = Background(top=(34, 12, 6), bottom=(52, 22, 8), blobs=[(255, 120, 40), (220, 70, 40), (255, 190, 60)], seed=2982)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, 0.0, 0.3)
        place_emoji(sub, "🦃", W / 2, 470 - 16 * math.sin(t * 5), 210 * out_back(k), alpha=k, rot=6 * math.sin(t * 4))
        pop_words(sub, ["Thanksgiving is", "32 days away.", "Shops forget this"], t, 0.0, 860, 104, (WHITE, ACC), gap=0.07, highlight={"32", "days", "forget"})
        kp = p(t, 1.5, 0.4)
        pill(sub, W / 2, 1150, "A 10-minute Google fix", F_XB, 50, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="⏱️")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Hours change on", "these days"], t, s1 + 0.1, 300, 86, (WHITE, GOLD), gap=0.08, highlight={"these", "days"})
        mini_calendar(sub, t, s1 + 0.6, 790, ACC, {26: ("Thanksgiving", s1 + 1.6), 27: ("Black Friday", s1 + 2.2)})
        kx = p(t, s1 + 3.0, 0.4)
        pill(sub, W / 2, 1200, "26 Thanksgiving · 27 Black Friday", F_XB, 44, WHITE, INK, alpha=out_cubic(kx), scale=out_back(kx), icon="📅")
        kq = p(t, s1 + 4.2, 0.4)
        pill(sub, W / 2, 1330, "Then Christmas Eve, Christmas, NYE", F_SEMI, 40, (255, 236, 220), INK, alpha=out_cubic(kq), scale=out_back(kq), icon="🎄")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["How to set it up", "for a local shop"], t, s2 + 0.1, 300, 82, (WHITE, ACC), gap=0.07, highlight={"set", "up"})
        steps = [("1", "Owner adds you as a", "manager on their profile", "👤"),
                 ("2", "Edit profile → Hours", "→ Special hours", "🛠️"),
                 ("3", "Enter the dates + hours", "the owner gave you", "✍️")]
        for i, (n, a, b, ic) in enumerate(steps):
            kk = p(t, s2 + 1.0 + i * 1.1, 0.45)
            if kk <= 0: continue
            c, d = card_base(880, 210)
            d.rounded_rectangle([30, 45, 150, 165], radius=60, fill=(*ACC, 255))
            d.text((90, 105), n, font=font(F_BLACK, 64), fill=(*INK, 255), anchor="mm")
            d.text((185, 78), a, font=font(F_XB, 44), fill=(*INK, 255), anchor="lm")
            d.text((185, 138), b, font=font(F_SEMI, 38), fill=(90, 96, 110, 255), anchor="lm")
            e = emoji_img(ic, 70)
            c.alpha_composite(e, (880 - 40 - e.width, int(105 - e.height / 2)))
            paste_card(sub, c, t, s2 + 1.0 + i * 1.1, W / 2 + 80 * (1 - out_cubic(kk)), 560 + i * 245, dy=0)
        kp = p(t, s2 + 5.0, 0.4)
        pill(sub, W / 2, 1340, "No password sharing needed", F_XB, 48, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="🔒")
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Example: a bakery's", "holiday hours"], t, s3 + 0.1, 290, 72, (WHITE, GOLD), gap=0.07, highlight={"holiday", "hours"})
        rows = [("Nov 26", "Thanksgiving", "Closed", s3 + 0.9),
                ("Nov 27", "Black Friday", "7am-8pm", s3 + 1.4),
                ("Dec 24", "Christmas Eve", "8am-2pm", s3 + 1.9),
                ("Dec 25", "Christmas", "Closed", s3 + 2.4),
                ("Dec 31", "New Year's Eve", "8am-4pm", s3 + 2.9)]
        hours_editor(sub, t, s3 + 0.5, 790, rows, ACC, h=740)
        kp = p(t, s3 + 4.0, 0.4)
        pill(sub, W / 2, 1270, "Done in about 10 minutes", F_XB, 48, ACC, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="✅")
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel2.mp4")
