"""Helpers for the 2026-11-23 'thank-you card insert gig for online shops' reels.
4x6 thank-you card design, Canva-style postcard editor, shipping box with card popping out,
Instagram-style #packingorders result rows, print sheet. All shops/handles shown are generic samples."""
import random
from reel_proof import *
from reel_insta import ig_search, ring_avatar

KRAFT = (196, 148, 96)
KRAFT_D = (150, 106, 62)
PAPER = (255, 251, 244)
GREEN = (40, 170, 100)


def qr(d, x, y, s, col=INK, seed=5, a=255):
    """Fake QR-style pattern (decorative) of size s at (x,y)."""
    n = 17
    cell = s / n
    rnd = random.Random(seed)
    d.rectangle([x, y, x + s, y + s], fill=(255, 255, 255, a))
    for i in range(n):
        for j in range(n):
            corner = (i < 5 and j < 5) or (i < 5 and j > 11) or (i > 11 and j < 5)
            if corner: continue
            if rnd.random() < 0.45:
                d.rectangle([x + i * cell, y + j * cell, x + (i + 1) * cell, y + (j + 1) * cell], fill=(*col, a))
    for (ci, cj) in [(0, 0), (12, 0), (0, 12)]:
        x0, y0 = x + ci * cell, y + cj * cell
        d.rectangle([x0, y0, x0 + 5 * cell, y0 + 5 * cell], fill=(*col, a))
        d.rectangle([x0 + cell, y0 + cell, x0 + 4 * cell, y0 + 4 * cell], fill=(255, 255, 255, a))
        d.rectangle([x0 + 2 * cell, y0 + 2 * cell, x0 + 3 * cell, y0 + 3 * cell], fill=(*col, a))


def thank_card(c, d, x, y, w, a, acc, shop="Pine & Wick", emoji="🕯️", name="Sam",
               tip="Burn 2 hours the first time", handle="@pineandwick", code="THANKS10", holiday=False):
    """Landscape 6x4 card (w x 2w/3). a = 5 reveal amounts (bg, thanks, tip, handle+QR, code)."""
    h = w * 2 / 3
    bgc = tuple(int(255 + (v - 255) * a[0]) for v in PAPER)
    d.rectangle([x, y, x + w, y + h], fill=(*bgc, 255))
    if a[0] > 0:
        al = int(255 * a[0])
        d.rectangle([x, y, x + w * 0.06, y + h], fill=(*acc, al))
        if holiday:
            for i in range(9):
                rx = x + w * 0.12 + (i * 97) % int(w * 0.85); ry = y + h * 0.04 + (i * 31) % int(h * 0.12)
                d.text((rx, ry), "❄", font=font(DEJAVU, w * 0.03), fill=(*acc, int(al * 0.6)), anchor="mm")
        d.text((x + w * 0.94, y + h * 0.1), shop.upper(), font=font(F_XB, w * 0.032), fill=(*GREY, al), anchor="rm")
    if a[1] > 0:
        al = int(255 * a[1])
        d.text((x + w * 0.11, y + h * 0.27), "Thank you,", font=font(F_BLACK, w * 0.085), fill=(*INK, al), anchor="lm")
        d.text((x + w * 0.11, y + h * 0.42), f"{name}!", font=font(F_BLACK, w * 0.085), fill=(*acc, al), anchor="lm")
        e = with_alpha(emoji_img(emoji, int(w * 0.13)).copy(), a[1])
        c.alpha_composite(e, (int(x + w * 0.83 - e.width / 2), int(y + h * 0.33 - e.height / 2)))
    if a[2] > 0:
        al = int(255 * a[2])
        d.text((x + w * 0.11, y + h * 0.58), "Tip: " + tip, font=font(F_SEMI, w * 0.04), fill=(*INK, al), anchor="lm")
    if a[3] > 0:
        al = int(255 * a[3])
        s = w * 0.16
        qr(d, x + w * 0.11, y + h * 0.68, s, a=al, seed=len(shop))
        d.text((x + w * 0.11 + s + w * 0.03, y + h * 0.75), "Tag us", font=font(F_SEMI, w * 0.034), fill=(*GREY, al), anchor="lm")
        d.text((x + w * 0.11 + s + w * 0.03, y + h * 0.84), handle, font=font(F_XB, w * 0.04), fill=(*INK, al), anchor="lm")
    if a[4] > 0:
        al = int(255 * a[4])
        sc = 0.7 + 0.3 * out_back(min(1, a[4]))
        bw, bh = w * 0.3 * sc, h * 0.2 * sc
        cx, cy = x + w * 0.79, y + h * 0.79
        d.rounded_rectangle([cx - bw / 2, cy - bh / 2, cx + bw / 2, cy + bh / 2], radius=bh * 0.25, fill=(*acc, al))
        d.text((cx, cy - bh * 0.2), "10% off next order", font=font(F_SEMI, w * 0.022 * sc), fill=(*INK, al), anchor="mm")
        d.text((cx, cy + bh * 0.18), code, font=font(F_BLACK, w * 0.042 * sc), fill=(*INK, al), anchor="mm")


