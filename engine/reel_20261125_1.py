"""Search [Hiring] on Reddit tonight (find small paid jobs in r/forhire: filter Hiring, sort New, 4-point fit check, reply with 1 sample + example math)."""
from reel_reddit import *

ACC = (255, 140, 60)
GOLD = (255, 222, 120)
bg = Background(top=(30, 14, 10), bottom=(110, 40, 20), blobs=[(200, 70, 20), (255, 140, 60), (80, 20, 40)], seed=1251)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Search [Hiring]", "on Reddit tonight"], t, -0.3, 370, 108, (WHITE, ACC), gap=0.07, highlight={"[hiring]", "reddit", "tonight"})
        search_bar(sub, t, 0.4, 640, "r/forhire  [Hiring]", ACC, type_dur=1.0)
        post_row(sub, t, 1.6, 860, "Edit 3 short videos for my shop", "sample · 1h", flag=None)
        post_row(sub, t, 1.9, 1060, "Fix typos on my 5-page site", "sample · 3h")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["People post small", "paid jobs here"], t, s1 + 0.1, 290, 88, (WHITE, ACC), gap=0.07, highlight={"small", "paid", "jobs"})
        rows = [("Write 3 Instagram captions", "$30 · 2h"), ("Canva flyer for a bake sale", "$25 · 4h"),
                ("Proofread a 10-page guide", "$40 · 6h")]
        for i, (tt, mm) in enumerate(rows):
            post_row(sub, t, s1 + 1.0 + i * 0.45, 560 + i * 200, tt, mm)
        draw_text(sub, "(sample posts)", F_SEMI, 34, W / 2, 1180, SOFT, alpha=out_cubic(p(t, s1 + 2.6, 0.4)))
        kb = p(t, s1 + 3.6, 0.4)
        pill(sub, W / 2, 1330, "No bidding app needed", F_BLACK, 50, GOLD, INK, alpha=out_cubic(kb), scale=out_back(kb), icon="🎯")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Filter Hiring.", "Sort by New."], t, s2 + 0.1, 270, 88, (WHITE, ACC), gap=0.07, highlight={"hiring.", "new."})
        community_header(sub, t, s2 + 0.6, 560, ACC, sel_at=s2 + 1.4, sort_at=s2 + 2.0)
        checklist(sub, t, s2 + 2.6, ["Matches your skill", "Says a budget", "Posted today"], 780, 90, ACC, size=48, every=0.5)
        post_row(sub, t, s2 + 4.4, 1130, "Edit 3 Reels · $60 budget", "sample · 1h", flag=("FIT", OKG), flag_at=s2 + 5.2)
        post_row(sub, t, s2 + 4.8, 1320, "Build me an app · no budget", "sample · 9d", flag=("SKIP", RED), flag_at=s2 + 5.6)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Reply fast with", "1 real sample"], t, s3 + 0.1, 270, 88, (WHITE, ACC), gap=0.07, highlight={"fast", "sample"})
        chat_bubble(sub, t, s3 + 0.8, 560, ["Hi! I edit short shop videos.", "Here's 1 I made: [link]", "3 Reels for $60, done Friday?"], me=True, color=(210, 80, 30))
        draw_text(sub, "(sample reply)", F_SEMI, 32, W - 130, 700, SOFT, alpha=out_cubic(p(t, s3 + 1.2, 0.4)), anchor="rm")
        draw_text(sub, "Example: 3 small jobs × $40", F_XB, 50, W / 2, 830, WHITE, alpha=out_cubic(p(t, s3 + 2.0, 0.4)))
        money_counter(sub, t, s3 + 2.4, 120, 1030, GOLD, label="example total")
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 34, W / 2, 1390, SOFT, alpha=out_cubic(p(t, s3 + 4.8, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel1.mp4")
