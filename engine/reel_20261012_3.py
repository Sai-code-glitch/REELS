"""Search this on LinkedIn tonight: find people posting that they need a freelancer."""
from reel_common import *

ACC = (80, 200, 255)    # cyan
GOLD = (255, 214, 92)
GREEN = (70, 210, 130)
RED = (255, 96, 110)
LBLUE = (10, 102, 194)
bg = Background(top=(4, 14, 34), bottom=(8, 30, 64), blobs=[(40, 140, 255), (40, 220, 220), (90, 80, 255)], seed=97)
QUERY = '"looking for a freelance"'


def search_bar(sub, cx, cy, t, start, w=860, typed_dur=1.0):
    k = out_back(p(t, start, 0.4))
    if k <= 0: return
    h = 120
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=60, fill=(250, 250, 252, 255))
    d.ellipse([40, 38, 80, 78], outline=(130, 136, 150, 255), width=6)
    d.line([74, 72, 92, 90], fill=(130, 136, 150, 255), width=7)
    n = int(len(QUERY) * p(t, start + 0.2, typed_dur))
    txt = QUERY[:n]
    f = font(F_SEMI, 44)
    d.text((115, 60), txt, font=f, fill=INK, anchor="lm")
    if (t * 2) % 1 < 0.5 and n < len(QUERY) + 1:
        x = 115 + d.textlength(txt, font=f) + 4
        d.line([x, 34, x, 86], fill=(*LBLUE, 255), width=4)
    card = card.resize((max(1, int(w * k)), max(1, int(h * k))))
    sub.alpha_composite(card, (int(cx - card.width / 2), int(cy - card.height / 2)))


def filters(sub, t, start, cy):
    chips = [("Posts", 0.0), ("Latest", 0.5), ("Past 24 hours", 1.0)]
    d = ImageDraw.Draw(sub)
    f = font(F_XB, 40)
    widths = [d.textlength(c, font=f) + 70 for c, _ in chips]
    x = W / 2 - (sum(widths) + 24 * 2) / 2
    for (c, at), wd in zip(chips, widths):
        kk = p(t, start + at, 0.35)
        if kk > 0:
            on = t > start + at + 0.35
            pill(sub, x + wd / 2, cy, c, F_XB, 40, (20, 140, 70) if on else (230, 234, 242), WHITE if on else INK, alpha=out_cubic(kk), scale=out_back(kk), pad=(35, 18))
        x += wd + 24


def post_card(sub, cx, cy, t, start):
    w, h = 860, 400
    k = p(t, start, 0.45)
    if k <= 0: return
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=32, fill=(250, 250, 252, 255))
    d.ellipse([36, 30, 116, 110], fill=(255, 170, 90, 255))
    d.text((76, 70), "J", font=font(F_XB, 40), fill=(255, 255, 255, 255), anchor="mm")
    d.text((140, 55), "Jordan · Fitness Coach", font=font(F_XB, 38), fill=INK, anchor="lm")
    d.text((140, 98), "3h ago", font=font(F_MED, 30), fill=(130, 136, 150, 255), anchor="lm")
    body = ["Looking for a freelance video", "editor for short clips this month.", "Anyone you'd recommend? 🙏"]
    for i, ln in enumerate(body):
        kk = out_cubic(p(t, start + 0.4 + i * 0.3, 0.3))
        d.text((40, 170 + i * 56), ln.replace(" 🙏", ""), font=font(F_SEMI, 40), fill=(*INK, int(255 * kk)), anchor="lm")
    d.line([40, 335, w - 40, 335], fill=(225, 228, 236, 255), width=3)
    d.text((40, 370), "Like", font=font(F_SEMI, 32), fill=(110, 116, 130, 255), anchor="lm")
    kc = p(t, start + 1.8, 0.3)
    pulse = 1 + 0.08 * math.sin(max(0, t - start - 2.1) * 9) * (t > start + 2.1)
    col = LBLUE if kc > 0 else (110, 116, 130)
    d.text((220, 370), "Comment", font=font(F_XB if kc > 0 else F_SEMI, int(32 * pulse)), fill=(*col, 255), anchor="lm")
    card = with_alpha(card, out_cubic(k))
    sub.alpha_composite(card, (int(cx - w / 2), int(cy - h / 2 + 70 * (1 - out_cubic(k)))))


