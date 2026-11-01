"""Helpers for the 2026-11-01 Thanksgiving pre-order form reels (Google Forms mock, order sheet, bakery post with DM comments)."""
from reel_giftcard import *

FORM_PURPLE = (103, 58, 183)
SHEET_GREEN = (15, 157, 88)
PIE = (214, 120, 40)

FIELDS = [
    ("Your name", "short", "Dana R."),
    ("Phone", "short", "(555) 014-2290"),
    ("Which pie?", "drop", "Pumpkin"),
    ("How many?", "drop", "2"),
    ("Pickup day", "radio", ["Tue Nov 24", "Wed Nov 25"]),
]


def gform(sub, t, start, top, title, steps=None, fill_at=None, w=860, sel=None, scale=1.0):
    """Google Forms-style card. steps: reveal time per field (len 5). fill_at: time answers type in."""
    k = p(t, start, 0.45)
    if k <= 0: return
    row = 150
    h = 300 + row * len(FIELDS) + 130
    c, d = gbase(w, h, fill=(255, 255, 255))
    d.rounded_rectangle([0, 0, w - 1, 40], radius=40, fill=(*FORM_PURPLE, 255))
    d.rectangle([0, 18, w - 1, 40], fill=(*FORM_PURPLE, 255))
    d.text((50, 110), title, font=font(F_BLACK, 52), fill=(*INK, 255), anchor="lm")
    d.text((50, 172), "Order by Nov 20 · pay at pickup", font=font(F_SEMI, 32), fill=(*GREY, 255), anchor="lm")
    d.line([50, 226, w - 50, 226], fill=(228, 231, 238, 255), width=3)
    y = 260
    for i, (lab, kind, ans) in enumerate(FIELDS):
        at = steps[i] if steps else start
        kk = out_cubic(p(t, at, 0.35))
        if kk > 0:
            al = int(255 * kk)
            dx = int(50 * (1 - kk))
            hi = sel is not None and sel == i
            if hi:
                d.rounded_rectangle([30, y - 14, w - 30, y + row - 20], radius=22, fill=(240, 234, 252, al))
                d.rectangle([30, y - 14, 40, y + row - 20], fill=(*FORM_PURPLE, al))
            d.text((60 + dx, y + 22), lab, font=font(F_XB, 36), fill=(*INK, al), anchor="lm")
            fa = out_cubic(p(t, fill_at + i * 0.35, 0.3)) if fill_at is not None else 0
            if kind == "radio":
                for j, opt in enumerate(ans):
                    ox = 60 + dx + j * 360
                    d.ellipse([ox, y + 64, ox + 40, y + 104], outline=(*GREY, al), width=4)
                    if fa > 0 and j == 1:
                        d.ellipse([ox + 9, y + 73, ox + 31, y + 95], fill=(*FORM_PURPLE, int(al * fa)))
                    d.text((ox + 58, y + 84), opt, font=font(F_SEMI, 34), fill=(70, 76, 90, al), anchor="lm")
            else:
                d.line([60 + dx, y + 110, w - 80, y + 110], fill=(200, 204, 214, al), width=3)
                if fa > 0:
                    d.text((60 + dx, y + 80), ans, font=font(F_SEMI, 36), fill=(*INK, int(al * fa)), anchor="lm")
                else:
                    ph = "Short answer" if kind == "short" else "Choose one"
                    d.text((60 + dx, y + 80), ph, font=font(F_SEMI, 32), fill=(170, 176, 190, al), anchor="lm")
        y += row
    kb = out_cubic(p(t, (steps[-1] if steps else start) + 0.5, 0.35))
    if kb > 0:
        d.rounded_rectangle([50, y + 20, 290, y + 100], radius=20, fill=(*FORM_PURPLE, int(255 * kb)))
        d.text((170, y + 60), "Submit", font=font(F_XB, 38), fill=(255, 255, 255, int(255 * kb)), anchor="mm")
    if scale != 1.0:
        c = c.resize((int(w * scale), int(h * scale)), Image.LANCZOS)
    with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - c.width / 2), int(top + 60 * (1 - out_cubic(k)))))


ORDERS = [
    ("Dana R.", "Pumpkin", "2", "Wed"),
    ("Luis M.", "Apple", "1", "Tue"),
    ("Kim P.", "Pecan", "1", "Wed"),
    ("Omar S.", "Pumpkin", "3", "Tue"),
    ("Jess T.", "Apple", "2", "Wed"),
]


