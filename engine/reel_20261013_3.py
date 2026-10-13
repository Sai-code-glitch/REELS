"""Your first invoice: 5 minutes, $0 (free Google Docs template)."""
from reel_common import *

ACC = (255, 120, 120)   # coral
GOLD = (255, 214, 92)
GREEN = (70, 210, 130)
RED = (255, 80, 90)
bg = Background(top=(36, 10, 18), bottom=(64, 18, 30), blobs=[(255, 90, 110), (255, 170, 60), (140, 80, 255)], seed=153)

ITEMS = [("Logo design (example)", 120), ("3 social posts (example)", 60)]


def card_base(w, h):
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=32, fill=(250, 250, 252, 255))
    return card, d


def phone_notif(sub, cx, cy, t, start):
    w, h = 860, 220
    k = p(t, start, 0.45)
    if k <= 0: return
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=40, fill=(245, 245, 250, 240))
    d.rounded_rectangle([34, 40, 124, 130], radius=22, fill=(*GREEN, 255))
    card.alpha_composite(emoji_img("💬", 56), (51, 57))
    d.text((150, 60), "Client · now", font=font(F_XB, 36), fill=INK, anchor="lm")
    d.text((150, 115), "Love it! How do I pay you?", font=font(F_SEMI, 40), fill=INK, anchor="lm")
    d.text((150, 165), "Send me an invoice 🙂" if False else "Send me an invoice.", font=font(F_MED, 36), fill=(110, 116, 130, 255), anchor="lm")
    y = cy - h / 2 - 140 * (1 - out_back(k))
    sub.alpha_composite(with_alpha(card, out_cubic(k)), (int(cx - w / 2), int(y)))


