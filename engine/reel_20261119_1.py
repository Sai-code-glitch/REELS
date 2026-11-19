"""Check 1 shop's Reels tab tonight (lead check for a short-video editing side gig + DM offering a free sample)."""
from reel_edit import *

ACC = (80, 220, 200)    # teal
GOLD = (255, 214, 92)
bg = Background(top=(6, 30, 36), bottom=(10, 60, 70), blobs=[(20, 120, 130), (80, 220, 200), (30, 70, 140)], seed=3231)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Check 1 shop's", "Reels tab tonight"], t, -0.3, 360, 104, (WHITE, ACC), gap=0.06, highlight={"1", "reels", "tonight"})
        reels_tab(sub, t, 0.3, 640, flag_at=1.6, w=820, h=900)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Fiverr's new list:"], t, s1 + 0.1, 300, 84, (WHITE, ACC), gap=0.07, highlight={"fiverr's"})
        kb = p(t, s1 + 0.8, 0.45)
        pill(sub, W / 2, 470, "Video editing", F_BLACK, 70, GOLD, INK, alpha=out_cubic(kb), scale=out_back(kb), icon="🎬")
        draw_text(sub, "is a top side hustle skill", F_XB, 50, W / 2, 590, WHITE, alpha=out_cubic(p(t, s1 + 1.4, 0.4)))
        draw_text(sub, "(Entrepreneur, Nov 13 2026)", F_SEMI, 36, W / 2, 660, SOFT, alpha=out_cubic(p(t, s1 + 1.8, 0.4)))
        phone_reel(sub, t, s1 + 2.4, W / 2, 1120, w=300, rot=-3)
        draw_text(sub, "Shops have clips. No time to edit.", F_XB, 44, W / 2, 1520, WHITE, alpha=out_cubic(p(t, s1 + 3.4, 0.4)))
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Open 1 local shop.", "Tap the Reels tab."], t, s2 + 0.1, 290, 76, (WHITE, ACC), gap=0.06, highlight={"reels"})
        reels_tab(sub, t, s2 + 0.6, 450, flag_at=s2 + 3.0)
        kq = p(t, s2 + 4.6, 0.4)
        pill(sub, W / 2, 1480, "Photos only? Pitch a Reel.", F_BLACK, 50, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="🎯")
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Send this DM"], t, s3 + 0.1, 270, 90, (WHITE, ACC), gap=0.07, highlight={"dm"})
        msgs = [("me", "Hi! Love your café. Send me 4 short phone clips and I'll edit a free 15-second Reel. Want to try?", s3 + 0.8, "typed"),
                ("them", "Sure! I'll film the drinks tonight", s3 + 3.6, None)]
        phone_chat(sub, t, s3 + 0.4, W / 2, 380, msgs, header="Pine Cup Café", sub_label="Sample café", w=820, h=780)
        kq = p(t, s3 + 4.6, 0.4)
        pill(sub, W / 2, 1280, "Free sample first. Then quote.", F_XB, 48, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="🤝")
        draw_text(sub, "Café and chat are fictional", F_SEMI, 34, W / 2, 1400, SOFT, alpha=out_cubic(p(t, s3 + 5.2, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel1.mp4")
