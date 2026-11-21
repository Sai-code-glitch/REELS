"""Helpers for the 2026-11-21 'Etsy saved replies' reels.
Mock Etsy-style messages inbox with unread counter, chat with a Saved replies picker,
Google-Docs-style reply pack, shop FAQ check. All shops/names shown are generic samples."""
import re, textwrap
from reel_usertest import *
from reel_etsy import ETSY, etsy_search

QUESTIONS = [
    ("Will it arrive by Dec 24?", "📦"),
    ("Can you gift wrap it?", "🎁"),
    ("Where is my order?", "🚚"),
    ("Can I add a name?", "✏️"),
    ("Can I return it?", "↩️"),
]
NAMES = ["Emma R.", "Jake T.", "Priya S.", "Liam W.", "Sofia M.", "Noah K.", "Ava L."]


def etsy_inbox(sub, t, start, top, rows, count_from=1, count_to=38, count_dur=2.4, w=880, row_h=138, title="Messages"):
    """rows: list of (name, question, emoji, appear_time). Unread badge counts up."""
    k = p(t, start, 0.4)
    if k <= 0: return
    h = 150 + row_h * len(rows) + 20
    c, d = card_base(w, h, radius=40, fill=(255, 255, 255, 255))
    d.rounded_rectangle([0, 0, w - 1, 130], radius=40, fill=(*ETSY, 255))
    d.rectangle([0, 90, w - 1, 130], fill=(*ETSY, 255))
    d.text((44, 66), title, font=font(F_BLACK, 48), fill=(255, 255, 255, 255), anchor="lm")
    n = int(round(lerp(count_from, count_to, out_cubic(p(t, start + 0.3, count_dur)))))
    lab = f"{n} unread"
    f = font(F_BLACK, 36)
    tw = d.textlength(lab, font=f)
    pulse = 1 + 0.08 * math.sin(t * 9)
    d.rounded_rectangle([w - 60 - tw - 40, 66 - 30 * pulse, w - 40, 66 + 30 * pulse], radius=30, fill=(255, 255, 255, 255))
    d.text((w - 60 - tw / 2, 66), lab, font=f, fill=(*ETSY, 255), anchor="mm")
    for i, (name, q, em, at) in enumerate(rows):
        kk = p(t, at, 0.35)
        if kk <= 0: continue
        y = 150 + i * row_h
        al = int(255 * out_cubic(kk))
        dx = int(70 * (1 - out_cubic(kk)))
        d.ellipse([36 + dx, y + 24, 116 + dx, y + 104], fill=(255, 226, 205, al))
        e = emoji_img(em, 52)
        e = with_alpha(e, out_cubic(kk))
        c.alpha_composite(e, (76 + dx - e.width // 2, y + 64 - e.height // 2))
        d.text((146 + dx, y + 42), name, font=font(F_XB, 34), fill=(*INK, al), anchor="lm")
        d.text((146 + dx, y + 92), q, font=font(F_SEMI, 36), fill=(70, 76, 90, al), anchor="lm")
        d.ellipse([w - 64, y + 52, w - 40, y + 76], fill=(*ETSY, al))
        if i < len(rows) - 1:
            d.line([146, y + row_h, w - 40, y + row_h], fill=(232, 235, 240, 255), width=2)
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(top + 60 * (1 - out_cubic(k)))))


