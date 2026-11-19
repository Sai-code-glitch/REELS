"""Helpers for the 2026-11-19 'short video editing side gig' reels
(Instagram Reels-tab check, phone video-editor timeline, 9:16 Reel preview playing,
raw clips flying into one Reel). Shop names are fictional samples."""
from reel_insta import *
from reel_chat import phone_chat

CLIPS = [("☕", (120, 72, 48), "Pour"), ("🥐", (226, 170, 96), "Tray"),
         ("🧁", (236, 140, 170), "Close-up"), ("👋", (90, 150, 210), "Hello")]
OVERLAY = ["NEW:", "Peppermint", "mocha"]
TEAL = (40, 200, 190)


def clip_tile(c, d, x, y, w, h, i, alpha=1.0, radius=14, label=True):
    em, col, lab = CLIPS[i % 4]
    al = int(255 * alpha)
    d.rounded_rectangle([x, y, x + w, y + h], radius=radius, fill=(*col, al))
    d.rounded_rectangle([x, y + h * 0.62, x + w, y + h], radius=radius, fill=(0, 0, 0, int(60 * alpha)))
    e = emoji_img(em, int(min(w, h) * 0.5))
    c.alpha_composite(with_alpha(e.copy(), alpha), (int(x + w / 2 - e.width / 2), int(y + h * 0.36 - e.height / 2)))
    if label and w > 90:
        d.text((x + w / 2, y + h * 0.81), lab, font=font(F_XB, max(14, int(h * 0.13))), fill=(255, 255, 255, al), anchor="mm")


def reel_frame(c, d, x, y, w, t, overlay_a=1.0, clip_dur=0.7, paused=None):
    """A 9:16 Reel playing: cycles through the 4 clips, overlay text on top."""
    h = int(w * 16 / 9)
    i = paused if paused is not None else int(t / clip_dur) % 4
    em, col, _ = CLIPS[i]
    d.rounded_rectangle([x, y, x + w, y + h], radius=int(w * 0.06), fill=(*col, 255))
    lt = (t % clip_dur) / clip_dur if paused is None else 0.5
    zoom = 1 + 0.12 * lt
    e = emoji_img(em, int(w * 0.48 * zoom))
    c.alpha_composite(e, (int(x + w / 2 - e.width / 2), int(y + h * 0.56 - e.height / 2)))
    if overlay_a > 0:
        al = int(255 * overlay_a)
        bw = w * 0.82
        d.rounded_rectangle([x + (w - bw) / 2, y + h * 0.13, x + (w + bw) / 2, y + h * 0.33], radius=int(w * 0.04), fill=(255, 255, 255, al))
        fs = int(w * 0.105)
        d.text((x + w / 2, y + h * 0.18), OVERLAY[0], font=font(F_BLACK, fs * 0.8), fill=(220, 40, 60, al), anchor="mm")
        d.text((x + w / 2, y + h * 0.235), OVERLAY[1], font=font(F_BLACK, fs), fill=(*INK, al), anchor="mm")
        d.text((x + w / 2, y + h * 0.29), OVERLAY[2] + " ☕"[:0], font=font(F_BLACK, fs), fill=(*INK, al), anchor="mm")
    # progress line at bottom
    d.rounded_rectangle([x + w * 0.06, y + h - w * 0.06, x + w * 0.94, y + h - w * 0.045], radius=3, fill=(255, 255, 255, 90))
    pk = ((t % (clip_dur * 4)) / (clip_dur * 4)) if paused is None else 0.4
    d.rounded_rectangle([x + w * 0.06, y + h - w * 0.06, x + w * 0.06 + w * 0.88 * pk, y + h - w * 0.045], radius=3, fill=(255, 255, 255, 255))
    return h


