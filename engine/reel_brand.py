"""Helpers for the 2026-11-18 'brand style guide side gig' reels
(1-page brand guide sheet, Canva-style editor that builds it, messy vs consistent
Instagram grid, eyedropper hex picker). Shop names are fictional samples."""
from reel_resume import *

BRAND = dict(name="Maple & Co.", kind="Bakery", emoji="🥐",
             colors=[((122, 62, 43), "#7A3E2B", "Main"), ((242, 201, 140), "#F2C98C", "Accent"), ((250, 244, 234), "#FAF4EA", "Background")],
             fonts=[("Headline", F_BLACK, "Bold Sans"), ("Body", F_MED, "Inter")])

MESSY = [((230, 60, 140), "SALE!", F_BLACK), ((40, 120, 230), "new", F_MED), ((255, 200, 0), "Hello", F_XB),
         ((20, 170, 120), "OPEN", F_SEMI), ((150, 60, 200), "Treats", F_BLACK), ((240, 110, 40), "fall", F_MED),
         ((30, 30, 30), "LOVE", F_XB), ((90, 210, 230), "yum", F_SEMI), ((200, 30, 40), "BOGO", F_BLACK)]


def brand_sheet(c, d, x, y, w, a, brand=BRAND):
    """1-page brand guide. a = [logo, colors, fonts, do/don't] alphas."""
    a = list(a) + [1.0] * (4 - len(a))
    h = int(w * 11 / 8.5)
    d.rectangle([x, y, x + w, y + h], fill=(255, 255, 255, 255))
    s = w / 700
    m = 50 * s
    main = brand["colors"][0][0]
    d.text((x + m, y + 50 * s), "BRAND GUIDE", font=font(F_BLACK, 30 * s), fill=(*GREY, 255), anchor="lm")
    d.text((x + w - m, y + 50 * s), "1 page", font=font(F_SEMI, 24 * s), fill=(*GREY, 255), anchor="rm")
    yy = y + 90 * s
    if a[0] > 0:  # logo block
        al = int(255 * a[0])
        d.rounded_rectangle([x + m, yy, x + w - m, yy + 170 * s], radius=20 * s, fill=(*brand["colors"][2][0], al))
        d.ellipse([x + m + 30 * s, yy + 25 * s, x + m + 150 * s, yy + 145 * s], fill=(*main, al))
        e = emoji_img(brand["emoji"], int(70 * s))
        c.alpha_composite(with_alpha(e, a[0]), (int(x + m + 90 * s - e.width / 2), int(yy + 85 * s - e.height / 2)))
        d.text((x + m + 180 * s, yy + 68 * s), brand["name"], font=font(F_BLACK, 52 * s), fill=(*main, al), anchor="lm")
        d.text((x + m + 182 * s, yy + 118 * s), brand["kind"].upper(), font=font(F_XB, 26 * s), fill=(*GREY, al), anchor="lm")
    yy += 200 * s
    if a[1] > 0:  # colors
        al = int(255 * a[1])
        d.text((x + m, yy), "COLORS", font=font(F_BLACK, 26 * s), fill=(*main, al), anchor="lm")
        sw = (w - 2 * m - 40 * s) / 3
        for i, (col, hx, lab) in enumerate(brand["colors"]):
            sx = x + m + i * (sw + 20 * s)
            d.rounded_rectangle([sx, yy + 30 * s, sx + sw, yy + 150 * s], radius=16 * s, fill=(*col, al), outline=(220, 222, 228, al), width=max(1, int(2 * s)))
            d.text((sx + 8 * s, yy + 176 * s), hx, font=font(F_XB, 26 * s), fill=(*INK, al), anchor="lm")
            d.text((sx + 8 * s, yy + 208 * s), lab, font=font(F_MED, 22 * s), fill=(*GREY, al), anchor="lm")
    yy += 250 * s
    if a[2] > 0:  # fonts
        al = int(255 * a[2])
        d.text((x + m, yy), "FONTS", font=font(F_BLACK, 26 * s), fill=(*main, al), anchor="lm")
        for i, (lab, fp, nm) in enumerate(brand["fonts"]):
            fy = yy + (60 + i * 70) * s
            d.text((x + m, fy), "Aa", font=font(fp, 48 * s), fill=(*INK, al), anchor="lm")
            d.text((x + m + 100 * s, fy), f"{lab}: {nm}", font=font(F_SEMI, 30 * s), fill=(*INK, al), anchor="lm")
    yy += 210 * s
    if a[3] > 0:  # do / don't
        al = int(255 * a[3])
        hw = (w - 2 * m - 20 * s) / 2
        for i, (lab, col, txt) in enumerate([("DO", OKG, "Logo on cream"), ("DON'T", RED2, "Stretch the logo")]):
            bx = x + m + i * (hw + 20 * s)
            d.rounded_rectangle([bx, yy, bx + hw, yy + 120 * s], radius=16 * s, outline=(*col, al), width=max(2, int(4 * s)))
            d.text((bx + 20 * s, yy + 36 * s), lab, font=font(F_BLACK, 28 * s), fill=(*col, al), anchor="lm")
            d.text((bx + 20 * s, yy + 84 * s), txt, font=font(F_SEMI, 24 * s), fill=(*INK, al), anchor="lm")
    return h


