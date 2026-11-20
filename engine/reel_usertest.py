"""Helpers for the 2026-11-20 'get paid to test websites' (user testing) reels.
Mock tester-app notification, browser test with REC + think-aloud, screener card,
example earnings bar chart, 5-testers stat. All sites/apps shown are generic samples."""
from reel_insta import *

GREEN = (40, 180, 110)
BLUE = (70, 120, 255)


def test_alert(sub, t, start, cy, body="$10 · about 20 min · Website", title="New test available", w=880):
    notification(sub, t, start, cy, "Tester app", title, body, (90, 110, 255), icon="🧪", w=w)


def _shop_page(c, d, x, y, w, h, t, hl=None, hl_k=0.0):
    """Generic sample shop page inside a browser."""
    d.rectangle([x, y, x + w, y + 90], fill=(245, 240, 232, 255))
    d.text((x + 34, y + 45), "Oak & Ember", font=font(F_BLACK, 38), fill=(*INK, 255), anchor="lm")
    d.text((x + w - 34, y + 45), "☰", font=font(DEJAVU, 40), fill=(*INK, 255), anchor="rm")
    # hero
    d.rounded_rectangle([x + 30, y + 120, x + w - 30, y + 470], radius=26, fill=(232, 190, 140, 255))
    e = emoji_img("🕯️", 190)
    c.alpha_composite(e, (int(x + w / 2 - e.width / 2), int(y + 295 - e.height / 2)))
    d.text((x + 34, y + 530), "Winter Pine Candle", font=font(F_XB, 44), fill=(*INK, 255), anchor="lm")
    d.text((x + 34, y + 590), "$24.00", font=font(F_BLACK, 42), fill=(*INK, 255), anchor="lm")
    # button
    d.rounded_rectangle([x + 34, y + 650, x + w - 34, y + 750], radius=50, fill=(*INK, 255))
    d.text((x + w / 2, y + 700), "Add to cart", font=font(F_BLACK, 40), fill=(255, 255, 255, 255), anchor="mm")
    # tiny hard-to-find link
    d.text((x + w - 40, y + h - 40), "returns", font=font(F_SEMI, 22), fill=(170, 170, 176, 255), anchor="rm")
    if hl == "returns" and hl_k > 0:
        r = 70 + 10 * math.sin(t * 8)
        cx, cyy = x + w - 85, y + h - 40
        d.ellipse([cx - r, cyy - r * 0.6, cx + r, cyy + r * 0.6], outline=(235, 64, 52, int(255 * hl_k)), width=6)


def browser_test(sub, t, start, top, task="Task 1: Find the return policy", rec_from=None, cursor=None, hl_at=None, w=880, h=1080):
    """Browser window running a recorded test. cursor: list of (time, x_frac, y_frac)."""
    k = p(t, start, 0.45)
    if k <= 0: return
    c, d = card_base(w, h, radius=40, fill=(255, 255, 255, 255))
    # chrome
    d.rounded_rectangle([0, 0, w - 1, 100], radius=40, fill=(232, 235, 242, 255))
    d.rectangle([0, 60, w - 1, 100], fill=(232, 235, 242, 255))
    for i, col in enumerate([(255, 95, 86), (255, 189, 46), (39, 201, 63)]):
        d.ellipse([30 + i * 40, 36, 56 + i * 40, 62], fill=(*col, 255))
    d.rounded_rectangle([170, 24, w - 170, 76], radius=26, fill=(255, 255, 255, 255))
    d.text((200, 50), "sample-shop.com", font=font(F_SEMI, 28), fill=(*GREY, 255), anchor="lm")
    # REC badge
    if rec_from is not None and t >= rec_from:
        on = (int((t - rec_from) * 2) % 2 == 0)
        d.rounded_rectangle([w - 150, 26, w - 26, 74], radius=24, fill=(30, 30, 36, 255))
        d.ellipse([w - 136, 40, w - 116, 60], fill=(235, 64, 52, 255 if on else 110))
        secs = int(t - rec_from)
        d.text((w - 46, 50), f"0:{secs:02d}", font=font(F_XB, 26), fill=(255, 255, 255, 255), anchor="rm")
    # task banner
    d.rectangle([0, 100, w, 190], fill=(255, 241, 196, 255))
    d.text((34, 145), task, font=font(F_XB, 36), fill=(*INK, 255), anchor="lm")
    hk = out_cubic(p(t, hl_at, 0.4)) if hl_at is not None else 0
    _shop_page(c, d, 0, 190, w, h - 190, t, hl="returns", hl_k=hk)
    # cursor
    if cursor:
        pts = cursor
        if t <= pts[0][0]:
            cx, cy = pts[0][1], pts[0][2]
        else:
            cx, cy = pts[-1][1], pts[-1][2]
            for (t0, x0, y0), (t1, x1, y1) in zip(pts, pts[1:]):
                if t0 <= t < t1:
                    kk = in_out((t - t0) / (t1 - t0))
                    cx, cy = lerp(x0, x1, kk), lerp(y0, y1, kk)
                    break
        px, py = cx * w, cy * h
        d.polygon([(px, py), (px, py + 56), (px + 15, py + 42), (px + 27, py + 68), (px + 37, py + 63), (px + 25, py + 38), (px + 44, py + 38)],
                  fill=(20, 20, 24, 255), outline=(255, 255, 255, 255))
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(top + 80 * (1 - out_cubic(k)))))