def phone_reel(sub, t, start, cx, cy, w=420, overlay_at=None, rot=0.0, label=None, label_col=None):
    k = p(t, start, 0.45)
    if k <= 0: return
    h = int(w * 16 / 9)
    pad = 26
    c = Image.new("RGBA", (w + 2 * pad, h + 2 * pad), (0, 0, 0, 0))
    d = ImageDraw.Draw(c)
    d.rounded_rectangle([0, 0, w + 2 * pad - 1, h + 2 * pad - 1], radius=int(w * 0.1), fill=(16, 18, 26, 255), outline=(80, 86, 104, 255), width=4)
    oa = 1.0 if overlay_at is None else out_cubic(p(t, overlay_at, 0.4))
    reel_frame(c, d, pad, pad, w, t, overlay_a=oa)
    s = 0.6 + 0.4 * out_back(k)
    c = c.resize((max(1, int(c.width * s)), max(1, int(c.height * s))), Image.LANCZOS)
    if rot: c = c.rotate(rot, resample=Image.BICUBIC, expand=True)
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(cx - c.width / 2), int(cy - c.height / 2)))
    if label:
        pill(sub, cx, cy - c.height / 2 - 4, label, F_BLACK, 40, label_col or (255, 214, 92), INK, alpha=out_cubic(k))


def editor_ui(sub, t, start, cy, steps, labels=None, w=880, h=1180, acc=TEAL):
    """Phone video editor. steps = times for [import clips, trim, add text, export]."""
    k = p(t, start, 0.45)
    if k <= 0: return
    c, d = card_base(w, h, radius=48, fill=(22, 24, 32, 255))
    # top bar
    d.text((44, 60), "✕", font=font(DEJAVU, 40), fill=(200, 204, 214, 255), anchor="lm")
    d.text((w / 2, 60), "Edit video", font=font(F_XB, 38), fill=(255, 255, 255, 255), anchor="mm")
    ke = out_cubic(p(t, steps[3], 0.35))
    ec = tuple(int(lerp(70, v, ke)) for v in acc)
    d.rounded_rectangle([w - 220, 30, w - 36, 90], radius=30, fill=(*ec, 255))
    d.text((w - 128, 60), "Export", font=font(F_BLACK, 32), fill=(255, 255, 255, 255), anchor="mm")
    # preview
    pw = 420
    ph = int(pw * 16 / 9)
    px, py = (w - pw) / 2, 120
    ki = out_cubic(p(t, steps[0], 0.4))
    if ki > 0.02:
        reel_frame(c, d, px, py, pw, t, overlay_a=out_cubic(p(t, steps[2], 0.4)))
        if ki < 1:
            d.rounded_rectangle([px, py, px + pw, py + ph], radius=20, fill=(22, 24, 32, int(255 * (1 - ki))))
    else:
        d.rounded_rectangle([px, py, px + pw, py + ph], radius=20, outline=(70, 76, 96, 255), width=4)
        d.text((px + pw / 2, py + ph / 2), "+ Add clips", font=font(F_XB, 36), fill=(150, 156, 170, 255), anchor="mm")
    # timeline
    ty = py + ph + 40
    d.text((44, ty), "0:00", font=font(F_SEMI, 26), fill=(150, 156, 170, 255), anchor="lm")
    kt = p(t, steps[1], 1.6)
    total = lerp(47, 13, out_cubic(kt))
    d.text((w - 44, ty), f"0:{int(round(total)):02d}", font=font(F_XB, 30), fill=(*acc, 255) if kt > 0 else (150, 156, 170, 255), anchor="rm")
    vy = ty + 40
    lens_raw = [14, 11, 12, 10]
    lens_cut = [3.5, 3, 3.5, 3]
    span = w - 88
    scale = span / 47
    x = 44
    for i in range(4):
        kc = out_cubic(p(t, steps[0] + 0.15 * i, 0.35))
        if kc <= 0: continue
        ln = lerp(lens_raw[i], lens_cut[i], out_cubic(p(t, steps[1] + 0.3 * i, 0.6)))
        cw = ln * scale * kc
        clip_tile(c, d, x, vy, max(8, cw - 6), 110, i, alpha=kc, label=True)
        if steps[1] <= t < steps[1] + 2.4 and kc >= 1:
            d.rounded_rectangle([x, vy, x + max(8, cw - 6), vy + 110], radius=14, outline=(255, 214, 92, 255), width=5)
        x += cw
    # text track
    kx = out_cubic(p(t, steps[2], 0.4))
    if kx > 0:
        txw = (x - 44) * kx
        d.rounded_rectangle([44, vy + 128, 44 + max(10, txw - 6), vy + 188], radius=12, fill=(255, 214, 92, 255))
        if txw > 260:
            d.text((64, vy + 158), "T  NEW: Peppermint mocha", font=font(F_XB, 26), fill=(*INK, 255), anchor="lm")
    # playhead
    if ki > 0.5:
        ph_x = 44 + (x - 44) * ((t * 0.35) % 1)
        d.line([ph_x, vy - 14, ph_x, vy + 200], fill=(255, 255, 255, 255), width=4)
    # export sheet
    if ke > 0:
        sy = h - 170 * ke
        d.rounded_rectangle([20, sy, w - 20, h + 40], radius=36, fill=(255, 255, 255, 255))
        d.text((60, sy + 60), "1080 × 1920  ·  30 fps", font=font(F_XB, 36), fill=(*INK, 255), anchor="lm")
        d.text((60, sy + 112), "9:16 vertical", font=font(F_SEMI, 30), fill=(*GREY, 255), anchor="lm")
        place_emoji(c, "✅", w - 90, sy + 85, 70, alpha=out_cubic(p(t, steps[3] + 0.4, 0.3)))
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(cy - h / 2 + 60 * (1 - out_cubic(k)))))
    if labels:
        for i, (lab, at) in enumerate(zip(labels, steps)):
            kl = p(t, at, 0.3)
            nxt = steps[i + 1] if i + 1 < len(steps) else 99
            if kl > 0 and t < nxt:
                pill(sub, W / 2, cy + h / 2 + 50, lab, F_BLACK, 46, (255, 214, 92), INK, alpha=out_cubic(kl), scale=out_back(kl))


