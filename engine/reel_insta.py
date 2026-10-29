"""Instagram + Canva-style mocks for the 2026-10-29 holiday Instagram-post reels."""
from reel_quote import *
from reel_maps import offer_card, mini_calendar

IG_PINK = (225, 48, 108)
IG_ORANGE = (247, 119, 55)
IG_PURPLE = (131, 58, 180)
RED = (235, 64, 52)


def ig_search(sub, t, start, cy, query, w=880, type_dur=1.2):
    k = p(t, start, 0.35)
    if k <= 0: return
    h = 120
    c, d = card_base(w, h, radius=36, fill=(255, 255, 255, 255))
    d.ellipse([36, 38, 76, 78], outline=(*GREY, 255), width=5)
    d.line([70, 72, 88, 90], fill=(*GREY, 255), width=6)
    n = int(len(query) * p(t, start + 0.2, type_dur))
    txt = query[:n]
    f = font(F_XB, 46)
    d.text((116, 60), txt, font=f, fill=(*INK, 255), anchor="lm")
    if n < len(query) or (t * 2) % 1 < 0.5:
        x = 116 + d.textlength(txt, font=f) + 4
        d.line([x, 34, x, 86], fill=(*IG_PINK, 255), width=4)
    s = out_back(k)
    c = with_alpha(c.resize((max(1, int(w * s)), max(1, int(h * s)))), out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - c.width / 2), int(cy - c.height / 2)))


def ring_avatar(c, d, cx, cy, r, emoji, color, ring=True):
    if ring:
        for i in range(10):
            col = tuple(int(IG_ORANGE[j] + (IG_PURPLE[j] - IG_ORANGE[j]) * i / 9) for j in range(3))
            d.arc([cx - r - 10, cy - r - 10, cx + r + 10, cy + r + 10], 36 * i, 36 * i + 40, fill=(*col, 255), width=8)
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(*color, 255))
    e = emoji_img(emoji, int(r * 1.1))
    c.alpha_composite(e, (int(cx - e.width / 2), int(cy - e.height / 2)))


def account_row(sub, t, start, cy, emoji, color, handle, last, stale, flag_at, w=880, h=170):
    """Search result row: avatar, handle, last post label that flags red/green at flag_at."""
    k = p(t, start, 0.4)
    if k <= 0: return
    c, d = card_base(w, h, radius=34, fill=(255, 255, 255, 255))
    ring_avatar(c, d, 95, h // 2, 50, emoji, color, ring=False)
    d.text((180, 60), handle, font=font(F_XB, 42), fill=(*INK, 255), anchor="lm")
    d.text((180, 116), f"Last post: {last}", font=font(F_SEMI, 34), fill=(*GREY, 255), anchor="lm")
    kf = p(t, flag_at, 0.35)
    if kf > 0:
        col = RED if stale else (40, 170, 100)
        lab = "QUIET" if stale else "ACTIVE"
        s = max(0.02, out_back(kf))
        bw, bh = 170 * s, 64 * s
        x1 = w - 40
        d.rounded_rectangle([x1 - bw, h / 2 - bh / 2, x1, h / 2 + bh / 2], radius=bh / 2, fill=(*col, int(255 * out_cubic(kf))))
        d.text((x1 - bw / 2, h / 2), lab, font=font(F_BLACK, 30 * s), fill=(255, 255, 255, int(255 * out_cubic(kf))), anchor="mm")
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2 + 70 * (1 - out_cubic(k))), int(cy - h / 2)))


