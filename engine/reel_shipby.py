"""Helpers for the 2026-11-10 holiday 'order by' shipping-cutoff banner reels
(shop site with announcement bar + find, IG story graphic, Canva story editor, date-math card, lead rows)."""
from reel_flyer import *
from reel_portfolio import timer

PINE = (22, 120, 80)
BERRY = (220, 50, 70)


def story(c, d, x, y, w, a, acc, date="TUE · DEC 15", shop="Oak & Wick", emoji="🕯️"):
    """9:16 Instagram story graphic. a = 5 reveal amounts (bg, headline, date box, sub line, shop)."""
    h = w * 16 / 9
    base = (250, 246, 238)
    bgc = tuple(int(255 + (v - 255) * a[0]) for v in base)
    d.rectangle([x, y, x + w, y + h], fill=(*bgc, 255))
    if a[0] > 0:
        al = int(255 * a[0])
        d.rectangle([x, y, x + w, y + h * 0.42], fill=(*PINE, al))
        for i in range(14):
            rx = x + (i * 137) % int(w); ry = y + (i * 61) % int(h * 0.4)
            r = w * 0.012
            d.ellipse([rx - r, ry - r, rx + r, ry + r], fill=(255, 255, 255, int(170 * a[0])))
    if a[1] > 0:
        al = int(255 * a[1])
        d.text((x + w / 2, y + h * 0.13), "LAST DAY", font=font(F_BLACK, w * 0.17), fill=(255, 255, 255, al), anchor="mm")
        d.text((x + w / 2, y + h * 0.22), "TO ORDER", font=font(F_BLACK, w * 0.17), fill=(255, 255, 255, al), anchor="mm")
        d.text((x + w / 2, y + h * 0.31), "FOR CHRISTMAS", font=font(F_BLACK, w * 0.095), fill=(*GOLD_C, al), anchor="mm")
    if a[2] > 0:
        al = int(255 * a[2])
        bw = w * 0.82 * (0.7 + 0.3 * out_back(min(1, a[2])))
        d.rounded_rectangle([x + w / 2 - bw / 2, y + h * 0.47, x + w / 2 + bw / 2, y + h * 0.58], radius=w * 0.05, fill=(*BERRY, al))
        d.text((x + w / 2, y + h * 0.525), date, font=font(F_BLACK, w * 0.095), fill=(255, 255, 255, al), anchor="mm")
    if a[3] > 0:
        e = with_alpha(emoji_img("🎁", int(w * 0.2 * (0.6 + 0.4 * a[3]))).copy(), a[3])
        c.alpha_composite(e, (int(x + w / 2 - e.width / 2), int(y + h * 0.68 - e.height / 2)))
        d.text((x + w / 2, y + h * 0.78), "US orders · arrives by Dec 25", font=font(F_XB, w * 0.052), fill=(*INK, int(255 * a[3])), anchor="mm")
    if a[4] > 0:
        al = int(255 * a[4])
        d.text((x + w / 2, y + h * 0.88), f"{shop.upper()}", font=font(F_BLACK, w * 0.07), fill=(*PINE, al), anchor="mm")
        d.text((x + w / 2, y + h * 0.93), "Shop now · link in bio", font=font(F_SEMI, w * 0.045), fill=(*GREY, al), anchor="mm")


def story_card(sub, t, start, cx, cy, acc, w=400, rot=0.0, steps=None, **kw):
    k = p(t, start, 0.45)
    if k <= 0: return
    h = int(w * 16 / 9)
    pad = 30
    c = Image.new("RGBA", (w + 2 * pad, h + 2 * pad), (0, 0, 0, 0))
    d = ImageDraw.Draw(c)
    d.rounded_rectangle([pad + 8, pad + 14, pad + w + 8, pad + h + 14], radius=28, fill=(0, 0, 0, 90))
    a = [out_cubic(p(t, s, 0.45)) for s in steps] if steps else [1] * 5
    st = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    story(st, ImageDraw.Draw(st), 0, 0, w, a, acc, **kw)
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


