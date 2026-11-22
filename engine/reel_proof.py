"""Helpers for the 2026-11-22 'website proofreading gig' reels.
Mock shop website with typos that get circled and fixed, Google-Docs-style squiggle check,
Ctrl+F find bar, fix-list table. All shops/sites shown are generic samples."""
import re
from reel_replies import *

RED = (230, 60, 60)
FIXG = (20, 150, 70)

TOK = re.compile(r"(\{[^}]*\})")


def _rich_line(c, d, x, y, line, f, t, flags, idx0, ink=INK):
    """Draw a line with {bad|good} tokens. flags[i] = (flag_at, fix_at). Returns next typo index."""
    i = idx0
    for tok in TOK.split(line):
        if not tok: continue
        if tok.startswith("{"):
            bad, good = tok[1:-1].split("|")
            fa, fx = flags[i] if i < len(flags) else (None, None)
            kf = p(t, fa, 0.35) if fa is not None else 0
            kx = p(t, fx, 0.35) if fx is not None else 0
            if kx > 0.5:
                word, col = good, FIXG
            else:
                word, col = bad, (RED if kf > 0 else ink)
            tw = d.textlength(word, font=f)
            if kx > 0.5:
                d.line([x, y + 30, x + tw, y + 30], fill=(*FIXG, 255), width=5)
            d.text((x, y), word, font=f, fill=(*col, 255), anchor="lm")
            if kf > 0 and kx <= 0.5:
                s = out_back(kf)
                padx, pady = 10 * s, 36 * s
                cx = x + tw / 2
                d.ellipse([cx - tw / 2 * s - padx, y - pady, cx + tw / 2 * s + padx, y + pady], outline=(*RED, 255), width=6)
            x += tw
            i += 1
        else:
            d.text((x, y), tok, font=f, fill=(*ink, 255), anchor="lm")
            x += d.textlength(tok, font=f)
    return i


def site_page(sub, t, start, top, lines, flags, shop="Pine & Wick Candles", emoji="🕯️", color=(255, 226, 190),
              url="pinewick.example", w=880, h=980, size=48, button="Shop gifts"):
    """Browser card with a small-shop homepage. lines may contain {bad|good} typo tokens."""
    k = p(t, start, 0.4)
    if k <= 0: return
    c, d = card_base(w, h, radius=40, fill=(255, 255, 255, 255))
    # chrome
    d.rounded_rectangle([0, 0, w - 1, 100], radius=40, fill=(240, 242, 247, 255))
    d.rectangle([0, 60, w - 1, 100], fill=(240, 242, 247, 255))
    for j, col in enumerate([(255, 95, 86), (255, 189, 46), (39, 201, 63)]):
        d.ellipse([34 + j * 36, 38, 58 + j * 36, 62], fill=(*col, 255))
    d.rounded_rectangle([160, 24, w - 34, 76], radius=26, fill=(255, 255, 255, 255))
    d.text((190, 50), url, font=font(F_SEMI, 30), fill=(*GREY, 255), anchor="lm")
    d.text((w - 56, 50), "sample", font=font(F_SEMI, 26), fill=(*GREY, 255), anchor="rm")
    # banner
    d.rectangle([0, 100, w, 330], fill=(*color, 255))
    e = emoji_img(emoji, 120)
    c.alpha_composite(e, (60, 215 - e.height // 2))
    d.text((210, 190), shop, font=font(F_BLACK, 46), fill=(*INK, 255), anchor="lm")
    d.text((210, 250), "Handmade · small batch", font=font(F_SEMI, 32), fill=(80, 86, 100, 255), anchor="lm")
    f = font(F_XB, size)
    y = 410
    idx = 0
    for line in lines:
        idx = _rich_line(c, d, 50, y, line, f, t, flags, idx)
        y += int(size * 2.1)
    # button
    by = h - 130
    d.rounded_rectangle([50, by, 50 + 380, by + 90], radius=45, fill=(*INK, 255))
    d.text((240, by + 45), button, font=font(F_XB, 38), fill=(255, 255, 255, 255), anchor="mm")
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(top + 60 * (1 - out_cubic(k)))))


