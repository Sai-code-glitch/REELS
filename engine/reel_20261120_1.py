"""Websites pay you to find what's confusing (user testing: why it exists, where to sign up, example week)."""
from reel_usertest import *

ACC = (190, 240, 90)    # lime
GOLD = (255, 214, 92)
bg = Background(top=(22, 14, 56), bottom=(48, 30, 110), blobs=[(90, 60, 200), (190, 240, 90), (60, 40, 150)], seed=3241)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Websites pay you", "to find what's", "confusing"], t, -0.3, 400, 108, (WHITE, ACC), gap=0.06, highlight={"pay", "confusing"})
        test_alert(sub, t, 0.7, 860)
        browser_test(sub, t, 1.1, 1010, rec_from=1.1, w=640, h=520, task="Find the return policy")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Why it exists:"], t, s1 + 0.1, 300, 90, (WHITE, ACC), gap=0.07, highlight={"exists:"})
        five_testers(sub, t, s1 + 0.6, 640, ACC, found_at=s1 + 1.6)
        draw_text(sub, "Testing with just 5 people", F_XB, 52, W / 2, 830, WHITE, alpha=out_cubic(p(t, s1 + 2.8, 0.4)))
        draw_text(sub, "finds most usability problems", F_XB, 52, W / 2, 900, WHITE, alpha=out_cubic(p(t, s1 + 3.0, 0.4)))
        draw_text(sub, "(Nielsen Norman Group)", F_SEMI, 36, W / 2, 975, SOFT, alpha=out_cubic(p(t, s1 + 3.4, 0.4)))
        kb = p(t, s1 + 4.4, 0.4)
        pill(sub, W / 2, 1150, "So companies pay real people", F_BLACK, 50, GOLD, INK, alpha=out_cubic(kb), scale=out_back(kb), icon="💡")
        draw_text(sub, "to try their site and talk out loud", F_XB, 44, W / 2, 1270, WHITE, alpha=out_cubic(p(t, s1 + 5.0, 0.4)))
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Start tonight:"], t, s2 + 0.1, 290, 92, (WHITE, ACC), gap=0.07, highlight={"tonight:"})
        checklist(sub, t, s2 + 0.7, ["Sign up on 1 tester site", "Fill your profile honestly", "Turn on test alerts", "Answer screeners fast"], 470, 140, ACC, size=54, x0=130, every=0.9)
        for i, nm in enumerate(["UserTesting", "Userlytics", "TryMyUI"]):
            kk = p(t, s2 + 4.4 + i * 0.25, 0.4)
            pill(sub, [250, 540, 830][i], 1080, nm, F_XB, 38, WHITE, INK, alpha=out_cubic(kk), scale=out_back(kk), pad=(26, 14))
        draw_text(sub, "Examples. Free to join.", F_SEMI, 36, W / 2, 1170, SOFT, alpha=out_cubic(p(t, s2 + 5.2, 0.4)))
        test_alert(sub, t, s2 + 5.8, 1360)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Example math"], t, s3 + 0.1, 270, 90, (WHITE, ACC), gap=0.07, highlight={"math"})
        bar_chart(sub, t, s3 + 0.4, 370, [("Mon", 10), ("Tue", 0), ("Wed", 10), ("Thu", 0), ("Fri", 10)], (110, 90, 230), title="Example week", h=700)
        kq = p(t, s3 + 3.4, 0.4)
        pill(sub, W / 2, 1180, "3 tests × ~$10 = $30", F_BLACK, 56, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="💵")
        draw_text(sub, "Not every test fits you. Rates vary.", F_XB, 42, W / 2, 1300, WHITE, alpha=out_cubic(p(t, s3 + 4.2, 0.4)))
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 34, W / 2, 1390, SOFT, alpha=out_cubic(p(t, s3 + 4.8, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel1.mp4")
