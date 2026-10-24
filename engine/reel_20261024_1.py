"""No clients yet? Make 3 samples tonight -- pick 3 real local shops, redo 1 thing each, label it SAMPLE."""
from reel_portfolio import *

ACC = (60, 225, 210)    # teal
GOLD = (255, 210, 90)
RED = (255, 90, 100)
bg = Background(top=(6, 18, 36), bottom=(4, 34, 44), blobs=[(30, 170, 200), (60, 90, 255), (40, 220, 170)], seed=2971)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, 0.0, 0.3)
        place_emoji(sub, "📁", W / 2, 470 - 16 * math.sin(t * 5), 210 * out_back(k), alpha=k, rot=6 * math.sin(t * 4))
        pop_words(sub, ["No clients yet?", "Make 3 samples", "tonight"], t, 0.0, 860, 104, (WHITE, ACC), gap=0.07, highlight={"3", "samples", "tonight"})
        kp = p(t, 1.5, 0.4)
        pill(sub, W / 2, 1150, "Your portfolio starts here", F_XB, 48, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="🚀")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Every client asks", "this first"], t, s1 + 0.1, 300, 86, (WHITE, GOLD), gap=0.08, highlight={"first"})
        phone_chat(sub, t, s1 + 0.6, W / 2, 470, [
            ("them", "Hi! Do you have examples of your work?", s1 + 1.1, None),
            ("me", "Not yet... but I'm a fast learner!", s1 + 2.4, "typed"),
        ], header="Dan's Plumbing", h=640)
        kx = p(t, s1 + 4.6, 0.4)
        pill(sub, W / 2, 1270, "No examples = no reply", F_XB, 50, (255, 230, 232), (200, 30, 50), alpha=out_cubic(kx), scale=out_back(kx), icon="❌")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Pick 3 real local shops.", "Redo 1 thing each."], t, s2 + 0.1, 300, 70, (WHITE, ACC), gap=0.07, highlight={"3", "1", "thing"})
        rows = [("🔧", "Dan's Plumbing", "Rewrite the homepage headline", (255, 214, 92)),
                ("🧁", "Rosa's Bakery", "Design 1 Instagram post", (255, 160, 190)),
                ("🕯️", "Maya Candle Co.", "Rewrite 1 product description", (150, 200, 255))]
        for i, (ic, shop, task, col) in enumerate(rows):
            sample_row(sub, t, s2 + 1.0 + i * 0.9, 560 + i * 235, ic, shop, task, col)
        kp = p(t, s2 + 4.4, 0.4)
        pill(sub, W / 2, 1330, "About 1 hour each", F_XB, 50, ACC, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="⏱️")
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["One sample, before + after"], t, s3 + 0.1, 290, 70, (WHITE, GOLD), gap=0.07, highlight={"before", "after"})
        before_after(sub, t, s3 + 0.5, 680, ACC, s3 + 2.0)
        kp = p(t, s3 + 3.6, 0.4)
        pill(sub, W / 2, 1090, "Label it SAMPLE, not a client", F_XB, 46, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="🏷️")
        kq = p(t, s3 + 4.4, 0.4)
        pill(sub, W / 2, 1220, "Don't send it to the shop unasked", F_SEMI, 40, (240, 242, 248), INK, alpha=out_cubic(kq), scale=out_back(kq), icon="🤝")
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel1.mp4")
