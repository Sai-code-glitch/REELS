"""Helpers for the 2026-11-12 holiday drink menu gig for local cafés
(4:5 menu graphic, Canva menu editor, blurry chalkboard photo, café Instagram lead rows)."""
from PIL import ImageFilter
from reel_etsy import *

CREAM = (250, 244, 232)
COCOA = (70, 40, 28)
HOLLY = (190, 40, 50)
DRINKS = [("Peppermint Mocha", "$5.75"), ("Gingerbread Latte", "$5.50"), ("Maple Chai", "$5.25"),
          ("Hot Cocoa", "$4.25"), ("Eggnog Cold Brew", "$5.95")]


def menu(c, d, x, y, w, a, acc, shop="Bean & Bell", drinks=DRINKS, n_rows=None):
    """4:5 holiday drink menu. a = 5 reveal amounts (bg, title, drink rows, NEW badge, footer)."""
    h = w * 5 / 4
    bgc = tuple(int(255 + (v - 255) * a[0]) for v in CREAM)
    d.rectangle([x, y, x + w, y + h], fill=(*bgc, 255))
    if a[0] > 0:
        al = int(255 * a[0])
        d.rectangle([x, y, x + w, y + h * 0.27], fill=(*COCOA, al))
        for i in range(16):
            rx = x + (i * 151) % int(w); ry = y + (i * 47) % int(h * 0.25)
            r = w * 0.01
            d.ellipse([rx - r, ry - r, rx + r, ry + r], fill=(255, 255, 255, int(150 * a[0])))
    if a[1] > 0:
        al = int(255 * a[1])
        d.text((x + w / 2, y + h * 0.1), "HOLIDAY", font=font(F_BLACK, w * 0.13), fill=(255, 255, 255, al), anchor="mm")
        d.text((x + w / 2, y + h * 0.2), "DRINKS", font=font(F_BLACK, w * 0.13), fill=(*GOLD_C, al), anchor="mm")
    rows = drinks if n_rows is None else drinks[:n_rows]
    for i, (name, price) in enumerate(rows):
        ka = clamp(a[2] * len(rows) - i)
        if ka <= 0: continue
        al = int(255 * out_cubic(ka))
        ry = y + h * (0.34 + i * 0.105)
        off = w * 0.06 * (1 - out_cubic(ka))
        f = font(F_XB, w * 0.058)
        d.text((x + w * 0.08 + off, ry), name, font=f, fill=(*COCOA, al), anchor="lm")
        d.text((x + w * 0.92, ry), price, font=font(F_BLACK, w * 0.06), fill=(*HOLLY, al), anchor="rm")
        x0 = x + w * 0.08 + off + d.textlength(name, font=f) + w * 0.03
        x1 = x + w * 0.92 - d.textlength(price, font=font(F_BLACK, w * 0.06)) - w * 0.03
        dx = x0
        while dx < x1:
            d.ellipse([dx, ry + w * 0.012, dx + w * 0.008, ry + w * 0.02], fill=(*GREY, al))
            dx += w * 0.022
    if a[3] > 0 and len(rows) > 0:
        s = max(0.05, out_back(min(1, a[3])))
        bx, by = x + w * 0.87, y + h * 0.2
        r = w * 0.075 * s
        d.ellipse([bx - r, by - r, bx + r, by + r], fill=(*HOLLY, 255))
        d.text((bx, by), "NEW", font=font(F_BLACK, w * 0.045 * s), fill=(255, 255, 255, 255), anchor="mm")
    if a[4] > 0:
        al = int(255 * a[4])
        d.line([x + w * 0.1, y + h * 0.88, x + w * 0.9, y + h * 0.88], fill=(*COCOA, int(al * 0.4)), width=max(2, int(w * 0.004)))
        d.text((x + w / 2, y + h * 0.935), f"{shop.upper()} · Oat milk +$0.75", font=font(F_XB, w * 0.045), fill=(*COCOA, al), anchor="mm")


