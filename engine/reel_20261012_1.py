"""First client is already in your contacts: warm-network referral text."""
from reel_common import *

ACC = (178, 140, 255)   # violet
GOLD = (255, 214, 92)
GREEN = (70, 210, 130)
RED = (255, 96, 110)
bg = Background(top=(16, 8, 40), bottom=(34, 14, 70), blobs=[(140, 90, 255), (60, 120, 255), (220, 90, 220)], seed=61)


def proposal_card(sub, cx, cy, t, start):
    w, h = 820, 300
    k = out_back(p(t, start, 0.5))
    if k <= 0: return
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=32, fill=(250, 250, 253, 255))
    d.text((40, 55), "Need a logo for my bakery", font=font(F_XB, 44), fill=INK, anchor="lm")
    d.text((40, 115), "Posted 2 hours ago · Fixed price", font=font(F_MED, 32), fill=(130, 136, 150, 255), anchor="lm")
    d.line([40, 160, w - 40, 160], fill=(225, 228, 236, 255), width=3)
    kp = p(t, start + 0.8, 1.2)
    n = int(round(50 * out_cubic(kp)))
    d.text((40, 230), "Proposals:", font=font(F_SEMI, 44), fill=(90, 96, 112, 255), anchor="lm")
    d.text((w - 40, 230), f"{n}+", font=font(F_BLACK, 84), fill=(*RED, 255), anchor="rm")
    card = card.resize((int(w * k), int(h * k)))
    sub.alpha_composite(card, (int(cx - card.width / 2), int(cy - card.height / 2)))


def phone_chat(sub, cx, cy, t, start):
    w, h = 820, 560
    k = p(t, start, 0.45)
    if k <= 0: return
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=44, fill=(245, 246, 250, 255))
    d.rounded_rectangle([0, 0, w - 1, 110], radius=44, fill=(232, 234, 242, 255))
    d.rectangle([0, 70, w - 1, 110], fill=(232, 234, 242, 255))
    d.ellipse([34, 26, 92, 84], fill=(*ACC, 255))
    d.text((63, 55), "M", font=font(F_XB, 34), fill=(255, 255, 255, 255), anchor="mm")
    d.text((112, 55), "Maya (old coworker)", font=font(F_XB, 38), fill=INK, anchor="lm")
    msgs = [("Hey! I just started designing", "logos + flyers on the side.", 0.5),
            ("Know anyone who needs one?", "Happy to do a starter price.", 1.6)]
    y = 140
    f = font(F_SEMI, 38)
    for a, b, at in msgs:
        kk = out_cubic(p(t, start + at, 0.35))
        if kk <= 0: continue
        tw = max(d.textlength(a, font=f), d.textlength(b, font=f))
        x1 = w - 36; x0 = x1 - tw - 60
        d.rounded_rectangle([x0, y, x1, y + 130], radius=36, fill=(110, 80, 240, int(255 * kk)))
        d.text((x0 + 30, y + 40), a, font=f, fill=(255, 255, 255, int(255 * kk)), anchor="lm")
        d.text((x0 + 30, y + 90), b, font=f, fill=(255, 255, 255, int(255 * kk)), anchor="lm")
        y += 160
    kr = out_cubic(p(t, start + 3.0, 0.35))
    if kr > 0:
        txt = "My sister needs a menu! 👀"
        tw = d.textlength("My sister needs a menu!", font=f) + 56
        d.rounded_rectangle([36, y, 36 + tw + 60, y + 84], radius=36, fill=(222, 224, 232, int(255 * kr)))
        d.text((66, y + 42), "My sister needs a menu!", font=f, fill=(*INK, int(255 * kr)), anchor="lm")
        e = emoji_img("👀", 40)
        card.alpha_composite(with_alpha(e.copy(), kr), (int(66 + tw - 40), int(y + 42 - e.height / 2)))
    card = with_alpha(card, out_cubic(k))
    sub.alpha_composite(card, (int(cx - w / 2), int(cy - h / 2 + 80 * (1 - out_cubic(k)))))


def people_grid(sub, t, start, cy):
    for i in range(10):
        kk = p(t, start + i * 0.08, 0.35)
        if kk <= 0: continue
        col, row = i % 5, i // 5
        x = 230 + col * 155
        y = cy + row * 170
        yes = i == 6 and t > start + 1.6
        place_emoji(sub, "🤩" if yes else "🙂", x, y, 110 * out_back(kk) * (1.25 if yes else 1), alpha=out_cubic(kk))
        ks = p(t, start + 1.0 + i * 0.05, 0.3)
        if ks > 0 and not yes:
            place_emoji(sub, "💬", x + 50, y - 50, 50 * out_back(ks), alpha=0.85 * out_cubic(ks))
    ky = p(t, start + 1.6, 0.4)
    if ky > 0:
        pill(sub, W / 2, cy + 340, "You only need ONE yes", F_XB, 52, GREEN, INK, alpha=out_cubic(ky), scale=out_back(ky), icon="✅")


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, 0.0, 0.35)
        place_emoji(sub, "📱", W / 2, 540 - 18 * math.sin(t * 6), 200 * out_back(k), alpha=k)
        pop_words(sub, ["Your first client", "is already in", "your contacts"], t, 0.0, 980, 116, (WHITE, ACC), gap=0.07, highlight={"client", "contacts"})
        pill(sub, W / 2, 1380, "Send this 2-line text", F_SEMI, 46, WHITE, INK, alpha=out_cubic(p(t, 1.4, 0.4)), scale=out_back(p(t, 1.4, 0.4)), icon="💬")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Job sites = you vs", "a crowd of strangers"], t, s1 + 0.1, 360, 78, (WHITE, RED), gap=0.07, highlight={"crowd", "strangers"})
        proposal_card(sub, W / 2, 700, t, s1 + 0.7)
        tags = [("No reviews yet", 2.6, "⭐"), ("Racing to the lowest price", 3.4, "📉"), ("Days with zero replies", 4.2, "⏳")]
        for i, (lab, at, ic) in enumerate(tags):
            kk = p(t, s1 + at, 0.35)
            pill(sub, W / 2, 1010 + i * 118, lab, F_SEMI, 44, (255, 236, 238), (190, 30, 50), alpha=out_cubic(kk), scale=out_back(kk), icon=ic)
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Text people who", "already trust you"], t, s2 + 0.1, 340, 84, (WHITE, ACC), gap=0.07, highlight={"trust"})
        phone_chat(sub, W / 2, 790, t, s2 + 0.5)
        checklist(sub, t, s2 + 4.6, ["Name ONE service", "Ask who they know"], 1250, 105, ACC, size=50, x0=170, every=0.8)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Text 10 people", "today"], t, s3 + 0.1, 360, 100, (WHITE, GOLD), highlight={"10"})
        people_grid(sub, t, s3 + 0.6, 620)
        k2 = p(t, s3 + 3.0, 0.4)
        draw_text(sub, "Example: menu design", F_XB, 52, W / 2, 1100, WHITE, alpha=out_cubic(k2))
        k3 = p(t, s3 + 3.3, 1.4)
        if k3 > 0:
            draw_text(sub, f"${int(round(80 * out_cubic(k3)))}", F_BLACK, 170, W / 2, 1250, GOLD, alpha=out_cubic(p(t, s3 + 3.3, 0.3)))
        draw_text(sub, "Example pricing. Results depend on your work.", F_MED, 36, W / 2, 1420, SOFT, alpha=out_cubic(p(t, s3 + 4.0, 0.5)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel1.mp4")
