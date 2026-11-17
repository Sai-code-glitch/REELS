"""Helpers for the 2026-11-17 'resume makeover side gig' reels
(mock 1-page resume bad/good, Google-Docs-style editor that builds it step by step,
before→after bullet rewrite card). All names/companies are fictional samples."""
from reel_tags import *
from reel_linkedin import li_composer, LI_BLUE

DOCS_BLUE = (26, 115, 232)
NAVY = (28, 52, 96)

GOOD = dict(
    name="JORDAN LEE",
    headline="Customer Support Specialist",
    contact="Austin, TX · jordan@email.com",
    summary=["Support rep who solves customer", "problems fast and keeps them happy."],
    job="Support Rep · BrightCart · 2023–now",
    bullets=["Answered 60+ tickets a day", "Cut reply time from 8h to 2h", "Trained 4 new teammates"],
    skills=["Zendesk", "Excel", "Spanish"],
)

BAD = dict(
    objective=["Objective: To obtain a challenging", "position where I can utilize my", "skills and grow with a company..."],
    bullets=["Responsible for answering emails", "Duties included helping customers", "Worked on various team projects"],
)


def resume_page(c, d, x, y, w, a, acc=NAVY, good=True):
    """Draw a US Letter resume page. a = [header, summary, experience, skills] alphas (good mode)."""
    a = list(a) + [1.0] * (4 - len(a))
    h = int(w * 11 / 8.5)
    d.rectangle([x, y, x + w, y + h], fill=(255, 255, 255, 255))
    m = w * 0.08
    fs = w / 700  # font scale
    if not good:
        # cluttered: tiny centred name, long objective, vague bullets, page 1 of 3
        d.text((x + w / 2, y + h * 0.06), "jordan lee - resume", font=font(F_MED, 26 * fs), fill=(60, 60, 60, 255), anchor="mm")
        d.text((x + w / 2, y + h * 0.095), "123 Some St, Apt 4 · 555-0100 · jl1999@email · Austin", font=font(F_MED, 18 * fs), fill=(110, 110, 110, 255), anchor="mm")
        yy = y + h * 0.15
        for ln in BAD["objective"]:
            d.text((x + m, yy), ln, font=font(F_MED, 27 * fs), fill=(70, 70, 70, 255), anchor="lm"); yy += 38 * fs
        yy += 26 * fs
        d.text((x + m, yy), "Work History", font=font(F_SEMI, 26 * fs), fill=(50, 50, 50, 255), anchor="lm"); yy += 44 * fs
        for ln in BAD["bullets"]:
            d.text((x + m, yy), "• " + ln, font=font(F_MED, 27 * fs), fill=(70, 70, 70, 255), anchor="lm"); yy += 40 * fs
        yy += 20 * fs
        for i in range(9):  # wall of grey filler text
            ww = (w - 2 * m) * (0.95 - 0.12 * ((i * 7) % 4) / 3)
            d.rounded_rectangle([x + m, yy, x + m + ww, yy + 12 * fs], radius=6, fill=(214, 216, 222, 255)); yy += 28 * fs
        d.text((x + w - m, y + h - 34 * fs), "Page 1 of 3", font=font(F_SEMI, 22 * fs), fill=(140, 140, 140, 255), anchor="rm")
        return h
    g = GOOD
    yy = y + h * 0.075
    if a[0] > 0:
        al = int(255 * a[0])
        d.text((x + m, yy), g["name"], font=font(F_BLACK, 62 * fs), fill=(*acc, al), anchor="lm")
        d.text((x + m, yy + 62 * fs), g["headline"], font=font(F_XB, 32 * fs), fill=(*INK, al), anchor="lm")
        d.text((x + m, yy + 104 * fs), g["contact"], font=font(F_MED, 24 * fs), fill=(110, 116, 130, al), anchor="lm")
        d.rectangle([x + m, yy + 140 * fs, x + w - m, yy + 146 * fs], fill=(*acc, al))
    yy += 185 * fs

    def head(lbl, yy, al):
        d.text((x + m, yy), lbl, font=font(F_BLACK, 26 * fs), fill=(*acc, al), anchor="lm")
    if a[1] > 0:
        al = int(255 * a[1])
        head("SUMMARY", yy, al)
        for i, ln in enumerate(g["summary"]):
            d.text((x + m, yy + (46 + i * 38) * fs), ln, font=font(F_SEMI, 28 * fs), fill=(*INK, al), anchor="lm")
    yy += 150 * fs
    if a[2] > 0:
        al = int(255 * a[2])
        head("EXPERIENCE", yy, al)
        d.text((x + m, yy + 46 * fs), g["job"], font=font(F_XB, 27 * fs), fill=(*INK, al), anchor="lm")
        for i, ln in enumerate(g["bullets"]):
            by = yy + (92 + i * 44) * fs
            d.ellipse([x + m + 4 * fs, by - 6 * fs, x + m + 16 * fs, by + 6 * fs], fill=(*acc, al))
            d.text((x + m + 30 * fs, by), ln, font=font(F_SEMI, 28 * fs), fill=(*INK, al), anchor="lm")
    yy += 250 * fs
    if a[3] > 0:
        al = int(255 * a[3])
        head("SKILLS", yy, al)
        sx = x + m
        for s in g["skills"]:
            f = font(F_XB, 24 * fs)
            tw = d.textlength(s, font=f) + 36 * fs
            d.rounded_rectangle([sx, yy + 30 * fs, sx + tw, yy + 74 * fs], radius=22 * fs, fill=(226, 234, 248, al))
            d.text((sx + tw / 2, yy + 52 * fs), s, font=f, fill=(*acc, al), anchor="mm")
            sx += tw + 16 * fs
        d.text((x + w - m, y + h - 34 * fs), "Page 1 of 1", font=font(F_SEMI, 22 * fs), fill=(140, 140, 140, al), anchor="rm")
    return h


