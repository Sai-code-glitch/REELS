"""Helpers for the 2026-11-11 Etsy listing-title rewrite reels
(Etsy listing card with word highlights, word meter, title builder, tag chips, Etsy search + result rows)."""
from reel_shipby import *

ETSY = (241, 100, 30)
RED2 = (230, 60, 60)
OKG = (30, 160, 90)


def layout_words(d, words, f, maxw):
    """Greedy wrap of a word list by pixel width -> list of lines, each a list of (index, word, x)."""
    lines, cur, x = [], [], 0
    sp = d.textlength(" ", font=f)
    for i, wd in enumerate(words):
        ww = d.textlength(wd, font=f)
        if cur and x + ww > maxw:
            lines.append(cur); cur, x = [], 0
        cur.append((i, wd, x))
        x += ww + sp
    if cur: lines.append(cur)
    return lines


def etsy_listing(sub, t, start, top, title, price, shop, emoji, color, w=880, size=40, bad=None, bad_at=None,
                 strike_at=None, new_title=None, swap_at=None, photo_h=330, cx=None):
    """Etsy listing card. bad: set of word indexes painted red from bad_at. swap_at: crossfade to new_title."""
    k = p(t, start, 0.4)
    if k <= 0: return
    tmp = ImageDraw.Draw(Image.new("RGBA", (10, 10)))
    f = font(F_SEMI, size)
    lh = int(size * 1.32)
    words = title.split()
    lines = layout_words(tmp, words, f, w - 90)
    nlines = lines
    if new_title:
        nlines = layout_words(tmp, new_title.split(), font(F_XB, size + 4), w - 90)
    nl = max(len(lines), len(nlines) if new_title else 0)
    h = photo_h + 50 + nl * lh + 150
    c, d = gbase(w, h, fill=(255, 255, 255))
    d.rounded_rectangle([0, 0, w - 1, photo_h], radius=40, fill=(*color, 255))
    d.rectangle([0, photo_h - 40, w - 1, photo_h], fill=(*color, 255))
    e = emoji_img(emoji, int(photo_h * 0.55))
    c.alpha_composite(e, (int(w / 2 - e.width / 2), int(photo_h / 2 - e.height / 2)))
    d.rounded_rectangle([w - 120, 26, w - 30, 116], radius=45, fill=(255, 255, 255, 235))
    d.text((w - 75, 73), "♡", font=font(DEJAVU, 46), fill=(*INK, 255), anchor="mm")
    ks = out_cubic(p(t, swap_at, 0.45)) if swap_at is not None else 0
    y0 = photo_h + 40
    if ks < 1:
        al = int(255 * (1 - ks))
        hb = bad_at is not None and t >= bad_at
        for li, ln in enumerate(lines):
            for i, wd, x in ln:
                red = hb and bad and i in bad
                col = (*RED2, al) if red else (40, 44, 56, al)
                d.text((45 + x, y0 + li * lh + lh / 2), wd, font=f, fill=col, anchor="lm")
                if red:
                    ww = d.textlength(wd, font=f)
                    d.line([45 + x, y0 + li * lh + lh * 0.82, 45 + x + ww, y0 + li * lh + lh * 0.82], fill=(*RED2, al), width=4)
        if strike_at is not None:
            kk = in_out(p(t, strike_at, 0.5))
            if kk > 0:
                for li, ln in enumerate(lines):
                    lw = ln[-1][2] + d.textlength(ln[-1][1], font=f)
                    yy = y0 + li * lh + lh / 2
                    d.line([45, yy, 45 + lw * kk, yy], fill=(*RED2, al), width=6)
    if ks > 0 and new_title:
        al = int(255 * ks)
        f2 = font(F_XB, size + 4)
        for li, ln in enumerate(nlines):
            for i, wd, x in ln:
                d.text((45 + x, y0 + li * lh + lh / 2 + 12 * (1 - ks)), wd, font=f2, fill=(*INK, al), anchor="lm")
    yb = y0 + nl * lh + 30
    d.text((45, yb + 22), shop, font=font(F_SEMI, 32), fill=(*GREY, 255), anchor="lm")
    d.text((45, yb + 82), price, font=font(F_BLACK, 48), fill=(*INK, 255), anchor="lm")
    with_alpha(c, out_cubic(k))
    x = (cx if cx is not None else W / 2) - w / 2
    sub.alpha_composite(c, (int(x), int(top + 60 * (1 - out_cubic(k)))))
    return h