def shop_site(sub, t, start, top, url, shop, emoji, color, bar_at=None, bar_text="🎄 Order by Tue Dec 15 for Christmas delivery",
              type_bar=False, find=None, w=880, h=700, tiles=(("🕯️", (250, 232, 200)), ("🧴", (232, 240, 255)), ("🎁", (255, 222, 230)))):
    """Online shop homepage. bar_at: time the holiday cutoff bar drops in at the top (typed if type_bar).
    find: (query, start, found)."""
    k = p(t, start, 0.4)
    if k <= 0: return
    c, d = gbase(w, h, fill=(255, 255, 255))
    d.rounded_rectangle([0, 0, w - 1, 110], radius=40, fill=(232, 235, 242, 255))
    d.rectangle([0, 70, w - 1, 110], fill=(232, 235, 242, 255))
    for i, col in enumerate([(255, 95, 86), (255, 189, 46), (39, 201, 63)]):
        d.ellipse([34 + i * 40, 40, 58 + i * 40, 64], fill=(*col, 255))
    d.rounded_rectangle([170, 26, w - 40, 84], radius=29, fill=(255, 255, 255, 255))
    d.text((210, 55), url, font=font(F_SEMI, 32), fill=(70, 76, 90, 255), anchor="lm")
    yb = 110
    if bar_at is not None:
        kb = out_cubic(p(t, bar_at, 0.4))
        if kb > 0:
            bh = 84 * kb
            d.rectangle([0, yb, w - 1, yb + bh], fill=(*BERRY, 255))
            txt = bar_text
            if type_bar:
                txt = bar_text[:int(len(bar_text) * p(t, bar_at + 0.3, 1.3))]
            if kb > 0.6:
                ff = font(F_XB, 32)
                # emoji in DejaVu-free way: draw tree emoji separately
                body = txt.replace("🎄 ", "")
                e = emoji_img("🎄", 40)
                tw = d.textlength(bar_text.replace("🎄 ", ""), font=ff) + 52
                x0 = w / 2 - tw / 2
                if txt.startswith("🎄"):
                    c.alpha_composite(e, (int(x0), int(yb + bh / 2 - e.height / 2)))
                d.text((x0 + 52, yb + bh / 2), body, font=ff, fill=(255, 255, 255, 255), anchor="lm")
            yb += bh
    hero_h = 260
    d.rectangle([0, yb, w - 1, yb + hero_h], fill=(*color, 255))
    e = emoji_img(emoji, 120)
    c.alpha_composite(e, (60, int(yb + hero_h / 2 - e.height / 2)))
    d.text((210, yb + hero_h / 2 - 32), shop, font=font(F_BLACK, 58), fill=(*INK, 255), anchor="lm")
    d.text((212, yb + hero_h / 2 + 38), "Handmade gifts · ships US", font=font(F_SEMI, 32), fill=(60, 66, 80, 255), anchor="lm")
    ny = yb + hero_h + 55
    f = font(F_XB, 36)
    x = 50
    for item in ["Shop", "Gifts", "About", "FAQ"]:
        d.text((x, ny), item, font=f, fill=(*INK, 255), anchor="lm")
        x += d.textlength(item, font=f) + 46
    ty = ny + 60
    if ty < h - 100:
        for i, (ic, col) in enumerate(tiles):
            tw = (w - 100 - 40) / 3
            tx = 50 + i * (tw + 20)
            d.rounded_rectangle([tx, ty, tx + tw, h - 40], radius=26, fill=(*col, 255))
            ei = emoji_img(ic, 84)
            c.alpha_composite(ei, (int(tx + tw / 2 - ei.width / 2), int((ty + h - 40) / 2 - ei.height / 2)))
    if find:
        q, fs, found = find
        kf = p(t, fs, 0.3)
        if kf > 0:
            fw, fh = w - 80, 110
            fy = ny - 40 + 20 * (1 - out_cubic(kf))
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


