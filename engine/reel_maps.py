"""Helpers for the 2026-10-25 holiday-hours reels (Maps search, special-hours editor, offer card)."""
from reel_portfolio import *

GREY = (110, 116, 130)


def search_bar(sub, t, start, cy, query, w=880, type_dur=1.4):
    k = p(t, start, 0.35)
    if k <= 0: return
    c, d = card_base(w, 130, fill=(255, 255, 255))
    e = emoji_img("📍", 60)
    c.alpha_composite(e, (40, int(65 - e.height / 2)))
    s = query[:int(len(query) * p(t, start + 0.2, type_dur))]
    d.text((124, 65), s, font=font(F_XB, 48), fill=(*INK, 255), anchor="lm")
    if (t * 2) % 1 < 0.6 and p(t, start + 0.2, type_dur) < 1:
        x = 124 + d.textlength(s, font=font(F_XB, 48)) + 6
        d.rectangle([x, 38, x + 5, 92], fill=(0, 132, 255, 255))
    e2 = emoji_img("🔍", 54)
    c.alpha_composite(e2, (w - 90, int(65 - e2.height / 2)))
    with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(cy - 65 + 40 * (1 - out_cubic(k)))))


def listing(sub, t, start, cy, icon, name, kind, stars, status_ok, status_at, color, w=880, h=230):
    """A Maps result row. status_ok True -> 'Holiday hours set', False -> 'Holiday hours: not set'."""
    c, d = card_base(w, h)
    d.rounded_rectangle([26, 26, 178, 178], radius=30, fill=(*color, 255))
    e = emoji_img(icon, 92)
    c.alpha_composite(e, (int(102 - e.width / 2), int(102 - e.height / 2)))
    d.text((206, 58), name, font=font(F_XB, 44), fill=(*INK, 255), anchor="lm")
    d.text((206, 112), f"{stars} ★ · {kind}", font=font(F_SEMI, 34), fill=(*GREY, 255), anchor="lm")
    ks = out_cubic(p(t, status_at, 0.35))
    if ks > 0:
        if status_ok:
            lab, bgc, fg = "✓ Holiday hours set", (220, 247, 228), (20, 130, 60)
        else:
            lab, bgc, fg = "! Holiday hours: not set", (255, 228, 230), (200, 30, 50)
        f = font(F_XB, 32)
        tw = d.textlength(lab, font=f)
        al = int(255 * ks)
        d.rounded_rectangle([206, 152, 206 + tw + 40, 204], radius=26, fill=(*bgc, al))
        d.text((226, 178), lab, font=f, fill=(*fg, al), anchor="lm")
    paste_card(sub, c, t, start, W / 2 + 80 * (1 - out_cubic(p(t, start, 0.45))), cy, dy=0)


def hours_editor(sub, t, start, cy, rows, acc, title="Special hours", w=880, h=760):
    """Mock Google-profile-style special hours editor. rows: (date, day, value, appear_time)."""
    k = p(t, start, 0.45)
    if k <= 0: return
    c, d = card_base(w, h)
    d.text((50, 70), "EDIT PROFILE · HOURS", font=font(F_XB, 28), fill=(*GREY, 255), anchor="lm")
    d.text((50, 128), title, font=font(F_BLACK, 52), fill=(*INK, 255), anchor="lm")
    d.line([50, 182, w - 50, 182], fill=(220, 224, 232, 255), width=3)
    for i, (date, day, val, at) in enumerate(rows):
        kk = p(t, at, 0.4)
        if kk <= 0: continue
        al = int(255 * out_cubic(kk))
        y = 215 + i * 104
        x = 50 + int(60 * (1 - out_cubic(kk)))
        d.rounded_rectangle([x, y, x + 150, y + 76], radius=20, fill=(*acc, al))
        d.text((x + 75, y + 38), date, font=font(F_BLACK, 34), fill=(*INK, al), anchor="mm")
        d.text((x + 180, y + 38), day, font=font(F_XB, 38), fill=(*INK, al), anchor="lm")
        closed = val.lower() == "closed"
        col = (200, 30, 50) if closed else (20, 130, 60)
        d.text((w - 50, y + 38), val, font=font(F_XB, 38), fill=(*col, al), anchor="rm")
    with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(cy - h / 2 + 60 * (1 - out_cubic(k)))))


def offer_card(sub, t, start, cy, lines, total, acc, title="Holiday Google refresh", w=860, h=640):
    """Simple invoice-style offer card. lines: (label, price, appear_time)."""
    k = p(t, start, 0.45)
    if k <= 0: return
    c, d = card_base(w, h)
    d.text((50, 70), "OFFER · EXAMPLE PRICING", font=font(F_XB, 28), fill=(*GREY, 255), anchor="lm")
    d.text((50, 130), title, font=font(F_BLACK, 50), fill=(*INK, 255), anchor="lm")
    d.line([50, 186, w - 50, 186], fill=(220, 224, 232, 255), width=3)
    last = start
    for i, (lab, price, at) in enumerate(lines):
        kk = p(t, at, 0.4)
        last = max(last, at)
        if kk <= 0: continue
        al = int(255 * out_cubic(kk))
        y = 240 + i * 92
        d.text((50, y), "✓", font=font(DEJAVU, 40), fill=(20, 150, 70, al), anchor="lm")
        d.text((100, y), lab, font=font(F_SEMI, 38), fill=(*INK, al), anchor="lm")
        d.text((w - 50, y), price, font=font(F_XB, 38), fill=(*INK, al), anchor="rm")
    kt = p(t, last + 0.6, 0.45)
    if kt > 0:
        al = int(255 * out_cubic(kt))
        d.rounded_rectangle([30, h - 150, w - 30, h - 40], radius=30, fill=(*acc, al))
        d.text((70, h - 95), "Total", font=font(F_XB, 44), fill=(*INK, al), anchor="lm")
        d.text((w - 70, h - 95), total, font=font(F_BLACK, 56), fill=(*INK, al), anchor="rm")
    with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(cy - h / 2 + 60 * (1 - out_cubic(k)))))


def mini_calendar(sub, t, start, cy, acc, marks, w=820, h=640, month="November 2026", first_wd=6, days=30):
    """Month grid; first_wd = weekday index of day 1 with Mon=0 (Nov 1 2026 is a Sunday -> 6). marks: {day: (label, at)}"""
    k = p(t, start, 0.45)
    if k <= 0: return
    c, d = card_base(w, h)
    d.text((w / 2, 62), month, font=font(F_BLACK, 46), fill=(*INK, 255), anchor="mm")
    cw = (w - 60) / 7
    for i, lab in enumerate("MTWTFSS"):
        d.text((30 + cw * i + cw / 2, 130), lab, font=font(F_XB, 30), fill=(*GREY, 255), anchor="mm")
    for day in range(1, days + 1):
        idx = first_wd + day - 1
        r, col = idx // 7, idx % 7
        x = 30 + cw * col + cw / 2; y = 195 + r * 82
        if day in marks:
            lab, at = marks[day]
            kk = out_back(p(t, at, 0.4))
            if kk > 0:
                rr = 36 * kk
                d.ellipse([x - rr, y - rr, x + rr, y + rr], fill=(*acc, 255))
        d.text((x, y), str(day), font=font(F_XB, 34), fill=(*INK, 255), anchor="mm")
    with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(cy - h / 2 + 60 * (1 - out_cubic(k)))))
