"""Copy this 3-line reply to hiring posts: match, proof, next step."""
from reel_common import *

ACC = (70, 225, 170)    # mint
GOLD = (255, 214, 92)
RED = (255, 96, 110)
bg = Background(top=(4, 26, 24), bottom=(8, 52, 46), blobs=[(30, 200, 150), (40, 160, 220), (120, 230, 120)], seed=193)

LINES = [
    ("1", "MATCH", "Hi Sam! I edit short videos", "for coaches like you."),
    ("2", "PROOF", "Here's a 20-sec sample:", "link.to/my-sample"),
    ("3", "NEXT STEP", "Want 1 test clip by Friday?", "Happy to DM details."),
]


def numbered(sub, t, start, y, n, label, alpha_scale=1.0):
    k = p(t, start, 0.4)
    if k <= 0: return
    d = ImageDraw.Draw(sub)
    s = out_back(k)
    r = 52 * s
    x = 220
    d.ellipse([x - r, y - r, x + r, y + r], fill=(*ACC, int(255 * out_cubic(k))))
    draw_text(sub, n, F_BLACK, 60, x, y, INK, alpha=out_cubic(k), scale=s)
    draw_text(sub, label, F_BLACK, 70, x + 100, y, WHITE, alpha=out_cubic(k), anchor="lm")


def wall_card(sub, cx, cy, t, start):
    k = p(t, start, 0.4)
    if k <= 0: return
    w, h = 420, 520
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=28, fill=(235, 238, 242, 255))
    for i in range(12):
        ww = [330, 300, 340, 280, 320][i % 5]
        d.rounded_rectangle([30, 34 + i * 38, 30 + ww, 54 + i * 38], radius=10, fill=(180, 186, 196, 255))
    card = with_alpha(card, out_cubic(k))
    sub.alpha_composite(card, (int(cx - w / 2), int(cy - h / 2 + 50 * (1 - out_cubic(k)))))


def short_card(sub, cx, cy, t, start):
    k = p(t, start, 0.4)
    if k <= 0: return
    w, h = 420, 220
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=28, fill=(225, 252, 240, 255))
    for i, ww in enumerate([320, 260, 300]):
        d.rounded_rectangle([30, 40 + i * 56, 30 + ww, 70 + i * 56], radius=12, fill=(*ACC, 255))
    card = with_alpha(card, out_cubic(k))
    sub.alpha_composite(card, (int(cx - w / 2), int(cy - h / 2 + 50 * (1 - out_cubic(k)))))


