"""Phone chat mock + calendar mock for Learn & Earn follow-up reels (2026-10-21)."""
import textwrap
from reel_common import *


def wrap(s, n):
    return textwrap.wrap(s, n)


def phone_chat(sub, t, start, cx, top, msgs, header="Maya's Bakery", w=820, h=1060):
    """msgs: list of (side 'me'|'them', text, appear_time, extra) ; extra may be 'typed' or a status string."""
    k = p(t, start, 0.4)
    if k <= 0: return
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=56, fill=(18, 20, 28, 255), outline=(70, 76, 96, 255), width=6)
    d.rounded_rectangle([18, 18, w - 19, h - 19], radius=44, fill=(242, 244, 248, 255))
    d.rounded_rectangle([18, 18, w - 19, 150], radius=44, fill=(255, 255, 255, 255))
    d.rectangle([18, 110, w - 19, 150], fill=(255, 255, 255, 255))
    d.ellipse([50, 50, 130, 130], fill=(255, 170, 90, 255))
    d.text((90, 90), header[0], font=font(F_BLACK, 44), fill=(255, 255, 255, 255), anchor="mm")
    d.text((154, 74), header, font=font(F_XB, 38), fill=(*INK, 255), anchor="lm")
    d.text((154, 116), "Business account", font=font(F_MED, 28), fill=(120, 126, 140, 255), anchor="lm")
    y = 190
    for side, txt, at, extra in msgs:
        kk = p(t, at, 0.35)
        if kk <= 0: continue
        s = txt
        if extra == "typed":
            s = txt[:int(len(txt) * p(t, at, 2.2))]
        lines = wrap(s, 26) or [""]
        full_lines = wrap(txt, 26)
        f = font(F_SEMI, 36)
        bw = max(d.textlength(l, font=f) for l in full_lines) + 56
        bh = len(full_lines) * 48 + 36
        al = int(255 * out_cubic(kk))
        if side == "me":
            x1 = w - 50; x0 = x1 - bw; fill = (0, 132, 255, al); fg = (255, 255, 255, al)
        else:
            x0 = 50; x1 = x0 + bw; fill = (255, 255, 255, al); fg = (*INK, al)
        dy = int(30 * (1 - out_cubic(kk)))
        d.rounded_rectangle([x0, y + dy, x1, y + bh + dy], radius=30, fill=fill)
        for i, l in enumerate(lines):
            d.text((x0 + 28, y + dy + 18 + 24 + i * 48), l, font=f, fill=fg, anchor="lm")
        y += bh + 14
        if extra and extra != "typed":
            d.text((x1 if side == "me" else x0, y + 6), extra, font=font(F_MED, 28), fill=(120, 126, 140, al), anchor="rt" if side == "me" else "lt")
            y += 48
        y += 18
    card = with_alpha(card, out_cubic(k))
    sub.alpha_composite(card, (int(cx - w / 2), int(top + 60 * (1 - out_cubic(k)))))


def notification(sub, t, start, cy, title, body, icon="💬", w=860):
    k = p(t, start, 0.45)
    if k <= 0: return
    card = Image.new("RGBA", (w, 190), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, w - 1, 189], radius=40, fill=(250, 250, 252, 240))
    card.alpha_composite(emoji_img(icon, 80), (36, 55))
    d.text((150, 62), title, font=font(F_XB, 38), fill=(*INK, 255), anchor="lm")
    d.text((w - 36, 62), "now", font=font(F_MED, 28), fill=(120, 126, 140, 255), anchor="rm")
    d.text((150, 124), body, font=font(F_SEMI, 36), fill=(60, 66, 80, 255), anchor="lm")
    card = with_alpha(card, out_cubic(k))
    sub.alpha_composite(card, (int(W / 2 - w / 2), int(cy - 95 - 140 * (1 - out_back(k)))))