def saved_picker(sub, t, start, top, buyer_q, items, pick=0, open_at=None, pick_at=None, reply=None, w=880, h=1060):
    """Etsy-style conversation: buyer question, Saved replies sheet opens, one is tapped, reply sends."""
    k = p(t, start, 0.4)
    if k <= 0: return
    c, d = card_base(w, h, radius=44, fill=(244, 245, 248, 255))
    d.rounded_rectangle([0, 0, w - 1, 120], radius=44, fill=(255, 255, 255, 255))
    d.rectangle([0, 80, w - 1, 120], fill=(255, 255, 255, 255))
    d.ellipse([36, 24, 108, 96], fill=(255, 226, 205, 255))
    d.text((72, 60), "E", font=font(F_BLACK, 40), fill=(*ETSY, 255), anchor="mm")
    d.text((130, 60), "Emma R.", font=font(F_XB, 38), fill=(*INK, 255), anchor="lm")
    d.text((w - 40, 60), "Etsy", font=font(F_BLACK, 38), fill=(*ETSY, 255), anchor="rm")
    # buyer bubble
    f = font(F_SEMI, 38)
    bw = d.textlength(buyer_q, font=f) + 60
    d.rounded_rectangle([40, 160, 40 + bw, 250], radius=34, fill=(255, 255, 255, 255))
    d.text((70, 205), buyer_q, font=f, fill=(*INK, 255), anchor="lm")
    # reply sent
    if reply and pick_at is not None:
        kr = p(t, pick_at + 0.5, 0.4)
        if kr > 0:
            al = int(255 * out_cubic(kr))
            lines = textwrap.wrap(reply, 30)
            rh = 40 + 50 * len(lines)
            mw = max(d.textlength(l, font=font(F_SEMI, 36)) for l in lines) + 60
            y0 = 290 + int(30 * (1 - out_cubic(kr)))
            d.rounded_rectangle([w - 40 - mw, y0, w - 40, y0 + rh], radius=34, fill=(*ETSY, al))
            for i, l in enumerate(lines):
                d.text((w - 40 - mw + 30, y0 + 45 + i * 50), l, font=font(F_SEMI, 36), fill=(255, 255, 255, al), anchor="lm")
            d.text((w - 44, y0 + rh + 30), "Sent in 2 taps", font=font(F_XB, 28), fill=(20, 150, 70, al), anchor="rm")
    # composer with saved-replies button
    d.rounded_rectangle([30, h - 120, w - 30, h - 30], radius=45, fill=(255, 255, 255, 255))
    d.text((80, h - 75), "Type a message", font=font(F_SEMI, 34), fill=(*GREY, 255), anchor="lm")
    btn_k = 1 + 0.12 * math.sin(t * 10) * (open_at is not None and open_at - 0.6 < t < open_at)
    d.rounded_rectangle([w - 300, h - 108, w - 44, h - 42], radius=33, fill=(*ETSY, 255))
    d.text((w - 172, h - 75), "Saved replies", font=font(F_XB, int(30 * btn_k)), fill=(255, 255, 255, 255), anchor="mm")
    # picker sheet
    if open_at is not None:
        ko = out_cubic(p(t, open_at, 0.4)) * (1 - out_cubic(p(t, pick_at + 0.3, 0.3)) if pick_at is not None else 1)
        if ko > 0:
            sh = 110 + 96 * len(items)
            sy = h - 140 - sh * ko
            sheet = Image.new("RGBA", (w - 60, sh), (0, 0, 0, 0))
            sd = ImageDraw.Draw(sheet)
            sd.rounded_rectangle([0, 0, w - 61, sh - 1], radius=34, fill=(255, 255, 255, 255), outline=(225, 228, 236, 255), width=3)
            sd.text((36, 55), "Saved replies", font=font(F_BLACK, 40), fill=(*INK, 255), anchor="lm")
            for i, (lab, em) in enumerate(items):
                yy = 110 + i * 96
                hl = pick_at is not None and i == pick and t >= pick_at - 0.25
                if hl:
                    sd.rounded_rectangle([16, yy + 4, w - 77, yy + 90], radius=24, fill=(255, 232, 214, 255))
                e = emoji_img(em, 48)
                sheet.alpha_composite(e, (40, yy + 47 - e.height // 2))
                sd.text((110, yy + 47), lab, font=font(F_XB, 36), fill=(*INK, 255), anchor="lm")
            sheet = with_alpha(sheet, ko)
            c.alpha_composite(sheet, (30, int(sy)))
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(top + 60 * (1 - out_cubic(k)))))


def reply_doc(sub, t, start, top, blocks, w=880, h=1140, title="Holiday saved replies"):
    """Docs-style page. blocks: list of (question, reply, appear_time, type_dur). [BRACKETS] highlighted."""
    k = p(t, start, 0.4)
    if k <= 0: return
    c, d = card_base(w, h, radius=36, fill=(255, 255, 255, 255))
    d.rounded_rectangle([0, 0, w - 1, 110], radius=36, fill=(236, 241, 251, 255))
    d.rectangle([0, 70, w - 1, 110], fill=(236, 241, 251, 255))
    d.rounded_rectangle([34, 28, 84, 84], radius=8, fill=(66, 133, 244, 255))
    for i in range(3):
        d.line([46, 44 + i * 12, 72, 44 + i * 12], fill=(255, 255, 255, 255), width=4)
    d.text((104, 56), title, font=font(F_XB, 36), fill=(*INK, 255), anchor="lm")
    d.text((w - 36, 56), "Free", font=font(F_XB, 30), fill=(20, 150, 70, 255), anchor="rm")
    y = 150
    fq = font(F_BLACK, 38)
    fr = font(F_SEMI, 34)
    for q, r, at, td in blocks:
        kk = p(t, at, 0.3)
        if kk <= 0: continue
        al = int(255 * out_cubic(kk))
        d.text((50, y + 24), q, font=fq, fill=(*INK, al), anchor="lm")
        y += 66
        n = int(len(r) * p(t, at + 0.3, td))
        lines = textwrap.wrap(r, 40)
        shown = 0
        for l in lines:
            if shown >= n: break
            part = l[:max(0, n - shown)]
            shown += len(l) + 1
            # draw with [BRACKET] highlight
            x = 50
            for tok in re.split(r"(\[[^\]]*\]?)", part):
                if not tok: continue
                tw = d.textlength(tok, font=fr)
                if tok.startswith("["):
                    d.rounded_rectangle([x - 4, y + 2, x + tw + 4, y + 46], radius=10, fill=(255, 236, 150, al))
                d.text((x, y + 24), tok, font=fr, fill=(60, 66, 80, al), anchor="lm")
                x += tw
            y += 50
        y += 34
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(top + 60 * (1 - out_cubic(k)))))


