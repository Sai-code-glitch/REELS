"""Your portfolio: 1 free page, 15 minutes -- free site builder, 4 blocks, link it in 3 places."""
from reel_portfolio import *

ACC = (130, 235, 110)   # green
GOLD = (255, 205, 80)
SKY = (120, 200, 255)
RED = (255, 90, 100)
bg = Background(top=(8, 26, 14), bottom=(18, 22, 8), blobs=[(60, 200, 90), (230, 190, 50), (40, 150, 120)], seed=2973)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        k = p(t, 0.0, 0.3)
        place_emoji(sub, "🌐", W / 2, 470 - 16 * math.sin(t * 5), 200 * out_back(k), alpha=k, rot=8 * math.sin(t * 3))
        pop_words(sub, ["Your portfolio:", "1 free page,", "15 minutes"], t, 0.0, 860, 106, (WHITE, ACC), gap=0.07, highlight={"1", "free", "15", "minutes"})
        kp = p(t, 1.5, 0.4)
        pill(sub, W / 2, 1150, "$0 tools only", F_XB, 50, GOLD, INK, alpha=out_cubic(kp), scale=out_back(kp), icon="💸")
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["You don't need a", "paid website yet"], t, s1 + 0.1, 300, 86, (WHITE, GOLD), gap=0.08, highlight={"paid", "yet"})
        kt = p(t, s1 + 0.8, 0.4)
        pill(sub, W / 2, 560, "$20/month site", F_BLACK, 70, (255, 230, 232), (200, 30, 50), alpha=out_cubic(kt), scale=out_back(kt), pad=(50, 26), icon="🧾")
        strike(sub, t, s1 + 1.6, 230, W - 230, 565, RED, width=14)
        pop_words(sub, ["Free options:"], t, s1 + 2.2, 760, 64, (WHITE, ACC), gap=0.06, path=F_XB)
        for i, (lab, ic) in enumerate([("Canva website", "🎨"), ("Google Sites", "📄"), ("Notion page", "🗒️")]):
            kk = p(t, s1 + 2.7 + i * 0.5, 0.4)
            pill(sub, W / 2, 900 + i * 140, lab, F_XB, 54, WHITE, INK, alpha=out_cubic(kk), scale=out_back(kk), pad=(44, 22), icon=ic)
        kq = p(t, s1 + 4.6, 0.4)
        draw_text(sub, "Free plans, with their own web address", F_MED, 38, W / 2, 1340, SOFT, alpha=out_cubic(kq))
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Add just 4 blocks"], t, s2 + 0.1, 270, 84, (WHITE, ACC), gap=0.08, highlight={"4", "blocks"})
        timer(sub, t, s2 + 0.4, 6.5, W / 2, 390, 15, GOLD)
        site_builder(sub, t, s2 + 0.5, 980, ACC, [s2 + 1.2, s2 + 2.6, s2 + 4.0, s2 + 5.2], h=1000)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Put the link in", "3 places"], t, s3 + 0.1, 300, 92, (WHITE, GOLD), gap=0.08, highlight={"3", "places"})
        checklist(sub, t, s3 + 0.9, ["Your Instagram bio", "Every pitch DM", "Your email signature"], 560, 140, ACC, size=56, x0=170, every=0.7)
        notification(sub, t, s3 + 3.3, 1100, "Your pitch DM", "Samples: samjones.my.canva.site", icon="🔗")
        kq = p(t, s3 + 4.6, 0.5)
        draw_text(sub, "Example pricing on page. Results depend on your work.", F_MED, 34, W / 2, 1350, SOFT, alpha=out_cubic(kq))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel3.mp4")