def wavy(d, x0, x1, y, col, width=4, amp=6, wl=16):
    pts = []
    x = x0
    while x <= x1:
        pts.append((x, y + amp * math.sin((x - x0) / wl * 2 * math.pi)))
        x += 3
    if len(pts) > 1:
        d.line(pts, fill=col, width=width)


def doc_check(sub, t, start, top, lines, marks, title="Homepage text (pasted)", w=880, h=760, size=40):
    """Docs card; words in {bad|good} get a red squiggle at marks[i] (time)."""
    k = p(t, start, 0.4)
    if k <= 0: return
    c, d = card_base(w, h, radius=36, fill=(255, 255, 255, 255))
    d.rounded_rectangle([0, 0, w - 1, 110], radius=36, fill=(236, 241, 251, 255))
    d.rectangle([0, 70, w - 1, 110], fill=(236, 241, 251, 255))
    d.rounded_rectangle([34, 28, 84, 84], radius=8, fill=(66, 133, 244, 255))
    for i in range(3):
        d.line([46, 44 + i * 12, 72, 44 + i * 12], fill=(255, 255, 255, 255), width=4)
    d.text((104, 56), title, font=font(F_XB, 34), fill=(*INK, 255), anchor="lm")
    d.text((w - 36, 56), "Free", font=font(F_XB, 30), fill=(*FIXG, 255), anchor="rm")
    f = font(F_SEMI, size)
    y = 180
    mi = 0
    for line in lines:
        x = 50
        for tok in TOK.split(line):
            if not tok: continue
            if tok.startswith("{"):
                bad = tok[1:-1].split("|")[0]
                tw = d.textlength(bad, font=f)
                d.text((x, y), bad, font=f, fill=(60, 66, 80, 255), anchor="lm")
                at = marks[mi] if mi < len(marks) else None
                if at is not None and t >= at:
                    kk = out_cubic(p(t, at, 0.35))
                    wavy(d, x, x + tw * kk, y + 28, (*RED, 255))
                x += tw
                mi += 1
            else:
                d.text((x, y), tok, font=f, fill=(60, 66, 80, 255), anchor="lm")
                x += d.textlength(tok, font=f)
        y += int(size * 1.9)
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(top + 60 * (1 - out_cubic(k)))))


def find_bar(sub, t, start, top, query, snippets, acc, type_dur=0.6, w=880):
    """Ctrl+F bar types the query, match count appears, snippet rows highlight the match.
    snippets: list of (text, appear_time)."""
    k = p(t, start, 0.4)
    if k <= 0: return
    h = 150 + 120 * len(snippets) + 30
    c, d = card_base(w, h, radius=36, fill=(255, 255, 255, 255))
    d.rounded_rectangle([30, 30, w - 30, 120], radius=24, fill=(244, 245, 249, 255), outline=(*acc, 255), width=4)
    d.text((60, 75), "Find:", font=font(F_XB, 36), fill=(*GREY, 255), anchor="lm")
    n = int(len(query) * p(t, start + 0.3, type_dur))
    q = query[:n]
    qx = 170
    d.text((qx, 75), q, font=font(F_BLACK, 42), fill=(*INK, 255), anchor="lm")
    if n < len(query) and int(t * 4) % 2 == 0:
        cx = qx + d.textlength(q, font=font(F_BLACK, 42)) + 4
        d.line([cx, 50, cx, 100], fill=(*INK, 255), width=4)
    shown = sum(1 for _, at in snippets if t >= at)
    if n >= len(query):
        lab = f"{shown} matches" if shown != 1 else "1 match"
        d.text((w - 60, 75), lab, font=font(F_XB, 34), fill=(*RED, 255), anchor="rm")
    f = font(F_SEMI, 38)
    for i, (txt, at) in enumerate(snippets):
        kk = p(t, at, 0.35)
        if kk <= 0: continue
        al = int(255 * out_cubic(kk))
        y = 190 + i * 120
        x = 60 + int(40 * (1 - out_cubic(kk)))
        for part in re.split(r"(" + re.escape(query) + r")", txt):
            if not part: continue
            tw = d.textlength(part, font=f)
            if part == query:
                d.rounded_rectangle([x - 6, y - 30, x + tw + 6, y + 30], radius=8, fill=(255, 220, 60, al))
            d.text((x, y), part, font=f, fill=(*INK, al), anchor="lm")
            x += tw
        if i < len(snippets) - 1:
            d.line([60, y + 60, w - 60, y + 60], fill=(*LINE, 255), width=2)
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(top + 60 * (1 - out_cubic(k)))))


