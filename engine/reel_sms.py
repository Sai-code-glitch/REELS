"""Text-message (SMS) mocks for the 2026-10-27 Black Friday text-pack reels."""
import textwrap
from reel_quote import *
from reel_maps import offer_card
from reel_email import build_row

SMS_GREY = (229, 229, 234)
SMS_BLUE = (0, 122, 255)
SMS_GREEN = (52, 199, 89)


def sms_thread(sub, t, start, cx, top, msgs, header="Rosa's Bakery", w=840, h=1000, avatar=(255, 150, 90)):
    """Phone with an SMS thread. msgs: (side 'them'|'me', text, appear_time, stamp_or_None)."""
    k = p(t, start, 0.4)
    if k <= 0: return
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=56, fill=(18, 20, 28, 255), outline=(70, 76, 96, 255), width=6)
    d.rounded_rectangle([18, 18, w - 19, h - 19], radius=44, fill=(255, 255, 255, 255))
    d.rectangle([18, 160, w - 19, 163], fill=(232, 233, 238, 255))
    d.ellipse([w / 2 - 40, 36, w / 2 + 40, 116], fill=(*avatar, 255))
    d.text((w / 2, 76), header[0], font=font(F_BLACK, 42), fill=(255, 255, 255, 255), anchor="mm")
    d.text((w / 2, 138), header + "  ·  Text Message", font=font(F_SEMI, 30), fill=(90, 96, 110, 255), anchor="mm")
    y = 200
    f = font(F_SEMI, 36)
    for side, txt, at, stamp in msgs:
        kk = p(t, at, 0.35)
        if kk <= 0: continue
        al = int(255 * out_cubic(kk))
        if stamp:
            d.text((w / 2, y + 10), stamp, font=font(F_XB, 26), fill=(130, 136, 150, al), anchor="mm")
            y += 44
        lines = textwrap.wrap(txt, 27)
        bw = max(d.textlength(l, font=f) for l in lines) + 56
        bh = len(lines) * 48 + 36
        if side == "me":
            x1 = w - 46; x0 = x1 - bw; fill = (*SMS_BLUE, al); fg = (255, 255, 255, al)
        else:
            x0 = 46; x1 = x0 + bw; fill = (*SMS_GREY, al); fg = (*INK, al)
        dy = int(30 * (1 - out_cubic(kk)))
        d.rounded_rectangle([x0, y + dy, x1, y + bh + dy], radius=30, fill=fill)
        for i, l in enumerate(lines):
            d.text((x0 + 28, y + dy + 42 + i * 48), l, font=f, fill=fg, anchor="lm")
        y += bh + 22
    card = with_alpha(card, out_cubic(k))
    sub.alpha_composite(card, (int(cx - w / 2), int(top + 60 * (1 - out_cubic(k)))))


def compose_box(sub, t, start, cy, text, type_dur, limit=160, w=880, good=SMS_GREEN, bad=(255, 69, 58), wrap_n=30, full=False):
    """Message composer that types `text` and shows a live N/160 counter (green under, red over)."""
    k = p(t, start, 0.35)
    if k <= 0: return
    n = len(text) if full else int(len(text) * p(t, start + 0.3, type_dur))
    shown = text[:n]
    lines = textwrap.wrap(text, wrap_n)
    lh = 50
    h = 70 + lh * len(lines) + 90
    card, d = card_base(w, h, radius=40, fill=(255, 255, 255, 255))
    # type the text line by line keeping final wrapping stable
    left = n
    for i, l in enumerate(lines):
        seg = l[:max(0, left)]
        d.text((40, 60 + i * lh), seg, font=font(F_SEMI, 38), fill=(*INK, 255), anchor="lm")
        left -= len(l) + 1
    over = n > limit
    col = bad if over else good
    d.line([30, h - 90, w - 30, h - 90], fill=(228, 231, 238, 255), width=3)
    d.text((40, h - 45), "Text message", font=font(F_SEMI, 30), fill=(*GREY, 255), anchor="lm")
    d.rounded_rectangle([w - 260, h - 75, w - 30, h - 15], radius=30, fill=(*col, 255))
    d.text((w - 145, h - 45), f"{n}/{limit}", font=font(F_BLACK, 36), fill=(255, 255, 255, 255), anchor="mm")
    card = with_alpha(card, out_cubic(k))
    sub.alpha_composite(card, (int(W / 2 - w / 2), int(cy - h / 2 + 50 * (1 - out_cubic(k)))))
    return h


def lock_screen(sub, t, start, top, acc, w=820, h=900, banners=()):
    """Phone lock screen with a time and banners dropping in: (app, title, body, color, icon, at)."""
    k = p(t, start, 0.4)
    if k <= 0: return
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=56, fill=(18, 20, 28, 255), outline=(70, 76, 96, 255), width=6)
    d.rounded_rectangle([18, 18, w - 19, h - 19], radius=44, fill=(36, 40, 70, 255))
    d.text((w / 2, 110), "FRI, NOV 27", font=font(F_XB, 30), fill=(220, 224, 240, 255), anchor="mm")
    d.text((w / 2, 200), "9:41", font=font(F_BLACK, 130), fill=(255, 255, 255, 255), anchor="mm")
    y = 320
    for app, title, body, color, icon, at in banners:
        kk = p(t, at, 0.4)
        if kk <= 0: continue
        bw, bh = w - 70, 170
        b, bd = card_base(bw, bh, radius=36, fill=(245, 246, 250, 240))
        bd.rounded_rectangle([26, 35, 126, 135], radius=24, fill=(*color, 255))
        ic = emoji_img(icon, 60)
        b.alpha_composite(ic, (76 - ic.width // 2, 85 - ic.height // 2))
        bd.text((150, 48), app.upper(), font=font(F_XB, 26), fill=(*GREY, 255), anchor="lm")
        bd.text((bw - 30, 48), "now", font=font(F_SEMI, 26), fill=(*GREY, 255), anchor="rm")
        bd.text((150, 92), title, font=font(F_BLACK, 36), fill=(*INK, 255), anchor="lm")
        bd.text((150, 134), body, font=font(F_SEMI, 30), fill=(80, 86, 100, 255), anchor="lm")
        b = with_alpha(b, out_cubic(kk))
        card.alpha_composite(b, (35, int(y - 80 * (1 - out_back(kk)))))
        y += bh + 20
    card = with_alpha(card, out_cubic(k))
    sub.alpha_composite(card, (int(W / 2 - w / 2), int(top + 60 * (1 - out_cubic(k)))))