def word_meter(sub, t, start, cx, cy, count, limit=15, dur=1.0, label="words", w=560):
    """Counts up to `count`; red over the limit, green within it."""
    k = p(t, start, 0.35)
    if k <= 0: return
    n = int(round(count * out_cubic(p(t, start + 0.1, dur))))
    over = n > limit
    col = RED2 if over else OKG
    h = 150
    c, d = gbase(w, h, fill=(255, 255, 255))
    d.rounded_rectangle([20, 20, 250, h - 20], radius=40, fill=(*col, 255))
    d.text((135, h / 2), str(n), font=font(F_BLACK, 76), fill=(255, 255, 255, 255), anchor="mm")
    d.text((280, h / 2 - 24), label, font=font(F_XB, 40), fill=(*INK, 255), anchor="lm")
    d.text((280, h / 2 + 26), f"Etsy tip: under {limit}", font=font(F_SEMI, 30), fill=(*GREY, 255), anchor="lm")
    s = 0.8 + 0.2 * out_back(k)
    c = with_alpha(c.resize((int(w * s), int(h * s))), out_cubic(k))
    sub.alpha_composite(c, (int(cx - c.width / 2), int(cy - c.height / 2)))


def formula_rows(sub, t, start, top, rows, acc, every=0.7, w=880, row=125):
    """rows: (emoji, label, value). Each slides in with a numbered dot."""
    for i, (ic, lab, val) in enumerate(rows):
        kk = p(t, start + i * every, 0.4)
        if kk <= 0: continue
        a = out_cubic(kk)
        h = row - 18
        c, d = gbase(w, h, fill=(255, 255, 255), radius=34)
        d.rounded_rectangle([18, 16, 18 + h - 32, h - 16], radius=26, fill=(*acc, 255))
        e = emoji_img(ic, 54)
        c.alpha_composite(e, (int(18 + (h - 32) / 2 - e.width / 2), int(h / 2 - e.height / 2)))
        d.text((h + 20, h / 2), lab, font=font(F_SEMI, 36), fill=(*GREY, 255), anchor="lm")
        d.text((w - 40, h / 2), val, font=font(F_BLACK, 44), fill=(*INK, 255), anchor="rm")
        c = with_alpha(c, a)
        sub.alpha_composite(c, (int(W / 2 - w / 2 + 70 * (1 - a)), int(top + i * row)))


def title_box(sub, t, start, top, title, type_dur, acc, w=880, size=46, show_count=True, limit=15):
    """Etsy 'Title' field being typed, with live word count."""
    k = p(t, start, 0.35)
    if k <= 0: return
    tmp = ImageDraw.Draw(Image.new("RGBA", (10, 10)))
    f = font(F_XB, size)
    n = int(len(title) * p(t, start + 0.2, type_dur))
    txt = title[:n]
    full_lines = layout_words(tmp, title.split(), f, w - 90)
    lines = layout_words(tmp, txt.split(), f, w - 90) if txt else []
    lh = int(size * 1.3)
    h = 110 + len(full_lines) * lh + 110
    c, d = gbase(w, h, fill=(255, 255, 255))
    d.text((45, 55), "Title", font=font(F_XB, 34), fill=(*INK, 255), anchor="lm")
    d.text((140, 55), "· Listing editor", font=font(F_SEMI, 30), fill=(*GREY, 255), anchor="lm")
    d.rounded_rectangle([25, 95, w - 25, 95 + len(full_lines) * lh + 30], radius=20, outline=(*ETSY, 255), width=4)
    for li, ln in enumerate(lines):
        for i, wd, x in ln:
            d.text((50 + x, 110 + li * lh + lh / 2), wd, font=f, fill=(*INK, 255), anchor="lm")
    if lines and (n < len(title) or (t * 2) % 1 < 0.5):
        last = lines[-1][-1]
        cxr = 50 + last[2] + d.textlength(last[1], font=f) + 6
        yy = 110 + (len(lines) - 1) * lh
        d.line([cxr, yy + 8, cxr, yy + lh - 8], fill=(*ETSY, 255), width=4)
    if show_count:
        wc = len(txt.split())
        col = OKG if wc <= limit else RED2
        lab = f"{wc} words"
        ff = font(F_XB, 34)
        tw = d.textlength(lab, font=ff) + 44
        d.rounded_rectangle([w - 30 - tw, h - 85, w - 30, h - 31], radius=27, fill=(*col, 255))
        d.text((w - 30 - tw / 2, h - 58), lab, font=ff, fill=(255, 255, 255, 255), anchor="mm")
        d.text((45, h - 58), "Etsy tip: under 15 words", font=font(F_SEMI, 30), fill=(*GREY, 255), anchor="lm")
    with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(top + 50 * (1 - out_cubic(k)))))
    return h


