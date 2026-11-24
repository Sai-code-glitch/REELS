"""Helpers for the 2026-11-24 'link-in-bio page gig for small shops' reels.
Instagram profile with a bio link, tap -> dead-end browser page, Linktree-style link page builder,
lead rows. All shops/handles shown are generic samples."""
from reel_insert import *

RED = (235, 64, 52)
OKG = (40, 170, 100)


def bio_profile(sub, t, start, top, acc, handle="@pineandwick", emoji="🕯️", color=(255, 214, 170),
                link="pineandwick.com/summer-sale", tap_at=None, w=880, h=560):
    """Profile header + bio + link line. At tap_at a finger taps the link (link pulses)."""
    k = p(t, start, 0.45)
    if k <= 0: return
    c, d = card_base(w, h, radius=40, fill=(255, 255, 255, 255))
    ring_avatar(c, d, 120, 130, 72, emoji, color)
    d.text((240, 92), handle, font=font(F_BLACK, 44), fill=(*INK, 255), anchor="lm")
    for i, (n, lab) in enumerate([("318", "posts"), ("2,140", "followers"), ("402", "following")]):
        x = 260 + i * 200
        d.text((x, 160), n, font=font(F_BLACK, 38), fill=(*INK, 255), anchor="mm")
        d.text((x, 200), lab, font=font(F_SEMI, 28), fill=(*GREY, 255), anchor="mm")
    d.text((48, 280), "Hand-poured candles", font=font(F_XB, 38), fill=(*INK, 255), anchor="lm")
    d.text((48, 335), "Gifts ship fast · Shop below", font=font(F_SEMI, 34), fill=(*INK, 255), anchor="lm")
    kt = p(t, tap_at, 0.5) if tap_at is not None else 0
    pulse = 1 + 0.08 * math.sin(kt * math.pi) if 0 < kt < 1 else 1
    e = emoji_img("🔗", 36)
    c.alpha_composite(e, (48, int(395 - e.height / 2)))
    d.text((96, 395), link, font=font(F_XB, 36 * pulse), fill=(56, 100, 220, 255), anchor="lm")
    d.rounded_rectangle([40, 450, w / 2 - 10, 520], radius=18, fill=(236, 238, 243, 255))
    d.rounded_rectangle([w / 2 + 10, 450, w - 40, 520], radius=18, fill=(236, 238, 243, 255))
    d.text((w / 4 + 15, 485), "Follow", font=font(F_XB, 32), fill=(*INK, 255), anchor="mm")
    d.text((3 * w / 4 - 15, 485), "Message", font=font(F_XB, 32), fill=(*INK, 255), anchor="mm")
    c = with_alpha(c, out_cubic(k))
    x0, y0 = int(W / 2 - w / 2), int(top + 70 * (1 - out_cubic(k)))
    sub.alpha_composite(c, (x0, y0))
    if tap_at is not None and t >= tap_at - 0.5:
        kf = p(t, tap_at - 0.5, 0.5)
        place_emoji(sub, "👆", x0 + 330, y0 + 470 - 30 * out_cubic(kf) + (12 if 0 < kt < 0.3 else 0), 110, alpha=out_cubic(kf) * (1 - p(t, tap_at + 0.8, 0.3)))


def dead_page(sub, t, start, top, title="Summer Sale", body=["This sale has ended.", "Page not found."], code="404", w=880, h=520):
    """Browser card showing a dead-end page."""
    k = p(t, start, 0.4)
    if k <= 0: return
    c, d = card_base(w, h, radius=36, fill=(255, 255, 255, 255))
    d.rounded_rectangle([0, 0, w - 1, 96], radius=36, fill=(236, 238, 243, 255))
    d.rectangle([0, 60, w - 1, 96], fill=(236, 238, 243, 255))
    d.rounded_rectangle([30, 22, w - 30, 76], radius=27, fill=(255, 255, 255, 255))
    d.text((60, 49), "🔒 pineandwick.com/summer-sale", font=font(F_SEMI, 28), fill=(*GREY, 255), anchor="lm")
    d.text((w / 2, 220), code, font=font(F_BLACK, 130), fill=(*RED, 255), anchor="mm")
    for i, l in enumerate(body):
        d.text((w / 2, 350 + i * 58), l, font=font(F_XB, 42), fill=(*INK, 255), anchor="mm")
    c = with_alpha(c, out_cubic(k))
    s = 0.9 + 0.1 * out_back(k)
    c = c.resize((int(w * s), int(h * s)))
    sub.alpha_composite(c, (int(W / 2 - c.width / 2), int(top)))


