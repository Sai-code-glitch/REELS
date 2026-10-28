"""Fix your LinkedIn headline in 2 minutes: 'I help [who] [result] with [service]'."""
from reel_linkedin import *

ACC = (255, 120, 190)   # pink
GOLD = (255, 214, 92)
RED = (255, 96, 110)
bg = Background(top=(26, 8, 40), bottom=(60, 16, 70), blobs=[(200, 60, 180), (120, 60, 240), (255, 110, 150)], seed=2812)
OLD = "Student | Open to opportunities"
NEW = "I help small shops sell more with holiday emails"


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, -0.2, 0.3)
        place_emoji(sub, "⏱️", W / 2, 470 - 16 * math.sin(t * 6), 180 * out_back(k), alpha=k, rot=8 * math.sin(t * 5))
        pop_words(sub, ["Fix your", "LinkedIn headline", "in 2 minutes"], t, -0.3, 840, 100, (WHITE, ACC), gap=0.06, highlight={"headline", "2", "minutes"})
        kp = p(t, 1.3, 0.4)
        pill(sub, W / 2, 1170, "It shows under every comment", F_XB, 46, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="👀")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["This headline", "says nothing"], t, s1 + 0.1, 300, 92, (WHITE, RED), gap=0.07, highlight={"nothing"})
        li_profile(sub, t, s1 + 0.6, 450, "Sam Rivera", OLD, NEW, swap_at=99, acc=(120, 70, 200))
        kx = p(t, s1 + 2.4, 0.35)
        place_emoji(sub, "❌", W / 2 + 330, 900, 120 * out_back(kx), alpha=out_cubic(kx))
        qs = [("Who do you help?", 3.0), ("With what?", 3.7)]
        for i, (q, at) in enumerate(qs):
            kk = p(t, s1 + at, 0.35)
            pill(sub, W / 2, 1210 + i * 120, q, F_XB, 46, WHITE, INK, alpha=out_cubic(kk), scale=out_back(kk), icon="🤔")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Use this formula"], t, s2 + 0.1, 270, 88, (WHITE, ACC), gap=0.07, highlight={"formula"})
        build_row(sub, t, s2 + 0.6, 400, ["I help WHO", "get RESULT"], [ACC, GOLD], size=46, gap=0.5)
        build_row(sub, t, s2 + 1.5, 510, ["with SERVICE"], [(140, 220, 255)], size=46)
        li_profile(sub, t, s2 + 2.0, 640, "Sam Rivera", OLD, NEW, swap_at=s2 + 3.0, acc=(120, 70, 200), type_dur=1.8)
        ks = p(t, s2 + 6.2, 0.35)
        place_emoji(sub, "✅", W / 2 + 340, 1090, 110 * out_back(ks), alpha=out_cubic(ks))
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Every comment", "becomes a mini ad"], t, s3 + 0.1, 320, 88, (WHITE, GOLD), gap=0.07, highlight={"mini", "ad"})
        li_comment(sub, t, s3 + 0.7, 650, "Sam Rivera", NEW,
                   "Happy to help with your holiday emails! Here's a sample I wrote.", GOLD, glow_at=s3 + 1.8)
        kk = p(t, s3 + 2.2, 0.4)
        place_emoji(sub, "👆", W / 2 - 230, 870 + 14 * math.sin(t * 8), 100, alpha=out_cubic(kk))
        checklist(sub, t, s3 + 2.8, ["Who you help", "The result", "Your service"], 1010, 105, ACC, size=50, x0=260, every=0.5)
        draw_text(sub, "Free to change. No paid tools needed.", F_SEMI, 40, W / 2, 1370, SOFT, alpha=out_cubic(p(t, s3 + 4.6, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel2.mp4")