def ig_profile(sub, t, start, top, handle, emoji, color, stale_at, w=880):
    """Profile with a 3x3 grid; at stale_at the grid dims and a 'last post 5 weeks ago' tag drops."""
    k = p(t, start, 0.45)
    if k <= 0: return
    h = 930
    c, d = card_base(w, h, radius=40, fill=(255, 255, 255, 255))
    ring_avatar(c, d, 120, 130, 72, emoji, color)
    d.text((240, 92), handle, font=font(F_BLACK, 44), fill=(*INK, 255), anchor="lm")
    for i, (n, lab) in enumerate([("212", "posts"), ("1,480", "followers"), ("390", "following")]):
        x = 260 + i * 200
        d.text((x, 160), n, font=font(F_BLACK, 38), fill=(*INK, 255), anchor="mm")
        d.text((x, 200), lab, font=font(F_SEMI, 28), fill=(*GREY, 255), anchor="mm")
    d.text((48, 270), "Hand-poured candles · Local pickup", font=font(F_SEMI, 34), fill=(*INK, 255), anchor="lm")
    ks = out_cubic(p(t, stale_at, 0.5))
    tiles = ["🕯️", "🌿", "🍂", "🕯️", "☕", "🌸", "🕯️", "🌞", "🌿"]
    cols = [(250, 214, 165), (200, 230, 200), (245, 190, 140), (240, 220, 200), (220, 200, 180), (250, 210, 220), (230, 210, 170), (255, 235, 160), (190, 220, 190)]
    sz = (w - 2 * 6) / 3
    for i in range(6):
        r, cc = divmod(i, 3)
        x0, y0 = cc * (sz + 6), 330 + r * (sz + 6)
        base = cols[i]
        grey = sum(base) // 3
        col = tuple(int(base[j] + (grey - base[j]) * ks * 0.8) for j in range(3))
        kt = out_cubic(p(t, start + 0.3 + i * 0.05, 0.3))
        d.rectangle([x0, y0, x0 + sz, y0 + sz], fill=(*col, int(255 * kt)))
        e = with_alpha(emoji_img(tiles[i], 90).copy(), kt * (1 - 0.5 * ks))
        c.alpha_composite(e, (int(x0 + sz / 2 - e.width / 2), int(y0 + sz / 2 - e.height / 2)))
    if ks > 0:
        kb = max(0.02, out_back(p(t, stale_at + 0.2, 0.4)))
        bw, bh = 640 * kb, 104 * kb
        cy = 626
        d.rounded_rectangle([w / 2 - bw / 2, cy - bh / 2, w / 2 + bw / 2, cy + bh / 2], radius=bh / 2, fill=(*RED, 255))
        d.text((w / 2, cy), "Last post: 5 weeks ago", font=font(F_BLACK, 44 * kb), fill=(255, 255, 255, 255), anchor="mm")
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(top + 70 * (1 - out_cubic(k)))))


def design(c, d, x, y, s, a, acc, line1="CYBER", line2="MONDAY", badge="20% OFF", foot="Nov 30 only · link in bio", emoji="🕯️"):
    """Draws the square sale post at (x,y) with size s. a = list of 5 reveal amounts (bg, headline, product, badge, footer)."""
    bgc = tuple(int(255 + (v - 255) * a[0]) for v in (28, 22, 60))
    d.rectangle([x, y, x + s, y + s], fill=(*bgc, 255))
    if a[0] > 0:
        for i in range(14):
            rx = x + (i * 97) % int(s); ry = y + (i * 53) % int(s * 0.5)
            r = s * 0.008
            d.ellipse([rx - r, ry - r, rx + r, ry + r], fill=(255, 255, 255, int(160 * a[0])))
    if a[1] > 0:
        al = int(255 * a[1])
        d.text((x + s / 2, y + s * 0.17), line1, font=font(F_BLACK, s * 0.15), fill=(*acc, al), anchor="mm")
        d.text((x + s / 2, y + s * 0.31), line2, font=font(F_BLACK, s * 0.15), fill=(255, 255, 255, al), anchor="mm")
    if a[2] > 0:
        e = with_alpha(emoji_img(emoji, int(s * 0.3 * (0.6 + 0.4 * a[2]))).copy(), a[2])
        c.alpha_composite(e, (int(x + s * 0.38 - e.width / 2), int(y + s * 0.6 - e.height / 2)))
    if a[3] > 0:
        r = s * 0.13 * out_back(min(1, a[3]))
        cx, cy = x + s * 0.7, y + s * 0.58
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(*acc, 255))
        parts = badge.split(" ")
        d.text((cx, cy - r * 0.22), parts[0], font=font(F_BLACK, r * 0.62), fill=(*INK, 255), anchor="mm")
        d.text((cx, cy + r * 0.4), parts[1] if len(parts) > 1 else "", font=font(F_BLACK, r * 0.4), fill=(*INK, 255), anchor="mm")
    if a[4] > 0:
        al = int(255 * a[4])
        d.rounded_rectangle([x + s * 0.08, y + s * 0.82, x + s * 0.92, y + s * 0.93], radius=s * 0.055, fill=(255, 255, 255, al))
        d.text((x + s / 2, y + s * 0.875), foot, font=font(F_XB, s * 0.048), fill=(*INK, al), anchor="mm")