def menu_card(sub, t, start, cx, cy, acc, w=560, rot=0.0, steps=None, **kw):
    k = p(t, start, 0.45)
    if k <= 0: return
    h = int(w * 5 / 4)
    pad = 30
    c = Image.new("RGBA", (w + 2 * pad, h + 2 * pad), (0, 0, 0, 0))
    d = ImageDraw.Draw(c)
    d.rounded_rectangle([pad + 8, pad + 14, pad + w + 8, pad + h + 14], radius=28, fill=(0, 0, 0, 90))
    a = [out_cubic(p(t, s, 0.45)) for s in steps] if steps else [1] * 5
    st = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    menu(st, ImageDraw.Draw(st), 0, 0, w, a, acc, **kw)
    m = Image.new("L", (w, h), 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, w - 1, h - 1], radius=28, fill=255)
    st.putalpha(Image.composite(st.getchannel("A"), m, m))
    c.alpha_composite(st, (pad, pad))
    s = 0.85 + 0.15 * out_back(k)
    c = c.resize((int(c.width * s), int(c.height * s)), Image.LANCZOS)
    if rot:
        c = c.rotate(rot, resample=Image.BICUBIC, expand=True)
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(cx - c.width / 2), int(cy - c.height / 2 + 60 * (1 - out_cubic(k)))))


_CHALK = {}


def chalk_img(w, h):
    """A dark, blurry, slightly tilted phone photo of a handwritten chalkboard (cached)."""
    key = (w, h)
    if key in _CHALK: return _CHALK[key]
    im = Image.new("RGBA", (w, h), (34, 38, 36, 255))
    d = ImageDraw.Draw(im)
    d.rectangle([0, 0, w, h], fill=(40, 46, 42, 255))
    d.rectangle([w * 0.06, h * 0.06, w * 0.94, h * 0.94], fill=(28, 34, 30, 255), outline=(120, 90, 60, 255), width=int(w * 0.03))
    fw = font(F_XB, w * 0.07)
    d.text((w / 2, h * 0.17), "Holiday drinks!!", font=fw, fill=(230, 230, 220, 230), anchor="mm")
    import random
    rnd = random.Random(7)
    for i in range(6):
        yy = h * (0.3 + i * 0.1)
        x = w * 0.14
        while x < w * 0.68:
            seg = rnd.uniform(w * 0.04, w * 0.11)
            d.line([x, yy + rnd.uniform(-4, 4), x + seg, yy + rnd.uniform(-4, 4)], fill=(220, 220, 210, 200), width=int(w * 0.014))
            x += seg + w * 0.025
        d.text((w * 0.8, yy), "$?", font=font(F_XB, w * 0.05), fill=(220, 220, 210, 160), anchor="mm")
    # glare + blur
    g = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    ImageDraw.Draw(g).ellipse([w * 0.5, -h * 0.1, w * 1.1, h * 0.4], fill=(255, 255, 240, 70))
    im.alpha_composite(g.filter(ImageFilter.GaussianBlur(w * 0.06)))
    im = im.filter(ImageFilter.GaussianBlur(w * 0.012))
    _CHALK[key] = im
    return im


def chalk_photo(sub, t, start, cx, cy, w=640, h=760, rot=-5, flag_at=None, flags=("Can't read it", "No prices", "Last year's")):
    k = p(t, start, 0.45)
    if k <= 0: return
    pad = 24
    c = Image.new("RGBA", (w + 2 * pad, h + 2 * pad + 80), (0, 0, 0, 0))
    d = ImageDraw.Draw(c)
    d.rounded_rectangle([pad, pad, pad + w, pad + h + 80], radius=20, fill=(255, 255, 255, 255))
    c.alpha_composite(chalk_img(w - 40, h - 40), (pad + 20, pad + 20))
    d.text((pad + 34, pad + h + 30), "📷 menu.jpg · posted Dec 2025", font=font(F_SEMI, 30), fill=(*GREY, 255), anchor="lm")
    s = 0.85 + 0.15 * out_back(k)
    c = c.resize((int(c.width * s), int(c.height * s)), Image.LANCZOS).rotate(rot, resample=Image.BICUBIC, expand=True)
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(cx - c.width / 2), int(cy - c.height / 2 + 60 * (1 - out_cubic(k)))))
    if flag_at is not None:
        for i, lab in enumerate(flags):
            kf = p(t, flag_at + i * 0.55, 0.4)
            if kf > 0:
                yy = cy - h * 0.3 + i * 150
                xx = cx + (230 if i % 2 == 0 else -230)
                pill(sub, xx, yy, lab, F_BLACK, 44, RED, WHITE, alpha=out_cubic(kf), scale=out_back(kf), icon="❌")


