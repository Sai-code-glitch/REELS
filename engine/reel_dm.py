"""Helpers for the 2026-11-27 'the 3-line DM that gets small shops to reply' reels.
Instagram-style DM thread, 3-line DM formula card, about-you vs about-them DM compare,
follow-up calendar strip. All shops, handles, messages and prices shown are generic samples."""
from reel_swipe import *
from reel_linkbio import lead_row
from reel_proof import stamp
from reel_portfolio import strike
from reel_chat import phone_chat, notification

OKGREEN = (40, 170, 100)
BADRED = (235, 64, 52)


def dm_formula(sub, t, start, top, rows, acc, every=1.1, w=900, row_h=210):
    """rows: (num, label, example_text). Each row: colored number dot, bold label, typed sample text."""
    for i, (num, lab, ex) in enumerate(rows):
        at = start + i * every
        kk = p(t, at, 0.4)
        if kk <= 0: continue
        a = out_cubic(kk)
        h = row_h - 22
        c, d = card_base(w, h, radius=36, fill=(255, 255, 255, 255))
        d.ellipse([28, 28, 118, 118], fill=(*acc, 255))
        d.text((73, 73), str(num), font=font(F_BLACK, 54), fill=(*INK, 255), anchor="mm")
        d.text((146, 70), lab, font=font(F_BLACK, 46), fill=(*INK, 255), anchor="lm")
        n = int(len(ex) * clamp((t - at - 0.35) / 0.8))
        d.text((146, 136), ex[:n], font=font(F_SEMI, 34), fill=(*GREY, 255), anchor="lm")
        c = with_alpha(c, a)
        sub.alpha_composite(c, (int(W / 2 - w / 2 + 70 * (1 - a)), int(top + i * row_h)))


def dm_card(sub, t, start, top, handle, lines, good, verdict_at, verdict, w=880, emoji="🕯️", color=(255, 214, 170)):
    """A single DM bubble inside a light card with a header; verdict pill slams in at verdict_at."""
    k = p(t, start, 0.4)
    if k <= 0: return
    lh = 54
    h = 170 + lh * len(lines) + 70
    c, d = card_base(w, h, radius=40, fill=(255, 255, 255, 255))
    d.ellipse([34, 30, 114, 110], fill=(*color, 255))
    e = emoji_img(emoji, 50)
    c.alpha_composite(e, (int(74 - e.width / 2), int(70 - e.height / 2)))
    d.text((136, 56), handle, font=font(F_XB, 38), fill=(*INK, 255), anchor="lm")
    d.text((136, 94), "Message request · sample", font=font(F_MED, 28), fill=(*GREY, 255), anchor="lm")
    f = font(F_SEMI, 38)
    bw = max(d.textlength(l, font=f) for l in lines) + 60
    x0, y0 = 40, 140
    d.rounded_rectangle([x0, y0, x0 + bw, y0 + lh * len(lines) + 40], radius=30, fill=(239, 240, 244, 255))
    for i, l in enumerate(lines):
        d.text((x0 + 30, y0 + 20 + lh / 2 + i * lh), l, font=f, fill=(*INK, 255), anchor="lm")
    kv = p(t, verdict_at, 0.35)
    if kv > 0:
        col = OKGREEN if good else BADRED
        fv = font(F_BLACK, 32)
        tw = d.textlength(verdict, font=fv)
        s = max(0.05, out_back(kv))
        bw2, bh2 = (tw + 50) * s, 62 * s
        x1, yc = w - 36, 70
        d.rounded_rectangle([x1 - bw2, yc - bh2 / 2, x1, yc + bh2 / 2], radius=bh2 / 2, fill=(*col, int(255 * out_cubic(kv))))
        d.text((x1 - bw2 / 2, yc), verdict, font=font(F_BLACK, 32 * s), fill=(255, 255, 255, int(255 * out_cubic(kv))), anchor="mm")
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(top + 60 * (1 - out_cubic(k)))))
    return h


def day_strip(sub, t, start, top, days, acc, every=0.6, w=880, h=210):
    """Row of day tiles: (day_label, emoji, caption, active). Active tiles get the accent color."""
    n = len(days)
    gap = 24
    tw = (w - gap * (n - 1)) / n
    x = W / 2 - w / 2
    for i, (lab, em, cap, act) in enumerate(days):
        kk = p(t, start + i * every, 0.4)
        if kk > 0:
            a = out_cubic(kk)
            c, d = card_base(int(tw), h, radius=30, fill=(*(acc if act else (255, 255, 255)), 255))
            d.text((tw / 2, 40), lab, font=font(F_BLACK, 36), fill=(*INK, 255), anchor="mm")
            e = emoji_img(em, 70)
            c.alpha_composite(e, (int(tw / 2 - e.width / 2), 70))
            d.text((tw / 2, 176), cap, font=font(F_XB, 28), fill=(*INK, 255), anchor="mm")
            c = with_alpha(c, a)
            sub.alpha_composite(c, (int(x), int(top + 50 * (1 - a))))
        x += tw + gap
