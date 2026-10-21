"""No reply? Send this on day 3 -- a short follow-up DM with one idea and one easy question."""
from reel_chat import *

ACC = (64, 224, 170)    # mint
GOLD = (255, 214, 92)
RED = (255, 96, 110)
bg = Background(top=(6, 30, 32), bottom=(10, 58, 66), blobs=[(30, 200, 160), (40, 140, 220), (90, 230, 140)], seed=2941)

DAY3 = "Hi Maya! Quick idea: a \"Gift boxes\" section on your menu page for the holidays. I can mock it up by Friday. Want a 2-line plan?"


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, 0.0, 0.3)
        place_emoji(sub, "📵", W / 2, 470 - 16 * math.sin(t * 6), 180 * out_back(k), alpha=k)
        pop_words(sub, ["No reply?", "Send this on day 3"], t, 0.0, 800, 94, (WHITE, ACC), gap=0.08, highlight={"day", "3"})
        kp = p(t, 1.3, 0.4)
        pill(sub, W / 2, 1080, "Copy-paste follow-up", F_BLACK, 58, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), pad=(50, 24), icon="📋")
        kq = p(t, 1.9, 0.4)
        draw_text(sub, "Works in email, DMs and LinkedIn", F_SEMI, 46, W / 2, 1230, SOFT, alpha=out_cubic(kq))
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Seen. No reply.", "Now what?"], t, s1 + 0.1, 300, 92, (WHITE, RED), gap=0.08, highlight={"no", "reply."})
        phone_chat(sub, t, s1 + 0.4, W / 2, 440, [
            ("me", "Hi Maya, I design menu pages for local cafes. Want a free tip for yours?", s1 + 0.7, "Seen Monday"),
        ], h=520)
        kx = p(t, s1 + 2.0, 0.35)
        place_emoji(sub, "🦗", W / 2, 1060, 130 * out_back(kx), alpha=out_cubic(kx))
        kp = p(t, s1 + 3.0, 0.4)
        pill(sub, W / 2, 1230, "Silence usually means \"busy\"", F_XB, 48, (245, 246, 250), INK, alpha=out_cubic(kp), scale=out_back(kp), icon="⏳")
        kp2 = p(t, s1 + 3.9, 0.4)
        pill(sub, W / 2, 1390, "Not \"no\". So follow up once.", F_XB, 48, ACC, INK, alpha=out_cubic(kp2), scale=out_back(kp2))
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Day 3 message"], t, s2 + 0.1, 290, 92, (WHITE, ACC), gap=0.08, highlight={"3"})
        phone_chat(sub, t, s2 + 0.3, W / 2, 380, [
            ("me", "Want a free tip for your menu page?", s2 + 0.3, "Seen Mon"),
            ("me", DAY3, s2 + 0.9, "typed"),
        ], h=810)
        labels = [("1", "Their name"), ("2", "One specific idea"), ("3", "One easy yes/no")]
        for i, (n, lab) in enumerate(labels):
            kk = p(t, s2 + 3.6 + i * 0.8, 0.4)
            pill(sub, W / 2, 1280 + i * 115, f"{n}. {lab}", F_XB, 48, GOLD if i == 2 else (245, 246, 250), INK, alpha=out_cubic(kk), scale=out_back(kk))
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Keep it short", "and easy to answer"], t, s3 + 0.1, 330, 88, (WHITE, GOLD), gap=0.08, highlight={"short", "easy"})
        checklist(sub, t, s3 + 0.9, ["Under 40 words", "Something new to offer", "No guilt trip", "One question only"], 600, 130, ACC, size=54, x0=170)
        notification(sub, t, s3 + 4.2, 1250, "Maya's Bakery", "Yes, send the plan!", icon="🧁")
        draw_text(sub, "Example message. Results depend on your work.", F_MED, 34, W / 2, 1440, SOFT, alpha=out_cubic(p(t, s3 + 4.8, 0.5)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel1.mp4")
