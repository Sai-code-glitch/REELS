"""Search this on Reddit tonight: find fresh [Hiring] posts on r/forhire."""
from reel_common import *

ACC = (255, 120, 60)    # reddit orange
GOLD = (255, 214, 92)
GREEN = (70, 210, 130)
RED = (255, 96, 110)
bg = Background(top=(30, 10, 6), bottom=(62, 22, 12), blobs=[(255, 90, 40), (255, 160, 60), (200, 50, 80)], seed=191)
QUERY = "r/forhire  [Hiring]"


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
    f = font(F_SEMI, 46)
    d.text((115, 60), txt, font=f, fill=INK, anchor="lm")
    if (t * 2) % 1 < 0.5:
        x = 115 + d.textlength(txt, font=f) + 4
        d.line([x, 34, x, 86], fill=(*ACC, 255), width=4)
    card = card.resize((max(1, int(w * k)), max(1, int(h * k))))
    sub.alpha_composite(card, (int(cx - card.width / 2), int(cy - card.height / 2)))


def chips(sub, t, start, cy, items):
    d = ImageDraw.Draw(sub)
    f = font(F_XB, 40)
    widths = [d.textlength(c, font=f) + 70 for c, _ in items]
    x = W / 2 - (sum(widths) + 24 * (len(items) - 1)) / 2
    for (c, at), wd in zip(items, widths):
        kk = p(t, start + at, 0.35)
        if kk > 0:
            on = t > start + at + 0.35
            pill(sub, x + wd / 2, cy, c, F_XB, 40, ACC if on else (240, 232, 228), WHITE if on else INK, alpha=out_cubic(kk), scale=out_back(kk), pad=(35, 18))
        x += wd + 24


def post_card(sub, cx, cy, t, start):
    w, h = 860, 430
    k = p(t, start, 0.45)
    if k <= 0: return
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=32, fill=(250, 250, 252, 255))
    d.ellipse([36, 30, 106, 100], fill=(*ACC, 255))
    d.text((71, 65), "r/", font=font(F_XB, 34), fill=(255, 255, 255, 255), anchor="mm")
    d.text((126, 50), "r/forhire", font=font(F_XB, 36), fill=INK, anchor="lm")
    d.text((126, 88), "u/smallpodcast · 2h", font=font(F_MED, 30), fill=(130, 136, 150, 255), anchor="lm")
    d.rounded_rectangle([40, 130, 230, 180], radius=25, fill=(20, 150, 80, 255))
    d.text((135, 155), "Hiring", font=font(F_XB, 30), fill=(255, 255, 255, 255), anchor="mm")
    body = ["Need someone to cut 4 short", "clips from our weekly podcast.", "Remote. Send samples please."]
    for i, ln in enumerate(body):
        kk = out_cubic(p(t, start + 0.4 + i * 0.3, 0.3))
        d.text((40, 225 + i * 54), ln, font=font(F_SEMI, 40), fill=(*INK, int(255 * kk)), anchor="lm")
    d.line([40, 375, w - 40, 375], fill=(225, 228, 236, 255), width=3)
    kc = p(t, start + 1.8, 0.3)
    pulse = 1 + 0.08 * math.sin(max(0, t - start - 2.1) * 9) * (t > start + 2.1)
    col = ACC if kc > 0 else (110, 116, 130)
    d.text((40, 405), "Reply", font=font(F_XB if kc > 0 else F_SEMI, int(32 * pulse)), fill=(*col, 255), anchor="lm")
    card = with_alpha(card, out_cubic(k))
    sub.alpha_composite(card, (int(cx - w / 2), int(cy - h / 2 + 70 * (1 - out_cubic(k)))))


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, 0.0, 0.35)
        place_emoji(sub, "🔎", W / 2, 500 - 18 * math.sin(t * 6), 190 * out_back(k), alpha=k)
        pop_words(sub, ["Search this on", "Reddit tonight"], t, 0.0, 850, 112, (WHITE, ACC), gap=0.08, highlight={"reddit", "tonight"})
        search_bar(sub, W / 2, 1180, t, 0.9, typed_dur=1.2)
        pill(sub, W / 2, 1360, "People post paid gigs here daily", F_SEMI, 42, WHITE, INK, alpha=out_cubic(p(t, 2.0, 0.4)), scale=out_back(p(t, 2.0, 0.4)), icon="🙋")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Most beginners only", "check gig sites"], t, s1 + 0.1, 360, 84, (WHITE, ACC), gap=0.07, highlight={"only", "gig", "sites"})
        k1 = p(t, s1 + 0.9, 0.4)
        place_emoji(sub, "🛒", 330, 680, 170 * out_back(k1), alpha=out_cubic(k1))
        draw_text(sub, "Gig sites", F_XB, 46, 330, 820, SOFT, alpha=out_cubic(k1))
        k2 = p(t, s1 + 1.6, 0.4)
        place_emoji(sub, "📣", 750, 680, 170 * out_back(k2), alpha=out_cubic(k2))
        draw_text(sub, "Hiring posts", F_XB, 46, 750, 820, ACC, alpha=out_cubic(k2))
        tags = [("Real people asking for help", 2.6, "👥"), ("Many list the task + budget", 3.4, "📝"), ("Fresh posts get fewer replies", 4.2, "⚡")]
        for i, (lab, at, ic) in enumerate(tags):
            kk = p(t, s1 + at, 0.35)
            pill(sub, W / 2, 1000 + i * 118, lab, F_SEMI, 42, (255, 236, 226), (140, 50, 10), alpha=out_cubic(kk), scale=out_back(kk), icon=ic)
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Sort by New.", "Filter: Hiring."], t, s2 + 0.1, 340, 92, (WHITE, ACC), gap=0.07, highlight={"new.", "hiring."})
        search_bar(sub, W / 2, 560, t, s2 + 0.4, typed_dur=0.8)
        chips(sub, t, s2 + 1.4, 700, [("New", 0.0), ("Hiring", 0.5), ("Today", 1.0)])
        post_card(sub, W / 2, 1010, t, s2 + 3.0)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Reply the", "smart way"], t, s3 + 0.1, 330, 100, (WHITE, GOLD), highlight={"smart"})
        checklist(sub, t, s3 + 0.8, ["Read the sub's rules", "Reply with 1 sample", "Keep it to 3 lines"], 560, 110, ACC, size=52, x0=160, every=0.5)
        kn = p(t, s3 + 2.4, 0.4)
        pill(sub, W / 2, 920, "Never pay to apply", F_XB, 48, RED, WHITE, alpha=out_cubic(kn), scale=out_back(kn), icon="🚫")
        k2 = p(t, s3 + 3.4, 0.4)
        draw_text(sub, "Example: 4 clips × $30", F_XB, 52, W / 2, 1090, WHITE, alpha=out_cubic(k2))
        k3 = p(t, s3 + 3.7, 1.3)
        if k3 > 0:
            draw_text(sub, f"${int(round(120 * out_cubic(k3)))}", F_BLACK, 170, W / 2, 1240, GOLD, alpha=out_cubic(p(t, s3 + 3.7, 0.3)))
        draw_text(sub, "Example pricing. Results depend on your work.", F_MED, 36, W / 2, 1380, SOFT, alpha=out_cubic(p(t, s3 + 4.2, 0.5)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel1.mp4")
