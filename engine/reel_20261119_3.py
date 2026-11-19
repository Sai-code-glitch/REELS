"""Why do shops pay for 15 seconds of video? (saves time, 4 clips -> 1 Reel, example pricing)."""
from reel_edit import *

ACC = (255, 190, 70)    # amber
GOLD = (255, 214, 92)
bg = Background(top=(14, 18, 46), bottom=(30, 34, 90), blobs=[(50, 60, 170), (255, 190, 70), (110, 50, 160)], seed=3233)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Why do shops pay", "for 15 seconds", "of video?"], t, -0.3, 380, 100, (WHITE, ACC), gap=0.06, highlight={"pay", "15", "seconds"})
        phone_reel(sub, t, 0.5, W / 2, 1180, w=300, rot=-3)
        kp = p(t, 1.3, 0.4)
        pill(sub, W / 2 + 250, 900, "$25", F_BLACK, 64, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="🏷️")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Because it saves them…"], t, s1 + 0.1, 290, 80, (WHITE, ACC), gap=0.07, highlight={"saves"})
        checklist(sub, t, s1 + 0.8, ["Learning an editing app", "An hour per video", "Posting nothing at all"], 480, 150, ACC, size=52, x0=140, every=0.9)
        kb = p(t, s1 + 4.0, 0.4)
        pill(sub, W / 2, 1050, "You sell their time back", F_XB, 54, GOLD, INK, alpha=out_cubic(kb), scale=out_back(kb), icon="⏱️")
        draw_text(sub, "Holiday season = more to post", F_SEMI, 42, W / 2, 1175, SOFT, alpha=out_cubic(p(t, s1 + 4.8, 0.4)))
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["47 sec of raw clips…"], t, s2 + 0.1, 270, 80, (WHITE, ACC), gap=0.07, highlight={"47"})
        clips_to_reel(sub, t, s2 + 0.6, 860, merge_at=s2 + 2.8)
        kk = p(t, s2 + 4.0, 0.4)
        pill(sub, W / 2, 1500, "…become 1 clean 13-sec Reel", F_BLACK, 48, GOLD, INK, alpha=out_cubic(kk), scale=out_back(kk), icon="✨")
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Example pricing"], t, s3 + 0.1, 270, 84, (WHITE, ACC), gap=0.07, highlight={"pricing"})
        rows = [("4 × 15-sec Reels ($25 each)", "$100", s3 + 0.9), ("Rush (48 hours)", "$20", s3 + 1.5)]
        quote_card(sub, t, s3 + 0.4, 380, "Pine Cup Café (sample)", rows, "$120", None, ACC)
        kq = p(t, s3 + 3.0, 0.4)
        pill(sub, W / 2, 1010, "On Fiverr: 20% fee → $96", F_BLACK, 52, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="💵")
        draw_text(sub, "Direct client: you keep more", F_XB, 44, W / 2, 1130, WHITE, alpha=out_cubic(p(t, s3 + 3.8, 0.4)))
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 34, W / 2, 1240, SOFT, alpha=out_cubic(p(t, s3 + 4.4, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel3.mp4")
