"""Helpers for the 2026-11-15 'first Fiverr gig' reels
(Fiverr search bar, gig result card, gig title field, gig image thumbnail, 3-package table)."""
from reel_calendar import *

FV = (29, 191, 115)      # Fiverr-style green
FV_DARK = (14, 120, 70)


def fv_logo(d, x, y, size=48, col=FV):
    d.text((x, y), "fiverr", font=font(F_BLACK, size), fill=(40, 44, 56, 255), anchor="lm")
    tw = d.textlength("fiverr", font=font(F_BLACK, size))
    r = size * 0.13
    d.ellipse([x + tw + 4, y + size * 0.18 - r, x + tw + 4 + 2 * r, y + size * 0.18 + r], fill=(*col, 255))
    return tw + 4 + 2 * r


def fiverr_search(sub, t, start, cy, query, w=880, type_dur=1.2):
    k = p(t, start, 0.35)
    if k <= 0: return
    h = 130
    c, d = gbase(w, h, fill=(255, 255, 255), radius=65)
    lw = fv_logo(d, 44, h / 2, 46)
    d.line([44 + lw + 22, 30, 44 + lw + 22, h - 30], fill=(220, 224, 232, 255), width=3)
    x0 = 44 + lw + 48
    n = int(len(query) * p(t, start + 0.2, type_dur))
    txt = query[:n]
    f = font(F_XB, 42)
    d.text((x0, h / 2), txt, font=f, fill=(*INK, 255), anchor="lm")
    if n < len(query) or (t * 2) % 1 < 0.5:
        x = x0 + d.textlength(txt, font=f) + 4
        d.line([x, 38, x, h - 38], fill=(*FV, 255), width=4)
    d.rounded_rectangle([w - 120, 20, w - 20, h - 20], radius=30, fill=(*FV, 255))
    d.ellipse([w - 86, 44, w - 58, 72], outline=(255, 255, 255, 255), width=5)
    d.line([w - 62, 70, w - 48, 84], fill=(255, 255, 255, 255), width=6)
    s = out_back(k)
    c = with_alpha(c.resize((max(1, int(w * s)), max(1, int(h * s)))), out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - c.width / 2), int(cy - c.height / 2)))


def thumb(w, h, acc, line1="HOLIDAY", line2="FLYERS", badge="2-day delivery", emoji="🎄", steps=None, t=0.0, sample=True):
    """Gig image (1280x769 ratio) built in up to 4 steps: bg, headline, sample flyer, badge."""
    a = [out_cubic(p(t, s, 0.45)) for s in steps] if steps else [1, 1, 1, 1]
    c = Image.new("RGBA", (int(w), int(h)), (0, 0, 0, 0))
    d = ImageDraw.Draw(c)
    base = tuple(int(240 + (v - 240) * a[0]) for v in (24, 34, 60))
    d.rectangle([0, 0, w, h], fill=(*base, 255))
    if a[0] > 0:
        for i in range(14):
            rx = (i * 137) % int(w); ry = (i * 61) % int(h)
            r = w * 0.008
            d.ellipse([rx - r, ry - r, rx + r, ry + r], fill=(255, 255, 255, int(120 * a[0])))
        d.rectangle([0, h * 0.86, w, h], fill=(*acc, int(255 * a[0])))
    if a[1] > 0:
        al = int(255 * a[1])
        d.text((w * 0.06, h * 0.26), line1, font=font(F_BLACK, h * 0.17), fill=(*acc, al), anchor="lm")
        d.text((w * 0.06, h * 0.45), line2, font=font(F_BLACK, h * 0.17), fill=(255, 255, 255, al), anchor="lm")
        d.text((w * 0.06, h * 0.62), "for small businesses", font=font(F_XB, h * 0.065), fill=(220, 226, 240, al), anchor="lm")
    if a[2] > 0 and sample:
        fw = int(w * 0.27)
        fl = Image.new("RGBA", (fw, int(fw * 1.3)), (0, 0, 0, 0))
        flyer(fl, ImageDraw.Draw(fl), 0, 0, fw, [1] * 5, acc, shop="Crumb & Co", emoji="🥧", offer="Pre-order pies", foot="Sat · Nov 28")
        fl = fl.rotate(-6, resample=Image.BICUBIC, expand=True)
        fl = with_alpha(fl, a[2])
        c.alpha_composite(fl, (int(w * 0.66), int(h * 0.06 + 40 * (1 - a[2]))))
    if a[3] > 0:
        al = int(255 * a[3])
        f = font(F_BLACK, h * 0.06)
        tw = d.textlength(badge, font=f) + h * 0.12
        d.rounded_rectangle([w * 0.06, h * 0.68, w * 0.06 + tw, h * 0.8], radius=h * 0.06, fill=(255, 255, 255, al))
        d.text((w * 0.06 + tw / 2, h * 0.74), badge, font=f, fill=(*INK, al), anchor="mm")
    return c


