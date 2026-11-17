"""Why do people pay $40 to fix one page? (why buyers pay, 3-line post to find them, example quote)."""
from reel_resume import *

ACC = (120, 230, 160)   # mint
GOLD = (255, 214, 92)
bg = Background(top=(4, 30, 26), bottom=(10, 62, 52), blobs=[(20, 110, 80), (120, 230, 160), (30, 70, 130)], seed=3213)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Why do people pay", "$40 to fix", "one page?"], t, -0.3, 380, 100, (WHITE, ACC), gap=0.06, highlight={"$40", "one", "page?"})
        resume_card(sub, t, 0.6, W / 2, 1180, w=480, good=True, rot=4)
        kp = p(t, 1.3, 0.4)
        pill(sub, W / 2 + 230, 960, "$40", F_BLACK, 64, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="🏷️")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Because most people…"], t, s1 + 0.1, 290, 84, (WHITE, ACC), gap=0.07, highlight={"people…"})
        checklist(sub, t, s1 + 0.8, ["Hate writing about themselves", "Don't know what to cut", "Want it done before January"], 480, 150, ACC, size=48, x0=120, every=0.9)
        kb = p(t, s1 + 4.0, 0.4)
        pill(sub, W / 2, 1050, "You sell time + confidence", F_XB, 50, GOLD, INK, alpha=out_cubic(kb), scale=out_back(kb), icon="⏱️")
        draw_text(sub, "New year = new job goals", F_SEMI, 42, W / 2, 1175, SOFT, alpha=out_cubic(p(t, s1 + 4.8, 0.4)))
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Post this on LinkedIn"], t, s2 + 0.1, 270, 84, (WHITE, ACC), gap=0.07, highlight={"linkedin"})
        li_composer(sub, t, s2 + 0.4, 400, ["Taking 3 resume fixes before January.", "1 page, 2-day turnaround.", "DM me 'resume' for a slot."],
                    ACC, every=1.3, type_each=1.1, post_at=s2 + 4.8)
        notification(sub, t, s2 + 5.6, 1260, "LinkedIn", "New message", "\"resume\"", LI_BLUE, icon="💬")
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Example pricing"], t, s3 + 0.1, 270, 84, (WHITE, ACC), gap=0.07, highlight={"pricing"})
        rows = [("1-page resume rewrite", "$40", s3 + 0.9), ("LinkedIn headline + About", "$20", s3 + 1.5), ("Cover letter template", "$15", s3 + 2.1)]
        quote_card(sub, t, s3 + 0.4, 380, "Resume refresh", rows, "$75", None, ACC)
        kq = p(t, s3 + 3.4, 0.4)
        pill(sub, W / 2, 1110, "3 clients × $75 = $225", F_BLACK, 54, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="💵")
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 34, W / 2, 1240, SOFT, alpha=out_cubic(p(t, s3 + 4.2, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel3.mp4")
