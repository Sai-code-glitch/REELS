"""Animated 30s vertical Reel renderer (1080x1920, 30fps) using PIL frames piped to ffmpeg."""
import math, random, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H, FPS = 1080, 1920, 30
F_BLACK = "/usr/share/fonts/opentype/inter/InterDisplay-Black.otf"
F_XB = "/usr/share/fonts/opentype/inter/InterDisplay-ExtraBold.otf"
F_SEMI = "/usr/share/fonts/opentype/inter/Inter-SemiBold.otf"
F_MED = "/usr/share/fonts/opentype/inter/Inter-Medium.otf"
F_EMOJI = "/usr/share/fonts/truetype/noto/NotoColorEmoji.ttf"

_font_cache = {}
def font(path, size):
    size = max(4, int(size))
    k = (path, size)
    if k not in _font_cache:
        _font_cache[k] = ImageFont.truetype(path, size)
    return _font_cache[k]

_emoji_cache = {}
def emoji_img(ch, px):
    """Noto Color Emoji only renders at 109px; render once then scale."""
    if ch not in _emoji_cache:
        f = ImageFont.truetype(F_EMOJI, 109)
        im = Image.new("RGBA", (160, 160), (0, 0, 0, 0))
        ImageDraw.Draw(im).text((10, 10), ch, font=f, embedded_color=True)
        _emoji_cache[ch] = im.crop(im.getbbox())
    base = _emoji_cache[ch]
    s = px / base.height
    return base.resize((max(1, int(base.width * s)), max(1, int(px))), Image.LANCZOS)

# ---------- easing ----------
def clamp(x, a=0.0, b=1.0): return max(a, min(b, x))
def p(t, start, dur): return clamp((t - start) / dur)
def out_cubic(x): return 1 - (1 - x) ** 3
def in_out(x): return 3 * x * x - 2 * x * x * x
def out_back(x, s=1.7):
    x -= 1
    return x * x * ((s + 1) * x + s) + 1
def lerp(a, b, x): return a + (b - a) * x

# ---------- background ----------
class Background:
    def __init__(self, top, bottom, blobs, seed=3):
        g = np.linspace(0, 1, H)[:, None, None]
        top, bottom = np.array(top)[None, None, :], np.array(bottom)[None, None, :]
        arr = (top * (1 - g) + bottom * g).repeat(W, axis=1).astype(np.uint8)
        self.base = Image.fromarray(arr, "RGB").convert("RGBA")
        self.sprites = []
        for col in blobs:
            r = 380
            yy, xx = np.mgrid[-r:r, -r:r]
            d = np.sqrt(xx ** 2 + yy ** 2) / r
            a = (np.clip(1 - d, 0, 1) ** 2.2 * 110).astype(np.uint8)
            im = np.zeros((2 * r, 2 * r, 4), np.uint8)
            im[..., :3] = col
            im[..., 3] = a
            self.sprites.append(Image.fromarray(im, "RGBA"))
        rnd = random.Random(seed)
        self.dots = [(rnd.uniform(0, W), rnd.uniform(0, H), rnd.uniform(2, 5), rnd.uniform(20, 70), rnd.uniform(0, 6.28)) for _ in range(46)]

    def frame(self, t):
        im = self.base.copy()
        paths = [(0.25, 0.22, 0.19, 0.11), (0.75, 0.55, 0.23, 0.13), (0.4, 0.85, 0.17, 0.09)]
        for spr, (cx, cy, ax, ay) in zip(self.sprites, paths):
            x = int(cx * W + ax * W * math.sin(t * 0.35 + cx * 6) - spr.width / 2)
            y = int(cy * H + ay * H * math.cos(t * 0.28 + cy * 5) - spr.height / 2)
            x = int(clamp(x, 0, W - spr.width)); y = int(clamp(y, 0, H - spr.height))
            im.alpha_composite(spr, (x, y))
        d = ImageDraw.Draw(im)
        for (x, y, r, sp, ph) in self.dots:
            yy = (y - sp * t) % H
            xx = x + 12 * math.sin(t + ph)
            a = int(60 + 50 * math.sin(t * 2 + ph))
            d.ellipse([xx - r, yy - r, xx + r, yy + r], fill=(255, 255, 255, max(0, a)))
        return im

# ---------- drawing helpers (on an RGBA overlay) ----------
def text_w(s, f, d): return d.textlength(s, font=f)