def fix_table(sub, t, start, top, rows, acc, title="Fix list: Pine & Wick", w=880, row_h=150):
    """Deliverable: rows of (page, found, fix, appear_time)."""
    k = p(t, start, 0.4)
    if k <= 0: return
    h = 220 + row_h * len(rows) + 20
    c, d = card_base(w, h, radius=36, fill=(255, 255, 255, 255))
    d.rounded_rectangle([0, 0, w - 1, 110], radius=36, fill=(*acc, 255))
    d.rectangle([0, 70, w - 1, 110], fill=(*acc, 255))
    d.text((44, 56), title, font=font(F_BLACK, 42), fill=(*INK, 255), anchor="lm")
    d.text((w - 40, 56), "PDF", font=font(F_BLACK, 32), fill=(*INK, 255), anchor="rm")
    for j, lab in enumerate(["PAGE", "FOUND", "FIX"]):
        d.text(([44, 270, 570][j], 160), lab, font=font(F_XB, 28), fill=(*GREY, 255), anchor="lm")
    d.line([30, 195, w - 30, 195], fill=(*LINE, 255), width=3)
    for i, (page, found, fix, at) in enumerate(rows):
        kk = p(t, at, 0.35)
        if kk <= 0: continue
        al = int(255 * out_cubic(kk))
        y = 195 + row_h * i + row_h / 2
        dx = int(50 * (1 - out_cubic(kk)))
        d.text((44 + dx, y), page, font=font(F_XB, 34), fill=(*INK, al), anchor="lm")
        ff = font(F_SEMI, 36)
        d.text((270 + dx, y), found, font=ff, fill=(*RED, al), anchor="lm")
        tw = d.textlength(found, font=ff)
        d.line([270 + dx, y + 2, 270 + dx + tw, y + 2], fill=(*RED, al), width=3)
        d.text((570 + dx, y), fix, font=font(F_XB, 36), fill=(*FIXG, al), anchor="lm")
        if i < len(rows) - 1:
            d.line([30, y + row_h / 2, w - 30, y + row_h / 2], fill=(*LINE, 255), width=2)
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(top + 60 * (1 - out_cubic(k)))))


def stamp(sub, t, start, cx, cy, label, col, size=58, rot=-8):
    """Rubber-stamp style label that slams in."""
    k = p(t, start, 0.35)
    if k <= 0: return
    f = font(F_BLACK, size)
    tmp = Image.new("RGBA", (900, 260), (0, 0, 0, 0))
    d = ImageDraw.Draw(tmp)
    tw = d.textlength(label, font=f)
    d.rounded_rectangle([450 - tw / 2 - 36, 130 - size * 0.9, 450 + tw / 2 + 36, 130 + size * 0.9], radius=20, outline=(*col, 255), width=8)
    d.text((450, 130), label, font=f, fill=(*col, 255), anchor="mm")
    tmp = tmp.crop(tmp.getbbox()).rotate(rot, resample=Image.BICUBIC, expand=True)
    s = lerp(1.8, 1.0, out_cubic(k))
    tmp = tmp.resize((int(tmp.width * s), int(tmp.height * s)), Image.LANCZOS)
    tmp = with_alpha(tmp, out_cubic(k))
    sub.alpha_composite(tmp, (int(cx - tmp.width / 2), int(cy - tmp.height / 2)))
