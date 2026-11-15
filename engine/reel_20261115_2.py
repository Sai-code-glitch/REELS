"""Your first Fiverr gig: 20 minutes, $0 (4 boxes: title, 5 tags, gig image, packages)."""
from reel_fiverr import *

ACC = (190, 140, 255)   # lavender
GOLD = (255, 214, 92)
bg = Background(top=(22, 10, 44), bottom=(50, 22, 96), blobs=[(110, 50, 200), (190, 140, 255), (40, 70, 170)], seed=3192)
TITLE = "design a holiday flyer for your small business"


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Your first", "Fiverr gig:", "20 minutes, $0"], t, -0.3, 420, 108, (WHITE, ACC), gap=0.06, highlight={"fiverr", "20", "$0"})
        timer(sub, t, 0.6, 2.8, W / 2, 760, 20, GOLD)
        gig_card(sub, t, 1.1, W / 2, 830, ACC, "I will " + TITLE, "$15", w=590, rot=3)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Fiverr only asks", "for 4 things"], t, s1 + 0.1, 290, 86, (WHITE, ACC), gap=0.07, highlight={"4"})
        formula_rows(sub, t, s1 + 0.8, 450, [
            ("✍️", "Gig title", "\"I will...\""),
            ("🏷️", "Search tags", "up to 5"),
            ("🖼️", "Gig image", "1280×769"),
            ("📦", "Packages", "up to 3"),
        ], FV, every=0.7, row=140)
        kq = p(t, s1 + 4.2, 0.4)
        pill(sub, W / 2, 1100, "Free to sign up as a seller", F_XB, 46, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="🆓")
        draw_text(sub, "Fiverr keeps 20% when you sell.", F_SEMI, 38, W / 2, 1220, SOFT, alpha=out_cubic(p(t, s1 + 4.9, 0.4)))
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Title: what + who for"], t, s2 + 0.1, 280, 80, (WHITE, ACC), gap=0.07, highlight={"what", "who"})
        gig_title(sub, t, s2 + 0.5, 390, TITLE, 2.0)
        draw_text(sub, "+ 5 tags buyers would type", F_XB, 46, W / 2, 860, WHITE, alpha=out_cubic(p(t, s2 + 3.0, 0.4)))
        tag_chips(sub, t, s2 + 3.3, 930, ["flyer design", "holiday flyer", "canva flyer", "small business", "bakery flyer"], ACC, every=0.35, size=40)
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Gig image: show", "a real sample"], t, s3 + 0.1, 290, 84, (WHITE, ACC), gap=0.07, highlight={"sample"})
        k = p(t, s3 + 0.5, 0.4)
        if k > 0:
            st = [s3 + 0.7, s3 + 1.4, s3 + 2.1, s3 + 2.8]
            im = thumb(880, 529, ACC, steps=st, t=t)
            fr = Image.new("RGBA", (900, 549), (255, 255, 255, 255))
            fr.alpha_composite(im, (10, 10))
            sub.alpha_composite(with_alpha(fr, out_cubic(k)), (90, int(450 + 50 * (1 - out_cubic(k)))))
        labs = [("1 · Dark background", s3 + 0.7), ("2 · Big headline", s3 + 1.4), ("3 · Your sample flyer", s3 + 2.1), ("4 · Delivery badge", s3 + 2.8)]
        for i, (lb, at) in enumerate(labs):
            draw_text(sub, lb, F_XB, 42, 150, 1070 + i * 70, WHITE, alpha=out_cubic(p(t, at, 0.4)), anchor="lm")
        draw_text(sub, "Make the sample in free Canva first", F_SEMI, 36, W / 2, 1400, SOFT, alpha=out_cubic(p(t, s3 + 4.2, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel2.mp4")
