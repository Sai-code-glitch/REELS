"""Stop starting DMs with "I'm a freelancer" (about-you vs about-them DM, 3 rules:
start with their shop / show a free sample / ask yes-no, respect a no, example math)."""
from reel_dm import *

ACC = (255, 120, 170)
GOLD = (255, 214, 110)
bg = Background(top=(30, 8, 30), bottom=(90, 20, 70), blobs=[(170, 30, 110), (255, 120, 170), (80, 30, 140)], seed=1273)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Stop starting DMs", "with \"I'm a", "freelancer\""], t, -0.3, 420, 104, (WHITE, ACC), gap=0.06,
                  highlight={"stop", "\"i'm", "freelancer\""})
        stamp(sub, t, 1.3, W / 2, 820, "EASY TO IGNORE", BADRED, size=80, rot=-8)
        place_emoji(sub, "🙈", W / 2, 1080 + 14 * math.sin(t * 6), 200 * out_back(p(t, 1.8, 0.5)), alpha=out_cubic(p(t, 1.8, 0.4)))
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["This DM is", "about you"], t, s1 + 0.1, 290, 86, (WHITE, ACC), gap=0.07, highlight={"you"})
        dm_card(sub, t, s1 + 0.7, 450, "@leafandpot", ["Hi! I'm a freelancer with", "5 years of experience.", "Let me know if you need help!"],
                False, s1 + 2.0, "ABOUT YOU", emoji="🪴", color=(170, 220, 170))
        draw_text(sub, "The shop has to figure out", F_XB, 46, W / 2, 960, WHITE, alpha=out_cubic(p(t, s1 + 3.0, 0.4)))
        draw_text(sub, "what you'd even do", F_XB, 46, W / 2, 1025, WHITE, alpha=out_cubic(p(t, s1 + 3.2, 0.4)))
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["This one is", "about them"], t, s2 + 0.1, 290, 86, (WHITE, ACC), gap=0.07, highlight={"them"})
        dm_card(sub, t, s2 + 0.7, 450, "@leafandpot", ["Your newest post has no price,", "so people keep asking.",
                                                       "I made a price-tag version, free.", "Want it?"],
                True, s2 + 2.4, "ABOUT THEM", emoji="🪴", color=(170, 220, 170))
        checklist(sub, t, s2 + 3.6, ["Their shop first", "Show a free sample", "End with yes/no"], 1000, 92, ACC, size=50, every=0.6)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Got a \"no thanks\"?", "Say thanks. Next shop."], t, s3 + 0.1, 290, 80, (WHITE, ACC), gap=0.07,
                  highlight={"\"no", "thanks\"?", "next"})
        draw_text(sub, "Example: 1 yes = $40 post pack", F_XB, 50, W / 2, 560, WHITE, alpha=out_cubic(p(t, s3 + 1.0, 0.4)))
        money_counter(sub, t, s3 + 1.4, 40, 760, GOLD, label="example, 1 shop")
        kb = p(t, s3 + 3.8, 0.4)
        pill(sub, W / 2, 1130, "Never pay to get a client", F_BLACK, 46, GOLD, INK, alpha=out_cubic(kb), scale=out_back(kb), icon="🛑")
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 34, W / 2, 1270, SOFT, alpha=out_cubic(p(t, s3 + 4.6, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel3.mp4")
