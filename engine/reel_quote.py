"""Quote / deposit / payment-link mocks for Learn & Earn reels (2026-10-26)."""
from reel_common import *

GREY = (110, 116, 130)
LINE = (228, 231, 238)


def card_base(w, h, radius=40, fill=(250, 251, 255, 255)):
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=radius, fill=fill)
    return card, d


def quote_card(sub, t, start, top, title, rows, total, deposit, acc, w=880, accept_at=None, deposit_at=None):
    """rows: list of (label, value, appear_time). Slides up from below."""
    k = p(t, start, 0.45)
    if k <= 0: return
    row_h = 92
    h = 190 + row_h * len(rows) + 120 + (100 if deposit else 0) + (130 if accept_at else 0)
    card, d = card_base(w, h)
    d.rounded_rectangle([0, 0, w - 1, 120], radius=40, fill=(*acc, 255))
    d.rectangle([0, 80, w - 1, 120], fill=(*acc, 255))
    d.text((44, 62), "QUOTE", font=font(F_BLACK, 50), fill=(*INK, 255), anchor="lm")
    d.text((w - 44, 62), "#001", font=font(F_XB, 38), fill=(*INK, 255), anchor="rm")
    d.text((44, 160), title, font=font(F_XB, 40), fill=(*INK, 255), anchor="lm")
    y = 200
    for lab, val, at in rows:
        kk = out_cubic(p(t, at, 0.35))
        if kk > 0:
            al = int(255 * kk)
            dx = int(60 * (1 - kk))
            d.text((44 + dx, y + row_h / 2), lab, font=font(F_SEMI, 38), fill=(70, 76, 90, al), anchor="lm")
            d.text((w - 44, y + row_h / 2), val, font=font(F_XB, 38), fill=(*INK, al), anchor="rm")
        d.line([44, y + row_h, w - 44, y + row_h], fill=(*LINE, 255), width=2)
        y += row_h
    kt = out_cubic(p(t, rows[-1][2] + 0.4, 0.35)) if rows else 1
    if kt > 0:
        d.text((44, y + 60), "Total", font=font(F_BLACK, 46), fill=(*INK, int(255 * kt)), anchor="lm")
        d.text((w - 44, y + 60), total, font=font(F_BLACK, 52), fill=(*INK, int(255 * kt)), anchor="rm")
    y += 120
    if deposit:
        kd = out_cubic(p(t, deposit_at if deposit_at else rows[-1][2] + 0.8, 0.35))
        if kd > 0:
            d.rounded_rectangle([30, y, w - 31, y + 84], radius=22, fill=(255, 241, 196, int(255 * kd)))
            d.text((54, y + 42), "Due before work starts", font=font(F_XB, 36), fill=(*INK, int(255 * kd)), anchor="lm")
            d.text((w - 54, y + 42), deposit, font=font(F_BLACK, 40), fill=(200, 110, 0, int(255 * kd)), anchor="rm")
        y += 100
    if accept_at:
        ka = out_cubic(p(t, accept_at, 0.35))
        if ka > 0:
            d.rounded_rectangle([44, y + 20, w - 45, y + 110], radius=45, fill=(40, 190, 120, int(255 * ka)))
            d.text((w / 2, y + 65), "Accept & pay deposit", font=font(F_BLACK, 40), fill=(255, 255, 255, int(255 * ka)), anchor="mm")
    card = with_alpha(card, out_cubic(k))
    sub.alpha_composite(card, (int(W / 2 - w / 2), int(top + 80 * (1 - out_cubic(k)))))