def order_sheet(sub, t, start, top, every=0.45, w=880, rows=ORDERS, title="Pie orders (sample)"):
    """Spreadsheet of form responses; rows tick in one by one. Sample names, not real customers."""
    k = p(t, start, 0.4)
    if k <= 0: return
    rh = 96
    h = 130 + rh * (len(rows) + 1) + 30
    c, d = gbase(w, h, fill=(255, 255, 255))
    d.rounded_rectangle([0, 0, w - 1, 110], radius=40, fill=(*SHEET_GREEN, 255))
    d.rectangle([0, 70, w - 1, 110], fill=(*SHEET_GREEN, 255))
    d.text((44, 56), title, font=font(F_BLACK, 42), fill=(255, 255, 255, 255), anchor="lm")
    cols = [44, 330, 600, 740]
    heads = ["Name", "Pie", "Qty", "Pickup"]
    y = 130
    d.rectangle([20, y, w - 20, y + rh], fill=(236, 246, 240, 255))
    for x, hd in zip(cols, heads):
        d.text((x, y + rh / 2), hd, font=font(F_XB, 34), fill=(*INK, 255), anchor="lm")
    y += rh
    for i, r in enumerate(rows):
        kk = out_cubic(p(t, start + 0.5 + i * every, 0.3))
        if kk > 0:
            al = int(255 * kk)
            if 0 < p(t, start + 0.5 + i * every, 0.6) < 1:
                d.rectangle([20, y, w - 20, y + rh], fill=(255, 246, 210, al))
            for x, v in zip(cols, r):
                d.text((x + int(30 * (1 - kk)), y + rh / 2), v, font=font(F_SEMI, 34), fill=(*INK, al), anchor="lm")
        d.line([20, y + rh, w - 20, y + rh], fill=(228, 231, 238, 255), width=2)
        y += rh
    with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(top + 60 * (1 - out_cubic(k)))))


def bakery_post(sub, t, start, top, comments, hl_at=None, w=880, handle="@crumbandco"):
    """Instagram-style post: pie photo tile, caption with 'DM to order', comment rows (sample)."""
    k = p(t, start, 0.45)
    if k <= 0: return
    img_h = 420
    h = 130 + img_h + 150 + 110 * len(comments) + 30
    c, d = card_base(w, h, radius=36, fill=(255, 255, 255, 255))
    ring_avatar(c, d, 70, 66, 34, "🥧", (250, 214, 165))
    d.text((126, 66), handle, font=font(F_XB, 36), fill=(*INK, 255), anchor="lm")
    d.text((w - 40, 66), "•••", font=font(F_XB, 34), fill=(*INK, 255), anchor="rm")
    d.rectangle([0, 130, w - 1, 130 + img_h], fill=(252, 226, 196, 255))
    for i, ic in enumerate(["🥧", "🍂", "🥧"]):
        e = emoji_img(ic, 190 if i != 1 else 120)
        c.alpha_composite(e, (int(w * (0.22 + 0.28 * i) - e.width / 2), int(130 + img_h / 2 - e.height / 2)))
    y = 130 + img_h + 50
    cap = "Thanksgiving pies are here!"
    d.text((40, y), cap, font=font(F_XB, 36), fill=(*INK, 255), anchor="lm")
    f2 = font(F_BLACK, 40)
    kh = out_cubic(p(t, hl_at, 0.35)) if hl_at is not None else 0
    tw = d.textlength("DM to order", font=f2)
    if kh > 0:
        d.rounded_rectangle([30, y + 36, 30 + (tw + 24) * kh, y + 104], radius=14, fill=(*GOLD_C, 255))
    d.text((42, y + 70), "DM to order", font=f2, fill=(*INK, 255), anchor="lm")
    y += 150
    for i, (who, txt, at) in enumerate(comments):
        kk = out_cubic(p(t, at, 0.35))
        if kk <= 0: continue
        al = int(255 * kk)
        yy = y + i * 110 + int(30 * (1 - kk))
        d.ellipse([40, yy - 30, 100, yy + 30], fill=(200, 206, 220, al))
        d.text((70, yy), who[0], font=font(F_XB, 30), fill=(255, 255, 255, al), anchor="mm")
        d.text((122, yy - 18), who, font=font(F_XB, 28), fill=(*GREY, al), anchor="lm")
        d.text((122, yy + 20), txt, font=font(F_SEMI, 34), fill=(*INK, al), anchor="lm")
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(top + 60 * (1 - out_cubic(k)))))


def dm_pile(sub, t, start, top, msgs, every=0.45, w=860):
    """Stack of incoming DM banners piling up (messy order-taking)."""
    for i, (name, body) in enumerate(msgs):
        kk = p(t, start + i * every, 0.35)
        if kk <= 0: continue
        h = 140
        c, d = gbase(w, h, fill=(255, 255, 255), radius=36)
        d.ellipse([28, 30, 108, 110], fill=(*IG_PINK, 255))
        d.text((68, 70), name[0], font=font(F_BLACK, 40), fill=(255, 255, 255, 255), anchor="mm")
        d.text((132, 46), name, font=font(F_XB, 32), fill=(*INK, 255), anchor="lm")
        d.text((132, 96), body, font=font(F_SEMI, 34), fill=(70, 76, 90, 255), anchor="lm")
        d.text((w - 36, 46), "now", font=font(F_SEMI, 26), fill=(*GREY, 255), anchor="rm")
        with_alpha(c, out_cubic(kk))
        rot = ((i % 3) - 1) * 2.0
        c = c.rotate(rot, resample=Image.BICUBIC, expand=True)
        sub.alpha_composite(c, (int(W / 2 - c.width / 2 + ((i % 2) * 2 - 1) * 20), int(top + i * 128 - 80 * (1 - out_back(kk)))))
