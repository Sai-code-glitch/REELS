"""Helpers for the 2026-11-14 'sell a 2027 printable calendar on Etsy' reels
(printable month page with real 2027 dates, Canva calendar editor, 12-page PDF fan,
niche search rows, Etsy digital-listing form, fee breakdown)."""
import calendar as _cal
from reel_market import *

MONTHS = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]
CANVA = (110, 70, 230)


def month_page(c, d, x, y, w, a, acc, month=1, year=2027, emoji="🐶", title_extra="Dog Mom", paper=(255, 253, 248)):
    """Printable portrait month page (8.5x11 ratio) drawn on canvas c at (x,y).
    a = list of 5 alphas: [grid, month title, theme emoji/banner, accent colour, footer]."""
    h = int(w * 11 / 8.5)
    d.rectangle([x, y, x + w, y + h], fill=(*paper, 255))
    a = list(a) + [1.0] * (5 - len(a))
    band = int(h * 0.26)
    if a[3] > 0:
        col = tuple(int(255 + (cc - 255) * a[3]) for cc in acc)
        d.rectangle([x, y, x + w, y + band], fill=(*col, 255))
    if a[2] > 0:
        e = emoji_img(emoji, int(band * 0.62))
        e = with_alpha(e, a[2])
        c.alpha_composite(e, (int(x + w - e.width - w * 0.06), int(y + band / 2 - e.height / 2)))
    if a[1] > 0:
        al = int(255 * a[1])
        tc = INK if a[3] < 0.5 else (255, 255, 255)
        d.text((x + w * 0.07, y + band * 0.42), MONTHS[month - 1], font=font(F_BLACK, w * 0.115), fill=(*tc, al), anchor="lm")
        d.text((x + w * 0.07, y + band * 0.75), f"{year} · {title_extra}", font=font(F_XB, w * 0.05), fill=(*tc, al), anchor="lm")
    if a[0] > 0:
        al = int(255 * a[0])
        gx0, gx1 = x + w * 0.05, x + w * 0.95
        gy0 = y + band + h * 0.04
        cw = (gx1 - gx0) / 7
        fh = font(F_XB, w * 0.04)
        for i, dn in enumerate(["S", "M", "T", "W", "T", "F", "S"]):
            d.text((gx0 + cw * (i + 0.5), gy0), dn, font=fh, fill=(*GREY, al), anchor="mm")
        weeks = _cal.Calendar(firstweekday=6).monthdayscalendar(year, month)
        rh = (y + h * 0.93 - gy0 - h * 0.03) / 6
        fd = font(F_SEMI, w * 0.042)
        for r, wk in enumerate(weeks):
            for ci, day in enumerate(wk):
                cx0 = gx0 + cw * ci
                cy0 = gy0 + h * 0.03 + rh * r
                d.rectangle([cx0, cy0, cx0 + cw, cy0 + rh], outline=(218, 214, 206, al), width=2)
                if day:
                    d.text((cx0 + cw * 0.12, cy0 + rh * 0.08), str(day), font=fd, fill=(*INK, al), anchor="lt")
    if a[4] > 0:
        d.text((x + w / 2, y + h * 0.965), "Printable · US Letter", font=font(F_SEMI, w * 0.032), fill=(*GREY, int(255 * a[4])), anchor="mm")
    return h


def page_card(sub, t, start, cx, cy, acc, w=420, rot=0.0, steps=None, shadow=True, **kw):
    """A month page that pops in (optionally building over steps)."""
    k = p(t, start, 0.45)
    if k <= 0: return
    h = int(w * 11 / 8.5)
    pad = 24
    c = Image.new("RGBA", (w + 2 * pad, h + 2 * pad), (0, 0, 0, 0))
    d = ImageDraw.Draw(c)
    if shadow:
        d.rectangle([pad + 10, pad + 14, pad + w + 10, pad + h + 14], fill=(0, 0, 0, 70))
    a = [out_cubic(p(t, s, 0.45)) for s in steps] if steps else [1] * 5
    month_page(c, d, pad, pad, w, a, acc, **kw)
    s = 0.6 + 0.4 * out_back(k)
    c = c.resize((max(1, int(c.width * s)), max(1, int(c.height * s))), Image.LANCZOS)
    if rot: c = c.rotate(rot, resample=Image.BICUBIC, expand=True)
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(cx - c.width / 2), int(cy - c.height / 2)))


