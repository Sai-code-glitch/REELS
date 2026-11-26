"""Helpers for the 2026-11-26 'Black Friday email swipe file' reels.
Gmail-style label picker, swipe-file table (Google Docs style), single email open view,
copy-vs-rewrite comparison. All brands, shops, emails and prices shown are generic samples."""
from reel_reddit import *
from reel_email import inbox, email_card, build_row

GRED = (217, 48, 37)
GBLUE = (26, 115, 232)
DOCBLUE = (66, 133, 244)


def gmail_bar(sub, t, start, cy, query, type_dur=0.9, w=880, h=120):
    """Gmail-style search pill with typing query."""
    k = p(t, start, 0.35)
    if k <= 0: return
    c, d = card_base(w, h, radius=h // 2, fill=(241, 243, 246, 255))
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=h // 2, outline=(*GBLUE, 255), width=4)
    e = emoji_img("🔍", 50)
    c.alpha_composite(e, (40, int(h / 2 - e.height / 2)))
    n = int(len(query) * clamp((t - start - 0.3) / type_dur))
    shown = query[:n] if n > 0 else ""
    if not shown:
        d.text((120, h / 2), "Search mail", font=font(F_SEMI, 46), fill=(*GREY, 255), anchor="lm")
    d.text((120, h / 2), shown, font=font(F_XB, 48), fill=(*INK, 255), anchor="lm")
    if (t * 2) % 1 < 0.6:
        x = 120 + d.textlength(shown, font=font(F_XB, 48)) + 6
        d.rectangle([x, h / 2 - 30, x + 5, h / 2 + 30], fill=(*GBLUE, 255))
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(cy - h / 2 + 40 * (1 - out_cubic(k)))))


def label_menu(sub, t, start, top, labels, new_label, new_at, check_at, w=760):
    """'Label as' dropdown: existing labels, then a new label typed in and ticked."""
    k = p(t, start, 0.4)
    if k <= 0: return
    row = 96
    h = 110 + row * (len(labels) + 1) + 30
    c, d = card_base(w, h, radius=30, fill=(255, 255, 255, 255))
    d.text((40, 60), "Label as:", font=font(F_XB, 38), fill=(*GREY, 255), anchor="lm")
    d.line([30, 105, w - 30, 105], fill=(*LINE, 255), width=3)
    y = 105 + row / 2
    for lab in labels:
        d.rounded_rectangle([40, y - 22, 84, y + 22], radius=8, outline=(*GREY, 255), width=4)
        d.text((110, y), lab, font=font(F_SEMI, 40), fill=(*INK, 255), anchor="lm")
        y += row
    kn = p(t, new_at, 0.35)
    if kn > 0:
        d.rounded_rectangle([20, y - row / 2 + 6, w - 20, y + row / 2 - 6], radius=18, fill=(232, 240, 254, int(255 * out_cubic(kn))))
        on = t >= check_at
        if on:
            d.rounded_rectangle([40, y - 22, 84, y + 22], radius=8, fill=(*GBLUE, 255))
            d.line([50, y, 60, y + 11, 76, y - 12], fill=(255, 255, 255, 255), width=6)
        else:
            d.rounded_rectangle([40, y - 22, 84, y + 22], radius=8, outline=(*GBLUE, 255), width=4)
        n = int(len(new_label) * clamp((t - new_at - 0.2) / 0.5))
        d.text((110, y), new_label[:n], font=font(F_BLACK, 42), fill=(*GBLUE, 255), anchor="lm")
        if on:
            d.text((w - 40, y), "applied", font=font(F_XB, 30), fill=(*OKG, 255), anchor="rm")
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(top + 50 * (1 - out_cubic(k)))))


