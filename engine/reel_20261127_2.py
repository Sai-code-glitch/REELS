"""Your first cold DM: 3 lines, $0 (formula noticed + sample + yes/no question, under 40 words,
day 1 send / day 4 one follow-up / then move on, 5 shops a day example)."""
from reel_dm import *

ACC = (120, 230, 160)
GOLD = (255, 222, 120)
bg = Background(top=(6, 26, 22), bottom=(16, 70, 56), blobs=[(20, 120, 90), (120, 230, 160), (20, 70, 110)], seed=1272)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Your first cold DM:", "3 lines, $0"], t, -0.3, 380, 104, (WHITE, ACC), gap=0.06,
                  highlight={"3", "lines,", "$0", "dm:"})
        build_row(sub, t, 0.5, 700, ["Noticed", "Sample", "Question"], [ACC, GOLD, (140, 200, 255)], size=44, gap=0.35)
        place_emoji(sub, "📩", W / 2, 1000 + 16 * math.sin(t * 5), 230 * out_back(p(t, 1.2, 0.5)), alpha=out_cubic(p(t, 1.2, 0.4)))
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Most first DMs", "are about YOU"], t, s1 + 0.1, 290, 86, (WHITE, ACC), gap=0.07,
                  highlight={"you"})
        dm_card(sub, t, s1 + 0.8, 450, "@beanandbell", ["Hi! I'm a freelance designer.", "Do you need any help?"],
                False, s1 + 2.2, "EASY TO IGNORE", emoji="☕", color=(200, 160, 120))
        draw_text(sub, "No idea what you'd do for them", F_XB, 46, W / 2, 900, WHITE, alpha=out_cubic(p(t, s1 + 3.0, 0.4)))
        kb = p(t, s1 + 4.0, 0.4)
        pill(sub, W / 2, 1040, "Make it about their shop", F_BLACK, 50, GOLD, INK, alpha=out_cubic(kb), scale=out_back(kb), icon="🏪")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Write these 3 lines"], t, s2 + 0.1, 270, 86, (WHITE, ACC), gap=0.07, highlight={"3", "lines"})
        dm_formula(sub, t, s2 + 0.6, 400, [(1, "1 thing you noticed", "\"Your holiday hours aren't on Google.\""),
                                         (2, "A free sample fix", "\"I wrote them up for you, free.\""),
                                         (3, "An easy yes/no", "\"Want me to send them?\"")], ACC, every=1.4)
        checklist(sub, t, s2 + 5.0, ["Under 40 words", "No links to click"], 1110, 90, ACC, size=48, every=0.6)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Follow up once.", "Then move on."], t, s3 + 0.1, 280, 86, (WHITE, ACC), gap=0.07,
                  highlight={"once.", "move"})
        day_strip(sub, t, s3 + 0.7, 440, [("Day 1", "📩", "Send DM", True), ("Day 4", "🔁", "1 nudge", True),
                                         ("Day 5+", "➡️", "Next shop", False)], ACC, every=0.5)
        draw_text(sub, "Example: 5 shops a day", F_XB, 50, W / 2, 760, WHITE, alpha=out_cubic(p(t, s3 + 2.0, 0.4)))
        money_counter(sub, t, s3 + 2.4, 25, 950, GOLD, label="shops reached in 5 days", prefix="")
        draw_text(sub, "Example only. Results depend on your work.", F_SEMI, 34, W / 2, 1320, SOFT, alpha=out_cubic(p(t, s3 + 4.6, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel2.mp4")
