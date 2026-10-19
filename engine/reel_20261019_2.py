"""Search this in Facebook groups tonight: owners asking 'looking for someone'."""
from reel_common import *

ACC = (120, 160, 255)   # facebook-ish blue
GOLD = (255, 214, 92)
GREEN = (70, 210, 130)
RED = (255, 96, 110)
FB = (24, 119, 242)
bg = Background(top=(10, 10, 40), bottom=(30, 24, 80), blobs=[(60, 90, 255), (140, 80, 255), (40, 160, 255)], seed=192)
QUERY = '"looking for someone"'


def search_bar(sub, cx, cy, t, start, w=860, typed_dur=1.0):
    k = out_back(p(t, start, 0.4))
    if k <= 0: return
    h = 120
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=60, fill=(240, 242, 245, 255))
    d.ellipse([40, 38, 80, 78], outline=(101, 103, 107, 255), width=6)
    d.line([74, 72, 92, 90], fill=(101, 103, 107, 255), width=7)
    n = int(len(QUERY) * p(t, start + 0.2, typed_dur))
    txt = QUERY[:n]
    f = font(F_SEMI, 46)
    d.text((115, 60), txt, font=f, fill=INK, anchor="lm")
    if (t * 2) % 1 < 0.5:
        x = 115 + d.textlength(txt, font=f) + 4
        d.line([x, 34, x, 86], fill=(*FB, 255), width=4)
    card = card.resize((max(1, int(w * k)), max(1, int(h * k))))
    sub.alpha_composite(card, (int(cx - card.width / 2), int(cy - card.height / 2)))


def group_header(sub, cx, cy, t, start):
    k = p(t, start, 0.4)
    if k <= 0: return
    w, h = 860, 130
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=28, fill=(*FB, 255))
    d.text((40, 48), "Small Business Owners", font=font(F_XB, 42), fill=(255, 255, 255, 255), anchor="lm")
    d.text((40, 94), "Your town · Group", font=font(F_MED, 32), fill=(220, 232, 255, 255), anchor="lm")
    card = with_alpha(card, out_cubic(k))
    sub.alpha_composite(card, (int(cx - w / 2), int(cy - h / 2 + 50 * (1 - out_cubic(k)))))


def post_card(sub, cx, cy, t, start):
    w, h = 860, 400
    k = p(t, start, 0.45)
    if k <= 0: return
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=32, fill=(255, 255, 255, 255))
    d.ellipse([36, 30, 116, 110], fill=(240, 120, 160, 255))
    d.text((76, 70), "M", font=font(F_XB, 40), fill=(255, 255, 255, 255), anchor="mm")
    d.text((140, 55), "Maria · Corner Café", font=font(F_XB, 38), fill=INK, anchor="lm")
    d.text((140, 98), "1h ago", font=font(F_MED, 30), fill=(130, 136, 150, 255), anchor="lm")
    body = ["Looking for someone to make a", "simple holiday menu flyer for", "our café. Any recommendations?"]
    for i, ln in enumerate(body):
        kk = out_cubic(p(t, start + 0.4 + i * 0.3, 0.3))
        d.text((40, 170 + i * 54), ln, font=font(F_SEMI, 40), fill=(*INK, int(255 * kk)), anchor="lm")
    d.line([40, 335, w - 40, 335], fill=(225, 228, 236, 255), width=3)
    d.text((40, 370), "Like", font=font(F_SEMI, 32), fill=(110, 116, 130, 255), anchor="lm")
    kc = p(t, start + 1.8, 0.3)
    pulse = 1 + 0.08 * math.sin(max(0, t - start - 2.1) * 9) * (t > start + 2.1)
    col = FB if kc > 0 else (110, 116, 130)
    d.text((200, 370), "Comment", font=font(F_XB if kc > 0 else F_SEMI, int(32 * pulse)), fill=(*col, 255), anchor="lm")
    card = with_alpha(card, out_cubic(k))
    sub.alpha_composite(card, (int(cx - w / 2), int(cy - h / 2 + 70 * (1 - out_cubic(k)))))


