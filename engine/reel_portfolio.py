"""Helpers for the 2026-10-24 portfolio reels (sample projects, case study, free 1-page portfolio)."""
from reel_chat import *


def card_base(w, h, fill=(250, 251, 255)):
    c = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(c)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=40, fill=(*fill, 255))
    return c, d


def paste_card(sub, c, t, start, cx, cy, dy=60, dur=0.45):
    k = p(t, start, dur)
    if k <= 0: return 0
    with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(cx - c.width / 2), int(cy - c.height / 2 + dy * (1 - out_cubic(k)))))
    return k


def tag(d, x, y, label, bg, fg=INK, size=28, anchor_right=False):
    f = font(F_XB, size)
    tw = d.textlength(label, font=f)
    w = tw + 40
    x0 = x - w if anchor_right else x
    d.rounded_rectangle([x0, y, x0 + w, y + size + 24], radius=(size + 24) / 2, fill=(*bg, 255))
    d.text((x0 + w / 2, y + (size + 24) / 2), label, font=f, fill=(*fg, 255), anchor="mm")


def strike(sub, t, start, x0, x1, y, color, width=16):
    k = in_out(p(t, start, 0.4))
    if k <= 0: return
    d = ImageDraw.Draw(sub)
    d.line([x0, y, x0 + (x1 - x0) * k, y - 10 * k], fill=(*color, 255), width=width)


def sample_row(sub, t, start, cy, icon, shop, task, color, w=880, h=200):
    """One 'sample project' row: shop name + what you redo."""
    c, d = card_base(w, h)
    d.rounded_rectangle([28, 28, 172, 172], radius=30, fill=(*color, 255))
    e = emoji_img(icon, 92)
    c.alpha_composite(e, (int(100 - e.width / 2), int(100 - e.height / 2)))
    d.text((204, 72), shop, font=font(F_XB, 44), fill=(*INK, 255), anchor="lm")
    d.text((204, 132), task, font=font(F_SEMI, 36), fill=(90, 96, 110, 255), anchor="lm")
    k = paste_card(sub, c, t, start, W / 2 + 80 * (1 - out_cubic(p(t, start, 0.45))), cy, dy=0)
    return k


def before_after(sub, t, start, cy, acc, swap_at, w=880, h=560):
    """Plumber homepage headline: before (weak) -> after (clear), wipe transition."""
    k = p(t, start, 0.45)
    if k <= 0: return
    c, d = card_base(w, h)
    # browser bar
    d.rounded_rectangle([0, 0, w - 1, 90], radius=40, fill=(228, 231, 238, 255))
    d.rectangle([0, 50, w - 1, 90], fill=(228, 231, 238, 255))
    for i, col in enumerate([(255, 95, 86), (255, 189, 46), (39, 201, 63)]):
        d.ellipse([34 + i * 44, 30, 62 + i * 44, 58], fill=(*col, 255))
    d.rounded_rectangle([190, 24, w - 40, 66], radius=21, fill=(255, 255, 255, 255))
    d.text((214, 45), "danplumbing.com", font=font(F_MED, 28), fill=(110, 116, 130, 255), anchor="lm")
    sw = in_out(p(t, swap_at, 0.7))
    before = Image.new("RGBA", (w, h - 90), (0, 0, 0, 0)); bd = ImageDraw.Draw(before)
    bd.text((w / 2, 130), "Welcome to our", font=font(F_SEMI, 56), fill=(150, 154, 166, 255), anchor="mm")
    bd.text((w / 2, 205), "website!", font=font(F_SEMI, 56), fill=(150, 154, 166, 255), anchor="mm")
    bd.text((w / 2, 320), "We do many services.", font=font(F_MED, 36), fill=(170, 174, 186, 255), anchor="mm")
    tag(bd, 50, 392, "BEFORE", (255, 226, 228), (200, 30, 50))
    after = Image.new("RGBA", (w, h - 90), (0, 0, 0, 0)); ad = ImageDraw.Draw(after)
    ad.text((w / 2, 120), "Leaky pipe?", font=font(F_BLACK, 74), fill=(*INK, 255), anchor="mm")
    ad.text((w / 2, 205), "Same-day repairs in Dayton", font=font(F_XB, 44), fill=(40, 46, 60, 255), anchor="mm")
    ad.rounded_rectangle([w / 2 - 200, 270, w / 2 + 200, 350], radius=40, fill=(*acc, 255))
    ad.text((w / 2, 310), "Call now", font=font(F_XB, 40), fill=(*INK, 255), anchor="mm")
    tag(ad, 50, 392, "AFTER · SAMPLE", (*acc,), INK)
    cut = int(w * sw)
    if cut < w:
        c.alpha_composite(before.crop((cut, 0, w, h - 90)), (cut, 90))
    if cut > 0:
        c.alpha_composite(after.crop((0, 0, cut, h - 90)), (0, 90))
        d.line([cut, 100, cut, h - 10], fill=(*acc, 255), width=8) if sw < 1 else None
    with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(cy - h / 2 + 60 * (1 - out_cubic(k)))))


