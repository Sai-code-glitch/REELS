"""Stop giving unlimited revisions -- add one line to your contract."""
from reel_common import *

ACC = (255, 150, 70)    # orange
GOLD = (255, 220, 100)
RED = (255, 90, 100)
GREEN = (80, 220, 140)
bg = Background(top=(36, 10, 16), bottom=(78, 26, 24), blobs=[(255, 110, 60), (230, 60, 110), (255, 190, 70)], seed=2932)


def revision_stack(sub, t, start):
    """Revision files piling up: v1 ... v9 with a growing counter."""
    n = 9
    for i in range(n):
        kk = p(t, start + i * 0.32, 0.3)
        if kk <= 0: continue
        x = 200 + (i % 3) * 340
        y = 600 + (i // 3) * 190
        col = (245, 246, 250) if i < 2 else (255, 225, 225)
        pill(sub, x, y, f"logo_v{i + 1}", F_XB, 46, col, INK if i < 2 else (170, 30, 40), alpha=out_cubic(kk), scale=out_back(kk), pad=(30, 24), icon="🖼️")
    k = p(t, start, n * 0.32)
    if k > 0:
        hours = int(round(14 * out_cubic(k)))
        draw_text(sub, f"{hours} hours", F_BLACK, 130, W / 2, 1270, RED, alpha=out_cubic(p(t, start, 0.3)))
        draw_text(sub, "on a job you quoted for 4", F_XB, 50, W / 2, 1380, WHITE, alpha=out_cubic(p(t, start + 0.3, 0.3)))


def contract_line(sub, t, start):
    w, h = 880, 560
    k = p(t, start, 0.4)
    if k <= 0: return
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=36, fill=(252, 250, 248, 255))
    d.text((44, 60), "Revisions", font=font(F_BLACK, 50), fill=(200, 90, 30, 255), anchor="lm")
    full1 = "2 rounds of revisions included."
    full2 = "Extra rounds: $25 each."
    full3 = "New ideas = new quote."
    for i, s in enumerate([full1, full2, full3]):
        ty = p(t, start + 0.6 + i * 1.3, 1.0)
        y = 170 + i * 120
        if ty <= 0:
            d.rounded_rectangle([44, y - 14, 44 + 600, y + 14], radius=12, fill=(232, 228, 224, 255))
            continue
        d.text((44, y), s[:int(len(s) * ty)], font=font(F_SEMI, 46), fill=(*INK, 255), anchor="lm")
        if ty >= 1 and i == 1:
            d.rounded_rectangle([40, y + 34, 40 + int(d.textlength(s, font=font(F_SEMI, 46))) + 8, y + 42], radius=4, fill=(*ACC, 255))
    kp = p(t, start + 5.0, 0.4)
    if kp > 0:
        d.text((44, 500), "Send it BEFORE you start the work.", font=font(F_XB, 36), fill=(30, 140, 80, int(255 * out_cubic(kp))), anchor="lm")
    card = with_alpha(card, out_cubic(k))
    sub.alpha_composite(card, (int(W / 2 - w / 2), int(560 + 60 * (1 - out_cubic(k)))))


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, 0.0, 0.3)
        place_emoji(sub, "🔁", W / 2, 470 - 16 * math.sin(t * 6), 180 * out_back(k), alpha=k)
        pop_words(sub, ["Stop giving", "unlimited revisions"], t, 0.0, 800, 96, (WHITE, ACC), gap=0.08, highlight={"unlimited", "revisions"})
        kp = p(t, 1.4, 0.4)
        pill(sub, W / 2, 1080, "Add 1 line to your contract", F_BLACK, 54, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), pad=(44, 24), icon="✍️")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["\"Just one more", "small change...\""], t, s1 + 0.1, 340, 92, (WHITE, RED), gap=0.08, highlight={"more", "small"})
        revision_stack(sub, t, s1 + 1.0)
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Write this into", "every agreement"], t, s2 + 0.1, 340, 92, (WHITE, ACC), gap=0.08, highlight={"every"})
        contract_line(sub, t, s2 + 0.4)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Client asks for", "round 3?"], t, s3 + 0.1, 330, 92, (WHITE, GOLD), gap=0.08, highlight={"3?"})
        kb = p(t, s3 + 0.9, 0.4)
        pill(sub, W / 2, 590, "Happy to! Round 3 is $25.", F_XB, 50, (245, 246, 250), INK, alpha=out_cubic(kb), scale=out_back(kb), pad=(44, 28), icon="💬")
        kb2 = p(t, s3 + 1.6, 0.4)
        pill(sub, W / 2, 730, "Want me to go ahead?", F_XB, 50, (245, 246, 250), INK, alpha=out_cubic(kb2), scale=out_back(kb2), pad=(44, 28))
        k3 = p(t, s3 + 2.4, 0.4)
        draw_text(sub, "Example: 4 extra rounds a month", F_XB, 48, W / 2, 900, WHITE, alpha=out_cubic(k3))
        k4 = p(t, s3 + 2.7, 1.3)
        if k4 > 0:
            draw_text(sub, f"+${int(round(100 * out_cubic(k4)))}", F_BLACK, 180, W / 2, 1050, GREEN, alpha=out_cubic(p(t, s3 + 2.7, 0.3)))
            draw_text(sub, "instead of free overtime", F_XB, 50, W / 2, 1180, ACC, alpha=out_cubic(p(t, s3 + 2.9, 0.3)))
        draw_text(sub, "Example pricing. Results depend on your work.", F_MED, 34, W / 2, 1300, SOFT, alpha=out_cubic(p(t, s3 + 3.6, 0.5)))
        for i in range(6):
            kk = p(t, s3 + 4.0 + i * 0.12, 1.4)
            if 0 < kk < 1:
                place_emoji(sub, "💵", 160 + i * 150, 1570 - 160 * out_cubic(kk), 80, alpha=1 - kk, rot=(i - 3) * 10 * kk)
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel2.mp4")
