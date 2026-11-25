"""Never pay to get a Reddit job (spot fake [Hiring] posts: 4 red flags, 3 green flags, safe way to get paid with a deposit)."""
from reel_reddit import *

ACC = (90, 210, 255)
GOLD = (255, 214, 102)
bg = Background(top=(6, 18, 40), bottom=(14, 50, 90), blobs=[(20, 80, 150), (90, 210, 255), (60, 20, 60)], seed=1253)

SCAM = (["Easy data entry, $50/hour!"], ["No experience needed.", "First pay a $50 training fee.", "Text me on another app."])


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Never pay to get", "a Reddit job"], t, -0.3, 360, 108, (WHITE, ACC), gap=0.07, highlight={"never", "pay"})
        post_card(sub, t, 0.4, 610, SCAM[0], SCAM[1], user="u/quickcash_jobs", age="5m ago", hi=1, hi_at=1.5,
                  stamp=("SCAM", RED), stamp_at=2.4)
        draw_text(sub, "(sample fake post)", F_SEMI, 32, W / 2, 1180, SOFT, alpha=out_cubic(p(t, 1.0, 0.4)))
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Fake job posts", "look real at first"], t, s1 + 0.1, 290, 88, (WHITE, ACC), gap=0.07, highlight={"fake", "real"})
        post_row(sub, t, s1 + 1.0, 560, "Edit 3 Reels · $60 budget", "sample · 1h", flag=("REAL", OKG), flag_at=s1 + 3.0)
        post_row(sub, t, s1 + 1.4, 760, "Easy typing job · $50/hour", "sample · 5m", flag=("FAKE", RED), flag_at=s1 + 3.5)
        post_row(sub, t, s1 + 1.8, 960, "Proofread a 10-page guide", "sample · 6h", flag=("REAL", OKG), flag_at=s1 + 4.0)
        kb = p(t, s1 + 4.8, 0.4)
        pill(sub, W / 2, 1200, "Check before you reply", F_BLACK, 50, GOLD, INK, alpha=out_cubic(kb), scale=out_back(kb), icon="🔎")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["4 red flags"], t, s2 + 0.1, 250, 92, (WHITE, (255, 120, 110)), gap=0.07, highlight={"red", "flags"})
        checklist(sub, t, s2 + 0.7, ["You pay a fee first", "They mail you a check", "Vague task, huge pay", "Rushes you to another app"], 420, 100, ACC, size=48, every=0.6, icon="🚩")
        draw_text(sub, "Green flags", F_BLACK, 70, W / 2, 900, (120, 230, 150), alpha=out_cubic(p(t, s2 + 3.5, 0.4)))
        checklist(sub, t, s2 + 3.9, ["Clear task you can do", "Budget in the post", "Money only comes TO you"], 1010, 100, ACC, size=48, every=0.6)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Safe way:", "ask for half first"], t, s3 + 0.1, 260, 88, (WHITE, ACC), gap=0.07, highlight={"safe", "half"})
        offer_card(sub, t, s3 + 0.8, 750, [("3 edited Reels", "$60", s3 + 1.3), ("Deposit before you start", "$30", s3 + 1.9),
                                           ("Rest when you deliver", "$30", s3 + 2.5)], "$60", ACC, title="Quote", h=660)
        split_bar(sub, t, s3 + 3.8, 1220, ("$30", "Deposit"), ("$30", "On delivery"), ACC, GOLD)
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 34, W / 2, 1430, SOFT, alpha=out_cubic(p(t, s3 + 4.6, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel3.mp4")
