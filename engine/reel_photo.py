"""Product-photo mocks for Learn & Earn holiday photo reels (2026-10-23): candle shots, photo cards, camera UI, window setup."""
from reel_chat import *

GREEN = (60, 210, 130)
RED_X = (255, 92, 104)


def mix(a, b, k):
    return tuple(int(lerp(x, y, k)) for x, y in zip(a, b))


def candle(c, d, x, y, sz, mode="hero"):
    """Draw a candle-jar product photo into canvas c at (x,y), square size sz.
    modes: dark, flash, hero, close, gift."""
    bgc = {"dark": (72, 64, 60), "flash": (40, 38, 44), "hero": (250, 246, 240), "close": (244, 236, 226), "gift": (246, 232, 214)}[mode]
    d.rounded_rectangle([x, y, x + sz, y + sz], radius=int(sz * 0.07), fill=(*bgc, 255))
    if mode == "dark":
        d.rectangle([x + sz * .08, y + sz * .62, x + sz * .28, y + sz * .9], fill=(96, 82, 72, 255))
        d.ellipse([x + sz * .7, y + sz * .12, x + sz * .9, y + sz * .32], fill=(108, 98, 90, 255))
    if mode == "close":
        # zoomed jar fills the frame: big label + wax texture
        d.rounded_rectangle([x + sz * .12, y + sz * .1, x + sz * .88, y + sz * 1.0], radius=int(sz * .06), fill=(255, 255, 255, 255), outline=(214, 204, 192, 255), width=4)
        d.rectangle([x + sz * .12, y + sz * .42, x + sz * .88, y + sz * .7], fill=(200, 60, 70, 255))
        d.text((x + sz * .5, y + sz * .52), "PINE", font=font(F_BLACK, sz * .13), fill=(255, 255, 255, 255), anchor="mm")
        d.text((x + sz * .5, y + sz * .63), "hand-poured soy", font=font(F_SEMI, sz * .055), fill=(255, 230, 230, 255), anchor="mm")
        for i in range(5):
            yy = y + sz * (.18 + i * .04)
            d.arc([x + sz * .2, yy, x + sz * .8, yy + sz * .06], 0, 180, fill=(232, 222, 210, 255), width=3)
        return
    jar = {"dark": (122, 112, 102), "flash": (255, 255, 255)}.get(mode, (255, 255, 255))
    lab = {"dark": (92, 82, 76)}.get(mode, (200, 60, 70))
    if mode == "flash":  # hard black shadow to the right
        d.rounded_rectangle([x + sz * .44, y + sz * .44, x + sz * .80, y + sz * .86], radius=int(sz * .05), fill=(8, 8, 10, 255))
    if mode in ("hero", "gift"):  # soft shadow
        d.ellipse([x + sz * .28, y + sz * .78, x + sz * .76, y + sz * .88], fill=(*mix(bgc, (150, 140, 130), .5), 255))
    d.rounded_rectangle([x + sz * .34, y + sz * .4, x + sz * .66, y + sz * .82], radius=int(sz * .05), fill=(*jar, 255), outline=(200, 190, 180, 255), width=3)
    d.rectangle([x + sz * .34, y + sz * .55, x + sz * .66, y + sz * .67], fill=(*lab, 255))
    d.line([x + sz * .5, y + sz * .4, x + sz * .5, y + sz * .33], fill=(60, 50, 40, 255), width=max(2, int(sz * .012)))
    if mode == "flash":  # blown-out glare
        d.ellipse([x + sz * .38, y + sz * .43, x + sz * .5, y + sz * .53], fill=(255, 255, 255, 255))
        d.ellipse([x + sz * .4, y + sz * .45, x + sz * .48, y + sz * .51], fill=(255, 255, 230, 255))
    if mode in ("hero", "gift"):
        e = emoji_img("🔥", max(4, int(sz * .1)))
        c.alpha_composite(e, (int(x + sz * .5 - e.width / 2), int(y + sz * .33 - e.height)))
    if mode == "gift":
        for ch, px, py, s in [("🎁", .06, .6, .26), ("🌲", .72, .5, .26), ("✨", .74, .12, .14), ("🎀", .1, .14, .14)]:
            e = emoji_img(ch, max(4, int(sz * s)))
            c.alpha_composite(e, (int(x + sz * px), int(y + sz * py)))