def guide_card(sub, t, start, cx, cy, w=560, rot=0.0, steps=None, label=None, label_col=None):
    k = p(t, start, 0.45)
    if k <= 0: return
    h = int(w * 11 / 8.5)
    pad = 30
    c = Image.new("RGBA", (w + 2 * pad, h + 2 * pad), (0, 0, 0, 0))
    d = ImageDraw.Draw(c)
    d.rectangle([pad + 12, pad + 16, pad + w + 12, pad + h + 16], fill=(0, 0, 0, 80))
    a = [out_cubic(p(t, s, 0.45)) for s in steps] if steps else [1] * 4
    brand_sheet(c, d, pad, pad, w, a)
    s = 0.6 + 0.4 * out_back(k)
    c = c.resize((max(1, int(c.width * s)), max(1, int(c.height * s))), Image.LANCZOS)
    if rot: c = c.rotate(rot, resample=Image.BICUBIC, expand=True)
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(cx - c.width / 2), int(cy - c.height / 2)))
    if label:
        pill(sub, cx, cy - c.height / 2 - 6, label, F_BLACK, 40, label_col or GOLD_C, WHITE if label_col else INK, alpha=out_cubic(k))


def canva_guide(sub, t, start, cy, steps, labels=None, w=880, h=1140, acc=(125, 42, 232)):
    """Canva-style editor window building the brand guide over steps[0..3]."""
    k = p(t, start, 0.45)
    if k <= 0: return
    c, d = gbase(w, h, fill=(236, 238, 244), radius=36)
    d.rounded_rectangle([0, 0, w - 1, 110], radius=36, fill=(*acc, 255))
    d.rectangle([0, 70, w - 1, 110], fill=(*acc, 255))
    d.text((40, 56), "Brand guide – sample", font=font(F_XB, 34), fill=(255, 255, 255, 255), anchor="lm")
    d.rounded_rectangle([w - 200, 28, w - 34, 84], radius=28, fill=(255, 255, 255, 255))
    d.text((w - 117, 56), "Share", font=font(F_XB, 28), fill=(*acc, 255), anchor="mm")
    pw = 600
    x, y = (w - pw) // 2, 140
    ph = int(pw * 11 / 8.5)
    d.rectangle([x - 3, y - 3, x + pw + 3, y + ph + 3], fill=(205, 209, 218, 255))
    a = [out_cubic(p(t, st, 0.45)) for st in steps]
    brand_sheet(c, d, x, y, pw, a)
    n = sum(1 for s in steps if t >= s)
    if labels and n > 0:
        kk = out_cubic(p(t, steps[n - 1], 0.3))
        d.rounded_rectangle([60, h - 110, w - 60, h - 20], radius=30, fill=(255, 255, 255, 255), outline=(*acc, 255), width=4)
        d.text((w / 2, h - 65), labels[n - 1], font=font(F_XB, 40), fill=(*INK, int(255 * kk)), anchor="mm")
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(cy - h / 2 + 60 * (1 - out_cubic(k)))))


def tile(d, x, y, sz, col, word, fp, bg=None, emoji=None, c=None):
    d.rounded_rectangle([x, y, x + sz, y + sz], radius=14, fill=(*(bg or col), 255))
    fg = (255, 255, 255) if bg is None else col
    d.text((x + sz / 2, y + sz / 2 + (30 if emoji else 0)), word, font=font(fp, sz * 0.22), fill=(*fg, 255), anchor="mm")
    if emoji and c is not None:
        e = emoji_img(emoji, int(sz * 0.32))
        c.alpha_composite(e, (int(x + sz / 2 - e.width / 2), int(y + sz * 0.3 - e.height / 2)))