def gig_card(sub, t, start, cx, top, acc, title, price, seller="YourName", level="New seller", w=760, rot=0.0, **tk):
    """Fiverr-style gig result card: thumbnail, seller row, title, 'From $X'."""
    k = p(t, start, 0.45)
    if k <= 0: return
    th = int(w * 769 / 1280)
    h = th + 330
    pad = 26
    c = Image.new("RGBA", (w + 2 * pad, h + 2 * pad), (0, 0, 0, 0))
    d = ImageDraw.Draw(c)
    d.rounded_rectangle([pad + 6, pad + 14, pad + w + 6, pad + h + 14], radius=36, fill=(0, 0, 0, 80))
    d.rounded_rectangle([pad, pad, pad + w, pad + h], radius=36, fill=(255, 255, 255, 255))
    im = thumb(w, th, acc, **tk)
    m = Image.new("L", (w, th), 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, w - 1, th + 40], radius=36, fill=255)
    im.putalpha(Image.composite(im.getchannel("A"), m, m))
    c.alpha_composite(im, (pad, pad))
    y = pad + th + 30
    d.ellipse([pad + 30, y, pad + 90, y + 60], fill=(*acc, 255))
    d.text((pad + 60, y + 30), seller[0], font=font(F_BLACK, 34), fill=(*INK, 255), anchor="mm")
    d.text((pad + 108, y + 30), seller, font=font(F_XB, 34), fill=(*INK, 255), anchor="lm")
    d.text((pad + w - 30, y + 30), level, font=font(F_SEMI, 28), fill=(*GREY, 255), anchor="rm")
    f = font(F_SEMI, 36)
    lines = layout_words(d, title.split(), f, w - 70)
    for li, ln in enumerate(lines[:2]):
        d.text((pad + 34, y + 100 + li * 48), " ".join(wd for _, wd, _ in ln), font=f, fill=(50, 54, 66, 255), anchor="lm")
    d.line([pad + 30, pad + h - 80, pad + w - 30, pad + h - 80], fill=(232, 234, 240, 255), width=2)
    d.text((pad + w - 34, pad + h - 40), f"From {price}", font=font(F_BLACK, 40), fill=(*INK, 255), anchor="rm")
    d.text((pad + 34, pad + h - 40), "♡", font=font(DEJAVU, 40), fill=(*GREY, 255), anchor="lm")
    s = 0.85 + 0.15 * out_back(k)
    c = c.resize((int(c.width * s), int(c.height * s)), Image.LANCZOS)
    if rot: c = c.rotate(rot, resample=Image.BICUBIC, expand=True)
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(cx - c.width / 2), int(top + 60 * (1 - out_cubic(k)))))
    return h


def gig_row(sub, t, start, cy, emoji, color, title, price, note, note_at, w=880, h=190):
    """Compact search-result row: emoji thumbnail, gig title, price, and a note pill."""
    k = p(t, start, 0.4)
    if k <= 0: return
    c, d = gbase(w, h, fill=(255, 255, 255), radius=34)
    tw_ = int((h - 40) * 1.66)
    d.rounded_rectangle([20, 20, 20 + tw_, h - 20], radius=22, fill=(*color, 255))
    e = emoji_img(emoji, 84)
    c.alpha_composite(e, (int(20 + tw_ / 2 - e.width / 2), int(h / 2 - e.height / 2)))
    x0 = 20 + tw_ + 26
    f = font(F_SEMI, 32)
    lines = layout_words(d, title.split(), f, w - x0 - 30)
    for li, ln in enumerate(lines[:2]):
        d.text((x0, 50 + li * 42), " ".join(wd for _, wd, _ in ln), font=f, fill=(50, 54, 66, 255), anchor="lm")
    d.text((x0, h - 42), f"From {price}", font=font(F_BLACK, 36), fill=(*INK, 255), anchor="lm")
    kn = p(t, note_at, 0.35)
    if kn > 0:
        ff = font(F_XB, 30)
        tw = d.textlength(note, font=ff) + 40
        al = int(255 * out_cubic(kn))
        d.rounded_rectangle([w - 26 - tw, h - 70, w - 26, h - 16], radius=27, fill=(*FV, al))
        d.text((w - 26 - tw / 2, h - 43), note, font=ff, fill=(255, 255, 255, al), anchor="mm")
    with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2 + 60 * (1 - out_cubic(k))), int(cy - h / 2)))