def photo_card(sub, t, start, cx, cy, sz, mode, tag=None, tag_color=(255, 214, 92), rot=0.0, from_dx=0):
    """Polaroid-style photo that pops in."""
    k = p(t, start, 0.45)
    if k <= 0: return
    pad = int(sz * .06)
    th = int(sz * .2) if tag else pad
    c = Image.new("RGBA", (sz + 2 * pad, sz + pad + th), (0, 0, 0, 0))
    d = ImageDraw.Draw(c)
    d.rounded_rectangle([0, 0, c.width - 1, c.height - 1], radius=int(sz * .06), fill=(255, 255, 255, 255))
    candle(c, d, pad, pad, sz, mode)
    if tag:
        d.text((c.width / 2, sz + pad + th / 2), tag, font=font(F_BLACK, sz * .1), fill=(*INK, 255), anchor="mm")
        d.rounded_rectangle([c.width / 2 - sz * .3, sz + pad + th - 14, c.width / 2 + sz * .3, sz + pad + th - 6], radius=4, fill=(*tag_color, 255))
    s = out_back(k)
    if rot or s != 1:
        c = c.resize((max(1, int(c.width * s)), max(1, int(c.height * s))), Image.LANCZOS)
        if rot: c = c.rotate(rot, resample=Image.BICUBIC, expand=True)
    with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(cx - c.width / 2 + from_dx * (1 - out_cubic(k))), int(cy - c.height / 2)))


def camera_ui(sub, t, start, cx, top, mode="hero", focus_at=None, shot_at=None, w=640, h=1000):
    """Phone camera app: viewfinder with product, 1x/2x pill, shutter; optional tap-to-focus + AE/AF lock + shutter flash."""
    k = p(t, start, 0.45)
    if k <= 0: return
    c = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(c)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=64, fill=(14, 15, 20, 255), outline=(80, 86, 104, 255), width=6)
    vf = w - 60
    vy = 130
    candle(c, d, 30, vy, vf, mode)
    # grid lines
    for i in (1, 2):
        d.line([30 + vf * i / 3, vy, 30 + vf * i / 3, vy + vf], fill=(255, 255, 255, 70), width=2)
        d.line([30, vy + vf * i / 3, 30 + vf, vy + vf * i / 3], fill=(255, 255, 255, 70), width=2)
    d.text((w / 2, 70), "PHOTO", font=font(F_XB, 30), fill=(255, 204, 0, 255), anchor="mm")
    # zoom pills
    zy = vy + vf + 60
    for i, z in enumerate(["1x", "2x"]):
        zx = w / 2 - 50 + i * 100
        on = z == "2x"
        d.ellipse([zx - 36, zy - 36, zx + 36, zy + 36], fill=((255, 204, 0, 255) if on else (50, 52, 60, 255)))
        d.text((zx, zy), z, font=font(F_XB, 28), fill=((20, 20, 20, 255) if on else (230, 230, 230, 255)), anchor="mm")
    sy = h - 110
    d.ellipse([w / 2 - 62, sy - 62, w / 2 + 62, sy + 62], outline=(255, 255, 255, 255), width=8)
    pressed = shot_at is not None and 0 < t - shot_at < 0.25
    r = 44 if pressed else 50
    d.ellipse([w / 2 - r, sy - r, w / 2 + r, sy + r], fill=(255, 255, 255, 255))
    if focus_at is not None:
        kf = p(t, focus_at, 0.35)
        if kf > 0:
            fx, fy = 30 + vf * .5, vy + vf * .6
            s = lerp(150, 110, out_cubic(kf))
            d.rectangle([fx - s, fy - s, fx + s, fy + s], outline=(255, 204, 0, int(255 * out_cubic(kf))), width=5)
            if t > focus_at + 0.6:
                d.rounded_rectangle([w / 2 - 130, vy + 24, w / 2 + 130, vy + 76], radius=10, fill=(255, 204, 0, 255))
                d.text((w / 2, vy + 50), "AE/AF LOCK", font=font(F_XB, 30), fill=(20, 20, 20, 255), anchor="mm")
    if shot_at is not None:
        kfl = p(t, shot_at, 0.3)
        if 0 < kfl < 1:
            d.rectangle([30, vy, 30 + vf, vy + vf], fill=(255, 255, 255, int(200 * (1 - kfl))))
    with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(cx - w / 2), int(top + 60 * (1 - out_cubic(k)))))


