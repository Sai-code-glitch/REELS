"""Helpers for the 2026-11-16 'sell printable Christmas gift tags on Etsy' reels
(single gift tag, 8-per-page US Letter tag sheet with cut lines, Canva-style tag editor,
mailed-vs-digital December timeline, 3-variant sheet fan)."""
from reel_calendar import *

THEMES = {
    "teacher": dict(emoji="🍎", title="Thanks, Teacher!", color=(214, 58, 58)),
    "neighbor": dict(emoji="🏡", title="Happy Holidays!", color=(30, 130, 80)),
    "coworker": dict(emoji="☕", title="Cheers, Coworker!", color=(150, 96, 60)),
    "plain": dict(emoji="🎁", title="Merry Christmas", color=(200, 60, 70)),
}
PAPER = (255, 253, 248)


def draw_tag(c, d, x, y, w, h, theme, a=(1, 1, 1, 1), plain_fill=(236, 236, 240)):
    """One gift tag. a = [shape, colour band, emoji, text]."""
    a = list(a) + [1.0] * (4 - len(a))
    col = theme["color"]
    r = int(min(w, h) * 0.12)
    if a[0] > 0:
        al = int(255 * a[0])
        d.rounded_rectangle([x, y, x + w, y + h], radius=r, fill=(255, 255, 255, al), outline=(*(200, 196, 188), al), width=max(1, int(w * 0.008)))
        hr = w * 0.045
        d.ellipse([x + w / 2 - hr, y + h * 0.09 - hr, x + w / 2 + hr, y + h * 0.09 + hr], outline=(*(170, 166, 160), al), width=max(1, int(w * 0.012)))
    band_y0, band_y1 = y + h * 0.19, y + h * 0.58
    if a[1] > 0:
        cc = tuple(int(plain_fill[i] + (col[i] - plain_fill[i]) * a[1]) for i in range(3))
        d.rectangle([x + w * 0.06, band_y0, x + w * 0.94, band_y1], fill=(*cc, 255))
    elif a[0] > 0:
        d.rectangle([x + w * 0.06, band_y0, x + w * 0.94, band_y1], fill=(*plain_fill, int(255 * a[0])))
    if a[2] > 0:
        e = with_alpha(emoji_img(theme["emoji"], max(4, int(h * 0.24))), a[2])
        c.alpha_composite(e, (int(x + w * 0.5 - e.width / 2), int(band_y0 + (band_y1 - band_y0) * 0.36 - e.height / 2)))
    if a[3] > 0:
        al = int(255 * a[3])
        tf = font(F_BLACK, max(6, w * 0.085))
        tc = (255, 255, 255) if a[1] > 0.5 else INK
        d.text((x + w / 2, band_y0 + (band_y1 - band_y0) * 0.8), theme["title"], font=tf, fill=(*tc, al), anchor="mm")
        lf = font(F_XB, max(6, w * 0.07))
        for i, lab in enumerate(["To:", "From:"]):
            yy = y + h * (0.70 + i * 0.15)
            d.text((x + w * 0.1, yy), lab, font=lf, fill=(*INK, al), anchor="lm")
            lx = x + w * 0.1 + d.textlength(lab, font=lf) + w * 0.03
            d.line([lx, yy + h * 0.035, x + w * 0.9, yy + h * 0.035], fill=(*(190, 186, 180), al), width=max(1, int(w * 0.008)))


def tag_sheet(c, d, x, y, w, a, theme, cols=2, rows=4):
    """US Letter page with 8 tags + dashed cut lines. a = [cut lines, band, emoji, text, footer]."""
    a = list(a) + [1.0] * (5 - len(a))
    h = int(w * 11 / 8.5)
    d.rectangle([x, y, x + w, y + h], fill=(*PAPER, 255))
    mx, my = w * 0.06, h * 0.05
    tw = (w - 2 * mx) / cols
    th = (h - 2 * my - h * 0.03) / rows
    for r in range(rows):
        for cc in range(cols):
            tx = x + mx + cc * tw + tw * 0.06
            ty = y + my + r * th + th * 0.06
            draw_tag(c, d, tx, ty, tw * 0.88, th * 0.88, theme, a=[1, a[1], a[2], a[3]])
    if a[0] > 0:
        al = int(255 * a[0])
        dash = max(4, int(w * 0.02))
        lw = max(1, int(w * 0.005))
        for cc in range(1, cols):
            xx = x + mx + cc * tw
            for yy in range(int(y + my), int(y + h - my - h * 0.03), dash * 2):
                d.line([xx, yy, xx, yy + dash], fill=(*GREY, al), width=lw)
        for r in range(1, rows):
            yy = y + my + r * th
            for xx in range(int(x + mx), int(x + w - mx), dash * 2):
                d.line([xx, yy, xx + dash, yy], fill=(*GREY, al), width=lw)
    if a[4] > 0:
        d.text((x + w / 2, y + h * 0.975), "8 tags · US Letter · cut on dashed lines", font=font(F_SEMI, w * 0.03), fill=(*GREY, int(255 * a[4])), anchor="mm")
    return h


def sheet_card(sub, t, start, cx, cy, theme, w=420, rot=0.0, steps=None, shadow=True):
    k = p(t, start, 0.45)
    if k <= 0: return
    h = int(w * 11 / 8.5)
    pad = 24
    c = Image.new("RGBA", (w + 2 * pad, h + 2 * pad), (0, 0, 0, 0))
    d = ImageDraw.Draw(c)
    if shadow:
        d.rectangle([pad + 10, pad + 14, pad + w + 10, pad + h + 14], fill=(0, 0, 0, 70))
    a = [out_cubic(p(t, s, 0.45)) for s in steps] if steps else [1] * 5
    tag_sheet(c, d, pad, pad, w, a, theme)
    s = 0.6 + 0.4 * out_back(k)
    c = c.resize((max(1, int(c.width * s)), max(1, int(c.height * s))), Image.LANCZOS)
    if rot: c = c.rotate(rot, resample=Image.BICUBIC, expand=True)
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(cx - c.width / 2), int(cy - c.height / 2)))


