"""Helpers for the 2026-11-13 'holiday cash from stuff you already own' reels
(Facebook Marketplace listing card bad/good, eBay search + Sold items filter + sold rows,
room-sweep item tiles, 'Your listings' panel)."""
from reel_menu import *

FB_BLUE2 = (8, 102, 255)
EBAY = [(229, 50, 56), (0, 100, 210), (245, 175, 2), (134, 184, 23)]
SOLD_G = (20, 140, 70)


def dim(im, k):
    """Scale RGB of an RGBA image by k, keep alpha."""
    r, g, b, a = im.split()
    r, g, b = [ch.point(lambda v: int(v * k)) for ch in (r, g, b)]
    return Image.merge("RGBA", (r, g, b, a))


def _listing_img(w, emoji, title, price, loc, desc, good, photo_h=420):
    f_t = font(F_XB, 46)
    tmp = ImageDraw.Draw(Image.new("RGBA", (10, 10)))
    tl = layout_words(tmp, title.split(), f_t, w - 90)
    h = photo_h + 60 + len(tl) * 60 + 70 + 60 + len(desc) * 50 + 40
    c, d = gbase(w, h, fill=(255, 255, 255))
    pc = (238, 242, 248) if good else (58, 54, 50)
    d.rounded_rectangle([0, 0, w - 1, photo_h], radius=40, fill=(*pc, 255))
    d.rectangle([0, photo_h - 40, w - 1, photo_h], fill=(*pc, 255))
    if good:
        d.ellipse([w / 2 - 230, photo_h * 0.12, w / 2 + 230, photo_h * 0.95], fill=(255, 250, 230, 255))
    e = emoji_img(emoji, int(photo_h * 0.6))
    if not good:
        e = dim(e, 0.32).rotate(-14, resample=Image.BICUBIC, expand=True)
    c.alpha_composite(e, (int(w / 2 - e.width / 2), int(photo_h / 2 - e.height / 2)))
    # photo dots (1 photo vs 3 photos)
    n = 3 if good else 1
    for i in range(n):
        x = w / 2 + (i - (n - 1) / 2) * 30
        d.ellipse([x - 8, photo_h - 34, x + 8, photo_h - 18], fill=(255, 255, 255, 255 if i == 0 else 140))
    y = photo_h + 50
    d.text((45, y), price, font=font(F_BLACK, 54), fill=(*INK, 255), anchor="lm")
    y += 62
    for ln in tl:
        d.text((45, y), " ".join(wd for _, wd, _ in ln), font=f_t, fill=(*INK, 255), anchor="lm")
        y += 60
    d.text((45, y + 4), loc, font=font(F_SEMI, 34), fill=(*GREY, 255), anchor="lm")
    y += 60
    d.line([45, y, w - 45, y], fill=(228, 231, 238, 255), width=3)
    y += 40
    for ln in desc:
        d.text((45, y), ln, font=font(F_SEMI, 36), fill=(60, 66, 80, 255), anchor="lm")
        y += 50
    return c


def mp_listing(sub, t, start, top, emoji, bad, good, swap_at=None, flags=None, flag_at=None, w=860, cx=None, show_good_only=False):
    """Marketplace listing. bad/good = (title, price, loc, [desc lines]). Crossfades bad -> good at swap_at.
    flags: list of (label, y_offset) red pills shown on the bad card from flag_at."""
    k = p(t, start, 0.4)
    if k <= 0: return
    ks = 1.0 if show_good_only else (out_cubic(p(t, swap_at, 0.5)) if swap_at is not None else 0.0)
    x = int((cx if cx is not None else W / 2) - w / 2)
    yoff = int(top + 60 * (1 - out_cubic(k)))
    if ks < 1:
        c = _listing_img(w, emoji, *bad, good=False)
        if flags and flag_at is not None:
            d = ImageDraw.Draw(c)
            for i, (lab, fy) in enumerate(flags):
                kf = p(t, flag_at + i * 0.5, 0.35)
                if kf <= 0: continue
                ff = font(F_XB, 34)
                tw = d.textlength(lab, font=ff) + 60
                al = int(255 * out_cubic(kf))
                x1 = w - 30
                d.rounded_rectangle([x1 - tw, fy - 30, x1, fy + 30], radius=30, fill=(*RED2, al))
                d.text((x1 - tw / 2, fy), lab, font=ff, fill=(255, 255, 255, al), anchor="mm")
        with_alpha(c, out_cubic(k) * (1 - ks))
        sub.alpha_composite(c, (x, yoff))
    if ks > 0:
        c = _listing_img(w, emoji, *good, good=True)
        with_alpha(c, out_cubic(k) * ks)
        sub.alpha_composite(c, (x, yoff + int(20 * (1 - ks))))


