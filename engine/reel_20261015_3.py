"""Nobody tells you how to deliver a Canva template (Canva templates to sell before the holidays, part 3)."""
from reel_common import *

ACC = (255, 150, 50)    # orange
GOLD = (255, 214, 92)
GREEN = (60, 205, 130)
RED = (255, 96, 110)
PURPLE = (124, 77, 255)
bg = Background(top=(10, 16, 40), bottom=(20, 34, 80), blobs=[(255, 140, 40), (60, 120, 255), (40, 200, 220)], seed=2883)


def share_menu(sub, t, start, cy=860):
    """Mock design-app share panel: Share click -> Template link -> Copied toast."""
    k = p(t, start, 0.45)
    if k <= 0: return
    w, h = 860, 860
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=40, fill=(242, 244, 248, 255))
    d.rounded_rectangle([0, 0, w - 1, 100], radius=40, fill=(*PURPLE, 255))
    d.rectangle([0, 60, w - 1, 100], fill=(*PURPLE, 255))
    d.text((40, 50), "Holiday Sale Pack", font=font(F_XB, 36), fill=(255, 255, 255, 255), anchor="lm")
    kc = p(t, start + 0.8, 0.25)
    press = 1 - 0.08 * math.sin(math.pi * kc)
    bw, bh = 170 * press, 56 * press
    d.rounded_rectangle([w - 120 - bw / 2, 50 - bh / 2, w - 120 + bw / 2, 50 + bh / 2], radius=28, fill=(255, 255, 255, 255))
    d.text((w - 120, 50), "Share", font=font(F_XB, 30), fill=(*PURPLE, 255), anchor="mm")
    km = p(t, start + 1.1, 0.35)
    if km > 0:
        a = int(255 * out_cubic(km))
        mx0, my0 = 120, 140
        d.rounded_rectangle([mx0, my0, w - 40, my0 + 560], radius=30, fill=(255, 255, 255, a), outline=(220, 222, 230, a), width=3)
        d.text((mx0 + 40, my0 + 60), "Share this design", font=font(F_BLACK, 42), fill=(*INK, a), anchor="lm")
        opts = ["Download", "Present", "View-only link", "Template link"]
        sel = p(t, start + 2.3, 0.3)
        for i, lab in enumerate(opts):
            y = my0 + 160 + i * 105
            hl = i == 3 and sel > 0
            if hl:
                d.rounded_rectangle([mx0 + 20, y - 44, w - 60, y + 44], radius=22, fill=(255, 236, 214, a), outline=(*ACC, a), width=5)
            d.text((mx0 + 50, y), lab, font=font(F_XB if hl else F_SEMI, 42), fill=(*INK, a), anchor="lm")
        kt = p(t, start + 3.4, 0.35)
        if kt > 0:
            at = int(255 * out_cubic(kt))
            d.rounded_rectangle([140, h - 120, w - 140, h - 40], radius=40, fill=(30, 34, 46, at))
            d.text((w / 2, h - 80), "Link copied!", font=font(F_XB, 38), fill=(*GREEN, at), anchor="mm")
    sub.alpha_composite(with_alpha(im, out_cubic(k)), (int(W / 2 - w / 2), int(cy - h / 2 + 60 * (1 - out_cubic(k)))))


