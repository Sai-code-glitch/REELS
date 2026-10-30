"""Helpers for the 2026-10-30 holiday e-gift-card reels (shop website mock, find bar, gift card, site-check rows)."""
from reel_insta import *
from reel_email import build_row
from reel_chat import phone_chat
from reel_portfolio import strike

GREEN = (40, 170, 90)


def gbase(w, h, fill=(250, 251, 255), radius=40):
    c = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(c)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=radius, fill=(*fill[:3], 255))
    return c, d


def browser(sub, t, start, top, url, shop, emoji, color, nav, add_at=None, find=None, w=880, h=760):
    """Small-shop website mock. add_at: time a '🎁 Gift cards' button pops into the nav.
    find: (query, start, found) -> Ctrl+F bar typing query then showing result."""
    k = p(t, start, 0.4)
    if k <= 0: return
    c, d = gbase(w, h, fill=(255, 255, 255))
    # chrome
    d.rounded_rectangle([0, 0, w - 1, 110], radius=40, fill=(232, 235, 242, 255))
    d.rectangle([0, 70, w - 1, 110], fill=(232, 235, 242, 255))
    for i, col in enumerate([(255, 95, 86), (255, 189, 46), (39, 201, 63)]):
        d.ellipse([34 + i * 40, 40, 58 + i * 40, 64], fill=(*col, 255))
    d.rounded_rectangle([170, 26, w - 40, 84], radius=29, fill=(255, 255, 255, 255))
    d.text((210, 55), url, font=font(F_SEMI, 32), fill=(70, 76, 90, 255), anchor="lm")
    # hero
    d.rectangle([0, 110, w - 1, 400], fill=(*color, 255))
    e = emoji_img(emoji, 120)
    c.alpha_composite(e, (60, int(255 - e.height / 2)))
    d.text((210, 225), shop, font=font(F_BLACK, 58), fill=(*INK, 255), anchor="lm")
    d.text((212, 295), "Handmade in your town", font=font(F_SEMI, 32), fill=(60, 66, 80, 255), anchor="lm")
    # nav
    f = font(F_XB, 36)
    x = 50; y = 460
    for item in nav:
        d.text((x, y), item, font=f, fill=(*INK, 255), anchor="lm")
        x += d.textlength(item, font=f) + 46
    if add_at is not None:
        ka = p(t, add_at, 0.45)
        if ka > 0:
            s = out_back(ka)
            lab = "🎁 Gift cards"
            bw, bh = 300 * s, 76 * s
            cx, cy = x + 150, y
            if cx + 150 > w - 30:
                cx, cy = w / 2, y + 110
            d.rounded_rectangle([cx - bw / 2, cy - bh / 2, cx + bw / 2, cy + bh / 2], radius=bh / 2, fill=(*GREEN, int(255 * out_cubic(ka))))
            if s > 0.3:
                gi = emoji_img("🎁", 44 * s)
                c.alpha_composite(with_alpha(gi, out_cubic(ka)), (int(cx - bw / 2 + 24 * s), int(cy - gi.height / 2)))
                d.text((cx + 26 * s, cy), "Gift cards", font=font(F_XB, 36 * s), fill=(255, 255, 255, int(255 * out_cubic(ka))), anchor="mm")
    # product tiles
    for i, (ic, col) in enumerate([("🧁", (255, 222, 230)), ("🍪", (250, 232, 200)), ("🥐", (232, 240, 255))]):
        tx = 50 + i * ((w - 100 - 40) / 3 + 20)
        tw = (w - 100 - 40) / 3
        d.rounded_rectangle([tx, 590, tx + tw, h - 40], radius=26, fill=(*col, 255))
        ei = emoji_img(ic, 90)
        c.alpha_composite(ei, (int(tx + tw / 2 - ei.width / 2), int((590 + h - 40) / 2 - ei.height / 2)))
    if find:
        q, fs, found = find
        kf = p(t, fs, 0.3)
        if kf > 0:
            fw, fh = w - 80, 110
            fy = 540 + 20 * (1 - out_cubic(kf))
            d.rounded_rectangle([40, fy, 40 + fw, fy + fh], radius=24, fill=(30, 34, 46, int(250 * out_cubic(kf))))
            n = int(len(q) * p(t, fs + 0.25, 0.8))
            d.text((80, fy + fh / 2), "Find:", font=font(F_SEMI, 34), fill=(170, 176, 190, 255), anchor="lm")
            d.text((180, fy + fh / 2), q[:n], font=font(F_XB, 44), fill=(255, 255, 255, 255), anchor="lm")
            kr = p(t, fs + 1.25, 0.3)
            if kr > 0:
                lab = "1 of 1" if found else "0 results"
                col = GREEN if found else RED
                ff = font(F_XB, 34)
                tw = d.textlength(lab, font=ff) + 40
                d.rounded_rectangle([40 + fw - 24 - tw, fy + 26, 40 + fw - 24, fy + fh - 26], radius=29, fill=(*col, int(255 * out_cubic(kr))))
                d.text((40 + fw - 24 - tw / 2, fy + fh / 2), lab, font=ff, fill=(255, 255, 255, int(255 * out_cubic(kr))), anchor="mm")
    with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(top + 60 * (1 - out_cubic(k)))))


