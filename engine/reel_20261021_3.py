"""Follow up on day 3, 7 and 14 -- a simple follow-up calendar, then close the loop."""
from reel_chat import *

ACC = (255, 150, 70)    # orange
GOLD = (255, 214, 92)
RED = (255, 96, 110)
BLUE = (92, 170, 255)
bg = Background(top=(40, 16, 8), bottom=(84, 34, 14), blobs=[(255, 120, 40), (255, 70, 90), (255, 190, 60)], seed=2963)

MARKS = {3: ("Day 3", "Quick idea", (52, 199, 120)), 7: ("Day 7", "Useful tip", (66, 133, 244)), 14: ("Day 14", "Close the loop", (255, 120, 60))}


def calendar(sub, t, start):
    k = p(t, start, 0.4)
    if k <= 0: return
    w, h = 880, 650
    card = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(card)
    d.rounded_rectangle([0, 0, w - 1, h - 1], radius=36, fill=(250, 251, 255, 255))
    d.rounded_rectangle([0, 0, w - 1, 100], radius=36, fill=(234, 67, 53, 255))
    d.rectangle([0, 60, w - 1, 100], fill=(234, 67, 53, 255))
    d.text((44, 52), "Follow-up calendar", font=font(F_XB, 40), fill=(255, 255, 255, 255), anchor="lm")
    d.text((w - 44, 52), "Pitch = Day 0", font=font(F_SEMI, 32), fill=(255, 235, 230, 255), anchor="rm")
    for i, dn in enumerate("SMTWTFS"):
        d.text((70 + i * 123, 150), dn, font=font(F_XB, 32), fill=(130, 136, 150, 255), anchor="mm")
    order = [3, 7, 14]
    for n in range(0, 21):
        r, c = divmod(n, 7)
        cx, cy = 70 + c * 123, 240 + r * 150
        if n in MARKS:
            kk = p(t, start + 0.8 + order.index(n) * 1.6, 0.45)
            if kk > 0:
                rad = 54 * out_back(kk)
                d.ellipse([cx - rad, cy - rad, cx + rad, cy + rad], fill=(*MARKS[n][2], 255))
            col = (255, 255, 255, 255) if kk > 0.5 else (*INK, 255)
        else:
            col = (*INK, 255) if n else (150, 156, 170, 255)
        d.text((cx, cy), str(n), font=font(F_XB, 44), fill=col, anchor="mm")
    card = with_alpha(card, out_cubic(k))
    sub.alpha_composite(card, (int(W / 2 - w / 2), int(400 + 60 * (1 - out_cubic(k)))))


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, 0.0, 0.3)
        place_emoji(sub, "📅", W / 2, 470 - 16 * math.sin(t * 6), 180 * out_back(k), alpha=k)
        pop_words(sub, ["Follow up on", "day 3, 7 and 14"], t, 0.0, 800, 100, (WHITE, GOLD), gap=0.08, highlight={"3", "7", "14"})
        kp = p(t, 1.3, 0.4)
        pill(sub, W / 2, 1080, "Then stop", F_BLACK, 60, ACC, INK, alpha=out_cubic(kp), scale=out_back(kp), pad=(50, 24), icon="✋")
        kq = p(t, 1.9, 0.4)
        draw_text(sub, "3 messages. Free. No spam.", F_SEMI, 46, W / 2, 1230, SOFT, alpha=out_cubic(kq))
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["One pitch,", "then silence?"], t, s1 + 0.1, 330, 96, (WHITE, RED), gap=0.08, highlight={"silence?"})
        kp = p(t, s1 + 0.9, 0.4)
        pill(sub, W / 2, 620, "You sent 1 message...", F_XB, 52, (245, 246, 250), INK, alpha=out_cubic(kp), scale=out_back(kp), icon="📤")
        kp2 = p(t, s1 + 1.7, 0.4)
        pill(sub, W / 2, 780, "...and gave up on day 2", F_XB, 52, (245, 246, 250), INK, alpha=out_cubic(kp2), scale=out_back(kp2), icon="🏳️")
        kx = p(t, s1 + 2.6, 0.35)
        place_emoji(sub, "🤷", W / 2, 990, 150 * out_back(kx), alpha=out_cubic(kx))
        kp3 = p(t, s1 + 3.6, 0.4)
        pill(sub, W / 2, 1200, "Give them a plan, not a guilt trip", F_XB, 46, ACC, INK, alpha=out_cubic(kp3), scale=out_back(kp3))
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Put it in your calendar"], t, s2 + 0.1, 300, 82, (WHITE, GOLD), gap=0.08, highlight={"calendar"})
        calendar(sub, t, s2 + 0.3)
        for i, n in enumerate([3, 7, 14]):
            lab, txt, col = MARKS[n]
            kk = p(t, s2 + 1.1 + i * 1.6, 0.4)
            y = 1170 + i * 115
            pill(sub, W / 2, y, f"{lab}: {txt}", F_XB, 46, col, WHITE, alpha=out_cubic(kk), scale=out_back(kk))
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Day 14: close", "the loop"], t, s3 + 0.1, 300, 92, (WHITE, ACC), gap=0.08, highlight={"close", "loop"})
        phone_chat(sub, t, s3 + 0.4, W / 2, 440, [
            ("me", "Hi Jo! Should I close your file for now? No worries either way. Happy to help later.", s3 + 0.7, "typed"),
        ], header="Jo's Studio", h=500)
        kk = p(t, s3 + 3.4, 0.4)
        draw_text(sub, "10 pitches + 3 follow-ups each", F_XB, 52, W / 2, 1040, WHITE, alpha=out_cubic(kk))
        k4 = p(t, s3 + 3.8, 1.3)
        if k4 > 0:
            draw_text(sub, f"{int(round(40 * out_cubic(k4)))}", F_BLACK, 170, W / 2, 1180, GOLD, alpha=out_cubic(p(t, s3 + 3.8, 0.3)))
            draw_text(sub, "chances to be seen, not 10", F_XB, 48, W / 2, 1300, ACC, alpha=out_cubic(p(t, s3 + 4.0, 0.3)))
        draw_text(sub, "Example. Results depend on your work.", F_MED, 34, W / 2, 1400, SOFT, alpha=out_cubic(p(t, s3 + 4.5, 0.5)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel3.mp4")
