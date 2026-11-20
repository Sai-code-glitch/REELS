"""Your first website test: 20 minutes, $0 (what you need, think-aloud method, rules for good ratings)."""
from reel_usertest import *

ACC = (90, 230, 160)    # mint
GOLD = (255, 214, 92)
bg = Background(top=(6, 34, 26), bottom=(12, 66, 52), blobs=[(20, 130, 90), (90, 230, 160), (20, 90, 120)], seed=3242)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Your first website", "test: 20 minutes, $0"], t, -0.3, 360, 96, (WHITE, ACC), gap=0.06, highlight={"20", "minutes,", "$0"})
        browser_test(sub, t, 0.4, 600, rec_from=0.4, w=760, h=940, cursor=[(0.6, 0.5, 0.95), (2.6, 0.88, 0.95)], hl_at=2.4)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["All you need:"], t, s1 + 0.1, 300, 90, (WHITE, ACC), gap=0.07, highlight={"need:"})
        checklist(sub, t, s1 + 0.8, ["A laptop or phone", "A working mic", "A quiet room", "20 minutes"], 480, 140, ACC, size=56, x0=170, every=0.8)
        kb = p(t, s1 + 4.2, 0.4)
        pill(sub, W / 2, 1120, "Most sites start with a practice test", F_XB, 44, GOLD, INK, alpha=out_cubic(kb), scale=out_back(kb), icon="🎧")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        browser_test(sub, t, s2 + 0.1, 230, rec_from=s2 + 0.1, h=815,
                     cursor=[(s2 + 0.5, 0.5, 0.35), (s2 + 2.2, 0.9, 0.12), (s2 + 4.0, 0.5, 0.75), (s2 + 5.6, 0.86, 0.95)], hl_at=s2 + 5.6)
        think_bubble(sub, t, s2 + 1.0, 1235, "\"I'd expect returns in the menu\"")
        think_bubble(sub, t, s2 + 3.2, 1360, "\"Nope. I'm a bit lost now\"")
        think_bubble(sub, t, s2 + 5.6, 1485, "\"Found it: tiny grey link\"", color=(255, 241, 196))
        labs = [("1. Read the task out loud", s2 + 0.4), ("2. Say what you expect", s2 + 2.2), ("3. Say what confuses you", s2 + 4.4)]
        for i, (lab, at) in enumerate(labs):
            nxt = labs[i + 1][1] if i + 1 < len(labs) else 99
            if at <= t < nxt:
                kl = p(t, at, 0.3)
                pill(sub, W / 2, 1120, lab, F_BLACK, 46, GOLD, INK, alpha=out_cubic(kl), scale=out_back(kl))
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["4 rules for good ratings"], t, s3 + 0.1, 270, 78, (WHITE, ACC), gap=0.07, highlight={"4", "ratings"})
        checklist(sub, t, s3 + 0.7, ["Talk the whole time", "Be honest, not nice", "Do every task", "End with 1 clear tip"], 440, 140, ACC, size=54, x0=160, every=0.8)
        for i in range(5):
            kk = p(t, s3 + 4.0 + i * 0.15, 0.35)
            place_emoji(sub, "⭐", 300 + i * 120, 1060, 100 * out_back(kk), alpha=out_cubic(kk))
        kq = p(t, s3 + 5.0, 0.4)
        pill(sub, W / 2, 1220, "Good ratings → more tests", F_BLACK, 54, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="📈")
        draw_text(sub, "Results depend on your work.", F_SEMI, 36, W / 2, 1340, SOFT, alpha=out_cubic(p(t, s3 + 5.6, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel2.mp4")