def canva_menu(sub, t, start, cy, acc, steps, w=880, h=1060, labels=None, **kw):
    """Canva-style editor whose 4:5 canvas builds the menu over steps[0..4]."""
    k = p(t, start, 0.45)
    if k <= 0: return
    c, d = card_base(w, h, radius=36, fill=(236, 239, 245, 255))
    d.rounded_rectangle([0, 0, w - 1, 100], radius=36, fill=(110, 70, 230, 255))
    d.rectangle([0, 60, w - 1, 100], fill=(110, 70, 230, 255))
    d.text((40, 52), "Instagram Post · 1080 x 1350", font=font(F_XB, 30), fill=(255, 255, 255, 255), anchor="lm")
    d.rounded_rectangle([w - 210, 24, w - 34, 80], radius=28, fill=(255, 255, 255, 255))
    d.text((w - 122, 52), "Download", font=font(F_XB, 28), fill=(110, 70, 230, 255), anchor="mm")
    tools = [("🖼️", "Design"), ("🔤", "Text"), ("⭐", "Elements"), ("📤", "Share")]
    n = sum(1 for s in steps if t >= s)
    for i, (ic, lab) in enumerate(tools):
        yy = 190 + i * 160
        if n > 0 and i == min(3, max(0, n - 2)):
            d.rounded_rectangle([14, yy - 56, 126, yy + 70], radius=20, fill=(220, 210, 255, 255))
        e = emoji_img(ic, 54)
        c.alpha_composite(e, (int(70 - e.width / 2), int(yy - e.height / 2)))
        d.text((70, yy + 50), lab, font=font(F_SEMI, 22), fill=(*INK, 255), anchor="mm")
    sw = 640
    x, y = 160 + (700 - sw) // 2, 130
    d.rectangle([x - 4, y - 4, x + sw + 4, y + sw * 5 / 4 + 4], fill=(210, 214, 222, 255))
    a = [out_cubic(p(t, st, 0.45)) for st in steps]
    menu(c, d, x, y, sw, a, acc, **kw)
    if labels and n > 0:
        kk = out_cubic(p(t, steps[n - 1], 0.3))
        d.rounded_rectangle([140, h - 120, w - 40, h - 26], radius=30, fill=(255, 255, 255, 255))
        d.text(((140 + w - 40) / 2, h - 73), labels[n - 1], font=font(F_XB, 38), fill=(*INK, int(255 * kk)), anchor="mm")
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(cy - h / 2 + 60 * (1 - out_cubic(k)))))


def cafe_row(sub, t, start, cy, emoji, color, handle, menu_label, good, flag_at, w=880, h=170):
    """Instagram account row: avatar, handle, 'Menu post: ...' and a LEAD / OK flag."""
    k = p(t, start, 0.4)
    if k <= 0: return
    c, d = card_base(w, h, radius=34, fill=(255, 255, 255, 255))
    lead = (not good) and t >= flag_at + 0.4
    if lead:
        d.rounded_rectangle([0, 0, w - 1, h - 1], radius=34, outline=(*GOLD_C, 255), width=8)
    ring_avatar(c, d, 95, h // 2, 50, emoji, color, ring=False)
    d.text((180, 60), handle, font=font(F_XB, 42), fill=(*INK, 255), anchor="lm")
    d.text((180, 116), f"Menu: {menu_label}", font=font(F_SEMI, 32), fill=(*GREY, 255), anchor="lm")
    kf = p(t, flag_at, 0.35)
    if kf > 0:
        col = (40, 170, 100) if good else RED
        lab = "CLEAR" if good else "LEAD"
        s = max(0.02, out_back(kf))
        bw, bh = 170 * s, 64 * s
        x1 = w - 40
        d.rounded_rectangle([x1 - bw, h / 2 - bh / 2, x1, h / 2 + bh / 2], radius=bh / 2, fill=(*col, int(255 * out_cubic(kf))))
        d.text((x1 - bw / 2, h / 2), lab, font=font(F_BLACK, 30 * s), fill=(255, 255, 255, int(255 * out_cubic(kf))), anchor="mm")
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2 + 70 * (1 - out_cubic(k))), int(cy - h / 2)))
