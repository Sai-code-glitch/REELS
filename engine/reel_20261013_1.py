"""I'd start freelancing with $0: build a portfolio from 3 sample projects."""
from reel_common import *

ACC = (60, 220, 180)    # mint
GOLD = (255, 214, 92)
GREEN = (70, 210, 130)
RED = (255, 96, 110)
bg = Background(top=(4, 26, 26), bottom=(6, 46, 44), blobs=[(40, 200, 160), (60, 140, 255), (255, 200, 80)], seed=131)

SAMPLES = [("Café menu", (255, 196, 140), "☕"), ("Gym flyer", (150, 200, 255), "💪"), ("Bakery post", (255, 170, 190), "🧁")]


def card_base(w, h):
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=34, fill=(250, 250, 252, 255))
    return card, d


def loop_diagram(sub, t, start, cy):
    """No samples -> no clients -> no samples (rotating loop)."""
    k = p(t, start, 0.5)
    if k <= 0: return
    r = 230
    ang = t * 0.9
    d = ImageDraw.Draw(sub)
    a = int(160 * out_cubic(k))
    d.arc([W / 2 - r, cy - r, W / 2 + r, cy + r], start=0, end=360, fill=(255, 255, 255, a), width=8)
    # dots travelling around the loop
    for j in range(4):
        aa = ang + j * math.pi / 2
        x, y = W / 2 + r * math.cos(aa), cy + r * math.sin(aa)
        d.ellipse([x - 14, y - 14, x + 14, y + 14], fill=(*GOLD, a))
    kk1 = p(t, start + 0.3, 0.4); kk2 = p(t, start + 0.9, 0.4)
    pill(sub, W / 2, cy - r, "No samples", F_XB, 50, (255, 236, 238), (190, 30, 50), alpha=out_cubic(kk1), scale=out_back(kk1), icon="📂")
    pill(sub, W / 2, cy + r, "No clients", F_XB, 50, (255, 236, 238), (190, 30, 50), alpha=out_cubic(kk2), scale=out_back(kk2), icon="🙅")
    place_emoji(sub, "🔁", W / 2, cy, 150 * out_back(p(t, start + 1.3, 0.4)), alpha=out_cubic(p(t, start + 1.3, 0.3)), rot=10 * math.sin(t * 3))


def design_canvas(sub, cx, cy, t, start):
    """Canva-style editor building a sample café menu."""
    w, h = 860, 600
    k = p(t, start, 0.45)
    if k <= 0: return
    card, d = card_base(w, h)
    # toolbar
    d.rounded_rectangle([0, 0, w - 1, 80], radius=34, fill=(124, 92, 255, 255))
    d.rectangle([0, 40, w - 1, 80], fill=(124, 92, 255, 255))
    d.text((36, 40), "Free design editor", font=font(F_XB, 36), fill=(255, 255, 255, 255), anchor="lm")
    d.text((w - 36, 40), "SAMPLE", font=font(F_BLACK, 32), fill=(255, 230, 120, 255), anchor="rm")
    # side panel
    d.rectangle([0, 80, 150, h - 34], fill=(236, 238, 244, 255))
    for i, lab in enumerate(["Text", "Photos", "Shapes", "Colors"]):
        d.rounded_rectangle([20, 110 + i * 110, 130, 190 + i * 110], radius=14, fill=(255, 255, 255, 255))
        d.text((75, 150 + i * 110), lab, font=font(F_SEMI, 24), fill=(110, 116, 130, 255), anchor="mm")
    # page
    px0, py0, px1, py1 = 200, 110, w - 50, h - 40
    d.rounded_rectangle([px0, py0, px1, py1], radius=16, fill=(255, 244, 228, 255), outline=(220, 210, 190, 255), width=3)
    kt = out_cubic(p(t, start + 0.6, 0.35))
    if kt > 0:
        d.text(((px0 + px1) / 2, py0 + 60), "CORNER CAFÉ", font=font(F_BLACK, 56), fill=(110, 60, 30, int(255 * kt)), anchor="mm")
        d.line([px0 + 80, py0 + 105, px1 - 80, py0 + 105], fill=(200, 150, 100, int(255 * kt)), width=4)
    items = [("Latte", "$4"), ("Croissant", "$3"), ("Iced mocha", "$5"), ("Bagel", "$3")]
    for i, (n, pr) in enumerate(items):
        kk = out_cubic(p(t, start + 1.0 + i * 0.3, 0.3))
        if kk <= 0: continue
        y = py0 + 165 + i * 72
        x = 30 * (1 - kk)
        d.text((px0 + 50 + x, y), n, font=font(F_SEMI, 40), fill=(80, 50, 30, int(255 * kk)), anchor="lm")
        d.text((px1 - 50 + x, y), pr, font=font(F_XB, 40), fill=(200, 100, 40, int(255 * kk)), anchor="rm")
    card = with_alpha(card, out_cubic(k))
    sub.alpha_composite(card, (int(cx - w / 2), int(cy - h / 2 + 70 * (1 - out_cubic(k)))))
    # cup emoji sticker pops on the page
    ke = p(t, start + 2.3, 0.4)
    place_emoji(sub, "☕", cx - w / 2 + px1 - 20, cy - h / 2 + py1 - 10, 90 * out_back(ke), alpha=out_cubic(ke), rot=12)


