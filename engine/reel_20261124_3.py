"""Why do shops pay to fix 1 link? (every post says 'link in bio' -> old link = dead end -> 4-button page -> example math)."""
from reel_linkbio import *

ACC = (120, 230, 140)
GOLD = (255, 220, 110)
bg = Background(top=(10, 22, 44), bottom=(20, 70, 60), blobs=[(30, 110, 90), (120, 230, 140), (20, 40, 90)], seed=1243)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Why do shops pay", "to fix 1 link?"], t, -0.3, 370, 104, (WHITE, ACC), gap=0.07, highlight={"pay", "1", "link?"})
        bio_profile(sub, t, 0.5, 640, ACC, link="pineandwick.com/old-sale", tap_at=2.6)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Every post says", "\"link in bio\""], t, s1 + 0.1, 290, 88, (WHITE, ACC), gap=0.07, highlight={"\"link", "bio\""})
        caps = [("🎁", "Gift sets are live! Link in bio"), ("🧼", "New scents → link in bio"), ("📦", "Shipping dates → link in bio")]
        for i, (em, cap) in enumerate(caps):
            kk = p(t, s1 + 0.9 + i * 0.4, 0.4)
            pill(sub, W / 2, 560 + i * 130, cap, F_XB, 42, WHITE, INK, alpha=out_cubic(kk), scale=out_back(kk), icon=em)
        draw_text(sub, "That 1 link is the only door", F_XB, 52, W / 2, 1000, WHITE, alpha=out_cubic(p(t, s1 + 2.8, 0.4)))
        draw_text(sub, "to their shop.", F_XB, 52, W / 2, 1068, WHITE, alpha=out_cubic(p(t, s1 + 2.8, 0.4)))
        kb = p(t, s1 + 4.2, 0.4)
        pill(sub, W / 2, 1240, "Old link = shoppers leave", F_BLACK, 48, (255, 120, 110), INK, alpha=out_cubic(kb), scale=out_back(kb), icon="🚪")
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Owners are busy packing.", "You build the page."], t, s2 + 0.1, 260, 74, (WHITE, ACC), gap=0.07, highlight={"packing.", "you", "build"})
        link_page(sub, t, s2 + 0.6, 400, ACC, [s2 + 1.4, s2 + 2.4, s2 + 3.4, s2 + 4.4], tap_at=s2 + 6.0)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Example math"], t, s3 + 0.1, 280, 88, (WHITE, ACC), gap=0.07, highlight={"math"})
        draw_text(sub, "4 shops × $30 link page", F_XB, 56, W / 2, 470, WHITE, alpha=out_cubic(p(t, s3 + 0.6, 0.4)))
        money_counter(sub, t, s3 + 1.2, 120, 760, GOLD, label="example total")
        draw_text(sub, "~10 minutes each once you practice", F_SEMI, 42, W / 2, 1080, SOFT, alpha=out_cubic(p(t, s3 + 3.6, 0.4)))
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 34, W / 2, 1300, SOFT, alpha=out_cubic(p(t, s3 + 4.4, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel3.mp4")
