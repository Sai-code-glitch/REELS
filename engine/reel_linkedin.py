"""LinkedIn mocks (search, filter chips, feed post, profile headline, composer) for 2026-10-28 reels."""
import textwrap
from reel_quote import *
from reel_maps import offer_card
from reel_email import build_row

LI_BLUE = (10, 102, 194)
LI_BG = (243, 242, 239)


def li_logo(d, x, y, s=56):
    d.rounded_rectangle([x, y, x + s, y + s], radius=int(s * 0.18), fill=(*LI_BLUE, 255))
    d.text((x + s / 2, y + s / 2 + 2), "in", font=font(F_BLACK, int(s * 0.62)), fill=(255, 255, 255, 255), anchor="mm")


def li_search(sub, t, start, cy, query, w=880, type_dur=1.2):
    k = p(t, start, 0.35)
    if k <= 0: return
    h = 120
    c, d = card_base(w, h, radius=60, fill=(255, 255, 255, 255))
    li_logo(d, 30, 32, 56)
    d.ellipse([112, 40, 148, 76], outline=(*GREY, 255), width=5)
    d.line([142, 70, 158, 86], fill=(*GREY, 255), width=6)
    n = int(len(query) * p(t, start + 0.2, type_dur))
    txt = query[:n]
    f = font(F_SEMI, 44)
    d.text((180, 60), txt, font=f, fill=(*INK, 255), anchor="lm")
    if n < len(query) or (t * 2) % 1 < 0.5:
        x = 180 + d.textlength(txt, font=f) + 4
        d.line([x, 34, x, 86], fill=(*LI_BLUE, 255), width=4)
    s = out_back(k)
    c = with_alpha(c.resize((max(1, int(w * s)), max(1, int(h * s)))), out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - c.width / 2), int(cy - c.height / 2)))


def li_chips(sub, t, start, cy, chips, every=0.45, size=40):
    d = ImageDraw.Draw(sub)
    f = font(F_XB, size)
    widths = [d.textlength(c, font=f) + 70 for c in chips]
    gap = 22
    x = W / 2 - (sum(widths) + gap * (len(chips) - 1)) / 2
    for i, (c, wd) in enumerate(zip(chips, widths)):
        at = start + i * every
        kk = p(t, at, 0.35)
        on = t > at + 0.35
        pill(sub, x + wd / 2, cy, c, F_XB, size, (1, 117, 79) if on else (235, 238, 244), WHITE if on else INK,
             alpha=out_cubic(kk), scale=out_back(kk), pad=(35, 18))
        x += wd + gap


def li_post(sub, t, start, cy, name, role, ago, body, avatar, w=880, comment_at=None, wrap_n=33, label=None):
    """Feed post card. body: text wrapped to lines that type in."""
    k = p(t, start, 0.45)
    if k <= 0: return
    lines = textwrap.wrap(body, wrap_n)
    h = 200 + 58 * len(lines) + 110
    c, d = card_base(w, h, radius=32, fill=(255, 255, 255, 255))
    d.ellipse([36, 34, 120, 118], fill=(*avatar, 255))
    d.text((78, 76), name[0], font=font(F_BLACK, 44), fill=(255, 255, 255, 255), anchor="mm")
    d.text((142, 58), name, font=font(F_XB, 38), fill=(*INK, 255), anchor="lm")
    d.text((142, 100), role, font=font(F_MED, 30), fill=(*GREY, 255), anchor="lm")
    d.text((142, 136), ago + " · 🌐".replace(" 🌐", ""), font=font(F_MED, 28), fill=(*GREY, 255), anchor="lm")
    for i, ln in enumerate(lines):
        kk = out_cubic(p(t, start + 0.4 + i * 0.25, 0.3))
        d.text((40, 200 + i * 58), ln, font=font(F_SEMI, 40), fill=(*INK, int(255 * kk)), anchor="lm")
    yb = h - 80
    d.line([40, yb - 30, w - 40, yb - 30], fill=(*LINE, 255), width=3)
    for j, lab in enumerate(["Like", "Comment", "Repost", "Send"]):
        x = 40 + j * ((w - 80) / 4)
        hot = lab == "Comment" and comment_at is not None and t > comment_at
        pulse = 1 + 0.08 * math.sin(max(0, t - comment_at) * 9) if hot else 1
        d.text((x + 8, yb + 12), lab, font=font(F_XB if hot else F_SEMI, int(32 * pulse)),
               fill=(*(LI_BLUE if hot else GREY), 255), anchor="lm")
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(cy - h / 2 + 70 * (1 - out_cubic(k)))))
    if label:
        kl = p(t, start + 0.8, 0.35)
        pill(sub, W / 2 + w / 2 - 150, cy - h / 2 - 10, label, F_XB, 32, (255, 214, 92), INK, alpha=out_cubic(kl), scale=out_back(kl), pad=(24, 12))
    return h


