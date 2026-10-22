"""Pitch this to 3 shops on Instagram tonight -- find shops with no email plan and send one DM."""
from reel_email import *

ACC = (255, 120, 200)   # pink
GOLD = (255, 214, 92)
SKY = (110, 190, 255)
bg = Background(top=(10, 12, 44), bottom=(30, 20, 80), blobs=[(255, 90, 180), (90, 110, 255), (180, 90, 255)], seed=2953)

PITCH = ("Hi Lena! Love the new fall candles. Black Friday is 5 weeks out. "
         "Want me to write your 3 sale emails? I'll send you 1 free subject line first.")


def search_bar(sub, t, start, cy, query):
    k = p(t, start, 0.4)
    if k <= 0: return
    w, h = 860, 120
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=60, fill=(245, 246, 250, 255))
    card.alpha_composite(emoji_img("🔍", 56), (40, 32))
    s = query[:int(len(query) * p(t, start + 0.3, 1.2))]
    caret = "|" if (t * 2) % 1 < 0.5 else ""
    d.text((120, 60), s + caret, font=font(F_XB, 46), fill=(*INK, 255), anchor="lm")
    card = with_alpha(card, out_cubic(k))
    sub.alpha_composite(card, (int(W / 2 - w / 2), int(cy - h / 2 + 40 * (1 - out_cubic(k)))))


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, 0.0, 0.3)
        place_emoji(sub, "📲", W / 2, 470 - 16 * math.sin(t * 6), 170 * out_back(k), alpha=k)
        pop_words(sub, ["Pitch this to", "3 shops on", "Instagram tonight"], t, 0.0, 820, 92, (WHITE, ACC), gap=0.08, highlight={"3", "shops", "tonight"})
        kp = p(t, 1.4, 0.4)
        pill(sub, W / 2, 1160, "Black Friday email gig", F_XB, 52, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), pad=(44, 22), icon="🛍️")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Step 1: find the shops"], t, s1 + 0.1, 300, 80, (WHITE, ACC), gap=0.08, highlight={"find"})
        search_bar(sub, t, s1 + 0.5, 480, "#shopsmall + your city")
        draw_text(sub, "Look for shops that:", F_XB, 50, W / 2, 660, SOFT, alpha=out_cubic(p(t, s1 + 1.8, 0.4)))
        checklist(sub, t, s1 + 2.2, ["Posted this week", "Have a shop link in bio", "Sell physical products", "No sign-up for emails"], 790, 125, ACC, size=52, x0=160)
        kp = p(t, s1 + 5.4, 0.4)
        pill(sub, W / 2, 1360, "Pick 3. That's tonight's list.", F_XB, 50, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="🎯")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Step 2: send this DM"], t, s2 + 0.1, 290, 84, (WHITE, ACC), gap=0.08, highlight={"dm"})
        phone_chat(sub, t, s2 + 0.3, W / 2, 380, [
            ("me", PITCH, s2 + 0.6, "typed"),
        ], header="Lena's Candles", h=560)
        labels = [("1", "A real compliment"), ("2", "The deadline"), ("3", "A free first step")]
        for i, (n, lab) in enumerate(labels):
            kk = p(t, s2 + 3.6 + i * 0.8, 0.4)
            pill(sub, W / 2, 1100 + i * 120, f"{n}. {lab}", F_XB, 50, GOLD if i == 2 else (245, 246, 250), INK, alpha=out_cubic(kk), scale=out_back(kk))
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["When they reply"], t, s3 + 0.1, 300, 88, (WHITE, ACC), gap=0.08, highlight={"reply"})
        notification(sub, t, s3 + 0.5, 500, "Lena's Candles", "Love it! How much for all 3?", icon="🕯️")
        phone_chat(sub, t, s3 + 1.6, W / 2, 640, [
            ("them", "How much for all 3?", s3 + 1.7, None),
            ("me", "$150 for 3 emails, ready by Nov 13. Want the free subject line now?", s3 + 2.3, "typed"),
        ], header="Lena's Candles", h=620)
        kq = p(t, s3 + 4.8, 0.45)
        draw_text(sub, "Example chat & pricing. Results depend on your work.", F_MED, 34, W / 2, 1360, SOFT, alpha=out_cubic(kq))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel3.mp4")