def big_tag(sub, t, start, cx, cy, theme, w=460, rot=0.0, swing=True):
    """One large gift tag on a string, swinging gently."""
    k = p(t, start, 0.45)
    if k <= 0: return
    h = int(w * 1.3)
    pad = 40
    c = Image.new("RGBA", (w + 2 * pad, h + 2 * pad), (0, 0, 0, 0))
    d = ImageDraw.Draw(c)
    d.rounded_rectangle([pad + 12, pad + 16, pad + w + 12, pad + h + 16], radius=int(w * 0.12), fill=(0, 0, 0, 70))
    draw_tag(c, d, pad, pad, w, h, theme)
    s = 0.6 + 0.4 * out_back(k)
    c = c.resize((max(1, int(c.width * s)), max(1, int(c.height * s))), Image.LANCZOS)
    ang = rot + (4 * math.sin(t * 2.2) if swing else 0)
    c = c.rotate(ang, resample=Image.BICUBIC, expand=True)
    c = with_alpha(c, out_cubic(k))
    # string
    top_y = cy - c.height / 2 + 40
    d2 = ImageDraw.Draw(sub)
    d2.line([cx, top_y - 140, cx, top_y + 60], fill=(230, 210, 160, int(255 * out_cubic(k))), width=5)
    sub.alpha_composite(c, (int(cx - c.width / 2), int(cy - c.height / 2)))


def canva_tags(sub, t, start, cy, steps, theme, w=880, h=1100, labels=None):
    """Canva-style editor building a tag sheet over steps[0..4]."""
    k = p(t, start, 0.45)
    if k <= 0: return
    c, d = card_base(w, h, radius=36, fill=(236, 239, 245, 255))
    d.rounded_rectangle([0, 0, w - 1, 100], radius=36, fill=(*CANVA, 255))
    d.rectangle([0, 60, w - 1, 100], fill=(*CANVA, 255))
    d.text((40, 52), "Gift tags · US Letter", font=font(F_XB, 32), fill=(255, 255, 255, 255), anchor="lm")
    d.rounded_rectangle([w - 210, 24, w - 34, 80], radius=28, fill=(255, 255, 255, 255))
    d.text((w - 122, 52), "Share", font=font(F_XB, 30), fill=(*CANVA, 255), anchor="mm")
    tools = [("📐", "Grid"), ("🎨", "Color"), ("⭐", "Elements"), ("🔤", "Text")]
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
    tag_sheet(c, d, x, y, pw, a, theme)
    if labels and n > 0:
        kk = out_cubic(p(t, steps[n - 1], 0.3))
        d.rounded_rectangle([140, h - 120, w - 40, h - 26], radius=30, fill=(255, 255, 255, 255))
        d.text(((140 + w - 40) / 2, h - 73), labels[n - 1], font=font(F_XB, 38), fill=(*INK, int(255 * kk)), anchor="mm")
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(cy - h / 2 + 60 * (1 - out_cubic(k)))))


def dec_timeline(sub, t, start, cy, acc, w=880):
    """December strip: Dec 1 → Dec 25, mailed-gift cutoff (Dec 17) vs printable (Dec 24)."""
    k = p(t, start, 0.4)
    if k <= 0: return
    h = 470
    c, d = gbase(w, h, fill=(255, 255, 255))
    d.text((45, 60), "December", font=font(F_BLACK, 46), fill=(*INK, 255), anchor="lm")
    x0, x1 = 70, w - 70
    ly = 200
    kl = in_out(p(t, start + 0.3, 0.9))
    d.line([x0, ly, x0 + (x1 - x0) * kl, ly], fill=(210, 214, 222, 255), width=12)

    def dx(day): return x0 + (x1 - x0) * (day - 1) / 24
    for day in (1, 8, 15, 22):
        if kl * 24 + 1 >= day:
            d.text((dx(day), ly + 45), f"{day}", font=font(F_SEMI, 30), fill=(*GREY, 255), anchor="mm")
    marks = [(17, RED2, "Mailed gifts", "~Dec 17", start + 1.3, 300), (24, OKG, "Printables", "Dec 24", start + 2.3, 400)]
    for day, col, lab, when, st, yy in marks:
        km = p(t, st, 0.35)
        if km <= 0: continue
        al = int(255 * out_cubic(km))
        xx = dx(day)
        rr = 22 * out_back(km)
        d.ellipse([xx - rr, ly - rr, xx + rr, ly + rr], fill=(*col, al))
        d.line([xx, ly + 25, xx, yy - 30], fill=(*col, al), width=4)
        f = font(F_XB, 36)
        txt = f"{lab}: {when}"
        tw = d.textlength(txt, font=f)
        bx = min(max(xx - tw / 2 - 24 - (90 if day == 17 else 0), 20), w - tw - 68)
        d.rounded_rectangle([bx, yy - 30, bx + tw + 48, yy + 30], radius=30, fill=(*col, al))
        d.text((bx + 24 + tw / 2, yy), txt, font=f, fill=(255, 255, 255, al), anchor="mm")
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(cy - h / 2 + 50 * (1 - out_cubic(k)))))
