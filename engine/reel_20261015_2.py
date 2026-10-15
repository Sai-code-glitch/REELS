"""3 Canva templates small shops need before Black Friday (Canva templates to sell before the holidays, part 2)."""
from reel_common import *

ACC = (255, 110, 180)   # pink
GOLD = (255, 214, 92)
GREEN = (60, 205, 130)
RED = (255, 96, 110)
bg = Background(top=(30, 8, 40), bottom=(60, 14, 70), blobs=[(255, 90, 170), (150, 70, 255), (255, 170, 80)], seed=2882)


def card(w, h, fill):
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    ImageDraw.Draw(im).rounded_rectangle([0, 0, w - 1, h - 1], radius=int(w * 0.05), fill=(*fill, 255))
    return im


def tpl_countdown(w, h):
    im = card(w, h, (20, 24, 48)); d = ImageDraw.Draw(im); s = w / 600
    d.text((w / 2, h * 0.2), "BLACK FRIDAY", font=font(F_XB, 44 * s), fill=(*GOLD, 255), anchor="mm")
    d.text((w / 2, h * 0.47), "3", font=font(F_BLACK, 220 * s), fill=(255, 255, 255, 255), anchor="mm")
    d.text((w / 2, h * 0.72), "DAYS LEFT", font=font(F_BLACK, 64 * s), fill=(255, 255, 255, 255), anchor="mm")
    d.text((w / 2, h * 0.87), "your shop name here", font=font(F_MED, 30 * s), fill=(180, 186, 210, 255), anchor="mm")
    return im


def tpl_giftcard(w, h):
    im = card(w, h, (250, 236, 220)); d = ImageDraw.Draw(im); s = w / 600
    d.rounded_rectangle([40 * s, 40 * s, w - 40 * s, h - 40 * s], radius=int(24 * s), outline=(196, 60, 70, 255), width=int(6 * s))
    d.text((w / 2, h * 0.28), "GIFT CARD", font=font(F_BLACK, 70 * s), fill=(196, 60, 70, 255), anchor="mm")
    d.text((w / 2, h * 0.5), "$25", font=font(F_BLACK, 150 * s), fill=(*INK, 255), anchor="mm")
    d.text((w / 2, h * 0.72), "To: ________   From: ________", font=font(F_SEMI, 30 * s), fill=(90, 90, 100, 255), anchor="mm")
    return im


def tpl_thanks(w, h):
    im = card(w, h, (226, 244, 236)); d = ImageDraw.Draw(im); s = w / 600
    d.text((w / 2, h * 0.24), "Thank you", font=font(F_BLACK, 88 * s), fill=(20, 110, 80, 255), anchor="mm")
    d.text((w / 2, h * 0.38), "for your order!", font=font(F_XB, 50 * s), fill=(20, 110, 80, 255), anchor="mm")
    d.text((w / 2, h * 0.58), "Enjoy 10% off next time:", font=font(F_SEMI, 34 * s), fill=(*INK, 255), anchor="mm")
    d.rounded_rectangle([w / 2 - 150 * s, h * 0.66, w / 2 + 150 * s, h * 0.78], radius=int(20 * s), fill=(20, 110, 80, 255))
    d.text((w / 2, h * 0.72), "THANKS10", font=font(F_BLACK, 44 * s), fill=(255, 255, 255, 255), anchor="mm")
    return im


TEMPLATES = [("Countdown sale post", tpl_countdown, "⏳"), ("Printable gift card", tpl_giftcard, "🎁"), ("Thank-you order insert", tpl_thanks, "💌")]


