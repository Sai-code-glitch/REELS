"""Inbox / email mocks for Learn & Earn Black Friday email reels (2026-10-22)."""
import textwrap
from reel_chat import *


def inbox(sub, t, start, top, rows, title="Inbox", w=880, row_h=150, sel_color=(255, 214, 92)):
    """rows: list of (sender, subject, appear_time, style) ; style in None|'dim'|'hot'."""
    k = p(t, start, 0.4)
    if k <= 0: return
    h = 120 + row_h * len(rows) + 20
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=40, fill=(250, 251, 255, 255))
    d.text((44, 62), title, font=font(F_BLACK, 46), fill=(*INK, 255), anchor="lm")
    d.text((w - 44, 62), "Nov 27", font=font(F_MED, 32), fill=(120, 126, 140, 255), anchor="rm")
    for i, (sender, subj, at, style) in enumerate(rows):
        kk = p(t, at, 0.35)
        if kk <= 0: continue
        y = 120 + i * row_h
        al = int(255 * out_cubic(kk))
        dx = int(80 * (1 - out_cubic(kk)))
        if style == "hot":
            d.rounded_rectangle([16, y + 6, w - 17, y + row_h - 6], radius=24, fill=(255, 241, 196, al))
        dim = style == "dim"
        sc = (150, 154, 166, al) if dim else (*INK, al)
        d.ellipse([40 + dx, y + 35, 120 + dx, y + 115], fill=((200, 204, 214, al) if dim else (255, 140, 90, al)))
        d.text((80 + dx, y + 75), sender[0], font=font(F_BLACK, 40), fill=(255, 255, 255, al), anchor="mm")
        d.text((150 + dx, y + 52), sender, font=font(F_XB if not dim else F_SEMI, 36), fill=sc, anchor="lm")
        d.text((150 + dx, y + 100), subj, font=font(F_SEMI if dim else F_XB, 36), fill=sc, anchor="lm")
        if i < len(rows) - 1:
            d.line([150, y + row_h, w - 40, y + row_h], fill=(228, 231, 238, 255), width=2)
    card = with_alpha(card, out_cubic(k))
    sub.alpha_composite(card, (int(W / 2 - w / 2), int(top + 60 * (1 - out_cubic(k)))))


def email_card(sub, t, start, cx, cy, tag, date, subject, body, color, w=860, h=300):
    """A single email preview card that slides in from the right."""
    k = p(t, start, 0.45)
    if k <= 0: return
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=34, fill=(250, 251, 255, 255))
    d.rounded_rectangle([0, 0, 22, h - 1], radius=10, fill=(*color, 255))
    d.rounded_rectangle([50, 30, 50 + d.textlength(tag, font=font(F_XB, 32)) + 40, 84], radius=27, fill=(*color, 255))
    d.text((70, 57), tag, font=font(F_XB, 32), fill=(*INK, 255), anchor="lm")
    d.text((w - 40, 57), date, font=font(F_XB, 34), fill=(110, 116, 130, 255), anchor="rm")
    d.text((50, 140), subject, font=font(F_BLACK, 44), fill=(*INK, 255), anchor="lm")
    for i, l in enumerate(textwrap.wrap(body, 36)[:2]):
        d.text((50, 205 + i * 46), l, font=font(F_SEMI, 34), fill=(90, 96, 110, 255), anchor="lm")
    card = with_alpha(card, out_cubic(k))
    sub.alpha_composite(card, (int(cx - w / 2 + 300 * (1 - out_cubic(k))), int(cy - h / 2)))


def build_row(sub, t, start, cy, parts, colors, size=50, gap=0.6):
    """Formula pills that pop in one by one, centered as a row: parts joined by '+'."""
    d = ImageDraw.Draw(sub)
    f = font(F_XB, size)
    widths = [d.textlength(s, font=f) + 60 for s in parts]
    plus = 70
    total = sum(widths) + plus * (len(parts) - 1)
    x = W / 2 - total / 2
    for i, (s, wd) in enumerate(zip(parts, widths)):
        kk = p(t, start + i * gap, 0.4)
        pill(sub, x + wd / 2, cy, s, F_XB, size, colors[i % len(colors)], INK, alpha=out_cubic(kk), scale=out_back(kk), pad=(30, 18))
        if i < len(parts) - 1:
            draw_text(sub, "+", F_BLACK, 60, x + wd + plus / 2, cy, WHITE, alpha=out_cubic(p(t, start + i * gap + 0.3, 0.3)))
        x += wd + plus