def li_profile(sub, t, start, top, name, old, new, swap_at, acc, w=880, type_dur=1.6, wrap_n=30):
    """Profile header: banner, avatar, name, headline. At swap_at the old headline is struck and new one types in."""
    k = p(t, start, 0.45)
    if k <= 0: return
    h = 640
    c, d = card_base(w, h, radius=36, fill=(255, 255, 255, 255))
    d.rounded_rectangle([0, 0, w - 1, 200], radius=36, fill=(*acc, 255))
    d.rectangle([0, 160, w - 1, 200], fill=(*acc, 255))
    d.ellipse([50, 110, 230, 290], fill=(255, 255, 255, 255))
    d.ellipse([60, 120, 220, 280], fill=(255, 170, 90, 255))
    d.text((140, 200), name[0], font=font(F_BLACK, 80), fill=(255, 255, 255, 255), anchor="mm")
    d.text((50, 340), name, font=font(F_BLACK, 50), fill=(*INK, 255), anchor="lm")
    ks = p(t, swap_at, 0.4)
    if ks < 1:
        lines = textwrap.wrap(old, wrap_n)
        al = int(255 * (1 - out_cubic(p(t, swap_at + 0.6, 0.3))))
        for i, ln in enumerate(lines):
            y = 410 + i * 56
            d.text((50, y), ln, font=font(F_SEMI, 42), fill=(70, 76, 90, al), anchor="lm")
            if ks > 0:
                lw = d.textlength(ln, font=font(F_SEMI, 42))
                d.line([50, y, 50 + lw * out_cubic(ks), y], fill=(230, 60, 70, al), width=6)
    if t > swap_at + 0.8:
        lines = textwrap.wrap(new, wrap_n)
        total = len(new)
        n = int(total * p(t, swap_at + 0.8, type_dur))
        left = n
        for i, ln in enumerate(lines):
            seg = ln[:max(0, left)]
            d.text((50, 410 + i * 56), seg, font=font(F_XB, 42), fill=(*INK, 255), anchor="lm")
            left -= len(ln) + 1
    d.rounded_rectangle([50, h - 110, 330, h - 40], radius=35, fill=(*LI_BLUE, 255))
    d.text((190, h - 75), "Open to work", font=font(F_XB, 32), fill=(255, 255, 255, 255), anchor="mm")
    d.rounded_rectangle([350, h - 110, 640, h - 40], radius=35, outline=(*LI_BLUE, 255), width=4)
    d.text((495, h - 75), "Services", font=font(F_XB, 32), fill=(*LI_BLUE, 255), anchor="mm")
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(top + 60 * (1 - out_cubic(k)))))
    return h


def li_comment(sub, t, start, cy, name, headline, text, acc, w=880, glow_at=None):
    """A comment row showing that your headline appears under your name."""
    k = p(t, start, 0.4)
    if k <= 0: return
    lines = textwrap.wrap(text, 34)
    h = 190 + 54 * len(lines)
    c, d = card_base(w, h, radius=30, fill=(248, 249, 252, 255))
    d.ellipse([30, 30, 100, 100], fill=(255, 170, 90, 255))
    d.text((65, 65), name[0], font=font(F_BLACK, 38), fill=(255, 255, 255, 255), anchor="mm")
    d.text((122, 52), name + "  · You", font=font(F_XB, 36), fill=(*INK, 255), anchor="lm")
    if glow_at is not None and t > glow_at:
        kg = out_cubic(p(t, glow_at, 0.3))
        tw = d.textlength(headline, font=font(F_SEMI, 30))
        d.rounded_rectangle([112, 76, 112 + tw + 22, 122], radius=12, fill=(*acc, int(255 * kg)))
    d.text((122, 99), headline, font=font(F_SEMI, 30), fill=(*INK, 255), anchor="lm")
    for i, ln in enumerate(lines):
        kk = out_cubic(p(t, start + 0.3 + i * 0.25, 0.3))
        d.text((40, 170 + i * 54), ln, font=font(F_SEMI, 38), fill=(*INK, int(255 * kk)), anchor="lm")
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(cy - h / 2 + 50 * (1 - out_cubic(k)))))


def li_composer(sub, t, start, top, lines, acc, w=880, every=0.9, type_each=0.8, post_at=None):
    """'Start a post' composer that types lines one after another, then a Post button pulses."""
    k = p(t, start, 0.4)
    if k <= 0: return
    wrapped = [textwrap.wrap(l, 31) for l in lines]
    nrows = sum(len(x) for x in wrapped) + len(lines) - 1
    h = 230 + 54 * nrows + 130
    c, d = card_base(w, h, radius=36, fill=(255, 255, 255, 255))
    d.ellipse([36, 34, 116, 114], fill=(255, 170, 90, 255))
    d.text((76, 74), "Y", font=font(F_BLACK, 42), fill=(255, 255, 255, 255), anchor="mm")
    d.text((136, 58), "You", font=font(F_XB, 38), fill=(*INK, 255), anchor="lm")
    d.text((136, 100), "Post to Anyone", font=font(F_SEMI, 30), fill=(*GREY, 255), anchor="lm")
    y = 180
    for i, wl in enumerate(wrapped):
        at = start + 0.4 + i * every
        full = " ".join(wl)
        n = int(len(full) * p(t, at, type_each))
        left = n
        for ln in wl:
            seg = ln[:max(0, left)]
            d.text((40, y), seg, font=font(F_SEMI, 40), fill=(*INK, 255), anchor="lm")
            left -= len(ln) + 1
            y += 54
        y += 54
    if post_at is not None:
        kp = p(t, post_at, 0.35)
        on = kp > 0
        pulse = 1 + 0.06 * math.sin(max(0, t - post_at) * 8) if on else 1
        bw, bh = int(200 * pulse), int(80 * pulse)
        bx, by = w - 50 - bw, h - 50 - bh
        d.rounded_rectangle([bx, by, bx + bw, by + bh], radius=bh // 2, fill=(*(LI_BLUE if on else (200, 204, 214)), 255))
        d.text((bx + bw / 2, by + bh / 2), "Post", font=font(F_BLACK, int(38 * pulse)), fill=(255, 255, 255, 255), anchor="mm")
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(top + 60 * (1 - out_cubic(k)))))
    return h