def card_img(w, acc, a, **kw):
    h = int(w * 2 / 3)
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    thank_card(im, ImageDraw.Draw(im), 0, 0, w, a, acc, **kw)
    m = Image.new("L", (w, h), 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, w - 1, h - 1], radius=max(6, w // 40), fill=255)
    im.putalpha(Image.composite(im.getchannel("A"), m, m))
    return im


def card_float(sub, t, start, cx, cy, acc, w=760, rot=0.0, steps=None, label=None, label_col=None, **kw):
    k = p(t, start, 0.45)
    if k <= 0: return
    a = [out_cubic(p(t, s, 0.45)) for s in steps] if steps else [1] * 5
    im = card_img(w, acc, a, **kw)
    pad = 30
    c = Image.new("RGBA", (w + 2 * pad, im.height + 2 * pad + (90 if label else 0)), (0, 0, 0, 0))
    d = ImageDraw.Draw(c)
    d.rounded_rectangle([pad + 8, pad + 14, pad + w + 8, pad + im.height + 14], radius=20, fill=(0, 0, 0, 90))
    c.alpha_composite(im, (pad, pad))
    if label:
        f = font(F_BLACK, 44)
        tw = d.textlength(label, font=f)
        ly = pad + im.height + 50
        d.rounded_rectangle([c.width / 2 - tw / 2 - 30, ly - 36, c.width / 2 + tw / 2 + 30, ly + 36], radius=36, fill=(*(label_col or acc), 255))
        d.text((c.width / 2, ly), label, font=f, fill=(*INK, 255), anchor="mm")
    s = 0.85 + 0.15 * out_back(k)
    c = c.resize((int(c.width * s), int(c.height * s)), Image.LANCZOS)
    if rot:
        c = c.rotate(rot, resample=Image.BICUBIC, expand=True)
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(cx - c.width / 2), int(cy - c.height / 2 + 60 * (1 - out_cubic(k)))))


def canva_card(sub, t, start, cy, acc, steps, w=880, h=880, labels=None, **kw):
    """Canva-style editor whose 6x4 canvas builds the card over steps[0..4]."""
    k = p(t, start, 0.45)
    if k <= 0: return
    c, d = card_base(w, h, radius=36, fill=(236, 239, 245, 255))
    d.rounded_rectangle([0, 0, w - 1, 100], radius=36, fill=(110, 70, 230, 255))
    d.rectangle([0, 60, w - 1, 100], fill=(110, 70, 230, 255))
    d.text((40, 52), "Postcard · 6 x 4 in", font=font(F_XB, 32), fill=(255, 255, 255, 255), anchor="lm")
    d.rounded_rectangle([w - 210, 24, w - 34, 80], radius=28, fill=(255, 255, 255, 255))
    d.text((w - 122, 52), "Download", font=font(F_XB, 28), fill=(110, 70, 230, 255), anchor="mm")
    tools = [("🖼️", "Design"), ("🔤", "Text"), ("⭐", "Elements"), ("🔳", "QR code")]
    n = sum(1 for s in steps if t >= s)
    for i, (ic, lab) in enumerate(tools):
        y = 190 + i * 140
        if n > 0 and i == min(3, max(0, n - 2)):
            d.rounded_rectangle([14, y - 56, 126, y + 66], radius=20, fill=(220, 210, 255, 255))
        e = emoji_img(ic, 50)
        c.alpha_composite(e, (int(70 - e.width / 2), int(y - e.height / 2)))
        d.text((70, y + 46), lab, font=font(F_SEMI, 21), fill=(*INK, 255), anchor="mm")
    cw = 680
    x, y = 165, 150
    d.rectangle([x - 4, y - 4, x + cw + 4, y + cw * 2 / 3 + 4], fill=(210, 214, 222, 255))
    a = [out_cubic(p(t, st, 0.45)) for st in steps]
    thank_card(c, d, x, y, cw, a, acc, **kw)
    if labels and n > 0:
        kk = out_cubic(p(t, steps[n - 1], 0.3))
        d.rounded_rectangle([165, h - 190, 165 + 680, h - 60], radius=36, fill=(255, 255, 255, 255))
        d.text((165 + 340, h - 125), labels[n - 1], font=font(F_BLACK, 44), fill=(*INK, int(255 * kk)), anchor="mm")
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(cy - h / 2 + 60 * (1 - out_cubic(k)))))


