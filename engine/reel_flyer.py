"""Helpers for the 2026-11-02 Small Business Saturday flyer reels (flyer design, Canva flyer editor, Facebook-style posts)."""
from reel_preorder import *

FB_BLUE = (24, 119, 242)
CREAM = (255, 248, 236)


def flyer(c, d, x, y, w, a, acc, shop="Leaf & Pot", emoji="🪴", offer="Free gift wrap all day", foot="9am-6pm · 12 Main St"):
    """Portrait flyer (w x 1.3w) at (x,y). a = 5 reveal amounts (bg, headline, product, offer, footer)."""
    h = w * 1.3
    bgc = tuple(int(255 + (v - 255) * a[0]) for v in CREAM)
    d.rectangle([x, y, x + w, y + h], fill=(*bgc, 255))
    if a[0] > 0:
        d.rectangle([x, y, x + w, y + h * 0.36], fill=(*acc, int(255 * a[0])))
        for i in range(12):
            rx = x + (i * 113) % int(w); ry = y + (i * 47) % int(h * 0.33)
            r = w * 0.01
            d.ellipse([rx - r, ry - r, rx + r, ry + r], fill=(255, 255, 255, int(150 * a[0])))
    if a[1] > 0:
        al = int(255 * a[1])
        d.text((x + w / 2, y + h * 0.08), shop.upper(), font=font(F_XB, w * 0.05), fill=(*INK, al), anchor="mm")
        d.text((x + w / 2, y + h * 0.16), "SMALL BUSINESS", font=font(F_BLACK, w * 0.11), fill=(255, 255, 255, al), anchor="mm")
        d.text((x + w / 2, y + h * 0.25), "SATURDAY", font=font(F_BLACK, w * 0.15), fill=(*INK, al), anchor="mm")
        bw = w * 0.42
        d.rounded_rectangle([x + w / 2 - bw / 2, y + h * 0.31, x + w / 2 + bw / 2, y + h * 0.38], radius=w * 0.04, fill=(*INK, al))
        d.text((x + w / 2, y + h * 0.345), "SAT · NOV 28", font=font(F_BLACK, w * 0.05), fill=(255, 255, 255, al), anchor="mm")
    if a[2] > 0:
        e = with_alpha(emoji_img(emoji, int(w * 0.3 * (0.6 + 0.4 * a[2]))).copy(), a[2])
        c.alpha_composite(e, (int(x + w / 2 - e.width / 2), int(y + h * 0.52 - e.height / 2)))
    if a[3] > 0:
        al = int(255 * a[3])
        bw = w * 0.84 * (0.7 + 0.3 * out_back(min(1, a[3])))
        d.rounded_rectangle([x + w / 2 - bw / 2, y + h * 0.66, x + w / 2 + bw / 2, y + h * 0.77], radius=w * 0.05, fill=(*acc, al))
        d.text((x + w / 2, y + h * 0.715), offer, font=font(F_BLACK, w * 0.058), fill=(*INK, al), anchor="mm")
    if a[4] > 0:
        al = int(255 * a[4])
        d.text((x + w / 2, y + h * 0.84), foot, font=font(F_XB, w * 0.05), fill=(*INK, al), anchor="mm")
        d.text((x + w / 2, y + h * 0.91), "Shop local this holiday", font=font(F_SEMI, w * 0.042), fill=(*GREY, al), anchor="mm")


def flyer_card(sub, t, start, cx, cy, acc, w=560, rot=0.0, steps=None, **kw):
    """Standalone flyer with shadow. steps: 5 reveal times (None = all shown)."""
    k = p(t, start, 0.45)
    if k <= 0: return
    h = int(w * 1.3)
    pad = 30
    c = Image.new("RGBA", (w + 2 * pad, h + 2 * pad), (0, 0, 0, 0))
    d = ImageDraw.Draw(c)
    d.rounded_rectangle([pad + 8, pad + 14, pad + w + 8, pad + h + 14], radius=20, fill=(0, 0, 0, 90))
    a = [out_cubic(p(t, s, 0.45)) for s in steps] if steps else [1] * 5
    fl = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    fd = ImageDraw.Draw(fl)
    flyer(fl, fd, 0, 0, w, a, acc, **kw)
    m = Image.new("L", (w, h), 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, w - 1, h - 1], radius=20, fill=255)
    fl.putalpha(Image.composite(fl.getchannel("A"), m, m))
    c.alpha_composite(fl, (pad, pad))
    s = 0.85 + 0.15 * out_back(k)
    c = c.resize((int(c.width * s), int(c.height * s)), Image.LANCZOS)
    if rot:
        c = c.rotate(rot, resample=Image.BICUBIC, expand=True)
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(cx - c.width / 2), int(cy - c.height / 2 + 60 * (1 - out_cubic(k)))))