def ebay_search(sub, t, start, cy, query, w=880, type_dur=1.2):
    k = p(t, start, 0.35)
    if k <= 0: return
    h = 130
    c, d = gbase(w, h, fill=(255, 255, 255), radius=65)
    f_logo = font(F_BLACK, 52)
    x = 44
    for ch, col in zip("ebay", EBAY):
        d.text((x, h / 2), ch, font=f_logo, fill=(*col, 255), anchor="lm")
        x += d.textlength(ch, font=f_logo) - 2
    d.line([200, 30, 200, h - 30], fill=(220, 224, 232, 255), width=3)
    n = int(len(query) * p(t, start + 0.2, type_dur))
    txt = query[:n]
    f = font(F_XB, 44)
    d.text((228, h / 2), txt, font=f, fill=(*INK, 255), anchor="lm")
    if n < len(query) or (t * 2) % 1 < 0.5:
        xx = 228 + d.textlength(txt, font=f) + 4
        d.line([xx, 38, xx, h - 38], fill=(*EBAY[1], 255), width=4)
    d.ellipse([w - 110, 20, w - 20, h - 20], fill=(*EBAY[1], 255))
    d.ellipse([w - 82, 44, w - 54, 72], outline=(255, 255, 255, 255), width=5)
    d.line([w - 58, 70, w - 44, 84], fill=(255, 255, 255, 255), width=6)
    s = out_back(k)
    c = with_alpha(c.resize((max(1, int(w * s)), max(1, int(h * s)))), out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - c.width / 2), int(cy - c.height / 2)))


def filter_toggle(sub, t, start, cy, on_at, label="Sold items", w=880, h=150, tap=True):
    k = p(t, start, 0.4)
    if k <= 0: return
    c, d = gbase(w, h, fill=(255, 255, 255))
    d.text((50, h / 2), "Filter", font=font(F_SEMI, 34), fill=(*GREY, 255), anchor="lm")
    d.text((190, h / 2), label, font=font(F_XB, 48), fill=(*INK, 255), anchor="lm")
    ko = in_out(p(t, on_at, 0.3))
    tw, th = 150, 80
    x0, y0 = w - 60 - tw, h / 2 - th / 2
    off, on = (200, 204, 214), SOLD_G
    col = tuple(int(off[i] + (on[i] - off[i]) * ko) for i in range(3))
    d.rounded_rectangle([x0, y0, x0 + tw, y0 + th], radius=th / 2, fill=(*col, 255))
    kx = x0 + th / 2 + (tw - th) * ko
    d.ellipse([kx - 32, h / 2 - 32, kx + 32, h / 2 + 32], fill=(255, 255, 255, 255))
    with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(cy - h / 2 + 60 * (1 - out_cubic(k)))))
    if tap:
        kt = p(t, on_at - 0.5, 0.5)
        if 0 < kt and t < on_at + 0.6:
            place_emoji(sub, "👆", W / 2 + w / 2 - 110 + 30 * (1 - kt), cy + 90 + 40 * (1 - kt), 100, alpha=min(1, kt * 2) * (1 - p(t, on_at + 0.3, 0.3)))


def sold_row(sub, t, start, cy, emoji, color, title, price, when, w=880, h=170, hl_at=None):
    k = p(t, start, 0.4)
    if k <= 0: return
    c, d = gbase(w, h, fill=(255, 255, 255))
    if hl_at is not None and t >= hl_at:
        d.rounded_rectangle([0, 0, w - 1, h - 1], radius=40, outline=(*GOLD_C, 255), width=8)
    d.rounded_rectangle([22, 22, h - 22, h - 22], radius=24, fill=(*color, 255))
    e = emoji_img(emoji, 76)
    c.alpha_composite(e, (int(h / 2 - e.width / 2), int(h / 2 - e.height / 2)))
    d.text((h + 6, 58), title, font=font(F_SEMI, 34), fill=(60, 66, 80, 255), anchor="lm")
    d.text((h + 6, 118), price, font=font(F_BLACK, 50), fill=(*SOLD_G, 255), anchor="lm")
    d.text((w - 44, 118), when, font=font(F_XB, 30), fill=(*SOLD_G, 255), anchor="rm")
    with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2 + 60 * (1 - out_cubic(k))), int(cy - h / 2)))