def invoice(sub, cx, cy, t, start, fields_every=0.75, show_total_at=None):
    w, h = 860, 860
    k = p(t, start, 0.45)
    if k <= 0: return
    card, d = card_base(w, h)
    d.rounded_rectangle([0, 0, w - 1, 120], radius=32, fill=(40, 44, 60, 255))
    d.rectangle([0, 80, w - 1, 120], fill=(40, 44, 60, 255))
    d.text((40, 60), "INVOICE", font=font(F_BLACK, 52), fill=(255, 255, 255, 255), anchor="lm")
    d.text((w - 40, 60), "#001", font=font(F_XB, 44), fill=(*GOLD, 255), anchor="rm")

    def fa(i):
        return out_cubic(p(t, start + 0.5 + i * fields_every, 0.3))

    a = fa(0)
    if a > 0:
        d.text((40, 165), "From: Sam Rivera", font=font(F_SEMI, 34), fill=(*INK, int(255 * a)), anchor="lm")
        d.text((40, 212), "To: Corner Café", font=font(F_SEMI, 34), fill=(*INK, int(255 * a)), anchor="lm")
    a = fa(1)
    if a > 0:
        d.text((w - 40, 165), "Date: Oct 13", font=font(F_SEMI, 34), fill=(*INK, int(255 * a)), anchor="rm")
        d.text((w - 40, 212), "Due: Oct 20", font=font(F_XB, 34), fill=(*RED, int(255 * a)), anchor="rm")
    d.line([40, 255, w - 40, 255], fill=(225, 228, 236, 255), width=3)
    for i, (lab, amt) in enumerate(ITEMS):
        a = fa(2 + i)
        if a <= 0: continue
        y = 310 + i * 70
        d.text((40, y), lab, font=font(F_SEMI, 38), fill=(*INK, int(255 * a)), anchor="lm")
        d.text((w - 40, y), f"${amt}", font=font(F_XB, 38), fill=(*INK, int(255 * a)), anchor="rm")
    d.line([40, 470, w - 40, 470], fill=(225, 228, 236, 255), width=3)
    tot = sum(a for _, a in ITEMS)
    kt = p(t, show_total_at if show_total_at is not None else start + 0.5 + 4 * fields_every, 1.4)
    if kt > 0:
        d.text((40, 530), "Total", font=font(F_XB, 48), fill=INK, anchor="lm")
        d.text((w - 40, 530), f"${int(round(tot * out_cubic(kt)))}", font=font(F_BLACK, 64), fill=(20, 150, 80, 255), anchor="rm")
    a = fa(5)
    if a > 0:
        d.rounded_rectangle([40, 600, w - 40, 820], radius=22, fill=(240, 242, 248, int(255 * a)))
        d.text((70, 645), "Pay by: bank transfer or PayPal", font=font(F_SEMI, 34), fill=(*INK, int(255 * a)), anchor="lm")
        d.text((70, 705), "Terms: due in 7 days", font=font(F_SEMI, 34), fill=(*INK, int(255 * a)), anchor="lm")
        d.text((70, 765), "Thank you for your business!", font=font(F_MED, 32), fill=(110, 116, 130, int(255 * a)), anchor="lm")
    card = with_alpha(card, out_cubic(k))
    sub.alpha_composite(card, (int(cx - w / 2), int(cy - h / 2 + 60 * (1 - out_cubic(k)))))


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, 0.0, 0.3)
        place_emoji(sub, "🧾", W / 2, 540 + 14 * math.sin(t * 6), 200 * out_back(k), alpha=k, rot=6 * math.sin(t * 4))
        pop_words(sub, ["Your first invoice:", "5 minutes, $0"], t, 0.0, 960, 108, (WHITE, ACC), gap=0.07, highlight={"5", "minutes,", "$0"})
        pill(sub, W / 2, 1300, "Free Google Docs template", F_SEMI, 46, WHITE, INK, alpha=out_cubic(p(t, 1.3, 0.4)), scale=out_back(p(t, 1.3, 0.4)), icon="📄")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Your client says this..."], t, s1 + 0.1, 330, 76, (WHITE, ACC), gap=0.07, highlight={"this..."})
        phone_notif(sub, W / 2, 600, t, s1 + 0.5)
        kq = p(t, s1 + 1.8, 0.4)
        place_emoji(sub, "😬", W / 2, 860, 150 * out_back(kq), alpha=out_cubic(kq))
        pop_words(sub, ["Don't reply", "\"umm... just send it?\""], t, s1 + 2.2, 1060, 68, (WHITE, RED), gap=0.06, highlight={"don't"})
        tags = [("Looks unprofessional", 3.6, "😕"), ("Easy to get paid late", 4.3, "⏳")]
        for i, (lab, at, ic) in enumerate(tags):
            kk = p(t, s1 + at, 0.35)
            pill(sub, W / 2, 1270 + i * 115, lab, F_SEMI, 46, (255, 236, 238), (190, 30, 50), alpha=out_cubic(kk), scale=out_back(kk), icon=ic)
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Send this instead"], t, s2 + 0.1, 320, 90, (WHITE, ACC), gap=0.07, highlight={"instead"})
        invoice(sub, W / 2, 900, t, s2 + 0.4, fields_every=0.85, show_total_at=99)
        labels = [("Who + to whom", 0.9), ("Date + due date", 1.75), ("Each item + price", 2.6), ("How to pay + terms", 4.7)]
        for lab, at in labels:
            kk = p(t, s2 + at, 0.3)
            if kk > 0 and t < s2 + at + 1.6:
                a = out_cubic(kk) * (1 - p(t, s2 + at + 1.3, 0.3))
                pill(sub, W / 2, 1420, lab, F_XB, 48, GOLD, INK, alpha=a, scale=out_back(kk), icon="👉")
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Example invoice"], t, s3 + 0.1, 300, 84, (WHITE, GOLD), gap=0.07, highlight={"example"})
        invoice(sub, W / 2, 820, t, s3 + 0.3, fields_every=0.0, show_total_at=s3 + 1.0)
        kb = p(t, s3 + 2.6, 0.4)
        pill(sub, W / 2, 1330, "Save it. Copy it for every client.", F_SEMI, 44, WHITE, INK, alpha=out_cubic(kb), scale=out_back(kb), icon="📁")
        draw_text(sub, "Example pricing. Results depend on your work.", F_MED, 36, W / 2, 1450, SOFT, alpha=out_cubic(p(t, s3 + 3.2, 0.5)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel3.mp4")
