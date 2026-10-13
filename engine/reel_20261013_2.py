"""Stop writing proposals from scratch: free AI draft, then make it specific."""
from reel_common import *

ACC = (190, 140, 255)   # lavender
GOLD = (255, 214, 92)
GREEN = (70, 210, 130)
RED = (255, 96, 110)
bg = Background(top=(18, 8, 38), bottom=(36, 16, 70), blobs=[(150, 80, 255), (255, 90, 200), (60, 140, 255)], seed=142)


def card_base(w, h, fill=(250, 250, 252, 255)):
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=32, fill=fill)
    return card, d


def generic_proposal(sub, cx, cy, t, start):
    w, h = 860, 560
    k = p(t, start, 0.45)
    if k <= 0: return
    card, d = card_base(w, h)
    d.text((40, 50), "Proposal #47", font=font(F_XB, 36), fill=(130, 136, 150, 255), anchor="lm")
    lines = ["Dear Sir/Madam,", "I am a hardworking and", "passionate freelancer with", "many skills. I am available", "24/7 and I will do my best", "for your project. Please hire..."]
    for i, ln in enumerate(lines):
        kk = out_cubic(p(t, start + 0.3 + i * 0.18, 0.25))
        d.text((40, 120 + i * 62), ln, font=font(F_SEMI, 40), fill=(*INK, int(255 * kk)), anchor="lm")
    card = with_alpha(card, out_cubic(k))
    sub.alpha_composite(card, (int(cx - w / 2), int(cy - h / 2 + 60 * (1 - out_cubic(k)))))
    ks = p(t, start + 2.0, 0.35)
    if ks > 0:  # rubber stamp
        st = Image.new("RGBA", (420, 140), (0, 0, 0, 0))
        sd = ImageDraw.Draw(st)
        sd.rounded_rectangle([4, 4, 416, 136], radius=20, outline=(*RED, 255), width=10)
        sd.text((210, 70), "GENERIC", font=font(F_BLACK, 76), fill=(*RED, 255), anchor="mm")
        st = st.rotate(-12, resample=Image.BICUBIC, expand=True)
        s = 1.6 - 0.6 * out_cubic(ks)
        st = st.resize((int(st.width * s), int(st.height * s)))
        sub.alpha_composite(with_alpha(st, out_cubic(ks)), (int(cx - st.width / 2 + 120), int(cy - st.height / 2 + 120)))


def chat(sub, cx, cy, t, start):
    w, h = 860, 660
    k = p(t, start, 0.45)
    if k <= 0: return
    card, d = card_base(w, h, fill=(244, 244, 250, 255))
    d.rounded_rectangle([0, 0, w - 1, 84], radius=32, fill=(255, 255, 255, 255))
    d.rectangle([0, 50, w - 1, 84], fill=(255, 255, 255, 255))
    d.text((40, 44), "Free AI chat", font=font(F_XB, 36), fill=INK, anchor="lm")
    d.ellipse([w - 70, 30, w - 42, 58], fill=(*GREEN, 255))
    # user bubble
    ku = out_cubic(p(t, start + 0.4, 0.35))
    if ku > 0:
        a = int(255 * ku)
        d.rounded_rectangle([200, 120, w - 30, 330], radius=28, fill=(124, 92, 255, a))
        ul = ["Write a 3-line proposal", "for this job post. Mention", "their need, 1 sample,", "and end with a question."]
        for i, ln in enumerate(ul):
            d.text((230, 160 + i * 46), ln, font=font(F_SEMI, 34), fill=(255, 255, 255, a), anchor="lm")
    # AI bubble typing
    ka = p(t, start + 1.4, 0.3)
    if ka > 0:
        a = int(255 * out_cubic(ka))
        d.rounded_rectangle([30, 360, w - 170, 620], radius=28, fill=(255, 255, 255, a))
        if t < start + 1.9:
            for j in range(3):
                yy = 490 - 10 * max(0, math.sin(t * 10 - j))
                d.ellipse([70 + j * 40, yy - 10, 90 + j * 40, yy + 10], fill=(160, 166, 180, a))
        else:
            al = ["Hi! You need weekly posts", "for your bakery. Here's a", "sample I made: [link]", "Want 2 post ideas free?"]
            full = " ".join(al)
            n = int(len(full) * p(t, start + 1.9, 1.6))
            done = 0
            for i, ln in enumerate(al):
                part = ln[: max(0, min(len(ln), n - done))]
                done += len(ln) + 1
                d.text((60, 405 + i * 50), part, font=font(F_SEMI, 36), fill=(*INK, a), anchor="lm")
    card = with_alpha(card, out_cubic(k))
    sub.alpha_composite(card, (int(cx - w / 2), int(cy - h / 2 + 60 * (1 - out_cubic(k)))))