def case_card(sub, t, start, cy, rows, acc, title="Sample project: Dan's Plumbing", w=880, h=700):
    k = p(t, start, 0.45)
    if k <= 0: return
    c, d = card_base(w, h)
    d.text((50, 70), "CASE STUDY", font=font(F_XB, 30), fill=(*acc, 255), anchor="lm")
    d.text((50, 125), title, font=font(F_BLACK, 44), fill=(*INK, 255), anchor="lm")
    d.line([50, 178, w - 50, 178], fill=(220, 224, 232, 255), width=3)
    for i, (lab, body, at) in enumerate(rows):
        kk = p(t, at, 0.4)
        if kk <= 0: continue
        y = 220 + i * 160
        al = int(255 * out_cubic(kk))
        d.rounded_rectangle([50, y, 104, y + 54], radius=27, fill=(*acc, al))
        d.text((77, y + 27), str(i + 1), font=font(F_BLACK, 32), fill=(*INK, al), anchor="mm")
        d.text((130, y + 22), lab, font=font(F_XB, 40), fill=(*INK, al), anchor="lm")
        for j, l in enumerate(wrap(body, 34)):
            d.text((130, y + 78 + j * 44), l, font=font(F_SEMI, 34), fill=(90, 96, 110, al), anchor="lm")
    with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(cy - h / 2 + 60 * (1 - out_cubic(k)))))


def site_builder(sub, t, start, cy, acc, steps, w=760, h=1000):
    """Mock one-page portfolio that builds block by block. steps: times for header, samples, price, button."""
    k = p(t, start, 0.45)
    if k <= 0: return
    c, d = card_base(w, h)
    d.rounded_rectangle([0, 0, w - 1, 84], radius=40, fill=(228, 231, 238, 255))
    d.rectangle([0, 44, w - 1, 84], fill=(228, 231, 238, 255))
    d.rounded_rectangle([40, 22, w - 40, 62], radius=20, fill=(255, 255, 255, 255))
    d.text((64, 42), "samjones.my.canva.site", font=font(F_MED, 28), fill=(110, 116, 130, 255), anchor="lm")
    a = [out_cubic(p(t, s, 0.4)) for s in steps]
    # header
    if a[0] > 0:
        al = int(255 * a[0])
        d.ellipse([w / 2 - 70, 120, w / 2 + 70, 260], fill=(*acc, al))
        d.text((w / 2, 190), "SJ", font=font(F_BLACK, 60), fill=(*INK, al), anchor="mm")
        d.text((w / 2, 310), "Sam Jones", font=font(F_BLACK, 56), fill=(*INK, al), anchor="mm")
        d.text((w / 2, 370), "I write websites that get calls", font=font(F_SEMI, 34), fill=(90, 96, 110, al), anchor="mm")
    # samples
    cols = [(255, 214, 92), (110, 190, 255), (255, 140, 170)]
    icons = ["🔧", "🧁", "🕯️"]
    for i in range(3):
        kk = out_cubic(p(t, steps[1] + i * 0.25, 0.35))
        if kk <= 0: continue
        sz = 200; gap = 30
        x = (w - 3 * sz - 2 * gap) / 2 + i * (sz + gap); y = 430
        d.rounded_rectangle([x, y, x + sz, y + sz], radius=26, fill=(*cols[i], int(255 * kk)))
        e = with_alpha(emoji_img(icons[i], 90).copy(), kk)
        c.alpha_composite(e, (int(x + sz / 2 - e.width / 2), int(y + 70 - e.height / 2)))
        d.text((x + sz / 2, y + 160), "Sample", font=font(F_XB, 30), fill=(*INK, int(255 * kk)), anchor="mm")
    if a[2] > 0:
        al = int(255 * a[2])
        d.text((w / 2, 720), "Homepage rewrite from $75", font=font(F_XB, 42), fill=(*INK, al), anchor="mm")
        d.text((w / 2, 772), "(example pricing)", font=font(F_MED, 30), fill=(130, 136, 150, al), anchor="mm")
    if a[3] > 0:
        al = int(255 * a[3])
        s = out_back(p(t, steps[3], 0.4))
        bw, bh = 400 * s, 96 * s
        d.rounded_rectangle([w / 2 - bw / 2, 880 - bh / 2, w / 2 + bw / 2, 880 + bh / 2], radius=bh / 2, fill=(*acc, al))
        d.text((w / 2, 880), "Message me", font=font(F_XB, 42 * s), fill=(*INK, al), anchor="mm")
    with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(cy - h / 2 + 60 * (1 - out_cubic(k)))))


def timer(sub, t, start, dur, cx, cy, minutes, color):
    k = p(t, start, dur)
    if t < start: return
    m = minutes * k
    a = out_cubic(p(t, start, 0.3))
    place_emoji(sub, "⏱️", cx - 170, cy, 80, alpha=a)
    draw_text(sub, f"{int(m):02d}:{int((m % 1) * 60):02d}", F_BLACK, 76, cx + 40, cy, color, alpha=a)
