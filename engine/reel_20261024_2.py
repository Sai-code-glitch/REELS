"""Stop saying 'I have no experience' -- show sample projects as 3-line case studies instead."""
from reel_portfolio import *

ACC = (255, 150, 70)    # orange
GOLD = (255, 215, 100)
RED = (255, 80, 90)
GREEN = (80, 225, 140)
bg = Background(top=(36, 8, 14), bottom=(22, 6, 18), blobs=[(255, 90, 60), (255, 170, 60), (200, 40, 120)], seed=2972)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, 0.0, 0.3)
        place_emoji(sub, "🛑", W / 2, 470 - 14 * math.sin(t * 6), 200 * out_back(k), alpha=k)
        pop_words(sub, ["Stop saying"], t, 0.0, 720, 110, (WHITE, ACC), gap=0.07)
        pop_words(sub, ["\"I have no", "experience\""], t, 0.25, 940, 104, (GOLD, ACC), gap=0.07)
        strike(sub, t, 1.2, 250, W - 250, 888, RED, width=16)
        strike(sub, t, 1.5, 220, W - 220, 1004, RED, width=16)
        kp = p(t, 1.8, 0.4)
        pill(sub, W / 2, 1190, "Say this instead", F_XB, 50, WHITE, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="👇")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Swap the apology", "for proof"], t, s1 + 0.1, 290, 86, (WHITE, ACC), gap=0.08, highlight={"proof"})
        phone_chat(sub, t, s1 + 0.6, W / 2, 450, [
            ("them", "Have you done this before?", s1 + 1.0, None),
            ("me", "Here are 3 sample projects I made for shops like yours. Happy to do a small first job.", s1 + 2.0, "typed"),
        ], header="Rosa's Bakery", h=700)
        kx = p(t, s1 + 4.8, 0.4)
        pill(sub, W / 2, 1300, "Honest + specific", F_XB, 50, GREEN, INK, alpha=out_cubic(kx), scale=out_back(kx), icon="✅")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Turn each sample into", "a 3-line case study"], t, s2 + 0.1, 290, 72, (WHITE, ACC), gap=0.07, highlight={"3-line", "case", "study"})
        case_card(sub, t, s2 + 0.8, 870, [
            ("The problem", "Homepage said 'Welcome to our website'", s2 + 1.6),
            ("What I did", "Rewrote it: what they fix, where, how to call", s2 + 3.0),
            ("Why it helps", "Visitors know in 3 seconds what to do next", s2 + 4.4),
        ], ACC)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Then do the math"], t, s3 + 0.1, 300, 96, (WHITE, GOLD), gap=0.08, highlight={"math"})
        steps = [("3 case studies", "📁", s3 + 0.7), ("x 10 pitches", "💬", s3 + 1.4), ("= 30 real chances", "🎯", s3 + 2.1)]
        for i, (lab, ic, at) in enumerate(steps):
            kk = p(t, at, 0.4)
            pill(sub, W / 2, 520 + i * 150, lab, F_XB, 58, WHITE if i < 2 else GOLD, INK, alpha=out_cubic(kk), scale=out_back(kk), pad=(44, 24), icon=ic)
        k3 = p(t, s3 + 3.0, 1.8)
        if k3 > 0:
            draw_text(sub, f"${int(round(75 * out_cubic(k3)))}", F_BLACK, 190, W / 2, 1060, GOLD, alpha=out_cubic(p(t, s3 + 3.0, 0.3)))
            draw_text(sub, "a small first job (example)", F_XB, 50, W / 2, 1190, WHITE, alpha=out_cubic(p(t, s3 + 3.2, 0.3)))
        kq = p(t, s3 + 4.4, 0.5)
        draw_text(sub, "Example pricing. Results depend on your work.", F_MED, 36, W / 2, 1300, SOFT, alpha=out_cubic(kq))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel2.mp4")