def resume_card(sub, t, start, cx, cy, w=640, good=True, steps=None, rot=0.0, flags=None, flag_at=None, label=None, label_col=None):
    """Floating resume page; flags: list of (text, y_frac) red sticky notes popping in from flag_at."""
    k = p(t, start, 0.45)
    if k <= 0: return
    h = int(w * 11 / 8.5)
    pad = 30
    c = Image.new("RGBA", (w + 2 * pad, h + 2 * pad), (0, 0, 0, 0))
    d = ImageDraw.Draw(c)
    d.rectangle([pad + 12, pad + 16, pad + w + 12, pad + h + 16], fill=(0, 0, 0, 80))
    a = [out_cubic(p(t, s, 0.45)) for s in steps] if steps else [1] * 4
    resume_page(c, d, pad, pad, w, a, good=good)
    s = 0.6 + 0.4 * out_back(k)
    c = c.resize((max(1, int(c.width * s)), max(1, int(c.height * s))), Image.LANCZOS)
    if rot: c = c.rotate(rot, resample=Image.BICUBIC, expand=True)
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(cx - c.width / 2), int(cy - c.height / 2)))
    if label:
        pill(sub, cx, cy - c.height / 2 - 10, label, F_BLACK, 40, label_col or GOLD_C, WHITE if label_col else INK, alpha=out_cubic(k))
    if flags and flag_at is not None:
        for i, (txt, yf, side) in enumerate(flags):
            kf = p(t, flag_at + i * 0.5, 0.35)
            if kf <= 0: continue
            fx = cx + (side * (c.width / 2 - 40))
            fy = cy - c.height / 2 + c.height * yf
            pill(sub, fx, fy, txt, F_BLACK, 40, RED2, WHITE, alpha=out_cubic(kf), scale=out_back(kf), icon="❌")