def canva_flyer(sub, t, start, cy, acc, steps, w=880, h=1080, labels=None, **kw):
    """Canva-style editor whose portrait canvas builds the flyer over steps[0..4]."""
    k = p(t, start, 0.45)
    if k <= 0: return
    c, d = card_base(w, h, radius=36, fill=(236, 239, 245, 255))
    d.rounded_rectangle([0, 0, w - 1, 100], radius=36, fill=(110, 70, 230, 255))
    d.rectangle([0, 60, w - 1, 100], fill=(110, 70, 230, 255))
    d.text((40, 52), "Flyer · 8.5 x 11 in", font=font(F_XB, 32), fill=(255, 255, 255, 255), anchor="lm")
    d.rounded_rectangle([w - 210, 24, w - 34, 80], radius=28, fill=(255, 255, 255, 255))
    d.text((w - 122, 52), "Download", font=font(F_XB, 28), fill=(110, 70, 230, 255), anchor="mm")
    tools = [("🖼️", "Design"), ("🔤", "Text"), ("📷", "Photos"), ("⭐", "Elements")]
    n = sum(1 for s in steps if t >= s)
    for i, (ic, lab) in enumerate(tools):
        y = 180 + i * 150
        if n > 0 and i == min(3, n - 1):
            d.rounded_rectangle([14, y - 56, 126, y + 70], radius=20, fill=(220, 210, 255, 255))
        e = emoji_img(ic, 54)
        c.alpha_composite(e, (int(70 - e.width / 2), int(y - e.height / 2)))
        d.text((70, y + 50), lab, font=font(F_SEMI, 22), fill=(*INK, 255), anchor="mm")
    fw = 560
    x, y = 160 + (680 - fw) // 2, 130
    d.rectangle([x - 4, y - 4, x + fw + 4, y + fw * 1.3 + 4], fill=(210, 214, 222, 255))
    a = [out_cubic(p(t, st, 0.45)) for st in steps]
    flyer(c, d, x, y, fw, a, acc, **kw)
    if labels and n > 0:
        kk = out_cubic(p(t, steps[n - 1], 0.3))
        d.rounded_rectangle([160, h - 140, 160 + 680, h - 40], radius=30, fill=(255, 255, 255, 255))
        d.text((160 + 340, h - 90), labels[n - 1], font=font(F_XB, 38), fill=(*INK, int(255 * kk)), anchor="mm")
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(cy - h / 2 + 60 * (1 - out_cubic(k)))))


def fb_search(sub, t, start, cy, query, w=880, type_dur=1.3):
    k = p(t, start, 0.35)
    if k <= 0: return
    h = 120
    c, d = card_base(w, h, radius=60, fill=(255, 255, 255, 255))
    d.ellipse([24, 20, 104, 100], fill=(*FB_BLUE, 255))
    d.text((66, 64), "f", font=font(F_BLACK, 62), fill=(255, 255, 255, 255), anchor="mm")
    n = int(len(query) * p(t, start + 0.2, type_dur))
    txt = query[:n]
    f = font(F_XB, 42)
    d.text((130, 60), txt, font=f, fill=(*INK, 255), anchor="lm")
    if n < len(query) or (t * 2) % 1 < 0.5:
        xx = 130 + d.textlength(txt, font=f) + 4
        d.line([xx, 34, xx, 86], fill=(*FB_BLUE, 255), width=4)
    s = out_back(k)
    c = with_alpha(c.resize((max(1, int(w * s)), max(1, int(h * s)))), out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - c.width / 2), int(cy - c.height / 2)))