def reply_builder(sub, t, start):
    w, h = 880, 760
    k = p(t, start, 0.4)
    if k <= 0: return
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=36, fill=(250, 252, 252, 255))
    d.text((44, 56), "Your reply", font=font(F_XB, 38), fill=(20, 130, 95, 255), anchor="lm")
    for i, (n, lab, a, b) in enumerate(LINES):
        kk = p(t, start + 0.6 + i * 1.6, 0.4)
        if kk <= 0: continue
        y = 140 + i * 205
        al = int(255 * out_cubic(kk))
        d.rounded_rectangle([44, y, 44 + 64, y + 64], radius=32, fill=(*ACC, al))
        d.text((76, y + 32), n, font=font(F_BLACK, 38), fill=(*INK, al), anchor="mm")
        d.text((130, y + 32), lab, font=font(F_XB, 32), fill=(20, 130, 95, al), anchor="lm")
        typed = p(t, start + 0.9 + i * 1.6, 0.9)
        full = a + "\n" + b
        nch = int(len(full) * typed)
        s = full[:nch].split("\n")
        d.text((44, y + 100), s[0], font=font(F_SEMI, 42), fill=(*INK, 255), anchor="lm")
        if len(s) > 1:
            col = (20, 110, 200, 255) if i == 1 else (*INK, 255)
            d.text((44, y + 155), s[1], font=font(F_SEMI, 42), fill=col, anchor="lm")
    card = with_alpha(card, out_cubic(k))
    sub.alpha_composite(card, (int(W / 2 - w / 2), int(470 + 60 * (1 - out_cubic(k)))))


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, 0.0, 0.35)
        place_emoji(sub, "📋", W / 2, 440 - 16 * math.sin(t * 6), 170 * out_back(k), alpha=k)
        pop_words(sub, ["Copy this 3-line", "reply to hiring posts"], t, 0.0, 760, 88, (WHITE, ACC), gap=0.08, highlight={"3-line", "hiring"})
        numbered(sub, t, 1.1, 1010, "1", "Match")
        numbered(sub, t, 1.4, 1140, "2", "Proof")
        numbered(sub, t, 1.7, 1270, "3", "Next step")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Long replies", "get skipped"], t, s1 + 0.1, 350, 100, (WHITE, RED), gap=0.08, highlight={"skipped"})
        wall_card(sub, 300, 860, t, s1 + 0.9)
        kx = p(t, s1 + 1.8, 0.35)
        place_emoji(sub, "❌", 300, 860, 200 * out_back(kx), alpha=out_cubic(kx))
        short_card(sub, 780, 760, t, s1 + 2.5)
        kc = p(t, s1 + 3.2, 0.35)
        place_emoji(sub, "✅", 780, 760, 150 * out_back(kc), alpha=out_cubic(kc))
        draw_text(sub, "3 lines", F_XB, 52, 780, 930, ACC, alpha=out_cubic(kc))
        kp = p(t, s1 + 4.2, 0.4)
        pill(sub, W / 2, 1300, "Busy clients skim. Make it easy.", F_SEMI, 44, WHITE, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="⏱️")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Build it", "line by line"], t, s2 + 0.1, 300, 96, (WHITE, ACC), gap=0.08, highlight={"line"})
        reply_builder(sub, t, s2 + 0.4)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Make it a", "nightly habit"], t, s3 + 0.1, 330, 96, (WHITE, GOLD), highlight={"nightly", "habit"})
        days = ["M", "T", "W", "T", "F"]
        for i, dd in enumerate(days):
            kk = p(t, s3 + 0.8 + i * 0.25, 0.35)
            x = 220 + i * 160
            pill(sub, x, 600, dd, F_BLACK, 48, ACC if kk > 0.99 else (230, 245, 240), INK, alpha=out_cubic(kk), scale=out_back(kk), pad=(34, 20))
            draw_text(sub, "5", F_XB, 44, x, 700, WHITE, alpha=out_cubic(kk))
        draw_text(sub, "replies a night", F_SEMI, 40, W / 2, 770, SOFT, alpha=out_cubic(p(t, s3 + 2.0, 0.4)))
        k3 = p(t, s3 + 2.2, 1.2)
        if k3 > 0:
            draw_text(sub, f"{int(round(25 * out_cubic(k3)))}", F_BLACK, 170, W / 2, 920, ACC, alpha=out_cubic(p(t, s3 + 2.2, 0.3)))
            draw_text(sub, "replies a week", F_XB, 50, W / 2, 1040, WHITE, alpha=out_cubic(p(t, s3 + 2.4, 0.3)))
        k4 = p(t, s3 + 3.6, 0.4)
        draw_text(sub, "Example: 1 yes = 1 small project", F_XB, 46, W / 2, 1170, WHITE, alpha=out_cubic(k4))
        k5 = p(t, s3 + 3.9, 1.2)
        if k5 > 0:
            draw_text(sub, f"${int(round(80 * out_cubic(k5)))}", F_BLACK, 140, W / 2, 1290, GOLD, alpha=out_cubic(p(t, s3 + 3.9, 0.3)))
        draw_text(sub, "Example pricing. Results depend on your work.", F_MED, 36, W / 2, 1410, SOFT, alpha=out_cubic(p(t, s3 + 4.3, 0.5)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel3.mp4")