BUTTONS = [("🛍️", "Shop all candles"), ("🎁", "Gifts under $30"), ("📦", "Holiday shipping dates"), ("⭐", "Read our reviews")]


def link_page(sub, t, start, top, acc, steps, w=700, h=1060, buttons=BUTTONS, tap_at=None, label=None):
    """Phone-shaped link page: avatar, name, then 4 buttons pop in at steps[0..3]."""
    k = p(t, start, 0.45)
    if k <= 0: return
    c, d = card_base(w, h, radius=60, fill=(20, 20, 28, 255))
    d.rounded_rectangle([18, 18, w - 18, h - 18], radius=46, fill=(255, 246, 236, 255))
    d.rounded_rectangle([w / 2 - 80, 34, w / 2 + 80, 58], radius=12, fill=(20, 20, 28, 255))
    ring_avatar(c, d, w / 2, 170, 70, "🕯️", (255, 214, 170), ring=False)
    d.text((w / 2, 285), "Pine & Wick", font=font(F_BLACK, 50), fill=(*INK, 255), anchor="mm")
    d.text((w / 2, 335), "Hand-poured candles", font=font(F_SEMI, 32), fill=(*GREY, 255), anchor="mm")
    for i, (em, lab) in enumerate(buttons):
        kk = p(t, steps[i], 0.4) if i < len(steps) else 0
        if kk <= 0: continue
        y = 430 + i * 140
        s = out_back(kk)
        bw, bh = (w - 100) * s, 110 * s
        tapped = tap_at is not None and i == 1 and 0 < t - tap_at < 0.4
        fill = tuple(int(v * 0.8) for v in acc) if tapped else acc
        d.rounded_rectangle([w / 2 - bw / 2, y - bh / 2, w / 2 + bw / 2, y + bh / 2], radius=bh / 2, fill=(*fill, int(255 * out_cubic(kk))))
        if kk > 0.6:
            e = emoji_img(em, 54)
            c.alpha_composite(with_alpha(e.copy(), out_cubic(kk)), (int(w / 2 - bw / 2 + 40), int(y - e.height / 2)))
            d.text((w / 2 + 30, y), lab, font=font(F_XB, 36), fill=(*INK, int(255 * out_cubic(kk))), anchor="mm")
    d.text((w / 2, h - 70), "free link page", font=font(F_SEMI, 26), fill=(*GREY, 255), anchor="mm")
    c = with_alpha(c, out_cubic(k))
    x0, y0 = int(W / 2 - w / 2), int(top + 80 * (1 - out_cubic(k)))
    sub.alpha_composite(c, (x0, y0))
    if tap_at is not None and t >= tap_at - 0.5:
        kf = p(t, tap_at - 0.5, 0.5)
        place_emoji(sub, "👆", x0 + w - 70, y0 + 600 - 30 * out_cubic(kf), 110, alpha=out_cubic(kf))


def lead_row(sub, t, start, cy, emoji, color, handle, link, ok, flag_at, w=880, h=170):
    k = p(t, start, 0.4)
    if k <= 0: return
    c, d = card_base(w, h, radius=34, fill=(255, 255, 255, 255))
    ring_avatar(c, d, 95, h // 2, 50, emoji, color, ring=False)
    d.text((180, 60), handle, font=font(F_XB, 42), fill=(*INK, 255), anchor="lm")
    d.text((180, 116), link, font=font(F_SEMI, 32), fill=(56, 100, 220, 255), anchor="lm")
    kf = p(t, flag_at, 0.35)
    if kf > 0:
        col = OKG if ok else RED
        lab = "WORKS" if ok else "LEAD"
        s = max(0.02, out_back(kf))
        bw, bh = 170 * s, 64 * s
        x1 = w - 40
        d.rounded_rectangle([x1 - bw, h / 2 - bh / 2, x1, h / 2 + bh / 2], radius=bh / 2, fill=(*col, int(255 * out_cubic(kf))))
        d.text((x1 - bw / 2, h / 2), lab, font=font(F_BLACK, 30 * s), fill=(255, 255, 255, int(255 * out_cubic(kf))), anchor="mm")
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2 + 70 * (1 - out_cubic(k))), int(cy - h / 2)))
