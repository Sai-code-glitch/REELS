"""Check 1 shop's colors tonight (lead check for a brand style guide side gig + DM with free sample)."""
from reel_brand import *

ACC = (190, 140, 255)   # lavender
GOLD = (255, 214, 92)
bg = Background(top=(22, 10, 48), bottom=(48, 20, 92), blobs=[(90, 40, 170), (190, 140, 255), (40, 60, 160)], seed=3221)


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Check 1 shop's", "colors tonight"], t, -0.3, 360, 108, (WHITE, ACC), gap=0.06, highlight={"1", "colors", "tonight"})
        ig_grid(sub, t, 0.4, 1060, w=760, every=0.05)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Fiverr's new data:"], t, s1 + 0.1, 300, 84, (WHITE, ACC), gap=0.07, highlight={"fiverr's"})
        kb = p(t, s1 + 0.8, 0.45)
        pill(sub, W / 2, 470, "Brand style guides", F_BLACK, 68, GOLD, INK, alpha=out_cubic(kb), scale=out_back(kb), icon="🎨")
        draw_text(sub, "are on its top side hustle list", F_XB, 48, W / 2, 590, WHITE, alpha=out_cubic(p(t, s1 + 1.4, 0.4)))
        draw_text(sub, "(Entrepreneur, Nov 2026)", F_SEMI, 36, W / 2, 660, SOFT, alpha=out_cubic(p(t, s1 + 1.8, 0.4)))
        guide_card(sub, t, s1 + 2.4, W / 2, 1110, w=440, rot=-3)
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Open 1 local shop's", "Instagram. Look for:"], t, s2 + 0.1, 290, 76, (WHITE, ACC), gap=0.06, highlight={"instagram."})
        ig_grid(sub, t, s2 + 0.6, 1000, w=760, flags=[("6+ random colors", 300), ("4 different fonts", 520), ("No look that repeats", 740)], flag_at=s2 + 2.0)
        kq = p(t, s2 + 5.0, 0.4)
        pill(sub, W / 2, 1500, "Messy grid = a lead", F_BLACK, 52, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="🎯")
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Send this DM"], t, s3 + 0.1, 270, 90, (WHITE, ACC), gap=0.07, highlight={"dm"})
        msgs = [("me", "Hi! Love your pastries. I made a free 1-page brand guide so your posts match. Want it?", s3 + 0.8, "typed"),
                ("them", "Oh nice, send it over!", s3 + 3.6, None)]
        phone_chat(sub, t, s3 + 0.4, W / 2, 380, msgs, header="Maple & Co.", sub_label="Sample bakery", w=820, h=760)
        kq = p(t, s3 + 4.6, 0.4)
        pill(sub, W / 2, 1260, "Free sample first. Then quote.", F_XB, 48, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="🤝")
        draw_text(sub, "Shop and chat are fictional", F_SEMI, 34, W / 2, 1380, SOFT, alpha=out_cubic(p(t, s3 + 5.2, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel1.mp4")