def faq_row(sub, t, start, cy, emoji, color, shop, faqs, flag_at, w=880, h=170):
    """Shop row: FAQ count; 0 FAQs gets flagged as a lead."""
    k = p(t, start, 0.4)
    if k <= 0: return
    c, d = card_base(w, h, radius=34, fill=(255, 255, 255, 255))
    d.ellipse([30, 35, 130, 135], fill=(*color, 255))
    e = emoji_img(emoji, 60)
    c.alpha_composite(e, (80 - e.width // 2, 85 - e.height // 2))
    d.text((160, 60), shop, font=font(F_XB, 40), fill=(*INK, 255), anchor="lm")
    d.text((160, 115), f"Shop FAQs: {faqs}", font=font(F_SEMI, 34), fill=(*GREY, 255), anchor="lm")
    kf = p(t, flag_at, 0.35)
    if kf > 0:
        good = faqs > 0
        lab = "Has FAQs" if good else "Lead!"
        col = (220, 222, 230) if good else (255, 214, 92)
        f = font(F_BLACK, 36)
        tw = d.textlength(lab, font=f)
        s = out_back(kf)
        cx, cyy = w - 50 - tw / 2 - 30, h / 2
        d.rounded_rectangle([cx - (tw / 2 + 30) * s, cyy - 36 * s, cx + (tw / 2 + 30) * s, cyy + 36 * s], radius=36, fill=(*col, 255))
        if s > 0.6:
            d.text((cx, cyy), lab, font=f, fill=(*INK, 255), anchor="mm")
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2 + 80 * (1 - out_cubic(k))), int(cy - h / 2)))


def shop_faq_page(sub, t, start, top, shop="Pine & Paper Co.", emoji="🎄", scroll_at=None, flag_at=None, w=880, h=900):
    """Etsy-style shop page scrolled to the FAQ section, which is empty."""
    k = p(t, start, 0.4)
    if k <= 0: return
    c, d = card_base(w, h, radius=40, fill=(255, 255, 255, 255))
    sc = out_cubic(p(t, scroll_at, 0.9)) if scroll_at is not None else 0
    off = int(-360 * sc)
    # banner
    d.rectangle([0, 0 + off, w, 260 + off], fill=(255, 226, 205, 255))
    e = emoji_img(emoji, 150)
    c.alpha_composite(e, (w // 2 - e.width // 2, 130 + off - e.height // 2))
    d.text((44, 320 + off), shop, font=font(F_BLACK, 48), fill=(*INK, 255), anchor="lm")
    d.text((44, 380 + off), "★★★★★  · Handmade ornaments", font=font(F_SEMI, 32), fill=(*GREY, 255), anchor="lm")
    for i, lab in enumerate(["Items", "Reviews", "About", "Shop policies", "FAQs"]):
        y = 460 + i * 110 + off
        d.line([44, y, w - 44, y], fill=(232, 235, 240, 255), width=2)
        d.text((44, y + 55), lab, font=font(F_XB, 40), fill=(*INK, 255), anchor="lm")
    yf = 460 + 4 * 110 + 120 + off
    d.rounded_rectangle([44, yf, w - 44, yf + 200], radius=26, fill=(246, 247, 250, 255), outline=(225, 228, 236, 255), width=3)
    d.text((w / 2, yf + 100), "No FAQs added yet", font=font(F_XB, 40), fill=(*GREY, 255), anchor="mm")
    if flag_at is not None:
        kf = p(t, flag_at, 0.4)
        if kf > 0:
            r = 1 + 0.03 * math.sin(t * 8)
            d.rounded_rectangle([30, yf - 14, w - 30, yf + 214], radius=34, outline=(235, 64, 52, int(255 * out_cubic(kf))), width=int(8 * r))
    # chrome bar
    d.rounded_rectangle([0, 0, w - 1, 90], radius=40, fill=(245, 246, 250, 255))
    d.rectangle([0, 50, w - 1, 90], fill=(245, 246, 250, 255))
    d.text((44, 45), "Etsy", font=font(F_BLACK, 40), fill=(*ETSY, 255), anchor="lm")
    d.text((w - 44, 45), "sample shop", font=font(F_SEMI, 28), fill=(*GREY, 255), anchor="rm")
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(top + 60 * (1 - out_cubic(k)))))


def clock_math(sub, t, start, cy, left, right, acc, w=880):
    """Two time tiles: 'by hand' vs 'saved reply'."""
    for i, (lab, val, col) in enumerate([left, right]):
        kk = p(t, start + i * 0.5, 0.45)
        if kk <= 0: continue
        cw = 400
        c, d = card_base(cw, 330, radius=36, fill=(255, 255, 255, 255))
        d.text((cw / 2, 70), lab, font=font(F_XB, 36), fill=(*GREY, 255), anchor="mm")
        d.text((cw / 2, 180), val, font=font(F_BLACK, 86), fill=(*col, 255), anchor="mm")
        d.text((cw / 2, 270), "per message", font=font(F_SEMI, 30), fill=(*GREY, 255), anchor="mm")
        c = with_alpha(c, out_cubic(kk))
        x = W / 2 - 440 + i * 480
        sub.alpha_composite(c, (int(x), int(cy - 165 + 60 * (1 - out_cubic(kk)))))