def ig_grid(sub, t, start, cy, handle="@mapleandco", consistent_at=None, flags=None, flag_at=None, w=860, every=0.08):
    """Instagram-profile grid: 9 messy posts; at consistent_at they flip to on-brand posts."""
    k = p(t, start, 0.4)
    if k <= 0: return
    hdr = 150
    gap = 10
    sz = (w - 2 * 30 - 2 * gap) // 3
    h = hdr + 3 * sz + 2 * gap + 40
    c, d = gbase(w, h, fill=(255, 255, 255), radius=36)
    d.ellipse([30, 30, 120, 120], fill=(*BRAND["colors"][0][0], 255))
    e = emoji_img(BRAND["emoji"], 52); c.alpha_composite(e, (75 - e.width // 2, 75 - e.height // 2))
    d.text((144, 58), handle, font=font(F_XB, 38), fill=(*INK, 255), anchor="lm")
    d.text((144, 100), "Bakery · sample account", font=font(F_MED, 28), fill=(*GREY, 255), anchor="lm")
    kc = p(t, consistent_at, 0.01) if consistent_at is not None else 0
    words_good = ["Fresh", "Pie", "Open", "Hours", "Treats", "Order", "Cozy", "Gift", "Thanks"]
    emo_good = ["🥐", "🥧", "☕", "🕗", "🍪", "📦", "🍂", "🎁", "💛"]
    for i in range(9):
        r, cc = divmod(i, 3)
        x = 30 + cc * (sz + gap); y = hdr + r * (sz + gap)
        ki = p(t, start + 0.2 + i * every, 0.3)
        if ki <= 0: continue
        flip = consistent_at is not None and t >= consistent_at + i * 0.07
        if flip:
            main, acc2, bgc = [col for col, _, _ in BRAND["colors"]]
            tile(d, x, y, sz, main, words_good[i], F_BLACK, bg=(bgc if i % 2 == 0 else acc2), emoji=emo_good[i], c=c)
        else:
            col, wd, fp = MESSY[i]
            tile(d, x, y, sz, col, wd, fp)
    c = with_alpha(c, out_cubic(k))
    x0, y0 = int(W / 2 - w / 2), int(cy - h / 2 + 60 * (1 - out_cubic(k)))
    sub.alpha_composite(c, (x0, y0))
    if flags and flag_at is not None:
        for i, (txt, fy) in enumerate(flags):
            kf = p(t, flag_at + i * 0.6, 0.35)
            if kf <= 0: continue
            pill(sub, W / 2, y0 + fy, txt, F_BLACK, 44, RED2, WHITE, alpha=out_cubic(kf), scale=out_back(kf), icon="❌")


def hex_picker(sub, t, start, cy, acc, w=860, h=560):
    """Eyedropper over a logo → swatch + hex code typing in."""
    k = p(t, start, 0.4)
    if k <= 0: return
    c, d = gbase(w, h, fill=(255, 255, 255), radius=36)
    d.text((40, 60), "Color picker", font=font(F_XB, 38), fill=(*INK, 255), anchor="lm")
    main = BRAND["colors"][0][0]
    d.ellipse([60, 140, 340, 420], fill=(*main, 255))
    e = emoji_img(BRAND["emoji"], 150); c.alpha_composite(e, (200 - e.width // 2, 280 - e.height // 2))
    kd = in_out(p(t, start + 0.6, 0.9))
    ex, ey = lerp(560, 120, kd), lerp(470, 190, kd)
    ks = p(t, start + 1.6, 0.4)
    if ks > 0:
        al = int(255 * out_cubic(ks))
        d.rounded_rectangle([420, 150, 800, 290], radius=22, fill=(*main, al))
        hx = BRAND["colors"][0][1]
        n = int(len(hx) * p(t, start + 1.9, 0.8))
        d.rounded_rectangle([420, 320, 800, 410], radius=20, fill=(244, 245, 250, al), outline=(*acc, al), width=4)
        d.text((450, 365), hx[:n], font=font(F_BLACK, 52), fill=(*INK, al), anchor="lm")
        d.text((40, 490), "Copy the code into your guide", font=font(F_SEMI, 34), fill=(*GREY, al), anchor="lm")
    c.alpha_composite(emoji_img("🖌️", 90), (int(ex), int(ey) - 80))
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(cy - h / 2 + 60 * (1 - out_cubic(k)))))
