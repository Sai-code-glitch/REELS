"""Stop starting work before the deposit -- 50/50 split + the exact line to send."""
from reel_quote import *

ACC = (255, 150, 90)    # coral
GOLD = (255, 220, 110)
bg = Background(top=(40, 12, 20), bottom=(60, 20, 30), blobs=[(255, 90, 90), (255, 160, 80), (200, 60, 140)], seed=2992)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, 0.0, 0.3)
        place_emoji(sub, "🛑", W / 2, 470 - 16 * math.sin(t * 5), 210 * out_back(k), alpha=k, rot=6 * math.sin(t * 4))
        pop_words(sub, ["Stop starting", "work before", "the deposit"], t, 0.0, 860, 112, (WHITE, ACC), gap=0.07, highlight={"stop", "deposit"})
        kp = p(t, 1.5, 0.4)
        pill(sub, W / 2, 1160, "Beginners skip this", F_XB, 50, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="👀")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["You finish the work.", "Then..."], t, s1 + 0.1, 300, 80, (WHITE, GOLD), gap=0.08, highlight={"then..."})
        chat_bubble(sub, t, s1 + 1.0, 540, ["Here's your finished logo!"], me=True, color=(70, 140, 255))
        chat_bubble(sub, t, s1 + 2.0, 690, ["Seen 3 days ago"], me=False, w=480)
        chat_bubble(sub, t, s1 + 2.8, 830, ["Hi, just following up on", "the payment..."], me=True, color=(70, 140, 255))
        kx = p(t, s1 + 3.9, 0.4)
        pill(sub, W / 2, 1040, "No reply. No payment.", F_XB, 50, (255, 230, 232), (200, 30, 50), alpha=out_cubic(kx), scale=out_back(kx), icon="👻")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Split every project", "50 / 50"], t, s2 + 0.1, 290, 84, (WHITE, ACC), gap=0.07, highlight={"50", "/"})
        split_bar(sub, t, s2 + 1.0, 560, ("50%", "before you start"), ("50%", "before final files"), ACC, GOLD)
        checklist(sub, t, s2 + 2.4, ["Deposit paid = you start", "Final half = they get files", "No deposit = no start date"], 820, 120, ACC, size=48, x0=140)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Send this line:"], t, s3 + 0.1, 270, 80, (WHITE, GOLD), gap=0.07, highlight={"this", "line:"})
        chat_bubble(sub, t, s3 + 0.6, 470, ["I start as soon as the 50%", "deposit is in. Final files", "go out with the last 50%."], me=True, color=(70, 140, 255), w=820)
        kl = p(t, s3 + 1.8, 0.4)
        draw_text(sub, "Example: $200 project", F_XB, 46, W / 2, 680, WHITE, alpha=out_cubic(kl))
        money_counter(sub, t, s3 + 2.1, 100, 860, GOLD, label="paid before you start")
        kr = p(t, s3 + 4.6, 0.4)
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 36, W / 2, 1270, SOFT, alpha=out_cubic(kr))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel2.mp4")