def gig_title(sub, t, start, top, title, type_dur, w=880, size=46, limit=80, label="Gig title"):
    """Fiverr gig title field: fixed 'I will' prefix + typed rest + character count."""
    k = p(t, start, 0.35)
    if k <= 0: return
    tmp = ImageDraw.Draw(Image.new("RGBA", (10, 10)))
    f = font(F_XB, size)
    pre = "I will "
    n = int(len(title) * p(t, start + 0.3, type_dur))
    full = pre + title
    txt = pre + title[:n]
    full_lines = layout_words(tmp, full.split(), f, w - 100)
    lines = layout_words(tmp, txt.split(), f, w - 100)
    lh = int(size * 1.3)
    h = 110 + len(full_lines) * lh + 120
    c, d = gbase(w, h, fill=(255, 255, 255))
    fv_logo(d, 45, 56, 38)
    d.text((190, 56), "· " + label, font=font(F_XB, 34), fill=(*INK, 255), anchor="lm")
    d.rounded_rectangle([25, 95, w - 25, 95 + len(full_lines) * lh + 30], radius=20, outline=(*FV, 255), width=4)
    cnt = 0
    for li, ln in enumerate(lines):
        for i, wd, x in ln:
            col = FV_DARK if i < 2 else INK
            d.text((50 + x, 110 + li * lh + lh / 2), wd, font=f, fill=(*col, 255), anchor="lm")
    if n < len(title) or (t * 2) % 1 < 0.5:
        last = lines[-1][-1]
        cxr = 50 + last[2] + d.textlength(last[1], font=f) + 6
        yy = 110 + (len(lines) - 1) * lh
        d.line([cxr, yy + 8, cxr, yy + lh - 8], fill=(*FV, 255), width=4)
    lab = f"{len(txt.strip())} chars"
    ff = font(F_XB, 34)
    tw = d.textlength(lab, font=ff) + 44
    d.rounded_rectangle([w - 30 - tw, h - 88, w - 30, h - 34], radius=27, fill=(*OKG, 255))
    d.text((w - 30 - tw / 2, h - 61), lab, font=ff, fill=(255, 255, 255, 255), anchor="mm")
    d.text((45, h - 61), "Say what you deliver + who for", font=font(F_SEMI, 30), fill=(*GREY, 255), anchor="lm")
    with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(top + 50 * (1 - out_cubic(k)))))
    return h


def packages(sub, t, start, top, acc, cols, rows, every=0.5, w=900, row_h=104, head_h=190, star=1, star_at=None, compact=False):
    """3-package table. cols: [(name, price)], rows: [(label, [v1, v2, v3])]. Cells tick in row by row."""
    k = p(t, start, 0.4)
    if k <= 0: return
    lab_w = 0 if compact else 230
    cw = (w - lab_w - 40) / 3
    h = head_h + len(rows) * row_h + 30
    c, d = gbase(w, h, fill=(255, 255, 255))
    ks = p(t, star_at, 0.4) if star_at is not None else 0
    for j, (nm, pr) in enumerate(cols):
        x = 20 + lab_w + j * cw
        kc = p(t, start + 0.2 + j * 0.25, 0.35)
        if kc <= 0: continue
        al = int(255 * out_cubic(kc))
        hl = j == star and ks > 0
        if hl:
            d.rounded_rectangle([x + 6, 12, x + cw - 6, h - 12], radius=30, fill=tuple(int(255 - (255 - v) * 0.35 * out_cubic(ks)) for v in acc) + (255,), outline=(*FV, int(255 * out_cubic(ks))), width=6)
        d.text((x + cw / 2, 58), nm, font=font(F_XB, 34), fill=(*GREY, al), anchor="mm")
        d.text((x + cw / 2, 128), pr, font=font(F_BLACK, 64 * (1 + 0.08 * out_back(ks) * hl)), fill=(*INK, al), anchor="mm")
    for i, (lab, vals) in enumerate(rows):
        y = head_h + i * row_h
        d.line([30, y, w - 30, y], fill=(232, 234, 240, 255), width=2)
        if not compact:
            d.text((40, y + row_h / 2), lab, font=font(F_SEMI, 32), fill=(*GREY, 255), anchor="lm")
        for j, v in enumerate(vals):
            kk = p(t, start + 1.0 + i * every + j * 0.12, 0.3)
            if kk <= 0: continue
            al = int(255 * out_cubic(kk))
            x = 20 + lab_w + j * cw + cw / 2
            sz = 36 if len(v) < 9 else 30
            d.text((x, y + row_h / 2 + 10 * (1 - out_cubic(kk))), v, font=font(F_XB, sz), fill=(*INK, al), anchor="mm")
    with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(top + 60 * (1 - out_cubic(k)))))
    return h
