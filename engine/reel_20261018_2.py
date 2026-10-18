"""Stop typing your client call notes (Free AI for freelancers, part 2)."""
from reel_common import *

ACC = (255, 150, 70)    # orange
GOLD = (255, 214, 100)
GREEN = (80, 220, 150)
RED = (255, 96, 110)
bg = Background(top=(36, 14, 10), bottom=(60, 26, 12), blobs=[(255, 120, 50), (255, 190, 80), (220, 70, 90)], seed=2922)

OUTPUT = [("📌", "Tasks: 3 logo options"), ("📅", "Deadline: Friday"), ("💬", "Colors: green + cream"), ("📧", "Recap email: drafted")]


def phone(t, start, w=560, h=900):
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=70, fill=(20, 20, 26, 255))
    d.rounded_rectangle([18, 18, w - 19, h - 19], radius=56, fill=(250, 248, 246, 255))
    d.rounded_rectangle([w / 2 - 70, 34, w / 2 + 70, 62], radius=14, fill=(20, 20, 26, 255))
    d.text((w / 2, 130), "Voice Memo", font=font(F_XB, 40), fill=(*INK, 255), anchor="mm")
    d.text((w / 2, 180), "Client call · Logo", font=font(F_MED, 30), fill=(120, 120, 130, 255), anchor="mm")
    el = max(0, t - start)
    mm, ss = int(el * 37) // 60, int(el * 37) % 60
    d.text((w / 2, 300), f"{mm:02d}:{ss:02d}", font=font(F_BLACK, 90), fill=(*INK, 255), anchor="mm")
    for i in range(22):
        x = 60 + i * 20
        amp = 20 + 70 * abs(math.sin(t * 7 + i * 0.9)) * abs(math.sin(i * 1.7 + t * 2))
        d.rounded_rectangle([x, 470 - amp, x + 10, 470 + amp], radius=5, fill=(*ACC, 255))
    pulse = 1 + 0.08 * math.sin(t * 6)
    r = 70 * pulse
    d.ellipse([w / 2 - r, 690 - r, w / 2 + r, 690 + r], fill=(*RED, 255))
    d.rounded_rectangle([w / 2 - 26, 664, w / 2 + 26, 716], radius=8, fill=(255, 255, 255, 255))
    return im


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = clamp(p(t, 0.0, 0.3) + 0.4)
        place_emoji(sub, "📝", W / 2 - 60, 500, 190 * out_back(k), alpha=k, rot=-8)
        kx = p(t, 0.6, 0.35)
        place_emoji(sub, "🚫", W / 2 + 90, 520, 150 * out_back(kx), alpha=out_cubic(kx))
        pop_words(sub, ["Stop typing", "your client", "call notes"], t, -0.25, 930, 116, (WHITE, ACC), gap=0.07, highlight={"stop", "notes"})
        kk = p(t, 1.3, 0.4)
        pill(sub, W / 2, 1320, "Let free AI do this part", F_SEMI, 46, WHITE, INK, alpha=out_cubic(kk), scale=out_back(kk), icon="🤖")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Typing while they talk", "= missed details"], t, s1 + 0.1, 330, 76, (WHITE, RED), gap=0.07, highlight={"missed", "details"})
        miss = [("Their budget?", 600), ("The deadline??", 790), ("Which colors???", 980)]
        for i, (lab, y) in enumerate(miss):
            k = p(t, s1 + 1.2 + i * 0.7, 0.4)
            pill(sub, W / 2 + (-90 if i % 2 else 90), y, lab, F_XB, 58, WHITE, INK, alpha=out_cubic(k), scale=out_back(k), pad=(50, 26), icon="❓")
        kk = p(t, s1 + 3.8, 0.4)
        pill(sub, W / 2, 1260, "Then you email back to ask. Again.", F_XB, 44, RED, WHITE, alpha=out_cubic(kk), scale=out_back(kk), icon="😬")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        if t < s2 + 4.0:
            pop_words(sub, ["1. Ask: OK to record?", "2. Hit record"], t, s2 + 0.1, 300, 70, (WHITE, ACC), gap=0.06, highlight={"ok", "record?"})
            kp = p(t, s2 + 0.5, 0.45)
            if kp > 0:
                ph = phone(t, s2 + 0.5).resize((476, 765))
                a = out_cubic(kp) * (1 - out_cubic(p(t, s2 + 3.6, 0.4)))
                sub.alpha_composite(with_alpha(ph, a), (int(W / 2 - 238), int(470 + 60 * (1 - out_cubic(kp)))))
        else:
            pop_words(sub, ["3. Paste the transcript", "into a free AI chat"], t, s2 + 4.0, 300, 70, (WHITE, ACC), gap=0.06, highlight={"transcript", "free"})
            kb = p(t, s2 + 4.6, 0.45)
            if kb > 0:
                box = Image.new("RGBA", (840, 420), (0, 0, 0, 0)); bd = ImageDraw.Draw(box)
                bd.rounded_rectangle([0, 0, 839, 419], radius=36, fill=(255, 255, 255, 250))
                bd.text((40, 60), "Your prompt", font=font(F_XB, 34), fill=(160, 100, 40, 255), anchor="lm")
                lines = ["Turn this call into:", "• a task list with deadlines", "• open questions", "• a short recap email"]
                for i, ln in enumerate(lines):
                    kl = p(t, s2 + 5.0 + i * 0.45, 0.3)
                    bd.text((40, 140 + i * 66), ln, font=font(F_SEMI if i else F_XB, 42), fill=(*INK, int(255 * out_cubic(kl))), anchor="lm")
                sub.alpha_composite(with_alpha(box, out_cubic(kb)), (120, int(560 + 50 * (1 - out_cubic(kb)))))
            kk = p(t, s2 + 6.8, 0.35)
            pill(sub, W / 2, 1170, "Save this prompt", F_XB, 48, GOLD, INK, alpha=out_cubic(kk), scale=out_back(kk), icon="📋")
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["A minute later"], t, s3 + 0.1, 300, 84, (WHITE, GREEN), gap=0.07, highlight={"minute", "later"})
        kc = p(t, s3 + 0.5, 0.45)
        if kc > 0:
            card = Image.new("RGBA", (840, 560), (0, 0, 0, 0)); cd = ImageDraw.Draw(card)
            cd.rounded_rectangle([0, 0, 839, 559], radius=40, fill=(255, 255, 255, 250))
            cd.text((40, 60), "Call summary", font=font(F_BLACK, 44), fill=(*INK, 255), anchor="lm")
            for i, (em, lab) in enumerate(OUTPUT):
                kl = p(t, s3 + 1.1 + i * 0.6, 0.35)
                if kl <= 0: continue
                y = 150 + i * 100
                e = with_alpha(emoji_img(em, 56).copy(), out_cubic(kl)); card.alpha_composite(e, (40, int(y + 40 - e.height / 2)))
                cd.text((135, y + 40), lab, font=font(F_XB, 42), fill=(*INK, int(255 * out_cubic(kl))), anchor="lm")
                if t > s3 + 1.4 + i * 0.6:
                    ce = emoji_img("✅", 50); card.alpha_composite(ce, (760, int(y + 40 - ce.height / 2)))
            sub.alpha_composite(with_alpha(card, out_cubic(kc)), (120, int(440 + 50 * (1 - out_cubic(kc)))))
        kk = p(t, s3 + 4.0, 0.4)
        pill(sub, W / 2, 1150, "Send the recap same day = pro", F_XB, 48, GREEN, INK, alpha=out_cubic(kk), scale=out_back(kk), icon="🚀")
        draw_text(sub, "Always read it before sending. AI can get details wrong.", F_MED, 33, W / 2, 1290, SOFT, alpha=out_cubic(p(t, s3 + 4.6, 0.5)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel2.mp4")
