"""Helpers for the 2026-11-25 'find small freelance jobs in Reddit [Hiring] posts' reels.
Reddit-style search bar, community header, [Hiring] post rows, full post card, reply composer,
red-flag stamp. All usernames, posts and prices shown are generic samples."""
from reel_linkbio import *

ORANGE = (255, 69, 0)
BLUE = (0, 121, 211)
FLAIR_HIRE = (70, 190, 110)
FLAIR_FOR = (90, 130, 230)


def search_bar(sub, t, start, cy, query, acc, type_dur=1.0, w=880, h=120):
    """Search pill; query types in over type_dur."""
    k = p(t, start, 0.35)
    if k <= 0: return
    c, d = card_base(w, h, radius=h // 2, fill=(255, 255, 255, 255))
    e = emoji_img("🔍", 52)
    c.alpha_composite(e, (40, int(h / 2 - e.height / 2)))
    n = int(len(query) * clamp((t - start - 0.3) / type_dur))
    shown = query[:n]
    d.text((120, h / 2), shown, font=font(F_XB, 50), fill=(*INK, 255), anchor="lm")
    if (t * 2) % 1 < 0.6 and n < len(query) + 1:
        x = 120 + d.textlength(shown, font=font(F_XB, 50)) + 6
        d.rectangle([x, h / 2 - 30, x + 5, h / 2 + 30], fill=(*ORANGE, 255))
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(cy - h / 2 + 40 * (1 - out_cubic(k)))))


def flair(d, x, y, lab, col, size=30):
    f = font(F_BLACK, size)
    tw = d.textlength(lab, font=f)
    d.rounded_rectangle([x, y - size * 0.75, x + tw + 32, y + size * 0.75], radius=size * 0.75, fill=(*col, 255))
    d.text((x + 16, y), lab, font=f, fill=(255, 255, 255, 255), anchor="lm")
    return x + tw + 32


def community_header(sub, t, start, cy, acc, name="r/forhire", chips=("Hiring", "For Hire"), sel_at=None, sort_at=None, w=880, h=250):
    k = p(t, start, 0.4)
    if k <= 0: return
    c, d = card_base(w, h, radius=36, fill=(255, 255, 255, 255))
    d.ellipse([36, 30, 126, 120], fill=(*ORANGE, 255))
    d.text((81, 75), "r/", font=font(F_BLACK, 40), fill=(255, 255, 255, 255), anchor="mm")
    d.text((150, 60), name, font=font(F_BLACK, 46), fill=(*INK, 255), anchor="lm")
    d.text((150, 104), "community · sample view", font=font(F_SEMI, 28), fill=(*GREY, 255), anchor="lm")
    x = 40
    for i, ch in enumerate(chips):
        sel = sel_at is not None and i == 0 and t >= sel_at
        f = font(F_XB, 34)
        tw = d.textlength(ch, font=f)
        fill = FLAIR_HIRE if sel else (236, 238, 243)
        d.rounded_rectangle([x, 160, x + tw + 50, 220], radius=30, fill=(*fill, 255))
        d.text((x + 25, 190), ch, font=f, fill=(255, 255, 255, 255) if sel else (*INK, 255), anchor="lm")
        x += tw + 70
    srt = "Sort: New" if (sort_at is not None and t >= sort_at) else "Sort: Hot"
    col = ORANGE if (sort_at is not None and t >= sort_at) else GREY
    d.text((w - 40, 190), srt, font=font(F_XB, 34), fill=(*col, 255), anchor="rm")
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(cy - h / 2 + 40 * (1 - out_cubic(k)))))


def post_row(sub, t, start, cy, title, meta, tag="Hiring", flag=None, flag_at=None, w=880, h=170, tag_col=FLAIR_HIRE):
    """Feed row: [tag] flair + title + meta; optional verdict pill (label, color) at flag_at."""
    k = p(t, start, 0.4)
    if k <= 0: return
    c, d = card_base(w, h, radius=30, fill=(255, 255, 255, 255))
    flair(d, 34, 52, tag, tag_col, size=28)
    d.text((34 + 0, 112), title, font=font(F_XB, 38), fill=(*INK, 255), anchor="lm")
    d.text((w - 36, 52), meta, font=font(F_SEMI, 28), fill=(*GREY, 255), anchor="rm")
    if flag and flag_at is not None:
        kf = p(t, flag_at, 0.35)
        if kf > 0:
            lab, col = flag
            s = max(0.02, out_back(kf))
            bw, bh = 150 * s, 58 * s
            x1, yc = w - 36, 112
            d.rounded_rectangle([x1 - bw, yc - bh / 2, x1, yc + bh / 2], radius=bh / 2, fill=(*col, int(255 * out_cubic(kf))))
            d.text((x1 - bw / 2, yc), lab, font=font(F_BLACK, 28 * s), fill=(255, 255, 255, int(255 * out_cubic(kf))), anchor="mm")
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2 + 70 * (1 - out_cubic(k))), int(cy - h / 2)))