def reels_tab(sub, t, start, top, flag_at, handle="@pinecupcafe", w=880, h=900):
    """Profile with a grid/Reels tab switch: photo grid, then Reels tab shows 'No Reels yet'."""
    k = p(t, start, 0.45)
    if k <= 0: return
    c, d = card_base(w, h, radius=40, fill=(255, 255, 255, 255))
    ring_avatar(c, d, 120, 120, 66, "☕", (120, 72, 48), ring=False)
    d.text((230, 86), handle, font=font(F_BLACK, 44), fill=(*INK, 255), anchor="lm")
    d.text((230, 146), "Café · Coffee & pastries", font=font(F_SEMI, 32), fill=(*GREY, 255), anchor="lm")
    ks = out_cubic(p(t, flag_at - 0.9, 0.4))  # switch to Reels tab
    ty = 240
    d.line([0, ty + 70, w, ty + 70], fill=(*LINE, 255), width=2)
    for i, lab in enumerate(["Posts", "▶  Reels"]):
        cx = w * (0.25 + 0.5 * i)
        on = (1 - ks) if i == 0 else ks
        col = tuple(int(lerp(GREY[j], INK[j], on)) for j in range(3))
        d.text((cx, ty + 35), lab, font=font(DEJAVU if False else F_XB, 36), fill=(*col, 255), anchor="mm")
    ux = lerp(w * 0.05, w * 0.55, ks)
    d.rectangle([ux, ty + 66, ux + w * 0.4, ty + 72], fill=(*INK, 255))
    gy = ty + 80
    sz = (w - 12) / 3
    if ks < 1:
        tiles = ["☕", "🥐", "🧁", "☕", "🍪", "🥐"]
        cols = [(214, 180, 150), (250, 214, 165), (250, 205, 220), (200, 170, 140), (240, 220, 190), (245, 200, 150)]
        for i in range(6):
            r, cc = divmod(i, 3)
            x0, y0 = cc * (sz + 6), gy + r * (sz + 6)
            a = (1 - ks) * out_cubic(p(t, start + 0.2 + 0.05 * i, 0.3))
            d.rectangle([x0, y0, x0 + sz, y0 + sz], fill=(*cols[i], int(255 * a)))
            c.alpha_composite(with_alpha(emoji_img(tiles[i], 90).copy(), a), (int(x0 + sz / 2 - 45), int(y0 + sz / 2 - 45)))
    if ks > 0:
        al = int(255 * ks)
        d.ellipse([w / 2 - 70, gy + 120, w / 2 + 70, gy + 260], outline=(*INK, al), width=6)
        d.polygon([(w / 2 - 22, gy + 155), (w / 2 - 22, gy + 225), (w / 2 + 36, gy + 190)], fill=(*INK, al))
        d.text((w / 2, gy + 320), "No Reels yet", font=font(F_BLACK, 54), fill=(*INK, al), anchor="mm")
        d.text((w / 2, gy + 385), "Only photos since spring", font=font(F_SEMI, 34), fill=(*GREY, al), anchor="mm")
    kf = p(t, flag_at, 0.4)
    if kf > 0:
        kb = max(0.02, out_back(kf))
        bw, bh = 420 * kb, 96 * kb
        cy = h - 90
        d.rounded_rectangle([w / 2 - bw / 2, cy - bh / 2, w / 2 + bw / 2, cy + bh / 2], radius=bh / 2, fill=(*RED, 255))
        d.text((w / 2, cy), "0 Reels = a lead", font=font(F_BLACK, 42 * kb), fill=(255, 255, 255, 255), anchor="mm")
    c = with_alpha(c, out_cubic(k))
    sub.alpha_composite(c, (int(W / 2 - w / 2), int(top + 70 * (1 - out_cubic(k)))))


