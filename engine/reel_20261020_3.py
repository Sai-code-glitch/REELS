"""No contract yet? Send this scope email first and get an "Agreed" reply."""
from reel_common import *

ACC = (190, 130, 255)   # violet
GOLD = (255, 214, 92)
RED = (255, 96, 110)
GREEN = (80, 220, 140)
bg = Background(top=(20, 8, 40), bottom=(46, 18, 86), blobs=[(150, 80, 255), (230, 80, 200), (80, 120, 255)], seed=2933)

EMAIL = [
    ("Hi Maya! Before I start, confirming:", (60, 64, 80)),
    ("• 5 product photos, edited", INK),
    ("• $200 total, $100 upfront", INK),
    ("• Delivered by Friday", INK),
    ("• 2 rounds of edits included", INK),
    ("Reply \"Agreed\" and I'll begin!", (120, 60, 200)),
]


def email_card(sub, t, start):
    w, h = 900, 900
    k = p(t, start, 0.4)
    if k <= 0: return
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=36, fill=(252, 252, 255, 255))
    d.text((44, 56), "New message", font=font(F_XB, 40), fill=(120, 60, 200, 255), anchor="lm")
    d.text((44, 130), "To: maya@shop.com", font=font(F_MED, 34), fill=(110, 116, 130, 255), anchor="lm")
    d.text((44, 185), "Subject: Project details", font=font(F_SEMI, 36), fill=(*INK, 255), anchor="lm")
    d.line([44, 225, w - 44, 225], fill=(225, 225, 235, 255), width=3)
    for i, (s, col) in enumerate(EMAIL):
        ty = p(t, start + 0.5 + i * 0.85, 0.7)
        y = 290 + i * 88
        if ty <= 0: continue
        d.text((44, y), s[:int(len(s) * ty)], font=font(F_SEMI, 42 if i else 38), fill=(*col, 255), anchor="lm")
    ks = p(t, start + 5.9, 0.4)
    if ks > 0:
        sc = out_back(ks)
        bw, bh = 220 * sc, 80 * sc
        cx, cy = w - 160, h - 80
        d.rounded_rectangle([cx - bw / 2, cy - bh / 2, cx + bw / 2, cy + bh / 2], radius=40, fill=(120, 60, 200, int(255 * out_cubic(ks))))
        d.text((cx, cy), "Send", font=font(F_BLACK, max(4, int(40 * sc))), fill=(255, 255, 255, 255), anchor="mm")
    card = with_alpha(card, out_cubic(k))
    sub.alpha_composite(card, (int(W / 2 - w / 2), int(450 + 60 * (1 - out_cubic(k)))))


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, 0.0, 0.3)
        place_emoji(sub, "✉️", W / 2, 470 - 16 * math.sin(t * 6), 170 * out_back(k), alpha=k)
        pop_words(sub, ["No contract yet?", "Send this email first"], t, 0.0, 800, 92, (WHITE, ACC), gap=0.08, highlight={"email", "first"})
        kp = p(t, 1.4, 0.4)
        pill(sub, W / 2, 1080, "Takes 2 minutes", F_BLACK, 58, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), pad=(48, 24), icon="⏱️")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Deals made in", "DMs get forgotten"], t, s1 + 0.1, 340, 92, (WHITE, RED), gap=0.08, highlight={"forgotten"})
        kc = p(t, s1 + 1.0, 0.4)
        pill(sub, W / 2, 620, "\"Sure, let's do it!\"", F_SEMI, 50, (245, 246, 250), INK, alpha=out_cubic(kc), scale=out_back(kc), pad=(44, 28), icon="💬")
        ka = p(t, s1 + 1.8, 0.4)
        draw_text(sub, "...do what? for how much? by when?", F_XB, 50, W / 2, 790, SOFT, alpha=out_cubic(ka))
        for i, q in enumerate(["What?", "How much?", "When?"]):
            kk = p(t, s1 + 2.6 + i * 0.4, 0.4)
            pill(sub, [240, 530, 840][i], 960, q, F_BLACK, 46, RED, WHITE, alpha=out_cubic(kk), scale=out_back(kk), pad=(34, 24))
        kp = p(t, s1 + 4.4, 0.4)
        pill(sub, W / 2, 1180, "Put the deal in one email", F_XB, 50, ACC, INK, alpha=out_cubic(kp), scale=out_back(kp), pad=(44, 26))
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Copy this", "scope email"], t, s2 + 0.1, 320, 96, (WHITE, ACC), gap=0.08, highlight={"scope", "email"})
        email_card(sub, t, s2 + 0.4)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Wait for the", "magic word"], t, s3 + 0.1, 320, 96, (WHITE, GOLD), gap=0.08, highlight={"magic", "word"})
        # phone notification sliding in
        kn = p(t, s3 + 0.9, 0.5)
        if kn > 0:
            nw, nh = 860, 190
            card = Image.new("RGBA", (nw, nh), (0, 0, 0, 0))
            d = ImageDraw.Draw(card)
            d.rounded_rectangle([0, 0, nw - 1, nh - 1], radius=40, fill=(250, 250, 255, 255))
            d.text((150, 60), "Maya  ·  now", font=font(F_SEMI, 34), fill=(110, 116, 130, 255), anchor="lm")
            d.text((150, 125), "Agreed! Sending the deposit.", font=font(F_XB, 44), fill=(*INK, 255), anchor="lm")
            card = with_alpha(card, out_cubic(kn))
            y = int(560 - 140 * (1 - out_cubic(kn)))
            sub.alpha_composite(card, (int(W / 2 - nw / 2), y))
            place_emoji(sub, "📩", W / 2 - nw / 2 + 80, y + nh / 2, 90, alpha=out_cubic(kn))
        kk = p(t, s3 + 1.7, 0.4)
        pill(sub, W / 2, 900, "Your written record", F_BLACK, 56, GREEN, INK, alpha=out_cubic(kk), scale=out_back(kk), pad=(46, 26), icon="✅")
        k3 = p(t, s3 + 2.5, 0.4)
        draw_text(sub, "Example: $200 job, 50% upfront", F_XB, 48, W / 2, 1060, WHITE, alpha=out_cubic(k3))
        k4 = p(t, s3 + 2.8, 1.3)
        if k4 > 0:
            draw_text(sub, f"${int(round(100 * out_cubic(k4)))}", F_BLACK, 170, W / 2, 1200, GOLD, alpha=out_cubic(p(t, s3 + 2.8, 0.3)))
            draw_text(sub, "before you lift a finger", F_XB, 48, W / 2, 1320, ACC, alpha=out_cubic(p(t, s3 + 3.0, 0.3)))
        draw_text(sub, "Example pricing. Results depend on your work.", F_MED, 34, W / 2, 1420, SOFT, alpha=out_cubic(p(t, s3 + 3.6, 0.5)))
        draw_text(sub, "Not legal advice. Big jobs: use a real contract.", F_MED, 34, W / 2, 1475, SOFT, alpha=out_cubic(p(t, s3 + 3.8, 0.5)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel3.mp4")
