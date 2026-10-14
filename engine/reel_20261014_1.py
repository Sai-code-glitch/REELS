"""Never lower your price. Cut scope instead (client asks for a discount, part 1)."""
from reel_common import *

ACC = (60, 220, 190)    # teal
GOLD = (255, 214, 92)
RED = (255, 90, 100)
GREEN = (40, 170, 100)
bg = Background(top=(6, 30, 34), bottom=(10, 52, 56), blobs=[(40, 200, 170), (60, 120, 255), (255, 200, 80)], seed=2871)

FULL = [("Logo design", True), ("3 social posts", True), ("Business card", True), ("3 revisions", True)]


def chat_bubble(sub, t, start, x, y, lines, me=False, w=780):
    k = p(t, start, 0.4)
    if k <= 0: return
    h = 60 + 62 * len(lines)
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    fill = (*ACC, 255) if me else (245, 246, 250, 255)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=40, fill=fill)
    for i, ln in enumerate(lines):
        d.text((40, 60 + i * 62), ln, font=font(F_SEMI, 44), fill=INK, anchor="lm")
    s = out_back(k)
    card = card.resize((max(1, int(w * s)), max(1, int(h * s))), Image.LANCZOS)
    card = with_alpha(card, out_cubic(k))
    px = x if not me else x - card.width
    sub.alpha_composite(card, (int(px), int(y)))


def package_card(sub, cx, cy, t, start, title, price, items, strike_from=None, every=0.6, color=ACC, price_t=None):
    w, h = 820, 660
    k = p(t, start, 0.45)
    if k <= 0: return
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=36, fill=(250, 250, 252, 255))
    d.rounded_rectangle([0, 0, w - 1, 130], radius=36, fill=(*color, 255))
    d.rectangle([0, 90, w - 1, 130], fill=(*color, 255))
    d.text((44, 66), title, font=font(F_BLACK, 54), fill=INK, anchor="lm")
    d.text((w - 44, 66), price, font=font(F_BLACK, 60), fill=INK, anchor="rm")
    for i, (lab, on) in enumerate(items):
        y = 210 + i * 110
        d.text((60, y), "✓" if on else "✕", font=font(DEJAVU, 52), fill=(GREEN if on else RED) + (255,), anchor="lm")
        d.text((140, y), lab, font=font(F_SEMI, 50), fill=INK if on else (150, 155, 168, 255), anchor="lm")
        if strike_from is not None and not on:
            ks = p(t, strike_from + i * every, 0.35)
            if ks > 0:
                tw = d.textlength(lab, font=font(F_SEMI, 50))
                d.line([130, y, 140 + tw * out_cubic(ks) + 10, y], fill=(*RED, 255), width=7)
    sub.alpha_composite(with_alpha(card, out_cubic(k)), (int(cx - w / 2), int(cy - h / 2 + 70 * (1 - out_cubic(k)))))


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, 0.0, 0.3)
        place_emoji(sub, "🛑", W / 2, 520 + 12 * math.sin(t * 6), 200 * out_back(k), alpha=k, rot=5 * math.sin(t * 4))
        pop_words(sub, ["Never lower", "your price.", "Do this instead"], t, 0.0, 920, 118, (WHITE, ACC), gap=0.07, highlight={"never", "instead"})
        pill(sub, W / 2, 1310, "When a client asks for a discount", F_SEMI, 44, WHITE, INK, alpha=out_cubic(p(t, 1.2, 0.4)), scale=out_back(p(t, 1.2, 0.4)), icon="💬")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["The client message:"], t, s1 + 0.1, 330, 78, (WHITE, ACC), gap=0.07, highlight={"message:"})
        chat_bubble(sub, t, s1 + 0.5, W / 2 - 390, 470, ["Love it! But can you do", "it for $100 instead of $150?"])
        kq = p(t, s1 + 1.8, 0.4)
        place_emoji(sub, "😰", W / 2, 850, 150 * out_back(kq), alpha=out_cubic(kq))
        pop_words(sub, ["Most beginners say", "\"ok sure\""], t, s1 + 2.3, 1050, 72, (WHITE, RED), gap=0.07, highlight={"\"ok", "sure\""})
        kb = p(t, s1 + 3.8, 0.4)
        pill(sub, W / 2, 1290, "Same work. 33% less pay.", F_XB, 50, (255, 236, 238), (190, 30, 50), alpha=out_cubic(kb), scale=out_back(kb), icon="📉")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Cut the scope,", "not the price"], t, s2 + 0.1, 330, 90, (WHITE, ACC), gap=0.07, highlight={"scope,"})
        items = list(FULL)
        cut_t = s2 + 2.6
        if t >= cut_t:
            items = [FULL[0], (FULL[1][0], False), (FULL[2][0], False), ("1 revision", True)]
        title, price = ("Full package", "$150") if t < cut_t + 2.2 else ("Lite package", "$100")
        package_card(sub, W / 2, 930, t, s2 + 0.5, title, price, items, strike_from=cut_t, every=0.5,
                     color=ACC if t < cut_t + 2.2 else GOLD)
        kk = p(t, cut_t + 2.4, 0.4)
        pill(sub, W / 2, 1430, "Smaller budget = smaller package", F_XB, 46, GOLD, INK, alpha=out_cubic(kk), scale=out_back(kk), icon="✂️")
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Example math"], t, s3 + 0.1, 300, 86, (WHITE, GOLD), gap=0.07, highlight={"math"})
        rows = [("Discount:", "$100 for 6 hrs", "≈ $17/hr", RED, "😩"), ("Lite package:", "$100 for 4 hrs", "= $25/hr", ACC, "😎")]
        for i, (a, b, c, col, ic) in enumerate(rows):
            kk = p(t, s3 + 0.6 + i * 1.3, 0.45)
            if kk <= 0: continue
            y = 560 + i * 330
            card = Image.new("RGBA", (880, 260), (0, 0, 0, 0))
            d = ImageDraw.Draw(card)
            d.rounded_rectangle([0, 0, 879, 259], radius=34, fill=(255, 255, 255, 235))
            d.rounded_rectangle([0, 0, 18, 259], radius=9, fill=(*col, 255))
            d.text((60, 70), a, font=font(F_XB, 48), fill=INK, anchor="lm")
            d.text((60, 160), b, font=font(F_SEMI, 46), fill=(90, 96, 110, 255), anchor="lm")
            d.text((830, 160), c, font=font(F_BLACK, 62), fill=(*col, 255) if col != ACC else (20, 150, 120, 255), anchor="rm")
            card.alpha_composite(emoji_img(ic, 80), (760, 30))
            sub.alpha_composite(with_alpha(card, out_cubic(kk)), (int(W / 2 - 440 + 80 * (1 - out_cubic(kk))), y))
        kb = p(t, s3 + 3.4, 0.4)
        pill(sub, W / 2, 1300, "Your rate stays the same", F_XB, 50, GOLD, INK, alpha=out_cubic(kb), scale=out_back(kb), icon="💪")
        draw_text(sub, "Example pricing. Results depend on your work.", F_MED, 36, W / 2, 1430, SOFT, alpha=out_cubic(p(t, s3 + 3.8, 0.5)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel1.mp4")