def draw_text(layer, s, path, size, cx, cy, fill, alpha=1.0, anchor="mm", scale=1.0):
    if alpha <= 0.01 or scale <= 0.01: return
    d = ImageDraw.Draw(layer)
    f = font(path, size * scale)
    c = (*fill[:3], int(255 * alpha))
    d.text((cx, cy), s, font=f, fill=c, anchor=anchor)

def pop_words(layer, lines, t, start, cy, size, colors, gap=0.11, path=F_BLACK, line_h=1.12, highlight=None):
    """Kinetic typography: each word scales in with an overshoot, line by line."""
    d = ImageDraw.Draw(layer)
    f = font(path, size)
    sp = text_w(" ", f, d)
    total_h = size * line_h * len(lines)
    y = cy - total_h / 2 + size * line_h / 2
    i = 0
    for li, line in enumerate(lines):
        words = line.split(" ")
        widths = [text_w(w, f, d) for w in words]
        x = W / 2 - (sum(widths) + sp * (len(words) - 1)) / 2
        for w, ww in zip(words, widths):
            k = p(t, start + i * gap, 0.38)
            if k > 0:
                s = out_back(k)
                col = colors[1] if (highlight and w.strip(".,!?").lower() in highlight) else colors[0]
                draw_text(layer, w, path, size, x + ww / 2, y + (1 - out_cubic(k)) * 40, col, alpha=out_cubic(k), scale=s)
            x += ww + sp
            i += 1
        y += size * line_h
    return start + i * gap

def pill(layer, cx, cy, label, path, size, bg, fg, alpha=1.0, scale=1.0, pad=(36, 18), icon=None):
    if alpha <= 0.01 or scale <= 0.01: return
    d = ImageDraw.Draw(layer)
    f = font(path, size * scale)
    tw = text_w(label, f, d)
    ic = int(size * 1.15 * scale) if icon else 0
    w = tw + 2 * pad[0] * scale + (ic + 14 * scale if icon else 0)
    h = size * scale + 2 * pad[1] * scale
    x0, y0 = cx - w / 2, cy - h / 2
    d.rounded_rectangle([x0, y0, x0 + w, y0 + h], radius=h / 2, fill=(*bg[:3], int(255 * alpha)))
    tx = x0 + pad[0] * scale
    if icon:
        e = emoji_img(icon, ic)
        if alpha < 1:
            e = e.copy(); e.putalpha(e.getchannel("A").point(lambda v: int(v * alpha)))
        layer.alpha_composite(e, (int(tx), int(cy - e.height / 2)))
        tx += ic + 14 * scale
    d.text((tx, cy), label, font=f, fill=(*fg[:3], int(255 * alpha)), anchor="lm")

def place_emoji(layer, ch, cx, cy, px, alpha=1.0, rot=0.0):
    if alpha <= 0.01 or px < 4: return
    e = emoji_img(ch, px)
    if rot: e = e.rotate(rot, resample=Image.BICUBIC, expand=True)
    if alpha < 1:
        e = e.copy(); e.putalpha(e.getchannel("A").point(lambda v: int(v * alpha)))
    layer.alpha_composite(e, (int(cx - e.width / 2), int(cy - e.height / 2)))

def progress_bar(layer, t, scenes, total, accent):
    d = ImageDraw.Draw(layer)
    n = len(scenes); gap = 10; x0, x1, y = 60, W - 60, 150
    seg = (x1 - x0 - gap * (n - 1)) / n
    for i, (s, e) in enumerate(scenes):
        sx = x0 + i * (seg + gap)
        d.rounded_rectangle([sx, y, sx + seg, y + 8], radius=4, fill=(255, 255, 255, 60))
        k = clamp((t - s) / (e - s))
        if k > 0:
            d.rounded_rectangle([sx, y, sx + max(8, seg * k), y + 8], radius=4, fill=(*accent, 255))

def render(scene_fn, out_path, duration=30.0, bg=None):
    proc = subprocess.Popen(
        ["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
         "-f", "lavfi", "-i", "anullsrc=r=44100:cl=stereo", "-t", str(duration),
         "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p", "-c:a", "aac", "-shortest",
         "-movflags", "+faststart", out_path], stdin=subprocess.PIPE)
    n = int(duration * FPS)
    for i in range(n):
        t = i / FPS
        frame = bg.frame(t)
        layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
        scene_fn(layer, t)
        frame.alpha_composite(layer)
        proc.stdin.write(frame.convert("RGB").tobytes())
    proc.stdin.close()
    proc.wait()
    return out_path