def notification(sub, t, start, cy, app, title, body, icon_color, icon="💳", w=880):
    """iOS-style banner dropping from the top."""
    k = p(t, start, 0.45)
    if k <= 0: return
    h = 190
    card, d = card_base(w, h, radius=44, fill=(245, 246, 250, 245))
    d.rounded_rectangle([34, 40, 134, 140], radius=26, fill=(*icon_color, 255))
    ic = emoji_img(icon, 64)
    card.alpha_composite(ic, (84 - ic.width // 2, 90 - ic.height // 2))
    d.text((160, 52), app.upper(), font=font(F_XB, 28), fill=(*GREY, 255), anchor="lm")
    d.text((w - 40, 52), "now", font=font(F_SEMI, 28), fill=(*GREY, 255), anchor="rm")
    d.text((160, 100), title, font=font(F_BLACK, 40), fill=(*INK, 255), anchor="lm")
    d.text((160, 148), body, font=font(F_SEMI, 34), fill=(80, 86, 100, 255), anchor="lm")
    card = with_alpha(card, out_cubic(k))
    sub.alpha_composite(card, (int(W / 2 - w / 2), int(cy - h / 2 - 160 * (1 - out_back(k)))))


def chat_bubble(sub, t, start, cy, text_lines, me=True, color=(70, 140, 255), w=760):
    k = p(t, start, 0.35)
    if k <= 0: return
    lh = 54
    h = 50 + lh * len(text_lines)
    card, d = card_base(w, h, radius=36, fill=(*color, 255) if me else (250, 251, 255, 255))
    fg = (255, 255, 255, 255) if me else (*INK, 255)
    for i, l in enumerate(text_lines):
        d.text((36, 25 + lh * i + lh / 2), l, font=font(F_SEMI, 38), fill=fg, anchor="lm")
    card = with_alpha(card, out_cubic(k))
    x = W - 110 - w if me else 110
    s = 0.85 + 0.15 * out_back(k)
    if s != 1:
        card = card.resize((max(1, int(w * s)), max(1, int(h * s))))
    sub.alpha_composite(card, (int(x + (w - card.width) / 2), int(cy - card.height / 2)))


def link_screen(sub, t, start, top, acc, steps_at, w=860):
    """Payment-link builder: name, amount, generated link."""
    k = p(t, start, 0.45)
    if k <= 0: return
    h = 760
    card, d = card_base(w, h)
    d.text((44, 70), "Create payment link", font=font(F_BLACK, 46), fill=(*INK, 255), anchor="lm")
    fields = [("Name", "Logo design - 50% deposit"), ("Amount", "$75.00")]
    for i, (lab, val) in enumerate(fields):
        kk = out_cubic(p(t, steps_at[i], 0.35))
        y = 140 + i * 170
        d.text((44, y + 20), lab, font=font(F_XB, 32), fill=(*GREY, 255), anchor="lm")
        d.rounded_rectangle([44, y + 50, w - 45, y + 140], radius=20, outline=(*(acc if kk > 0 else LINE), 255), width=4, fill=(255, 255, 255, 255))
        n = int(len(val) * kk)
        d.text((70, y + 95), val[:n], font=font(F_XB, 38), fill=(*INK, 255), anchor="lm")
    kb = out_cubic(p(t, steps_at[2], 0.35))
    d.rounded_rectangle([44, 500, w - 45, 590], radius=45, fill=(*acc, int(120 + 135 * kb)))
    d.text((w / 2, 545), "Create link", font=font(F_BLACK, 40), fill=(*INK, 255), anchor="mm")
    kl = out_cubic(p(t, steps_at[3], 0.35))
    if kl > 0:
        d.rounded_rectangle([44, 625, w - 45, 715], radius=20, fill=(230, 248, 238, int(255 * kl)))
        d.text((70, 670), "pay.link/your-name/deposit", font=font(F_XB, 36), fill=(20, 130, 80, int(255 * kl)), anchor="lm")
        d.text((w - 70, 670), "Copy", font=font(F_BLACK, 34), fill=(20, 130, 80, int(255 * kl)), anchor="rm")
    card = with_alpha(card, out_cubic(k))
    sub.alpha_composite(card, (int(W / 2 - w / 2), int(top + 80 * (1 - out_cubic(k)))))


def split_bar(sub, t, start, cy, left, right, lcol, rcol, w=860):
    """A bar that splits into two halves: deposit / on delivery."""
    k = out_cubic(p(t, start, 0.6))
    if k <= 0: return
    d = ImageDraw.Draw(sub)
    x0 = W / 2 - w / 2
    gap = 24 * k
    half = w / 2
    d.rounded_rectangle([x0 - gap / 2, cy - 60, x0 + half * k - gap / 2, cy + 60], radius=30, fill=(*lcol, 255))
    d.rounded_rectangle([x0 + half + gap / 2 + half * (1 - k), cy - 60, x0 + w + gap / 2, cy + 60], radius=30, fill=(*rcol, 255))
    kt = p(t, start + 0.5, 0.3)
    draw_text(sub, left[0], F_BLACK, 52, x0 + half / 2, cy - 6, INK, alpha=out_cubic(kt))
    draw_text(sub, right[0], F_BLACK, 52, x0 + half * 1.5 + gap, cy - 6, INK, alpha=out_cubic(kt))
    draw_text(sub, left[1], F_XB, 38, x0 + half / 2, cy + 110, WHITE, alpha=out_cubic(kt))
    draw_text(sub, right[1], F_XB, 38, x0 + half * 1.5 + gap, cy + 110, WHITE, alpha=out_cubic(kt))
