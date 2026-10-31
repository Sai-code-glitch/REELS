"""Helpers for the 2026-10-31 Google review QR card reels (review rows, QR counter card, profile 'Ask for reviews' panel)."""
import random
from reel_giftcard import *
from reel_portfolio import timer

STAR = (251, 188, 5)
GBLUE = (26, 115, 232)


def qr_img(size, seed=7, fg=(20, 22, 30), bg=(255, 255, 255)):
    """Pseudo QR-style pattern (decorative mock, not a scannable code)."""
    n = 25
    rnd = random.Random(seed)
    cell = size / (n + 2)
    im = Image.new("RGBA", (size, size), (*bg, 255))
    d = ImageDraw.Draw(im)
    def finder(cx, cy):
        x0, y0 = (cx + 1) * cell, (cy + 1) * cell
        d.rectangle([x0, y0, x0 + 7 * cell, y0 + 7 * cell], fill=(*fg, 255))
        d.rectangle([x0 + cell, y0 + cell, x0 + 6 * cell, y0 + 6 * cell], fill=(*bg, 255))
        d.rectangle([x0 + 2 * cell, y0 + 2 * cell, x0 + 5 * cell, y0 + 5 * cell], fill=(*fg, 255))
    for i in range(n):
        for j in range(n):
            if (i < 8 and j < 8) or (i > n - 9 and j < 8) or (i < 8 and j > n - 9):
                continue
            if rnd.random() < 0.48:
                d.rectangle([(i + 1) * cell, (j + 1) * cell, (i + 2) * cell, (j + 2) * cell], fill=(*fg, 255))
    finder(0, 0); finder(n - 7, 0); finder(0, n - 7)
    return im


def stars_row(d, x, y, size, n=5, color=STAR, anchor_center=True, alpha=255):
    f = font(DEJAVU, size)
    s = "★" * n
    d.text((x, y), s, font=f, fill=(*color, alpha), anchor="mm" if anchor_center else "lm")


def review_row(sub, t, start, cy, icon, color, name, rating, count, last, flag_at, lead, w=880, h=210):
    """Maps-style result row with rating, review count and last-review age. lead -> gold outline + red tag."""
    k = p(t, start, 0.4)
    if k <= 0: return
    c, d = gbase(w, h, fill=(255, 255, 255))
    if lead and t >= flag_at:
        d.rounded_rectangle([0, 0, w - 1, h - 1], radius=40, outline=(*GOLD_C, 255), width=8)
    d.rounded_rectangle([28, 28, 154, 154], radius=28, fill=(*color, 255))
    e = emoji_img(icon, 82)
    c.alpha_composite(e, (int(91 - e.width / 2), int(91 - e.height / 2)))
    d.text((184, 56), name, font=font(F_XB, 42), fill=(*INK, 255), anchor="lm")
    d.text((184, 108), f"{rating}", font=font(F_XB, 34), fill=(*INK, 255), anchor="lm")
    stars_row(d, 240, 108, 32, anchor_center=False)
    d.text((410, 108), f"({count})", font=font(F_SEMI, 34), fill=(*GREY, 255), anchor="lm")
    d.text((184, 160), f"Last review: {last}", font=font(F_SEMI, 30), fill=(*GREY, 255), anchor="lm")
    kf = p(t, flag_at, 0.35)
    if kf > 0:
        lab = "Few reviews" if lead else "Busy profile"
        col = RED if lead else GREEN
        ff = font(F_XB, 30)
        tw = d.textlength(lab, font=ff) + 40
        d.rounded_rectangle([w - 34 - tw, 34, w - 34, 86], radius=26, fill=(*col, int(255 * out_cubic(kf))))
        d.text((w - 34 - tw / 2, 60), lab, font=ff, fill=(255, 255, 255, int(255 * out_cubic(kf))), anchor="mm")
    with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2 + 60 * (1 - out_cubic(k))), int(cy - h / 2)))