def reply_card(sub, cx, cy, t, start):
    w, h = 860, 300
    k = p(t, start, 0.4)
    if k <= 0: return
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=32, fill=(232, 240, 252, 255))
    d.text((40, 45), "Your comment", font=font(F_XB, 34), fill=(*LBLUE, 255), anchor="lm")
    lines = ["Hi Jordan! I edit short clips for", "coaches. Here's a 20-sec sample.", "Happy to DM you details!"]
    for i, ln in enumerate(lines):
        kk = out_cubic(p(t, start + 0.3 + i * 0.35, 0.3))
        d.text((40, 115 + i * 58), ln, font=font(F_SEMI, 40), fill=(*INK, int(255 * kk)), anchor="lm")
    card = with_alpha(card, out_cubic(k))
    sub.alpha_composite(card, (int(cx - w / 2), int(cy - h / 2 + 60 * (1 - out_cubic(k)))))


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, 0.0, 0.35)
        place_emoji(sub, "🔎", W / 2, 520 - 18 * math.sin(t * 6), 190 * out_back(k), alpha=k)
        pop_words(sub, ["Search this on", "LinkedIn tonight"], t, 0.0, 860, 104, (WHITE, ACC), gap=0.08, highlight={"linkedin", "tonight"})
        search_bar(sub, W / 2, 1180, t, 0.9, typed_dur=1.4)
        pill(sub, W / 2, 1360, "People post when they need help", F_SEMI, 42, WHITE, INK, alpha=out_cubic(p(t, 2.0, 0.4)), scale=out_back(p(t, 2.0, 0.4)), icon="🙋")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Not every gig is on", "a job board"], t, s1 + 0.1, 360, 84, (WHITE, ACC), gap=0.07, highlight={"not", "job", "board"})
        k1 = p(t, s1 + 0.9, 0.4)
        place_emoji(sub, "📋", 330, 680, 170 * out_back(k1), alpha=out_cubic(k1))
        draw_text(sub, "Job boards", F_XB, 46, 330, 820, SOFT, alpha=out_cubic(k1))
        k2 = p(t, s1 + 1.6, 0.4)
        place_emoji(sub, "💬", 750, 680, 170 * out_back(k2), alpha=out_cubic(k2))
        draw_text(sub, "Feed posts", F_XB, 46, 750, 820, ACC, alpha=out_cubic(k2))
        tags = [("Many ask their network first", 2.6, "👥"), ("Search finds them in seconds", 3.4, "⏱️"), ("Early, helpful replies stand out", 4.2, "⚡")]
        for i, (lab, at, ic) in enumerate(tags):
            kk = p(t, s1 + at, 0.35)
            pill(sub, W / 2, 1000 + i * 118, lab, F_SEMI, 42, (225, 240, 255), (10, 70, 150), alpha=out_cubic(kk), scale=out_back(kk), icon=ic)
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Filter for", "fresh posts"], t, s2 + 0.1, 340, 92, (WHITE, ACC), gap=0.07, highlight={"fresh"})
        search_bar(sub, W / 2, 560, t, s2 + 0.4, typed_dur=0.8)
        filters(sub, t, s2 + 1.4, 700)
        post_card(sub, W / 2, 990, t, s2 + 3.0)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Reply fast +", "show proof"], t, s3 + 0.1, 340, 96, (WHITE, GOLD), highlight={"fast", "proof"})
        reply_card(sub, W / 2, 640, t, s3 + 0.5)
        checklist(sub, t, s3 + 2.3, ["Name your skill", "Link 1 sample", "Move to DM"], 880, 100, ACC, size=48, x0=170, every=0.5)
        k2 = p(t, s3 + 4.0, 0.4)
        draw_text(sub, "Example: 5 short edits", F_XB, 48, W / 2, 1210, WHITE, alpha=out_cubic(k2))
        k3 = p(t, s3 + 4.2, 1.3)
        if k3 > 0:
            draw_text(sub, f"${int(round(200 * out_cubic(k3)))}", F_BLACK, 150, W / 2, 1340, GOLD, alpha=out_cubic(p(t, s3 + 4.2, 0.3)))
        draw_text(sub, "Example pricing. Results depend on your work.", F_MED, 36, W / 2, 1470, SOFT, alpha=out_cubic(p(t, s3 + 4.6, 0.5)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel3.mp4")