def item_tile(sub, t, start, cx, cy, emoji, label, color, size=380, check_at=None, price=None):
    k = p(t, start, 0.4)
    if k <= 0: return
    c, d = gbase(size, size, fill=(255, 255, 255))
    d.rounded_rectangle([24, 24, size - 24, size * 0.68], radius=30, fill=(*color, 255))
    e = emoji_img(emoji, int(size * 0.38))
    c.alpha_composite(e, (int(size / 2 - e.width / 2), int(size * 0.35 - e.height / 2 + 12)))
    d.text((size / 2, size * 0.83), label, font=font(F_XB, int(size * 0.095)), fill=(*INK, 255), anchor="mm")
    if check_at is not None:
        kc = p(t, check_at, 0.35)
        if kc > 0:
            r = 40 * out_back(kc)
            d.ellipse([size - 80 - r, 70 - r, size - 80 + r, 70 + r], fill=(*SOLD_G, 255))
            d.text((size - 80, 72), "✓", font=font(DEJAVU, int(46 * out_back(kc)) + 1), fill=(255, 255, 255, 255), anchor="mm")
    if price is not None:
        lab, at = price
        kp = p(t, at, 0.35)
        if kp > 0:
            ff = font(F_BLACK, 44)
            tw = d.textlength(lab, font=ff) + 40
            al = int(255 * out_cubic(kp))
            d.rounded_rectangle([40, 40, 40 + tw, 104], radius=32, fill=(*GOLD_C, al))
            d.text((40 + tw / 2, 72), lab, font=ff, fill=(*INK, al), anchor="mm")
    s = 0.6 + 0.4 * out_back(k)
    c = with_alpha(c.resize((max(1, int(size * s)), max(1, int(size * s)))), out_cubic(k))
    sub.alpha_composite(c, (int(cx - c.width / 2), int(cy - c.height / 2)))


def listings_panel(sub, t, start, top, rows, w=880, row_h=132, title="Your listings"):
    """rows: (emoji, color, name, price, status_at) status flips Active -> Sold at status_at (None = stays Active)."""
    k = p(t, start, 0.45)
    if k <= 0: return
    h = 130 + row_h * len(rows) + 30
    c, d = gbase(w, h, fill=(255, 255, 255))
    d.text((50, 70), title, font=font(F_BLACK, 50), fill=(*INK, 255), anchor="lm")
    d.text((w - 50, 70), "Marketplace", font=font(F_XB, 32), fill=(*FB_BLUE2, 255), anchor="rm")
    for i, (em, col, name, price, sat) in enumerate(rows):
        y = 130 + i * row_h
        kk = p(t, start + 0.3 + i * 0.25, 0.35)
        if kk <= 0: continue
        al = int(255 * out_cubic(kk))
        d.line([40, y, w - 40, y], fill=(232, 235, 240, al), width=2)
        d.rounded_rectangle([40, y + 16, 40 + row_h - 32, y + row_h - 16], radius=20, fill=(*col, al))
        e = emoji_img(em, 64)
        c.alpha_composite(with_alpha(e.copy(), out_cubic(kk)), (int(40 + (row_h - 32) / 2 - e.width / 2), int(y + row_h / 2 - e.height / 2)))
        d.text((40 + row_h, y + row_h / 2 - 20), name, font=font(F_XB, 38), fill=(*INK, al), anchor="lm")
        d.text((40 + row_h, y + row_h / 2 + 26), price, font=font(F_SEMI, 32), fill=(*GREY, al), anchor="lm")
        sold = sat is not None and t >= sat
        lab, colr = ("Sold", SOLD_G) if sold else ("Active", FB_BLUE2)
        ff = font(F_XB, 30)
        tw = d.textlength(lab, font=ff) + 44
        d.rounded_rectangle([w - 50 - tw, y + row_h / 2 - 28, w - 50, y + row_h / 2 + 28], radius=28, fill=(*colr, al))
        d.text((w - 50 - tw / 2, y + row_h / 2), lab, font=ff, fill=(255, 255, 255, al), anchor="mm")
    with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(top + 60 * (1 - out_cubic(k)))))
    return h
