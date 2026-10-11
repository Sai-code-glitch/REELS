"""Ask for 50% upfront: ghosting chat mock + deposit invoice."""
from reel_common import *

ACC = (255, 120, 110)   # coral
GOLD = (255, 214, 92)
GREEN = (60, 200, 120)
bg = Background(top=(34, 8, 18), bottom=(60, 14, 32), blobs=[(255, 90, 90), (255, 160, 60), (200, 50, 140)], seed=47)


def chat(sub, cx, cy, t, start):
    w, h = 800, 600
    k = p(t, start, 0.45)
    if k <= 0: return
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=40, fill=(245, 246, 250, 255))
    d.rounded_rectangle([0, 0, w - 1, 100], radius=40, fill=(230, 232, 240, 255))
    d.rectangle([0, 60, w - 1, 100], fill=(230, 232, 240, 255))
    d.ellipse([30, 22, 86, 78], fill=(180, 186, 200, 255))
    d.text((106, 50), "New client", font=font(F_XB, 38), fill=INK, anchor="lm")
    msgs = [(True, "Final logo is done! 🎉", 0.6), (True, "Here's the invoice: $120", 1.3), (False, "Seen  ·  3 days ago", 2.2)]
    y = 150
    for mine, txt, at in msgs:
        kk = out_cubic(p(t, start + at, 0.35))
        if kk <= 0: continue
        if mine:
            f = font(F_SEMI, 38)
            tw = d.textlength(txt.replace(" 🎉", ""), font=f) + (50 if "🎉" in txt else 0)
            x1 = w - 40; x0 = x1 - tw - 60
            d.rounded_rectangle([x0, y, x1, y + 84], radius=36, fill=(40, 120, 255, int(255 * kk)))
            d.text((x0 + 30, y + 42), txt.replace(" 🎉", ""), font=f, fill=(255, 255, 255, int(255 * kk)), anchor="lm")
            if "🎉" in txt:
                e = emoji_img("🎉", 40)
                card.alpha_composite(with_alpha(e.copy(), kk), (int(x1 - 30 - e.width), int(y + 42 - e.height / 2)))
            y += 110
        else:
            d.text((w - 50, y + 10), txt, font=font(F_MED, 32), fill=(140, 144, 160, int(255 * kk)), anchor="rm")
            y += 70
    kd = p(t, start + 3.0, 0.4)
    if kd > 0:
        d.text((w / 2, 520), "...no reply", font=font(F_XB, 44), fill=(200, 40, 60, int(255 * kd)), anchor="mm")
    card = with_alpha(card, out_cubic(k))
    sub.alpha_composite(card, (int(cx - w / 2), int(cy - h / 2 + 80 * (1 - out_cubic(k)))))


def invoice(sub, cx, cy, t, start):
    w, h = 820, 700
    k = p(t, start, 0.45)
    if k <= 0: return
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=36, fill=(252, 252, 254, 255))
    d.text((50, 70), "INVOICE #001", font=font(F_BLACK, 50), fill=INK, anchor="lm")
    d.text((w - 50, 70), "Example", font=font(F_SEMI, 32), fill=(140, 144, 160, 255), anchor="rm")
    d.line([50, 120, w - 50, 120], fill=(220, 222, 230, 255), width=3)
    rows = [("Logo + 2 revisions", "$120", 0.5, INK), ("Deposit (50%) due now", "$60", 1.2, (200, 60, 50)), ("Balance on delivery", "$60", 1.9, INK)]
    for i, (lab, val, at, col) in enumerate(rows):
        kk = out_cubic(p(t, start + at, 0.4))
        if kk <= 0: continue
        y = 190 + i * 110
        d.text((50 + 40 * (1 - kk), y), lab, font=font(F_SEMI, 42), fill=(*col[:3], int(255 * kk)), anchor="lm")
        d.text((w - 50, y), val, font=font(F_BLACK, 52), fill=(*col[:3], int(255 * kk)), anchor="rm")
    kn = out_cubic(p(t, start + 2.5, 0.4))
    if kn > 0:
        d.text((w / 2, 640), "Work starts after the deposit", font=font(F_XB, 38), fill=(40, 120, 255, int(255 * kn)), anchor="mm")
    # PAID stamp
    ks = p(t, start + 3.2, 0.35)
    if ks > 0:
        st = Image.new("RGBA", (300, 120), (0, 0, 0, 0))
        sd = ImageDraw.Draw(st)
        sd.rounded_rectangle([4, 4, 296, 116], radius=20, outline=(*GREEN, 255), width=10)
        sd.text((150, 60), "PAID", font=font(F_BLACK, 72), fill=(*GREEN, 255), anchor="mm")
        s = 1.6 - 0.6 * out_cubic(ks)
        st = st.rotate(-12, expand=True, resample=Image.BICUBIC)
        st = st.resize((int(st.width * s), int(st.height * s)))
        st = with_alpha(st, out_cubic(ks))
        card.alpha_composite(st, (int(w / 2 - st.width / 2), int(515 - st.height / 2)))
    card = with_alpha(card, out_cubic(k))
    sub.alpha_composite(card, (int(cx - w / 2), int(cy - h / 2 + 80 * (1 - out_cubic(k)))))


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, 0.0, 0.35)
        place_emoji(sub, "🧾", W / 2, 560 - 20 * math.sin(t * 6) * (1 - p(t, 1.5, 1)), 200 * out_back(k), alpha=k, rot=6 * math.sin(t * 4))
        pop_words(sub, ["Never start a", "client job", "without this"], t, 0.0, 1000, 120, (WHITE, ACC), gap=0.08, highlight={"never", "this"})
        pill(sub, W / 2, 1400, "Beginners often skip it", F_SEMI, 46, WHITE, INK, alpha=out_cubic(p(t, 1.5, 0.4)), scale=out_back(p(t, 1.5, 0.4)), icon="⚠️")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["You finish the work.", "Then this happens"], t, s1 + 0.1, 350, 76, (WHITE, ACC), gap=0.07, highlight={"this", "happens"})
        chat(sub, W / 2, 830, t, s1 + 0.8)
        kk = p(t, s1 + 4.6, 0.4)
        pill(sub, W / 2, 1240, "Work done. No payment.", F_XB, 50, (255, 236, 238), (190, 30, 50), alpha=out_cubic(kk), scale=out_back(kk), icon="👻")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Ask for 50%", "upfront"], t, s2 + 0.1, 340, 100, (WHITE, GOLD), gap=0.08, highlight={"50%", "upfront"})
        invoice(sub, W / 2, 840, t, s2 + 0.7)
        kk = p(t, s2 + 5.0, 0.4)
        pill(sub, W / 2, 1270, "Free templates: Google Docs, Canva", F_SEMI, 42, WHITE, INK, alpha=out_cubic(kk), scale=out_back(kk), icon="🆓")
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Before you start"], t, s3 + 0.1, 340, 96, (WHITE, GOLD), highlight={"start"})
        money_counter(sub, t, s3 + 0.5, 60, 610, GOLD, label="of a $120 job secured")
        checklist(sub, t, s3 + 2.6, ["50% deposit paid", "Scope in writing", "Revisions + deadline set"], 960, 112, ACC, size=52, x0=170, every=0.7)
        draw_text(sub, "Example pricing. Results depend on your work.", F_MED, 36, W / 2, 1360, SOFT, alpha=out_cubic(p(t, s3 + 3.0, 0.5)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel3.mp4")
