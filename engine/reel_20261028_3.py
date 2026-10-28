"""Post this on LinkedIn tonight: a 4-line 'taking holiday projects' post."""
from reel_linkedin import *

ACC = (80, 230, 170)    # mint
GOLD = (255, 200, 80)
bg = Background(top=(4, 26, 26), bottom=(8, 48, 44), blobs=[(30, 190, 140), (40, 150, 200), (120, 220, 120)], seed=2813)
POST = ["I'm taking 3 holiday projects this November.",
        "I write sale emails + posts for small shops.",
        "Here's a sample: [your link]",
        "Know a shop that needs help? Tag them below."]


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, -0.2, 0.3)
        place_emoji(sub, "✍️", W / 2, 470 - 16 * math.sin(t * 6), 180 * out_back(k), alpha=k, rot=6 * math.sin(t * 4))
        pop_words(sub, ["Post this on", "LinkedIn tonight"], t, -0.3, 790, 104, (WHITE, ACC), gap=0.06, highlight={"linkedin", "tonight"})
        kp = p(t, 1.0, 0.4)
        pill(sub, W / 2, 1020, "4 lines. Copy it.", F_XB, 54, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="📋")
        kq = p(t, 1.8, 0.4)
        pill(sub, W / 2, 1160, "Your network can't refer a secret", F_SEMI, 42, WHITE, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="🤫")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Most people never", "say they freelance"], t, s1 + 0.1, 330, 84, (WHITE, ACC), gap=0.07, highlight={"never", "freelance"})
        ppl = ["👩", "🧔", "👨‍🦱", "👩‍🦰", "🧑"]
        for i, e in enumerate(ppl):
            kk = p(t, s1 + 0.9 + i * 0.2, 0.4)
            x = 190 + i * 175
            place_emoji(sub, e, x, 700 + 10 * math.sin(t * 4 + i), 130 * out_back(kk), alpha=out_cubic(kk))
            kq = p(t, s1 + 2.2 + i * 0.15, 0.3)
            place_emoji(sub, "❓", x, 570, 64 * out_back(kq), alpha=out_cubic(kq))
        tags = [("Friends, ex-coworkers, classmates", 3.2, "👥"), ("They know shop owners", 3.9, "🏪"), ("But don't know you can help", 4.6, "🙈")]
        for i, (lab, at, ic) in enumerate(tags):
            kk = p(t, s1 + at, 0.35)
            pill(sub, W / 2, 920 + i * 125, lab, F_SEMI, 42, (220, 250, 238), (10, 80, 60), alpha=out_cubic(kk), scale=out_back(kk), icon=ic)
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Copy these 4 lines"], t, s2 + 0.1, 270, 84, (WHITE, ACC), gap=0.07, highlight={"4", "lines"})
        li_composer(sub, t, s2 + 0.3, 370, POST, ACC, every=1.3, type_each=1.0, post_at=s2 + 6.0)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Have the offer", "ready to send"], t, s3 + 0.1, 300, 88, (WHITE, GOLD), gap=0.07, highlight={"offer", "ready"})
        offer_card(sub, t, s3 + 0.5, 760, [
            ("3 holiday sale posts", "$60", s3 + 1.1),
            ("1 Black Friday email", "$40", s3 + 1.7),
            ("1 round of edits", "incl.", s3 + 2.3),
        ], "$100", ACC, title="Holiday post pack", h=620)
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 36, W / 2, 1140, SOFT, alpha=out_cubic(p(t, s3 + 3.6, 0.4)))
        kq = p(t, s3 + 4.3, 0.4)
        pill(sub, W / 2, 1270, "Reply to every comment same day", F_XB, 42, WHITE, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="⚡")
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel3.mp4")