def date_math(sub, t, start, top, acc, rows, result, result_at, w=880):
    """rows: (emoji, label, value, appear_time). result: (label, value)."""
    k = p(t, start, 0.4)
    if k <= 0: return
    row_h = 130
    h = 60 + row_h * len(rows) + 170
    c, d = card_base(w, h)
    y = 40
    for i, (ic, lab, val, at) in enumerate(rows):
        kk = out_cubic(p(t, at, 0.35))
        if kk > 0:
            al = int(255 * kk)
            dx = int(50 * (1 - kk))
            e = with_alpha(emoji_img(ic, 64).copy(), kk)
            c.alpha_composite(e, (40 + dx, int(y + row_h / 2 - e.height / 2)))
            d.text((130 + dx, y + row_h / 2), lab, font=font(F_SEMI, 38), fill=(60, 66, 80, al), anchor="lm")
            d.text((w - 44, y + row_h / 2), val, font=font(F_BLACK, 46), fill=(*INK, al), anchor="rm")
        d.line([40, y + row_h, w - 40, y + row_h], fill=(*LINE, 255), width=3)
        y += row_h
    kr = p(t, result_at, 0.4)
    if kr > 0:
        al = int(255 * out_cubic(kr))
        s = out_back(kr)
        d.rounded_rectangle([30, y + 25, w - 30, y + 145], radius=34, fill=(*acc, al))
        d.text((70, y + 85), result[0], font=font(F_XB, 44), fill=(*INK, al), anchor="lm")
        d.text((w - 70, y + 85), result[1], font=font(F_BLACK, int(58 * max(0.3, s))), fill=(*INK, al), anchor="rm")
    with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(top + 60 * (1 - out_cubic(k)))))


def canva_story(sub, t, start, cy, acc, steps, w=880, h=1100, labels=None, **kw):
    """Canva-style editor whose 9:16 canvas builds the story over steps[0..4]."""
    k = p(t, start, 0.45)
    if k <= 0: return
    c, d = card_base(w, h, radius=36, fill=(236, 239, 245, 255))
    d.rounded_rectangle([0, 0, w - 1, 100], radius=36, fill=(110, 70, 230, 255))
    d.rectangle([0, 60, w - 1, 100], fill=(110, 70, 230, 255))
    d.text((40, 52), "Instagram Story · 1080 x 1920", font=font(F_XB, 30), fill=(255, 255, 255, 255), anchor="lm")
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
    sw = 480
    x, y = 160 + (680 - sw) // 2, 125
    d.rectangle([x - 4, y - 4, x + sw + 4, y + sw * 16 / 9 + 4], fill=(210, 214, 222, 255))
    a = [out_cubic(p(t, st, 0.45)) for st in steps]
    story(c, d, x, y, sw, a, acc, **kw)
    if labels and n > 0:
        kk = out_cubic(p(t, steps[n - 1], 0.3))
        d.rounded_rectangle([140, h - 120, w - 40, h - 26], radius=30, fill=(255, 255, 255, 255))
        d.text(((140 + w - 40) / 2, h - 73), labels[n - 1], font=font(F_XB, 38), fill=(*INK, int(255 * kk)), anchor="mm")
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(cy - h / 2 + 60 * (1 - out_cubic(k)))))


def lead_row(sub, t, start, cy, emoji, color, site, has, flag_at, query="order by", w=880, h=170):
    k = p(t, start, 0.4)
    if k <= 0: return
    lead = (not has) and t >= flag_at + 0.4
    c, d = gbase(w, h, fill=(255, 255, 255))
    if lead:
        d.rounded_rectangle([0, 0, w - 1, h - 1], radius=40, outline=(*GOLD_C, 255), width=8)
    d.rounded_rectangle([28, 28, 142, 142], radius=28, fill=(*color, 255))
    e = emoji_img(emoji, 74)
    c.alpha_composite(e, (int(85 - e.width / 2), int(85 - e.height / 2)))
    d.text((170, 62), site, font=font(F_XB, 40), fill=(*INK, 255), anchor="lm")
    d.text((170, 116), f"Find: “{query}”", font=font(F_SEMI, 30), fill=(*GREY, 255), anchor="lm")
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
