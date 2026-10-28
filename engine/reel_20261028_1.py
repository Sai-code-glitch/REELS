"""Search this on LinkedIn tonight, part 2: find "need holiday help" posts."""
from reel_linkedin import *

ACC = (90, 190, 255)    # LinkedIn-ish sky blue
GOLD = (255, 214, 92)
bg = Background(top=(4, 12, 32), bottom=(6, 28, 66), blobs=[(30, 110, 230), (40, 200, 230), (80, 90, 240)], seed=2811)
Q = '"need holiday help"'


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, -0.2, 0.3)
        place_emoji(sub, "🔎", W / 2, 450 - 16 * math.sin(t * 6), 180 * out_back(k), alpha=k)
        pop_words(sub, ["Search this on", "LinkedIn tonight"], t, -0.3, 760, 104, (WHITE, ACC), gap=0.06, highlight={"linkedin", "tonight"})
        kp = p(t, 0.7, 0.35)
        pill(sub, W / 2, 960, "Part 2: holiday gigs", F_XB, 50, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="🎁")
        li_search(sub, t, 1.2, 1170, Q, type_dur=1.2)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["November gets busy.", "Small teams ask", "their network first"], t, s1 + 0.1, 380, 78, (WHITE, ACC), gap=0.07, highlight={"busy.", "network"})
        rows = [("Shops getting ready for Black Friday", "🛍️", 1.6), ("Coaches planning January launches", "📅", 2.4),
                ("Small agencies short on hands", "🧑‍💻", 3.2)]
        for i, (lab, ic, at) in enumerate(rows):
            kk = p(t, s1 + at, 0.35)
            pill(sub, W / 2, 720 + i * 130, lab, F_SEMI, 42, (225, 240, 255), (10, 60, 130), alpha=out_cubic(kk), scale=out_back(kk), icon=ic)
        kx = p(t, s1 + 4.4, 0.4)
        draw_text(sub, "They post it before a job board", F_XB, 52, W / 2, 1190, GOLD, alpha=out_cubic(kx), scale=0.8 + 0.2 * out_back(kx))
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Filter for this week"], t, s2 + 0.1, 270, 84, (WHITE, ACC), gap=0.07, highlight={"this", "week"})
        li_search(sub, t, s2 + 0.3, 420, Q, type_dur=0.7)
        li_chips(sub, t, s2 + 1.2, 560, ["Posts", "Latest", "Past week"])
        li_post(sub, t, s2 + 2.8, 900, "Maya Chen", "Owner, small candle shop", "5h",
                "Need holiday help! Looking for a freelancer to write our sale emails + 3 posts. Drop your work below",
                (255, 150, 90), comment_at=s2 + 5.0, label="EXAMPLE POST")
        kc = p(t, s2 + 5.4, 0.4)
        pill(sub, W / 2, 1290, "Comment with 1 sample, then DM", F_XB, 44, GOLD, INK, alpha=out_cubic(kc), scale=out_back(kc), icon="💬")
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["3 more searches", "to try"], t, s3 + 0.1, 320, 88, (WHITE, GOLD), gap=0.07, highlight={"3", "searches"})
        qs = ['"looking for a freelancer"', '"anyone recommend a"', '"need help with" holiday']
        for i, q in enumerate(qs):
            kk = p(t, s3 + 0.9 + i * 0.6, 0.35)
            pill(sub, W / 2, 560 + i * 125, q, F_XB, 44, WHITE, INK, alpha=out_cubic(kk), scale=out_back(kk), icon="🔎")
        draw_text(sub, "Example: 3 posts + 1 email", F_XB, 50, W / 2, 1000, WHITE, alpha=out_cubic(p(t, s3 + 3.0, 0.3)))
        k3 = p(t, s3 + 3.2, 1.4)
        if k3 > 0:
            pulse = 1 + 0.05 * math.sin(max(0, t - s3 - 4.6) * 8) * (t > s3 + 4.6)
            draw_text(sub, f"${int(round(150 * out_cubic(k3)))}", F_BLACK, 190, W / 2, 1160, GOLD, alpha=out_cubic(p(t, s3 + 3.2, 0.3)), scale=pulse)
        for i in range(6):
            kk = p(t, s3 + 4.6 + i * 0.1, 1.3)
            if 0 < kk < 1:
                ang = math.pi * (i % 2) + (i // 2 - 1) * 0.3
                place_emoji(sub, "💵", W / 2 + math.cos(ang) * 420 * out_cubic(kk), 1160 + math.sin(ang) * 300 * out_cubic(kk), 80, alpha=1 - kk)
        draw_text(sub, "Example pricing. Results depend on your work.", F_MED, 36, W / 2, 1330, SOFT, alpha=out_cubic(p(t, s3 + 4.2, 0.5)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel1.mp4")