def ship_box(sub, t, start, cx, cy, acc, open_at, pop_at, w=560, card_kw=None):
    """Kraft shipping box; flaps open at open_at; a thank-you card rises out at pop_at."""
    k = p(t, start, 0.4)
    if k <= 0: return
    al = out_cubic(k)
    hgt = int(w * 0.62)
    # card rising (drawn first so box front covers its lower part)
    kp = p(t, pop_at, 0.7)
    if kp > 0:
        cw = int(w * 0.82)
        im = card_img(cw, acc, [1] * 5, **(card_kw or {}))
        rise = out_back(kp, 1.3) * hgt * 0.95
        im = im.rotate(-6 * out_cubic(kp), resample=Image.BICUBIC, expand=True)
        sub.alpha_composite(with_alpha(im, al), (int(cx - im.width / 2), int(cy - rise - im.height * 0.35)))
    box = Image.new("RGBA", (w + 200, hgt + 260), (0, 0, 0, 0))
    d = ImageDraw.Draw(box)
    ox, oy = 100, 200
    ko = out_cubic(p(t, open_at, 0.5))
    # flaps (rotate open outward)
    fl = 150 * (1 - ko) + 30
    lift = 170 * ko
    d.polygon([(ox, oy), (ox + w / 2, oy), (ox + w / 2 - 40 * ko, oy - lift + 20 * (1 - ko)), (ox - 90 * ko, oy - lift * 0.8)], fill=(*KRAFT_D, 255))
    d.polygon([(ox + w, oy), (ox + w / 2, oy), (ox + w / 2 + 40 * ko, oy - lift + 20 * (1 - ko)), (ox + w + 90 * ko, oy - lift * 0.8)], fill=(*KRAFT_D, 255))
    if ko < 0.5:
        d.rectangle([ox, oy - 10, ox + w, oy + 10], fill=(*KRAFT_D, 255))
    # front
    d.rounded_rectangle([ox, oy, ox + w, oy + hgt], radius=14, fill=(*KRAFT, 255))
    d.rectangle([ox + w / 2 - 50, oy, ox + w / 2 + 50, oy + hgt * 0.35], fill=(220, 190, 140, 255))
    d.rounded_rectangle([ox + w * 0.58, oy + hgt * 0.55, ox + w * 0.92, oy + hgt * 0.85], radius=8, fill=(255, 255, 255, 255))
    d.text((ox + w * 0.75, oy + hgt * 0.65), "SHIP TO", font=font(F_XB, w * 0.035), fill=(*INK, 255), anchor="mm")
    d.line([ox + w * 0.63, oy + hgt * 0.75, ox + w * 0.87, oy + hgt * 0.75], fill=(*GREY, 255), width=4)
    box = with_alpha(box, al)
    sub.alpha_composite(box, (int(cx - ox - w / 2), int(cy - oy)))