def tag_chips(sub, t, start, top, tags, acc, every=0.35, size=40, maxw=880):
    d = ImageDraw.Draw(sub)
    f = font(F_XB, size)
    x0 = W / 2 - maxw / 2
    x, y = x0, top
    ch = size + 36
    for i, tg in enumerate(tags):
        tw = d.textlength(tg, font=f) + 60
        if x + tw > x0 + maxw:
            x, y = x0, y + ch + 20
        kk = p(t, start + i * every, 0.35)
        if kk > 0:
            a = out_cubic(kk)
            s = max(0.05, out_back(kk))
            cxm, cym = x + tw / 2, y + ch / 2 - 30 * (1 - a)
            bw, bh = tw * s, ch * s
            d.rounded_rectangle([cxm - bw / 2, cym - bh / 2, cxm + bw / 2, cym + bh / 2], radius=bh / 2, fill=(*acc, int(255 * a)))
            d.text((cxm, cym), tg, font=font(F_XB, size * s), fill=(*INK, int(255 * a)), anchor="mm")
        x += tw + 18


def etsy_search(sub, t, start, cy, query, w=880, type_dur=1.2):
    k = p(t, start, 0.35)
    if k <= 0: return
    h = 130
    c, d = gbase(w, h, fill=(255, 255, 255), radius=65)
    d.text((48, h / 2), "Etsy", font=font(F_BLACK, 50), fill=(*ETSY, 255), anchor="lm")
    d.line([180, 30, 180, h - 30], fill=(220, 224, 232, 255), width=3)
    n = int(len(query) * p(t, start + 0.2, type_dur))
    txt = query[:n]
    f = font(F_XB, 44)
    d.text((210, h / 2), txt, font=f, fill=(*INK, 255), anchor="lm")
    if n < len(query) or (t * 2) % 1 < 0.5:
        x = 210 + d.textlength(txt, font=f) + 4
        d.line([x, 38, x, h - 38], fill=(*ETSY, 255), width=4)
    d.ellipse([w - 110, 20, w - 20, h - 20], fill=(*ETSY, 255))
    d.ellipse([w - 82, 44, w - 54, 72], outline=(255, 255, 255, 255), width=5)
    d.line([w - 58, 70, w - 44, 84], fill=(255, 255, 255, 255), width=6)
    s = out_back(k)
    c = with_alpha(c.resize((max(1, int(w * s)), max(1, int(h * s)))), out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - c.width / 2), int(cy - c.height / 2)))


def result_row(sub, t, start, cy, emoji, color, snippet, words, flag_at, limit=15, w=880, h=214):
    k = p(t, start, 0.4)
    if k <= 0: return
    over = words > limit
    lead = over and t >= flag_at + 0.4
    c, d = gbase(w, h, fill=(255, 255, 255))
    if lead:
        d.rounded_rectangle([0, 0, w - 1, h - 1], radius=40, outline=(*GOLD_C, 255), width=8)
    d.rounded_rectangle([26, 26, h - 26, h - 26], radius=26, fill=(*color, 255))
    e = emoji_img(emoji, 80)
    c.alpha_composite(e, (int(h / 2 - e.width / 2), int(h / 2 - e.height / 2)))
    f = font(F_SEMI, 32)
    tmp = layout_words(d, snippet.split(), f, w - h - 60)
    for li, ln in enumerate(tmp[:2]):
        line = " ".join(wd for _, wd, _ in ln)
        if li == 1 and len(tmp) > 2: line += " …"
        d.text((h + 10, 56 + li * 44), line, font=f, fill=(60, 66, 80, 255), anchor="lm")
    kf = p(t, flag_at, 0.35)
    if kf > 0:
        lab = f"{words} words" + ("  · LEAD" if over else "  · OK")
        col = RED2 if over else OKG
        ff = font(F_XB, 32)
        tw = d.textlength(lab, font=ff) + 44
        al = int(255 * out_cubic(kf))
        d.rounded_rectangle([h + 10, h - 76, h + 10 + tw, h - 26], radius=25, fill=(*col, al))
        d.text((h + 10 + tw / 2, h - 51), lab, font=ff, fill=(255, 255, 255, al), anchor="mm")
    with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2 + 60 * (1 - out_cubic(k))), int(cy - h / 2)))
