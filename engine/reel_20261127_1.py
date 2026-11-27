"""Copy this DM to 1 shop tonight (3-line DM: what I noticed / free sample / yes-no question,
then example reply + example math)."""
from reel_dm import *

ACC = (90, 200, 255)
GOLD = (255, 214, 92)
bg = Background(top=(8, 16, 40), bottom=(20, 50, 110), blobs=[(30, 90, 200), (90, 200, 255), (60, 30, 140)], seed=1271)

MSGS = [("me", "Hi! Love your candles. Your bio link goes to a sale that ended.", 0, None),
        ("me", "I made a fixed version for you, free. Pic below.", 0, None),
        ("me", "Want me to send it over?", 0, "Seen")]


def msgs_at(base, every=1.3, typed=True):
    return [(s, tx, base + i * every, "typed" if (typed and i < 2) else ex) for i, (s, tx, _, ex) in enumerate(MSGS)]


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Copy this DM to", "1 shop tonight"], t, -0.3, 360, 104, (WHITE, ACC), gap=0.06,
                  highlight={"dm", "1", "shop", "tonight"})
        phone_chat(sub, t, 0.4, W / 2, 560, [("me", MSGS[0][1], 0.7, None), ("me", MSGS[1][1], 1.3, None),
                                              ("me", MSGS[2][1], 1.9, None)],
                   header="Pine & Wick", sub_label="Small candle shop · sample", h=740)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Step 1: find 1 thing", "you can fix"], t, s1 + 0.1, 290, 86, (WHITE, ACC), gap=0.07,
                  highlight={"1", "fix"})
        lead_row(sub, t, s1 + 0.8, 520, "🕯️", (255, 214, 170), "@pineandwick", "linktr.ee/… → Summer Sale", False, s1 + 1.6)
        lead_row(sub, t, s1 + 1.2, 710, "☕", (200, 160, 120), "@beanandbell", "Holiday hours: missing", False, s1 + 2.0)
        lead_row(sub, t, s1 + 1.6, 900, "🪴", (170, 220, 170), "@leafandpot", "Bio link works", True, s1 + 2.4)
        kb = p(t, s1 + 3.4, 0.4)
        pill(sub, W / 2, 1110, "Pick ONE real problem", F_BLACK, 50, GOLD, INK, alpha=out_cubic(kb), scale=out_back(kb), icon="🎯")
        draw_text(sub, "Then make the fix as a free sample", F_SEMI, 40, W / 2, 1240, WHITE, alpha=out_cubic(p(t, s1 + 4.2, 0.4)))
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Step 2: send 3 lines"], t, s2 + 0.1, 270, 86, (WHITE, ACC), gap=0.07, highlight={"3", "lines"})
        dm_formula(sub, t, s2 + 0.7, 400, [(1, "What you noticed", "\"Your bio link goes to a sale…\""),
                                         (2, "A free sample", "\"I made a fixed version…\""),
                                         (3, "A yes/no question", "\"Want me to send it over?\"")], ACC, every=1.4)
        draw_text(sub, "No \"I'm a freelancer\" intro.", F_XB, 46, W / 2, 1110, GOLD, alpha=out_cubic(p(t, s2 + 5.0, 0.4)))
        draw_text(sub, "Make it about their shop.", F_XB, 46, W / 2, 1180, WHITE, alpha=out_cubic(p(t, s2 + 5.6, 0.4)))
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["A \"yes\" is easy", "to say to that"], t, s3 + 0.1, 280, 86, (WHITE, ACC), gap=0.07,
                  highlight={"\"yes\"", "easy"})
        notification(sub, t, s3 + 0.7, 520, "pineandwick", "Yes please! What do you charge?", icon="💬")
        draw_text(sub, "(example reply)", F_SEMI, 32, W / 2, 665, SOFT, alpha=out_cubic(p(t, s3 + 1.2, 0.4)))
        draw_text(sub, "Example: $30 fix × 3 shops", F_XB, 50, W / 2, 760, WHITE, alpha=out_cubic(p(t, s3 + 1.8, 0.4)))
        money_counter(sub, t, s3 + 2.2, 90, 960, GOLD, label="example, not a promise")
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 34, W / 2, 1330, SOFT, alpha=out_cubic(p(t, s3 + 4.6, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel1.mp4")