def reply_card(sub, cx, cy, t, start):
    w, h = 860, 300
    k = p(t, start, 0.4)
    if k <= 0: return
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=32, fill=(231, 240, 255, 255))
    d.text((40, 45), "Your comment", font=font(F_XB, 34), fill=(*FB, 255), anchor="lm")
    lines = ["Hi Maria! I design flyers for", "local shops. Here's one I made.", "Happy to send a quote by DM!"]
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
        place_emoji(sub, "👀", W / 2, 470 - 18 * math.sin(t * 6), 180 * out_back(k), alpha=k)
        pop_words(sub, ["Search this in", "Facebook groups", "tonight"], t, 0.0, 860, 104, (WHITE, ACC), gap=0.08, highlight={"facebook", "groups", "tonight"})
        search_bar(sub, W / 2, 1230, t, 0.9, typed_dur=1.2)
        pill(sub, W / 2, 1400, "Owners ask their groups first", F_SEMI, 42, WHITE, INK, alpha=out_cubic(p(t, 2.0, 0.4)), scale=out_back(p(t, 2.0, 0.4)), icon="🏪")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Busy owners don't post", "on job boards"], t, s1 + 0.1, 360, 80, (WHITE, ACC), gap=0.07, highlight={"don't", "job", "boards"})
        k1 = p(t, s1 + 0.9, 0.4)
        place_emoji(sub, "☕", 330, 680, 170 * out_back(k1), alpha=out_cubic(k1))
        draw_text(sub, "Café owner", F_XB, 46, 330, 820, SOFT, alpha=out_cubic(k1))
        k2 = p(t, s1 + 1.6, 0.4)
        place_emoji(sub, "💬", 750, 680, 170 * out_back(k2), alpha=out_cubic(k2))
        draw_text(sub, "Asks the group", F_XB, 46, 750, 820, ACC, alpha=out_cubic(k2))
        tags = [("Local business groups", 2.6, "🏙️"), ("Town community groups", 3.4, "🏡"), ("Niche seller groups", 4.2, "🛍️")]
        for i, (lab, at, ic) in enumerate(tags):
            kk = p(t, s1 + at, 0.35)
            pill(sub, W / 2, 1000 + i * 118, lab, F_SEMI, 44, (230, 236, 255), (30, 50, 140), alpha=out_cubic(kk), scale=out_back(kk), icon=ic)
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Search inside", "each group"], t, s2 + 0.1, 330, 92, (WHITE, ACC), gap=0.07, highlight={"inside"})
        group_header(sub, W / 2, 540, t, s2 + 0.4)
        search_bar(sub, W / 2, 690, t, s2 + 1.0, typed_dur=0.9)
        post_card(sub, W / 2, 1000, t, s2 + 2.6)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Comment.", "Don't spam."], t, s3 + 0.1, 320, 100, (WHITE, GOLD), highlight={"comment.", "spam."})
        reply_card(sub, W / 2, 610, t, s3 + 0.5)
        checklist(sub, t, s3 + 2.1, ["Follow the group rules", "Show 1 real sample", "DM only when invited"], 850, 96, ACC, size=48, x0=160, every=0.45)
        k2 = p(t, s3 + 3.8, 0.4)
        draw_text(sub, "Example: 1 menu flyer", F_XB, 50, W / 2, 1170, WHITE, alpha=out_cubic(k2))
        k3 = p(t, s3 + 4.0, 1.3)
        if k3 > 0:
            draw_text(sub, f"${int(round(60 * out_cubic(k3)))}", F_BLACK, 150, W / 2, 1300, GOLD, alpha=out_cubic(p(t, s3 + 4.0, 0.3)))
        draw_text(sub, "Example pricing. Results depend on your work.", F_MED, 36, W / 2, 1430, SOFT, alpha=out_cubic(p(t, s3 + 4.4, 0.5)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel2.mp4")