def clips_to_reel(sub, t, start, cy, merge_at):
    """4 raw clips (with long durations) fly into a single 9:16 Reel."""
    durs = ["0:14", "0:11", "0:12", "0:10"]
    km = in_out(p(t, merge_at, 0.9))
    tw, th = 190, 300
    for i in range(4):
        ka = out_cubic(p(t, start + 0.2 * i, 0.4))
        if ka <= 0: continue
        x0 = 120 + i * 220 + tw / 2
        y0 = cy - 220
        tx, ty = W / 2, cy + 170
        x = lerp(x0, tx, km); y = lerp(y0, ty, km)
        sc = lerp(1, 0.3, km)
        a = ka * (1 - p(t, merge_at + 0.7, 0.2))
        if a <= 0.01: continue
        tile = Image.new("RGBA", (tw, th), (0, 0, 0, 0))
        td = ImageDraw.Draw(tile)
        clip_tile(tile, td, 0, 0, tw - 1, th - 1, i, alpha=1.0, radius=20)
        td.rounded_rectangle([tw - 100, 12, tw - 12, 56], radius=20, fill=(0, 0, 0, 160))
        td.text((tw - 56, 34), durs[i], font=font(F_XB, 26), fill=(255, 255, 255, 255), anchor="mm")
        tile = tile.resize((max(1, int(tw * sc)), max(1, int(th * sc))), Image.LANCZOS)
        tile = tile.rotate((i - 1.5) * 4 * (1 - km), resample=Image.BICUBIC, expand=True)
        sub.alpha_composite(with_alpha(tile, a), (int(x - tile.width / 2), int(y - tile.height / 2)))
    if t >= merge_at + 0.6:
        phone_reel(sub, t, merge_at + 0.6, W / 2, cy + 170, w=300)
