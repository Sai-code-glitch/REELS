"""Your first contract: 10 minutes, $0 -- the 5 lines every simple freelance contract needs."""
from reel_common import *

ACC = (92, 170, 255)    # sky blue
GOLD = (255, 214, 92)
RED = (255, 96, 110)
bg = Background(top=(8, 14, 40), bottom=(16, 34, 84), blobs=[(60, 120, 255), (120, 80, 230), (40, 200, 230)], seed=2931)

CLAUSES = [
    ("1. Scope", "1 logo + 3 social graphics"),
    ("2. Price", "$300, 50% upfront"),
    ("3. Deadline", "Delivered by Nov 3"),
    ("4. Revisions", "2 rounds included"),
    ("5. Payment", "Balance due on delivery"),
]


def doc_card(sub, t, start):
    """Mock Google-Docs style contract that fills in line by line."""
    k = p(t, start, 0.4)
    if k <= 0: return
    w, h = 880, 1080
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=36, fill=(250, 251, 255, 255))
    d.rounded_rectangle([0, 0, w - 1, 96], radius=36, fill=(66, 133, 244, 255))
    d.rectangle([0, 60, w - 1, 96], fill=(66, 133, 244, 255))
    d.text((44, 50), "Simple Freelance Agreement", font=font(F_XB, 38), fill=(255, 255, 255, 255), anchor="lm")
    d.text((44, 150), "Client: Maya's Bakery   |   You: Alex", font=font(F_MED, 32), fill=(110, 116, 130, 255), anchor="lm")
    for i, (lab, val) in enumerate(CLAUSES):
        kk = p(t, start + 0.6 + i * 1.15, 0.4)
        y = 240 + i * 150
        if kk <= 0:
            d.rounded_rectangle([44, y, 44 + 520, y + 26], radius=12, fill=(228, 231, 238, 255))
            continue
        al = int(255 * out_cubic(kk))
        d.text((44, y + 10), lab, font=font(F_BLACK, 44), fill=(30, 90, 200, al), anchor="lm")
        typed = p(t, start + 0.8 + i * 1.15, 0.7)
        s = val[:int(len(val) * typed)]
        d.text((44, y + 70), s, font=font(F_SEMI, 42), fill=(*INK, 255), anchor="lm")
        if typed >= 1:
            d.ellipse([w - 110, y - 12, w - 50, y + 48], fill=(52, 199, 120, 255))
            d.text((w - 80, y + 18), "✓", font=font(DEJAVU, 40), fill=(255, 255, 255, 255), anchor="mm")
    kd = p(t, start + 6.6, 0.4)
    if kd > 0:
        al = int(255 * out_cubic(kd))
        d.line([44, h - 40, 420, h - 40], fill=(150, 156, 170, al), width=3)
        d.text((44, h - 75), "Signed: Maya", font=font(F_SEMI, 34), fill=(*INK, al), anchor="lm")
    card = with_alpha(card, out_cubic(k))
    sub.alpha_composite(card, (int(W / 2 - w / 2), int(430 + 60 * (1 - out_cubic(k)))))


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, 0.0, 0.3)
        place_emoji(sub, "📝", W / 2, 470 - 16 * math.sin(t * 6), 180 * out_back(k), alpha=k)
        pop_words(sub, ["Your first contract:", "10 minutes, $0"], t, 0.0, 800, 96, (WHITE, ACC), gap=0.08, highlight={"10", "minutes,", "$0"})
        kp = p(t, 1.3, 0.4)
        pill(sub, W / 2, 1080, "Just 5 lines", F_BLACK, 60, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), pad=(50, 24), icon="✋")
        kq = p(t, 1.9, 0.4)
        draw_text(sub, "Free Google Doc. No lawyer fees.", F_SEMI, 46, W / 2, 1230, SOFT, alpha=out_cubic(kq))
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["No contract =", "messy projects"], t, s1 + 0.1, 330, 96, (WHITE, RED), gap=0.08, highlight={"messy"})
        bubbles = [("\"Can you add one more?\"", 600), ("\"I'll pay next month\"", 780), ("\"I thought it included...\"", 960)]
        for i, (txt, y) in enumerate(bubbles):
            kk = p(t, s1 + 0.9 + i * 0.7, 0.4)
            x = W / 2 + (-60 if i % 2 == 0 else 60)
            pill(sub, x, y, txt, F_SEMI, 46, (245, 246, 250), INK, alpha=out_cubic(kk), scale=out_back(kk), pad=(40, 26), icon="💬")
        kx = p(t, s1 + 3.3, 0.35)
        place_emoji(sub, "😩", W / 2, 1160, 150 * out_back(kx), alpha=out_cubic(kx))
        kp = p(t, s1 + 4.2, 0.4)
        pill(sub, W / 2, 1360, "Put it in writing before you start", F_XB, 44, ACC, INK, alpha=out_cubic(kp), scale=out_back(kp))
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Write these 5 lines"], t, s2 + 0.1, 300, 92, (WHITE, ACC), gap=0.08, highlight={"5", "lines"})
        doc_card(sub, t, s2 + 0.3)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Then get a", "\"yes\" in writing"], t, s3 + 0.1, 330, 92, (WHITE, GOLD), gap=0.08, highlight={"\"yes\""})
        opts = [("✍️", "Free e-sign tool"), ("✉️", "Email reply: \"Agreed\""), ("💬", "Signed PDF in chat")]
        for i, (ic, lab) in enumerate(opts):
            kk = p(t, s3 + 0.9 + i * 0.5, 0.4)
            pill(sub, W / 2, 600 + i * 150, lab, F_XB, 52, (245, 246, 250), INK, alpha=out_cubic(kk), scale=out_back(kk), pad=(46, 26), icon=ic)
        k3 = p(t, s3 + 2.8, 0.4)
        draw_text(sub, "Example: $300 job, 50% upfront", F_XB, 48, W / 2, 1060, WHITE, alpha=out_cubic(k3))
        k4 = p(t, s3 + 3.1, 1.3)
        if k4 > 0:
            draw_text(sub, f"${int(round(150 * out_cubic(k4)))}", F_BLACK, 170, W / 2, 1200, GOLD, alpha=out_cubic(p(t, s3 + 3.1, 0.3)))
            draw_text(sub, "paid before you start", F_XB, 48, W / 2, 1320, ACC, alpha=out_cubic(p(t, s3 + 3.3, 0.3)))
        draw_text(sub, "Example pricing. Results depend on your work.", F_MED, 34, W / 2, 1420, SOFT, alpha=out_cubic(p(t, s3 + 3.8, 0.5)))
        draw_text(sub, "Not legal advice. Bigger jobs: ask a pro.", F_MED, 34, W / 2, 1475, SOFT, alpha=out_cubic(p(t, s3 + 4.0, 0.5)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel1.mp4")