def gift_card(sub, t, start, cx, cy, shop, amount, color, emoji, w=720, h=430, rot=0.0, shine=True):
    k = p(t, start, 0.5)
    if k <= 0: return
    c = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(c)
    top, bot = np.array(color), np.array([max(0, v - 70) for v in color])
    for y in range(h):
        g = y / h
        d.line([0, y, w, y], fill=(*[int(v) for v in top * (1 - g) + bot * g], 255))
    mask = Image.new("L", (w, h), 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, w - 1, h - 1], radius=40, fill=255)
    c.putalpha(mask)
    d = ImageDraw.Draw(c)
    if shine:
        sx = int((t - start) * 500 % (w + 600)) - 300
        sh = Image.new("RGBA", (w, h), (0, 0, 0, 0))
        ImageDraw.Draw(sh).polygon([(sx, 0), (sx + 90, 0), (sx - 60, h), (sx - 150, h)], fill=(255, 255, 255, 70))
        sh.putalpha(Image.fromarray(np.minimum(np.array(sh.getchannel("A")), np.array(mask))))
        c.alpha_composite(sh)
    d.text((44, 60), "GIFT CARD", font=font(F_XB, 34), fill=(255, 255, 255, 230), anchor="lm")
    d.text((44, 140), shop, font=font(F_BLACK, 54), fill=(255, 255, 255, 255), anchor="lm")
    d.text((44, h - 70), amount, font=font(F_BLACK, 110), fill=(255, 255, 255, 255), anchor="lm")
    if w >= 700: d.text((w - 44, h - 60), "Buy online · send by email", font=font(F_SEMI, 26), fill=(255, 255, 255, 220), anchor="rm")
    e = emoji_img(emoji, 130)
    c.alpha_composite(e, (w - 44 - e.width, 40))
    s = 0.6 + 0.4 * out_back(k)
    c = c.resize((max(1, int(w * s)), max(1, int(h * s))), Image.LANCZOS)
    if rot:
        c = c.rotate(rot, resample=Image.BICUBIC, expand=True)
    with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(cx - c.width / 2), int(cy - c.height / 2)))


def site_row(sub, t, start, cy, emoji, color, site, has, flag_at, w=880, h=170):
    k = p(t, start, 0.4)
    if k <= 0: return
    lead = (not has) and t >= flag_at
    c, d = gbase(w, h, fill=(255, 255, 255))
    if lead:
        d.rounded_rectangle([0, 0, w - 1, h - 1], radius=40, outline=(*GOLD_C, 255), width=8)
    d.rounded_rectangle([28, 28, 142, 142], radius=28, fill=(*color, 255))
    e = emoji_img(emoji, 74)
    c.alpha_composite(e, (int(85 - e.width / 2), int(85 - e.height / 2)))
    d.text((170, 62), site, font=font(F_XB, 40), fill=(*INK, 255), anchor="lm")
    d.text((170, 116), "Find: “gift card”", font=font(F_SEMI, 30), fill=(*GREY, 255), anchor="lm")
    kf = p(t, flag_at, 0.35)
    if kf > 0:
        lab = "Has one" if has else "0 results"
        col = GREEN if has else RED
        ff = font(F_XB, 34)
        tw = d.textlength(lab, font=ff) + 44
        d.rounded_rectangle([w - 36 - tw, 58, w - 36, 112], radius=27, fill=(*col, int(255 * out_cubic(kf))))
        d.text((w - 36 - tw / 2, 85), lab, font=ff, fill=(255, 255, 255, int(255 * out_cubic(kf))), anchor="mm")
    with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2 + 60 * (1 - out_cubic(k))), int(cy - h / 2)))
    if lead:
        pass


GOLD_C = (255, 214, 92)


def night_clock(sub, t, start, cy, label="11:48 PM"):
    k = p(t, start, 0.4)
    if k <= 0: return
    place_emoji(sub, "🌙", W / 2 - 340, cy - 20 + 10 * math.sin(t * 3), 130, alpha=out_cubic(k))
    draw_text(sub, label, F_BLACK, 150, W / 2 + 70, cy, WHITE, alpha=out_cubic(k), scale=0.7 + 0.3 * out_back(k))
