"""Why pay $6 for tags you print at home? (reasons, digital bundle listing, fee math)."""
from reel_tags import *

ACC = (255, 196, 90)    # gold-amber
GOLD = (255, 214, 92)
bg = Background(top=(6, 22, 40), bottom=(10, 52, 72), blobs=[(20, 90, 120), (255, 190, 90), (60, 50, 150)], seed=3203)
COW = THEMES["coworker"]


def scene(layer, t):
    progress_bar(layer, t, SCENES, 30, ACC)
    s0, e0 = SCENES[0]
    if t < e0:
        sub = new_layer()
        pop_words(sub, ["Why pay $6 for", "tags you print", "at home?"], t, -0.3, 400, 104, (WHITE, ACC), gap=0.06, highlight={"$6", "print"})
        big_tag(sub, t, 0.8, W / 2 - 150, 1170, COW, w=330, rot=-8)
        big_tag(sub, t, 1.1, W / 2 + 170, 1210, THEMES["plain"], w=330, rot=7)
        faded(layer, sub, t, s0, e0)

    s1, e1 = SCENES[1]
    if s1 <= t < e1:
        sub = new_layer()
        pop_words(sub, ["Because buyers want…"], t, s1 + 0.1, 290, 84, (WHITE, ACC), gap=0.07, highlight={"buyers"})
        checklist(sub, t, s1 + 0.8, ["Tags that match their wrap", "A cute To/From, done for them", "Tags tonight, not in a week"], 470, 150, ACC, size=48, x0=130, every=0.9)
        kb = p(t, s1 + 4.0, 0.4)
        pill(sub, W / 2, 1050, "They buy convenience", F_XB, 52, GOLD, INK, alpha=out_cubic(kb), scale=out_back(kb), icon="⏱️")
        draw_text(sub, "You sell the same file again and again", F_SEMI, 40, W / 2, 1175, SOFT, alpha=out_cubic(p(t, s1 + 4.8, 0.4)))
        faded(layer, sub, t, s1, e1)

    s2, e2 = SCENES[2]
    if s2 <= t < e2:
        sub = new_layer()
        pop_words(sub, ["Sell a 3-sheet bundle"], t, s2 + 0.1, 270, 84, (WHITE, ACC), gap=0.07, highlight={"3-sheet", "bundle"})
        listing_form(sub, t, s2 + 0.5, 400, ACC, [
            ("Type", "Digital files", "💾"),
            ("Files", "3 sheets · 24 tags", "📄"),
            ("Photos", "5 mockups", "🖼️"),
            ("Price (example)", "$6.00", "💵"),
        ], every=0.8)
        kq = p(t, s2 + 4.4, 0.4)
        pill(sub, W / 2, 1100, "Teacher + neighbor + coworker", F_XB, 46, GOLD, INK, alpha=out_cubic(kq), scale=out_back(kq), icon="🎁")
        draw_text(sub, "One download covers their whole list", F_SEMI, 40, W / 2, 1225, SOFT, alpha=out_cubic(p(t, s2 + 5.2, 0.4)))
        faded(layer, sub, t, s2, e2)

    s3, e3 = SCENES[3]
    if s3 <= t < e3:
        sub = new_layer()
        pop_words(sub, ["Fee math on $6", "(example)"], t, s3 + 0.1, 280, 84, (WHITE, ACC), gap=0.07, highlight={"$6"})
        formula_rows(sub, t, s3 + 0.6, 440, [
            ("🏷️", "Listing fee", "−$0.20"),
            ("🧾", "Transaction 6.5%", "−$0.39"),
            ("💳", "Processing 3% + $0.25", "−$0.43"),
        ], ACC, every=0.6, row=130)
        dollar_counter(sub, t, s3 + 2.6, 4.98, 960, ACC, "you keep per sale", size=190)
        draw_text(sub, "Etsy US rates, 2026. Check yours.", F_SEMI, 34, W / 2, 1210, SOFT, alpha=out_cubic(p(t, s3 + 4.4, 0.4)))
        draw_text(sub, "Example pricing. Results depend on your work.", F_SEMI, 34, W / 2, 1265, SOFT, alpha=out_cubic(p(t, s3 + 4.8, 0.4)))
        faded(layer, sub, t, s3, e3)

    cta(layer, t, ACC, GOLD)
    watermark(layer)


if __name__ == "__main__":
    main(scene, bg, "reel3.mp4")