def docs_editor(sub, t, start, cy, steps, labels=None, w=880, h=1120):
    """Google-Docs-style window building the good resume over steps[0..3]."""
    k = p(t, start, 0.45)
    if k <= 0: return
    c, d = gbase(w, h, fill=(236, 239, 245), radius=36)
    d.rounded_rectangle([0, 0, w - 1, 110], radius=36, fill=(255, 255, 255, 255))
    d.rectangle([0, 70, w - 1, 110], fill=(255, 255, 255, 255))
    d.rounded_rectangle([34, 26, 90, 92], radius=8, fill=(*DOCS_BLUE, 255))
    for i in range(3):
        d.rectangle([46, 46 + i * 14, 78, 52 + i * 14], fill=(255, 255, 255, 255))
    d.text((112, 44), "Resume – Jordan (sample)", font=font(F_XB, 32), fill=(*INK, 255), anchor="lm")
    d.text((112, 82), "File  Edit  View  Insert  Format", font=font(F_SEMI, 24), fill=(*GREY, 255), anchor="lm")
    d.rounded_rectangle([w - 190, 30, w - 34, 86], radius=28, fill=(*DOCS_BLUE, 255))
    d.text((w - 112, 58), "Share", font=font(F_XB, 28), fill=(255, 255, 255, 255), anchor="mm")
    pw = 640
    x, y = (w - pw) // 2, 140
    ph = int(pw * 11 / 8.5)
    d.rectangle([x - 3, y - 3, x + pw + 3, y + ph + 3], fill=(205, 209, 218, 255))
    a = [out_cubic(p(t, st, 0.45)) for st in steps]
    resume_page(c, d, x, y, pw, a, good=True)
    n = sum(1 for s in steps if t >= s)
    if labels and n > 0:
        kk = out_cubic(p(t, steps[n - 1], 0.3))
        d.rounded_rectangle([60, h - 120, w - 60, h - 26], radius=30, fill=(255, 255, 255, 255), outline=(*DOCS_BLUE, 255), width=4)
        d.text((w / 2, h - 73), labels[n - 1], font=font(F_XB, 40), fill=(*INK, int(255 * kk)), anchor="mm")
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(cy - h / 2 + 60 * (1 - out_cubic(k)))))


def bullet_fix(sub, t, start, cy, before, after, swap_at, hl=None, w=880, h=300):
    """Card: struck-through vague bullet → specific bullet with number highlight."""
    k = p(t, start, 0.4)
    if k <= 0: return
    c, d = gbase(w, h, fill=(255, 255, 255), radius=34)
    d.rounded_rectangle([30, 26, 190, 72], radius=23, fill=(*RED2, 255))
    d.text((110, 49), "BEFORE", font=font(F_BLACK, 26), fill=(255, 255, 255, 255), anchor="mm")
    f1 = font(F_SEMI, 40)
    d.text((40, 115), before, font=f1, fill=(120, 124, 136, 255), anchor="lm")
    ks = in_out(p(t, swap_at - 0.5, 0.4))
    if ks > 0:
        tw = d.textlength(before, font=f1)
        d.line([36, 117, 36 + (tw + 8) * ks, 117], fill=(*RED2, 255), width=6)
    ka = p(t, swap_at, 0.4)
    if ka > 0:
        al = int(255 * out_cubic(ka))
        d.rounded_rectangle([30, 160, 170, 206], radius=23, fill=(*OKG, al))
        d.text((100, 183), "AFTER", font=font(F_BLACK, 26), fill=(255, 255, 255, al), anchor="mm")
        f2 = font(F_XB, 44)
        n = int(len(after) * p(t, swap_at, 0.8))
        shown = after[:n]
        xx = 40
        if hl and hl in after:
            i0 = after.index(hl)
            pre, mid = shown[:i0], shown[i0:i0 + len(hl)]
            post = shown[i0 + len(hl):]
            d.text((xx, 250), pre, font=f2, fill=(*INK, al), anchor="lm"); xx += d.textlength(pre, font=f2)
            if mid:
                mw = d.textlength(mid, font=f2)
                d.rounded_rectangle([xx - 4, 222, xx + mw + 4, 278], radius=10, fill=(255, 230, 140, al))
                d.text((xx, 250), mid, font=f2, fill=(*INK, al), anchor="lm"); xx += mw
            d.text((xx, 250), post, font=f2, fill=(*INK, al), anchor="lm")
        else:
            d.text((xx, 250), shown, font=f2, fill=(*INK, al), anchor="lm")
    with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2 + 60 * (1 - out_cubic(k))), int(cy - h / 2)))