def swipe_table(sub, t, start, top, rows, row_at, every=0.7, title="Swipe file", w=900,
                cols=("Subject", "Offer", "Deadline"), widths=(0.46, 0.27, 0.27), hl_col=None, hl_at=None):
    """Google-Docs-style table that fills row by row. rows = list of tuples (len == len(cols))."""
    k = p(t, start, 0.4)
    if k <= 0: return
    head = 150
    rh = 118
    h = head + 80 + rh * len(rows) + 30
    c, d = card_base(w, h, radius=34, fill=(255, 255, 255, 255))
    d.rounded_rectangle([0, 0, w - 1, 96], radius=34, fill=(*DOCBLUE, 255))
    d.rectangle([0, 60, w - 1, 96], fill=(*DOCBLUE, 255))
    d.text((40, 50), title, font=font(F_BLACK, 42), fill=(255, 255, 255, 255), anchor="lm")
    d.text((w - 40, 50), "Google Docs · free", font=font(F_SEMI, 28), fill=(225, 235, 255, 255), anchor="rm")
    x0, x1 = 30, w - 30
    xs = [x0]
    for fr in widths:
        xs.append(xs[-1] + (x1 - x0) * fr)
    y = head - 20
    for i, cname in enumerate(cols):
        fill = (255, 236, 160) if (hl_col == i and hl_at is not None and t >= hl_at) else (238, 242, 250)
        d.rectangle([xs[i], y, xs[i + 1], y + 80], fill=(*fill, 255), outline=(*LINE, 255), width=2)
        d.text((xs[i] + 18, y + 40), cname, font=font(F_BLACK, 34), fill=(*INK, 255), anchor="lm")
    y += 80
    for r, vals in enumerate(rows):
        d.rectangle([x0, y, x1, y + rh], outline=(*LINE, 255), width=2)
        for i in range(1, len(cols)):
            d.line([xs[i], y, xs[i], y + rh], fill=(*LINE, 255), width=2)
        at = row_at + r * every
        kr = clamp((t - at) / 0.5)
        if kr > 0:
            for i, v in enumerate(vals):
                lines = v.split("\n")
                for j, ln in enumerate(lines):
                    n = int(len(ln) * kr)
                    yy = y + rh / 2 + (j - (len(lines) - 1) / 2) * 40
                    col = INK
                    if hl_col == i and hl_at is not None and t >= hl_at:
                        col = (180, 90, 0)
                    d.text((xs[i] + 18, yy), ln[:n], font=font(F_XB, 32), fill=(*col, 255), anchor="lm")
        y += rh
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(top + 60 * (1 - out_cubic(k)))))


def email_open(sub, t, start, top, sender, subject, lines, marks=None, w=880, tag=None, tag_col=None, tag_at=None,
               x_off=0, sender_col=(255, 140, 90)):
    """Opened email view. marks = list of (line_index, label, color, at) highlight + side label."""
    k = p(t, start, 0.45)
    if k <= 0: return
    lh = 58
    h = 250 + lh * len(lines) + 40
    c, d = card_base(w, h, radius=36, fill=(255, 255, 255, 255))
    d.ellipse([36, 36, 116, 116], fill=(*sender_col, 255))
    d.text((76, 76), sender[0], font=font(F_BLACK, 42), fill=(255, 255, 255, 255), anchor="mm")
    d.text((140, 58), sender, font=font(F_XB, 36), fill=(*INK, 255), anchor="lm")
    d.text((140, 98), "to me · sample email", font=font(F_SEMI, 28), fill=(*GREY, 255), anchor="lm")
    d.text((40, 185), subject, font=font(F_BLACK, 46), fill=(*INK, 255), anchor="lm")
    d.line([40, 235, w - 40, 235], fill=(*LINE, 255), width=3)
    y = 235 + 30 + lh / 2
    mk = {m[0]: m for m in (marks or [])}
    for i, ln in enumerate(lines):
        col = (60, 66, 80)
        if i in mk:
            _, lab, mcol, at = mk[i]
            kk = p(t, at, 0.3)
            if kk > 0:
                tw = d.textlength(ln, font=font(F_SEMI, 38))
                d.rounded_rectangle([30, y - 27, 30 + (tw + 24) * out_cubic(kk), y + 27], radius=10,
                                    fill=(*[int(255 - (255 - v) * 0.22) for v in mcol], 255))
                col = INK
        d.text((42, y), ln, font=font(F_SEMI, 38), fill=(*col, 255), anchor="lm")
        y += lh
    if tag and tag_at is not None:
        kt = p(t, tag_at, 0.35)
        if kt > 0:
            f = font(F_BLACK, 30)
            tw = d.textlength(tag, font=f)
            d.rounded_rectangle([w - tw - 80, 40, w - 36, 96], radius=28, fill=(*tag_col, int(255 * out_cubic(kt))))
            d.text((w - 58 - tw / 2 - 0, 68), tag, font=f, fill=(255, 255, 255, int(255 * out_cubic(kt))), anchor="mm")
    c = with_alpha(c, out_cubic(k))
    x0, y0 = int(W / 2 - w / 2 + x_off), int(top + 60 * (1 - out_cubic(k)))
    sub.alpha_composite(c, (x0, y0))
    # side labels for marks (drawn on sub, right-aligned under highlight row)
    return y0, h


def mark_labels(sub, t, top, marks, lh=58, x=None):
    """Small colored pills to the right side of a card for marks (line_index, label, color, at)."""
    for (i, lab, col, at) in marks:
        kk = p(t, at + 0.15, 0.35)
        if kk <= 0: continue
        y = top + 235 + 30 + lh / 2 + i * lh
        pill(sub, (x or W - 240), y, lab, F_BLACK, 30, col, (255, 255, 255), alpha=out_cubic(kk), scale=out_back(kk), pad=(22, 10))