def final_proposal(sub, cx, cy, t, start):
    w, h = 860, 470
    k = p(t, start, 0.45)
    if k <= 0: return
    card, d = card_base(w, h)
    d.text((40, 50), "To: Maya · Sweet Crumb Bakery", font=font(F_MED, 32), fill=(130, 136, 150, 255), anchor="lm")
    d.line([40, 90, w - 40, 90], fill=(225, 228, 236, 255), width=3)
    segs = [
        [("Hi ", INK), ("Maya", (130, 70, 230)), ("! Loved your new", INK)],
        [("pumpkin loaf", (130, 70, 230)), (" post. You need", INK)],
        [("weekly posts, so I made a", INK)],
        [("sample", (130, 70, 230)), (": [link]. Want 2 free", INK)],
        [("post ideas for November?", INK)],
    ]
    f = font(F_SEMI, 40)
    for i, row in enumerate(segs):
        kk = out_cubic(p(t, start + 0.3 + i * 0.25, 0.3))
        x = 40
        for txt, col in row:
            d.text((x, 140 + i * 62), txt, font=f, fill=(*col, int(255 * kk)), anchor="lm")
            x += d.textlength(txt, font=f)
    card = with_alpha(card, out_cubic(k))
    sub.alpha_composite(card, (int(cx - w / 2), int(cy - h / 2 + 60 * (1 - out_cubic(k)))))


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, 0.0, 0.3)
        place_emoji(sub, "✍️", W / 2, 560 + 14 * math.sin(t * 6), 200 * out_back(k), alpha=k, rot=8 * math.sin(t * 4))
        pop_words(sub, ["Stop writing", "proposals", "from scratch"], t, 0.0, 990, 110, (WHITE, ACC), gap=0.06, highlight={"stop", "scratch"})
        pill(sub, W / 2, 1380, "Free AI draft + your 2-min fix", F_SEMI, 46, WHITE, INK, alpha=out_cubic(p(t, 1.3, 0.4)), scale=out_back(p(t, 1.3, 0.4)), icon="🤖")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Don't send proposals", "that look like this"], t, s1 + 0.1, 350, 80, (WHITE, RED), gap=0.07, highlight={"don't"})
        generic_proposal(sub, W / 2, 780, t, s1 + 0.5)
        tags = [("Same text for every job", 3.4, "📋"), ("All about you, not them", 4.2, "🙄")]
        for i, (lab, at, ic) in enumerate(tags):
            kk = p(t, s1 + at, 0.35)
            pill(sub, W / 2, 1160 + i * 118, lab, F_SEMI, 46, (255, 236, 238), (190, 30, 50), alpha=out_cubic(kk), scale=out_back(kk), icon=ic)
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Let AI write", "the first draft"], t, s2 + 0.1, 350, 86, (WHITE, ACC), gap=0.07, highlight={"first", "draft"})
        chat(sub, W / 2, 830, t, s2 + 0.4)
        checklist(sub, t, s2 + 4.4, ["Then make it yours:"], 1250, 100, ACC, size=52, x0=210, icon="👇")
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Add 1 real detail", "about THEM"], t, s3 + 0.1, 340, 86, (WHITE, GOLD), gap=0.07, highlight={"real", "them"})
        final_proposal(sub, W / 2, 720, t, s3 + 0.4)
        checklist(sub, t, s3 + 2.4, ["Their name", "Something from their page", "A question to reply to"], 1050, 100, GOLD, size=50, x0=190, every=0.6)
        draw_text(sub, "Never paste AI text unread. Results depend on your work.", F_MED, 32, W / 2, 1430, SOFT, alpha=out_cubic(p(t, s3 + 4.6, 0.5)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel2.mp4")