def canva_cal(sub, t, start, cy, acc, steps, w=880, h=1100, labels=None, dup_at=None, **kw):
    """Canva-style editor building a month page over steps[0..4]; dup_at shows 'Page 1 of 12'."""
    k = p(t, start, 0.45)
    if k <= 0: return
    c, d = card_base(w, h, radius=36, fill=(236, 239, 245, 255))
    d.rounded_rectangle([0, 0, w - 1, 100], radius=36, fill=(*CANVA, 255))
    d.rectangle([0, 60, w - 1, 100], fill=(*CANVA, 255))
    d.text((40, 52), "Calendar · US Letter", font=font(F_XB, 32), fill=(255, 255, 255, 255), anchor="lm")
    d.rounded_rectangle([w - 210, 24, w - 34, 80], radius=28, fill=(255, 255, 255, 255))
    d.text((w - 122, 52), "Share", font=font(F_XB, 30), fill=(*CANVA, 255), anchor="mm")
    tools = [("🗓️", "Template"), ("🔤", "Text"), ("⭐", "Elements"), ("🎨", "Color")]
    n = sum(1 for s in steps if t >= s)
    for i, (ic, lab) in enumerate(tools):
        yy = 190 + i * 160
        if n > 0 and i == min(3, n - 1):
            d.rounded_rectangle([14, yy - 56, 126, yy + 70], radius=20, fill=(220, 210, 255, 255))
        e = emoji_img(ic, 54)
        c.alpha_composite(e, (int(70 - e.width / 2), int(yy - e.height / 2)))
        d.text((70, yy + 50), lab, font=font(F_SEMI, 22), fill=(*INK, 255), anchor="mm")
    pw = 560
    x, y = 160 + (w - 160 - pw) // 2, 135
    ph = int(pw * 11 / 8.5)
    d.rectangle([x - 4, y - 4, x + pw + 4, y + ph + 4], fill=(205, 209, 218, 255))
    a = [out_cubic(p(t, st, 0.45)) for st in steps]
    month_page(c, d, x, y, pw, a, acc, **kw)
    if dup_at is not None and t >= dup_at:
        kd = p(t, dup_at, 1.2)
        num = max(1, int(round(1 + 11 * out_cubic(kd))))
        lab = f"Pages: {num} of 12"
        ff = font(F_XB, 34)
        tw = d.textlength(lab, font=ff) + 50
        d.rounded_rectangle([x + pw - tw, y + ph - 70, x + pw - 10, y + ph - 16], radius=27, fill=(*CANVA, 255))
        d.text((x + pw - 10 - (tw - 10) / 2, y + ph - 43), lab, font=ff, fill=(255, 255, 255, 255), anchor="mm")
    if labels and n > 0:
        kk = out_cubic(p(t, steps[n - 1], 0.3))
        d.rounded_rectangle([140, h - 120, w - 40, h - 26], radius=30, fill=(255, 255, 255, 255))
        d.text(((140 + w - 40) / 2, h - 73), labels[n - 1], font=font(F_XB, 38), fill=(*INK, int(255 * kk)), anchor="mm")
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(cy - h / 2 + 60 * (1 - out_cubic(k)))))


def twelve_fan(sub, t, start, cy, acc, every=0.12, w=190, cols=4, gapx=24, gapy=26, **kw):
    """12 mini month pages flying into a 4x3 grid."""
    h = int(w * 11 / 8.5)
    tot_w = cols * w + (cols - 1) * gapx
    rows = 12 // cols
    tot_h = rows * h + (rows - 1) * gapy
    for i in range(12):
        kk = p(t, start + i * every, 0.4)
        if kk <= 0: continue
        r, cc = divmod(i, cols)
        tx = W / 2 - tot_w / 2 + cc * (w + gapx) + w / 2
        ty = cy - tot_h / 2 + r * (h + gapy) + h / 2
        a = out_cubic(kk)
        x = lerp(W / 2, tx, a); y = lerp(cy + 300, ty, a)
        c = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        d = ImageDraw.Draw(c)
        month_page(c, d, 0, 0, w - 1, [1, 1, 1, 1, 0], acc, month=i + 1, **kw)
        c = with_alpha(c, a)
        sub.alpha_composite(c, (int(x - w / 2), int(y - h / 2)))


