"""Copy this reply when a client says "too expensive" (client asks for a discount, part 2)."""
from reel_common import *

ACC = (160, 140, 255)   # lilac
GOLD = (255, 214, 92)
RED = (255, 90, 100)
GREEN = (60, 205, 130)
BLUE = (60, 140, 255)
bg = Background(top=(16, 12, 44), bottom=(34, 20, 78), blobs=[(130, 90, 255), (60, 140, 255), (255, 110, 190)], seed=2872)


def bubble_img(lines, me, size=42, w=700):
    h = 44 + int(size * 1.35) * len(lines)
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    fill = (*BLUE, 255) if me else (236, 238, 244, 255)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=34, fill=fill)
    for i, ln in enumerate(lines):
        d.text((32, 22 + int(size * 1.35) * i + size * 0.68), ln, font=font(F_SEMI, size), fill=(255, 255, 255, 255) if me else INK, anchor="lm")
    return im


def typed(lines, k):
    """Reveal characters across lines by progress k (0..1)."""
    total = sum(len(l) for l in lines)
    n = int(total * k)
    out = []
    for l in lines:
        out.append(l[:max(0, n)])
        n -= len(l)
    return out


def phone(sub, t, start, msgs, cx=W / 2, cy=930, h=1060):
    """msgs: list of (lines, me, appear_time, type_dur)."""
    w = 820
    k = p(t, start, 0.45)
    if k <= 0: return
    ph = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(ph)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=60, fill=(20, 20, 28, 255))
    d.rounded_rectangle([18, 18, w - 19, h - 19], radius=46, fill=(255, 255, 255, 255))
    d.rounded_rectangle([18, 18, w - 19, 150], radius=46, fill=(246, 247, 251, 255))
    d.rectangle([18, 110, w - 19, 150], fill=(246, 247, 251, 255))
    d.ellipse([50, 50, 130, 130], fill=(*GOLD, 255))
    d.text((90, 90), "C", font=font(F_BLACK, 44), fill=INK, anchor="mm")
    d.text((150, 72), "Corner Café", font=font(F_XB, 38), fill=INK, anchor="lm")
    d.text((150, 112), "Client", font=font(F_MED, 30), fill=(120, 126, 140, 255), anchor="lm")
    y = 180
    for lines, me, at, dur in msgs:
        kk = p(t, at, 0.3)
        if kk <= 0: continue
        shown = typed(lines, p(t, at, dur)) if (me and dur > 0) else lines
        b = bubble_img(lines, me)
        # draw typed text: rebuild with shown lines but same size
        b = bubble_img([s if s else " " for s in shown], me)
        x = w - 40 - b.width if me else 40
        ph.alpha_composite(with_alpha(b, out_cubic(kk)), (x, int(y + 30 * (1 - out_cubic(kk)))))
        y += b.height + 26
    sub.alpha_composite(with_alpha(ph, out_cubic(k)), (int(cx - w / 2), int(cy - h / 2 + 80 * (1 - out_cubic(k)))))


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, 0.0, 0.3)
        place_emoji(sub, "📋", W / 2, 520 + 12 * math.sin(t * 6), 200 * out_back(k), alpha=k, rot=5 * math.sin(t * 4))
        pop_words(sub, ["Copy this reply to", "\"too expensive\""], t, 0.0, 920, 108, (WHITE, GOLD), gap=0.07, highlight={"\"too", "expensive\""})
        pill(sub, W / 2, 1230, "Keeps the client AND your rate", F_SEMI, 46, WHITE, INK, alpha=out_cubic(p(t, 1.2, 0.4)), scale=out_back(p(t, 1.2, 0.4)), icon="🤝")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["They message you:"], t, s1 + 0.1, 330, 80, (WHITE, ACC), gap=0.07, highlight={"you:"})
        kb = p(t, s1 + 0.5, 0.4)
        if kb > 0:
            b = bubble_img(["Hmm, that's a bit too", "expensive for us..."], False, size=48, w=760)
            sub.alpha_composite(with_alpha(b, out_cubic(kb)), (int(W / 2 - 380), int(470 + 40 * (1 - out_cubic(kb)))))
        pop_words(sub, ["Don't reply like this:"], t, s1 + 1.8, 830, 64, (WHITE, RED), gap=0.06, highlight={"don't"})
        wrong = [("\"Ok, I'll do $50 off\"", 2.6), ("\"But I'm worth it!\"", 3.6)]
        for i, (lab, at) in enumerate(wrong):
            kk = p(t, s1 + at, 0.35)
            pill(sub, W / 2, 990 + i * 130, lab, F_SEMI, 48, (255, 236, 238), (190, 30, 50), alpha=out_cubic(kk), scale=out_back(kk), icon="❌")
        kk = p(t, s1 + 4.8, 0.4)
        pill(sub, W / 2, 1310, "Panic discount or argument = lost", F_XB, 42, GOLD, INK, alpha=out_cubic(kk), scale=out_back(kk), icon="😬")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Send this instead"], t, s2 + 0.1, 300, 84, (WHITE, ACC), gap=0.07, highlight={"instead"})
        msgs = [
            (["Hmm, that's a bit too", "expensive for us..."], False, s2 + 0.5, 0),
            (["Totally understand!", "What budget did you", "have in mind? I can", "adjust what's included", "so it fits."], True, s2 + 1.1, 3.2),
        ]
        phone(sub, t, s2 + 0.3, msgs, cy=920, h=900)
        steps = [("1. Agree, stay calm", 1.4), ("2. Ask their budget", 2.6), ("3. Adjust scope, not rate", 4.0)]
        for lab, at in steps:
            kk = p(t, s2 + at, 0.3)
            if kk > 0 and t < s2 + at + 1.5:
                a = out_cubic(kk) * (1 - p(t, s2 + at + 1.2, 0.3))
                pill(sub, W / 2, 1460, lab, F_XB, 50, GOLD, INK, alpha=a, scale=out_back(kk), icon="👉")
        kk = p(t, s2 + 5.6, 0.4)
        pill(sub, W / 2, 1460, "Screenshot this reply", F_XB, 50, WHITE, INK, alpha=out_cubic(kk), scale=out_back(kk), icon="📸")
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Example outcome"], t, s3 + 0.1, 290, 84, (WHITE, GOLD), gap=0.07, highlight={"outcome"})
        msgs = [
            (["Our max is $300."], False, s3 + 0.5, 0),
            (["Perfect. For $300:", "logo + 2 social posts.", "Want me to start?"], True, s3 + 1.2, 1.8),
            (["Yes, let's do it! 🙌" if False else "Yes, let's do it!"], False, s3 + 3.4, 0),
        ]
        phone(sub, t, s3 + 0.2, msgs, cy=830, h=760)
        for i, (lab, at) in enumerate([("Client kept", 4.2), ("Rate kept", 4.7)]):
            kk = p(t, s3 + at, 0.35)
            pill(sub, W / 2 - 210 + i * 420, 1300, lab, F_XB, 46, GREEN, INK, alpha=out_cubic(kk), scale=out_back(kk), icon="✅")
        draw_text(sub, "Example pricing. Results depend on your work.", F_MED, 36, W / 2, 1430, SOFT, alpha=out_cubic(p(t, s3 + 5.0, 0.5)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel2.mp4")