def table_card(sub, t, start, cx, cy, shop, emoji, color, w=600, h=840, rot=0.0, steps=None, seed=7):
    """Counter / table card asking for a Google review. steps: 5 reveal times (bg, headline, stars, qr, footer)."""
    k = p(t, start, 0.45)
    if k <= 0: return
    a = [1.0] * 5 if steps is None else [out_cubic(p(t, s, 0.45)) for s in steps]
    tw_, th_ = w, h
    w, h = 600, 840
    c = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(c)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=36, fill=(255, 255, 255, 255))
    if a[0] > 0:
        al = int(255 * a[0])
        d.rounded_rectangle([0, 0, w - 1, 250], radius=36, fill=(*color, al))
        d.rectangle([0, 200, w - 1, 250], fill=(*color, al))
        e = with_alpha(emoji_img(emoji, 90).copy(), a[0])
        c.alpha_composite(e, (int(w / 2 - e.width / 2), 30))
        d.text((w / 2, 190), shop, font=font(F_BLACK, 46), fill=(255, 255, 255, al), anchor="mm")
    if a[1] > 0:
        al = int(255 * a[1])
        d.text((w / 2, 310), "Loved your visit?", font=font(F_BLACK, 50), fill=(*INK, al), anchor="mm")
    if a[2] > 0:
        stars_row(d, w / 2, 380, 58, alpha=int(255 * a[2]))
    if a[3] > 0:
        qs = int(330 * (0.7 + 0.3 * out_back(min(1, a[3]))))
        q = with_alpha(qr_img(qs, seed), a[3])
        c.alpha_composite(q, (int(w / 2 - qs / 2), int(595 - qs / 2)))
    if a[4] > 0:
        al = int(255 * a[4])
        d.text((w / 2, 795), "Scan to review us on Google", font=font(F_XB, 32), fill=(*GREY, al), anchor="mm")
    s = 0.6 + 0.4 * out_back(k)
    c = c.resize((max(1, int(tw_ * s)), max(1, int(th_ * s))), Image.LANCZOS)
    if rot:
        c = c.rotate(rot, resample=Image.BICUBIC, expand=True)
    with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(cx - c.width / 2), int(cy - c.height / 2)))


def profile_panel(sub, t, start, top, shop, emoji, color, ask_at, link_at, copy_at, w=880, h=760, link="g.page/r/rosas-bakery/review"):
    """Mock 'your business profile' panel: buttons, 'Ask for reviews' highlight, share-link sheet with Copy."""
    k = p(t, start, 0.45)
    if k <= 0: return
    c, d = gbase(w, h, fill=(255, 255, 255))
    d.text((50, 66), "YOUR BUSINESS ON GOOGLE", font=font(F_XB, 28), fill=(*GREY, 255), anchor="lm")
    d.rounded_rectangle([50, 110, 170, 230], radius=28, fill=(*color, 255))
    e = emoji_img(emoji, 80)
    c.alpha_composite(e, (int(110 - e.width / 2), int(170 - e.height / 2)))
    d.text((200, 148), shop, font=font(F_BLACK, 48), fill=(*INK, 255), anchor="lm")
    d.text((200, 205), "4.9", font=font(F_XB, 32), fill=(*INK, 255), anchor="lm")
    stars_row(d, 252, 205, 30, anchor_center=False)
    d.text((412, 205), "(11)", font=font(F_SEMI, 32), fill=(*GREY, 255), anchor="lm")
    btns = [("✎", "Edit profile"), ("★", "Ask for reviews"), ("↗", "Promote")]
    bw = (w - 100 - 40) / 3
    ka = out_cubic(p(t, ask_at, 0.35))
    for i, (ic, lab) in enumerate(btns):
        x0 = 50 + i * (bw + 20); y0 = 270
        hi = i == 1 and ka > 0
        fill = (232, 240, 254) if not hi else tuple(int(232 + (v - 232) * ka) for v in GBLUE)
        d.rounded_rectangle([x0, y0, x0 + bw, y0 + 150], radius=28, fill=(*fill, 255))
        fg = (*GBLUE, 255) if not hi or ka < 0.5 else (255, 255, 255, 255)
        d.text((x0 + bw / 2, y0 + 50), ic, font=font(DEJAVU, 46), fill=fg, anchor="mm")
        d.text((x0 + bw / 2, y0 + 112), lab, font=font(F_XB, 27), fill=fg, anchor="mm")
    kl = p(t, link_at, 0.4)
    if kl > 0:
        al = int(255 * out_cubic(kl))
        y0 = 470 + int(40 * (1 - out_cubic(kl)))
        d.rounded_rectangle([30, y0, w - 30, y0 + 260], radius=32, fill=(244, 246, 250, al), outline=(220, 224, 232, al), width=3)
        d.text((70, y0 + 52), "Share review link", font=font(F_XB, 36), fill=(*INK, al), anchor="lm")
        d.rounded_rectangle([70, y0 + 100, w - 70, y0 + 210], radius=26, fill=(255, 255, 255, al))
        d.text((100, y0 + 155), link, font=font(F_SEMI, 32), fill=(*GBLUE, al), anchor="lm")
        kc = p(t, copy_at, 0.3)
        lab = "Copied!" if kc > 0 else "Copy"
        col = GREEN if kc > 0 else GBLUE
        ff = font(F_XB, 30)
        tw = d.textlength(lab, font=ff) + 36
        d.rounded_rectangle([w - 90 - tw, y0 + 127, w - 90, y0 + 183], radius=28, fill=(*col, al))
        d.text((w - 90 - tw / 2, y0 + 155), lab, font=ff, fill=(255, 255, 255, al), anchor="mm")
    with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(top + 60 * (1 - out_cubic(k)))))