def niche_row(sub, t, start, cy, emoji, color, query, verdict, good, flag_at, w=880, h=150):
    """Search-suggestion row: emoji tile + query + verdict pill (green good / red bad)."""
    k = p(t, start, 0.4)
    if k <= 0: return
    c, d = gbase(w, h, fill=(255, 255, 255), radius=34)
    if good and t >= flag_at + 0.3:
        d.rounded_rectangle([0, 0, w - 1, h - 1], radius=34, outline=(*GOLD_C, 255), width=8)
    d.rounded_rectangle([22, 22, h - 22, h - 22], radius=24, fill=(*color, 255))
    e = emoji_img(emoji, 64)
    c.alpha_composite(e, (int(h / 2 - e.width / 2), int(h / 2 - e.height / 2)))
    d.ellipse([h + 6, h / 2 - 16, h + 30, h / 2 + 8], outline=(*GREY, 255), width=4)
    d.line([h + 26, h / 2 + 4, h + 36, h / 2 + 14], fill=(*GREY, 255), width=5)
    d.text((h + 52, h / 2), query, font=font(F_XB, 40), fill=(*INK, 255), anchor="lm")
    kf = p(t, flag_at, 0.35)
    if kf > 0:
        ff = font(F_XB, 30)
        tw = d.textlength(verdict, font=ff) + 40
        al = int(255 * out_cubic(kf))
        col = OKG if good else RED2
        d.rounded_rectangle([w - 26 - tw, h / 2 - 28, w - 26, h / 2 + 28], radius=28, fill=(*col, al))
        d.text((w - 26 - tw / 2, h / 2), verdict, font=ff, fill=(255, 255, 255, al), anchor="mm")
    with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2 + 60 * (1 - out_cubic(k))), int(cy - h / 2)))


def crowd_grid(sub, t, start, top, acc, n=24, cols=6, size=120, gap=18):
    """A crowded wall of near-identical generic calendar tiles."""
    tot = cols * size + (cols - 1) * gap
    for i in range(n):
        kk = p(t, start + i * 0.04, 0.3)
        if kk <= 0: continue
        r, cc = divmod(i, cols)
        x = W / 2 - tot / 2 + cc * (size + gap)
        y = top + r * (size + gap)
        c, d = gbase(size, size, fill=(255, 255, 255), radius=18)
        d.rectangle([12, 12, size - 12, 40], fill=(*(200, 204, 214), 255))
        for gy in range(3):
            for gx in range(4):
                d.rectangle([14 + gx * 24, 50 + gy * 20, 30 + gx * 24, 62 + gy * 20], fill=(225, 228, 236, 255))
        d.text((size / 2, 26), "2027", font=font(F_XB, 20), fill=(*INK, 255), anchor="mm")
        c = with_alpha(c, out_cubic(kk))
        sub.alpha_composite(c, (int(x), int(y + 20 * (1 - out_cubic(kk)))))


def listing_form(sub, t, start, top, acc, rows, every=0.7, w=880, row_h=118, title="New listing"):
    """Etsy-style listing form; rows: (label, value, emoji). Each row ticks in."""
    k = p(t, start, 0.4)
    if k <= 0: return
    h = 110 + len(rows) * row_h + 30
    c, d = gbase(w, h, fill=(255, 255, 255))
    d.text((45, 58), "Etsy", font=font(F_BLACK, 44), fill=(*ETSY, 255), anchor="lm")
    d.text((170, 58), "· " + title, font=font(F_XB, 36), fill=(*INK, 255), anchor="lm")
    for i, (lab, val, ic) in enumerate(rows):
        kk = p(t, start + 0.4 + i * every, 0.35)
        y = 110 + i * row_h
        d.line([40, y, w - 40, y], fill=(230, 232, 238, 255), width=2)
        d.text((45, y + row_h / 2), lab, font=font(F_SEMI, 34), fill=(*GREY, 255), anchor="lm")
        if kk > 0:
            al = int(255 * out_cubic(kk))
            d.text((w - 120, y + row_h / 2), val, font=font(F_XB, 38), fill=(*INK, al), anchor="rm")
            e = with_alpha(emoji_img(ic, int(56 * max(0.1, out_back(kk)))), out_cubic(kk))
            c.alpha_composite(e, (int(w - 70 - e.width / 2), int(y + row_h / 2 - e.height / 2)))
    with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(top + 60 * (1 - out_cubic(k)))))
    return h


def dollar_counter(sub, t, start, value, cy, color, label, dur=1.8, size=210):
    """Counts up to a value with cents, then pulses."""
    k = p(t, start, dur)
    if t < start: return
    v = value * out_cubic(k)
    pulse = 1 + 0.05 * math.sin(max(0, t - (start + dur)) * 8) * (t > start + dur)
    draw_text(sub, f"${v:,.2f}", F_BLACK, size, W / 2, cy, color, alpha=out_cubic(p(t, start, 0.3)), scale=pulse)
    draw_text(sub, label, F_XB, 52, W / 2, cy + size * 0.72, WHITE, alpha=out_cubic(p(t, start + 0.2, 0.3)))