def pdf_page(sub, t, start, cx, cy):
    k = p(t, start, 0.45)
    if k <= 0: return
    w, h = 600, 760
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=26, fill=(255, 255, 255, 255))
    d.polygon([(w - 110, 0), (w, 0), (w, 110)], fill=(230, 232, 240, 255))
    d.rounded_rectangle([40, 40, 160, 90], radius=12, fill=(220, 60, 60, 255))
    d.text((100, 65), "PDF", font=font(F_BLACK, 32), fill=(255, 255, 255, 255), anchor="mm")
    d.text((w / 2, 200), "Your Holiday", font=font(F_BLACK, 56), fill=(*INK, 255), anchor="mm")
    d.text((w / 2, 265), "Sale Pack", font=font(F_BLACK, 56), fill=(*INK, 255), anchor="mm")
    d.text((w / 2, 360), "Thanks for your order!", font=font(F_SEMI, 34), fill=(100, 106, 120, 255), anchor="mm")
    kb = p(t, start + 0.8, 0.4)
    bw = 440 * (0.7 + 0.3 * out_back(kb)) if kb > 0 else 0
    if bw > 0:
        d.rounded_rectangle([w / 2 - bw / 2, 450, w / 2 + bw / 2, 550], radius=50, fill=(*PURPLE, 255))
        d.text((w / 2, 500), "Open your template", font=font(F_XB, 36), fill=(255, 255, 255, 255), anchor="mm")
    d.text((w / 2, 630), "Free Canva account works", font=font(F_MED, 30), fill=(100, 106, 120, 255), anchor="mm")
    sub.alpha_composite(with_alpha(im, out_cubic(k)), (int(cx - w / 2), int(cy - h / 2 + 60 * (1 - out_cubic(k)))))


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, 0.0, 0.3)
        place_emoji(sub, "🔗", W / 2, 500 + 12 * math.sin(t * 6), 200 * out_back(k), alpha=k, rot=6 * math.sin(t * 4))
        pop_words(sub, ["Nobody tells you", "how to deliver a", "Canva template"], t, 0.0, 930, 100, (WHITE, ACC), gap=0.07, highlight={"deliver", "canva", "template"})
        kk = p(t, 1.3, 0.4)
        pill(sub, W / 2, 1280, "Do it this way, not by email", F_SEMI, 46, WHITE, INK, alpha=out_cubic(kk), scale=out_back(kk), icon="📩")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Beginners send this:"], t, s1 + 0.1, 340, 80, (WHITE, RED), gap=0.07, highlight={"this:"})
        wrong = [("A flat PNG file", "Buyer can't edit it", 0.8), ("Your Canva login", "Never share this", 2.2)]
        for i, (lab, why, at) in enumerate(wrong):
            kk = p(t, s1 + at, 0.35)
            y = 560 + i * 280
            pill(sub, W / 2, y, lab, F_XB, 56, (255, 236, 238), (170, 30, 50), alpha=out_cubic(kk), scale=out_back(kk), icon="❌")
            draw_text(sub, why, F_SEMI, 44, W / 2, y + 100, SOFT, alpha=out_cubic(p(t, s1 + at + 0.4, 0.3)))
        kk = p(t, s1 + 4.0, 0.45)
        pill(sub, W / 2, 1220, "Send a template link", F_BLACK, 60, GREEN, INK, alpha=out_cubic(kk), scale=out_back(kk), icon="✅")
        draw_text(sub, "Buyer gets their own copy to edit", F_SEMI, 44, W / 2, 1340, WHITE, alpha=out_cubic(p(t, s1 + 4.5, 0.4)))
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Get the link in 3 taps"], t, s2 + 0.1, 280, 78, (WHITE, ACC), gap=0.07, highlight={"3", "taps"})
        share_menu(sub, t, s2 + 0.3, cy=860)
        steps = [("1. Tap Share", 0.9, 2.4), ("2. Choose Template link", 2.5, 3.8), ("3. Copy it", 3.9, 5.4)]
        for lab, a, b in steps:
            kk = p(t, s2 + a, 0.3)
            if kk > 0 and t < s2 + b:
                al = out_cubic(kk) * (1 - p(t, s2 + b - 0.3, 0.3))
                pill(sub, W / 2, 1420, lab, F_XB, 54, GOLD, INK, alpha=al, scale=out_back(kk), icon="👉")
        kk = p(t, s2 + 5.5, 0.4)
        pill(sub, W / 2, 1420, "Look for it under Share", F_XB, 50, WHITE, INK, alpha=out_cubic(kk), scale=out_back(kk), icon="🔍")
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Then paste it in a PDF"], t, s3 + 0.1, 280, 78, (WHITE, GOLD), gap=0.07, highlight={"pdf"})
        pdf_page(sub, t, s3 + 0.4, W / 2, 790)
        steps = [("Upload it as a digital download", 2.6), ("Buyer clicks, edits, done", 3.8)]
        for i, (lab, at) in enumerate(steps):
            kk = p(t, s3 + at, 0.35)
            pill(sub, W / 2, 1265 + i * 120, lab, F_XB, 44, ACC if i == 0 else WHITE, INK, alpha=out_cubic(kk), scale=out_back(kk), icon="📤" if i == 0 else "✨")
        draw_text(sub, "Use your own or free-to-use elements.", F_MED, 36, W / 2, 1500, SOFT, alpha=out_cubic(p(t, s3 + 4.8, 0.5)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel3.mp4")
