"""3 photos every shop needs before Black Friday -- sell a holiday 3-shot photo set (phone + window, part 2)."""
from reel_photo import *

ACC = (255, 158, 64)    # amber
GOLD = (255, 214, 92)
MINT = (90, 220, 170)
PINK = (255, 120, 170)
bg = Background(top=(34, 18, 8), bottom=(20, 10, 22), blobs=[(255, 150, 60), (255, 100, 120), (255, 210, 120)], seed=2961)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        # fanned photo set behind the hook
        photo_card(sub, t, 0.0, W / 2 - 250, 470, 230, "hero", rot=10)
        photo_card(sub, t, 0.1, W / 2, 440, 230, "close", rot=0)
        photo_card(sub, t, 0.2, W / 2 + 250, 470, 230, "gift", rot=-10)
        pop_words(sub, ["3 photos every shop", "needs before", "Black Friday"], t, 0.0, 900, 96, (WHITE, ACC), gap=0.07, highlight={"3", "photos", "black", "friday"})
        kp = p(t, 1.4, 0.4)
        pill(sub, W / 2, 1210, "Your phone + a window, part 2", F_XB, 48, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), pad=(40, 22), icon="📸")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Lots of small shops", "have 1 dark photo"], t, s1 + 0.1, 330, 88, (WHITE, PINK), gap=0.08, highlight={"1", "dark", "photo"})
        photo_card(sub, t, s1 + 0.8, W / 2, 760, 420, "dark", tag="Pine Candle  $24", tag_color=(180, 184, 196))
        kx = p(t, s1 + 2.2, 0.35)
        place_emoji(sub, "😕", W / 2 + 270, 600, 130 * out_back(kx), alpha=out_cubic(kx))
        kp = p(t, s1 + 3.2, 0.4)
        pill(sub, W / 2, 1150, "Easy to scroll right past", F_XB, 52, (245, 246, 250), INK, alpha=out_cubic(kp), scale=out_back(kp), icon="👆")
        kq = p(t, s1 + 4.2, 0.4)
        pill(sub, W / 2, 1300, "You shoot the fix for them", F_XB, 52, ACC, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="📱")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["The 3-shot set"], t, s2 + 0.1, 300, 96, (WHITE, ACC), gap=0.08, highlight={"3-shot"})
        shot_row(sub, t, s2 + 0.6, 560, "hero", 1, "Hero", "Whole product, plain white background", GOLD)
        shot_row(sub, t, s2 + 2.2, 860, "close", 2, "Close-up", "Label, texture and size up close", MINT)
        shot_row(sub, t, s2 + 3.8, 1160, "gift", 3, "Gift scene", "Holiday props so it looks giftable", PINK)
        kq = p(t, s2 + 5.6, 0.4)
        draw_text(sub, "Same window light for all 3", F_SEMI, 46, W / 2, 1400, SOFT, alpha=out_cubic(kq))
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Example pricing"], t, s3 + 0.1, 300, 84, (WHITE, GOLD), gap=0.08, highlight={"pricing"})
        k1 = p(t, s3 + 0.6, 0.4)
        pill(sub, W / 2, 460, "5 best sellers x 3 shots", F_XB, 54, (245, 246, 250), INK, alpha=out_cubic(k1), scale=out_back(k1), icon="📸")
        k2 = p(t, s3 + 1.1, 0.4)
        pill(sub, W / 2, 590, "$100 per shop", F_XB, 54, ACC, INK, alpha=out_cubic(k2), scale=out_back(k2), icon="🛍️")
        k3 = p(t, s3 + 1.6, 0.4)
        pill(sub, W / 2, 720, "x 3 shops", F_XB, 54, MINT, INK, alpha=out_cubic(k3), scale=out_back(k3), icon="🏪")
        money_counter(sub, t, s3 + 2.2, 300, 990, GOLD, label="example total")
        kq = p(t, s3 + 4.8, 0.5)
        draw_text(sub, "Example pricing. Results depend on your work.", F_MED, 36, W / 2, 1360, SOFT, alpha=out_cubic(kq))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel1.mp4")