def window_setup(sub, t, start, cy, acc):
    """Top-down setup diagram: window on the left with light rays -> product -> white card on the right; phone at bottom."""
    k = p(t, start, 0.4)
    if k <= 0: return
    c = Image.new("RGBA", (860, 560), (0, 0, 0, 0))
    d = ImageDraw.Draw(c)
    d.rounded_rectangle([0, 0, 859, 559], radius=40, fill=(250, 251, 255, 255))
    d.text((430, 46), "TOP VIEW", font=font(F_XB, 30), fill=(130, 136, 150, 255), anchor="mm")
    # window
    d.rounded_rectangle([40, 110, 90, 450], radius=10, fill=(150, 210, 255, 255), outline=(90, 150, 220, 255), width=4)
    d.text((65, 490), "Window", font=font(F_XB, 30), fill=(*INK, 255), anchor="mm")
    # rays
    kr = p(t, start + 0.4, 0.8)
    for i in range(5):
        yy = 150 + i * 65
        x1 = lerp(100, 360, out_cubic(kr))
        d.line([100, yy, x1, 280 + (yy - 280) * .4], fill=(255, 200, 60, int(220 * out_cubic(kr))), width=6)
    # product
    d.ellipse([370, 230, 470, 330], fill=(200, 60, 70, 255))
    d.text((420, 370), "Product", font=font(F_XB, 30), fill=(*INK, 255), anchor="mm")
    # white card
    kw = p(t, start + 1.2, 0.4)
    if kw > 0:
        xo = 80 * (1 - out_cubic(kw))
        d.rounded_rectangle([700 + xo, 130, 740 + xo, 430], radius=8, fill=(255, 255, 255, int(255 * kw)), outline=(*acc, int(255 * kw)), width=5)
        d.text((720 + xo, 490), "White paper", font=font(F_XB, 30), fill=(*INK, int(255 * kw)), anchor="mm")
        kb = p(t, start + 1.6, 0.6)
        for i in range(3):
            yy = 220 + i * 60
            d.line([690, yy, lerp(690, 490, out_cubic(kb)), 280], fill=(255, 220, 120, int(160 * out_cubic(kb))), width=4)
    with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - 430), int(cy - 280 + 50 * (1 - out_cubic(k)))))
    kp = p(t, start + 2.2, 0.4)
    place_emoji(sub, "📱", W / 2, cy + 230, 120 * out_back(kp), alpha=out_cubic(kp))


def shot_row(sub, t, start, cy, mode, num, title, desc, color, w=880, h=250):
    """Horizontal card: photo thumbnail left, numbered title + description right; slides in."""
    k = p(t, start, 0.45)
    if k <= 0: return
    c = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(c)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=34, fill=(250, 251, 255, 255))
    candle(c, d, 24, 24, h - 48, mode)
    tx = h + 10
    d.rounded_rectangle([tx, 34, tx + 64, 98], radius=32, fill=(*color, 255))
    d.text((tx + 32, 66), str(num), font=font(F_BLACK, 40), fill=(*INK, 255), anchor="mm")
    d.text((tx + 84, 66), title, font=font(F_BLACK, 50), fill=(*INK, 255), anchor="lm")
    for i, l in enumerate(textwrap.wrap(desc, 26)[:2]):
        d.text((tx, 146 + i * 48), l, font=font(F_SEMI, 38), fill=(80, 86, 100, 255), anchor="lm")
    with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2 + 300 * (1 - out_cubic(k))), int(cy - h / 2)))