def post_row(sub, t, start, cy, emoji, color, handle, caption, has_card, flag_at, w=880, h=190):
    """Instagram-style result row: packing-video thumb, handle, caption, NO CARD / HAS CARD flag."""
    k = p(t, start, 0.4)
    if k <= 0: return
    c, d = card_base(w, h, radius=34, fill=(255, 255, 255, 255))
    d.rounded_rectangle([24, 20, 24 + 120, h - 20], radius=18, fill=(*color, 255))
    e = emoji_img("📦", 70)
    c.alpha_composite(e, (84 - e.width // 2, h // 2 - e.height // 2))
    d.polygon([(118, 34), (134, 44), (118, 54)], fill=(255, 255, 255, 230))
    ring_avatar(c, d, 210, h // 2 - 36, 26, emoji, color, ring=False)
    d.text((250, h // 2 - 36), handle, font=font(F_XB, 38), fill=(*INK, 255), anchor="lm")
    d.text((180, h // 2 + 34), caption, font=font(F_SEMI, 32), fill=(*GREY, 255), anchor="lm")
    kf = p(t, flag_at, 0.35)
    if kf > 0:
        col = GREEN if has_card else RED
        lab = "HAS CARD" if has_card else "NO CARD"
        s = max(0.02, out_back(kf))
        bw, bh = 200 * s, 64 * s
        x1 = w - 30
        y0 = h / 2 - 36
        d.rounded_rectangle([x1 - bw, y0 - bh / 2, x1, y0 + bh / 2], radius=bh / 2, fill=(*col, int(255 * out_cubic(kf))))
        d.text((x1 - bw / 2, y0), lab, font=font(F_BLACK, 28 * s), fill=(255, 255, 255, int(255 * out_cubic(kf))), anchor="mm")
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2 + 70 * (1 - out_cubic(k))), int(cy - h / 2)))


def print_sheet(sub, t, start, cy, acc, cut_at, w=620, **kw):
    """Letter page holding 2 cards with a dashed cut line; scissors run along it at cut_at."""
    k = p(t, start, 0.45)
    if k <= 0: return
    h = int(w * 11 / 8.5)
    c = Image.new("RGBA", (w + 40, h + 40), (0, 0, 0, 0))
    d = ImageDraw.Draw(c)
    d.rectangle([28, 34, w + 28, h + 34], fill=(0, 0, 0, 80))
    d.rectangle([20, 20, w + 20, h + 20], fill=(255, 255, 255, 255))
    cw = int(w * 0.84)
    ch = int(cw * 2 / 3)
    gap = (h - 2 * ch) / 3
    for i in range(2):
        im = card_img(cw, acc, [1] * 5, **kw)
        c.alpha_composite(im, (20 + (w - cw) // 2, int(20 + gap + i * (ch + gap))))
    ly = 20 + h / 2
    for xx in range(30, w + 10, 28):
        d.line([xx, ly, xx + 14, ly], fill=(*GREY, 255), width=3)
    kc = p(t, cut_at, 1.4)
    if kc > 0:
        e = emoji_img("✂️", 60)
        c.alpha_composite(e, (int(20 + (w - 40) * in_out(kc)), int(ly - e.height / 2)))
    s = 0.85 + 0.15 * out_back(k)
    c = c.resize((int(c.width * s), int(c.height * s)), Image.LANCZOS)
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - c.width / 2), int(cy - c.height / 2 + 60 * (1 - out_cubic(k)))))


def tool_tile(sub, t, start, cx, cy, emoji, name, sub_lab, acc, cw=400, ch=420):
    k = p(t, start, 0.45)
    if k <= 0: return
    c, d = card_base(cw, ch, radius=40, fill=(255, 255, 255, 255))
    e = emoji_img(emoji, 130)
    c.alpha_composite(e, (cw // 2 - e.width // 2, 130 - e.height // 2))
    d.text((cw / 2, 270), name, font=font(F_BLACK, 48), fill=(*INK, 255), anchor="mm")
    d.text((cw / 2, 335), sub_lab, font=font(F_SEMI, 32), fill=(*GREY, 255), anchor="mm")
    d.rounded_rectangle([cw / 2 - 60, 380, cw / 2 + 60, 404], radius=12, fill=(*acc, 255))
    c = with_alpha(c, out_cubic(k))
    s = 0.8 + 0.2 * out_back(k)
    c = c.resize((int(cw * s), int(ch * s)))
    sub.alpha_composite(c, (int(cx - c.width / 2), int(cy - c.height / 2)))


def clock(sub, t, start, dur, cy, minutes, color):
    if t < start: return
    m = minutes * out_cubic(p(t, start, dur))
    a = out_cubic(p(t, start, 0.3))
    place_emoji(sub, "⏱️", W / 2 - 190, cy, 96, alpha=a)
    draw_text(sub, f"{int(m):02d}:00", F_BLACK, 100, W / 2 + 50, cy, color, alpha=a)