def think_bubble(sub, t, start, cy, text, w=820, color=(255, 255, 255), icon="🗣️"):
    k = p(t, start, 0.35)
    if k <= 0: return
    h = 120
    c, d = card_base(w, h, radius=60, fill=(*color, 245))
    ic = emoji_img(icon, 66)
    c.alpha_composite(ic, (34, int(h / 2 - ic.height / 2)))
    d.text((124, h / 2), text, font=font(F_XB, 38), fill=(*INK, 255), anchor="lm")
    s = 0.8 + 0.2 * out_back(k)
    c = c.resize((max(1, int(w * s)), max(1, int(h * s))), Image.LANCZOS)
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - c.width / 2), int(cy - c.height / 2)))


def screener(sub, t, start, top, questions, result_at, result="You qualify!", good=True, w=880, acc=BLUE):
    """questions: list of (question, [options], selected_index, select_time)."""
    k = p(t, start, 0.45)
    if k <= 0: return
    qh = 250
    h = 130 + qh * len(questions) + 150
    c, d = card_base(w, h, radius=40, fill=(255, 255, 255, 255))
    d.text((40, 66), "Quick screener", font=font(F_BLACK, 46), fill=(*INK, 255), anchor="lm")
    d.text((w - 40, 66), f"{len(questions)} question" + ("s" if len(questions) > 1 else ""), font=font(F_SEMI, 30), fill=(*GREY, 255), anchor="rm")
    y = 130
    for q, opts, sel, at in questions:
        d.text((40, y + 30), q, font=font(F_XB, 36), fill=(*INK, 255), anchor="lm")
        ox = 40
        for i, o in enumerate(opts):
            f = font(F_SEMI, 32)
            tw = d.textlength(o, font=f) + 70
            on = i == sel and t >= at
            ks = out_cubic(p(t, at, 0.25)) if i == sel else 0
            fill = tuple(int(lerp(244, v, ks)) for v in acc) if on else (244, 245, 249)
            d.rounded_rectangle([ox, y + 80, ox + tw, y + 170], radius=24, fill=(*fill, 255), outline=(*LINE, 255), width=2)
            d.text((ox + tw / 2, y + 125), o, font=f, fill=(255, 255, 255, 255) if on and ks > 0.5 else (*INK, 255), anchor="mm")
            ox += tw + 18
        y += qh
    kr = p(t, result_at, 0.4)
    if kr > 0:
        kb = max(0.02, out_back(kr))
        col = GREEN if good else (235, 64, 52)
        bw, bh = (w - 80) * kb, 100 * kb
        cy = y + 60
        d.rounded_rectangle([w / 2 - bw / 2, cy - bh / 2, w / 2 + bw / 2, cy + bh / 2], radius=bh / 2, fill=(*col, 255))
        d.text((w / 2, cy), result, font=font(F_BLACK, 44 * kb), fill=(255, 255, 255, 255), anchor="mm")
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(top + 80 * (1 - out_cubic(k)))))


def bar_chart(sub, t, start, top, bars, acc, title="Example week", every=0.45, w=880, h=760, unit="$"):
    """bars: list of (label, value). Bars grow one by one; total counts up."""
    k = p(t, start, 0.45)
    if k <= 0: return
    c, d = card_base(w, h, radius=40, fill=(255, 255, 255, 255))
    d.text((40, 66), title, font=font(F_BLACK, 46), fill=(*INK, 255), anchor="lm")
    vmax = max(v for _, v in bars)
    base_y = h - 110
    maxh = h - 300
    n = len(bars)
    bw = (w - 80) / n
    total = 0.0
    for i, (lab, v) in enumerate(bars):
        kb = out_cubic(p(t, start + 0.5 + i * every, 0.5))
        x0 = 40 + i * bw + 18
        x1 = 40 + (i + 1) * bw - 18
        d.text(((x0 + x1) / 2, base_y + 46), lab, font=font(F_XB, 30), fill=(*GREY, 255), anchor="mm")
        if kb > 0 and v > 0:
            bh = maxh * (v / vmax) * kb
            d.rounded_rectangle([x0, base_y - bh, x1, base_y], radius=16, fill=(*acc, 255))
            d.text(((x0 + x1) / 2, base_y - bh - 30), f"{unit}{int(round(v * kb))}", font=font(F_BLACK, 34), fill=(*INK, 255), anchor="mm")
        total += v * kb
    d.line([40, base_y, w - 40, base_y], fill=(*LINE, 255), width=3)
    d.text((w - 40, 66), f"{unit}{int(round(total))}", font=font(F_BLACK, 52), fill=(*GREEN, 255), anchor="rm")
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(top + 80 * (1 - out_cubic(k)))))


def five_testers(sub, t, start, cy, acc, found_at):
    """5 tester avatars; each drops a 'problem found' pin."""
    faces = ["🧑", "👩", "👨", "🧔", "👵"]
    for i, f in enumerate(faces):
        kk = p(t, start + i * 0.18, 0.4)
        if kk <= 0: continue
        x = 180 + i * 180
        place_emoji(sub, f, x, cy, 120 * out_back(kk), alpha=out_cubic(kk))
        kf = p(t, found_at + i * 0.25, 0.35)
        if kf > 0:
            place_emoji(sub, "🐞", x + 10, cy - 120 - 20 * (1 - out_cubic(kf)), 70 * out_back(kf), alpha=out_cubic(kf))