def canva_editor(sub, t, start, cy, acc, steps, w=880, h=1060, labels=None):
    """Canva-style editor: top bar, tool rail, square canvas that builds over steps[0..4]."""
    k = p(t, start, 0.45)
    if k <= 0: return
    c, d = card_base(w, h, radius=36, fill=(236, 239, 245, 255))
    d.rounded_rectangle([0, 0, w - 1, 100], radius=36, fill=(110, 70, 230, 255))
    d.rectangle([0, 60, w - 1, 100], fill=(110, 70, 230, 255))
    d.text((40, 52), "Instagram post · 1080 x 1080", font=font(F_XB, 32), fill=(255, 255, 255, 255), anchor="lm")
    d.rounded_rectangle([w - 170, 24, w - 34, 80], radius=28, fill=(255, 255, 255, 255))
    d.text((w - 102, 52), "Share", font=font(F_XB, 28), fill=(110, 70, 230, 255), anchor="mm")
    tools = [("🖼️", "Design"), ("🔤", "Text"), ("📷", "Photos"), ("⭐", "Elements")]
    for i, (ic, lab) in enumerate(tools):
        y = 170 + i * 150
        active = i == min(3, sum(1 for s in steps if t >= s) - 1) if t >= steps[0] else False
        if active:
            d.rounded_rectangle([14, y - 56, 126, y + 70], radius=20, fill=(220, 210, 255, 255))
        e = emoji_img(ic, 54)
        c.alpha_composite(e, (int(70 - e.width / 2), int(y - e.height / 2)))
        d.text((70, y + 50), lab, font=font(F_SEMI, 22), fill=(*INK, 255), anchor="mm")
    s = 680
    x, y = 160, 150
    d.rectangle([x - 4, y - 4, x + s + 4, y + s + 4], fill=(210, 214, 222, 255))
    a = [out_cubic(p(t, st, 0.45)) for st in steps]
    design(c, d, x, y, s, a, acc)
    # step label under canvas
    if labels:
        idx = sum(1 for st in steps if t >= st) - 1
        if idx >= 0:
            kk = out_cubic(p(t, steps[idx], 0.3))
            d.rounded_rectangle([160, 880, 160 + s, 990], radius=30, fill=(255, 255, 255, 255))
            d.text((160 + s / 2, 935), labels[idx], font=font(F_XB, 38), fill=(*INK, int(255 * kk)), anchor="mm")
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(cy - h / 2 + 60 * (1 - out_cubic(k)))))


def feed_post(sub, t, start, cy, acc, handle="@oakwickcandles", w=760):
    """Instagram feed post card showing the finished design (no fake engagement numbers)."""
    k = p(t, start, 0.45)
    if k <= 0: return
    h = w + 270
    c, d = card_base(w, h, radius=36, fill=(255, 255, 255, 255))
    ring_avatar(c, d, 64, 62, 32, "🕯️", (250, 214, 165))
    d.text((120, 62), handle, font=font(F_XB, 34), fill=(*INK, 255), anchor="lm")
    d.text((w - 40, 62), "•••", font=font(F_XB, 34), fill=(*INK, 255), anchor="rm")
    design(c, d, 0, 124, w, [1, 1, 1, 1, 1], acc)
    yb = 124 + w + 44
    d.text((40, yb), "♡", font=font(DEJAVU, 52), fill=(*INK, 255), anchor="lm")
    d.text((110, yb), "↗", font=font(DEJAVU, 48), fill=(*INK, 255), anchor="lm")
    d.text((40, yb + 62), "Cyber Monday only. Tap the link in bio.", font=font(F_SEMI, 30), fill=(*INK, 255), anchor="lm")
    c = with_alpha(c, out_cubic(k))
    sc = 0.9 + 0.1 * out_back(k)
    c = c.resize((int(w * sc), int(h * sc)))
    sub.alpha_composite(c, (int(W / 2 - c.width / 2), int(cy - c.height / 2)))


def timeline(sub, t, start, top, items, acc, every=0.7, w=880, row=150):
    """Vertical post schedule: (date, label, emoji)."""
    d = ImageDraw.Draw(sub)
    x0 = W / 2 - w / 2
    for i, (date, lab, ic) in enumerate(items):
        kk = p(t, start + i * every, 0.4)
        if kk <= 0: continue
        y = top + i * row
        a = out_cubic(kk)
        if i > 0:
            d.line([x0 + 70, y - row + 50, x0 + 70, y - 50], fill=(255, 255, 255, int(120 * a)), width=6)
        r = 46 * max(0.02, out_back(kk))
        d.ellipse([x0 + 70 - r, y - r, x0 + 70 + r, y + r], fill=(*acc, int(255 * a)))
        d.text((x0 + 70, y), str(i + 1), font=font(F_BLACK, 44 * max(0.1, out_back(kk))), fill=(*INK, int(255 * a)), anchor="mm")
        dx = 60 * (1 - a)
        d.text((x0 + 150 + dx, y - 26), date, font=font(F_XB, 34), fill=(*acc, int(255 * a)), anchor="lm")
        d.text((x0 + 150 + dx, y + 24), lab, font=font(F_BLACK, 48), fill=(255, 255, 255, int(255 * a)), anchor="lm")
        place_emoji(sub, ic, x0 + w - 50 - dx, y, 80, alpha=a)