def thumbs(sub, t, start, cy, size=230, gap=40, show_labels=True):
    tot = 3 * size + 2 * gap
    x0 = W / 2 - tot / 2
    for i, (lab, col, ic) in enumerate(SAMPLES):
        kk = p(t, start + i * 0.35, 0.4)
        if kk <= 0: continue
        s = out_back(kk)
        tile = Image.new("RGBA", (size, size), (0, 0, 0, 0))
        d = ImageDraw.Draw(tile)
        d.rounded_rectangle([0, 0, size - 1, size - 1], radius=26, fill=(*col, 255))
        d.rounded_rectangle([20, size - 70, size - 20, size - 22], radius=12, fill=(255, 255, 255, 200))
        d.text((size / 2, size - 46), lab, font=font(F_XB, 30), fill=INK, anchor="mm")
        tile.alpha_composite(emoji_img(ic, 100), (int(size / 2 - 50), 35))
        tile = tile.resize((max(1, int(size * s)), max(1, int(size * s))))
        cx = x0 + i * (size + gap) + size / 2
        sub.alpha_composite(with_alpha(tile, out_cubic(kk)), (int(cx - tile.width / 2), int(cy - tile.height / 2)))


def portfolio(sub, cx, cy, t, start, filled_at):
    w, h = 860, 560
    k = p(t, start, 0.45)
    if k <= 0: return
    card, d = card_base(w, h)
    d.ellipse([40, 36, 140, 136], fill=(60, 200, 160, 255))
    d.text((90, 86), "S", font=font(F_BLACK, 52), fill=(255, 255, 255, 255), anchor="mm")
    d.text((170, 66), "Sam · Beginner designer", font=font(F_XB, 40), fill=INK, anchor="lm")
    d.text((170, 112), "Menus · Flyers · Social posts", font=font(F_MED, 32), fill=(110, 116, 130, 255), anchor="lm")
    d.line([40, 170, w - 40, 170], fill=(225, 228, 236, 255), width=3)
    d.text((40, 215), "Portfolio", font=font(F_XB, 36), fill=INK, anchor="lm")
    filled = t >= filled_at
    if not filled:
        d.rounded_rectangle([40, 260, w - 40, 500], radius=22, outline=(200, 206, 220, 255), width=4)
        d.text((w / 2, 380), "0 samples yet", font=font(F_XB, 48), fill=(190, 196, 210, 255), anchor="mm")
    card = with_alpha(card, out_cubic(k))
    sub.alpha_composite(card, (int(cx - w / 2), int(cy - h / 2 + 60 * (1 - out_cubic(k)))))
    if filled:
        thumbs(sub, t, filled_at, cy + 100, size=220, gap=36)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, 0.0, 0.3)
        draw_text(sub, "$0", F_BLACK, 300 * out_back(k), W / 2, 560 + 10 * math.sin(t * 5), GOLD, alpha=k)
        pop_words(sub, ["I'd start freelancing", "with $0.", "Here's how"], t, 0.0, 1000, 96, (WHITE, ACC), gap=0.06, highlight={"$0.", "how"})
        pill(sub, W / 2, 1360, "No courses. No paid tools.", F_SEMI, 46, WHITE, INK, alpha=out_cubic(p(t, 1.3, 0.4)), scale=out_back(p(t, 1.3, 0.4)), icon="🙌")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Beginners get stuck", "in this loop"], t, s1 + 0.1, 360, 86, (WHITE, RED), gap=0.07, highlight={"stuck", "loop"})
        loop_diagram(sub, t, s1 + 0.7, 800)
        kb = p(t, s1 + 3.6, 0.4)
        pop_words(sub, ["Break it with", "proof you make yourself"], t, s1 + 3.6, 1270, 64, (WHITE, ACC), gap=0.06, highlight={"proof"})
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Make 3 sample projects"], t, s2 + 0.1, 320, 84, (WHITE, ACC), gap=0.07, highlight={"3", "sample"})
        if t < s2 + 4.6:
            design_canvas(sub, W / 2, 760, t, s2 + 0.4)
        else:
            thumbs(sub, t, s2 + 4.6, 640)
            checklist(sub, t, s2 + 5.4, ["For made-up businesses", "Label them \"sample\""], 960, 105, ACC, size=52, x0=170, every=0.7)
        pill(sub, W / 2, 1420, "Free tools: Canva or Google Slides", F_SEMI, 42, (230, 255, 246), (10, 110, 80), alpha=out_cubic(p(t, s2 + 2.4, 0.4)), scale=out_back(p(t, s2 + 2.4, 0.4)), icon="🆓")
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Now clients see proof,", "not promises"], t, s3 + 0.1, 330, 76, (WHITE, GOLD), gap=0.06, highlight={"proof,"})
        portfolio(sub, W / 2, 760, t, s3 + 0.4, s3 + 1.8)
        kc = p(t, s3 + 3.6, 1.0)
        if kc > 0:
            draw_text(sub, "Total spent: $0", F_BLACK, 96, W / 2, 1150, GOLD, alpha=out_cubic(p(t, s3 + 3.6, 0.3)), scale=out_back(min(1, kc * 1.5)))
        pill(sub, W / 2, 1300, "Link it in every message you send", F_SEMI, 42, WHITE, INK, alpha=out_cubic(p(t, s3 + 4.4, 0.4)), scale=out_back(p(t, s3 + 4.4, 0.4)), icon="🔗")
        draw_text(sub, "Results depend on your work.", F_MED, 36, W / 2, 1430, SOFT, alpha=out_cubic(p(t, s3 + 4.8, 0.5)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel1.mp4")