def fb_chips(sub, t, start, cy, chips, active=0, act_at=None, every=0.3):
    d = ImageDraw.Draw(sub)
    f = font(F_XB, 38)
    widths = [d.textlength(ch, font=f) + 60 for ch in chips]
    x = W / 2 - (sum(widths) + 20 * (len(chips) - 1)) / 2
    for i, (ch, bw) in enumerate(zip(chips, widths)):
        kk = out_cubic(p(t, start + i * every, 0.3))
        if kk > 0:
            on = i == active and act_at is not None and t >= act_at
            fill = (*FB_BLUE, int(255 * kk)) if on else (255, 255, 255, int(230 * kk))
            fg = (255, 255, 255, int(255 * kk)) if on else (*INK, int(255 * kk))
            d.rounded_rectangle([x, cy - 36, x + bw, cy + 36], radius=36, fill=fill)
            d.text((x + bw / 2, cy), ch, font=f, fill=fg, anchor="mm")
        x += bw + 20


def fb_post(sub, t, start, cy, emoji, color, shop, ago, body, has_flyer, flag_at, acc, w=880, h=260):
    """Facebook-style page post row. Flags NO FLYER (red) or HAS FLYER (green) at flag_at. Sample shops."""
    k = p(t, start, 0.4)
    if k <= 0: return
    c, d = card_base(w, h, radius=34, fill=(255, 255, 255, 255))
    d.ellipse([30, 30, 120, 120], fill=(*color, 255))
    e = emoji_img(emoji, 54)
    c.alpha_composite(e, (int(75 - e.width / 2), int(75 - e.height / 2)))
    d.text((144, 56), shop, font=font(F_XB, 40), fill=(*INK, 255), anchor="lm")
    d.text((144, 100), f"{ago} · 🌐".replace(" · 🌐", ""), font=font(F_SEMI, 30), fill=(*GREY, 255), anchor="lm")
    d.text((40, h - 75), body, font=font(F_SEMI, 36), fill=(*INK, 255), anchor="lm")
    if has_flyer:
        mini = Image.new("RGBA", (120, 156), (0, 0, 0, 0))
        flyer(mini, ImageDraw.Draw(mini), 0, 0, 120, [1] * 5, acc, emoji=emoji)
        c.alpha_composite(mini, (w - 160, 52))
    kf = p(t, flag_at, 0.35)
    if kf > 0:
        col = (40, 170, 100) if has_flyer else RED
        lab = "HAS FLYER" if has_flyer else "NO FLYER"
        s = max(0.02, out_back(kf))
        bw, bh = (200 if has_flyer else 220) * s, 60 * s
        x1 = w - 40 if not has_flyer else w - 180
        yb = 76
        d.rounded_rectangle([x1 - bw, yb - bh / 2, x1, yb + bh / 2], radius=bh / 2, fill=(*col, int(255 * out_cubic(kf))))
        d.text((x1 - bw / 2, yb), lab, font=font(F_BLACK, 28 * s), fill=(255, 255, 255, int(255 * out_cubic(kf))), anchor="mm")
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2 + 70 * (1 - out_cubic(k))), int(cy - h / 2)))


def plain_post(sub, t, start, top, acc, w=820, scroll_at=None):
    """A shop's text-only Facebook post that gets scrolled past (problem scene)."""
    k = p(t, start, 0.45)
    if k <= 0: return
    h = 560
    c, d = card_base(w, h, radius=36, fill=(255, 255, 255, 255))
    d.ellipse([36, 36, 126, 126], fill=(170, 220, 180, 255))
    e = emoji_img("🪴", 54)
    c.alpha_composite(e, (int(81 - e.width / 2), int(81 - e.height / 2)))
    d.text((150, 62), "Leaf & Pot", font=font(F_XB, 40), fill=(*INK, 255), anchor="lm")
    d.text((150, 106), "Just now", font=font(F_SEMI, 30), fill=(*GREY, 255), anchor="lm")
    for i, ln in enumerate(["we are open saturday", "come by", "thanks"]):
        d.text((40, 210 + i * 62), ln, font=font(F_SEMI, 44), fill=(*INK, 255), anchor="lm")
    d.line([40, 430, w - 40, 430], fill=(228, 231, 238, 255), width=3)
    for i, lab in enumerate(["👍 Like", "💬 Comment", "↗ Share"]):
        d.text((w * (0.18 + 0.32 * i), 495), lab.split(" ", 1)[1], font=font(F_SEMI, 32), fill=(*GREY, 255), anchor="mm")
    off = 0
    if scroll_at is not None:
        ks = in_out(p(t, scroll_at, 0.9))
        off = -700 * ks
        c = with_alpha(c, out_cubic(k) * (1 - ks))
    else:
        c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(top + off + 60 * (1 - out_cubic(k)))))
