"""Your first holiday post: 10 minutes, $0 (build a Cyber Monday sample in a free design tool)."""
from reel_insta import *
from reel_portfolio import timer

ACC = (90, 230, 220)    # teal
GOLD = (255, 210, 80)
bg = Background(top=(4, 20, 34), bottom=(10, 46, 72), blobs=[(30, 160, 200), (60, 220, 190), (90, 90, 230)], seed=2913)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, -0.2, 0.3)
        place_emoji(sub, "🎨", W / 2, 450 - 16 * math.sin(t * 6), 180 * out_back(k), alpha=k, rot=6 * math.sin(t * 4))
        pop_words(sub, ["Your first holiday", "post: 10 minutes, $0"], t, -0.3, 770, 98, (WHITE, ACC), gap=0.06, highlight={"10", "minutes,", "$0"})
        kp = p(t, 1.0, 0.4)
        pill(sub, W / 2, 1000, "Free design tool. 5 steps.", F_XB, 52, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="⚡")
        timer(sub, t, 1.4, 2.2, W / 2, 1170, 10, WHITE)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Shops want to see", "a sample first"], t, s1 + 0.1, 340, 88, (WHITE, ACC), gap=0.07, highlight={"sample"})
        checklist(sub, t, s1 + 1.0, ["Free Canva account", "1 product photo", "1 offer + 1 date"], 640, 150, ACC, size=58, x0=170, every=0.8)
        kx = p(t, s1 + 4.0, 0.4)
        pill(sub, W / 2, 1150, "No client needed yet", F_BLACK, 52, GOLD, INK, alpha=out_cubic(kx), scale=out_back(kx), icon="🙌")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Build it in 5 steps"], t, s2 + 0.1, 260, 84, (WHITE, ACC), gap=0.07, highlight={"5", "steps"})
        st = [s2 + 0.7 + i * 1.3 for i in range(5)]
        canva_editor(sub, t, s2 + 0.3, 880, GOLD, st, labels=["1. Dark background", "2. Big 2-word headline", "3. Product photo", "4. One clear offer", "5. Date + where to buy"])
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Now it's your sample"], t, s3 + 0.1, 270, 84, (WHITE, GOLD), gap=0.07, highlight={"sample"})
        feed_post(sub, t, s3 + 0.5, 800, GOLD, w=680)
        draw_text(sub, "Example design. Use the shop's real offer.", F_SEMI, 34, W / 2, 1310, SOFT, alpha=out_cubic(p(t, s3 + 2.0, 0.4)))
        kq = p(t, s3 + 2.8, 0.4)
        pill(sub, W / 2, 1430, "Send it to 3 local shops", F_XB, 48, ACC, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="📩")
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel3.mp4")
