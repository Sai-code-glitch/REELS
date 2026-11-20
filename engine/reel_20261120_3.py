"""Stop failing tester screeners (common mistakes, honest answers, open alerts fast)."""
from reel_usertest import *

ACC = (255, 150, 80)    # orange
GOLD = (255, 214, 92)
bg = Background(top=(44, 10, 18), bottom=(90, 24, 34), blobs=[(170, 40, 60), (255, 150, 80), (120, 30, 90)], seed=3243)

Q1 = [("Do you shop online weekly?", ["Yes", "No"], 0, 99)]


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Stop failing", "tester screeners"], t, -0.3, 380, 112, (WHITE, ACC), gap=0.06, highlight={"stop", "failing"})
        screener(sub, t, 0.5, 700, [("Do you own a dog?", ["Yes", "No"], 0, 1.0)], result_at=1.5, result="Not a match", good=False)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Most paid tests start", "with a screener"], t, s1 + 0.1, 320, 76, (WHITE, ACC), gap=0.07, highlight={"screener"})
        draw_text(sub, "Beginners lose tests by:", F_XB, 50, W / 2, 520, SOFT, alpha=out_cubic(p(t, s1 + 1.0, 0.4)))
        checklist(sub, t, s1 + 1.4, ["Saying yes to everything", "Opening alerts hours late", "Leaving the profile empty"], 660, 150, ACC, size=52, x0=120, every=0.9, icon="❌")
        kb = p(t, s1 + 4.6, 0.4)
        pill(sub, W / 2, 1200, "Fix these 3 and you'll fit more tests", F_XB, 44, GOLD, INK, alpha=out_cubic(kb), scale=out_back(kb), icon="🎯")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Answer honestly"], t, s2 + 0.1, 270, 92, (WHITE, ACC), gap=0.07, highlight={"honestly"})
        screener(sub, t, s2 + 0.5, 360, [("Do you shop online weekly?", ["Yes", "No"], 0, s2 + 1.6),
                                         ("Which device?", ["Phone", "Laptop", "Tablet"], 1, s2 + 2.8)],
                 result_at=s2 + 3.8, result="You qualify!", good=True)
        kq = p(t, s2 + 5.0, 0.4)
        pill(sub, W / 2, 1220, "Fake answers can get you removed", F_BLACK, 46, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="⚠️")
        draw_text(sub, "The right tests will fit the real you", F_XB, 42, W / 2, 1340, WHITE, alpha=out_cubic(p(t, s2 + 5.6, 0.4)))
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Tests fill up fast"], t, s3 + 0.1, 270, 90, (WHITE, ACC), gap=0.07, highlight={"fast"})
        test_alert(sub, t, s3 + 0.6, 480)
        notification(sub, t, s3 + 2.0, 700, "Tester app", "Test full", "Opened 3 hours later", (150, 150, 160), icon="⏰")
        test_alert(sub, t, s3 + 3.2, 920, title="You're in! Test started", body="Opened in 2 minutes")
        kq = p(t, s3 + 4.2, 0.4)
        pill(sub, W / 2, 1140, "Alerts on. Open fast.", F_BLACK, 56, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="🔔")
        draw_text(sub, "Often ~$10 per 20-min test. Rates vary.", F_XB, 40, W / 2, 1260, WHITE, alpha=out_cubic(p(t, s3 + 4.8, 0.4)))
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 34, W / 2, 1350, SOFT, alpha=out_cubic(p(t, s3 + 5.2, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel3.mp4")