def todo(sub, t, start, cy=860):
    k = p(t, start, 0.45)
    if k <= 0: return
    w, h = 820, 640
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=44, fill=(255, 249, 214, 255))
    d.text((50, 70), "Shop to-do: November", font=font(F_BLACK, 50), fill=(*INK, 255), anchor="lm")
    items = [("Order extra stock", True), ("Pack & ship orders", True), ("Answer customer DMs", True), ("Design sale posts", False)]
    for i, (lab, ok) in enumerate(items):
        kk = p(t, start + 0.5 + i * 0.55, 0.3)
        if kk <= 0: continue
        y = 180 + i * 110
        a = int(255 * out_cubic(kk))
        d.rounded_rectangle([50, y - 30, 110, y + 30], radius=12, outline=(*INK, a), width=5)
        if ok:
            d.line([(62, y), (78, y + 18), (102, y - 20)], fill=(20, 150, 90, a), width=9)
        else:
            d.text((80, y), "?", font=font(F_BLACK, 44), fill=(220, 50, 70, a), anchor="mm")
        d.text((140, y), lab, font=font(F_XB, 46), fill=(*INK, a) if ok else (220, 50, 70, a), anchor="lm")
    sub.alpha_composite(with_alpha(im, out_cubic(k)), (int(W / 2 - w / 2), int(cy - h / 2 + 60 * (1 - out_cubic(k)))))


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, 0.0, 0.3)
        place_emoji(sub, "🛍️", W / 2, 500 + 12 * math.sin(t * 6), 200 * out_back(k), alpha=k, rot=6 * math.sin(t * 4))
        pop_words(sub, ["3 Canva templates", "shops need before", "Black Friday"], t, 0.0, 930, 92, (WHITE, GOLD), gap=0.07, highlight={"3", "black", "friday"})
        kk = p(t, 1.3, 0.4)
        pill(sub, W / 2, 1290, "Make them this weekend", F_SEMI, 48, WHITE, INK, alpha=out_cubic(kk), scale=out_back(kk), icon="🗓️")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["A small shop owner's", "November looks like this"], t, s1 + 0.1, 330, 70, (WHITE, ACC), gap=0.07, highlight={"november"})
        todo(sub, t, s1 + 0.6, cy=820)
        kk = p(t, s1 + 3.8, 0.4)
        pill(sub, W / 2, 1270, "No time to design = your gig", F_XB, 54, GOLD, INK, alpha=out_cubic(kk), scale=out_back(kk), icon="💡")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        seg = 2.6
        i = min(2, int((t - s2) / seg))
        lt = t - s2 - i * seg
        name, fn, ic = TEMPLATES[i]
        kk = clamp(lt / 0.4)
        draw_text(sub, f"#{i + 1}", F_BLACK, 120, W / 2, 330, ACC, alpha=out_cubic(kk), scale=out_back(kk))
        im = fn(640, 640)
        sc = 0.6 + 0.4 * out_back(kk)
        im = im.resize((int(640 * sc), int(640 * sc)))
        out_a = 1 - p(lt, seg - 0.25, 0.25) if i < 2 else 1
        sub.alpha_composite(with_alpha(im, out_cubic(kk) * out_a), (int(W / 2 - im.width / 2), int(820 - im.height / 2)))
        kp = p(lt, 0.3, 0.35)
        pill(sub, W / 2, 1270, name, F_XB, 56, WHITE, INK, alpha=out_cubic(kp) * out_a, scale=out_back(kp), icon=ic)
        faded(layer, sub, t, s2, e2, slide=False)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Bundle all 3"], t, s3 + 0.1, 290, 88, (WHITE, GOLD), gap=0.07, highlight={"3"})
        fns = [tpl_countdown, tpl_giftcard, tpl_thanks]
        for i, fn in enumerate(fns):
            kk = p(t, s3 + 0.4 + i * 0.25, 0.45)
            if kk <= 0: continue
            im = fn(300, 300).rotate((i - 1) * -8, resample=Image.BICUBIC, expand=True)
            x = W / 2 + (i - 1) * 250
            y = 630 + abs(i - 1) * 30
            sub.alpha_composite(with_alpha(im, out_cubic(kk)), (int(x - im.width / 2), int(y - im.height / 2 + 80 * (1 - out_cubic(kk)))))
        kk = p(t, s3 + 1.4, 0.4)
        pill(sub, W / 2, 900, "Holiday Shop Kit  ·  $15", F_BLACK, 58, ACC, INK, alpha=out_cubic(kk), scale=out_back(kk), icon="🏷️")
        checklist(sub, t, s3 + 2.2, ["Editable in free Canva", "Instant download", "Nothing to ship"], 1050, 105, ACC, size=50, x0=220)
        draw_text(sub, "Example pricing. Results depend on your work.", F_MED, 36, W / 2, 1400, SOFT, alpha=out_cubic(p(t, s3 + 4.6, 0.5)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel2.mp4")