def post_card(sub, t, start, top, title_lines, body, user="u/pineandwick", age="2h ago", tag="Hiring",
              hi=None, hi_at=None, w=880, stamp=None, stamp_at=None):
    """Full post: header, flair, title, body lines. hi = index of body line to highlight red at hi_at.
    stamp = (label, color) drawn rotated over the card at stamp_at."""
    k = p(t, start, 0.45)
    if k <= 0: return
    lh = 56
    h = 170 + 70 * len(title_lines) + lh * len(body) + 50
    c, d = card_base(w, h, radius=40, fill=(255, 255, 255, 255))
    d.ellipse([36, 34, 96, 94], fill=(*ORANGE, 255))
    d.text((66, 64), "r/", font=font(F_BLACK, 28), fill=(255, 255, 255, 255), anchor="mm")
    d.text((116, 50), "r/forhire", font=font(F_XB, 32), fill=(*INK, 255), anchor="lm")
    d.text((116, 84), f"{user} · {age}", font=font(F_SEMI, 26), fill=(*GREY, 255), anchor="lm")
    flair(d, 40, 140, tag, FLAIR_HIRE, size=28)
    y = 210
    for tl in title_lines:
        d.text((40, y), tl, font=font(F_BLACK, 46), fill=(*INK, 255), anchor="lm")
        y += 70
    y += 10
    for i, bl in enumerate(body):
        col = INK
        if hi is not None and i == hi and hi_at is not None and t >= hi_at:
            kk = p(t, hi_at, 0.3)
            tw = d.textlength(bl, font=font(F_SEMI, 38))
            d.rounded_rectangle([30, y - 30, 30 + (tw + 20) * out_cubic(kk), y + 30], radius=12, fill=(255, 220, 215, 255))
            col = RED
        d.text((40, y), bl, font=font(F_SEMI, 38), fill=(*col, 255), anchor="lm")
        y += lh
    c = with_alpha(c, out_cubic(k))
    x0, y0 = int(W / 2 - w / 2), int(top + 70 * (1 - out_cubic(k)))
    sub.alpha_composite(c, (x0, y0))
    if stamp and stamp_at is not None:
        ks = p(t, stamp_at, 0.35)
        if ks > 0:
            lab, col = stamp
            f = font(F_BLACK, 110)
            tmp = Image.new("RGBA", (620, 200), (0, 0, 0, 0))
            td = ImageDraw.Draw(tmp)
            td.rounded_rectangle([8, 8, 612, 192], radius=30, outline=(*col, 255), width=14, fill=(255, 255, 255, 200))
            td.text((310, 100), lab, font=f, fill=(*col, 255), anchor="mm")
            s = 1.3 - 0.55 * out_cubic(ks)
            tmp = tmp.resize((int(620 * s), int(200 * s))).rotate(-12, resample=Image.BICUBIC, expand=True)
            tmp = with_alpha(tmp, out_cubic(ks))
            sub.alpha_composite(tmp, (int(W / 2 + 230 - tmp.width / 2), int(y0 + 95 - tmp.height / 2)))
    return y0 + h


def reply_box(sub, t, start, top, parts, acc, w=880, header="Reply to u/pineandwick", send_at=None):
    """Composer; parts = [(tag_label, text_lines, at)] each tag pill + its lines type in."""
    k = p(t, start, 0.45)
    if k <= 0: return
    lh = 50
    rows = sum(len(tl) for _, tl, _ in parts)
    h = 130 + rows * lh + len(parts) * 70 + 140
    c, d = card_base(w, h, radius=40, fill=(255, 255, 255, 255))
    d.text((40, 60), header, font=font(F_XB, 34), fill=(*GREY, 255), anchor="lm")
    d.line([40, 100, w - 40, 100], fill=(*LINE, 255), width=3)
    y = 150
    for i, (lab, lines, at) in enumerate(parts):
        kk = p(t, at, 0.35)
        if kk > 0:
            al = int(255 * out_cubic(kk))
            f = font(F_BLACK, 26)
            tw = d.textlength(lab, font=f)
            d.rounded_rectangle([40, y - 22, 40 + tw + 30, y + 22], radius=22, fill=(*acc, al))
            d.text((55, y), lab, font=f, fill=(*INK, al), anchor="lm")
            for j, l in enumerate(lines):
                frac = clamp((t - at - 0.2 - j * 0.35) / 0.5)
                n = int(len(l) * frac)
                d.text((40, y + 55 + j * lh), l[:n], font=font(F_SEMI, 36), fill=(*INK, 255), anchor="lm")
        y += 70 + len(lines) * lh
    if send_at is not None:
        ks = p(t, send_at, 0.3)
        sent = t >= send_at + 0.3
        fill = (*FLAIR_HIRE, 255) if sent else (*BLUE, int(255 * max(0.35, out_cubic(ks))))
        d.rounded_rectangle([w - 260, h - 110, w - 40, h - 36], radius=37, fill=fill)
        d.text((w - 150, h - 73), "Sent ✓" if sent else "Reply", font=font(F_BLACK, 34), fill=(255, 255, 255, 255), anchor="mm")
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(top + 70 * (1 - out_cubic(k)))))
